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
	 
#script_get_center_ideal_prosperity
		# INPUT: arg1 = center_no
		# OUTPUT: reg0 = ideal_prosperity
get_center_ideal_prosperity = (
	"get_center_ideal_prosperity",
			[(store_script_param, ":center_no", 1),
				(assign, ":ideal", 100),
				
				(call_script, "script_center_get_goods_availability", ":center_no"),
				(store_mul, ":hardship_index", reg0, 2), #currently x2
				#	 (val_div, ":hardship_index", 2), #Currently x2.5
				
				(val_sub, ":ideal", ":hardship_index"),
				(val_max, ":ideal", 0),
				
				(try_begin),
					(is_between, ":center_no", villages_begin, villages_end),
					(party_slot_eq, ":center_no", slot_center_has_fish_pond, 1),
					(val_add, ":ideal", 5),
				(try_end),
				
				(assign, reg0, ":ideal"),
		])


		# script_calculate_amount_of_cattle_can_be_stolen
		# Input: arg1 = village_no
		# Output: reg0 = max_amount
calculate_amount_of_cattle_can_be_stolen = (
		"calculate_amount_of_cattle_can_be_stolen",
			[
				(store_script_param, ":village_no", 1),
				(call_script, "script_get_max_skill_of_player_party", "skl_looting"),
				(assign, ":max_skill", reg0),
				(store_mul, ":can_steal", ":max_skill", 2),
				(call_script, "script_party_count_fit_for_battle", "p_main_party"),
				(store_add, ":num_men_effect", reg0, 10),
				(val_div, ":num_men_effect", 10),
				(val_add, ":can_steal", ":num_men_effect"),
				(party_get_slot, ":num_cattle", ":village_no", slot_village_number_of_cattle),
				(val_min, ":can_steal", ":num_cattle"),
				(assign, reg0, ":can_steal"),
		])
		
		#script_merchant_road_info_to_s42
	# WARNING: heavily modified by 1257AD devs
	#INPUT: town
	#OUTPUT: reg0, ":last_bandit_party_found"
	#		 reg1, ":last_bandit_party_origin"
	#	     reg2, ":last_bandit_party_destination"
	#	     reg3, ":last_bandit_party_hours_ago"
merchant_road_info_to_s42 = (
	"merchant_road_info_to_s42", #also does itemss to s32
		[
		(store_script_param, ":center", 1),
		
		(assign, ":last_bandit_party_found", -1),
		(assign, ":last_bandit_party_origin", -1),
		(assign, ":last_bandit_party_destination", -1),
		(assign, ":last_bandit_party_hours_ago", -1),
		
		(str_clear, s32),
		
		(str_clear, s42),
		(str_clear, s47), #safe roads
		
		(try_for_range, ":center_to_reset", centers_begin, centers_end),
			(party_set_slot, ":center_to_reset", slot_party_temp_slot_1, 0),
		(try_end),
		
		(assign, ":road_attacks", 0),
		(assign, ":trades", 0),
		
		#first mention all attacks
		(try_for_range, ":log_entry_iterator", 0, "$num_log_entries"),
			(store_sub, ":log_entry_no", "$num_log_entries", ":log_entry_iterator"),
			#how long ago?
			(this_or_next|troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
			
			#       reference - (call_script, "script_add_log_entry", logent_traveller_attacked, ":winner_party" (actor),  ":origin" (center object), ":destination" (troop_object), ":winner_faction"),
			
			(troop_get_slot, ":origin",         "trp_log_array_center_object",         ":log_entry_no"),
			(troop_get_slot, ":destination",    "trp_log_array_troop_object",          ":log_entry_no"),
			
			(this_or_next|eq, ":origin", ":center"),
			(eq, ":destination", ":center"),
			
			
			(troop_get_slot, ":event_time",            "trp_log_array_entry_time",              ":log_entry_no"),
			(store_current_hours, ":cur_hour"),
			(store_sub, ":hours_ago", ":cur_hour", ":event_time"),
			(assign, reg3, ":hours_ago"),
			
			(lt, ":hours_ago", 672), #four weeks
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
			(display_message, "str_attack_on_travellers_found_reg3_hours_ago"),
			(else_try),
			(eq, "$cheat_mode", 1),
			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
			(display_message, "str_trade_event_found_reg3_hours_ago"),
			(try_end),
			
			(try_begin), #possibly make script -- get_colloquial_for_time
			(lt, ":hours_ago", 24),
			(str_store_string, s46, "str_a_short_while_ago"),
			(else_try),
			(lt, ":hours_ago", 48),
			(str_store_string, s46, "str_one_day_ago"),
			(else_try),
			(lt, ":hours_ago", 72),
			(str_store_string, s46, "@two days ago"),
			(else_try),
			(lt, ":hours_ago", 154),
			(str_store_string, s46, "str_earlier_this_week"),
			(else_try),
			(lt, ":hours_ago", 240),
			(str_store_string, s46, "str_about_a_week_ago"),
			(else_try),
			(lt, ":hours_ago", 480),
			(str_store_string, s46, "str_about_two_weeks_ago"),
			(else_try),
			(str_store_string, s46, "str_several_weeks_ago"),
			(try_end),
			
			
			
			(troop_get_slot, ":actor", "trp_log_array_actor", ":log_entry_no"),
			(troop_get_slot, ":faction_object", "trp_log_array_faction_object", ":log_entry_no"),
			
			(str_store_string, s39, "str_unknown_assailants"),
			(assign, ":assailants_known", -1),
			(try_begin),
			(party_is_active, ":actor"),
			(store_faction_of_party, ":actor_faction", ":actor"),
			(eq, ":faction_object", ":actor_faction"),
			(assign, ":assailants_known", ":actor"),
			(str_store_party_name, s39, ":assailants_known"),
			(assign, "$g_bandit_party_for_bounty", -1),
			(try_begin), #possibly make script -- get_colloquial_for_faction
				(eq, ":faction_object", "fac_kingdom_1"),
				(str_store_string, s39, "str_teutons"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_2"),
				(str_store_string, s39, "str_lithuanians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_3"),
				(str_store_string, s39, "str_mongols"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_4"),
				(str_store_string, s39, "str_danes"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_5"),
				(str_store_string, s39, "str_polish"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_6"),
				(str_store_string, s39, "str_hre"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_7"),
				(str_store_string, s39, "str_hungarians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_8"),
				(str_store_string, s39, "str_novgorodians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_9"),
				(str_store_string, s39, "str_english"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_10"),
				(str_store_string, s39, "str_french"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_11"),
				(str_store_string, s39, "str_norwegians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_12"),
				(str_store_string, s39, "str_scots"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_13"),
				(str_store_string, s39, "str_irish"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_14"),
				(str_store_string, s39, "str_swedes"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_15"),
				(str_store_string, s39, "str_galicians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_16"),
				(str_store_string, s39, "str_portugese"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_17"),
				(str_store_string, s39, "str_aragonese"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_18"),
				(str_store_string, s39, "str_castilans"),
				# (else_try),
				(eq, ":faction_object", "fac_kingdom_19"),
				(str_store_string, s39, "str_navarrians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_20"),
				(str_store_string, s39, "str_granadians"),
			(else_try),
				(eq, ":faction_object", "fac_papacy"),
				(str_store_string, s39, "str_papal"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_22"),
				(str_store_string, s39, "str_byzantinians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_23"),
				(str_store_string, s39, "str_jerusalem"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_24"),
				(str_store_string, s39, "str_sicilians"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_25"),
				(str_store_string, s39, "str_mamluks"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_26"),
				(str_store_string, s39, "str_latin"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_27"),
				(str_store_string, s39, "str_ilkhanate"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_28"),
				(str_store_string, s39, "str_hafsid"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_29"),
				(str_store_string, s39, "str_serbian"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_30"),
				(str_store_string, s39, "str_bulgarian"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_31"),
				(str_store_string, s39, "str_marinid"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_32"),
				(str_store_string, s39, "str_venice"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_33"),
				(str_store_string, s39, "str_balt"),
				# (else_try),
				# (eq, ":faction_object", "fac_kingdom_34"),
				# (str_store_string, s39, "str_tuscan"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_37"),
				(str_store_string, s39, "str_wales"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_38"),
				(str_store_string, s39, "str_genoa"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_39"),
				(str_store_string, s39, "str_pisa"),
			(else_try),
				(eq, ":faction_object", "fac_kingdom_40"),
				(str_store_string, s39, "str_guelph"),  
			(else_try),
				(eq, ":faction_object", "fac_kingdom_41"),
				(str_store_string, s39, "str_ghibeline"),   
			(else_try),
				(eq, ":faction_object", "fac_kingdom_42"),
				(str_store_string, s39, "str_bohemian"),    
			(else_try),
				(eq, ":faction_object", "fac_player_supporters_faction"),
				(str_store_string, s39, "str_your_followers"),
			(else_try), #bandits
				(assign, ":last_bandit_party_found", ":assailants_known"),
				(assign, ":last_bandit_party_origin", ":origin"),
				(assign, ":last_bandit_party_destination", ":destination"),
				(assign, ":last_bandit_party_hours_ago", ":hours_ago"),
			(try_end),
			(try_end),
			
			(try_begin),
			(eq, ":origin", ":center"),
			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
			(party_slot_eq, ":destination", slot_party_temp_slot_1, 0),
			
			(party_set_slot, ":destination", slot_party_temp_slot_1, 1),
			(str_store_party_name, s40, ":destination"),
			(str_store_string, s44, "str_we_have_heard_that_travellers_heading_to_s40_were_attacked_on_the_road_s46_by_s39"),
			(str_store_string, s43, "str_s42"),
			(str_store_string, s42, "str_s43_s44"),
			
			(val_add, ":road_attacks", 1),
			#travellers were attacked on the road to...
			(else_try),
			(eq, ":destination", ":center"),
			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
			(party_slot_eq, ":origin", slot_party_temp_slot_1, 0),
			
			(party_set_slot, ":origin", slot_party_temp_slot_1, 1),
			(str_store_party_name, s40, ":origin"),
			(str_store_string, s44, "str_we_have_heard_that_travellers_coming_from_s40_were_attacked_on_the_road_s46_by_s39"),
			
			(str_store_string, s43, "str_s42"),
			(str_store_string, s42, "str_s43_s44"),
			
			(val_add, ":road_attacks", 1),
			
			#travellers from here traded at...
			#		(else_try),
			#			(eq, ":origin", ":center"),
			#			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
			#			(party_slot_eq, ":destination", slot_party_temp_slot_1, 0),
			
			#			(party_set_slot, ":destination", slot_party_temp_slot_1, 1),
			#			(str_store_party_name, s40, ":destination"),
			#			(str_store_string, s44, "@Travellers headed to {s40} traded there {s46}"),
			#			(str_store_string, s43, "@{s42"),
			#			(str_store_string, s42, "str_s43_s44"),
			
			#caravan from traded at...
			(else_try),
			(eq, ":destination", ":center"),
			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
			(party_slot_eq, ":origin", slot_party_temp_slot_1, 0),
			
			(party_set_slot, ":origin", slot_party_temp_slot_1, 1),
			(str_store_party_name, s40, ":origin"),
			(str_store_string, s44, "str_travellers_coming_from_s40_traded_here_s46"),
			(str_store_string, s43, "str_s42"),
			(str_store_string, s42, "str_s43_s44"),
			
			(val_add, ":trades", 1),
			
			#caravan from traded at...
			(try_end),
			
		(try_end),
		
		
		(try_begin),
			(le, ":trades", 2),
			(eq, ":road_attacks", 0),
			(store_current_hours, ":hours"),
			(lt, ":hours", 168),
			(str_store_string, s42, "str_it_is_still_early_in_the_caravan_season_so_we_have_seen_little_tradings42"),
		(else_try),
			(eq, ":trades", 0),
			(eq, ":road_attacks", 0),
			(str_store_string, s42, "str_there_has_been_very_little_trading_activity_here_recentlys42"),
		(else_try),
			(le, ":trades", 2),
			(eq, ":road_attacks", 0),
			(str_store_string, s42, "str_there_has_some_trading_activity_here_recently_but_not_enoughs42"),
		(else_try),
			(le, ":trades", 2),
			(le, ":road_attacks", 2),
			(str_store_string, s42, "str_there_has_some_trading_activity_here_recently_but_the_roads_are_dangerouss42"),
		(else_try),
			(ge, ":road_attacks", 3),
			(str_store_string, s42, "str_the_roads_around_here_are_very_dangerouss42"),
		(else_try),
			(ge, ":road_attacks", 1),
			(str_store_string, s42, "str_we_have_received_many_traders_in_town_here_although_there_is_some_danger_on_the_roadss42"),
		(else_try),
			(str_store_string, s42, "str_we_have_received_many_traders_in_town_heres42"),
		(try_end),
		
		#do safe roads
		(assign, ":unused_trade_route_found", 0),
		(try_for_range, ":trade_route_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
			(party_get_slot, ":trade_center", ":center", ":trade_route_slot"),
			(is_between, ":trade_center", centers_begin, centers_end),
			
			(party_slot_eq, ":trade_center", slot_party_temp_slot_1, 0),
			
			#		(party_get_slot, ":town_lord", ":trade_center", slot_town_lord),
			
			(str_store_party_name, s41, ":trade_center"),
			(try_begin),
			(eq, ":unused_trade_route_found", 1),
			(str_store_string, s44, "str_s44_s41"),
			(else_try),
			(str_store_string, s44, "str_s41"),
			(try_end),
			(assign, ":unused_trade_route_found", 1),
		(try_end),
		(try_begin),
			(eq, ":unused_trade_route_found", 1),
			(str_store_string, s47, "str_there_is_little_news_about_the_caravan_routes_to_the_towns_of_s44_and_nearby_parts_but_no_news_is_good_news_and_those_are_therefore_considered_safe"),
		(try_end),
		
		(assign, ":safe_village_road_found", 0),
		(try_for_range, ":village", villages_begin, villages_end),
			(party_slot_eq, ":village", slot_village_market_town, ":center"),
			(party_slot_eq, ":village", slot_party_temp_slot_1, 0),
			
			#		(party_get_slot, ":town_lord", ":village", slot_town_lord),
			(str_store_party_name, s41, ":village"),
			(try_begin),
			(eq, ":safe_village_road_found", 1),
			(str_store_string, s44, "str_s44_s41"),
			(else_try),
			(str_store_string, s44, "str_s41"),
			(try_end),
			(assign, ":safe_village_road_found", 1),
		(try_end),
		
		(try_begin),
			(eq, ":safe_village_road_found", 1),
			(eq, ":unused_trade_route_found", 1),
			(str_store_string, s47, "str_s47_also_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe"),
		(else_try),
			(eq, ":safe_village_road_found", 1),
			(str_store_string, s47, "str_however_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe"),
		(try_end),
		
		(str_store_string, s33, "str_we_have_shortages_of"),
		(assign, ":some_shortages_found", 0),
		(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
			(store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
			(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
			(party_get_slot, ":price", ":center", ":cur_good_price_slot"),
			(gt, ":price", 1100),
			
			(str_store_item_name, s34, ":cur_good"),
			(assign, reg1, ":price"),
			(str_store_string, s33, "str_s33_s34_reg1"),
			
			(assign, ":some_shortages_found", 1),
		(try_end),
		
		(try_begin),
			(eq, ":some_shortages_found", 0),
			(str_store_string, s32, "str_we_have_adequate_stores_of_all_commodities"),
		(else_try),
			(str_store_string, s32, "str_s33_and_some_other_commodities"),
		(try_end),
		
		(assign, reg0, ":last_bandit_party_found"),
		(assign, reg1, ":last_bandit_party_origin"),
		(assign, reg2, ":last_bandit_party_destination"),
		(assign, reg3, ":last_bandit_party_hours_ago"),
		
		
		])
		
		
	#script_find_total_prosperity_score
	# INPUT: center_no
	# OUTPUT: reg0 = total_prosperity_score
find_total_prosperity_score =	(
		"find_total_prosperity_score",
		[
		(store_script_param, ":center_no", 1),
		
		(try_begin), #":total_prosperity_score" changes between 10..100
			(is_between, ":center_no", walled_centers_begin, walled_centers_end),
			
			(party_get_slot, ":center_prosperity", ":center_no", slot_town_prosperity),
			(store_add, ":center_prosperity_add_200_div_10", ":center_prosperity", 200),
			(val_div, ":center_prosperity_add_200_div_10", 10),
			(try_begin),
			(is_between, ":center_no", towns_begin, towns_end),
			(store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 15),
			(else_try),
			(store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 5),
			(try_end),
			(assign, ":total_prosperity_score", ":this_center_score"),
			
			(try_for_range_backwards, ":village_no", villages_begin, villages_end),
			(party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
			
			(party_get_slot, ":village_prosperity", ":village_no", slot_town_prosperity),
			(store_add, ":village_prosperity_add_200_div_10", ":village_prosperity", 200),
			(val_div, ":village_prosperity_add_200_div_10", 10),
			(store_mul, ":this_village_score", ":village_prosperity_add_200_div_10", 5),
			
			(val_add, ":total_prosperity_score", ":this_village_score"),
			(try_end),
		(else_try),
			(party_get_slot, ":center_prosperity", ":center_no", slot_town_prosperity),
			(store_add, ":center_prosperity_add_200_div_10", ":center_prosperity", 200),
			(val_div, ":center_prosperity_add_200_div_10", 10),
			(store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 5),
			(assign, ":total_prosperity_score", ":this_center_score"),
		(try_end),
		(val_div, ":total_prosperity_score", 10),
		
		(assign, reg0, ":total_prosperity_score"),
	])
	