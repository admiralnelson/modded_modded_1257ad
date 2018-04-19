from header import *

#script_update_report_to_army_quest_note
		# 
		# INPUT: arg1 = faction_no, arg2= faction_strategy, arg3 = old_faction state
		# OUTPUT: none
update_report_to_army_quest_note=(
	"update_report_to_army_quest_note",
			[
				(store_script_param, ":faction_no", 1),
				(store_script_param, ":new_strategy", 2),
				(store_script_param, ":old_faction_ai_state", 3),
				
				(try_begin),
					(le, "$number_of_report_to_army_quest_notes", 13),
					
					(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
					
					(try_begin), #updating quest notes for only report to army quest
						(eq, ":faction_no", "$players_kingdom"),
						(neq, ":new_strategy", ":old_faction_ai_state"),
						(check_quest_active, "qst_report_to_army"),
						(ge, ":faction_marshal", 0),
						
						(str_store_troop_name_link, s11, ":faction_marshal"),
						(store_current_hours, ":hours"),
						(call_script, "script_game_get_date_text", 0, ":hours"),
						
						(try_begin),
							(this_or_next|eq, ":new_strategy", sfai_attacking_enemies_around_center),
							(this_or_next|eq, ":new_strategy", sfai_attacking_center),
							(eq, ":new_strategy", sfai_gathering_army),
							(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
							(ge, ":faction_object", 0),
							(str_store_party_name_link, s21, ":faction_object"),
						(try_end),
						
						(try_begin),
							(eq, ":new_strategy", sfai_gathering_army),
							
							(try_begin),
								(ge, "$g_gathering_reason", 0),
								(str_store_party_name_link, s21, "$g_gathering_reason"),
								(str_store_string, s14, "str_we_should_prepare_to_defend_s21_but_we_should_gather_our_forces_until_we_are_strong_enough_to_engage_them"),
							(else_try),
								(str_store_string, s14, "str_it_is_time_to_go_on_the_offensive_and_we_must_first_assemble_the_army"),
							(try_end),
							
							(str_store_string, s14, "@({s1}) {s11}: {s14}"),
							(add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
							(val_add, "$number_of_report_to_army_quest_notes", 1),
						(else_try),
							(eq, ":new_strategy", sfai_attacking_enemies_around_center),
							
							(try_begin),
								(is_between, ":faction_object", walled_centers_begin, walled_centers_end),
								(str_store_string, s14, "str_we_should_ride_to_break_the_siege_of_s21"),
								(str_store_string, s14, "@({s1}) {s11}: {s14}"),
								(add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
								(val_add, "$number_of_report_to_army_quest_notes", 1),
							(else_try),
								(is_between, ":faction_object", villages_begin, villages_end),
								(str_store_string, s14, "str_we_should_ride_to_defeat_the_enemy_gathered_near_s21"),
								(str_store_string, s14, "@({s1}) {s11}: {s14}"),
								(add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
								(val_add, "$number_of_report_to_army_quest_notes", 1),
							(try_end),
						(else_try),
							(this_or_next|eq, ":new_strategy", sfai_attacking_center),
							(eq, ":new_strategy", sfai_raiding_village),
							
							(try_begin),
								(is_between, ":faction_object", walled_centers_begin, walled_centers_end),
								(str_store_string, s14, "str_we_believe_the_fortress_will_be_worth_the_effort_to_take_it"),
								(str_store_string, s14, "@{s14} ({s21})"),
								(str_store_string, s14, "@({s1}) {s11}: {s14}"),
								(add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
								(val_add, "$number_of_report_to_army_quest_notes", 1),
							(else_try),
								(is_between, ":faction_object", villages_begin, villages_end),
								(str_store_string, s14, "str_we_shall_leave_a_fiery_trail_through_the_heart_of_the_enemys_lands_targeting_the_wealthy_settlements_if_we_can"),
								(str_store_string, s14, "@{s14} ({s21})"),
								(str_store_string, s14, "@({s1}) {s11}: {s14}"),
								(add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
								(val_add, "$number_of_report_to_army_quest_notes", 1),
							(try_end),
						(try_end),
					(try_end),
				(try_end),
		])
		
		
		# script_check_and_finish_active_army_quests_for_faction
		# Input: faction_no
		# Output: none
check_and_finish_active_army_quests_for_faction=(
	"check_and_finish_active_army_quests_for_faction",
			[
				(store_script_param_1, ":faction_no"),
				(try_begin),
					(eq, "$players_kingdom", ":faction_no"),
					(try_begin),
						(check_quest_active, "qst_report_to_army"),
						(call_script, "script_cancel_quest", "qst_report_to_army"),
					(try_end),
					(assign, ":one_active", 0),
					(try_for_range, ":quest_no", army_quests_begin, army_quests_end),
						(check_quest_active, ":quest_no"),
						(call_script, "script_cancel_quest", ":quest_no"),
						(troop_get_slot, ":army_quest_giver_troop", ":quest_no", slot_quest_giver_troop),
						(assign, ":one_active", 1),
					(try_end),
					(try_begin),
						(check_quest_active, "qst_follow_army"),
						(assign, ":one_active", 1),
						(troop_get_slot, ":army_quest_giver_troop", "qst_follow_army", slot_quest_giver_troop),
						(call_script, "script_end_quest", "qst_follow_army"),
					(try_end),
					(eq, ":one_active", 1),
					(faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
					(store_current_hours, ":cur_hours"),
					(store_sub, ":total_time_served", ":cur_hours", ":last_offensive_time"),
					(store_mul, ":xp_reward", ":total_time_served", 5),
					(val_div, ":xp_reward", 50),
					(val_mul, ":xp_reward", 50),
					(val_add, ":xp_reward", 50),
					(add_xp_as_reward, ":xp_reward"),
					(call_script, "script_troop_change_relation_with_troop", "trp_player", ":army_quest_giver_troop", 2),
				(try_end),
		])

		
		# script_finish_quest
		# Input: arg1 = quest_no, arg2 = finish_percentage
		# Output: none
finish_quest=(
	"finish_quest",
			[
				(store_script_param_1, ":quest_no"),
				(store_script_param_2, ":finish_percentage"),
				
				(quest_get_slot, ":quest_giver", ":quest_no", slot_quest_giver_troop),
				(quest_get_slot, ":quest_importance", ":quest_no", slot_quest_importance),
				(quest_get_slot, ":quest_xp_reward", ":quest_no", slot_quest_xp_reward),
				(quest_get_slot, ":quest_gold_reward", ":quest_no", slot_quest_gold_reward),
				
				(try_begin),
					(lt, ":finish_percentage", 100),
					(val_mul, ":quest_xp_reward", ":finish_percentage"),
					(val_div, ":quest_xp_reward", 100),
					(val_mul, ":quest_gold_reward", ":finish_percentage"),
					(val_div, ":quest_gold_reward", 100),
					#Changing the relation factor. Negative relation if less than 75% of the quest is finished.
					#Positive relation if more than 75% of the quest is finished.
					(assign, ":importance_multiplier", ":finish_percentage"),
					(val_sub, ":importance_multiplier", 75),
					(val_mul, ":quest_importance", ":importance_multiplier"),
					(val_div, ":quest_importance", 100),
				(else_try),
					(val_div, ":quest_importance", 4),
					(val_add, ":quest_importance", 1),
					(call_script, "script_change_player_relation_with_troop", ":quest_giver", ":quest_importance"),
				(try_end),
				
				(add_xp_as_reward, ":quest_xp_reward"),
				(call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
				(call_script, "script_end_quest", ":quest_no"),
		])
		