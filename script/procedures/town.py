from header import *


		# script_get_heroes_attached_to_center_aux
		# For internal use only
get_heroes_attached_to_center_aux	= (
	"get_heroes_attached_to_center_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_get_num_companion_stacks, ":num_stacks",":center_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
					(call_script, "script_get_heroes_attached_to_center_aux", ":attached_party", ":party_no_to_collect_heroes"),
				(try_end),
		])

		# script_get_heroes_attached_to_center
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
get_heroes_attached_to_center	= (
	"get_heroes_attached_to_center",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_clear, ":party_no_to_collect_heroes"),
				(call_script, "script_get_heroes_attached_to_center_aux", ":center_no", ":party_no_to_collect_heroes"),
				
				#rebellion changes begin -Arma
				(try_for_range, ":pretender", pretenders_begin, pretenders_end),
					(neq, ":pretender", "$supported_pretender"),
					(troop_slot_eq, ":pretender", slot_troop_cur_center, ":center_no"),
					(party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
				(try_end),
				
				#     (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
				#        (faction_slot_eq, ":rebel_faction", slot_faction_state, sfs_inactive_rebellion),
				#        (faction_slot_eq, ":rebel_faction", slot_faction_inactive_leader_location, ":center_no"),
				#        (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
				#        (party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
				#     (try_end),
				#rebellion changes end
				
				
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner_aux
		# For internal use only
get_heroes_attached_to_center_as_prisoner_aux	= (
	"get_heroes_attached_to_center_as_prisoner_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_get_num_prisoner_stacks, ":num_stacks",":center_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
					(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":attached_party", ":party_no_to_collect_heroes"),
				(try_end),
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
get_heroes_attached_to_center_as_prisoner	= (
	"get_heroes_attached_to_center_as_prisoner",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_clear, ":party_no_to_collect_heroes"),
				(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":center_no", ":party_no_to_collect_heroes"),
		])
		
		# script_give_center_to_faction
		# added dimplomacy
		# WARNING: modified by 1257dev
		# Input: arg1 = center_no, arg2 = faction
give_center_to_faction	= (
	"give_center_to_faction",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":faction_no"),
				
				##diplomacy begin
				(party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
				(try_begin),
					(party_slot_eq, ":center_no", slot_village_infested_by_bandits, "trp_peasant_woman"),
					(party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
				(try_end),
				(try_begin),
					(eq, "$g_constable_training_center", ":center_no"),
					(assign, "$g_constable_training_center", -1),
				(try_end),
				##diplomacy end
				(try_begin),
					(eq, ":faction_no", "fac_player_supporters_faction"),
					(faction_get_slot, ":player_faction_king", "fac_player_supporters_faction", slot_faction_leader),
					(eq, ":player_faction_king", "trp_player"),
					
					(try_begin),
						(is_between, ":center_no", walled_centers_begin, walled_centers_end),
						(assign, ":number_of_walled_centers_players_kingdom_has", 1),
					(else_try),
						(assign, ":number_of_walled_centers_players_kingdom_has", 0),
					(try_end),
					
					(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
						(store_faction_of_party, ":owner_faction_no", ":walled_center"),
						(eq, ":owner_faction_no", "fac_player_supporters_faction"),
						(val_add, ":number_of_walled_centers_players_kingdom_has", 1),
					(try_end),
					
					(ge, ":number_of_walled_centers_players_kingdom_has", 10),
					(unlock_achievement, ACHIEVEMENT_VICTUM_SEQUENS),
				(try_end),
				
				(try_begin),
					(check_quest_active, "qst_join_siege_with_army"),
					(quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, ":center_no"),
					(call_script, "script_abort_quest", "qst_join_siege_with_army", 0),
					#Reactivating follow army quest
					(faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
					(str_store_troop_name_link, s9, ":faction_marshall"),
					(setup_quest_text, "qst_follow_army"),
					(str_store_string, s2, "@{s9} wants you to resume following his army until further notice."),
					(call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
					(assign, "$g_player_follow_army_warnings", 0),
				(try_end),
				
				#(store_faction_of_party, ":old_faction", ":center_no"),
				(call_script, "script_give_center_to_faction_aux", ":center_no", ":faction_no"),
				(call_script, "script_update_village_market_towns"),
				
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(call_script, "script_faction_recalculate_strength", ":cur_faction"),
				(try_end),
				(assign, "$g_recalculate_ais", 1),
				#(call_script, "script_raf_set_ai_recalculation_flags", ":faction_no"),
				
				(try_begin),
					(eq, ":faction_no", "fac_player_supporters_faction"),
					(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
					(call_script, "script_activate_player_faction", "trp_player"),
				(try_end),
				
				#(call_script, "script_activate_deactivate_player_faction", ":old_faction"),
				#(try_begin),
				#(eq, ":faction_no", "fac_player_supporters_faction"),
				#(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				#(call_script, "script_give_center_to_lord", ":center_no", "trp_player", 0),
				
				#check with Armagan -- what is this here for?
				#(try_for_range, ":cur_village", villages_begin, villages_end),
				#(store_faction_of_party, ":cur_village_faction", ":cur_village"),
				#(eq, ":cur_village_faction", "fac_player_supporters_faction"),
				#(neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
				#(call_script, "script_give_center_to_lord", ":cur_village", "trp_player", 0),
				#(try_end),
				#(try_end),
		])
		
		# script_give_center_to_faction_aux
		# Input: arg1 = center_no, arg2 = faction
give_center_to_faction_aux	= (
	"give_center_to_faction_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":faction_no"),
				
				#(try_begin), #tom
				#(neq, ":center_no", -1), #tom extra check
				
				(store_faction_of_party, ":old_faction", ":center_no"),
				(party_set_faction, ":center_no", ":faction_no"),
				
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
					(gt, ":farmer_party", 0),
					(party_is_active, ":farmer_party"),
					(party_set_faction, ":farmer_party", ":faction_no"),
				(try_end),
				
				(try_begin),
					#This bit of seemingly redundant code (the neq condition) is designed to prevent a bug that occurs when a player first conquers a center -- apparently this script is called again AFTER it is handed to a lord
					#Without this line, then the player's dialog selection does not have any affect, because town_lord is set again to stl_unassigned after the player makes his or her choice
					(neq, ":faction_no", ":old_faction"),
					
					(party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
					(party_get_slot, ":old_town_lord", ":center_no", slot_town_lord),
					(party_set_slot, ":center_no", slot_town_lord, stl_unassigned),
					(party_set_banner_icon, ":center_no", 0),#Removing banner
					(call_script, "script_update_faction_notes", ":old_faction"),
				(try_end),
				
				(call_script, "script_update_faction_notes", ":faction_no"),
				(call_script, "script_update_center_notes", ":center_no"),
				
				(try_begin),
					(ge, ":old_town_lord", 0),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(call_script, "script_update_troop_notes", ":old_town_lord"),
				(try_end),
				
				(try_for_range, ":other_center", centers_begin, centers_end),
					(party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
					(call_script, "script_give_center_to_faction_aux", ":other_center", ":faction_no"),
				(try_end),
				# (else_try), #tom
				# (assign, reg0, ":faction_no"),
				# (display_message, "@{reg0} bugova"),
				# (try_end), #tom
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner_aux
		# For internal use only
get_heroes_attached_to_center_as_prisoner_aux	= (
	"get_heroes_attached_to_center_as_prisoner_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_get_num_prisoner_stacks, ":num_stacks",":center_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
					(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":attached_party", ":party_no_to_collect_heroes"),
				(try_end),
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
get_heroes_attached_to_center_as_prisoner	= (
	"get_heroes_attached_to_center_as_prisoner",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_clear, ":party_no_to_collect_heroes"),
				(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":center_no", ":party_no_to_collect_heroes"),
		])


		# script_give_center_to_faction_aux
		# WARNING modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = faction
give_center_to_faction_aux	= (
	"give_center_to_faction_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":faction_no"),
				
				#(try_begin), #tom
				#(neq, ":center_no", -1), #tom extra check
				
				(store_faction_of_party, ":old_faction", ":center_no"),
				(party_set_faction, ":center_no", ":faction_no"),
				
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
					(gt, ":farmer_party", 0),
					(party_is_active, ":farmer_party"),
					(party_set_faction, ":farmer_party", ":faction_no"),
				(try_end),
				
				(try_begin),
					#This bit of seemingly redundant code (the neq condition) is designed to prevent a bug that occurs when a player first conquers a center -- apparently this script is called again AFTER it is handed to a lord
					#Without this line, then the player's dialog selection does not have any affect, because town_lord is set again to stl_unassigned after the player makes his or her choice
					(neq, ":faction_no", ":old_faction"),
					
					(party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
					(party_get_slot, ":old_town_lord", ":center_no", slot_town_lord),
					(party_set_slot, ":center_no", slot_town_lord, stl_unassigned),
					(party_set_banner_icon, ":center_no", 0),#Removing banner
					(call_script, "script_update_faction_notes", ":old_faction"),
				(try_end),
				
				(call_script, "script_update_faction_notes", ":faction_no"),
				(call_script, "script_update_center_notes", ":center_no"),
				
				(try_begin),
					(ge, ":old_town_lord", 0),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(call_script, "script_update_troop_notes", ":old_town_lord"),
				(try_end),
				
				(try_for_range, ":other_center", centers_begin, centers_end),
					(party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
					(call_script, "script_give_center_to_faction_aux", ":other_center", ":faction_no"),
				(try_end),
				# (else_try), #tom
				# (assign, reg0, ":faction_no"),
				# (display_message, "@{reg0} bugova"),
				# (try_end), #tom
		])