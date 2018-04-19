from header import *

# script_diplomacy_start_war_between_kingdoms
		# sets relations between two kingdoms and their vassals.
		# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
		# Output: none
diplomacy_start_war_between_kingdoms = (
	"diplomacy_start_war_between_kingdoms", #sets relations between two kingdoms and their vassals.
			[
				(store_script_param, ":kingdom_a", 1),
				(store_script_param, ":kingdom_b", 2),
				(store_script_param, ":initializing_war_peace_cond", 3), #1 = after start of game
				
				(call_script, "script_npc_decision_checklist_peace_or_war", ":kingdom_a", ":kingdom_b", -1),
				(assign, ":explainer_string", reg1),
				
				#
				(try_begin),
					(eq, ":kingdom_a", "fac_player_supporters_faction"),
					(assign, ":war_event", logent_player_faction_declares_war),
				(else_try),
					(eq, ":explainer_string", "str_s12s15_declared_war_to_control_calradia"),
					(assign, ":war_event", logent_player_faction_declares_war), #for savegame compatibility, this event stands in for the attempt to declare war on all of calradia
				(else_try),
					(eq, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
					(assign, ":war_event", logent_faction_declares_war_out_of_personal_enmity),
				(else_try),
					(eq, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
					(assign, ":war_event", logent_faction_declares_war_out_of_personal_enmity),
				(else_try),
					(eq, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
					(assign, ":war_event", logent_faction_declares_war_to_regain_territory),
				(else_try),
					(eq, ":explainer_string", "str_s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects"),
					(assign, ":war_event", logent_faction_declares_war_to_respond_to_provocation),
				(else_try),
					(eq, ":explainer_string", "str_s12s15_is_alarmed_by_the_growing_power_of_s16"),
					(assign, ":war_event", logent_faction_declares_war_to_curb_power),
				(try_end),
				(call_script, "script_add_log_entry", ":war_event", ":kingdom_a", 0, 0, ":kingdom_b"),
				
				
				
				(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":kingdom_a", ":kingdom_b"),
				(assign, ":current_diplomatic_status", reg0),
				(try_begin), #effects of policy only after the start of the game
					(eq, ":initializing_war_peace_cond", 1),
					(eq, ":current_diplomatic_status", -1),
					(call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_declares_war_with_justification),
				(else_try),
					(eq, ":initializing_war_peace_cond", 1),
					(eq, ":current_diplomatic_status", 0),
					(call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_attacks_without_provocation),
				(else_try),
					(eq, ":current_diplomatic_status", 1),
					(call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_breaks_truce),
				(try_end),
				
				(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
				(val_min, ":relation", -10),
				(val_add, ":relation", -30),
				(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
				
				(try_begin),
					(eq, "$players_kingdom", ":kingdom_a"),
					(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
					(val_min, ":relation", -30),
					(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
				(else_try),
					(eq, "$players_kingdom", ":kingdom_b"),
					(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
					(val_min, ":relation", -30),
					(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
				(try_end),
				
				(try_begin),
					(eq, ":initializing_war_peace_cond", 1),
					
					#Remove this -- this scrambles who declares war on whom
					#        (try_begin),
					#         (store_random_in_range, ":random_no", 0, 2),
					#        (this_or_next|eq, ":kingdom_a", "fac_player_supporters_faction"),
					#		(eq, ":random_no", 0),
					#     (assign, ":local_temp", ":kingdom_a"),
					#    (assign, ":kingdom_a", ":kingdom_b"),
					#   (assign, ":kingdom_b", ":local_temp"),
					#(try_end),
					
					(str_store_faction_name_link, s1, ":kingdom_a"),
					(str_store_faction_name_link, s2, ":kingdom_b"),
					(display_log_message, "@{s1} has declared war against {s2}."),
					
					(store_current_hours, ":hours"),
					(faction_set_slot, ":kingdom_a", slot_faction_ai_last_decisive_event, ":hours"),
					(faction_set_slot, ":kingdom_b", slot_faction_ai_last_decisive_event, ":hours"),
					
					#set provocation and truce days
					(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
					(store_add, ":provocation_slot", ":kingdom_b", slot_faction_provocation_days_with_factions_begin),
					(val_sub, ":truce_slot", kingdoms_begin),
					(val_sub, ":provocation_slot", kingdoms_begin),
					(faction_set_slot, ":kingdom_a", ":truce_slot", 0),
					(faction_set_slot, ":kingdom_a", ":provocation_slot", 0),
					
					(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
					(store_add, ":provocation_slot", ":kingdom_a", slot_faction_provocation_days_with_factions_begin),
					(val_sub, ":truce_slot", kingdoms_begin),
					(val_sub, ":provocation_slot", kingdoms_begin),
					(faction_set_slot, ":kingdom_b", ":truce_slot", 0),
					(faction_set_slot, ":kingdom_b", ":provocation_slot", 0),
					
					(call_script, "script_add_notification_menu", "mnu_notification_war_declared", ":kingdom_a", ":kingdom_b"),
					
					(call_script, "script_update_faction_notes", ":kingdom_a"),
					(call_script, "script_update_faction_notes", ":kingdom_b"),
					
					# (call_script, "script_raf_set_ai_recalculation_flags", ":kingdom_a"),
					# (call_script, "script_raf_set_ai_recalculation_flags", ":kingdom_b"),
					(assign, "$g_recalculate_ais", 1),
				(try_end),
				
				(try_begin),
					(check_quest_active, "qst_cause_provocation"),
					(neg|check_quest_succeeded, "qst_cause_provocation"),
					(this_or_next|eq, "$players_kingdom", ":kingdom_a"),
					(eq, "$players_kingdom", ":kingdom_b"),
					(call_script, "script_abort_quest", "qst_cause_provocation", 0),
				(try_end),
		])
		
		#script_diplomacy_party_attacks_neutral
		# called from game_menus (plundering a village, raiding a village),  from dialogs: surprise attacking a neutral lord, any attack on caravan or villagers
		# WARNING: modified by 1257AD devs
		# INPUT: attacker_party, defender_party
		# OUTPUT: none
diplomacy_party_attacks_neutral	= (
	"diplomacy_party_attacks_neutral", #called from game_menus (plundering a village, raiding a village),  from dialogs: surprise attacking a neutral lord, any attack on caravan or villagers
			#Has no effect if factions are already at war
			[
				(store_script_param, ":attacker_party", 1),
				(store_script_param, ":defender_party", 2),
				
				(store_faction_of_party, ":attacker_faction", ":attacker_party"),
				(store_faction_of_party, ":defender_faction", ":defender_party"),
				
				(party_stack_get_troop_id, ":attacker_leader", ":attacker_party", 0),
				
				(try_begin),
					(eq, ":attacker_party", "p_main_party"),
					(neq, ":attacker_faction", "fac_player_supporters_faction"),
					(assign, ":attacker_faction", "$players_kingdom"),
				(else_try),
					(eq, ":attacker_party", "p_main_party"),
					(eq, ":attacker_faction", "fac_player_supporters_faction"),
				(try_end),
				
				(try_begin),
					(eq, ":attacker_party", "p_main_party"),
					(store_relation, ":relation", ":attacker_faction", ":defender_faction"),
					(ge, ":relation", 0),
					(call_script, "script_change_player_honor", -2),
				(try_end),
				
				
				(try_begin),
					(check_quest_active, "qst_cause_provocation"),
					(quest_slot_eq, "qst_cause_provocation", slot_quest_target_faction, ":defender_faction"),
					(quest_get_slot, ":giver_troop", "qst_cause_provocation", slot_quest_giver_troop),
					(store_faction_of_troop, ":attacker_faction", ":giver_troop"),
					(call_script, "script_succeed_quest", "qst_cause_provocation"),
				(try_end),
				
				(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":attacker_faction", ":defender_faction"),
				(assign, ":diplomatic_status", reg0),
				
				(try_begin),
					(eq, ":attacker_faction", "fac_player_supporters_faction"),
					(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
					#player faction inactive, no effect
				(else_try),
					(eq, ":diplomatic_status", -2),
					#war, no effect
				(else_try),
					
					(eq, ":attacker_faction", "fac_player_supporters_faction"),
					(faction_slot_eq, ":attacker_faction", slot_faction_leader, "trp_player"),
					(call_script, "script_faction_follows_controversial_policy", "fac_player_supporters_faction",logent_policy_ruler_attacks_without_provocation),
				(else_try),
					(eq, ":diplomatic_status", 1),
					#truce
					(party_stack_get_troop_id, ":defender_party_leader", ":defender_party", 0),
					(try_begin),
						(neg|is_between, ":defender_party_leader", active_npcs_begin, active_npcs_end),
						(store_faction_of_party, ":defender_party_faction", ":defender_party"),
						(faction_get_slot, ":defender_party_leader", ":defender_party_faction", slot_faction_leader),
					(try_end),
					
					(call_script, "script_add_log_entry", logent_border_incident_troop_breaks_truce, ":attacker_leader", -1, ":defender_party_leader", ":attacker_faction"),
				(else_try),
					#truce
					#rafi
					(party_stack_get_troop_id, ":defender_party_leader", ":defender_party", 0),
					(try_begin),
						(neg|is_between, ":defender_party_leader", active_npcs_begin, active_npcs_end),
						(store_faction_of_party, ":defender_party_faction", ":defender_party"),
						(faction_get_slot, ":defender_party_leader", ":defender_party_faction", slot_faction_leader),
					(try_end),
					# end rafi
					(call_script, "script_add_log_entry", logent_border_incident_troop_attacks_neutral, ":attacker_leader", -1, ":defender_party_leader", ":attacker_faction"),
				(try_end),
				
				(try_begin),
					(is_between, ":defender_party", villages_begin, villages_end),
					(call_script, "script_add_log_entry", logent_village_raided, ":attacker_leader",  ":defender_party", -1, ":defender_faction"),
				(else_try),
					(party_get_template_id, ":template", ":defender_party"),
					(neq, ":template", "pt_kingdom_hero_party"),
					(try_begin),
						(ge, "$cheat_mode", 1),
						(str_store_faction_name, s5, ":defender_faction"),
						(display_message, "@{!}DEbug - {s5} caravan attacked"),
					(try_end),
					
					(call_script, "script_add_log_entry", logent_caravan_accosted, ":attacker_leader",  -1, -1, ":defender_faction"),
				(try_end),
				
				(store_add, ":slot_truce_days", ":attacker_faction", slot_faction_provocation_days_with_factions_begin),
				(val_sub, ":slot_truce_days", kingdoms_begin),
				(faction_set_slot, ":defender_faction", ":slot_truce_days", 0),
				
				(store_add, ":slot_provocation_days", ":attacker_faction", slot_faction_provocation_days_with_factions_begin),
				(val_sub, ":slot_provocation_days", kingdoms_begin),
				(try_begin),
					(neq, ":diplomatic_status", -2),
					(faction_slot_eq, ":defender_faction", ":slot_provocation_days", 0),
					(faction_set_slot, ":defender_faction", ":slot_provocation_days", 30),
				(try_end),
		])
		

		# script_diplomacy_start_peace_between_kingdoms
		# this procedure includes diplomacy mods
		# WARNING: modified by 1257AD devs
		# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
		# Output: none
diplomacy_start_peace_between_kingdoms	= (
	"diplomacy_start_peace_between_kingdoms", #sets relations between two kingdoms
			[
				(store_script_param, ":kingdom_a", 1),
				(store_script_param, ":kingdom_b", 2),
				(store_script_param, ":initializing_war_peace_cond", 3), #set to 1 if not the start of the game
				
				(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
				(val_max, ":relation", 0),
				(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
				(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
				
				(try_begin),
					(eq, "$players_kingdom", ":kingdom_a"),
					(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
					(val_max, ":relation", 0),
					(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
					(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
				(else_try),
					(eq, "$players_kingdom", ":kingdom_b"),
					(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
					(val_max, ":relation", 0),
					(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
					(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
				(try_end),
				
				(try_for_range, ":cur_center", centers_begin, centers_end),
					(store_faction_of_party, ":faction_no", ":cur_center"),
					(this_or_next|eq, ":faction_no", ":kingdom_a"),
					(eq, ":faction_no", ":kingdom_b"),
					(party_get_slot, ":besieger_party", ":cur_center", slot_center_is_besieged_by),
					(ge, ":besieger_party", 0), #town is under siege
					(party_is_active, ":besieger_party"),
					(store_faction_of_party, ":besieger_party_faction_no", ":besieger_party"),
					(this_or_next|eq, ":besieger_party_faction_no", ":kingdom_a"),
					(eq, ":besieger_party_faction_no", ":kingdom_b"),
					(call_script, "script_lift_siege", ":cur_center", 0),
				(try_end),
				
				(try_begin),
					(this_or_next|eq, "$players_kingdom", ":kingdom_a"),
					(eq, "$players_kingdom", ":kingdom_b"),
					
					(ge, "$g_player_besiege_town", 0),
					(party_is_active, "$g_player_besiege_town"),
					
					(store_faction_of_party, ":besieged_center_faction_no", "$g_player_besiege_town"),
					
					(this_or_next|eq, ":besieged_center_faction_no", ":kingdom_a"),
					(eq, ":besieged_center_faction_no", ":kingdom_b"),
					
					(call_script, "script_lift_siege", "$g_player_besiege_town", 0),
					(assign, "$g_player_besiege_town", -1),
				(try_end),
				
				(try_begin),
					(eq, ":initializing_war_peace_cond", 1),
					(str_store_faction_name_link, s1, ":kingdom_a"),
					(str_store_faction_name_link, s2, ":kingdom_b"),
					(display_log_message, "@{s1} and {s2} have made peace with each other."),
					(call_script, "script_add_notification_menu", "mnu_notification_peace_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
					(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
					(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
					(assign, "$g_recalculate_ais", 1),
					# (call_script, "script_raf_set_ai_recalculation_flags", ":kingdom_a"),
					# (call_script, "script_raf_set_ai_recalculation_flags", ":kingdom_b"),
					
				(try_end),
				
				(try_begin), #add truce
					(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
					(val_sub, ":truce_slot", kingdoms_begin),
					##diplomacy begin
					#(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
					(faction_set_slot, ":kingdom_b", ":truce_slot", 20),
					##diplomacy end
					(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
					(val_sub, ":truce_slot", kingdoms_begin),
					##diplomacy begin
					#(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
					(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
					##diplomacy end
					(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
					(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
					#(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
					(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
					(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
					(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
					#(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
					(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
				(try_end),
		])
		

		# script_event_kingdom_make_peace_with_kingdom
		# Input: arg1 = source_kingdom, arg2 = target_kingdom
		# Output: none
event_kingdom_make_peace_with_kingdom	= (
	"event_kingdom_make_peace_with_kingdom",
			[
				(store_script_param_1, ":source_kingdom"),
				(store_script_param_2, ":target_kingdom"),
				(try_begin),
					(check_quest_active, "qst_capture_prisoners"),
					(try_begin),
						(eq, "$players_kingdom", ":source_kingdom"),
						(quest_slot_eq, "qst_capture_prisoners", slot_quest_target_faction, ":target_kingdom"),
						(call_script, "script_cancel_quest", "qst_capture_prisoners"),
					(else_try),
						(eq, "$players_kingdom", ":target_kingdom"),
						(quest_slot_eq, "qst_capture_prisoners", slot_quest_target_faction, ":source_kingdom"),
						(call_script, "script_cancel_quest", "qst_capture_prisoners"),
					(try_end),
				(try_end),
				
				(try_begin),
					(check_quest_active, "qst_capture_enemy_hero"),
					(try_begin),
						(eq, "$players_kingdom", ":source_kingdom"),
						(quest_slot_eq, "qst_capture_enemy_hero", slot_quest_target_faction, ":target_kingdom"),
						(call_script, "script_cancel_quest", "qst_capture_enemy_hero"),
					(else_try),
						(eq, "$players_kingdom", ":target_kingdom"),
						(quest_slot_eq, "qst_capture_enemy_hero", slot_quest_target_faction, ":source_kingdom"),
						(call_script, "script_cancel_quest", "qst_capture_enemy_hero"),
					(try_end),
				(try_end),
				
				
				
				(try_begin),
					(check_quest_active, "qst_persuade_lords_to_make_peace"),
					(quest_get_slot, ":lord_1", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
					(quest_get_slot, ":lord_2", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
					
					(try_begin),
						(lt, ":lord_1", 0),
						(val_mul, ":lord_1", -1),
					(try_end),
					(try_begin),
						(lt, ":lord_2", 0),
						(val_mul, ":lord_2", -1),
					(try_end),
					
					
					(store_faction_of_troop, ":lord_1_faction", ":lord_1"),
					(store_faction_of_troop, ":lord_2_faction", ":lord_2"),
					
					(this_or_next|eq, ":lord_1_faction", ":source_kingdom"),
					(eq, ":lord_2_faction", ":source_kingdom"),
					
					(this_or_next|eq, ":lord_1_faction", ":target_kingdom"),
					(eq, ":lord_2_faction", ":target_kingdom"),
					
					(call_script, "script_cancel_quest", "qst_persuade_lords_to_make_peace"),
					
				(try_end),
				
				#Rescue prisoners cancelled in simple_triggers
				
				(try_begin),
					(this_or_next|faction_slot_eq, ":target_kingdom", slot_faction_leader, "trp_player"),
					(faction_slot_eq, ":source_kingdom", slot_faction_leader, "trp_player"),
					
					(call_script, "script_change_player_right_to_rule", 3),
				(try_end),
				
		])

		# script_randomly_start_war_peace
		# Aims to introduce a slightly simpler system in which the AI kings' reasoning could be made more  transparent to the player. 
		# At the start of the game, this may lead to less variation in outcomes, though
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = initializing_war_peace_cond (1 = true, 0 = false)
		# Output: none
randomly_start_war_peace_new	= (
	"randomly_start_war_peace_new",
			[
				(store_script_param_1, ":initializing_war_peace_cond"),
				
				(assign, ":players_kingdom_at_peace", 0), #if the player kingdom is at peace, then create an enmity
				(try_begin),
					(is_between, "$players_kingdom", "fac_kingdom_1", kingdoms_end),
					(assign, ":players_kingdom_at_peace", 1),
				(try_end),
				
				#(try_for_range, ":cur_kingdom", "fac_kingdom_1", kingdoms_end),
				(assign, ":cur_kingdom", "$g_diplo_kingdom"),
				(try_begin),
					(faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
					(neq, ":cur_kingdom", "fac_player_supporters_faction"), #tom
			#(neq, ":cur_kingdom", "fac_papacy"), #tom
					(try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
						(neq, ":cur_kingdom", ":cur_kingdom_2"),
						
						(faction_slot_eq, ":cur_kingdom_2", slot_faction_state, sfs_active),
						
						(call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom", ":cur_kingdom_2", -1),
						(assign, ":kingdom_1_to_kingdom_2", reg0),
						
						(store_relation, ":cur_relation", ":cur_kingdom", ":cur_kingdom_2"),
						(call_script, "script_distance_between_factions", ":cur_kingdom", ":cur_kingdom_2"),
						(assign, ":fac_distance", reg0),
						(try_begin),
							(lt, ":cur_relation", 0), #AT WAR
							(this_or_next | eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
							(gt, ":fac_distance", 0),
							
							(try_begin),
								(eq, ":cur_kingdom", "$players_kingdom"),
								(assign, ":players_kingdom_at_peace", 0),
							(try_end),
							
							(ge, ":kingdom_1_to_kingdom_2", 1),
							
							(try_begin),
								(eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
								
								(store_mul, ":goodwill_level", ":kingdom_1_to_kingdom_2", 2),
								(store_random_in_range, ":random", 0, 20),
								(try_begin),
									(lt, ":random", ":goodwill_level"),
									(call_script, "script_add_notification_menu", "mnu_question_peace_offer", ":cur_kingdom", 0),
								(try_end),
							(else_try),
								(call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom_2", ":cur_kingdom", -1),
								(assign, ":kingdom_2_to_kingdom_1", reg0),
								(ge, ":kingdom_2_to_kingdom_1", 1),
								
								(store_mul, ":goodwill_level", ":kingdom_1_to_kingdom_2", ":kingdom_2_to_kingdom_1"),
								(store_random_in_range, ":random", 0, 20),
								(lt, ":random", ":goodwill_level"),
								
								(try_begin),
									(eq, "$g_include_diplo_explanation", 0),
									(assign, "$g_include_diplo_explanation", ":cur_kingdom"),
									(str_store_string, s57, "str_s14"),
								(try_end),
								
								(call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
							(try_end),
						(else_try),
							(ge, ":cur_relation", 0), #AT PEACE
							
							(call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom", ":cur_kingdom_2", -1),
							
							#negative, leans towards war/positive, leans towards peace
							(le, reg0, 0), #still no chance of war unless provocation, or at start of game
							
							(assign, ":hostility", reg0),
							
							(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_kingdom", ":cur_kingdom_2"),
							(le, reg0, 0), #no truce
							
							# rafi
							(assign, ":provocation", 0),
							(try_begin),
								(eq, reg0, -1),
								(assign, ":provocation", 30),
							(try_end),
							
							(val_add, ":hostility", ":provocation"),
							#(val_add, ":hostility", reg0), #increase hostility if there is a provocation
							
							(val_sub, ":hostility", 1), #greater chance at start of game
							(val_add, ":hostility", ":initializing_war_peace_cond"), #this variable = 1 after the start
							
							(store_mul, ":hostility_squared", ":hostility", ":hostility"),
							(store_random_in_range, ":random", 0, 50),
							(lt, ":random", ":hostility_squared"),
							
							(try_begin),
								(eq, "$g_include_diplo_explanation", 0),
								(assign, "$g_include_diplo_explanation", ":cur_kingdom"),
								(str_store_string, s57, "str_s14"),
							(try_end),
							(call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
							
							(try_begin), #do some war damage for
								(eq, ":initializing_war_peace_cond", 0),
								(store_random_in_range, ":war_damage_inflicted", 10, 120),
								(store_add, ":slot_war_damage_inflicted", ":cur_kingdom", slot_faction_war_damage_inflicted_on_factions_begin),
								(val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
								(faction_set_slot, ":cur_kingdom_2",  ":slot_war_damage_inflicted", ":war_damage_inflicted"),
								
								(store_add, ":slot_war_damage_inflicted", ":cur_kingdom_2", slot_faction_war_damage_inflicted_on_factions_begin),
								(val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
								(faction_set_slot, ":cur_kingdom", ":slot_war_damage_inflicted", ":war_damage_inflicted"),
							(try_end),
						(try_end),
					(try_end),
				(try_end),
				
				(try_begin),
					(eq, ":players_kingdom_at_peace", 1),
					(val_add, "$players_kingdom_days_at_peace", 1),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg3, "$players_kingdom_days_at_peace"),
						(display_message, "@{!}DEBUG -- Player's kingdom has had {reg3} days of peace"),
					(try_end),
				(else_try),
					(assign, "$players_kingdom_days_at_peace", 0),
				(try_end),
				
		])