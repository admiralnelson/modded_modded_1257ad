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


		# script_give_center_to_lord
		# Input: arg1 = center_no, arg2 = lord_troop, arg3 = add_garrison_to_center
		("give_center_to_lord",
			[
				(store_script_param, ":center_no", 1),
				(store_script_param, ":lord_troop_id", 2), #-1 only in the case of a player deferring ownership of a center
				(store_script_param, ":add_garrison", 3),
				##diplomacy begin
				(party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
				(try_begin),
					(party_slot_eq, ":center_no", slot_village_infested_by_bandits, "trp_peasant_woman"),
					(party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
				(try_end),
				##diplomacy end
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(ge, ":lord_troop_id", 0),
					(str_store_party_name, s4, ":center_no"),
					(str_store_troop_name, s5, ":lord_troop_id"),
					(display_message, "@{!}DEBUG -- {s4} awarded to {s5}"),
				(try_end),
				
				(try_begin),
					(eq, ":lord_troop_id", "trp_player"),
					(unlock_achievement, ACHIEVEMENT_ROYALITY_PAYMENT),
					
					(assign, ":number_of_fiefs_player_have", 1),
					(try_for_range, ":cur_center", centers_begin, centers_end),
						(neq, ":cur_center", ":center_no"),
						(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
						(val_add, ":number_of_fiefs_player_have", 1),
					(try_end),
					
					(ge, ":number_of_fiefs_player_have", 5),
					(unlock_achievement, ACHIEVEMENT_MEDIEVAL_EMLAK),
				(try_end),
				
				(party_get_slot, ":old_lord_troop_id", ":center_no", slot_town_lord),
				
				(try_begin), #This script is ONLY called with lord_troop_id = -1 when it is the player faction
					(eq, ":lord_troop_id", -1),
					(assign, ":lord_troop_faction", "fac_player_supporters_faction"),
					(party_set_banner_icon, ":center_no", 0),#Removing banner
					
				(else_try),
					(eq, ":lord_troop_id", "trp_player"),
					(assign, ":lord_troop_faction", "$players_kingdom"), #was changed on Apr 27 from fac_plyr_sup_fac
					
				(else_try),
					(store_troop_faction, ":lord_troop_faction", ":lord_troop_id"),
				(try_end),
				(faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
				
				(try_begin),
					(eq, ":faction_leader", ":old_lord_troop_id"),
					(call_script, "script_add_log_entry", logent_liege_grants_fief_to_vassal, ":faction_leader", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
					(troop_set_slot, ":lord_troop_id", slot_troop_promised_fief, 0),
				(try_end),
				
				(try_begin),
					(eq, ":lord_troop_id", -1), #Lord troop ID -1 is only used when a player is deferring assignment of a fief
					(party_set_faction, ":center_no", "$players_kingdom"),
				(else_try),
					(eq, ":lord_troop_id", "trp_player"),
					(gt, "$players_kingdom", 0),
					(party_set_faction, ":center_no", "$players_kingdom"),
				(else_try),
					(eq, ":lord_troop_id", "trp_player"),
					(neg|is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
					(party_set_faction, ":center_no", "fac_player_supporters_faction"),
				(else_try),
					(party_set_faction, ":center_no", ":lord_troop_faction"),
				(try_end),
				(party_set_slot, ":center_no", slot_town_lord, ":lord_troop_id"),
				
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":farmer_party_no", ":center_no", slot_village_farmer_party),
					(gt, ":farmer_party_no", 0),
					(party_is_active, ":farmer_party_no"),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(party_set_faction, ":farmer_party_no", ":center_faction"),
				(try_end),
				
				(try_begin),
					(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(gt, ":lord_troop_id", -1),
					
					#normal_banner_begin
					(troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
					(gt, ":cur_banner", 0),
					(val_sub, ":cur_banner", banner_scene_props_begin),
					(val_add, ":cur_banner", banner_map_icons_begin),
					(party_set_banner_icon, ":center_no", ":cur_banner"),
					# custom_banner_begin
					#        (troop_get_slot, ":flag_icon", ":lord_troop_id", slot_troop_custom_banner_map_flag_type),
					#        (ge, ":flag_icon", 0),
					#        (val_add, ":flag_icon", custom_banner_map_icons_begin),
					#        (party_set_banner_icon, ":center_no", ":flag_icon"),
				(try_end),
				
				#    (try_begin),
				#		(eq, 1, 0),
				#       (eq, ":lord_troop_id", "trp_player"),
				#       (neq, ":old_lord_troop_id", "trp_player"),
				#       (party_get_slot, ":center_relation", ":center_no", slot_center_player_relation),
				#       (is_between, ":center_relation", -4, 5),
				#       (call_script, "script_change_player_relation_with_center", ":center_no", 5),
				#       (gt, ":old_lord_troop_id", 0),
				#       (call_script, "script_change_player_relation_with_troop", ":old_lord_troop_id", -25),
				#   (try_end),
				(try_begin),
					(gt, ":lord_troop_id", -1),
					(call_script, "script_update_troop_notes", ":lord_troop_id"),
				(try_end),
				
				(call_script, "script_update_center_notes", ":center_no"),
				
				(try_begin),
					(gt, ":lord_troop_faction", 0),
					(call_script, "script_update_faction_notes", ":lord_troop_faction"),
				(try_end),
				
				(try_begin),
					(ge, ":old_lord_troop_id", 0),
					(call_script, "script_update_troop_notes", ":old_lord_troop_id"),
					(store_troop_faction, ":old_lord_troop_faction", ":old_lord_troop_id"),
					(call_script, "script_update_faction_notes", ":old_lord_troop_faction"),
				(try_end),
				
				(try_begin),
					(eq, ":add_garrison", 1),
					(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(assign, ":garrison_strength", 3),
					(try_begin),
						(party_slot_eq, ":center_no", slot_party_type, spt_town),
						(assign, ":garrison_strength", 9),
					(try_end),
					(try_for_range, ":unused", 0, ":garrison_strength"),
						(call_script, "script_cf_reinforce_party", ":center_no"),
					(try_end),
					## ADD some XP initially
					(try_for_range, ":unused", 0, 7),
						(store_mul, ":xp_range_min", 150, ":garrison_strength"),
						(store_mul, ":xp_range_max", 200, ":garrison_strength"),
						
						(store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
						(party_upgrade_with_xp, ":center_no", ":xp", 0),
					(try_end),
				(try_end),
				
				(faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
				(store_current_hours, ":hours"),
				
				#the next block handles gratitude, objections and jealousies
				(try_begin),
					(gt, ":hours", 0),
					(gt, ":lord_troop_id", 0),
					
					(call_script, "script_troop_change_relation_with_troop", ":lord_troop_id", ":faction_leader", 10),
					(val_add, "$total_promotion_changes", 10),
					
					#smaller factions are more dramatically influenced by internal jealousies
					#Disabled as of NOV 2010
					#		(try_begin),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 4),
					#			(assign, ":faction_size_multiplier", 6),
					#		(else_try),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 8),
					#			(assign, ":faction_size_multiplier", 5),
					#		(else_try),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 16),
					#			(assign, ":faction_size_multiplier", 4),
					#		(else_try),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 32),
					#			(assign, ":faction_size_multiplier", 3),
					#		(else_try),
					#			(assign, ":faction_size_multiplier", 2),
					#		(try_end),
					
					#factional politics -- each lord in the faction adjusts his relation according to the relation with the lord receiving the faction
					(try_for_range, ":other_lord", active_npcs_begin, active_npcs_end),
						(troop_slot_eq, ":other_lord", slot_troop_occupation, slto_kingdom_hero),
						(neq, ":other_lord", ":lord_troop_id"),
						
						(store_troop_faction, ":other_troop_faction", ":other_lord"),
						(eq, ":lord_troop_faction", ":other_troop_faction"),
						
						(neq, ":other_lord", ":faction_leader"),
						
						(call_script, "script_troop_get_relation_with_troop", ":other_lord", ":lord_troop_id"),
						(assign, ":relation_with_troop", reg0),
						#relation reduction = relation/10 minus 2. So,0 = -2, 8 = -1, 16+ = no change or bonus, 24+ gain one point
						(store_div, ":relation_with_liege_change", ":relation_with_troop", 8), #changed from 16
						(val_sub, ":relation_with_liege_change", 2),
						
						(val_clamp, ":relation_with_liege_change", -5, 3),
						
						(try_begin),
							#upstanding and goodnatured lords will not lose relation unless they actively dislike the other lord
							(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_upstanding),
							(troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_goodnatured),
							(ge, ":relation_with_troop", 0),
							(val_max, ":relation_with_liege_change", 0),
						(else_try),
							#penalty is increased for lords who have the more unpleasant reputation types
							(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_selfrighteous),
							(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_debauched),
							(troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_quarrelsome),
							(lt, ":relation_with_liege_change", 0),
							(val_mul, ":relation_with_liege_change", 3),
							(val_div, ":relation_with_liege_change", 2),
						(try_end),
						
						
						(neq, ":relation_with_liege_change", 0),
						#removed Nov 2010
						#		  	(val_mul, ":relation_reduction", ":faction_size_multiplier"),
						#		  	(val_div, ":relation_reduction", 2),
						#removed Nov 2010
						
						(try_begin),
							(troop_slot_eq, ":other_lord", slot_troop_stance_on_faction_issue, ":lord_troop_id"),
							(val_add, ":relation_with_liege_change", 1),
							(val_max, ":relation_with_liege_change", 1),
						(try_end),
						
						(call_script, "script_troop_change_relation_with_troop", ":other_lord", ":faction_leader", ":relation_with_liege_change"),
						(val_add, "$total_promotion_changes", ":relation_with_liege_change"),
						
						(try_begin),
							(this_or_next|le, ":relation_with_liege_change", -4), #Nov 2010 - changed from -8
							(this_or_next|troop_slot_eq, ":other_lord", slot_troop_promised_fief, 1), #1 is any fief
							(troop_slot_eq, ":other_lord", slot_troop_promised_fief, ":center_no"),
							(call_script, "script_add_log_entry", logent_troop_feels_cheated_by_troop_over_land, ":other_lord", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
						(try_end),
						
					(try_end),
				(try_end),
				
				#Villages from another faction will also be transferred along with a fortress
				(try_begin),
					(is_between, ":center_no", walled_centers_begin, walled_centers_end),
					(try_for_range, ":cur_village", villages_begin, villages_end),
						(party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),
						(store_faction_of_party, ":cur_village_faction", ":cur_village"),
						(neq, ":cur_village_faction", ":lord_troop_faction"),
						
						(call_script, "script_give_center_to_lord", ":cur_village", ":lord_troop_id", 0),
					(try_end),
				(try_end),
		]),


		# script_refresh_village_merchant_inventory
		# Input: arg1 = village_no
		# Output: none
	("refresh_village_merchant_inventory",
		[
			(store_script_param_1, ":village_no"),
			(party_get_slot, ":merchant_troop", ":village_no", slot_town_elder),
			(reset_item_probabilities,0),

		(assign, ":total_probability", 0),
			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
		
			(call_script, "script_center_get_production", ":village_no", ":cur_goods"),
		(assign, ":cur_probability", reg0),

		(val_max, ":cur_probability", 5),
				
		(val_add, ":total_probability", ":cur_probability"),
			(try_end),
		
		(try_begin),
		(party_get_slot, ":prosperity", ":village_no", slot_town_prosperity),
		(val_div, ":prosperity", 15), #up to 6
		(store_add, ":number_of_items_in_village", ":prosperity", 1),
		(try_end),

			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
			(call_script, "script_center_get_production", ":village_no", ":cur_goods"),
		(assign, ":cur_probability", reg0),

		(val_max, ":cur_probability", 5),

				(val_mul, ":cur_probability", ":number_of_items_in_village"),
		(val_mul, ":cur_probability", 100),
		(val_div, ":cur_probability", ":total_probability"),

				(set_item_probability_in_merchandise, ":cur_goods", ":cur_probability"),
			(try_end),

			(troop_clear_inventory, ":merchant_troop"),
			(troop_add_merchandise, ":merchant_troop", itp_type_goods, ":number_of_items_in_village"),
			(troop_ensure_inventory_space, ":merchant_troop", 80),

			#Adding 1 prosperity to the village while reducing each 3000 gold from the elder
			(store_troop_gold, ":gold",":merchant_troop"),
			(try_begin),
				(gt, ":gold", 3500),
				(store_div, ":prosperity_added", ":gold", 3000),
				(store_mul, ":gold_removed", ":prosperity_added", 3000),
				(troop_remove_gold, ":merchant_troop", ":gold_removed"),
				(call_script, "script_change_center_prosperity", ":village_no", ":prosperity_added"),
			(try_end),
	]),
		

		# script_refresh_village_defenders
		# Input: arg1 = village_no
		# Output: none
		("refresh_village_defenders",
			[
				(store_script_param_1, ":village_no"),
				
				(assign, ":ideal_size", 50),
				(try_begin),
					(party_get_num_companions, ":party_size", ":village_no"),
					(lt, ":party_size", ":ideal_size"),
					(party_add_template, ":village_no", "pt_village_defenders"),
				(try_end),
		]),

# script_lift_siege
		# Input: arg1 = center_no, arg2 = display_message
		# Output: none
		#called from triggers
		("lift_siege",
			[
				(store_script_param, ":center_no", 1),
				(store_script_param, ":display_message", 2),
				(party_set_slot, ":center_no", slot_center_is_besieged_by, -1), #clear siege
				(call_script, "script_village_set_state",  ":center_no", 0), #clear siege flag
				(try_begin),
					(eq, ":center_no", "$g_player_besiege_town"),
					(assign, "$g_siege_method", 0), #remove siege progress
				(try_end),
				(try_begin),
					(eq, ":display_message", 1),
					(str_store_party_name_link, s3, ":center_no"),
					(display_message, "@{s3} is no longer under siege."),
				(try_end),
		]),