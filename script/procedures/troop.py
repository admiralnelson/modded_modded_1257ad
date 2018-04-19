from header import *

#script_setup_talk_info
		# INPUT: $g_talk_troop, $g_talk_troop_relation
setup_talk_info	= (
	"setup_talk_info",
			[
				(talk_info_set_relation_bar, "$g_talk_troop_relation"),
				(str_store_troop_name, s61, "$g_talk_troop"),
				(str_store_string, s61, "@{!} {s61}"),
				(assign, reg1, "$g_talk_troop_relation"),
				(str_store_string, s62, "str_relation_reg1"),
				(talk_info_set_line, 0, s61),
				(talk_info_set_line, 1, s62),
				(call_script, "script_describe_relation_to_s63", "$g_talk_troop_relation"),
				(talk_info_set_line, 3, s63),
		])

		#NPC companion changes begin
		#script_setup_talk_info_companions
setup_talk_info_companions	= (
	"setup_talk_info_companions",
			[
				(call_script, "script_npc_morale", "$g_talk_troop"),
				(assign, ":troop_morale", reg0),
				
				(talk_info_set_relation_bar, ":troop_morale"),
				
				(str_store_troop_name, s61, "$g_talk_troop"),
				(str_store_string, s61, "@{!} {s61}"),
				(assign, reg1, ":troop_morale"),
				(str_store_string, s62, "str_morale_reg1"),
				(talk_info_set_line, 0, s61),
				(talk_info_set_line, 1, s62),
				(talk_info_set_line, 3, s63),
		])

		#script_setup_troop_meeting:
		# INPUT:
		# param1: troop_id with which meeting will be made.
		# param2: troop_dna (optional)
		
setup_troop_meeting	= (
	"setup_troop_meeting",
			[
				(store_script_param_1, ":meeting_troop"),
				(store_script_param_2, ":troop_dna"),
				(call_script, "script_get_meeting_scene"),
				(assign, ":meeting_scene", reg0),
				(modify_visitors_at_site,":meeting_scene"),
				(reset_visitors),
				(set_visitor,0,"trp_player"),
				(try_begin),
					(gt, ":troop_dna", -1),
					(set_visitor,17,":meeting_troop",":troop_dna"),
				(else_try),
					(set_visitor,17,":meeting_troop"),
				(try_end),
				(set_jump_mission,"mt_conversation_encounter"),
				(jump_to_scene,":meeting_scene"),
				(change_screen_map_conversation, ":meeting_troop"),
		])


		# script_change_troop_faction
		# Implementation of "lord defected" logic  
		# Input: arg1 = troop_no, arg2 = faction
change_troop_faction = (
	"change_troop_faction",
			[
				(store_script_param_1, ":troop_no"),
				(store_script_param_2, ":faction_no"),
				(try_begin),
					#Reactivating inactive or defeated faction
					(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
					(neg|faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
					(faction_set_slot, ":faction_no", slot_faction_state, sfs_active),
					#(call_script, "script_store_average_center_value_per_faction"),
				(try_end),
				
				#Political ramifications
				(store_faction_of_troop, ":orig_faction", ":troop_no"),
				#remove if he is marshal
				(try_begin),
					(faction_slot_eq, ":orig_faction", slot_faction_marshall, ":troop_no"),
					(call_script, "script_check_and_finish_active_army_quests_for_faction", ":orig_faction"),
					#No current issue on the agenda
					(try_begin),
						(faction_slot_eq, ":orig_faction", slot_faction_political_issue, 0),
						
						(faction_set_slot, ":orig_faction", slot_faction_political_issue, 1), #Appointment of marshal
						(store_current_hours, ":hours"),
						(val_max, ":hours", 0),
						(faction_set_slot, ":orig_faction", slot_faction_political_issue_time, ":hours"), #Appointment of marshal
						(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
							(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
							(eq, ":active_npc_faction", ":orig_faction"),
							(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
						(try_end),
						(try_begin),
							(eq, "$players_kingdom", ":orig_faction"),
							(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
						(try_end),
					(try_end),
					
					(try_begin),
						(troop_get_slot, ":old_marshall_party", ":troop_no", slot_troop_leaded_party),
						(party_is_active, ":old_marshall_party"),
						(party_set_marshall, ":old_marshall_party", 0),
					(try_end),
					
					(faction_set_slot, ":orig_faction", slot_faction_marshall, -1),
				(try_end),
				#Removal as marshal ends
				
				#Other political ramifications
				(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
				(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":active_npc", slot_troop_stance_on_faction_issue, ":troop_no"),
					(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
				(try_end),
				#Political ramifications end
				
				
				(try_begin),
					(ge, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":troop_no"),
					(display_message, "@{!}DEBUG - {s4} faction changed in normal faction change"),
				(try_end),
				
				(troop_set_faction, ":troop_no", ":faction_no"),
				(troop_set_slot, ":troop_no", slot_troop_recruitment_random, 0),
				(troop_set_slot, ":troop_no", slot_lord_recruitment_argument, 0),
				(troop_set_slot, ":troop_no", slot_lord_recruitment_candidate, 0),
				(troop_set_slot, ":troop_no", slot_troop_promised_fief, 0),
				
				#Give new title
				(call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
				
				(try_begin),
					(this_or_next|eq, ":faction_no", "$players_kingdom"),
					(eq, ":faction_no", "fac_player_supporters_faction"),
					(call_script, "script_check_concilio_calradi_achievement"),
				(try_end),
				
				#Takes walled centers and dependent villages with him
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(party_set_faction, ":center_no", ":faction_no"),
					(try_for_range, ":village_no", villages_begin, villages_end),
						(party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
						(party_set_faction, ":village_no", ":faction_no"),
						(party_get_slot, ":farmer_party_no", ":village_no", slot_village_farmer_party),
						(try_begin),
							(gt, ":farmer_party_no", 0),
							(party_is_active, ":farmer_party_no"),
							(party_set_faction, ":farmer_party_no", ":faction_no"),
						(try_end),
						(try_begin),
							(party_get_slot, ":old_town_lord", ":village_no", slot_town_lord),
							(neq, ":old_town_lord", ":troop_no"),
							(party_set_slot, ":village_no", slot_town_lord, stl_unassigned),
						(try_end),
					(try_end),
				(try_end),
				
				#Dependant kingdom ladies switch faction
				(try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
					(call_script, "script_get_kingdom_lady_social_determinants", ":kingdom_lady"),
					(assign, ":closest_male_relative", reg0),
					(assign, ":new_center", reg1),
					
					(eq, ":closest_male_relative", ":troop_no"),
					
					(try_begin),
						(ge, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":kingdom_lady"),
						(display_message, "@{!}DEBUG - {s4} faction changed by guardian moving"),
					(try_end),
					
					(troop_set_faction, ":kingdom_lady", ":faction_no"),
					(troop_slot_eq, ":kingdom_lady", slot_troop_prisoner_of_party, -1),
					(troop_set_slot, ":kingdom_lady", slot_troop_cur_center, ":new_center"),
				(try_end),
				
				#Remove his control over villages under another fortress
				(try_for_range, ":village_no", villages_begin, villages_end),
					(party_slot_eq, ":village_no", slot_town_lord, ":troop_no"),
					(store_faction_of_party, ":village_faction", ":village_no"),
					(try_begin),
						(neq, ":village_faction", ":faction_no"),
						(party_set_slot, ":village_no", slot_town_lord, stl_unassigned),
					(try_end),
				(try_end),
				
				#Free prisoners
				(try_begin),
					(troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
					(gt, ":leaded_party", 0),
					(party_set_faction, ":leaded_party", ":faction_no"),
					(party_get_num_prisoner_stacks, ":num_stacks", ":leaded_party"),
					(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
						(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":leaded_party", ":troop_iterator"),
						(store_troop_faction, ":cur_faction", ":cur_troop_id"),
						(troop_is_hero, ":cur_troop_id"),
						(eq, ":cur_faction", ":faction_no"),
						(call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
						(party_remove_prisoners, ":leaded_party", ":cur_troop_id", 1),
					(try_end),
				(try_end),
				
				#Annull all quests of which the lord is giver
				(try_for_range, ":quest", all_quests_begin, all_quests_end),
					(check_quest_active, ":quest"),
					(quest_slot_eq, ":quest", slot_quest_giver_troop, ":troop_no"),
					
					(str_store_troop_name, s4, ":troop_no"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(display_message, "str_s4_changing_sides_aborts_quest"),
					(try_end),
					(call_script, "script_abort_quest", ":quest", 0),
				(try_end),
				
				#Boot all lords out of centers whose faction has changed
				(try_for_range, ":lord_to_move", active_npcs_begin, active_npcs_end),
					(troop_get_slot, ":lord_led_party", ":lord_to_move", slot_troop_leaded_party),
					(party_is_active, ":lord_led_party"),
					(party_get_attached_to, ":led_party_attached", ":lord_led_party"),
					(is_between, ":led_party_attached", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":led_party_faction", ":lord_led_party"),
					(store_faction_of_party, ":attached_party_faction", ":led_party_attached"),
					(neq, ":led_party_faction", ":attached_party_faction"),
					
					(party_detach, ":lord_led_party"),
				(try_end),
				
				#Increase relation with lord in new faction by 5
				#Or, if player kingdom, make inactive pending confirmation
				(faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
				(try_begin),
					(eq, ":faction_liege", "trp_player"),
					(neq, ":troop_no", "$g_talk_troop"),
					(troop_set_slot, ":troop_no", slot_troop_occupation, slto_inactive), #POSSIBLE REASON 1
				(else_try),
					(is_between, ":faction_liege", active_npcs_begin, active_npcs_end),
					(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
					(call_script, "script_troop_change_relation_with_troop", ":faction_liege", ":troop_no", 5),
					(val_add, "$total_indictment_changes", 5),
				(try_end),
				
				#Break courtship relations
				(try_begin),
					(troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
					#Already married, do nothing
				(else_try),
					(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
					(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
						(troop_get_slot, ":courted_lady", ":troop_no", ":love_interest_slot"),
						(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":courted_lady", ":troop_no"),
					(try_end),
					(call_script, "script_assign_troop_love_interests", ":troop_no"),
				(else_try),
					(is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
					(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
						(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
							(troop_slot_eq, ":active_npc", ":love_interest_slot", ":troop_no"),
							(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":troop_no", ":active_npc"),
						(try_end),
					(try_end),
				(try_end),
				
				#Stop raidings/sieges of new faction's fief if there is any
				(troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":raided_by", ":center_no", slot_village_raided_by),
					(eq, ":raided_by", ":troop_party"),
					(party_set_slot, ":center_no", slot_village_raided_by, -1),
					(try_begin),
						(party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
						(party_set_slot, ":center_no", slot_village_state, svs_normal),
						(party_set_extra_text, ":center_no", "str_empty_string"),
					(try_end),
				(else_try),
					(party_get_slot, ":besieged_by", ":center_no", slot_center_is_besieged_by),
					(eq, ":besieged_by", ":troop_party"),
					(party_set_slot, ":center_no", slot_center_is_besieged_by, -1),
					(try_begin),
						(party_slot_eq, ":center_no", slot_village_state, svs_under_siege),
						(party_set_slot, ":center_no", slot_village_state, svs_normal),
						(party_set_extra_text, ":center_no", "str_empty_string"),
					(try_end),
				(try_end),
				
				(call_script, "script_update_all_notes"),
				
				(call_script, "script_update_village_market_towns"),
				
				# (call_script, "script_raf_set_ai_recalculation_flags", ":orig_faction"),
				# (call_script, "script_raf_set_ai_recalculation_flags", ":faction_no"),
				(assign, "$g_recalculate_ais", 1),
		])
		
		# script_troop_set_title_according_to_faction
		# Input: arg1 = troop_no, arg2 = faction_no
troop_set_title_according_to_faction = (
	"troop_set_title_according_to_faction",
			[
				(store_script_param, ":troop_no", 1),
				(store_script_param, ":faction_no", 2),
				(try_begin),
					(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
					(str_store_troop_name_plural, s0, ":troop_no"),
					(troop_get_type, ":gender", ":troop_no"),
					(store_sub, ":title_index", ":faction_no", kingdoms_begin),
					(try_begin),
						(eq, ":gender", 0), #male
						(val_add, ":title_index", kingdom_titles_male_begin),
					(else_try),
						(val_add, ":title_index", kingdom_titles_female_begin),
					(try_end),
					(str_store_string, s1, ":title_index"),
					(troop_set_name, ":troop_no", s1),
					(troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
					(gt, ":troop_party", 0),
					(str_store_troop_name, s5, ":troop_no"),
					(party_set_name, ":troop_party", "str_s5_s_party"),
				(try_end),
		])
		
		
# script_create_kingdom_hero_party
		# creates player kingdom!
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = troop_no, arg2 = center_no
		# Output: $pout_party = party_no
		("create_kingdom_hero_party",
			[
				(store_script_param, ":troop_no", 1),
				(store_script_param, ":center_no", 2),
				
				(store_troop_faction, ":troop_faction_no", ":troop_no"),
				
				(assign, "$pout_party", -1),
				(set_spawn_radius, 0),
				(spawn_around_party, ":center_no", "pt_kingdom_hero_party"),
				
				(assign, "$pout_party", reg0),
				
				(party_set_faction, "$pout_party", ":troop_faction_no"),
				(party_set_slot, "$pout_party", slot_party_type, spt_kingdom_hero_party),
				(call_script, "script_party_set_ai_state", "$pout_party", spai_undefined, -1),
				(troop_set_slot, ":troop_no", slot_troop_leaded_party, "$pout_party"),
				(party_add_leader, "$pout_party", ":troop_no"),
				(str_store_troop_name, s5, ":troop_no"),
				(party_set_name, "$pout_party", "str_s5_s_party"),
				
				(party_set_slot, "$pout_party", slot_party_commander_party, -1), #we need this because 0 is player's party!
				
				#Setting the flag icon
				#normal_banner_begin
				(troop_get_slot, ":cur_banner", ":troop_no", slot_troop_banner_scene_prop),
				(try_begin),
					(gt, ":cur_banner", 0),
					(val_sub, ":cur_banner", banner_scene_props_begin),
					(val_add, ":cur_banner", banner_map_icons_begin),
					(party_set_banner_icon, "$pout_party", ":cur_banner"),
					#custom_banner_begin
					#(troop_get_slot, ":flag_icon", ":troop_no", slot_troop_custom_banner_map_flag_type),
					#(try_begin),
					#  (ge, ":flag_icon", 0),
					#  (val_add, ":flag_icon", custom_banner_map_icons_begin),
					#  (party_set_banner_icon, "$pout_party", ":flag_icon"),
				(try_end),
				
				(try_begin),
					#because of below two lines, lords can only hire more than one party_template(stack) at game start once a time during all game.
					(troop_slot_eq, ":troop_no", slot_troop_spawned_before, 0),
					(troop_set_slot, ":troop_no", slot_troop_spawned_before, 1),
					(assign, ":num_tries", 20),
					(try_begin),
						(store_troop_faction, ":troop_kingdom", ":troop_no"),
						(faction_slot_eq, ":troop_kingdom", slot_faction_leader, ":troop_no"),
						(assign, ":num_tries", 50),
					(try_end),
					
					#(str_store_troop_name, s0, ":troop_no"),
					#(display_message, "{!}str_debug__hiring_men_to_party_for_s0"),
					
					(try_for_range, ":unused", 0, ":num_tries"),
						(call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"),
					(try_end),
			
			#tom
			(try_begin), ##add a few noble pages to the mix as well
			(faction_get_slot, ":center_culture", ":troop_kingdom", slot_faction_culture),
			(faction_get_slot, ":castle", ":center_culture", slot_faction_tier_1_castle_troop),
			(store_random_in_range, ":catle_amount", 2, 7),
			(party_add_members, "$pout_party", ":castle", ":catle_amount"),
			(try_end),
					#tom
			
					# (assign, ":xp_rounds", 0),
					
					# (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
					# (try_begin),
						# (this_or_next|eq, ":troop_faction_no", "$players_kingdom"),
						# (eq, ":troop_faction_no", "fac_player_supporters_faction"),
						# (assign, ":xp_rounds", 0),
					# (else_try),
						# (eq, ":reduce_campaign_ai", 0), #hard
						# (assign, ":xp_rounds", 2),
					# (else_try),
						# (eq, ":reduce_campaign_ai", 1), #moderate
						# (assign, ":xp_rounds", 1),
					# (else_try),
						# (eq, ":reduce_campaign_ai", 2), #easy
						# (assign, ":xp_rounds", 0),
					# (try_end),
					
					# (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
					# (store_div, ":renown_xp_rounds", ":renown", 100),
					# (val_add, ":xp_rounds", ":renown_xp_rounds"),
					#(try_for_range, ":unused", 0, ":xp_rounds"),
						# no xp for joo
						#(call_script, "script_upgrade_hero_party", "$pout_party", 4000),
						#(call_script, "script_upgrade_hero_party", "$pout_party", 400),
					#(try_end),
				(try_end),
		]),
		
		# script_troop_does_business_in_center
		# Currently called from process_ai_state, could be called from elsewhere
		# It is used for lord to (1)Court ladies (2)Collect rents (3)Look for volunteers
		# WARNING: heavily modified by 1257AD devs
		# INPUT: arg1 = troop_no, arg2 = center_no
		# OUTPUT: none
		("troop_does_business_in_center",
			[
				(store_script_param, ":troop_no", 1),
				(store_script_param, ":center_no", 2),
				
				(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
				
				(store_current_hours, ":current_time"),
				(try_begin),
					#         (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"), #this was added to get lords in centers out and visiting their fiefs, but I've adjusted the decision checklist
					(is_between, ":center_no", walled_centers_begin, walled_centers_end),
					(party_set_slot, ":led_party", slot_party_last_in_any_center, ":current_time"),
					(try_begin),
						(call_script, "script_lord_get_home_center", ":troop_no"),
						(eq, ":center_no", reg0),
						(party_set_slot, ":led_party", slot_party_last_in_home_center, ":current_time"),
					(try_end),
				(try_end),
				
				#Collect the rents - tom, done diffrently
				(try_begin),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					
					(party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
					(party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
					(troop_get_slot, ":troop_wealth", ":troop_no", slot_troop_wealth),
					(val_add, ":troop_wealth", ":accumulated_rents"),
					(val_add, ":troop_wealth", ":accumulated_tariffs"),
					
					(troop_set_slot, ":troop_no", slot_troop_wealth, ":troop_wealth"),
					(party_set_slot, ":center_no", slot_center_accumulated_rents, 0),
					(party_set_slot, ":center_no", slot_center_accumulated_tariffs, 0),
					
					(try_begin),
						(this_or_next|eq, "$cheat_mode", 1),
						(eq, "$cheat_mode", 3),
						(assign, reg1, ":troop_wealth"),
						(str_store_party_name, s4, ":center_no"),
						(add_troop_note_from_sreg, ":troop_no", 1, "str_current_wealth_reg1_taxes_last_collected_from_s4", 0),
					(try_end),
				(try_end),
				
				#Recruit volunteers
				(try_begin),
					(is_between, ":center_no", villages_begin, villages_end),
					
					(party_get_slot, ":troop_type", ":center_no", slot_center_npc_volunteer_troop_type),
					(party_get_slot, ":troop_amount", ":center_no", slot_center_npc_volunteer_troop_amount),
					(party_set_slot, ":center_no", slot_center_npc_volunteer_troop_amount, -1),
					(party_add_members, ":led_party", ":troop_type", ":troop_amount"),
					
				(try_end),
				
				#Courtship
				(try_begin),
					(party_get_slot, ":time_of_last_courtship", ":led_party", slot_party_leader_last_courted),
					(store_sub, ":hours_since_last_courtship", ":current_time", ":time_of_last_courtship"),
					(gt, ":hours_since_last_courtship", 72),
					
					# rafi no courtship for TO
					(store_faction_of_troop, ":fac", ":troop_no"),
					
					(troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
					(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
						(neq, ":fac", "fac_kingdom_1"), # rafi
						(troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
						(gt, ":love_interest", 0),
						(troop_get_slot, ":love_interest_town", ":love_interest", slot_troop_cur_center),
						(eq, ":center_no", ":love_interest_town"),
						
						(call_script, "script_courtship_event_troop_court_lady", ":troop_no", ":love_interest"),
						(party_set_slot, ":led_party", slot_party_leader_last_courted, ":current_time"),
					(try_end),
				(try_end),
		]),
		