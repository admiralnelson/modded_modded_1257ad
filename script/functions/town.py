from header import *


# script_find_travel_location
# Input: arg1 = center_no
# Output: reg0 = new_center_no (to travel within the same faction)
find_travel_location = (
	"find_travel_location",
			[
				(store_script_param_1, ":center_no"),
				(store_faction_of_party, ":faction_no", ":center_no"),
				(assign, ":total_weight", 0),
				(try_for_range, ":cur_center_no", centers_begin, centers_end),
					(neq, ":center_no", ":cur_center_no"),
					(store_faction_of_party, ":center_faction_no", ":cur_center_no"),
					(eq, ":faction_no", ":center_faction_no"),
					
					(store_distance_to_party_from_party, ":cur_distance", ":center_no", ":cur_center_no"),
					(val_add, ":cur_distance", 1),
					
					(assign, ":new_weight", 100000),
					(val_div, ":new_weight", ":cur_distance"),
					(val_add, ":total_weight", ":new_weight"),
				(try_end),
				
				(assign, reg0, -1),
				
				(try_begin),
					(eq, ":total_weight", 0),
				(else_try),
					(store_random_in_range, ":random_weight", 0 , ":total_weight"),
					(assign, ":total_weight", 0),
					(assign, ":done", 0),
					(try_for_range, ":cur_center_no", centers_begin, centers_end),
						(eq, ":done", 0),
						(neq, ":center_no", ":cur_center_no"),
						(store_faction_of_party, ":center_faction_no", ":cur_center_no"),
						(eq, ":faction_no", ":center_faction_no"),
						
						(store_distance_to_party_from_party, ":cur_distance", ":center_no", ":cur_center_no"),
						(val_add, ":cur_distance", 1),
						
						(assign, ":new_weight", 100000),
						(val_div, ":new_weight", ":cur_distance"),
						(val_add, ":total_weight", ":new_weight"),
						(lt, ":random_weight", ":total_weight"),
						(assign, reg0, ":cur_center_no"),
						(assign, ":done", 1),
					(try_end),
				(try_end),
		])

# script_create_cattle_herd
# Input: arg1 = center_no, arg2 = amount (0 = default)
# Output: reg0 = party_no
create_cattle_herd = (
	"create_cattle_herd",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":amount"),
				
				(assign, ":herd_party", -1),
				(set_spawn_radius,1),
				
				(spawn_around_party,":center_no", "pt_cattle_herd"),
				(assign, ":herd_party", reg0),
				(party_get_position, pos1, ":center_no"),
				(call_script, "script_map_get_random_position_around_position_within_range", 1, 2),
				(party_set_position, ":herd_party", pos2),
				
				(party_set_slot, ":herd_party", slot_party_type, spt_cattle_herd),
				(party_set_slot, ":herd_party", slot_party_ai_state, spai_undefined),
				(party_set_ai_behavior, ":herd_party", ai_bhvr_hold),
				
				(party_set_slot, ":herd_party", slot_party_commander_party, -1), #we need this because 0 is player's party!
				
				(try_begin),
					(gt, ":amount", 0),
					(party_clear, ":herd_party"),
					(party_add_members, ":herd_party", "trp_cattle", ":amount"),
				(try_end),
				
				(assign, reg0, ":herd_party"),
		])

		
#script_buy_cattle_from_village
# Input: arg1 = village_no, arg2 = amount, arg3 = single_cost
# Output: reg0 = party_no
buy_cattle_from_village = (
	"buy_cattle_from_village",
			[
				(store_script_param, ":village_no", 1),
				(store_script_param, ":amount", 2),
				(store_script_param, ":single_cost", 3),
				
				#Changing price of the cattle
				(try_for_range, ":unused", 0, ":amount"),
					(call_script, "script_game_event_buy_item", "itm_cattle_meat", 0),
					(call_script, "script_game_event_buy_item", "itm_cattle_meat", 0),
				(try_end),
				
				(party_get_slot, ":num_cattle", ":village_no", slot_village_number_of_cattle),
				(val_sub, ":num_cattle", ":amount"),
				(party_set_slot, ":village_no", slot_village_number_of_cattle, ":num_cattle"),
				(store_mul, ":cost", ":single_cost", ":amount"),
				(troop_remove_gold, "trp_player", ":cost"),
				
				(assign, ":continue", 1),
				(try_for_parties, ":cur_party"),
					(eq, ":continue", 1),
					(party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
					(store_distance_to_party_from_party, ":dist", ":village_no", ":cur_party"),
					(lt, ":dist", 6),
					(assign, ":subcontinue", 1),
					(try_begin),
						(check_quest_active, "qst_move_cattle_herd"),
						(quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
						(assign, ":subcontinue", 0),
					(try_end),
					(eq, ":subcontinue", 1),
					(party_add_members, ":cur_party", "trp_cattle", ":amount"),
					(assign, ":continue", 0),
					(assign, reg0, ":cur_party"),
				(try_end),
				(try_begin),
					(eq, ":continue", 1),
					(call_script, "script_create_cattle_herd", ":village_no", ":amount"),
				(try_end),
		])

# script_center_get_food_consumption
# Input: arg1 = center_no
# Output: reg0: food consumption (1 food item counts as 100 units)
center_get_food_consumption = (
	"center_get_food_consumption",
			[
				(store_script_param_1, ":center_no"),
				(assign, ":food_consumption", 0),
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_town),
					(assign, ":food_consumption", 500),
				(else_try),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(assign, ":food_consumption", 50),
				(try_end),
				(assign, reg0, ":food_consumption"),
		])

# script_center_get_food_store_limit
# WARNING: modified by 1257AD devs
# Input: arg1 = center_no
# Output: reg0: food consumption (1 food item counts as 100 units)
center_get_food_store_limit = (
	"center_get_food_store_limit",
			[
				(store_script_param_1, ":center_no"),
				(assign, ":food_store_limit", 0),
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_town),
					(assign, ":food_store_limit", 50000),
				(else_try),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(assign, ":food_store_limit", 1500),
				(try_end),
				# rafi - cut food in half
				(val_div, ":food_store_limit", 4),
				# end rafi
				(assign, reg0, ":food_store_limit"),
		])

# script_village_set_state
# no longer resemble script in native version
# 1257AD prosperity system resides here
# WARNING: heavily modified by 1257AD
# Input: arg1 = center_no arg2:new_state
# Output: reg0: food consumption (1 food item counts as 100 units)
village_set_state = (
	"village_set_state",
			[
				(store_script_param_1, ":village_no"),
				(store_script_param_2, ":new_state"),
				#      (party_get_slot, ":old_state", ":village_no", slot_village_state),
				(try_begin),
					(eq, ":new_state", 0),
					(party_set_extra_text, ":village_no", "str_empty_string"),
					(party_set_slot, ":village_no", slot_village_raided_by, -1),
				(else_try),
					(eq, ":new_state", svs_being_raided),
					(party_set_extra_text, ":village_no", "@(Being Raided)"),
				(else_try),
					(eq, ":new_state", svs_looted),
					(party_set_extra_text, ":village_no", "@(Looted)"),
					
					(party_set_slot, ":village_no", slot_village_raided_by, -1),
					(call_script, "script_change_center_prosperity", ":village_no", -60), #reduced from 30
					(val_add, "$newglob_total_prosperity_from_villageloot", -60),
			
					##PROSPERITY SYSTEM
					(party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
						(try_begin),
							(is_between, ":bound_center", towns_begin, towns_end),
								(call_script, "script_change_center_prosperity", ":bound_center", -30),
						(else_try), #castles handle it better
							(gt, ":bound_center", 0),
								(call_script, "script_change_center_prosperity", ":bound_center", -20),
					(try_end),
					##PROSPERITY SYSTEM
			
					(try_begin), #optional - lowers the relationship between a lord and his liege if his fief is looted
						(eq, 5, 0),
							(party_get_slot, ":town_lord", ":village_no", slot_town_lord),
							(is_between, ":town_lord", active_npcs_begin, active_npcs_end),
								(store_faction_of_troop, ":town_lord_faction", ":town_lord"),
								(faction_get_slot, ":faction_leader", ":town_lord_faction", slot_faction_leader),
								(call_script, "script_troop_change_relation_with_troop", ":town_lord", ":faction_leader", -1),
								(val_add, "$total_battle_ally_changes", -1),
						(try_end),
				(else_try),
					(eq, ":new_state", svs_under_siege),
						(party_set_extra_text, ":village_no", "@(Under Siege)"),
					
						#Divert all caravans heading to the center
						#Note that occasionally, no alternative center will be found. In that case, the caravan will try to run the blockade
						(try_for_parties, ":party_no"),
							(gt, ":party_no", "p_spawn_points_end"),
							(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
							(party_slot_eq, ":party_no", slot_party_ai_object, ":village_no"),
								(party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
								(store_faction_of_party, ":merchant_faction", ":party_no"),						
								(call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":origin", ":merchant_faction"),
									(assign, ":target_center", reg0),
										(is_between, ":target_center", centers_begin, centers_end),						
											(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
											(party_set_ai_object, ":party_no", ":target_center"),
											(party_set_flags, ":party_no", pf_default_behavior, 0),
											(party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
											(party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
						(try_end),
				(try_end),
				(party_set_slot, ":village_no", slot_village_state, ":new_state"),
		])

# script_get_center_faction_relation_including_player
		# called from triggers
		# Input: arg1: center_no, arg2: target_faction_no
		# Output: reg0: relation
		
get_center_faction_relation_including_player =	(
	"get_center_faction_relation_including_player",
			[
				(store_script_param, ":center_no", 1),
				(store_script_param, ":target_faction_no", 2),
				(store_faction_of_party, ":center_faction", ":center_no"),
				(store_relation, ":relation", ":center_faction", ":target_faction_no"),
				(try_begin),
					(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(store_relation, ":relation", "fac_player_supporters_faction", ":target_faction_no"),
				(try_end),
				(assign, reg0, ":relation"),
		])

#script_get_available_mercenary_troop_and_amount_of_center
# INPUT: arg1 = center_no
# OUTPUT: reg0 = mercenary_troop_type, reg1 = amount
get_available_mercenary_troop_and_amount_of_center = (
	"get_available_mercenary_troop_and_amount_of_center",
			[(store_script_param, ":center_no", 1),
				(party_get_slot, ":mercenary_troop", ":center_no", slot_center_mercenary_troop_type),
				(party_get_slot, ":mercenary_amount", ":center_no", slot_center_mercenary_troop_amount),
				(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
				(val_min, ":mercenary_amount", ":free_capacity"),
				(store_troop_gold, ":cur_gold", "trp_player"),
				(call_script, "script_game_get_join_cost", ":mercenary_troop"),
				(assign, ":join_cost", reg0),
				(try_begin),
					(gt, ":join_cost", 0),
					(val_div, ":cur_gold", ":join_cost"),
					(val_min, ":mercenary_amount", ":cur_gold"),
				(try_end),
				(assign, reg0, ":mercenary_troop"),
				(assign, reg1, ":mercenary_amount"),
		])
		
# script_create_village_farmer_party
# spawns villager party
# WARNING : modified by 1257AD devs
# WARNING : IT'S ALSO DISABLED BY TOM!! look simple_triggers at : 2300
# Input: arg1 = village_no
# Output: reg0 = party_no
create_village_farmer_party = (
	"create_village_farmer_party",
			[(store_script_param, ":village_no", 1),

				(party_get_slot, ":town_no", ":village_no", slot_village_market_town),
				(store_faction_of_party, ":party_faction", ":town_no"),
				
				#    (store_faction_of_party, ":town_faction", ":town_no"),
				#    (try_begin),
				#		(neq, ":town_faction", ":party_faction"),
				#		(assign, ":town_no", -1),
				#		(assign, ":score_to_beat", 9999),
				#		(try_for_range, ":other_town", towns_begin, towns_end),
				#			(store_faction_of_party, ":other_town_faction", ":town_no"),
				#			(store_relation, ":relation", ":other_town_faction", ":party_faction"),
				#			(ge, ":relation", 0),
				
				#			(store_distance_to_party_from_party, ":distance", ":village_no", ":other_town"),
				#			(lt, ":distance", ":score_to_beat"),
				#			(assign, ":town_no", ":other_town"),
				#			(assign, ":score_to_beat", ":distance"),
				#		(try_end),
				#	(try_end),
				
				(try_begin),
			(is_between, ":party_faction", kingdoms_begin, kingdoms_end), #tom
					(is_between, ":town_no", towns_begin, towns_end),
					(set_spawn_radius, 0),
					(spawn_around_party, ":village_no", "pt_village_farmers"),
					(assign, ":new_party", reg0),
					
					(party_set_faction, ":new_party", ":party_faction"),
					(party_set_slot, ":new_party", slot_party_home_center, ":village_no"),
					(party_set_slot, ":new_party", slot_party_last_traded_center, ":village_no"),
					
					(party_set_slot, ":new_party", slot_party_type, spt_village_farmer),
					(party_set_slot, ":new_party", slot_party_ai_state, spai_trading_with_town),
					(party_set_slot, ":new_party", slot_party_ai_object, ":town_no"),
					(party_set_ai_behavior, ":new_party", ai_bhvr_travel_to_party),
					(party_set_ai_object, ":new_party", ":town_no"),
					(party_set_flags, ":new_party", pf_default_behavior, 0),
					(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
					(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
						(store_add, ":cur_good_price_slot", ":cur_goods", ":item_to_price_slot"),
						(party_get_slot, ":cur_village_price", ":village_no", ":cur_good_price_slot"),
						(party_set_slot, ":new_party", ":cur_good_price_slot", ":cur_village_price"),
					(try_end),
					(assign, reg0, ":new_party"),
				(try_end),
		])
	 