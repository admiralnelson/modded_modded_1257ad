from header import *

#script_game_get_item_buy_price_factor:
	# This script is called from the game engine for calculating the buying price of any item.
	# INPUT:
	# param1: item_kind_id
	# OUTPUT:
	# trigger_result and reg0 = price_factor
game_get_item_buy_price_factor= (
	"game_get_item_buy_price_factor",
		[
			(store_script_param_1, ":item_kind_id"),
			(assign, ":price_factor", 100),
			
			(call_script, "script_get_trade_penalty", ":item_kind_id"),
			(assign, ":trade_penalty", reg0),
			
			(try_begin),
				(is_between, "$g_encountered_party", centers_begin, centers_end),
				(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
				(store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
				(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
				(party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
				
				#new
				#(try_begin),
				#	(is_between, "$g_encountered_party", villages_begin, villages_end),
				#	(party_get_slot, ":market_town", "$g_encountered_party", slot_village_market_town),
				#	(party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
				#	(val_max, ":price_factor", ":price_in_market_town"),
				#(try_end),
				
				#For villages, the good will be sold no cheaper than in the market town
				#This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers
				
				(val_mul, ":price_factor", 100), #normalize price factor to range 0..100
				(val_div, ":price_factor", average_price_factor),
			(try_end),
			
			(store_add, ":penalty_factor", 100, ":trade_penalty"),
			
			(val_mul, ":price_factor", ":penalty_factor"),
			(val_div, ":price_factor", 100),
			
			(assign, reg0, ":price_factor"),
			(set_trigger_result, reg0),
	])

#script_game_get_item_sell_price_factor:
	# This script is called from the game engine for calculating the selling price of any item.
	# INPUT:
	# param1: item_kind_id
	# OUTPUT:
	# trigger_result and reg0 = price_factor
game_get_item_sell_price_factor =	(
	"game_get_item_sell_price_factor",
		[
			(store_script_param_1, ":item_kind_id"),
			(assign, ":price_factor", 100),
			
			(call_script, "script_get_trade_penalty", ":item_kind_id"),
			(assign, ":trade_penalty", reg0),
			
			(try_begin),
				(is_between, "$g_encountered_party", centers_begin, centers_end),
				(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
				(store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
				(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
				(party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
				(val_mul, ":price_factor", 100),#normalize price factor to range 0..100
				(val_div, ":price_factor", average_price_factor),
			(else_try),
				#increase trade penalty while selling weapons, armor, and horses
				#(val_mul, ":trade_penalty", 4),
				(val_mul, ":trade_penalty", 12), #tom - rafi set 16 # rafi
			(try_end),
			
			
			(store_add, ":penalty_divisor", 100, ":trade_penalty"),
			
			(val_mul, ":price_factor", 100),
			(val_div, ":price_factor", ":penalty_divisor"),
			
			(assign, reg0, ":price_factor"),
			(set_trigger_result, reg0),
	])

# script_get_trade_penalty
	# Trade penalty if player has bad relation with the town or merchant(?)
	# Input:
	# param1: troop_id,
	# Output: reg0
	
get_trade_penalty = (
	"get_trade_penalty",
		[
			(store_script_param_1, ":item_kind_id"),
			(assign, ":penalty",0),
			
			(party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
			(try_begin),
				(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
				(assign, ":penalty", 13), #reduced slightly 20-15-12
				(store_mul, ":skill_bonus", ":trade_skill", 1),
				(val_sub, ":penalty", ":skill_bonus"),
				(val_max, ":penalty", 3),
			(else_try),
				(assign, ":penalty",100),
				(store_mul, ":skill_bonus", ":trade_skill", 5),
				(val_sub, ":penalty", ":skill_bonus"),
			(try_end),
			
			(assign, ":penalty_multiplier", 1000),
			##       # Apply penalty if player is hostile to merchants faction
			##      (store_relation, ":merchants_reln", "fac_merchants", "fac_player_supporters_faction"),
			##      (try_begin),
			##        (lt, ":merchants_reln", 0),
			##        (store_sub, ":merchants_reln_dif", 10, ":merchants_reln"),
			##        (store_mul, ":merchants_relation_penalty", ":merchants_reln_dif", 20),
			##        (val_add, ":penalty_multiplier", ":merchants_relation_penalty"),
			##      (try_end),
			
			# Apply penalty if player is on bad terms with the town
			(try_begin),
				(is_between, "$g_encountered_party", centers_begin, centers_end),
				(party_get_slot, ":center_relation", "$g_encountered_party", slot_center_player_relation),
				(store_mul, ":center_relation_penalty", ":center_relation", -3),
				(val_add, ":penalty_multiplier", ":center_relation_penalty"),
				(try_begin),
					(lt, ":center_relation", 0),
					(store_sub, ":center_penalty_multiplier", 100, ":center_relation"),
					(val_mul, ":penalty_multiplier", ":center_penalty_multiplier"),
					(val_div, ":penalty_multiplier", 100),
				(try_end),
			(try_end),
			
			# Apply penalty if player is on bad terms with the merchant (not currently used)
			(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
			(assign, ":troop_reln", reg0),
			#(troop_get_slot, ":troop_reln", "$g_talk_troop", slot_troop_player_relation),
			(try_begin),
				(lt, ":troop_reln", 0),
				(store_sub, ":troop_reln_dif", 0, ":troop_reln"),
				(store_mul, ":troop_relation_penalty", ":troop_reln_dif", 20),
				(val_add, ":penalty_multiplier", ":troop_relation_penalty"),
			(try_end),
			
			
			(try_begin),
				(is_between, "$g_encountered_party", villages_begin, villages_end),
				(val_mul, ":penalty", 5), #1.25x trade penalty in villages.
				(val_div, ":penalty", 4),
			(try_end),
			
			#(try_begin),
			#(is_between, "$g_encountered_party", centers_begin, centers_end),
			##Double trade penalty if no local production or consumption
			#(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
			#(call_script, "script_center_get_production", "$g_encountered_party", ":item_kind_id"),
			#(eq, reg0, 0),
			#(call_script, "script_center_get_consumption", "$g_encountered_party", ":item_kind_id"),
			#(eq, reg0, 0),
			#(val_mul, ":penalty", 2),
			#(try_end),
			
			(val_mul, ":penalty",  ":penalty_multiplier"),
			(val_div, ":penalty", 1000),
			(val_max, ":penalty", 1),
			(assign, reg0, ":penalty"),
	])


#script_center_get_production
		# WARNING: no longer behaves like native, modified by 1257AD devs
		# INPUT: arg1 = town center, arg2 = goods
		# OUTPUT: reg0 = prosperity, reg1 = base_production_modded_by_raw_materials, reg2 = base_production
center_get_production	= (
	"center_get_production",
			[
				#Actually, this could be reset somewhat to yield supply and demand as raw numbers
				#Demand could be set values for rural and urban
				#Supply could be based on capital goods -- head of cattle, head of sheep, fish ponds, fishing fleets, acres of grain fields, olive orchards, olive presses, wine presses, mills, smithies, salt pans, potters' kilns, etc
				#Prosperity would increase both demand and supply
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":cur_good"),
				
				(assign, ":base_production", 0),
				
				#Grain products
				(try_begin),
					(eq, ":cur_good", "itm_bread"), #Demand = 3000 across Calradia
					(party_get_slot, ":base_production", ":center_no", slot_center_mills),
					(val_mul, ":base_production", 20), #one mills per village, five mills per town = 160 mills
				(else_try),
					(eq, ":cur_good", "itm_grain"), #Demand =  3200+, 1600 to mills, 1500 on its own, extra to breweries
					(party_get_slot, ":base_production", ":center_no", slot_center_acres_grain),
					(val_div, ":base_production", 125), #10000 acres is the average across Calradia, extra in Swadia, less in snows and steppes, a bit from towns
				(else_try),
					(eq, ":cur_good", "itm_ale"), #
					(party_get_slot, ":base_production", ":center_no", slot_center_breweries),
					(val_mul, ":base_production", 25),
					
				(else_try),
					(eq, ":cur_good", "itm_smoked_fish"), #Demand = 20
					(party_get_slot, ":base_production", ":center_no", slot_center_fishing_fleet),
					(val_mul, ":base_production", 4), #was originally 5
				(else_try),
					(eq, ":cur_good", "itm_salt"),
					(party_get_slot, ":base_production", ":center_no", slot_center_salt_pans),
					(val_mul, ":base_production", 35),
					
					#Cattle products
				(else_try),
					(eq, ":cur_good", "itm_cattle_meat"), #Demand = 5
					(party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
					(val_div, ":base_production", 4), #was 9
				(else_try),
					(eq, ":cur_good", "itm_dried_meat"), #Demand = 15
					(party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
					(val_div, ":base_production", 2), #was 3
				(else_try),
			(eq, ":cur_good", "itm_cheese"), 	 #Demand = 10
			(party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
			(party_get_slot, ":sheep_addition", ":center_no", slot_center_head_sheep),
			(val_div, ":sheep_addition", 2),
			(val_add, ":base_production", ":sheep_addition"),
			(party_get_slot, ":gardens", ":center_no", slot_center_household_gardens),
			(val_mul, ":base_production", ":gardens"),
			(val_div, ":base_production", 10), 
		(else_try),
			(eq, ":cur_good", "itm_butter"), 	 #Demand = 2
			(party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
			(party_get_slot, ":gardens", ":center_no", slot_center_household_gardens),
			(val_mul, ":base_production", ":gardens"),
			(val_div, ":base_production", 15),
				(else_try),
					(eq, ":cur_good", "itm_raw_leather"), 	 #Demand = ??
					(party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
					(val_div, ":base_production", 6),
					(party_get_slot, ":sheep_addition", ":center_no", slot_center_head_sheep),
					(val_div, ":sheep_addition", 12),
					(val_add, ":base_production", ":sheep_addition"),
					
				(else_try),
					(eq, ":cur_good", "itm_leatherwork"), 	 #Demand = ??
					(party_get_slot, ":base_production", ":center_no", slot_center_tanneries),
					(val_mul, ":base_production", 20),
					
				(else_try),
					(eq, ":cur_good", "itm_honey"), 	 #Demand = 5
					(party_get_slot, ":base_production", ":center_no", slot_center_apiaries),
					(val_mul, ":base_production", 6),
				(else_try),
					(eq, ":cur_good", "itm_cabbages"), 	 #Demand = 7
					(party_get_slot, ":base_production", ":center_no", slot_center_household_gardens),
					(val_mul, ":base_production", 10),
				(else_try),
					(eq, ":cur_good", "itm_apples"), 	 #Demand = 7
					(party_get_slot, ":base_production", ":center_no", slot_center_household_gardens),
					(val_mul, ":base_production", 10),
					
					#Sheep products
				(else_try),
					(eq, ":cur_good", "itm_sausages"), 	 #Demand = 5
					(party_get_slot, ":base_production", ":center_no", slot_center_head_sheep), #average of 90 sheep
					(val_div, ":base_production", 15),
				(else_try),
					(eq, ":cur_good", "itm_wool"), 	 #(Demand = 0, but 15 averaged out perhaps)
					(party_get_slot, ":base_production", ":center_no", slot_center_head_sheep), #average of 90 sheep
					(val_div, ":base_production", 5),
				(else_try),
					(eq, ":cur_good", "itm_wool_cloth"), 	 #(Demand = 1500 across Calradia)
					(party_get_slot, ":base_production", ":center_no", slot_center_wool_looms),
					(val_mul, ":base_production", 5), #300 across Calradia
					
				(else_try),
					(this_or_next|eq, ":cur_good", "itm_pork"),
					(eq, ":cur_good", "itm_chicken"),
					(try_begin),
						(is_between, ":center_no", villages_begin, villages_end),
						(assign, ":base_production", 30),
					(else_try),
						(assign, ":base_production", 0),
					(try_end),
					
				(else_try),
					(eq, ":cur_good", "itm_iron"), 	 #Demand = 5, one supplies three smithies
					(party_get_slot, ":base_production", ":center_no", slot_center_iron_deposits),
					(val_mul, ":base_production", 10),
				(else_try),
					(eq, ":cur_good", "itm_tools"), 	 #Demand = 560 across Calradia
					(party_get_slot, ":base_production", ":center_no", slot_center_smithies),
					(val_mul, ":base_production", 3),
					
					#Other artisanal goods
				(else_try),
					(eq, ":cur_good", "itm_pottery"), #560 is total demand
					(party_get_slot, ":base_production", ":center_no", slot_center_pottery_kilns),
					(val_mul, ":base_production", 5),
					
				(else_try),
					(eq, ":cur_good", "itm_raw_grapes"),
					(party_get_slot, ":base_production", ":center_no", slot_center_acres_vineyard),
					(val_div, ":base_production", 100),
				(else_try),
					(eq, ":cur_good", "itm_wine"),
					(party_get_slot, ":base_production", ":center_no", slot_center_wine_presses),
					(val_mul, ":base_production", 25),
				(else_try),
					(eq, ":cur_good", "itm_raw_olives"),
					(party_get_slot, ":base_production", ":center_no", slot_center_acres_olives),
					(val_div, ":base_production", 150),
				(else_try),
					(eq, ":cur_good", "itm_oil"),
					(party_get_slot, ":base_production", ":center_no", slot_center_olive_presses),
					(val_mul, ":base_production", 12),
					
					#Flax and linen
				(else_try),
					(eq, ":cur_good", "itm_linen"),
					(party_get_slot, ":base_production", ":center_no", slot_center_linen_looms),
					(val_mul, ":base_production", 5),
				(else_try),
					(eq, ":cur_good", "itm_raw_flax"),
					(party_get_slot, ":base_production", ":center_no", slot_center_acres_flax),
					(val_div, ":base_production", 80),
				(else_try),
					(eq, ":cur_good", "itm_velvet"),
					(party_get_slot, ":base_production", ":center_no", slot_center_silk_looms),
					(val_mul, ":base_production", 5),
				(else_try),
					(eq, ":cur_good", "itm_raw_silk"),
					(party_get_slot, ":base_production", ":center_no", slot_center_silk_farms),
					(val_div, ":base_production", 20),
				(else_try),
					(eq, ":cur_good", "itm_raw_dyes"),
					(party_get_slot, ":base_production", ":center_no", slot_center_kirmiz_farms),
					(val_div, ":base_production", 20),
				(else_try),
					(eq, ":cur_good", "itm_raw_date_fruit"),
					(party_get_slot, ":base_production", ":center_no", slot_center_acres_dates),
					(val_div, ":base_production", 120),
				(else_try),
					(eq, ":cur_good", "itm_furs"), 	 #Demand = 90 across Calradia
					(party_get_slot, ":base_production", ":center_no", slot_center_fur_traps),
					(val_mul, ":base_production", 25),
				(else_try),
					(eq, ":cur_good", "itm_spice"),
					(try_begin),
						(eq, ":center_no", "p_town_2_2"), #Tulga
						(assign, ":base_production", 100),
					(else_try),
						(eq, ":center_no", "p_town_4_1"), #Ichamur
						(assign, ":base_production", 50),
					(else_try),
						(eq, ":center_no", "p_town_4_2"), #Shariz
						(assign, ":base_production", 50),
					(else_try),
						(eq, ":center_no", "p_town_7_2"), #Bariyye
						(assign, ":base_production", 50),
					(try_end),
				(try_end),
				
				#Modify production by other goods
				(assign, ":modified_production", ":base_production"),
				(try_begin),
					(eq, ":cur_good", "itm_bread"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_grain", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_ale"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_grain", ":base_production", 2),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_dried_meat"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_salt", ":base_production", 2),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_smoked_fish"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_salt", ":base_production", 2),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_tools"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_iron", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_wool_cloth"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_wool", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_wine"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_grapes", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_oil"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_olives", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_velvet"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_silk", ":base_production", 1),
					(assign, ":initially_modified_production", reg0),
					
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_dyes", ":initially_modified_production", 2),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_leatherwork"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_leather", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(else_try),
					(eq, ":cur_good", "itm_linen"),
					(call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_flax", ":base_production", 1),
					(assign, ":modified_production", reg0),
				(try_end),
				
				
				(assign, ":base_production_modded_by_raw_materials", ":modified_production"), #this is just logged for the report screen
				
				#Increase both positive and negative production by the center's prosperity
				#Richer towns have more people and consume more, but also produce more
				(try_begin),
					(party_get_slot, ":prosperity_plus_75", ":center_no", slot_town_prosperity),
					(val_add, ":prosperity_plus_75", 75),
					(val_mul, ":modified_production", ":prosperity_plus_75"),
					(val_div, ":modified_production", 125),
				(try_end),
				
				(try_begin),
					(this_or_next|party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
					(party_slot_eq, ":center_no", slot_village_state, svs_looted),
					(assign, ":modified_production", 0),
				(try_end),
				
				(assign, reg0, ":modified_production"), #modded by prosperity
				(assign, reg1, ":base_production_modded_by_raw_materials"),
				(assign, reg2, ":base_production"),
				
		])
		
		# script_center_get_consumption
		# economy stuff I guess
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = town center, arg2 = current good
		# OUTPUT:  reg0 = modified consumption, reg1 = raw material consumption, reg2 = consumer consumption
center_get_consumption	= (
	"center_get_consumption",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":cur_good"),
				
				(assign, ":consumer_consumption", 0),
				
				# rafi
				(store_faction_of_party, ":fac", ":center_no"),
				(call_script, "script_raf_aor_faction_to_region", ":fac"),
				# end rafi
				
				(try_begin),
					# rafi
					(this_or_next | eq, ":fac", "fac_kingdom_23"),
					(this_or_next | eq, reg0, region_andalusian),
					(this_or_next | eq, reg0, region_north_african),
					(eq, reg0, region_mamluk),
					(item_slot_ge, ":cur_good", slot_item_desert_demand, 0), #Otherwise use rural or urban
					(item_get_slot, ":consumer_consumption", ":cur_good", slot_item_desert_demand),
					# end rafi
					# (this_or_next|is_between, ":center_no", "p_town_4_2", "p_castle_1"),
					# (ge, ":center_no", "p_village_91"),
					# (item_slot_ge, ":cur_good", slot_item_desert_demand, 0), #Otherwise use rural or urban
					# (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_desert_demand),
				(else_try),
					(is_between, ":center_no", villages_begin, villages_end),
					(item_get_slot, ":consumer_consumption", ":cur_good", slot_item_rural_demand),
				(else_try),
					(is_between, ":center_no", towns_begin, towns_end),
					(item_get_slot, ":consumer_consumption", ":cur_good", slot_item_urban_demand),
				(try_end),
				
				
				(assign, ":raw_material_consumption", 0),
				(try_begin),
					(eq, ":cur_good", "itm_grain"),
					(party_get_slot, ":grain_for_bread", ":center_no", slot_center_mills),
					(val_mul, ":grain_for_bread", 20),
					
					(party_get_slot, ":grain_for_ale", ":center_no", slot_center_breweries),
					(val_mul, ":grain_for_ale", 5),
					
					(store_add, ":raw_material_consumption", ":grain_for_bread", ":grain_for_ale"),
					
				(else_try),
					(eq, ":cur_good", "itm_iron"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_smithies),
					(val_mul, ":raw_material_consumption", 3),
					
				(else_try),
					(eq, ":cur_good", "itm_wool"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_wool_looms),
					(val_mul, ":raw_material_consumption", 5),
					
				(else_try),
					(eq, ":cur_good", "itm_raw_flax"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_linen_looms),
					(val_mul, ":raw_material_consumption", 5),
					
				(else_try),
					(eq, ":cur_good", "itm_raw_leather"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_tanneries),
					(val_mul, ":raw_material_consumption", 20),
					
				(else_try),
					(eq, ":cur_good", "itm_raw_grapes"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_wine_presses),
					(val_mul, ":raw_material_consumption", 30),
					
				(else_try),
					(eq, ":cur_good", "itm_raw_olives"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_olive_presses),
					(val_mul, ":raw_material_consumption", 12),
					
					
				(else_try),
					(eq, ":cur_good", "itm_raw_dyes"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_silk_looms),
					(val_mul, ":raw_material_consumption", 1),
				(else_try),
					(eq, ":cur_good", "itm_raw_silk"),
					(party_get_slot, ":raw_material_consumption", ":center_no", slot_center_silk_looms),
					(val_mul, ":raw_material_consumption", 5),
					
					
				(else_try),
					(eq, ":cur_good", "itm_salt"),
					(party_get_slot, ":salt_for_beef", ":center_no", slot_center_head_cattle),
					(val_div, ":salt_for_beef", 10),
					
					(party_get_slot, ":salt_for_fish", ":center_no", slot_center_fishing_fleet),
					(val_div, ":salt_for_fish", 5),
					
					(store_add, ":raw_material_consumption", ":salt_for_beef", ":salt_for_fish"),
				(try_end),
				
				(try_begin), #Reduce consumption of raw materials if their cost is high
					(gt, ":raw_material_consumption", 0),
					(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
					(store_add, ":cur_good_price_slot", ":cur_good", ":item_to_price_slot"),
					(party_get_slot, ":cur_center_price", ":center_no", ":cur_good_price_slot"),
					(gt, ":cur_center_price", 1000),
					(val_mul, ":raw_material_consumption", 1000),
					(val_div, ":raw_material_consumption", ":cur_center_price"),
				(try_end),
				
				
				
				(store_add, ":modified_consumption", ":consumer_consumption", ":raw_material_consumption"),
				(try_begin),
					(party_get_slot, ":prosperity_plus_75", ":center_no", slot_town_prosperity),
					(val_add, ":prosperity_plus_75", 75),
					(val_mul, ":modified_consumption", ":prosperity_plus_75"),
					(val_div, ":modified_consumption", 125),
				(try_end),
				
				
				(assign, reg0, ":modified_consumption"), #modded by prosperity
				(assign, reg1, ":raw_material_consumption"),
				(assign, reg2, ":consumer_consumption"),
		])
		
		#script_get_enterprise_name
		# INPUT: arg1 = item_no
		# Output: reg0: production string
get_enterprise_name	= (
	"get_enterprise_name",
			[
				(store_script_param_1, ":item_produced"),
				(assign, ":enterprise_name", "str_bread_site"),
				(try_begin),
					(eq, ":item_produced", "itm_bread"),
					(assign, ":enterprise_name", "str_bread_site"),
				(else_try),
					(eq, ":item_produced", "itm_ale"),
					(assign, ":enterprise_name", "str_ale_site"),
				(else_try),
					(eq, ":item_produced", "itm_oil"),
					(assign, ":enterprise_name", "str_oil_site"),
				(else_try),
					(eq, ":item_produced", "itm_wine"),
					(assign, ":enterprise_name", "str_wine_site"),
				(else_try),
					(eq, ":item_produced", "itm_leatherwork"),
					(assign, ":enterprise_name", "str_leather_site"),
				(else_try),
					(eq, ":item_produced", "itm_wool_cloth"),
					(assign, ":enterprise_name", "str_wool_cloth_site"),
				(else_try),
					(eq, ":item_produced", "itm_linen"),
					(assign, ":enterprise_name", "str_linen_site"),
				(else_try),
					(eq, ":item_produced", "itm_velvet"),
					(assign, ":enterprise_name", "str_velvet_site"),
				(else_try),
					(eq, ":item_produced", "itm_tools"),
					(assign, ":enterprise_name", "str_tool_site"),
				(try_end),
				(assign, reg0, ":enterprise_name"),
		])
		