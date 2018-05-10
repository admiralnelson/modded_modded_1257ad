from header import *

#script_npc_decision_checklist_peace_or_war
	# WARNING: heavily modified by 1257AD devs
	#INPUT: actor_faction, target_faction, envoy
	#OUTPUT: s14 explainer_string, reg0 result, reg1 explainer_string
npc_decision_checklist_peace_or_war =	(
		"npc_decision_checklist_peace_or_war",
		#this script is used to add a bit more color to diplomacy, particularly with regards to the player
		
		[
		(store_script_param, ":actor_faction", 1),
		(store_script_param, ":target_faction", 2),
		(store_script_param, ":envoy", 3),
		
		(assign, ":actor_strength", 0),
		(assign, ":target_strength", 0),
		(assign, ":actor_centers_held_by_target", 0),
		
		(assign, ":two_factions_share_border", 0),
		(assign, ":third_party_war", 0),
		(assign, ":num_third_party_wars", 0),
		
		(assign, ":active_mutual_enemy", 0), #an active enemy with which the target is at war
		(assign, "$g_concession_demanded", 0),
		
		(faction_get_slot, ":actor_religion", ":actor_faction", slot_faction_religion),
		(faction_get_slot, ":target_religion", ":target_faction", slot_faction_religion),
		
		(store_relation, ":current_faction_relation", ":actor_faction", ":target_faction"),
		
		(call_script, "script_distance_between_factions", ":actor_faction", ":target_faction"),
		(assign, ":war_distance", reg0),
		
		(try_begin),
			(eq, ":target_faction", "fac_player_supporters_faction"),
			(assign, ":modified_honor_and_relation", "$player_honor"), #this can be affected by the emissary's skill
			
			(val_add, ":target_strength", 2), #for player party
		(else_try),
			(assign, ":modified_honor_and_relation", 0), #this can be affected by the emissary's skill
		(try_end),
		
		(faction_get_slot, ":actor_leader", ":actor_faction", slot_faction_leader),
		(faction_get_slot, ":target_leader", ":target_faction", slot_faction_leader),
		
		(call_script, "script_troop_get_relation_with_troop", ":actor_leader", ":target_leader"),
		
		(assign, ":relation_bonus", reg0),
		(val_min, ":relation_bonus", 10),
		(val_add, ":modified_honor_and_relation", ":relation_bonus"),
		
		# rafi
		(try_begin),
			(le, ":war_distance", max_war_distance),
			(assign, ":two_factions_share_border", 1),
			# (else_try),
			# (eq, ":actor_faction", "fac_crusade"),
			# (eq, ":target_faction", "$g_crusade"),
			# (assign, ":two_factions_share_border", 1),
			# (val_sub, ":modified_honor_and_relation", religious_effect_crusade),
			# (else_try),
			# (eq, ":target_faction", "fac_crusade"),
			# (eq, ":actor_faction", "$g_crusade"),
			# (assign, ":two_factions_share_border", 1),
			# (val_sub, ":modified_honor_and_relation", religious_effect_crusade),
		(try_end),
		# rafi
		
		# rafi religious differences
		(assign, ":religious_differences", 0),
		(try_begin),
			(neq, ":actor_religion", ":target_religion"),
			(eq, ":two_factions_share_border", 1),
			(try_begin),
			(eq, ":actor_religion", religion_catholic),
			(eq, ":target_religion", religion_orthodox),
			(assign, ":religious_differences", 2),
			(else_try),
			(eq, ":target_religion", religion_catholic),
			(eq, ":actor_religion", religion_orthodox),
			(assign, ":religious_differences", 2),
			(else_try),
			(assign, ":religious_differences", 1),
			(try_end),
		(try_end),
		
		(try_begin),
			(eq, ":religious_differences", 1),
			(val_sub, ":modified_honor_and_relation", religious_effect_aggressive), # religion effect
		(else_try),
			(eq, ":religious_differences", 2),
			(val_sub, ":modified_honor_and_relation", religious_effect_docile),
		(try_end),
		# rafi
		
		
		
		(str_store_troop_name, s15, ":actor_leader"),
		(str_store_troop_name, s16, ":target_leader"),
		
		
		(assign, ":war_damage_suffered", 0),
		(assign, ":war_damage_inflicted", 0),
		
		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":actor_faction", ":target_faction"),
		(assign, ":war_peace_truce_status", reg0),
		(str_clear, s12),
		(try_begin),
			(eq, ":war_peace_truce_status", -2),
			(str_store_string, s12, "str_s15_is_at_war_with_s16_"),
			
			(store_add, ":war_damage_inflicted_slot", ":target_faction", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":war_damage_inflicted_slot", kingdoms_begin),
			(faction_get_slot, ":war_damage_inflicted", ":actor_faction", ":war_damage_inflicted_slot"),
			
			(store_add, ":war_damage_suffered_slot", ":actor_faction", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":war_damage_suffered_slot", kingdoms_begin),
			(faction_get_slot, ":war_damage_suffered", ":target_faction", ":war_damage_suffered_slot"),
			
			
		(else_try),
			#truce in effect
			(eq, ":war_peace_truce_status", 1),
			(str_store_string, s12, "str_in_the_short_term_s15_has_a_truce_with_s16_as_a_matter_of_general_policy_"),
		(else_try),
			#provocation noted
			(eq, ":war_peace_truce_status", -1),
			(str_store_string, s12, "str_in_the_short_term_s15_was_recently_provoked_by_s16_and_is_under_pressure_to_declare_war_as_a_matter_of_general_policy_"),
		(try_end),
		
		#clear for dialog with lords
		(try_begin),
			(is_between, "$g_talk_troop", active_npcs_begin, active_npcs_end),
			(str_clear, s12),
		(try_end),
		
		(try_begin),
			(gt, ":envoy", -1),
			(store_skill_level, ":persuasion_x_2", "skl_persuasion", ":envoy"),
			(val_mul, ":persuasion_x_2", 2),
			(val_add, ":modified_honor_and_relation", ":persuasion_x_2"),
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg4, ":modified_honor_and_relation"),
			(display_message, "str_envoymodified_diplomacy_score_honor_plus_relation_plus_envoy_persuasion_=_reg4"),
			(try_end),
			
		(try_end),
		
		
		(try_for_range, ":kingdom_to_reset", kingdoms_begin, kingdoms_end),
			(faction_set_slot, ":kingdom_to_reset", slot_faction_temp_slot, 0),
		(try_end),
		
		(try_for_parties, ":party_no"),
			(assign, ":party_value", 0),
			# (try_begin),
				# (is_between, ":party_no", towns_begin, towns_end),
				# (assign, ":party_value", 3),
			# (else_try),
				# (is_between, ":party_no", castles_begin, castles_end),
				# (assign, ":party_value", 2),
			# (else_try),
				# (is_between, ":party_no", villages_begin, villages_end),
				# (assign, ":party_value", 1),
			# (else_try),
				# (party_get_template_id, ":template", ":party_no"),
				# (eq, ":template", "pt_kingdom_hero_party"),
				# (assign, ":party_value", 2),
			# (try_end),
			
			(store_faction_of_party, ":party_current_faction", ":party_no"),
			(party_get_slot, ":party_original_faction", ":party_no", slot_center_original_faction),
			(party_get_slot, ":party_ex_faction", ":party_no", slot_center_ex_faction),
			
			# rafi
			(try_begin),
			(is_between, ":party_current_faction", kingdoms_begin, kingdoms_end),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_town),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_mongol_party), #rom
			(party_slot_eq, ":party_no", slot_party_type, spt_patrol),
			(party_get_slot, ":party_value", ":party_no", slot_party_cached_strength),
			(le, ":party_value", 0),
			(store_party_size_wo_prisoners, ":psize", ":party_no"),
			(gt, ":psize", 1),
			(call_script, "script_party_calculate_strength", ":party_no", 1),
			(assign, ":party_value", reg0),
			(try_end),
			# end rafi
			
			#total strengths
			(try_begin),
			(is_between, ":party_current_faction", kingdoms_begin, kingdoms_end),
			(faction_get_slot, ":faction_strength", ":party_current_faction", slot_faction_temp_slot),
			(val_add, ":faction_strength", ":party_value"),
			(faction_set_slot, ":party_current_faction", slot_faction_temp_slot, ":faction_strength"),
			(try_end),
			
			
			(try_begin),
			(eq, ":party_current_faction", ":target_faction"),
			(val_add, ":target_strength", ":party_value"),
			
			(try_begin),
				(this_or_next|eq, ":party_original_faction", ":actor_faction"),
				(eq, ":party_ex_faction", ":actor_faction"),
				(val_add, ":actor_centers_held_by_target", 1),
				(try_begin),
				(is_between, ":party_no", walled_centers_begin, walled_centers_end),
				(assign, "$g_concession_demanded", ":party_no"),
				(str_store_party_name, s18, "$g_concession_demanded"),
				(try_end),
			(try_end),
			
			# Could include two factions share border, but war is unlikely to break out in the first place unless there is a common border
			
			# (try_begin),
			# (is_between, ":party_no", walled_centers_begin, walled_centers_end),
			# (try_for_range, ":other_center", walled_centers_begin, walled_centers_end),
			# (assign, ":two_factions_share_border", 0),
			# (store_faction_of_party, ":other_faction", ":other_center"),
			# (eq, ":other_faction", ":actor_faction"),
			# (store_distance_to_party_from_party, ":distance", ":party_no", ":other_center"),
			# (le, ":distance", 15),
			# (assign, ":two_factions_share_border", 1),
			# (try_end),
			# (try_end),
			(else_try),
			(eq, ":party_current_faction", ":actor_faction"),
			(val_add, ":actor_strength", ":party_value"),
			(try_end),
		(try_end),
		
		#Total Europe strength = 110 x 1 (villages,), 48? x 2 castles, 22 x 3 towns, 88 x 2 lord parties = 272 + 176 = 448
		(assign, ":strongest_kingdom", -1),
		(assign, ":score_to_beat", 60), #Maybe raise once it works
		(try_for_range, ":strongest_kingdom_candidate", kingdoms_begin, kingdoms_end),
			(faction_get_slot, ":candidate_strength", ":strongest_kingdom_candidate", slot_faction_temp_slot),
			(gt, ":candidate_strength", ":score_to_beat"),
			(assign, ":strongest_kingdom", ":strongest_kingdom_candidate"),
			(assign, ":score_to_beat", ":candidate_strength"),
		(try_end),
		
		
		(try_begin),
			(eq, "$cheat_mode", 2),
			(gt, ":strongest_kingdom", 1),
			(str_store_faction_name, s4, ":strongest_kingdom"),
			(assign, reg3, ":score_to_beat"),
			(display_message, "@{!}DEBUG - {s4} strongest kingdom with {reg3} strength"),
		(try_end),
		
		
		(assign, ":strength_ratio", 1),
		(try_begin),
			(gt, ":actor_strength", 0),
			(store_mul, ":strength_ratio", ":target_strength", 100),
			(val_div, ":strength_ratio", ":actor_strength"),
		(try_end),
		
		# rafi
		# (try_begin),
			# (eq, "$cheat_mode", 1),
			# (str_store_faction_name, s51, ":target_faction"),
			# (str_store_faction_name, s52, ":actor_faction"),
			# (assign, reg21, ":strength_ratio"),
			# (assign, reg22, ":target_strength"),
			# (assign, reg23, ":actor_strength"),
			# (assign, reg24, ":war_damage_suffered"),
			# (display_message, "@target: {s51} - {reg22} actor: {s52} - {reg23} strength ratio: {reg21} war damage: {reg24}"),
		# (try_end),
		# rafi
		
		(try_for_range, ":possible_mutual_enemy", kingdoms_begin, kingdoms_end),
			(neq, ":possible_mutual_enemy", ":target_faction"),
			(neq, ":possible_mutual_enemy", ":actor_faction"),
			(faction_slot_eq, ":possible_mutual_enemy", slot_faction_state, sfs_active),
			
			(store_relation, ":relation", ":possible_mutual_enemy", ":actor_faction"),
			(lt, ":relation", 0),
			(assign, ":third_party_war", ":possible_mutual_enemy"),
			(val_add, ":num_third_party_wars", 1),
			
			(store_relation, ":relation", ":possible_mutual_enemy", ":target_faction"),
			(lt, ":relation", 0),
			(assign, ":active_mutual_enemy", ":possible_mutual_enemy"),
		(try_end),
		
		(store_current_hours, ":cur_hours"),
		(faction_get_slot, ":faction_ai_last_decisive_event", ":actor_faction", slot_faction_ai_last_decisive_event),
		(store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
		
		(try_begin),
			(gt, "$supported_pretender", 0),
			(this_or_next|eq, "$supported_pretender", ":actor_leader"),
			(eq, "$supported_pretender", ":target_leader"),
			(this_or_next|eq, ":actor_faction", "$supported_pretender_old_faction"),
			(eq, ":target_faction", "$supported_pretender_old_faction"),
			
			(assign, ":result", -3),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_cannot_negotiate_with_s16_as_to_do_so_would_undermine_reg4herhis_own_claim_to_the_throne_this_civil_war_must_almost_certainly_end_with_the_defeat_of_one_side_or_another"),
			
			# rafi crusades
			# (else_try),
			# (eq, ":target_faction", "$g_crusade"),
			# (eq, ":actor_faction", "fac_crusade"),
			# (assign, ":result", -3),
			# (assign, ":explainer_string", "str_s12s15_is_participating_in_a_crusade_against_s16"),
			# end rafi
		(else_try),
			(gt, ":actor_centers_held_by_target", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Actor centers held by target noted"),
			(try_end),
			
			(lt, ":war_damage_suffered", 200),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}War damage under minimum"),
			(try_end),
			
			(lt, ":strength_ratio", 125),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Strength ratio correct"),
			(try_end),
			
			(eq, ":num_third_party_wars", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Third party wars"),
			(try_end),
			
			(assign, ":result", -2),
			(assign, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
			
			##tom -- papacy, everybody loves em
		(else_try),
			(eq, ":target_faction", "fac_papacy"),
			(eq, ":actor_religion", religion_catholic),
			(assign, ":result", 2),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_prefer_to_remain_friendly_to_s16_due_them_being_the_head_of_cataholic_church"),
			##tom
			# rafi
		(else_try),
			(lt, ":modified_honor_and_relation", 0),
			(gt, ":religious_differences", 0),
			(lt, ":strength_ratio", 125),
			(lt, ":war_damage_suffered", 100),
			(neq, ":war_peace_truce_status", 1),
			(eq, ":num_third_party_wars", 0),
			
			#(assign, ":result", -3),
			(assign, ":result", -1),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_distrusts_s16_due_to_religious_differences"),
			
			# rafi
			
		(else_try),
			(lt, ":modified_honor_and_relation", -20),
			(lt, ":strength_ratio", 125),
			#(lt, ":war_damage_suffered", 400),
			(lt, ":war_damage_suffered", 200),
			(this_or_next|neq, ":war_peace_truce_status", -2),
			(lt, ":hours_since_last_decisive_event", 720),
			
			(eq, ":num_third_party_wars", 0),
			
			(assign, ":result", -3),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
		(else_try),
			(gt, ":actor_centers_held_by_target", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Actor centers held by target noted"),
			(try_end),
			
			#(lt, ":war_damage_suffered", 200),
			(lt, ":war_damage_suffered", 100),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}War damage under minimum"),
			(try_end),
			
			(lt, ":strength_ratio", 125),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Strength ratio correct"),
			(try_end),
			
			(eq, ":num_third_party_wars", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Third party wars"),
			(try_end),
			
			(assign, ":result", -2),
			(assign, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(lt, ":strength_ratio", 125),
			(le, ":num_third_party_wars", 1),
			(ge, ":war_damage_inflicted", 5),
			(this_or_next|neq, ":war_peace_truce_status", -2),
			(lt, ":hours_since_last_decisive_event", 720),
			
			(store_mul, ":war_damage_suffered_x_2", ":war_damage_suffered", 2),
			(gt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
			
			(assign, ":result", -2),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_feels_that_reg4shehe_is_winning_the_war_against_s16_and_sees_no_reason_not_to_continue"),
		(else_try),
			(le, ":war_peace_truce_status", -1),
			
			(this_or_next|eq, ":war_peace_truce_status", -1), #either a war is just beginning, or there is a provocation
			(le, ":war_damage_inflicted", 1),
			
			(lt, ":strength_ratio", 150),
			(eq, ":num_third_party_wars", 0),
			
			#(faction_slot_ge, ":actor_faction", slot_faction_instability, 60),
			(faction_slot_ge, ":actor_faction", slot_faction_instability, 10), # rafi
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects"),
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(lt, ":war_damage_inflicted", 100),
			(eq, ":num_third_party_wars", 1),
			
			(assign, ":result", -1),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12even_though_reg4shehe_is_fighting_on_two_fronts_s15_is_inclined_to_continue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor"),
			
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(lt, ":war_damage_inflicted", 100),
			(eq, ":num_third_party_wars", 0),
			
			(assign, ":result", -1),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_feels_that_reg4shehe_must_pursue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor"),
		(else_try),
			(this_or_next|faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_attacking_center),
			(this_or_next|faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_raiding_village),
			(faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_attacking_enemy_army),
			(faction_get_slot, ":offensive_object", ":actor_faction", slot_faction_ai_object),
			(party_is_active, ":offensive_object"),
			(store_faction_of_party, ":offensive_object_faction", ":offensive_object"),
			(eq, ":offensive_object_faction", ":target_faction"),
			(str_store_party_name, s17, ":offensive_object"),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_is_currently_on_the_offensive_against_s17_now_held_by_s16_and_reluctant_to_negotiate"),
			
		(else_try),
			(eq, ":two_factions_share_border", 0),
			(assign, ":result", 10),
			(assign, ":explainer_string", "str_s12s15_is_too_far_to_engage_s16"),
			
		(else_try),
			#Attack strongest kingdom, if it is also at war
			(eq, ":strongest_kingdom", ":target_faction"),
			(eq, ":num_third_party_wars", 0),
			
			#Either not at war, or at war for two months
			(this_or_next|ge, ":war_peace_truce_status", -1),
			(lt, ":hours_since_last_decisive_event", 1440),
			
			(eq, ":two_factions_share_border", 1),
			
			(assign, ":at_least_one_other_faction_at_war_with_strongest", 0),
			(try_for_range, ":kingdom_to_check", kingdoms_begin, kingdoms_end),
			(neq, ":kingdom_to_check", ":actor_faction"),
			(neq, ":kingdom_to_check", ":target_faction"),
			(faction_slot_eq, ":kingdom_to_check", slot_faction_state, sfs_active),
			(store_relation, ":relation_of_factions", ":kingdom_to_check", ":target_faction"),
			(lt, ":relation_of_factions", 0),
			(assign, ":at_least_one_other_faction_at_war_with_strongest", 1),
			(try_end),
			(eq, ":at_least_one_other_faction_at_war_with_strongest", 1),
			
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_is_alarmed_by_the_growing_power_of_s16"),
			
			#bid to conquer all Calradia
		(else_try),
			(eq, ":num_third_party_wars", 0),
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- No third party wars for {s15}"),
			(try_end),
			(eq, ":actor_faction", ":strongest_kingdom"),
			#peace with no truce or provocation
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s15} is strongest kingdom"),
			(try_end),
			
			
			(faction_get_slot, ":actor_strength", ":actor_faction", slot_faction_temp_slot),
			(faction_get_slot, ":target_strength", ":target_faction", slot_faction_temp_slot),
			(store_sub, ":strength_difference", ":actor_strength", ":target_strength"),
			(ge, ":strength_difference", 30),
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s15} has 30 point advantage over {s16}"),
			(try_end),
			
			
			(assign, ":nearby_center_found", 0),
			(try_for_range, ":actor_faction_walled_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":walled_center_faction_1", ":actor_faction_walled_center"),
			(eq, ":walled_center_faction_1", ":actor_faction"),
			(try_for_range, ":target_faction_walled_center", walled_centers_begin, walled_centers_end),
				(store_faction_of_party, ":walled_center_faction_2", ":target_faction_walled_center"),
				(eq, ":walled_center_faction_2", ":target_faction"),
				(store_distance_to_party_from_party, ":distance", ":target_faction_walled_center", ":actor_faction_walled_center"),
				(lt, ":distance", 25),
				(assign, ":nearby_center_found", 1),
			(try_end),
			(try_end),
			(eq, ":nearby_center_found", 1),
			
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s15} has proximity to {s16}"),
			(try_end),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_declared_war_to_control_calradia"),
			
		(else_try),
			(lt, ":modified_honor_and_relation", 0),
			(eq, ":religious_differences", 1),
			(lt, ":strength_ratio", 125),
			(eq, ":num_third_party_wars", 0),
			(le, ":war_damage_suffered", 100),
			
			(assign, ":result", 0),
			(assign, ":explainer_string", "str_s12s15_distrusts_s16_due_to_religious_differences"),
			
		(else_try),
			(lt, ":modified_honor_and_relation", -20),
			
			(assign, ":result", 0),
			(assign, ":explainer_string", "str_s12s15_distrusts_s16_and_fears_that_any_deals_struck_between_the_two_realms_will_not_be_kept"),
			
			#wishes to deal
		(else_try),
			(lt, ":current_faction_relation", 0),
			(ge, ":num_third_party_wars", 2),
			(assign, ":result", 3),
			
			(assign, ":explainer_string", "str_s12s15_is_at_war_on_too_many_fronts_and_eager_to_make_peace_with_s16"),
		(else_try),
			(gt, ":active_mutual_enemy", 0),
			(eq, ":actor_centers_held_by_target", 0),
			(this_or_next|ge, ":current_faction_relation", 0),
			#(eq, ":two_factions_share_border", 0),
			#(eq, 1, 1),
			
			(assign, ":result", 3),
			(str_store_faction_name, s17, ":active_mutual_enemy"),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_seems_to_think_that_s16_and_reg4shehe_have_a_common_enemy_in_the_s17"),
			
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(ge, ":hours_since_last_decisive_event", 720),
			
			(troop_get_type, reg4, ":actor_leader"),
			
			(assign, ":result", 2),
			(assign, ":explainer_string", "str_s12s15_feels_frustrated_by_reg4herhis_inability_to_strike_a_decisive_blow_against_s16"),
			
			
		(else_try),
			(lt, ":current_faction_relation", 0),
			(gt, ":war_damage_suffered", 100),
			
			(val_mul, ":war_damage_suffered_x_2", 2),
			(lt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
			
			(assign, ":result", 2),
			(assign, ":explainer_string", "str_s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace"),
			
		(else_try),
			(gt, ":third_party_war", 0),
			(ge, ":modified_honor_and_relation", 0),
			(lt, ":current_faction_relation", 0),
			
			(assign, ":result", 1),
			(str_store_faction_name, s17, ":third_party_war"),
			(assign, ":explainer_string", "str_s12s15_would_like_to_firm_up_a_truce_with_s16_to_respond_to_the_threat_from_the_s17"),
		(else_try),
			(gt, ":third_party_war", 0),
			(ge, ":modified_honor_and_relation", 0),
			
			(assign, ":result", 1),
			(str_store_faction_name, s17, ":third_party_war"),
			(assign, ":explainer_string", "str_s12s15_wishes_to_be_at_peace_with_s16_so_as_to_pursue_the_war_against_the_s17"),
		(else_try),
			(gt, ":strength_ratio", 175),
			(eq, ":two_factions_share_border", 1),
			
			(assign, ":result", 1),
			(assign, ":explainer_string", "str_s12s15_seems_to_be_intimidated_by_s16_and_would_like_to_avoid_hostilities"),
		(else_try),
			(lt, ":current_faction_relation", 0),
			
			(assign, ":result", 1),
			(assign, ":explainer_string", "str_s12s15_has_no_particular_reason_to_continue_the_war_with_s16_and_would_probably_make_peace_if_given_the_opportunity"),
		(else_try),
			(assign, ":result", 1),
			(assign, ":explainer_string", "str_s12s15_seems_to_be_willing_to_improve_relations_with_s16"),
		(try_end),
		
		(str_store_string, s14, ":explainer_string"),
		(assign, reg0, ":result"),
		(assign, reg1, ":explainer_string"),
		
	])