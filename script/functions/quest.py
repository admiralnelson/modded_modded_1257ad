from header import *

		# script_get_quest - combines old get_random_quest with new get_dynamic_quest
		
		# Input: arg1 = troop_no (of the troop in conversation), arg2 = min_importance (of the quest)
		# Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
get_quest = (
			"get_quest",
			[
				(store_script_param_1, ":giver_troop"),
				
				(store_character_level, ":player_level", "trp_player"),
				(store_troop_faction, ":giver_faction_no", ":giver_troop"),
				
				(troop_get_slot, ":giver_party_no", ":giver_troop", slot_troop_leaded_party),
				(troop_get_slot, ":giver_reputation", ":giver_troop", slot_lord_reputation_type),
				
				(assign, ":giver_center_no", -1),
				(try_begin),
					(gt, ":giver_party_no", 0),
					(party_get_attached_to, ":giver_center_no", ":giver_party_no"),
				(else_try),
					(is_between, "$g_encountered_party", centers_begin, centers_end),
					(assign, ":giver_center_no", "$g_encountered_party"),
				(try_end),
				
				(try_begin),
					(troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
					(try_begin),
						(ge, "$g_talk_troop_faction_relation", 0),
						(assign, ":quests_begin", lord_quests_begin),
						(assign, ":quests_end", lord_quests_end),
						(assign, ":quests_begin_2", lord_quests_begin_2),
						(assign, ":quests_end_2", lord_quests_end_2),
					(else_try),
						(assign, ":quests_begin", enemy_lord_quests_begin),
						(assign, ":quests_end", enemy_lord_quests_end),
						(assign, ":quests_begin_2", 0),
						(assign, ":quests_end_2", 0),
					(try_end),
				(else_try),
					(is_between, ":giver_troop", village_elders_begin, village_elders_end),
					(assign, ":quests_begin", village_elder_quests_begin),
					(assign, ":quests_end", village_elder_quests_end),
					(assign, ":quests_begin_2", village_elder_quests_begin_2),
					(assign, ":quests_end_2", village_elder_quests_end_2),
				(else_try),
					(is_between, ":giver_troop", mayors_begin, mayors_end),
					(assign, ":quests_begin", mayor_quests_begin),
					(assign, ":quests_end", mayor_quests_end),
					(assign, ":quests_begin_2", mayor_quests_begin_2),
					(assign, ":quests_end_2", mayor_quests_end_2),
				(else_try),
					(assign, ":quests_begin", lady_quests_begin),
					(assign, ":quests_end", lady_quests_end),
					(assign, ":quests_begin_2", lady_quests_begin_2),
					(assign, ":quests_end_2", lady_quests_end_2),
				(try_end),
				
				(assign, ":result", -1),
				(assign, ":quest_target_troop", -1),
				(assign, ":quest_target_center", -1),
				(assign, ":quest_target_faction", -1),
				(assign, ":quest_object_faction", -1),
				(assign, ":quest_object_troop", -1),
				(assign, ":quest_object_center", -1),
				(assign, ":quest_target_party", -1),
				(assign, ":quest_target_party_template", -1),
				(assign, ":quest_target_amount", -1),
				(assign, ":quest_target_dna", -1),
				(assign, ":quest_target_item", -1),
				(assign, ":quest_importance", 1),
				(assign, ":quest_xp_reward", 0),
				(assign, ":quest_gold_reward", 0),
				(assign, ":quest_convince_value", 0),
				(assign, ":quest_expiration_days", 0),
				(assign, ":quest_dont_give_again_period", 0),
				
				(try_begin), #get dynamic quest is a separate script, so that we can scan a number of different troops at once for it
					(call_script, "script_get_dynamic_quest", "$g_talk_troop"),
					
					(assign, ":result", reg0),
					(assign, ":relevant_troop", reg1),
					(assign, ":relevant_party", reg2),
					(assign, ":relevant_faction", reg3),
					
					#GUILDMASTER QUESTS
					(try_begin),
						(eq, ":result", "qst_track_down_bandits"),
						(assign, ":quest_target_party", ":relevant_party"),
						(assign ,":quest_expiration_days", 60),
						(assign, ":quest_xp_reward", 1000),
						(assign, ":quest_gold_reward", 1000),
						
					(else_try),
						(eq, ":result", "qst_retaliate_for_border_incident"),
						(assign, ":quest_target_troop", ":relevant_troop"),
						(assign, ":quest_target_faction", ":relevant_faction"),
						
						(assign ,":quest_expiration_days", 30),
						(assign, ":quest_xp_reward", 1000),
						(assign, ":quest_gold_reward", 1000),
						
						#KINGDOM LORD QUESTS
					(else_try),
						(eq, ":result", "qst_cause_provocation"),
						(assign, ":quest_target_faction", ":relevant_faction"),
						(assign, ":quest_expiration_days", 30),
						(assign, ":quest_dont_give_again_period", 100),
						(assign, ":quest_xp_reward", 1000),
						(assign, ":quest_gold_reward", 1000),
						
					(else_try),
						(eq, ":result", "qst_destroy_bandit_lair"),
						(assign, ":quest_target_party", ":relevant_party"),
						(assign ,":quest_expiration_days", 60),
						(assign, ":quest_xp_reward", 3000),
						(assign, ":quest_gold_reward", 1500),
						
						#KINGDOM LADY OR KINGDOM HERO QUESTS
					(else_try),
						(eq, ":result", "qst_rescue_prisoner"),
						(assign, ":quest_target_troop", ":relevant_troop"),
						(assign, ":quest_target_center", ":relevant_party"),
						
						(assign, ":quest_expiration_days", 30),
						(assign, ":quest_dont_give_again_period", 5),
						(assign, ":quest_xp_reward", 1500),
						(assign, ":quest_gold_reward", 3000),
					(try_end),
				(try_end),
				
				#no dynamic quest available
				(try_begin),
					(eq, ":result", -1),
					
					(try_for_range, ":unused", 0, 20), #Repeat trial twenty times
						(eq, ":result", -1),
						(assign, ":quest_target_troop", -1),
						(assign, ":quest_target_center", -1),
						(assign, ":quest_target_faction", -1),
						(assign, ":quest_object_faction", -1),
						(assign, ":quest_object_troop", -1),
						(assign, ":quest_object_center", -1),
						(assign, ":quest_target_party", -1),
						(assign, ":quest_target_party_template", -1),
						(assign, ":quest_target_amount", -1),
						(assign, ":quest_target_dna", -1),
						(assign, ":quest_target_item", -1),
						(assign, ":quest_importance", 1),
						(assign, ":quest_xp_reward", 0),
						(assign, ":quest_gold_reward", 0),
						(assign, ":quest_convince_value", 0),
						(assign, ":quest_expiration_days", 0),
						(assign, ":quest_dont_give_again_period", 0),
						
						(store_sub, ":num_possible_old_quests", ":quests_end", ":quests_begin"),
						(store_sub, ":num_possible_new_quests", ":quests_end_2", ":quests_begin_2"),
						(store_add, ":num_possible_total_quests", ":num_possible_old_quests", ":num_possible_new_quests"),
						
						(store_random_in_range, ":quest_no", 0, ":num_possible_total_quests"),
						(try_begin),
							(lt, ":quest_no", ":num_possible_old_quests"),
							(store_random_in_range, ":quest_no", ":quests_begin", ":quests_end"),
						(else_try),
							(store_random_in_range, ":quest_no", ":quests_begin_2", ":quests_end_2"),
						(try_end),
						
						#TODO: Remove this when test is done
						#       (assign, ":quest_no", "qst_meet_spy_in_enemy_town"),
						#TODO: Remove this when test is done end
						(neg|check_quest_active,":quest_no"),
						(neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
						(try_begin),
							# Village Elder quests
							(eq, ":quest_no", "qst_deliver_grain"),
							(try_begin),
								(is_between, ":giver_center_no", villages_begin, villages_end),
								#The quest giver is the village elder
								(call_script, "script_get_troop_item_amount", ":giver_troop", "itm_grain"),
								(eq, reg0, 0),
								(neg|party_slot_ge, ":giver_center_no", slot_town_prosperity, 40),
								(assign, ":quest_target_center", ":giver_center_no"),
								(store_random_in_range, ":quest_target_amount", 4, 8),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 20),
								(assign, ":result", ":quest_no"),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_deliver_cattle"),
							(try_begin),
								(is_between, ":giver_center_no", villages_begin, villages_end),
								#The quest giver is the village elder
								(party_get_slot, ":num_cattle", ":giver_center_no", slot_village_number_of_cattle),
								(lt, ":num_cattle", 50),
								(assign, ":quest_target_center", ":giver_center_no"),
								(store_random_in_range, ":quest_target_amount", 5, 10),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 20),
								(assign, ":result", ":quest_no"),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_train_peasants_against_bandits"),
							(try_begin),
								(is_between, ":giver_center_no", villages_begin, villages_end),
								#The quest giver is the village elder
								(store_skill_level, ":player_trainer", "skl_trainer", "trp_player"),
								(gt, ":player_trainer", 0),
								(store_random_in_range, ":quest_target_amount", 5, 8),
								(assign, ":quest_target_center", ":giver_center_no"),
								(assign, ":quest_expiration_days", 20),
								(assign, ":quest_dont_give_again_period", 40),
								(assign, ":result", ":quest_no"),
							(try_end),
						(else_try),
							# Mayor quests
							(eq, ":quest_no", "qst_escort_merchant_caravan"),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(store_random_party_in_range, ":quest_target_center", towns_begin, towns_end),
							(store_distance_to_party_from_party, ":dist", ":giver_center_no",":quest_target_center"),
							(assign, ":quest_gold_reward", ":dist"),
							# rafi 15 denars/unit traveled
							(store_mul, ":quest_gold_reward", ":dist", 15),
							# (val_add, ":quest_gold_reward", 25),
							# (val_mul, ":quest_gold_reward", 25),
							# (val_div, ":quest_gold_reward", 20),
							(store_random_in_range, ":quest_target_amount", 6, 12),
							(assign, "$escort_merchant_caravan_mode", 0),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_deliver_wine"),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(store_random_party_in_range, ":quest_target_center", towns_begin, towns_end),
							(store_random_in_range, ":random_no", 0, 2),
							(try_begin),
								(eq, ":random_no", 0),
								(assign, ":quest_target_item", "itm_quest_wine"),
							(else_try),
								(assign, ":quest_target_item", "itm_quest_ale"),
							(try_end),
							(store_random_in_range, ":quest_target_amount", 6, 12),
							(store_distance_to_party_from_party, ":dist", ":giver_center_no",":quest_target_center"),
							(assign, ":quest_gold_reward", ":dist"),
							# rafi
							(val_mul, ":quest_gold_reward", 10), # 10 denars per unit traveled
							# end rafi
							#(val_add, ":quest_gold_reward", 2),
							#(assign, ":multiplier", 5),
							#(val_add, ":multiplier", ":quest_target_amount"),
							#(val_mul, ":quest_gold_reward", ":multiplier"),
							#(val_div, ":quest_gold_reward", 100),
							#(val_mul, ":quest_gold_reward", 10),
							(store_item_value,"$qst_deliver_wine_debt",":quest_target_item"),
							(val_mul,"$qst_deliver_wine_debt",":quest_target_amount"),
							(val_mul,"$qst_deliver_wine_debt", 6),
							(val_div,"$qst_deliver_wine_debt",5),
							(assign, ":quest_expiration_days", 7),
							(assign, ":quest_dont_give_again_period", 20),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_troublesome_bandits"),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(store_character_level, ":quest_gold_reward", "trp_player"),
							(val_add, ":quest_gold_reward", 20),
							(val_mul, ":quest_gold_reward", 35),
							(val_div, ":quest_gold_reward",100),
							(val_mul, ":quest_gold_reward", 10),
							(assign, ":quest_expiration_days", 30),
							(assign, ":quest_dont_give_again_period", 30),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_kidnapped_girl"),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							# rafi
							(assign, ":i_max", 99),
							(try_for_range, ":unused", 0, ":i_max"),
								(store_random_in_range, ":quest_target_center", villages_begin, villages_end),
								(store_distance_to_party_from_party, ":dist", ":giver_center_no", ":quest_target_center"),
								(le, ":dist", 50),
								(assign, ":i_max", 0),
							(try_end),
							(assign, reg21, ":dist"),
							(str_store_party_name, s21, ":quest_target_center"),
							(display_message, "@DEBUG -- {s21} distance {reg21}"),
							# rafi
							#(store_random_in_range, ":quest_target_center", villages_begin, villages_end),
							(store_character_level, ":quest_target_amount"),
							(val_add, ":quest_target_amount", 15),
							(store_distance_to_party_from_party, ":dist", ":giver_center_no", ":quest_target_center"),
							(val_add, ":dist", 15),
							(val_mul, ":dist", 2),
							(val_mul, ":quest_target_amount", ":dist"),
							(val_div, ":quest_target_amount",100),
							(val_mul, ":quest_target_amount",10),
							(assign, ":quest_gold_reward", ":quest_target_amount"),
							(val_div, ":quest_gold_reward", 40),
							(val_mul, ":quest_gold_reward", 10),
							(assign, ":quest_expiration_days", 15),
							(assign, ":quest_dont_give_again_period", 30),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_move_cattle_herd"),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(call_script, "script_cf_select_random_town_at_peace_with_faction", ":giver_faction_no"),
							(neq, ":giver_center_no", reg0),
							(assign, ":quest_target_center", reg0),
							(store_distance_to_party_from_party, ":dist",":giver_center_no",":quest_target_center"),
							# rafi 10 denars per unit traveled
							(store_mul, ":quest_gold_reward", ":dist", 10),
							#(assign, ":quest_gold_reward", ":dist"),
							# (val_add, ":quest_gold_reward", 25),
							# (val_mul, ":quest_gold_reward", 50),
							# (val_div, ":quest_gold_reward", 20),
							(assign, ":quest_expiration_days", 30),
							(assign, ":quest_dont_give_again_period", 20),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_persuade_lords_to_make_peace"),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(store_faction_of_party, ":cur_object_faction", ":giver_center_no"),
							(call_script, "script_cf_faction_get_random_enemy_faction", ":cur_object_faction"),
							(assign, ":cur_target_faction", reg0),
							(call_script, "script_cf_get_random_lord_except_king_with_faction", ":cur_object_faction"),
							(assign, ":cur_object_troop", reg0),
							(this_or_next|troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_quarrelsome),
							(this_or_next|troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_selfrighteous),
							(this_or_next|troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_martial),
							(troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_debauched),
							
							(call_script, "script_cf_get_random_lord_except_king_with_faction", ":cur_target_faction"),
							(assign, ":quest_target_troop", reg0),
							(this_or_next|troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_quarrelsome),
							(this_or_next|troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_selfrighteous),
							(this_or_next|troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_martial),
							(troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_debauched),
							
							(assign, ":quest_object_troop", ":cur_object_troop"),
							(assign, ":quest_target_faction", ":cur_target_faction"),
							(assign, ":quest_object_faction", ":cur_object_faction"),
							(assign, ":quest_gold_reward", 12000),
							(assign, ":quest_convince_value", 7000),
							(assign, ":quest_expiration_days", 30),
							(assign, ":quest_dont_give_again_period", 100),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_deal_with_looters"),
							(is_between, ":player_level", 0, 15),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(store_faction_of_party, ":cur_object_faction", ":giver_center_no"),
							(store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters"),
							(party_template_set_slot,"pt_looters",slot_party_template_num_killed,":num_looters_destroyed"),
							(quest_set_slot,":quest_no",slot_quest_current_state,0),
							(quest_set_slot,":quest_no",slot_quest_target_party_template,"pt_looters"),
							(assign, ":quest_gold_reward", 500),
							(assign, ":quest_xp_reward", 500),
							(assign, ":quest_expiration_days", 20),
							(assign, ":quest_dont_give_again_period", 30),
							(assign, ":result", ":quest_no"),
						(else_try),
							(eq, ":quest_no", "qst_deal_with_night_bandits"),
							(is_between, ":player_level", 0, 15),
							(is_between, ":giver_center_no", centers_begin, centers_end),
							(party_slot_ge, ":giver_center_no", slot_center_has_bandits, 1),
							(assign, ":quest_target_center", ":giver_center_no"),
							(assign, ":quest_expiration_days", 4),
							(assign, ":quest_dont_give_again_period", 15),
							(assign, ":result", ":quest_no"),
						(else_try),
							# Lady quests
							(eq, ":quest_no", "qst_rescue_lord_by_replace"),
							(eq, 1, 0),
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(is_between, ":player_level", 5, 25),
								
								(assign, ":prisoner_relative", -1),
								
								(try_begin),
									(troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_father), #get giver_troop's father
									(gt, ":cur_target_troop", 0), #if giver_troop has a father as a troop in game
									(troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0), #if giver_troop's father is in a prison
									(assign, ":prisoner_relative", ":cur_target_troop"),
								(try_end),
								
								(try_begin),
									(eq, ":prisoner_relative", -1), #if giver_troop has no father or giver_troop's father is not in prison.
									(troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_spouse), #get giver_troop's spouse
									(gt, ":cur_target_troop", 0), #if giver_troop has a spouse as a troop in game
									(troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0), #if giver_troop's spouse is in a prison
									(assign, ":prisoner_relative", ":cur_target_troop"),
								(try_end),
								
								(try_begin),
									(eq, ":prisoner_relative", -1), #if ((giver_troop has no father) or (giver_troop's father is not in prison)) and ((giver_troop has no spouse) or (giver_troop's spouse is not in prison)).
									(troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_guardian), #get giver_troop's spouse
									(gt, ":cur_target_troop", 0), #if giver_troop has a guardian as a troop in game
									(troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0), #if giver_troop's guardian is in a prison
									(assign, ":prisoner_relative", ":cur_target_troop"),
								(try_end),
								
								(try_begin),
									(eq, "$cheat_mode", 1),
									(assign, reg0, ":prisoner_relative"),
									(display_message, "str_prisoner_relative_is_reg0"),
								(try_end),
								
								(gt, ":prisoner_relative", -1),
								#(changed 2) no need to this anymore (troop_slot_ge, ":prisoner_relative", slot_troop_prisoner_of_party, 0),
								(call_script, "script_search_troop_prisoner_of_party", ":prisoner_relative"),
								(assign, ":cur_target_center", reg0),
								
								#(changed 3) no need to check only towns anymore (is_between, ":cur_target_center", towns_begin, towns_end),#Skip if he is not in a town
								(is_between, ":cur_target_center", walled_centers_begin, walled_centers_end), #Skip if he is not in a walled center
								
								(assign, ":quest_target_center", ":cur_target_center"),
								(assign, ":quest_target_troop", ":prisoner_relative"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 73),
								(assign, ":result", ":quest_no"),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_deliver_message_to_prisoner_lord"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(is_between, ":player_level", 5, 25),
								(troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_father),
								(try_begin),
									(eq, ":cur_target_troop", 0),
									(troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_spouse),
								(try_end),
								#(troop_slot_eq, ":cur_target_troop", slot_troop_is_prisoner, 1),#Skip if the lady's father/husband is not in prison
								(gt, ":cur_target_troop", -1),
								(troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0),
								(call_script, "script_search_troop_prisoner_of_party", ":cur_target_troop"),
								(assign, ":cur_target_center", reg0),
								(is_between, ":cur_target_center", towns_begin, towns_end),#Skip if he is not in a town
								(assign, ":quest_target_center", ":cur_target_center"),
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 30),
								(assign, ":result", ":quest_no"),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_duel_for_lady"),
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(ge, ":player_level", 10),
								(call_script, "script_cf_troop_get_random_enemy_troop_with_occupation", ":giver_troop", slto_kingdom_hero),#Can fail
								(assign, ":cur_target_troop", reg0),
								(neg|troop_slot_eq, ":giver_troop", slot_troop_spouse, ":cur_target_troop"), #must not be in the family
								(neg|troop_slot_eq, ":giver_troop", slot_troop_father, ":cur_target_troop"),
								(neg|troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0),
								(troop_slot_ge, ":cur_target_troop", slot_troop_leaded_party, 0),
								(neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_goodnatured),
								(neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_upstanding),
								(neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_martial),
								
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 50),
								(assign, ":result", ":quest_no"),
							(try_end),
							# Enemy Lord Quests
						(else_try),
							(eq, ":quest_no", "qst_lend_surgeon"),
							(try_begin),
								(eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)
								(neq, ":giver_reputation", lrep_quarrelsome),
								(neq, ":giver_reputation", lrep_debauched),
								(assign, ":max_surgery_level", 0),
								(assign, ":best_surgeon", -1),
								(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
								(try_for_range, ":i_stack", 1, ":num_stacks"),
									(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
									(troop_is_hero, ":stack_troop"),
									(store_skill_level, ":cur_surgery_skill", skl_surgery, ":stack_troop"),
									(gt, ":cur_surgery_skill", ":max_surgery_level"),
									(assign, ":max_surgery_level", ":cur_surgery_skill"),
									(assign, ":best_surgeon", ":stack_troop"),
								(try_end),
								
								(store_character_level, ":cur_level", "trp_player"),
								(assign, ":required_skill", 5),
								(val_div, ":cur_level", 10),
								(val_add, ":required_skill", ":cur_level"),
								(ge, ":max_surgery_level", ":required_skill"), #Skip if party skill level is less than the required value
								
								(assign, ":quest_object_troop", ":best_surgeon"),
								(assign, ":quest_importance", 1),
								(assign, ":quest_xp_reward", 10),
								(assign, ":quest_gold_reward", 10),
								(assign, ":quest_dont_give_again_period", 50),
								(assign, ":result", ":quest_no"),
							(try_end),
							# Lord Quests
						(else_try),
							(eq, ":quest_no", "qst_meet_spy_in_enemy_town"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(eq, "$players_kingdom", ":giver_faction_no"),
								(neq, ":giver_reputation", lrep_goodnatured),
								(neq, ":giver_reputation", lrep_martial),
								
								(call_script, "script_troop_get_player_relation", ":giver_troop"),
								(assign, ":giver_relation", reg0),
								(gt, ":giver_relation", 3),
								(call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),
								(assign, ":enemy_faction", reg0),
								(store_relation, ":reln", ":enemy_faction", "fac_player_supporters_faction"),
								(lt, ":reln", 0),
								(call_script, "script_cf_select_random_town_with_faction", ":enemy_faction"),
								(assign, ":cur_target_center", reg0),
								#Just to make sure that there is a free walker
								(call_script, "script_cf_center_get_free_walker", ":cur_target_center"),
								(assign, ":quest_target_center", ":cur_target_center"),
								(store_random_in_range, ":quest_target_amount", secret_signs_begin, secret_signs_end),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_gold_reward", 500),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 50),
								(quest_set_slot, "qst_meet_spy_in_enemy_town", slot_quest_gold_reward, 500),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_raid_caravan_to_start_war"),
							(eq, 1, 0), #disable this as a random quest
							
							(try_begin),
								(eq, "$players_kingdom", ":giver_faction_no"),
								(this_or_next|eq, ":giver_reputation", lrep_cunning),
								(this_or_next|eq, ":giver_reputation", lrep_quarrelsome),
								(             eq, ":giver_reputation", lrep_debauched),
								(gt, ":player_level", 10),
								(eq, 1, 0), #disable this as a random quest
								
								(neg|faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),#Can not take the quest from the king
								(call_script, "script_cf_faction_get_random_friendly_faction", ":giver_faction_no"),#Can fail
								(assign, ":quest_target_faction", reg0),
								(store_troop_faction, ":quest_object_faction", ":giver_troop"),
								(assign, ":quest_target_party_template", "pt_kingdom_caravan_party"),
								(assign, ":quest_target_amount", 2),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 100),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_deliver_message"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(lt, ":player_level", 20),
								(neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
								(call_script, "script_cf_get_random_lord_in_a_center_with_faction", ":giver_faction_no"),#Can fail
								(assign, ":cur_target_troop", reg0),
								(neq, ":cur_target_troop", ":giver_troop"),#Skip himself
								(call_script, "script_get_troop_attached_party", ":cur_target_troop"),
								(assign, ":cur_target_center", reg0),#cur_target_center will definitely be a valid center
								(neq,":giver_center_no", ":cur_target_center"),#Skip current center
								
								(assign, ":quest_target_center", ":cur_target_center"),
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(assign, ":quest_xp_reward", 30),
								(assign, ":quest_gold_reward", 40),
								(assign, ":quest_dont_give_again_period", 10),
								
								(assign, ":result", ":quest_no"),
								
								(assign, ":quest_expiration_days", 30),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_escort_lady"),
							(try_begin),
							(ge, "$g_talk_troop_faction_relation", 0),
							(ge, ":player_level", 10),

				(ge, ":giver_troop", 0), #skip troops without fathers in range				

				(assign, ":cur_object_troop", -1),
								(try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
					(troop_slot_eq, ":lady", slot_troop_father, ":giver_troop"),
					(assign, ":cur_object_troop", ":lady"),
				(try_end),

				(ge, ":cur_object_troop", 0),
							
				(troop_get_slot, ":giver_troop_confirm", ":cur_object_troop", slot_troop_father),  # just to make sure
				(eq, ":giver_troop", ":giver_troop_confirm"), # just to make sure

							(store_random_in_range, ":random_no", 0, 2),
							(try_begin),
								(eq, ":random_no", 0),
								(troop_get_slot, ":cur_object_troop_2", ":giver_troop", slot_troop_spouse),
					(is_between, ":cur_object_troop_2", kingdom_ladies_begin, kingdom_ladies_end),
					(troop_get_slot, ":giver_troop_confirm", ":cur_object_troop_2", slot_troop_spouse),  # just to make sure
					(eq, ":giver_troop", ":giver_troop_confirm"), # just to make sure
								(assign, ":cur_object_troop", ":cur_object_troop_2"),
							(try_end),
							(gt, ":cur_object_troop", 0),#Skip lords without a lady
							(troop_get_type, ":cur_troop_gender", ":cur_object_troop"),
							(eq, ":cur_troop_gender", 1),#Skip if it is not female
							(gt, ":giver_center_no", 0),#Skip if lord is outside the center
							(troop_slot_eq, ":cur_object_troop", slot_troop_cur_center, ":giver_center_no"),#Skip if the lady is not at the same center
							(call_script, "script_cf_select_random_town_with_faction", ":giver_faction_no"),#Can fail
							(assign, ":cur_target_center", reg0),
							(neq, ":cur_target_center", ":giver_center_no"),
							(hero_can_join),#Skip if player has no available slots

							(assign, ":quest_object_troop", ":cur_object_troop"),
							(assign, ":quest_target_center", ":cur_target_center"),
							(assign, ":quest_expiration_days", 20),
							(assign, ":quest_dont_give_again_period", 30),
							(assign, ":result", ":quest_no"),
						(try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_hunt_down_raiders"),
							##          (try_begin),
							##            (gt, ":player_level", 10),
							##            (faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),
							##            (call_script, "script_cf_select_random_town_with_faction", ":giver_faction_no"),#Can fail
							##            (assign, ":cur_object_center", reg0),
							##            (neq, ":cur_object_center", ":giver_center_no"),#Skip current center
							##            (call_script, "script_get_random_enemy_center", ":giver_party_no"),
							##            (assign, ":cur_target_center", reg0),
							##            (ge, ":cur_target_center", 0),
							##            (store_faction_of_party, ":cur_target_faction", ":cur_target_center"),
							##            (is_between,  ":cur_target_faction", kingdoms_begin, kingdoms_end),
							##
							##            (assign, ":quest_object_center", ":cur_object_center"),
							##            (assign, ":quest_target_center", ":cur_target_center"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 1500),
							##            (assign, ":quest_gold_reward", 1000),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_bring_back_deserters"),
							##          (try_begin),
							##            (gt, ":player_level", 5),
							##            (faction_get_slot, ":cur_target_party_template", ":giver_faction_no", slot_faction_deserter_party_template),
							##            (faction_get_slot, ":cur_target_troop", ":giver_faction_no", slot_faction_deserter_troop),
							##            (gt, ":cur_target_party_template", 0),#Skip factions with no deserter party templates
							##            (store_num_parties_of_template, ":num_deserters", ":cur_target_party_template"),
							##            (ge, ":num_deserters", 2),#Skip if there are less than 2 active deserter parties
							##
							##            (assign, ":quest_target_troop", ":cur_target_troop"),
							##            (assign, ":quest_target_party_template", ":cur_target_party_template"),
							##            (assign, ":quest_target_amount", 5),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 500),
							##            (assign, ":quest_gold_reward", 300),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_deliver_supply_to_center_under_siege"),
							##          (try_begin),
							##            (gt, ":player_level", 10),
							##            (gt, ":giver_center_no", 0),#Skip if lord is outside the center
							##            (call_script, "script_cf_get_random_siege_location_with_faction", ":giver_faction_no"),#Can fail
							##            (assign, ":quest_target_center", reg0),
							##            (assign, ":quest_target_amount", 10),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 500),
							##            (assign, ":quest_gold_reward", 300),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_rescue_lady_under_siege"),
							##          (try_begin),
							##            (gt, ":player_level", 15),
							##            (troop_get_slot, ":cur_object_troop", ":giver_troop", slot_troop_daughter),
							##            (store_random_in_range, ":random_no", 0, 2),
							##            (try_begin),
							##              (this_or_next|eq,  ":cur_object_troop", 0),
							##              (eq, ":random_no", 0),
							##              (troop_get_slot, ":cur_object_troop_2", ":giver_troop", slot_troop_spouse),
							##              (gt, ":cur_object_troop_2", 0),
							##              (assign, ":cur_object_troop", ":cur_object_troop_2"),
							##            (try_end),
							##            (gt, ":cur_object_troop", 0),#Skip lords without a lady
							##            (troop_get_type, ":cur_troop_gender", ":cur_object_troop"),
							##            (eq, ":cur_troop_gender", 1),#Skip if lady is not female
							##            (troop_get_slot, ":cur_target_center", ":cur_object_troop", slot_troop_cur_center),
							##            (is_between, ":cur_target_center", centers_begin, centers_end),#Skip if she is not in a center
							##            (neq,":giver_center_no", ":cur_target_center"),#Skip current center
							##            (call_script, "script_cf_get_random_siege_location_with_faction", ":giver_faction_no"),#Can fail
							##            (assign, ":cur_target_center", reg0),
							##            (troop_set_slot, ":cur_object_troop", slot_troop_cur_center, ":cur_target_center"),#Move lady to the siege location
							##            (assign, ":quest_object_troop", ":cur_object_troop"),
							##            (assign, ":quest_target_center", ":cur_target_center"),
							##            (assign, ":quest_target_troop", ":giver_troop"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 200),
							##            (assign, ":quest_gold_reward", 750),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_deliver_message_to_lover"),
							##          (try_begin),
							##            (is_between, ":player_level", 5, 30),
							##            (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_lover),
							##            (gt, ":cur_target_troop", 0),#Skip lords without a lover
							##            (troop_get_slot, ":cur_target_center", ":cur_target_troop", slot_troop_cur_center),
							##            (is_between, ":cur_target_center", centers_begin, centers_end),#Skip if she is not in a center
							##            (neq,":giver_center_no", ":cur_target_center"),#Skip current center
							##            (assign, ":quest_target_troop", ":cur_target_troop"),
							##            (assign, ":quest_target_center", ":cur_target_center"),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_bring_reinforcements_to_siege"),
							##          (try_begin),
							##            (gt, ":player_level", 10),
							##            (call_script, "script_cf_get_random_siege_location_with_attacker_faction", ":giver_faction_no"),#Can fail
							##            (assign, ":cur_target_center", reg0),
							##            (store_random_in_range, ":random_no", 5, 11),
							##            (troops_can_join, ":random_no"),#Skip if the player doesn't have enough room
							##            (call_script, "script_cf_get_number_of_random_troops_from_party", ":giver_party_no", ":random_no"),#Can fail
							##            (assign, ":cur_object_troop", reg0),
							##            (party_get_battle_opponent, ":cur_target_party", ":cur_target_center"),
							##            (party_get_num_companion_stacks, ":num_stacks", ":cur_target_party"),
							##            (gt, ":num_stacks", 0),#Skip if the besieger party has no troops
							##            (party_stack_get_troop_id, ":cur_target_troop", ":cur_target_party", 0),
							##            (troop_is_hero, ":cur_target_troop"),#Skip if the besieger party has no heroes
							##            (neq, ":cur_target_troop", ":giver_troop"),#Skip if the quest giver is the same troop
							##            (assign, ":quest_target_troop", ":cur_target_troop"),
							##            (assign, ":quest_object_troop", ":cur_object_troop"),
							##            (assign, ":quest_target_party", ":cur_target_party"),
							##            (assign, ":quest_target_center", ":cur_target_center"),
							##            (assign, ":quest_target_amount", ":random_no"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 400),
							##            (assign, ":quest_gold_reward", 200),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
						(else_try),
							(eq, ":quest_no", "qst_deliver_message_to_enemy_lord"),
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(is_between, ":player_level", 5,25),
								(call_script, "script_cf_get_random_lord_from_another_faction_in_a_center", ":giver_faction_no"),#Can fail
								(assign, ":cur_target_troop", reg0),
								(call_script, "script_get_troop_attached_party", ":cur_target_troop"),
								(assign, ":quest_target_center", reg0),#quest_target_center will definitely be a valid center
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(assign, ":quest_importance", 1),
								(assign, ":quest_xp_reward", 200),
								(assign, ":quest_gold_reward", 0),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 40),
							(try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_bring_prisoners_to_enemy"),
							##          (try_begin),
							##            (gt, ":player_level", 10),
							##            (is_between, ":giver_center_no", centers_begin, centers_end),#Skip if the quest giver is not at a center
							##            (store_random_in_range, ":random_no", 5, 11),
							##            (troops_can_join_as_prisoner, ":random_no"),#Skip if the player doesn't have enough room
							##            (call_script, "script_get_random_enemy_town", ":giver_center_no"),
							##            (assign, ":cur_target_center", reg0),
							##            (ge, ":cur_target_center", 0),#Skip if there are no enemy towns
							##            (store_faction_of_party, ":cur_target_faction", ":cur_target_center"),
							##            (faction_get_slot, ":cur_object_troop", ":cur_target_faction", slot_faction_tier_5_troop),
							##            (assign, ":quest_target_center", ":cur_target_center"),
							##            (assign, ":quest_object_troop", ":cur_object_troop"),
							##            (assign, ":quest_target_amount", ":random_no"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 300),
							##            (assign, ":quest_gold_reward", 200),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
						(else_try),
							(eq, ":quest_no", "qst_deal_with_bandits_at_lords_village"),
							(try_begin),
								(neq, ":giver_reputation", lrep_debauched),
								(neq, ":giver_reputation", lrep_quarrelsome),
								(ge, "$g_talk_troop_faction_relation", 0),
								(assign, ":end_cond", villages_end),
								(assign, ":cur_target_center", -1),
								(try_for_range, ":cur_village", villages_begin, ":end_cond"),
									(party_slot_eq, ":cur_village", slot_town_lord, ":giver_troop"),
									(party_slot_eq, ":cur_village", slot_village_infested_by_bandits, 1),
									(party_slot_eq, ":cur_village", slot_village_state, svs_normal),
									(assign, ":cur_target_center", ":cur_village"),
									(assign, ":end_cond", 0),
								(try_end),
								(ge, ":cur_target_center", 0),
								(neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
								(assign, ":quest_target_center", ":cur_target_center"),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 30),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_raise_troops"),
							(try_begin),
								(neq, ":giver_reputation", lrep_martial),
								(neq, ":giver_faction_no", "fac_player_supporters_faction"), #we need tier_1_troop a valid value
								(ge, "$g_talk_troop_faction_relation", 0),
								(store_character_level, ":cur_level", "trp_player"),
								(gt, ":cur_level", 5),
								(troop_slot_ge, "trp_player", slot_troop_renown, 100),
								
								(store_random_in_range, ":quest_target_amount", 5, 8),
								(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
								(le, ":quest_target_amount", ":free_capacity"),
								(faction_get_slot, ":quest_object_troop", ":giver_faction_no", slot_faction_tier_1_troop),
								(store_random_in_range, ":level_up", 20, 40),
								(val_add, ":level_up", ":cur_level"),
								(val_div, ":level_up", 10),
								
								(store_mul, ":quest_gold_reward", ":quest_target_amount", 10),
								
								(assign, ":quest_target_troop", ":quest_object_troop"),
								(try_for_range, ":unused", 0, ":level_up"),
									(troop_get_upgrade_troop, ":level_up_troop", ":quest_target_troop", 0),
									(gt, ":level_up_troop", 0),
									(assign, ":quest_target_troop", ":level_up_troop"),
									(val_mul, ":quest_gold_reward", ":quest_gold_reward", 7),
									(val_div, ":quest_gold_reward", ":quest_gold_reward", 4),
								(try_end),
								
								(assign, ":quest_xp_reward", ":quest_gold_reward"),
								(val_mul, ":quest_xp_reward", 3),
								(val_div, ":quest_xp_reward", 10),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 120),
								(assign, ":quest_dont_give_again_period", 15),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_collect_taxes"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(neq, ":giver_reputation", lrep_goodnatured),
								(neq, ":giver_reputation", lrep_upstanding),
								(ge, "$g_talk_troop_faction_relation", 0),
								(call_script, "script_cf_troop_get_random_leaded_town_or_village_except_center", ":giver_troop", ":giver_center_no"),
								(assign, ":quest_target_center", reg0),
								(assign, ":quest_importance", 1),
								(assign, ":quest_gold_reward", 0),
								(assign, ":quest_xp_reward", 100),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 50),
								(assign, ":quest_dont_give_again_period", 20),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_hunt_down_fugitive"),
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(call_script, "script_cf_select_random_village_with_faction", ":giver_faction_no"),
								(assign, ":quest_target_center", reg0),
								(store_random_in_range, ":quest_target_dna", 0, 1000000),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 30),
							(try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_capture_messenger"),
							##          (try_begin),
							##            (call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),
							##            (assign, ":cur_target_faction", reg0),
							##            (faction_get_slot, ":cur_target_troop", ":cur_target_faction", slot_faction_messenger_troop),
							##            (gt, ":cur_target_troop", 0),#Checking the validiy of cur_target_troop
							##            (store_num_parties_destroyed_by_player, ":quest_target_amount", "pt_messenger_party"),
							##
							##            (assign, ":quest_target_troop", ":cur_target_troop"),
							##            (assign, ":quest_target_party_template", ":cur_target_party_template"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 700),
							##            (assign, ":quest_gold_reward", 400),
							##            (assign, ":result", ":quest_no"),
							##          (try_end),
						(else_try),
							(eq, ":quest_no", "qst_kill_local_merchant"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(this_or_next|eq, ":giver_reputation", lrep_quarrelsome),
								(this_or_next|eq, ":giver_reputation", lrep_cunning),
								(             eq, ":giver_reputation", lrep_debauched),
								(neg|faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),#Can not take the quest from the king
								(ge, "$g_talk_troop_faction_relation", 0),
								(gt, ":player_level", 5),
								(is_between, ":giver_center_no", towns_begin, towns_end),
								(assign, ":quest_importance", 1),
								(assign, ":quest_xp_reward", 300),
								(assign, ":quest_gold_reward", 1000),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 10),
								(assign, ":quest_dont_give_again_period", 30),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_bring_back_runaway_serfs"),
							(try_begin),
								(neq, ":giver_reputation", lrep_goodnatured),
								(neq, ":giver_reputation", lrep_upstanding),
								(ge, "$g_talk_troop_faction_relation", 0),
								(ge, ":player_level", 5),
								(gt, ":giver_center_no", 0),#Skip if lord is outside the center
								(eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)
								
								(assign, ":cur_object_center", -1),
								(try_for_range, ":cur_village", villages_begin, villages_end),
									(party_slot_eq, ":cur_village", slot_town_lord, ":giver_troop"),
									(store_distance_to_party_from_party, ":dist", ":cur_village", ":giver_center_no"),
									(lt, ":dist", 25),
									(assign, ":cur_object_center", ":cur_village"),
								(try_end),
								(ge, ":cur_object_center", 0),#Skip if the quest giver is not the owner of any villages around the center
								(call_script, "script_cf_select_random_town_with_faction", ":giver_faction_no"),
								(assign, ":cur_target_center", reg0),
								(neq, ":cur_target_center", ":giver_center_no"),#Skip current center
								(store_distance_to_party_from_party, ":dist", ":cur_target_center", ":giver_center_no"),
								(ge, ":dist", 20),
								(assign, ":quest_target_party_template", "pt_runaway_serfs"),
								(assign, ":quest_object_center", ":cur_object_center"),
								(assign, ":quest_target_center", ":cur_target_center"),
								(assign, ":quest_importance", 1),
								(assign, ":quest_xp_reward", 200),
								(assign, ":quest_gold_reward", 150),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 20),
								(assign, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
								(assign, "$qst_bring_back_runaway_serfs_num_parties_fleed", 0),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_follow_spy"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(neq, ":giver_reputation", lrep_goodnatured),
								(party_get_skill_level, ":tracking_skill", "p_main_party", "skl_tracking"),
								(ge, ":tracking_skill", 2),
								(ge, ":player_level", 10),
								(eq, "$g_defending_against_siege", 0), #Skip if the center is under siege (because of resting)
								(gt, ":giver_party_no", 0), #Skip if the quest giver doesn't have a party
								(gt, ":giver_center_no", 0), #skip if the quest giver is not in a center
								(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town), #skip if we are not in a town.
								(party_get_position, pos2, "p_main_party"),
								(assign, ":min_distance", 99999),
								(assign, ":cur_object_center", -1),
								(try_for_range, ":unused_2", 0, 10),
									(call_script, "script_cf_get_random_enemy_center", ":giver_party_no"),
									(assign, ":random_object_center", reg0),
									(party_get_position, pos3, ":random_object_center"),
									(map_get_random_position_around_position, pos4, pos3, 6),
									(get_distance_between_positions, ":cur_distance", pos2, pos4),
									(lt, ":cur_distance", ":min_distance"),
									(assign, ":min_distance", ":cur_distance"),
									(assign, ":cur_object_center", ":random_object_center"),
									(copy_position, pos63, pos4), #Do not change pos63 until quest is accepted
								(try_end),
								(gt, ":cur_object_center", 0), #Skip if there are no enemy centers
								
								(assign, ":quest_object_center", ":cur_object_center"),
								(assign, ":quest_dont_give_again_period", 50),
								(assign, ":result", ":quest_no"),
								(assign, "$qst_follow_spy_run_away", 0),
								(assign, "$qst_follow_spy_meeting_state", 0),
								(assign, "$qst_follow_spy_meeting_counter", 0),
								(assign, "$qst_follow_spy_spy_back_in_town", 0),
								(assign, "$qst_follow_spy_partner_back_in_town", 0),
								(assign, "$qst_follow_spy_no_active_parties", 0),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_capture_enemy_hero"),
							(try_begin),
								(eq, "$players_kingdom", ":giver_faction_no"),
								(neg|faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
								(ge, ":player_level", 15),
								(call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),#Can fail
								(assign, ":quest_target_faction", reg0),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 80),
								(assign, ":quest_gold_reward", 2000),
								(assign, ":result", ":quest_no"),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_lend_companion"),
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								(assign, ":total_heroes", 0),
								(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
								(try_for_range, ":i_stack", 0, ":num_stacks"),
									(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
									(troop_is_hero, ":stack_troop"),
									(is_between, ":stack_troop", companions_begin, companions_end),
									(store_character_level, ":stack_level", ":stack_troop"),
									(ge, ":stack_level", 15),
									(assign, ":is_quest_hero", 0),
									(try_for_range, ":i_quest", 0, all_quests_end),
										(check_quest_active, ":i_quest"),
										(this_or_next|quest_slot_eq, ":i_quest", slot_quest_target_troop, ":stack_troop"),
										(quest_slot_eq, ":i_quest", slot_quest_object_troop, ":stack_troop"),
										(assign, ":is_quest_hero", 1),
									(try_end),
									(eq, ":is_quest_hero", 0),
									(val_add, ":total_heroes", 1),
								(try_end),
								(gt, ":total_heroes", 0),#Skip if party has no eligible heroes
								(store_random_in_range, ":random_hero", 0, ":total_heroes"),
								(assign, ":total_heroes", 0),
								(assign, ":cur_target_troop", -1),
								(try_for_range, ":i_stack", 0, ":num_stacks"),
									(eq, ":cur_target_troop", -1),
									(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
									(troop_is_hero, ":stack_troop"),
									(is_between, ":stack_troop", companions_begin, companions_end),
									(neq, ":stack_troop", "trp_player"),
									(store_character_level, ":stack_level", ":stack_troop"),
									(ge, ":stack_level", 15),
									(assign, ":is_quest_hero", 0),
									(try_for_range, ":i_quest", 0, all_quests_end),
										(check_quest_active, ":i_quest"),
										(this_or_next|quest_slot_eq, ":i_quest", slot_quest_target_troop, ":stack_troop"),
										(quest_slot_eq, ":i_quest", slot_quest_object_troop, ":stack_troop"),
										(assign, ":is_quest_hero", 1),
									(try_end),
									(eq, ":is_quest_hero", 0),
									(val_add, ":total_heroes", 1),
									(gt, ":total_heroes", ":random_hero"),
									(assign, ":cur_target_troop", ":stack_troop"),
								(try_end),
								(is_between, ":cur_target_troop", companions_begin, companions_end),
								
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(store_current_day, ":quest_target_amount"),
								(val_add, ":quest_target_amount", 8),
								
								(assign, ":quest_importance", 1),
								(assign, ":quest_xp_reward", 300),
								(assign, ":quest_gold_reward", 400),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_dont_give_again_period", 30),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_collect_debt"),
							(eq, 1, 0), #disable this quest pending talk with armagan
							(try_begin),
								(ge, "$g_talk_troop_faction_relation", 0),
								# Find a vassal (within the same kingdom?)
								(call_script, "script_cf_get_random_lord_in_a_center_with_faction", ":giver_faction_no"),#Can fail
								(assign, ":quest_target_troop", reg0),
								(neq, ":quest_target_troop", ":giver_troop"),#Skip himself
								(call_script, "script_get_troop_attached_party", ":quest_target_troop"),
								(assign, ":quest_target_center", reg0),#cur_target_center will definitely be a valid center
								(neq,":giver_center_no", ":quest_target_center"),#Skip current center
								
								(assign, ":quest_xp_reward", 30),
								(assign, ":quest_gold_reward", 40),
								(assign, ":result", ":quest_no"),
								(store_random_in_range, ":quest_target_amount", 6, 9),
								(val_mul, ":quest_target_amount", 500),
								(store_div, ":quest_convince_value", ":quest_target_amount", 5),
								(assign, ":quest_expiration_days", 90),
								(assign, ":quest_dont_give_again_period", 20),
							(try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_capture_conspirators"),
							##          (try_begin),
							##            (eq, 1,0), #TODO: disable this for now
							##            (ge, ":player_level", 10),
							##            (is_between, ":giver_center_no", towns_begin, towns_end),#Skip if quest giver's center is not a town
							##            (party_slot_eq, ":giver_center_no", slot_town_lord, ":giver_troop"),#Skip if the current center is not ruled by the quest giver
							##            (call_script, "script_cf_get_random_kingdom_hero", ":giver_faction_no"),#Can fail
							##
							##            (assign, ":quest_target_troop", reg0),
							##            (assign, ":quest_target_center", ":giver_center_no"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 10),
							##            (assign, ":quest_gold_reward", 10),
							##            (assign, ":result", ":quest_no"),
							##            (store_character_level, ":cur_level"),
							##            (val_div, ":cur_level", 5),
							##            (val_max, ":cur_level", 3),
							##            (store_add, ":max_parties", 4, ":cur_level"),
							##            (store_random_in_range, "$qst_capture_conspirators_num_parties_to_spawn", 4, ":max_parties"),
							##            (assign, "$qst_capture_conspirators_num_troops_to_capture", 0),
							##            (assign, "$qst_capture_conspirators_num_parties_spawned", 0),
							##            (assign, "$qst_capture_conspirators_leave_meeting_counter", 0),
							##            (assign, "$qst_capture_conspirators_party_1", 0),
							##            (assign, "$qst_capture_conspirators_party_2", 0),
							##            (assign, "$qst_capture_conspirators_party_3", 0),
							##            (assign, "$qst_capture_conspirators_party_4", 0),
							##            (assign, "$qst_capture_conspirators_party_5", 0),
							##            (assign, "$qst_capture_conspirators_party_6", 0),
							##            (assign, "$qst_capture_conspirators_party_7", 0),
							##          (try_end),
							##        (else_try),
							##          (eq, ":quest_no", "qst_defend_nobles_against_peasants"),
							##          (try_begin),
							##            (eq, 1,0), #TODO: disable this for now
							##            (ge, ":player_level", 10),
							##            (is_between, ":giver_center_no", towns_begin, towns_end),#Skip if quest giver's center is not a town
							##            (party_slot_eq, ":giver_center_no", slot_town_lord, ":giver_troop"),#Skip if the current center is not ruled by the quest giver
							##
							##            (assign, ":quest_target_center", ":giver_center_no"),
							##            (assign, ":quest_importance", 1),
							##            (assign, ":quest_xp_reward", 10),
							##            (assign, ":quest_gold_reward", 10),
							##            (assign, ":result", ":quest_no"),
							##            (store_character_level, ":cur_level"),
							##            (val_div, ":cur_level", 5),
							##            (val_max, ":cur_level", 4),
							##            (store_add, ":max_parties", 4, ":cur_level"),
							##            (store_random_in_range, "$qst_defend_nobles_against_peasants_num_peasant_parties_to_spawn", 4, ":cur_level"),
							##            (store_random_in_range, "$qst_defend_nobles_against_peasants_num_noble_parties_to_spawn", 4, ":cur_level"),
							##            (assign, "$qst_defend_nobles_against_peasants_num_nobles_to_save", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_num_nobles_saved", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_1", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_2", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_3", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_4", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_5", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_6", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_7", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_8", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
							##            (assign, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
							##          (try_end),
						(else_try),
							(eq, ":quest_no", "qst_incriminate_loyal_commander"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(neq, ":giver_reputation", lrep_upstanding),
								(neq, ":giver_reputation", lrep_goodnatured),
								(eq, "$players_kingdom", ":giver_faction_no"),
								(ge, ":player_level", 10),
								(faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),
								(assign, ":try_times", 1),
								(assign, ":found", 0),
								(try_for_range, ":unused", 0, ":try_times"),
									(call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),#Can fail
									(assign, ":cur_target_faction", reg0),
									
									(faction_get_slot, ":cur_target_troop", ":cur_target_faction", slot_faction_leader),
									(assign, ":num_centerless_heroes", 0),
									(try_for_range, ":cur_kingdom_hero", active_npcs_begin, active_npcs_end),
										(troop_slot_eq, ":cur_kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
										#(troop_slot_eq, ":cur_kingdom_hero", slot_troop_is_prisoner, 0),
										(neg|troop_slot_ge, ":cur_kingdom_hero", slot_troop_prisoner_of_party, 0),
										(neq, ":cur_target_troop", ":cur_kingdom_hero"),
										(store_troop_faction, ":cur_kingdom_hero_faction", ":cur_kingdom_hero"),
										(eq, ":cur_target_faction", ":cur_kingdom_hero_faction"),
										##                (call_script, "script_get_number_of_hero_centers", ":cur_kingdom_hero"),
										##                (eq, reg0, 0),
										(val_add, ":num_centerless_heroes", 1),
									(try_end),
									(gt, ":num_centerless_heroes", 0),
									(assign, ":cur_object_troop", -1),
									(store_random_in_range, ":random_kingdom_hero", 0, ":num_centerless_heroes"),
									(try_for_range, ":cur_kingdom_hero", active_npcs_begin, active_npcs_end),
										(eq, ":cur_object_troop", -1),
										(troop_slot_eq, ":cur_kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
										(neq, ":cur_target_troop", ":cur_kingdom_hero"),
										(store_troop_faction, ":cur_kingdom_hero_faction", ":cur_kingdom_hero"),
										(eq, ":cur_target_faction", ":cur_kingdom_hero_faction"),
										##                (call_script, "script_get_number_of_hero_centers", ":cur_kingdom_hero"),
										##                (eq, reg0, 0),
										(val_sub, ":random_kingdom_hero", 1),
										(lt, ":random_kingdom_hero", 0),
										(assign, ":cur_object_troop", ":cur_kingdom_hero"),
									(try_end),
									
									(assign, ":cur_target_center", -1),
									(call_script, "script_get_troop_attached_party", ":cur_target_troop"),
									(is_between, reg0, towns_begin, towns_end),
									(party_slot_eq, reg0, slot_town_lord, ":cur_target_troop"),
									(assign, ":cur_target_center", reg0),
									
									(assign, ":try_times", -1),#Exit the second loop
									(assign, ":found", 1),
								(try_end),
								(eq, ":found", 1),
								
								(assign, "$incriminate_quest_sacrificed_troop", 0),
								
								(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
								(try_for_range, ":i_stack", 1, ":num_stacks"),
									(eq ,"$incriminate_quest_sacrificed_troop", 0),
									(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
									(neg|troop_is_hero, ":stack_troop"),
									(store_character_level, ":stack_troop_level", ":stack_troop"),
									(ge, ":stack_troop_level", 25),
									(assign, "$incriminate_quest_sacrificed_troop", ":stack_troop"),
								(try_end),
								(gt, "$incriminate_quest_sacrificed_troop", 0),
								
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(assign, ":quest_object_troop", ":cur_object_troop"),
								(assign, ":quest_target_center", ":cur_target_center"),
								(assign, ":quest_target_faction", ":cur_target_faction"),
								
								(assign, ":quest_importance", 1),
								(assign, ":quest_xp_reward", 700),
								(assign, ":quest_gold_reward", 1000),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 30),
								(assign, ":quest_dont_give_again_period", 180),
							(try_end),
						(else_try),
							(eq, ":quest_no", "qst_capture_prisoners"),
							(eq, "$player_has_homage", 0),
							
							(try_begin),
								(eq, "$players_kingdom", ":giver_faction_no"),
								(call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),#Can fail
								(assign, ":cur_target_faction", reg0),
								(store_add, ":max_tier_no", slot_faction_tier_5_troop, 1),
								(store_random_in_range, ":random_tier_no", slot_faction_tier_2_troop, ":max_tier_no"),
								(faction_get_slot, ":cur_target_troop", ":cur_target_faction", ":random_tier_no"),
								(gt, ":cur_target_troop", 0),
								(store_random_in_range, ":quest_target_amount", 3, 7),
								(assign, ":quest_target_troop", ":cur_target_troop"),
								(assign, ":quest_target_faction", ":cur_target_faction"),
								(assign, ":quest_importance", 1),
								(store_character_level, ":quest_gold_reward", ":cur_target_troop"),
								(val_add, ":quest_gold_reward", 5),
								(val_mul, ":quest_gold_reward", ":quest_gold_reward"),
								(val_div, ":quest_gold_reward", 5),
								(val_mul, ":quest_gold_reward", ":quest_target_amount"),
								(assign, ":quest_xp_reward", ":quest_gold_reward"),
								(assign, ":result", ":quest_no"),
								(assign, ":quest_expiration_days", 90),
								(assign, ":quest_dont_give_again_period", 20),
							(try_end),
						(try_end),
					(try_end),
				(try_end),
				#end of quest finding
				
				
				(try_begin),
					(neq, ":result", -1),
					
					(try_begin),
						(party_is_active, ":quest_target_center"),
						(store_faction_of_party, ":quest_target_faction", ":quest_target_center"),
					(try_end),
					
					(quest_set_slot, ":result", slot_quest_target_troop, ":quest_target_troop"),
					(quest_set_slot, ":result", slot_quest_target_center, ":quest_target_center"),
					(quest_set_slot, ":result", slot_quest_object_troop, ":quest_object_troop"),
					(quest_set_slot, ":result", slot_quest_target_faction, ":quest_target_faction"),
					(quest_set_slot, ":result", slot_quest_object_faction, ":quest_object_faction"),
					(quest_set_slot, ":result", slot_quest_object_center, ":quest_object_center"),
					(quest_set_slot, ":result", slot_quest_target_party, ":quest_target_party"),
					(quest_set_slot, ":result", slot_quest_target_party_template, ":quest_target_party_template"),
					(quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
					(quest_set_slot, ":result", slot_quest_importance, ":quest_importance"),
					(quest_set_slot, ":result", slot_quest_xp_reward, ":quest_xp_reward"),
					(quest_set_slot, ":result", slot_quest_gold_reward, ":quest_gold_reward"),
					(quest_set_slot, ":result", slot_quest_convince_value, ":quest_convince_value"),
					(quest_set_slot, ":result", slot_quest_expiration_days, ":quest_expiration_days"),
					(quest_set_slot, ":result", slot_quest_dont_give_again_period, ":quest_dont_give_again_period"),
					(quest_set_slot, ":result", slot_quest_current_state, 0),
					(quest_set_slot, ":result", slot_quest_giver_troop, ":giver_troop"),
					(quest_set_slot, ":result", slot_quest_giver_center, ":giver_center_no"),
					(quest_set_slot, ":result", slot_quest_target_dna, ":quest_target_dna"),
					(quest_set_slot, ":result", slot_quest_target_item, ":quest_target_item"),
				(try_end),
				
				(assign, reg0, ":result"),
		])

		# script_get_dynamic_quest - combines old get_random_quest with new get_dynamic_quest
		
		# Input: arg1 = troop_no (of the troop in conversation)
		# Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
		#		 reg1 = relevant troop
		#		 reg2 = relevant party
		#		 reg3 = relevant faction
get_dynamic_quest = (
			"get_dynamic_quest",
			#Dynamic quests are rarer, more important quests
			#this is a separate script from get_quest, so that tavern keepers can scan all NPCs for quests
			[
				(store_script_param_1, ":giver_troop"),
				
				(assign, ":result", -1),
				(assign, ":relevant_troop", -1),
				(assign, ":relevant_party", -1),
				(assign, ":relevant_faction", -1),
				
				(try_begin),
					(eq, ":giver_troop", -1),
					
				(else_try),
					#1 rescue prisoner
					(neg|check_quest_active, "qst_rescue_prisoner"),
					(this_or_next|troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
					(troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_lady),
					
					(assign, ":target_troop", -1),
					(try_for_range, ":possible_prisoner", active_npcs_begin, active_npcs_end),
						(troop_get_slot, ":captor_location", ":possible_prisoner", slot_troop_prisoner_of_party),
						(is_between, ":captor_location", walled_centers_begin, walled_centers_end),
						(store_troop_faction, ":giver_troop_faction_no", ":giver_troop"),
						(store_faction_of_party, ":captor_location_faction_no", ":captor_location"),
						(store_relation, ":giver_captor_relation", ":giver_troop_faction_no", ":captor_location_faction_no"),
						(lt, ":giver_captor_relation", 0),
						
						(call_script, "script_troop_get_family_relation_to_troop", ":giver_troop", ":possible_prisoner"),
						(ge, reg0, 10),
						
						(assign, ":offered_parole", 0),
						(try_begin),
							(call_script, "script_cf_prisoner_offered_parole", ":possible_prisoner"),
							(assign, ":offered_parole", 1),
						(try_end),
						(eq, ":offered_parole", 0),
						
						(neg|party_slot_eq, ":captor_location", slot_town_lord, "trp_player"),
						
						(assign, ":target_troop", ":possible_prisoner"),
						(assign, ":target_party", ":captor_location"),
					(try_end),
					
					(gt, ":target_troop", -1),
					(assign, ":result", "qst_rescue_prisoner"),
					(assign, ":relevant_troop", ":target_troop"),
					(assign, ":relevant_party", ":target_party"),
					
				(else_try),
					#2 retaliate for border incident
					(is_between, ":giver_troop", mayors_begin, mayors_end),
					(store_faction_of_troop, ":giver_faction", ":giver_troop"),
					
					(neg|check_quest_active, "qst_retaliate_for_border_incident"),
					(quest_slot_eq, "qst_retaliate_for_border_incident", slot_quest_dont_give_again_remaining_days, 0),
					(assign, ":target_leader", 0),
					
					(try_for_range, ":kingdom", "fac_kingdom_1", kingdoms_end),
						(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":giver_faction", ":kingdom"),
						(assign, ":diplomatic_status", reg0),
						(eq, ":diplomatic_status", -1),
						(assign, ":duration", reg1),
						(ge, ":duration", 10),
						
						
						(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
							(store_faction_of_troop, ":lord_faction", ":lord"),
							(eq, ":lord_faction", ":kingdom"),
							
							(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
							
							(assign, ":target_leader", ":lord"),
							(assign, ":target_faction", ":kingdom"),
						(try_end),
					(try_end),
					(is_between, ":target_leader", active_npcs_begin, active_npcs_end),
					
					(assign, ":result", "qst_retaliate_for_border_incident"),
					(assign, ":relevant_troop", ":target_leader"),
					(assign, ":relevant_faction", ":target_faction"),
				(else_try), #Find bandit hideout
					(troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
					(neg|check_quest_active, "qst_destroy_bandit_lair"),
					(quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_dont_give_again_remaining_days, 0),
					
					#		(display_message, "@Checking for bandit lair quest"),
					
					(assign, ":lair_found", -1),
					
					(try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
						(party_template_get_slot, ":bandit_lair", ":bandit_template", slot_party_template_lair_party),
						
						#No party is active because bandit lairs are removed as soon as they are attacked, by the player -- but can only be removed by the player. This will reset bandit lair to zero
						(gt, ":bandit_lair", "p_spawn_points_end"),
						
						(assign, ":closest_town", -1),
						(assign, ":score_to_beat", 99999),
						
						(try_for_range, ":town_no", towns_begin, towns_end),
							(store_distance_to_party_from_party, ":distance", ":bandit_lair", ":town_no"),
							(lt, ":distance", ":score_to_beat"),
							(assign, ":closest_town", ":town_no"),
							(assign, ":score_to_beat", ":distance"),
						(try_end),
						
						#(str_store_party_name, s7, ":closest_town"),
						#(party_get_slot, ":closest_town_lord", ":closest_town", slot_town_lord),
						#(str_store_troop_name, s8, ":closest_town_lord"),
						
						(party_slot_eq, ":closest_town", slot_town_lord, ":giver_troop"),
						(assign, ":lair_found", ":bandit_lair"),
					(try_end),
					
					(gt, ":lair_found", "p_spawn_points_end"),
					
					(assign ,":result", "qst_destroy_bandit_lair"),
					(assign, ":relevant_party", ":lair_found"),
				(else_try),  #3 - bounty on bandit party
					(is_between, ":giver_troop", mayors_begin, mayors_end),
					(neg|check_quest_active, "qst_track_down_bandits"),
					(quest_slot_eq, "qst_track_down_bandits", slot_quest_dont_give_again_remaining_days, 0),
					
					(assign, ":cur_town", -1),
					(try_for_range, ":town", towns_begin, towns_end),
						(party_slot_eq, ":town", slot_town_elder, ":giver_troop"),
						(assign, ":cur_town", ":town"),
					(try_end),
					(gt, ":cur_town", -1),
					
					(call_script, "script_merchant_road_info_to_s42", ":cur_town"),
					(assign, ":bandit_party_found", reg0),
					(party_is_active, ":bandit_party_found"),
					(gt, ":bandit_party_found", 0),
					
					(try_begin),
						(eq, "$cheat_mode", 1),
						(display_message, "str_traveller_attack_found"),
					(try_end),
					
					(assign ,":result", "qst_track_down_bandits"),
					(assign, ":relevant_party", ":bandit_party_found"),
				(else_try),  #raid a caravan to start war
					(troop_slot_eq, ":giver_troop", slot_lord_reputation_type, lrep_debauched),
					(store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
					
					(assign, ":junior_debauched_lord_in_faction", -1),
					(try_for_range, ":lord_in_faction", active_npcs_begin, active_npcs_end),
						(troop_slot_eq, ":lord_in_faction", slot_lord_reputation_type, lrep_debauched),
						(store_faction_of_troop, ":debauched_lord_faction", ":lord_in_faction"),
						(eq, ":debauched_lord_faction", ":giver_troop_faction"),
						(assign, ":junior_debauched_lord_in_faction", ":lord_in_faction"),
					(try_end),
					(eq, ":giver_troop", ":junior_debauched_lord_in_faction"),
					
					(assign, ":faction_to_attack", 0),
					(assign, ":faction_to_attack_score", 0),
					
					(try_for_range, ":faction_candidate", kingdoms_begin, kingdoms_end),
						(neq, ":faction_to_attack", -1),
						(neq, ":faction_candidate", ":giver_troop_faction"),
						(faction_slot_eq, ":faction_candidate", slot_faction_state, sfs_active),
						(neq, ":faction_candidate", "$players_kingdom"),
						
						(store_relation, ":relation", ":faction_candidate", ":giver_troop_faction"),
						
						(store_add, ":provocation_slot", ":giver_troop_faction", slot_faction_provocation_days_with_factions_begin),
						(val_sub, ":provocation_slot", kingdoms_begin),
						(faction_get_slot, ":provocation_days", ":faction_candidate", ":provocation_slot"),
						
						(try_begin),
							(lt, ":relation", 0),
							(assign, ":faction_to_attack", -1), #disqualifies if thefaction is already at war
						(else_try),
							(ge, ":provocation_days", 1),
							(assign, ":faction_to_attack", -1), #disqualifies if the faction has already provoked someone
						(else_try),
							(ge, ":relation", 0),
							(assign, ":faction_to_attack_temp_score", 2),
							#add in scores - no truce?
							
							#				(store_add, ":truce_slot", ":giver_troop_faction", slot_faction_truce_days_with_factions_begin),
							#				(store_add, ":provocation_slot", ":giver_troop_faction", slot_faction_provocation_days_with_factions_begin),
							#				(val_sub, ":truce_slot", kingdoms_begin),
							#				(val_sub, ":provocation_slot", kingdoms_begin),
							#				(faction_slot_eq, ":faction_candidate", ":provocation_slot", 0),
							#				(try_begin),
							#					(faction_slot_ge, ":faction_candidate", ":truce_slot", 1),
							#					(val_sub, ":faction_to_attack_temp_score", 1),
							#				(try_end),
							
							(gt, ":faction_to_attack_temp_score", ":faction_to_attack_score"),
							
							(assign, ":faction_to_attack", ":faction_candidate"),
							(assign, ":faction_to_attack_temp_score", ":faction_to_attack_score"),
						(try_end),
					(try_end),
					
					(is_between, ":faction_to_attack", kingdoms_begin, kingdoms_end),
					
					(assign ,":result", "qst_cause_provocation"),
					(assign, ":relevant_faction", ":faction_to_attack"),
					
				(try_end),
				
				(assign, reg0, ":result"),
				(assign, reg1, ":relevant_troop"),
				(assign, reg2, ":relevant_party"),
				(assign, reg3, ":relevant_faction"),
				
		])

		# script_get_political_quest- combines old get_random_quest with new get_dynamic_quest
		# Political quests are given by the player's political "coach" -- ie, a spouse or the minister -- to improve standing in the faction
		# Input: arg1 = troop_no (of the troop in conversation)
		# Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
		#		 reg1 = quest_target_troop
		#		 reg2 = quest_object_troop
get_political_quest = (
			"get_political_quest",
			#Political quests are given by the player's political "coach" -- ie, a spouse or the minister -- to improve standing in the faction
			[
				(store_script_param, ":giver_troop", 1),
				
				(assign, ":result", -1),
				(assign, ":quest_target_troop", -1),
				(assign, ":quest_object_troop", -1),
				(assign, ":quest_dont_give_again_period", 7), #one week on average
				
				
				
				(try_begin), #this for kingdom hero, "we have a mutual enemy"
					(neg|check_quest_active, "qst_denounce_lord"),
					(try_begin),
						(ge, "$cheat_mode", 1),
						(quest_get_slot, reg4, "qst_denounce_lord", slot_quest_dont_give_again_remaining_days),
						(display_message, "@{!}DEBUG -- Checking for denounce lord, eligible in {reg4} days"),
					(try_end),
					
					(neg|quest_slot_ge, "qst_denounce_lord", slot_quest_dont_give_again_remaining_days, 1),
					(neq, ":giver_troop", "$g_player_minister"),
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":giver_troop"),
					(neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
					
					
					#		(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_martial),
					(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_quarrelsome),
					(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_goodnatured),
					
					#		(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 10),
					
					
					(assign, ":target_lord", -1),
					(assign, ":score_to_beat", 1),
					
					(try_for_range, ":potential_target", active_npcs_begin, active_npcs_end),
						(store_faction_of_troop, ":potential_target_faction", ":potential_target"),
						(eq, ":potential_target_faction", "$players_kingdom"),
						(neq, ":potential_target", ":giver_troop"),
						(neg|faction_slot_eq, ":potential_target_faction", slot_faction_leader, ":potential_target"),
						
						#cannot denounce if you also have an intrigue against lord active
						(this_or_next|neg|check_quest_active, "qst_intrigue_against_lord"),
						(neg|quest_slot_eq, "qst_intrigue_against_lord", slot_quest_target_troop, ":potential_target"),
						
						(call_script, "script_troop_get_relation_with_troop", ":potential_target", ":giver_troop"),
						(assign, ":relation_with_giver_troop", reg0),
						(lt, ":relation_with_giver_troop", ":score_to_beat"),
						
						(str_store_troop_name, s4, ":potential_target"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(display_message, "@{!}DEBUG -- Rival found in {s4}"),
						(try_end),
						
						(try_begin),
							(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_debauched),
							(assign, ":max_rel_w_player", 15),
						(else_try),
							(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_quarrelsome),
							(assign, ":max_rel_w_player", 10),
						(else_try),
							(assign, ":max_rel_w_player", 5),
						(try_end),
						
						(call_script, "script_troop_get_relation_with_troop", ":potential_target", "trp_player"),
						(assign, ":relation_with_player", reg0),
						(lt, ":relation_with_player", ":max_rel_w_player"),
						
						(str_store_troop_name, s4, ":potential_target"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(display_message, "@{!}DEBUG -- {s4} is not close friend of player"),
						(try_end),
						
						(assign, ":enemies_in_faction", 0),
						(try_for_range, ":other_lord", active_npcs_begin, active_npcs_end),
							(store_faction_of_troop, ":other_lord_faction", ":other_lord"),
							(eq, ":other_lord_faction", "$players_kingdom"),
							(call_script, "script_troop_get_relation_with_troop", ":potential_target", ":other_lord"),
							(lt, reg0, 0),
							(val_add, ":enemies_in_faction", 1),
						(try_end),
						
						(str_store_troop_name, s4, ":potential_target"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(assign, reg3, ":enemies_in_faction"),
							(display_message, "@{!}DEBUG -- {s4} has {reg3} rivals"),
						(try_end),
						
						(this_or_next|ge, ":enemies_in_faction", 3),
						(ge, "$cheat_mode", 1),
						
						(assign, ":score_to_beat", ":relation_with_giver_troop"),
						(assign, ":target_lord", ":potential_target"),
					(try_end),
					
					(is_between, ":target_lord", active_npcs_begin, active_npcs_end),
					
					
					(assign, ":result", "qst_denounce_lord"),
					(assign, ":quest_target_troop", ":target_lord"),
					
				(else_try),
					(neg|check_quest_active, "qst_intrigue_against_lord"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(quest_get_slot, reg4, "qst_intrigue_against_lord", slot_quest_dont_give_again_remaining_days),
						(display_message, "@{!}DEBUG -- Checking for intrigue, eligible in {reg4} days"),
					(try_end),
					
					(neg|quest_slot_ge, "qst_intrigue_against_lord", slot_quest_dont_give_again_remaining_days, 1),
					
					
					
					(neq, ":giver_troop", "$g_player_minister"),
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":giver_troop"),
					(neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
					
					(try_begin),
						(ge, "$cheat_mode", 1),
						(display_message, "@{!}DEBUG -- Trying for intrigue against lord"),
					(try_end),
					
					
					(assign, ":target_lord", -1),
					(assign, ":score_to_beat", 10),
					
					(try_for_range, ":potential_target", active_npcs_begin, active_npcs_end),
						(store_faction_of_troop, ":potential_target_faction", ":potential_target"),
						(eq, ":potential_target_faction", "$players_kingdom"),
						(neq, ":potential_target", ":giver_troop"),
						(neg|faction_slot_eq, ":potential_target_faction", slot_faction_leader, ":potential_target"),
						
						
						(this_or_next|neg|check_quest_active, "qst_denounce_lord"),
						(neg|quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, ":potential_target"),
						
						(faction_get_slot, ":faction_liege", "$players_kingdom", slot_faction_leader),
						(call_script, "script_troop_get_relation_with_troop", ":potential_target", ":faction_liege"),
						(assign, ":relation_with_liege", reg0),
						(lt, ":relation_with_liege", ":score_to_beat"),
						
						(str_store_troop_name, s4, ":potential_target"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(display_message, "@{!}DEBUG -- {s4} has sufficiently low relation with liege"),
						(try_end),
						
						
						(call_script, "script_troop_get_relation_with_troop", ":potential_target", ":giver_troop"),
						(assign, ":relation_with_giver_troop", reg0),
						(lt, ":relation_with_giver_troop", 0),
						
						(str_store_troop_name, s4, ":potential_target"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(display_message, "@{!}DEBUG -- {s4} has sufficiently low relation with giver troop"),
						(try_end),
						
						
						(call_script, "script_troop_get_relation_with_troop", ":potential_target", "trp_player"),
						(assign, ":relation_with_player", reg0),
						(lt, ":relation_with_player", 0),
						
						(str_store_troop_name, s4, ":potential_target"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(display_message, "@{!}DEBUG -- {s4} has sufficiently low relation with player"),
						(try_end),
						
						(assign, ":score_to_beat", ":relation_with_liege"),
						(assign, ":target_lord", ":potential_target"),
					(try_end),
					
					(is_between, ":target_lord", active_npcs_begin, active_npcs_end),
					
					
					(assign, ":result", "qst_intrigue_against_lord"),
					(assign, ":quest_target_troop", ":target_lord"),
					
					
				(else_try),
					#Resolve dispute, if there is a good chance of achieving the result
					(try_begin),
						(ge, "$cheat_mode", 1),
						(quest_get_slot, reg4, "qst_resolve_dispute", slot_quest_dont_give_again_remaining_days),
						(display_message, "@{!}DEBUG -- Checking for resolve dispute, eligible in {reg4} days"),
					(try_end),
					
					(neg|quest_slot_ge, "qst_resolve_dispute", slot_quest_dont_give_again_remaining_days, 1),
					
					
					
					(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
					(eq, "$g_talk_troop", "$g_player_minister"),
					
					(assign, ":target_lord", -1),
					(assign, ":object_lord", -1),
					(assign, ":best_chance_of_success", 20),
					
					(try_for_range, ":lord_1", active_npcs_begin, active_npcs_end),
						(store_faction_of_troop, ":lord_1_faction", ":lord_1"),
						(eq, ":lord_1_faction", "$players_kingdom"),
						(neq, ":lord_1", "$g_talk_troop"),
						
						(try_for_range, ":lord_2", active_npcs_begin, active_npcs_end),
							(store_faction_of_troop, ":lord_2_faction", ":lord_2"),
							(eq, ":lord_2_faction", "$players_kingdom"),
							
							(neq, ":lord_1", ":lord_2"),
							(neq, ":lord_2", "$g_talk_troop"),
							
							(call_script, "script_troop_get_relation_with_troop", ":lord_1", ":lord_2"),
							(assign, ":lord_1_relation_with_lord_2", reg0),
							(lt, ":lord_1_relation_with_lord_2", -5),
							
							(call_script, "script_troop_get_relation_with_troop", ":lord_1", "trp_player"),
							(assign, ":relation_with_lord_1", reg0),
							
							(call_script, "script_troop_get_relation_with_troop", ":lord_2", "trp_player"),
							(assign, ":relation_with_lord_2", reg0),
							
							(gt, ":relation_with_lord_1", 0),
							(gt, ":relation_with_lord_2", 0),
							
							(store_mul, ":chance_of_success", ":relation_with_lord_1", ":relation_with_lord_2"),
							
							
							(gt, ":chance_of_success", ":best_chance_of_success"),
							(assign, ":best_chance_of_success", ":chance_of_success"),
							(assign, ":target_lord", ":lord_1"),
							(assign, ":object_lord", ":lord_2"),
						(try_end),
					(try_end),
					
					
					(is_between, ":target_lord", active_npcs_begin, active_npcs_end),
					
					(assign, ":result", "qst_resolve_dispute"),
					(assign, ":quest_target_troop", ":target_lord"),
					(assign, ":quest_object_troop", ":object_lord"),
					
				(else_try),
					(try_begin),
						(ge, "$cheat_mode", 1),
						(quest_get_slot, reg4, "qst_offer_gift", slot_quest_dont_give_again_remaining_days),
						(display_message, "@{!}DEBUG -- Checking for offer gift, eligible in {reg4} days"),
					(try_end),
					
					(neg|quest_slot_ge, "qst_offer_gift", slot_quest_dont_give_again_remaining_days, 1),
					
					(assign, ":relative_found", -1),
					(assign, ":score_to_beat", 5),
					
					(try_for_range, ":potential_relative", active_npcs_begin, active_npcs_end),
						(store_faction_of_troop, ":relative_faction", ":potential_relative"),
						(eq, ":relative_faction", "$players_kingdom"),
						(neq, ":potential_relative", ":giver_troop"),
						(neg|faction_slot_eq, ":relative_faction", slot_faction_leader, ":potential_relative"),
						
						(call_script, "script_troop_get_family_relation_to_troop", ":giver_troop", ":potential_relative"),
						(assign, ":family_relation", reg0),
						(ge, ":family_relation", ":score_to_beat"),
						
						(store_sub, ":min_relation_w_player", 0, ":family_relation"),
						
						(call_script, "script_troop_get_relation_with_troop", "trp_player", ":potential_relative"),
						(assign, ":relation_with_player", reg0),
						(is_between, ":relation_with_player", ":min_relation_w_player", 0),
						
						(assign, ":score_to_beat", ":family_relation"),
						(assign, ":relative_found", ":potential_relative"),
						
					(try_end),
					
					(is_between, ":relative_found", active_npcs_begin, active_npcs_end),
					
					(assign, ":result", "qst_offer_gift"),
					(assign, ":quest_target_troop", ":relative_found"),
				(try_end),
				
				
				(try_begin),
					(gt, ":result", -1),
					(quest_set_slot, ":result", slot_quest_target_troop, ":quest_target_troop"),
					(quest_set_slot, ":result", slot_quest_target_troop, ":quest_object_troop"),
					
					(quest_set_slot, ":result", slot_quest_giver_troop, ":giver_troop"),
					(quest_set_slot, ":result", slot_quest_dont_give_again_period, ":quest_dont_give_again_period"),
				(try_end),
				
				(assign, reg0, ":result"),
				(assign, reg1, ":quest_target_troop"),
				(assign, reg2, ":quest_object_troop"),
				
		])

		# script_npc_find_quest_for_player_to_s11
		# Input: arg1 = faction_no
		# Output: reg0 = quest_giver_found
npc_find_quest_for_player_to_s11 = (
			"npc_find_quest_for_player_to_s11",
			[
				(store_script_param, ":faction", 1),
				
				(assign, ":quest_giver_found", -1),
				(try_for_range, ":quest_giver", active_npcs_begin, mayors_end),
					(eq, ":quest_giver_found", -1),
					
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":quest_giver"),
					
					(gt, ":quest_giver", "$g_troop_list_no"),
					
					(assign, "$g_troop_list_no", ":quest_giver"),
					
					(this_or_next|troop_slot_eq, ":quest_giver", slot_troop_occupation, slto_kingdom_hero),
					(is_between, ":quest_giver", mayors_begin, mayors_end),
					
					(neg|troop_slot_ge, ":quest_giver", slot_troop_prisoner_of_party, centers_begin),
					
					(try_begin),
						(is_between, ":quest_giver", mayors_begin, mayors_end),
						(assign, ":quest_giver_faction", -1),
						(try_for_range,":town", towns_begin, towns_end),
							(party_slot_eq, ":town", slot_town_elder, ":quest_giver"),
							(store_faction_of_party, ":quest_giver_faction", ":town"),
						(try_end),
					(else_try),
						(store_faction_of_troop, ":quest_giver_faction", ":quest_giver"),
					(try_end),
					(eq, ":faction", ":quest_giver_faction"),
					
					(call_script, "script_get_dynamic_quest", ":quest_giver"),
					(gt, reg0, -1),
					
					(assign, ":quest_giver_found", ":quest_giver"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":quest_giver_found"),
						(display_message, "str_test_diagnostic_quest_found_for_s4"),
					(try_end),
					
				(try_end),
				
				(assign, reg0, ":quest_giver_found"),
				
		])
		
		