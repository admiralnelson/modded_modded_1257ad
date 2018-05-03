from header import *

#script_update_report_to_army_quest_note
		# 
		# INPUT: arg1 = faction_no, arg2= faction_strategy, arg3 = old_faction state
		# OUTPUT: none
update_report_to_army_quest_note = (
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
check_and_finish_active_army_quests_for_faction = (
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
finish_quest = (
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
		

		
		# script_abort_quest
		# Input: arg1 = quest_no, arg2 = apply relation penalty
		# Output: none
abort_quest = (
	"abort_quest",
			[
				(store_script_param_1, ":quest_no"),
				(store_script_param_2, ":abort_type"), #0=aborted by event, 1=abort by talking 2=abort by expire
				
				(assign, ":quest_return_penalty", -1),
				(assign, ":quest_expire_penalty", -2),
				
				#      (quest_get_slot, ":quest_object_troop", ":quest_no", slot_quest_object_troop),
				(try_begin),
					(this_or_next|eq, ":quest_no", "qst_deliver_message"),
					(eq, ":quest_no", "qst_deliver_message_to_enemy_lord"),
					(assign, ":quest_return_penalty", -2),
					(assign, ":quest_expire_penalty", -3),
				(else_try),
					(eq, ":quest_no", "qst_kidnapped_girl"),
					(party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
					(quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
					(try_begin),
						(party_is_active, ":quest_target_party"),
						(remove_party, ":quest_target_party"),
					(try_end),
				(else_try),
					(eq, ":quest_no", "qst_escort_lady"),
					(quest_get_slot, ":quest_object_troop", "qst_escort_lady", slot_quest_object_troop),
					(party_remove_members, "p_main_party", ":quest_object_troop", 1),
					(assign, ":quest_return_penalty", -2),
					(assign, ":quest_expire_penalty", -3),
					##      (else_try),
					##        (eq, ":quest_no", "qst_rescue_lady_under_siege"),
					##        (party_remove_members, "p_main_party", ":quest_object_troop", 1),
					##      (else_try),
					##        (eq, ":quest_no", "qst_deliver_message_to_lover"),
					##      (else_try),
					##        (eq, ":quest_no", "qst_bring_prisoners_to_enemy"),
					##        (try_begin),
					##          (check_quest_succeeded, ":quest_no"),
					##          (quest_get_slot, ":quest_target_amount", ":quest_no", slot_quest_target_amount),
					##          (quest_get_slot, ":quest_object_troop", ":quest_no", slot_quest_object_troop),
					##          (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					##          (call_script, "script_game_get_join_cost", ":quest_object_troop"),
					##          (assign, ":reward", reg0),
					##          (val_mul, ":reward", ":quest_target_amount"),
					##          (val_div, ":reward", 2),
					##        (else_try),
					##          (quest_get_slot, ":reward", ":quest_no", slot_quest_target_amount),
					##        (try_end),
					##        (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":reward"),
					##      (else_try),
					##        (eq, ":quest_no", "qst_bring_reinforcements_to_siege"),
					##        (quest_get_slot, ":quest_target_amount", ":quest_no", slot_quest_target_amount),
					##        (quest_get_slot, ":quest_object_troop", ":quest_no", slot_quest_object_troop),
					##        (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					##        (call_script, "script_game_get_join_cost", ":quest_object_troop"),
					##        (assign, ":reward", reg0),
					##        (val_mul, ":reward", ":quest_target_amount"),
					##        (val_mul, ":reward", 2),
					##        (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":reward"),
					##      (else_try),
					##        (eq, ":quest_no", "qst_deliver_supply_to_center_under_siege"),
					##        (quest_get_slot, ":quest_target_amount", ":quest_no", slot_quest_target_amount),
					##        (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					##        (store_item_value, ":reward", "itm_siege_supply"),
					##        (val_mul, ":reward", ":quest_target_amount"),
					##        (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":reward"),
				(else_try),
					(eq, ":quest_no", "qst_raise_troops"),
					(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					(call_script, "script_change_debt_to_troop", ":quest_giver_troop", 100),
					(assign, ":quest_return_penalty", -4),
					(assign, ":quest_expire_penalty", -5),
				(else_try),
					(eq, ":quest_no", "qst_deal_with_looters"),
					(try_for_parties, ":cur_party_no"),
						(party_get_template_id, ":cur_party_template", ":cur_party_no"),
						(eq, ":cur_party_template", "pt_looters"),
						(party_set_flags, ":cur_party_no", pf_quest_party, 0),
					(try_end),
					(assign, ":quest_return_penalty", -4),
					(assign, ":quest_expire_penalty", -5),
				(else_try),
					(eq, ":quest_no", "qst_deal_with_bandits_at_lords_village"),
					(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					(call_script, "script_change_debt_to_troop", ":quest_giver_troop", 200),
					(assign, ":quest_return_penalty", -5),
					(assign, ":quest_expire_penalty", -6),
				(else_try),
					(eq, ":quest_no", "qst_collect_taxes"),
					(quest_get_slot, ":gold_reward", ":quest_no", slot_quest_gold_reward),
					(quest_set_slot, ":quest_no", slot_quest_gold_reward, 0),
					(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					(call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":gold_reward"),
					(assign, ":quest_return_penalty", -4),
					(assign, ":quest_expire_penalty", -6),
					##      (else_try),
					##        (eq, ":quest_no", "qst_capture_messenger"),
					##      (else_try),
					##        (eq, ":quest_no", "qst_bring_back_deserters"),
				(else_try),
					(eq, ":quest_no", "qst_hunt_down_fugitive"),
					(assign, ":quest_return_penalty", -3),
					(assign, ":quest_expire_penalty", -4),
				(else_try),
					(eq, ":quest_no", "qst_kill_local_merchant"),
				(else_try),
					(eq, ":quest_no", "qst_bring_back_runaway_serfs"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -1),
				(else_try),
					(eq, ":quest_no", "qst_lend_companion"),
				(else_try),
					(eq, ":quest_no", "qst_collect_debt"),
					(try_begin),
						(quest_slot_eq, "qst_collect_debt", slot_quest_current_state, 1), #debt collected but not delivered
						(quest_get_slot, ":debt", "qst_collect_debt", slot_quest_target_amount),
						(quest_get_slot, ":quest_giver", "qst_collect_debt", slot_quest_giver_troop),
						(call_script, "script_change_debt_to_troop", ":quest_giver", ":debt"),
						(assign, ":quest_return_penalty", -3),
						(assign, ":quest_expire_penalty", -6),
					(else_try),
						(assign, ":quest_return_penalty", -3),
						(assign, ":quest_expire_penalty", -4),
					(try_end),
				(else_try),
					(eq, ":quest_no", "qst_deal_with_bandits_at_lords_village"),
					(assign, ":quest_return_penalty", -6),
					(assign, ":quest_expire_penalty", -6),
				(else_try),
					(eq, ":quest_no", "qst_cause_provocation"),
					(assign, ":quest_return_penalty", -10),
					(assign, ":quest_expire_penalty", -13),
				(else_try),
					(eq, ":quest_no", "qst_persuade_lords_to_make_peace"),
					(assign, ":quest_return_penalty", -10),
					(assign, ":quest_expire_penalty", -13),
				(else_try),
					(eq, ":quest_no", "qst_deal_with_night_bandits"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -1),
					
				(else_try),
					(eq, ":quest_no", "qst_follow_spy"),
					(assign, ":quest_return_penalty", -2),
					(assign, ":quest_expire_penalty", -3),
					(try_begin),
						(party_is_active, "$qst_follow_spy_spy_party"),
						(remove_party, "$qst_follow_spy_spy_party"),
					(try_end),
					(try_begin),
						(party_is_active, "$qst_follow_spy_spy_partners_party"),
						(remove_party, "$qst_follow_spy_spy_partners_party"),
					(try_end),
				(else_try),
					(eq, ":quest_no", "qst_capture_enemy_hero"),
					(assign, ":quest_return_penalty", -3),
					(assign, ":quest_expire_penalty", -4),
				(else_try),
					(eq, ":quest_no", "qst_lend_companion"), #MV fix for Native bug when lords disappear or wars start
					(quest_get_slot, ":quest_target_troop", "qst_lend_companion", slot_quest_target_troop),
					(troop_set_slot, ":quest_target_troop", slot_troop_current_mission, npc_mission_rejoin_when_possible), 
			(troop_set_slot, ":quest_target_troop", slot_troop_days_on_mission, 0),
					##      (else_try),
					##        (eq, ":quest_no", "qst_lend_companion"),
					##        (quest_get_slot, ":quest_target_troop", "qst_lend_companion", slot_quest_target_troop),
					##        (party_add_members, "p_main_party", ":quest_target_troop", 1),
					##      (else_try),
					##        (eq, ":quest_no", "qst_capture_conspirators"),
					##      (else_try),
					##        (eq, ":quest_no", "qst_defend_nobles_against_peasants"),
				(else_try),
					(eq, ":quest_no", "qst_incriminate_loyal_commander"),
					(assign, ":quest_return_penalty", -5),
					(assign, ":quest_expire_penalty", -6),
					##      (else_try),
					##        (eq, ":quest_no", "qst_hunt_down_raiders"),
					##      (else_try),
					##        (eq, ":quest_no", "qst_capture_prisoners"),
					##        #Enemy lord quests
				(else_try),
					(eq, ":quest_no", "qst_lend_surgeon"),
					
					#Kingdom lady quests
				(else_try),
					(eq, ":quest_no", "qst_rescue_lord_by_replace"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -1),
				(else_try),
					(eq, ":quest_no", "qst_deliver_message_to_prisoner_lord"),
					(assign, ":quest_return_penalty", 0),
					(assign, ":quest_expire_penalty", -1),
				(else_try),
					(eq, ":quest_no", "qst_duel_for_lady"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -1),
					
					#Kingdom Army quests
				(else_try),
					(eq, ":quest_no", "qst_follow_army"),
					(assign, ":quest_return_penalty", 0), #was -4
					(assign, ":quest_expire_penalty", 0), #was -5
				(else_try),
					(eq, ":quest_no", "qst_deliver_cattle_to_army"),
					(assign, ":quest_return_penalty", 0),
					(assign, ":quest_expire_penalty", 0),
				(else_try),
					(eq, ":quest_no", "qst_join_siege_with_army"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -2),
				(else_try),
					(eq, ":quest_no", "qst_scout_waypoints"),
					(assign, ":quest_return_penalty", 0),
					(assign, ":quest_expire_penalty", 0),
					
					#Village Elder quests
				(else_try),
					(eq, ":quest_no", "qst_deliver_grain"),
					(assign, ":quest_return_penalty", -6),
					(assign, ":quest_expire_penalty", -7),
				(else_try),
					(eq, ":quest_no", "qst_deliver_cattle"),
					(assign, ":quest_return_penalty", -3),
					(assign, ":quest_expire_penalty", -4),
				(else_try),
					(eq, ":quest_no", "qst_train_peasants_against_bandits"),
					(assign, ":quest_return_penalty", -4),
					(assign, ":quest_expire_penalty", -5),
					
					#Mayor quests
				(else_try),
					(eq, ":quest_no", "qst_deliver_wine"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -3),
					(val_add, "$debt_to_merchants_guild", "$qst_deliver_wine_debt"),
				(else_try),
					(eq, ":quest_no", "qst_move_cattle_herd"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -3),
				(else_try),
					(eq, ":quest_no", "qst_escort_merchant_caravan"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -3),
				(else_try),
					(eq, ":quest_no", "qst_troublesome_bandits"),
					(assign, ":quest_return_penalty", -1),
					(assign, ":quest_expire_penalty", -2),
					#Other quests
				(else_try),
					(eq, ":quest_no", "qst_join_faction"),
					(assign, ":quest_return_penalty", -3),
					(assign, ":quest_expire_penalty", -3),
					(try_begin),
						(call_script, "script_get_number_of_hero_centers", "trp_player"),
						(gt, reg0, 0),
						(call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
					(try_end),
					
					
					(try_begin), #if the vassalage is part of a surrender option, then the faction returns to a state of war
						(quest_slot_eq, "qst_join_faction", slot_quest_failure_consequence, 1),
						(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_player_supporters_faction", "$g_invite_faction", 0),
						(call_script, "script_change_player_honor", -5),
						(quest_set_slot, "qst_join_faction", slot_quest_failure_consequence, 0),
					(try_end),
					
					
					(assign, "$g_invite_faction", 0),
					(assign, "$g_invite_faction_lord", 0),
					(assign, "$g_invite_offered_center", 0),
				(else_try),
					(eq, ":quest_no", "qst_eliminate_bandits_infesting_village"),
					(assign, ":quest_return_penalty", -3),
					(assign, ":quest_expire_penalty", -3),
				(else_try),
					(ge, ":quest_no", "qst_resolve_dispute"),
					(assign, ":authority_loss", -2),
					(assign, ":quest_return_penalty", 0),
					(assign, ":quest_expire_penalty", 0),
				(else_try),
					(ge, ":quest_no", "qst_consult_with_minister"),
					(assign, ":authority_loss", -2),
					(assign, ":quest_return_penalty", 0),
					(assign, ":quest_expire_penalty", 0),
				(try_end),
				
				(try_begin),
					(gt, ":abort_type", 0),
					(lt, ":quest_no", "qst_resolve_dispute"),
					
					(quest_get_slot, ":quest_giver", ":quest_no", slot_quest_giver_troop),
					(assign, ":relation_penalty", ":quest_return_penalty"),
					(try_begin),
						(eq, ":abort_type", 2),
						(assign, ":relation_penalty", ":quest_expire_penalty"),
					(try_end),
					(try_begin),
						(this_or_next|is_between, ":quest_giver", village_elders_begin, village_elders_end),
						(is_between, ":quest_giver", mayors_begin, mayors_end),
						(quest_get_slot, ":quest_giver_center", ":quest_no", slot_quest_giver_center),
						(call_script, "script_change_player_relation_with_center", ":quest_giver_center", ":relation_penalty"),
					(else_try),
						(call_script, "script_change_player_relation_with_troop", ":quest_giver", ":relation_penalty"),
					(try_end),
				(try_end),
				
				(fail_quest, ":quest_no"),
				
				#NPC companion changes begin
				(try_begin),
					(gt, ":abort_type", 0),
					(neq, ":quest_no", "qst_consult_with_minister"),
					(neq, ":quest_no", "qst_resolve_dispute"),
					(neq, ":quest_no", "qst_visit_lady"),
					(neq, ":quest_no", "qst_formal_marriage_proposal"),
					(neq, ":quest_no", "qst_duel_courtship_rival"),
					(neq, ":quest_no", "qst_follow_army"),
					(neq, ":quest_no", "qst_denounce_lord"),
					(neq, ":quest_no", "qst_intrigue_against_lord"),
					(neq, ":quest_no", "qst_offer_gift"),
					(neq, ":quest_no", "qst_organize_feast"),
					
					(call_script, "script_objectionable_action", tmt_honest, "str_fail_quest"),
				(try_end),
				#NPC companion changes end
				
				(try_begin),
					(eq, ":quest_no", "qst_resolve_dispute"),
					(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
					(call_script, "script_change_player_right_to_rule", ":authority_loss"),
					(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
						(store_faction_of_troop, ":lord_faction", ":lord"),
						(eq, ":lord_faction", "fac_player_supporters_faction"),
						(call_script, "script_troop_change_relation_with_troop", ":lord", "trp_player", ":authority_loss"),
					(try_end),
				(try_end),
				
				
				(try_begin),
					(eq, ":quest_no", "qst_organize_feast"),
					(call_script, "script_add_notification_menu", "mnu_notification_feast_quest_expired", 0, 0),
				(try_end),
				
				
				(call_script, "script_end_quest", ":quest_no"),
		])

#script_start_quest
		# INPUT: arg1 = quest_no, arg2 = giver_troop_no, s2 = description_text
		# OUTPUT: none
start_quest = (
	"start_quest",
			[(store_script_param, ":quest_no", 1),
				(store_script_param, ":giver_troop_no", 2),
				
				(quest_set_slot, ":quest_no", slot_quest_giver_troop, ":giver_troop_no"),
				
				(try_begin),
					(eq, ":giver_troop_no", -1),
					(str_store_string, s63, "str_political_suggestion"),
				(else_try),
					(is_between, ":giver_troop_no", active_npcs_begin, active_npcs_end),
					(str_store_troop_name_link, s62, ":giver_troop_no"),
					(str_store_string, s63, "@Given by: {s62}"),
				(else_try),
					(str_store_troop_name, s62, ":giver_troop_no"),
					(str_store_string, s63, "@Given by: {s62}"),
				(try_end),
				(store_current_hours, ":cur_hours"),
				(str_store_date, s60, ":cur_hours"),
				(str_store_string, s60, "@Given on: {s60}"),
				(add_quest_note_from_sreg, ":quest_no", 0, s60, 0),
				(add_quest_note_from_sreg, ":quest_no", 1, s63, 0),
				(add_quest_note_from_sreg, ":quest_no", 2, s2, 0),
				
				(try_begin),
					(quest_slot_ge, ":quest_no", slot_quest_expiration_days, 1),
					(quest_get_slot, reg0, ":quest_no", slot_quest_expiration_days),
					(add_quest_note_from_sreg, ":quest_no", 7, "@You have {reg0} days to finish this quest.", 0),
				(try_end),
				
				#Adding dont_give_again_for_days value
				(try_begin),
					(quest_slot_ge, ":quest_no", slot_quest_dont_give_again_period, 1),
					(quest_get_slot, ":dont_give_again_period", ":quest_no", slot_quest_dont_give_again_period),
					(quest_set_slot, ":quest_no", slot_quest_dont_give_again_remaining_days, ":dont_give_again_period"),
				(try_end),
				(start_quest, ":quest_no", ":giver_troop_no"),
				
				(try_begin),
					(eq, ":quest_no", "qst_report_to_army"),
					(assign, "$number_of_report_to_army_quest_notes", 8),
					(faction_get_slot, ":faction_ai_state", "$players_kingdom", slot_faction_ai_state),
					(call_script, "script_update_report_to_army_quest_note", "$players_kingdom", ":faction_ai_state", -1),
				(try_end),
				
				(display_message, "str_quest_log_updated"),
		])
		
		#script_conclude_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
conclude_quest = (
	"conclude_quest",
			[
				(store_script_param, ":quest_no", 1),
				(conclude_quest, ":quest_no"),
				(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
				(str_store_troop_name, s59, ":quest_giver_troop"),
				(add_quest_note_from_sreg, ":quest_no", 7, "@This quest has been concluded. Talk to {s59} to finish it.", 0),
		])
		
		#script_succeed_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
succeed_quest = (
	"succeed_quest",
			[
				(store_script_param, ":quest_no", 1),
				(succeed_quest, ":quest_no"),
				(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
				(str_store_troop_name, s59, ":quest_giver_troop"),
				(add_quest_note_from_sreg, ":quest_no", 7, "@This quest has been successfully completed. Talk to {s59} to claim your reward.", 0),
		])
		
		#script_fail_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
fail_quest = (
	"fail_quest",
			[
				(store_script_param, ":quest_no", 1),
				(fail_quest, ":quest_no"),
				(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
				(str_store_troop_name, s59, ":quest_giver_troop"),
				(add_quest_note_from_sreg, ":quest_no", 7, "@This quest has failed. Talk to {s59} to explain the situation.", 0),
		])
		
		#script_report_quest_troop_positions
		# INPUT: arg1 = quest_no, arg2 = troop_no, arg3 = note_index
		# OUTPUT: none
report_quest_troop_positions = (
	"report_quest_troop_positions",
			[
				(store_script_param, ":quest_no", 1),
				(store_script_param, ":troop_no", 2),
				(store_script_param, ":note_index", 3),
				(call_script, "script_get_information_about_troops_position", ":troop_no", 1),
				(str_store_string, s5, "@At the time quest was given:^{s1}"),
				(add_quest_note_from_sreg, ":quest_no", ":note_index", s5, 1),
				(call_script, "script_update_troop_location_notes", ":troop_no", 1),
		])
		
		#script_end_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
end_quest = (
	"end_quest",
			[
				(store_script_param, ":quest_no", 1),
				(str_clear, s1),
				(add_quest_note_from_sreg, ":quest_no", 0, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 1, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 2, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 3, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 4, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 5, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 6, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 7, s1, 0),
				(try_begin),
					(neg|check_quest_failed, ":quest_no"),
					(val_add, "$g_total_quests_completed", 1),
				(try_end),
				(try_begin),
					(eq, ":quest_no", "qst_consult_with_minister"),
					(assign, "$g_minister_notification_quest", 0),
				(try_end),
				(complete_quest, ":quest_no"),
				(try_begin),
					(is_between, ":quest_no", mayor_quests_begin, mayor_quests_end),
					(assign, "$merchant_quest_last_offerer", -1),
					(assign, "$merchant_offered_quest", -1),
				(try_end),
		])
		
		#script_cancel_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
cancel_quest = (
	"cancel_quest",
			[(store_script_param, ":quest_no", 1),
				(str_clear, s1),
				(add_quest_note_from_sreg, ":quest_no", 0, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 1, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 2, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 3, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 4, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 5, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 6, s1, 0),
				(add_quest_note_from_sreg, ":quest_no", 7, s1, 0),
				(cancel_quest, ":quest_no"),
				(try_begin),
					(is_between, ":quest_no", mayor_quests_begin, mayor_quests_end),
					(assign, "$merchant_quest_last_offerer", -1),
					(assign, "$merchant_offered_quest", -1),
				(try_end),
		])
		
		
