from header import *

#script_game_event_buy_item:
	# This script is called from the game engine when player buys an item.
	# INPUT:
	# param1: item_kind_id
game_event_buy_item =(
	"game_event_buy_item",
		[
			(store_script_param_1, ":item_kind_id"),
			(store_script_param_2, ":reclaim_mode"),
			(try_begin),
				(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
				(store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
				(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
				(party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
				(try_begin),
					(eq, ":reclaim_mode", 0),
					(val_add, ":multiplier", 10),
				(else_try),
					(val_add, ":multiplier", 15),
				(try_end),
				(val_min, ":multiplier", maximum_price_factor),
				(party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
			(try_end),
	])

#script_game_event_sell_item:
	# This script is called from the game engine when player sells an item.
	# INPUT:
	# param1: item_kind_id
game_event_sell_item =	(
	"game_event_sell_item",
		[
			(store_script_param_1, ":item_kind_id"),
			(store_script_param_2, ":return_mode"),
			(try_begin),
				(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
				(store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
				(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
				(party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
				(try_begin),
					(eq, ":return_mode", 0),
					(val_sub, ":multiplier", 15),
				(else_try),
					(val_sub, ":multiplier", 10),
				(try_end),
				(val_max, ":multiplier", minimum_price_factor),
				(party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
			(try_end),
	])

#script_set_trade_route_between_centers
		# INPUT:
		# param1: center_no_1
		# param1: center_no_2
set_trade_route_between_centers	= (
	"set_trade_route_between_centers",
			[(store_script_param, ":center_no_1", 1),
				(store_script_param, ":center_no_2", 2),
				(assign, ":center_1_added", 0),
				(assign, ":center_2_added", 0),
				(try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
					(try_begin),
						(eq, ":center_1_added", 0),
						(party_slot_eq, ":center_no_1", ":cur_slot", 0),
						(party_set_slot, ":center_no_1", ":cur_slot", ":center_no_2"),
						(assign, ":center_1_added", 1),
					(try_end),
					(try_begin),
						(eq, ":center_2_added", 0),
						(party_slot_eq, ":center_no_2", ":cur_slot", 0),
						(party_set_slot, ":center_no_2", ":cur_slot", ":center_no_1"),
						(assign, ":center_2_added", 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":center_1_added", 0),
					(str_store_party_name, s1, ":center_no_1"),
					(display_message, "@{!}DEBUG -- ERROR: More than 15 trade routes are given for {s1}."),
				(try_end),
				(try_begin),
					(eq, ":center_2_added", 0),
					(str_store_party_name, s1, ":center_no_2"),
					(display_message, "@{!}DEBUG -- ERROR: More than 15 trade routes are given for {s1}."),
				(try_end),
		])

		# script_average_trade_good_prices
		# Called from start
		# INPUT: none
		# OUTPUT: none
		
average_trade_good_prices	= (
	"average_trade_good_prices", #Called from start
			[
				#This should be done by route rather than distance
				(store_sub, ":item_to_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
				
				(try_for_range, ":center_no", towns_begin, towns_end),
					(this_or_next|is_between, ":center_no", towns_begin, towns_end),
					(is_between, ":center_no", villages_begin, villages_end),
					
					(try_for_range, ":other_center", centers_begin, centers_end),
						(this_or_next|is_between, ":center_no", towns_begin, towns_end),
						(is_between, ":center_no", villages_begin, villages_end),
						
						(neq, ":other_center", ":center_no"),
						(store_distance_to_party_from_party, ":cur_distance", ":center_no", ":other_center"),
						(lt, ":cur_distance", 50), #Reduced from 110
						(store_sub, ":dist_factor", 50, ":cur_distance"),
						
						(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
							(store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
							(party_get_slot, ":center_price", ":center_no", ":cur_good_slot"),
							(party_get_slot, ":other_center_price", ":other_center", ":cur_good_slot"),
							(store_sub, ":price_dif", ":center_price", ":other_center_price"),
							
							(assign, ":price_dif_change", ":price_dif"),
							
							(val_mul ,":price_dif_change", ":dist_factor"),
							(val_div ,":price_dif_change", 1000), #Maximum of 1/20 per center
							(val_add, ":other_center_price", ":price_dif_change"),
							(party_set_slot, ":other_center", ":cur_good_slot", ":other_center_price"),
							
							(val_sub, ":center_price", ":price_dif_change"),
							(party_set_slot, ":center_no", ":cur_good_slot", ":center_price"),
						(try_end),
					(try_end),
				(try_end),
		])
		
		# script_average_trade_good_prices_2
		# Called from start
		# INPUT: none
		# OUTPUT: none
average_trade_good_prices_2	= (
	"average_trade_good_prices_2", #Called from start
			[
				
				#This should be done by route rather than distance
				(store_sub, ":item_to_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
				
				(try_for_range, ":center_no", towns_begin, towns_end),
					(try_for_range, ":other_center", centers_begin, centers_end),
						(this_or_next|is_between, ":other_center", towns_begin, towns_end),
						(is_between, ":other_center", villages_begin, villages_end),
						
						(this_or_next|party_slot_eq, ":other_center", slot_village_market_town, ":center_no"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_1, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_2, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_3, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_4, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_5, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_6, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_7, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_8, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_9, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_10, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_11, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_12, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_13, ":other_center"),
						(this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_14, ":other_center"),
						(party_slot_eq, ":center_no", slot_town_trade_route_15, ":other_center"),
						
						#          (neq, ":other_center", ":center_no"),
						#          (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":other_center"),
						#          (lt, ":cur_distance", 50), #Reduced from 110
						#          (store_sub, ":dist_factor", 50, ":cur_distance"),
						
						(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
							(store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
							(party_get_slot, ":center_price", ":center_no", ":cur_good_slot"),
							(party_get_slot, ":other_center_price", ":other_center", ":cur_good_slot"),
							(store_sub, ":price_dif", ":center_price", ":other_center_price"),
							
							(store_div, ":price_dif_change", ":price_dif", 5), #this is done twice, reduced from 4
							#            (assign, ":price_dif_change", ":price_dif"),
							
							#            (val_mul ,":price_dif_change", ":dist_factor"),
							#            (val_div ,":price_dif_change", 500), #Maximum of 1/10 per center
							(val_add, ":other_center_price", ":price_dif_change"),
							(party_set_slot, ":other_center", ":cur_good_slot", ":other_center_price"),
							
							(val_sub, ":center_price", ":price_dif_change"),
							(party_set_slot, ":center_no", ":cur_good_slot", ":center_price"),
							
						(try_end),
					(try_end),
				(try_end),
		])
		
		
		
		#script_average_trade_good_productions
		# INPUT: none (called only from game start?)
		#This is currently deprecated, as I was going to try to fine-tune production
average_trade_good_productions	= (
	"average_trade_good_productions",
			[
				(store_sub, ":item_to_slot", slot_town_trade_good_productions_begin, trade_goods_begin),
				(try_for_range, ":center_no", towns_begin, towns_end),
					(this_or_next|is_between, ":center_no", towns_begin, towns_end),
					(is_between, ":center_no", villages_begin, villages_end),
					(try_for_range, ":other_center", centers_begin, centers_end),
						(this_or_next|is_between, ":center_no", towns_begin, towns_end),
						(is_between, ":center_no", villages_begin, villages_end),
						(neq, ":other_center", ":center_no"),
						(store_distance_to_party_from_party, ":cur_distance", ":center_no", ":other_center"),
						(lt, ":cur_distance", 110),
						(store_sub, ":dist_factor", 110, ":cur_distance"),
						(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
							(store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
							(party_get_slot, ":center_production", ":center_no", ":cur_good_slot"),
							(party_get_slot, ":other_center_production", ":other_center", ":cur_good_slot"),
							(store_sub, ":prod_dif", ":center_production", ":other_center_production"),
							(gt, ":prod_dif", 0),
							(store_mul, ":prod_dif_change", ":prod_dif", 1),
							##            (try_begin),
							##              (is_between, ":center_no", towns_begin, towns_end),
							##              (is_between, ":other_center", towns_begin, towns_end),
							##              (val_mul, ":cur_distance", 2),
							##            (try_end),
							(val_mul ,":prod_dif_change", ":dist_factor"),
							(val_div ,":prod_dif_change", 110),
							(val_add, ":other_center_production", ":prod_dif_change"),
							(party_set_slot, ":other_center", ":cur_good_slot", ":other_center_production"),
						(try_end),
					(try_end),
				(try_end),
		])
		
		#script_normalize_trade_good_productions
		#Adjusts productions according to the amount of the item produced
		# INPUT: none
		# This currently deprecated, as I was going to try to fine-tune productions
normalize_trade_good_productions	= (
	"normalize_trade_good_productions",
			[
				(store_sub, ":item_to_slot", slot_town_trade_good_productions_begin, trade_goods_begin),
				(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
					(assign, ":total_production", 0),
					(assign, ":num_centers", 0),
					(store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
					(try_for_range, ":center_no", centers_begin, centers_end),
						(val_add, ":num_centers", 1),
						(try_begin),
							(is_between, ":center_no", towns_begin, towns_end), #each town is weighted as 5 villages...
							(val_add, ":num_centers", 4),
						(try_end),
						(party_get_slot, ":center_production", ":center_no", ":cur_good_slot"),
						(val_add, ":total_production", ":center_production"),
					(try_end),
					(store_div, ":new_production_difference", ":total_production", ":num_centers"),
					(neq, ":new_production_difference", 0),
					(try_for_range, ":center_no", centers_begin, centers_end),
						(this_or_next|is_between, ":center_no", towns_begin, towns_end),
						(is_between, ":center_no", villages_begin, villages_end),
						(party_get_slot, ":center_production", ":center_no", ":cur_good_slot"),
						(val_sub, ":center_production", ":new_production_difference"),
						(party_set_slot, ":center_no", ":cur_good_slot", ":center_production"),
					(try_end),
				(try_end),
		])
		
		#script_update_trade_good_prices
		# INPUT: none
update_trade_good_prices	= (
	"update_trade_good_prices",
			[
				(try_for_range, ":center_no", centers_begin, centers_end),
					(this_or_next|is_between, ":center_no", towns_begin, towns_end),
					(is_between, ":center_no", villages_begin, villages_end),
					(call_script, "script_update_trade_good_price_for_party", ":center_no"),
				(try_end),
				
				(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
					(assign, ":total_price", 0),
					(assign, ":total_constants", 0),
					
					(try_for_range, ":center_no", centers_begin, centers_end),
						(this_or_next|is_between, ":center_no", towns_begin, towns_end),
						(is_between, ":center_no", villages_begin, villages_end),
						
						(store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
						(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
						(party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),
						
						(try_begin),
							(is_between, ":center_no", towns_begin, towns_end),
							(assign, ":constant", 5),
						(else_try),
							(assign, ":constant", 1),
						(try_end),
						
						(val_mul, ":cur_price", ":constant"),
						
						(val_add, ":total_price", ":cur_price"),
						(val_add, ":total_constants", ":constant"),
					(try_end),
					
					(try_for_range, ":center_no", centers_begin, centers_end),
						(this_or_next|is_between, ":center_no", towns_begin, towns_end),
						(is_between, ":center_no", villages_begin, villages_end),
						
						(store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
						(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
						(party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),
						
						(val_mul, ":cur_price", 1000),
						(val_mul, ":cur_price", ":total_constants"),
						(val_div, ":cur_price", ":total_price"),
						
						(val_clamp, ":cur_price", minimum_price_factor, maximum_price_factor),
						(party_set_slot, ":center_no", ":cur_good_price_slot", ":cur_price"),
					(try_end),
				(try_end),
		])
		
		#script_update_trade_good_price_for_party
		# INPUT: arg1 = party_no
		#Called once every 72 hours
update_trade_good_price_for_party	= (
	"update_trade_good_price_for_party",
			[
				(store_script_param, ":center_no", 1),
				(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
					(store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
					(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
					(party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),
					
					(call_script, "script_center_get_production", ":center_no", ":cur_good"),
					(assign, ":production", reg0),
					
					(call_script, "script_center_get_consumption", ":center_no", ":cur_good"),
					(assign, ":consumption", reg0),
					
					(val_sub, ":production", ":consumption"),
					
					#Change averages production x 2(1+random(2)) (was 4, random(8)) for excess demand
					(try_begin),
						#supply is greater than demand
						(gt, ":production", 0),
						(store_mul, ":change_factor", ":production", 1), #price will be decreased by his factor
						(store_random_in_range, ":random_change", 0, ":change_factor"),
						(val_add, ":random_change", ":change_factor"),
						(val_add, ":random_change", ":change_factor"),
						
						#simulation starts
						(store_sub, ":final_price", ":cur_price", ":random_change"),
						(val_clamp, ":final_price", minimum_price_factor, maximum_price_factor),
						(try_begin), #Excess of supply decelerates over time, as low price reduces output
							#if expected final price is 100 then it will multiply random_change by 0.308x ((100+300)/(1300) = 400/1300).
							(lt, ":final_price", 1000),
							(store_add, ":final_price_plus_300", ":final_price", 300),
							(val_mul, ":random_change", ":final_price_plus_300"),
							(val_div, ":random_change", 1300),
						(try_end),
						(val_sub, ":cur_price", ":random_change"),
					(else_try),
						(lt, ":production", 0),
						(store_sub, ":change_factor", 0, ":production"), #price will be increased by his factor
						(val_mul, ":change_factor", 1),
						(store_random_in_range, ":random_change", 0, ":change_factor"),
						(val_add, ":random_change", ":change_factor"),
						(val_add, ":random_change", ":change_factor"),
						(val_add, ":cur_price", ":random_change"),
					(try_end),
					
					#Move price towards average by 3%...
					#Equilibrium is 33 cycles, or 100 days
					#Change per cycle is Production x 4
					#Thus, max differential = -5 x 4 x 33 = -660 for -5
					(try_begin),
						(is_between, ":center_no", villages_begin, villages_end),
						(store_sub, ":price_difference", ":cur_price", average_price_factor),
						(val_mul, ":price_difference", 96),
						(val_div, ":price_difference", 100),
						(store_add, ":new_price", average_price_factor, ":price_difference"),
					(else_try),
						(store_sub, ":price_difference", ":cur_price", average_price_factor),
						(val_mul, ":price_difference", 96),
						(val_div, ":price_difference", 100),
						(store_add, ":new_price", average_price_factor, ":price_difference"),
					(try_end),
					
					#Price of manufactured goods drift towards primary raw material
					(try_begin),
						(item_get_slot, ":raw_material", ":cur_good", slot_item_primary_raw_material),
						(neq, ":raw_material", 0),
						(store_sub, ":raw_material_price_slot", ":raw_material", trade_goods_begin),
						(val_add, ":raw_material_price_slot", slot_town_trade_good_prices_begin),
						
						(party_get_slot, ":total_raw_material_price", ":center_no", ":raw_material_price_slot"),
						(val_mul, ":total_raw_material_price", 3),
						(assign, ":number_of_centers", 3),
						
						(try_for_range, ":village_no", villages_begin, villages_end),
							(party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
							(party_get_slot, ":raw_material_price", ":village_no", ":raw_material_price_slot"),
							(val_add, ":total_raw_material_price", ":raw_material_price"),
							(val_add, ":number_of_centers", 1),
						(try_end),
						
						(store_div, ":average_raw_material_price", ":total_raw_material_price", ":number_of_centers"),
						
						(gt, ":average_raw_material_price", ":new_price"),
						(store_sub, ":raw_material_boost", ":average_raw_material_price", ":new_price"),
						(val_div, ":raw_material_boost", 10),
						(val_add, ":new_price", ":raw_material_boost"),
					(try_end),
					
					(val_clamp, ":new_price", minimum_price_factor, maximum_price_factor),
					(party_set_slot, ":center_no", ":cur_good_price_slot", ":new_price"),
					
					#(assign, reg3, ":new_price"),
					#(str_store_item_name, s2, ":cur_good"),
					#(display_log_message, "@DEBUG : {s1}-{s2}, prod:{reg1}, cons:{reg2}, price:{reg3}"),
				(try_end),
		])

		#script_do_merchant_town_trade
		# INPUT: arg1 = party_no (of the merchant), arg2 = center_no
do_merchant_town_trade	= (
	"do_merchant_town_trade",
			[
				(store_script_param_1, ":party_no"),
				(store_script_param_2, ":center_no"),
				
				(party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
				
				(try_begin),
					(eq, "$cheat_mode", 2),
					(str_store_party_name, s4, ":center_no"),
					(str_store_party_name, s5, ":origin"),
					(display_message, "@{!}DEBUG -- Caravan trades in {s4}, originally from {s5}"),
				(try_end),
				
				(call_script, "script_add_log_entry", logent_party_traded, ":party_no", ":origin", ":center_no", -1),
				
				(call_script, "script_do_party_center_trade", ":party_no", ":center_no", 4), #change prices by 20%, also, sets party_last_traded to new
				
				(assign, ":total_change", reg0),
				#Adding the earnings to the wealth (maximum changed price is the earning)
				(val_div, ":total_change", 2),
				(str_store_party_name, s1, ":party_no"),
				(str_store_party_name, s2, ":center_no"),
				(assign, reg1, ":total_change"),
				
				#Adding tariffs to the town
				(party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
				(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
				
				(assign, ":tariffs_generated", ":total_change"),
				(val_mul, ":tariffs_generated", ":prosperity"),
				(val_div, ":tariffs_generated", 100),
				(val_div, ":tariffs_generated", 10), #10 for caravans, 20 for villages
				(val_add, ":accumulated_tariffs", ":tariffs_generated"),
				
				(try_begin),
					(ge, "$cheat_mode", 3),
					(assign, reg4, ":tariffs_generated"),
					(str_store_party_name, s4, ":center_no"),
					(assign, reg5, ":accumulated_tariffs"),
					(display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
				(try_end),
				
				(party_set_slot, ":center_no", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
				
		#Adding 1 to center prosperity with 18% for each caravan in that center
			(try_begin),
				(store_random_in_range, ":rand", 0, 80),
				(call_script, "script_center_get_goods_availability", ":center_no"),
				(assign, ":hardship_index", reg0),
				(gt, ":rand", ":hardship_index"),
				(try_begin),
					(store_random_in_range, ":rand", 0, 100),
					(gt, ":rand", 90), ##tom was 82
					(call_script, "script_change_center_prosperity", ":center_no", 1),
					(val_add, "$newglob_total_prosperity_from_caravan_trade", 1),
				(try_end),
			(try_end),      
				
		])
		