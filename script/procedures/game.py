from header import *
#script_game_enable_cheat_menu
# This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
# INPUT:
# none
# OUTPUT:
# none

game_enable_cheat_menu =	(
	"game_enable_cheat_menu",
		[
			(store_script_param, ":input", 1),
			(try_begin),
				(eq, ":input", 0),
				(assign, "$cheat_mode", 0),
			(else_try),
				(eq, ":input", 1),
				(assign, "$cheat_mode", 1),
			(try_end),
	])

#script_game_event_detect_party:
	# This script is called from the game engine when player party inspects another party.
	# INPUT:
	# param1: Party-id
game_event_detect_party =	(
		"game_event_detect_party",
		[
			(store_script_param_1, ":party_id"),
			(try_begin),
				(party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
				(party_stack_get_troop_id, ":leader", ":party_id", 0),
				(is_between, ":leader", active_npcs_begin, active_npcs_end),
				(call_script, "script_update_troop_location_notes", ":leader", 0),
			(else_try),
				(is_between, ":party_id", walled_centers_begin, walled_centers_end),
				(party_get_num_attached_parties, ":num_attached_parties",  ":party_id"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":party_id", ":attached_party_rank"),
					(party_stack_get_troop_id, ":leader", ":attached_party", 0),
					(is_between, ":leader", active_npcs_begin, active_npcs_end),
					(call_script, "script_update_troop_location_notes", ":leader", 0),
				(try_end),
			(try_end),
	])

	#script_game_event_undetect_party:
	# This script is called from the game engine when player party inspects another party.
	# INPUT:
	# param1: Party-id
game_event_undetect_party =	(
	"game_event_undetect_party",
		[
			(store_script_param_1, ":party_id"),
			(try_begin),
				(party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
				(party_stack_get_troop_id, ":leader", ":party_id", 0),
				(is_between, ":leader", active_npcs_begin, active_npcs_end),
				(call_script, "script_update_troop_location_notes", ":leader", 0),
			(try_end),
	])

#script_game_get_statistics_line:
	# This script is called from the game engine when statistics page is opened.
	# INPUT:
	# param1: line_no
game_get_statistics_line =	(
	"game_get_statistics_line",
		[
			(store_script_param_1, ":line_no"),
			(try_begin),
				(eq, ":line_no", 0),
				(get_player_agent_kill_count, reg1),
				(str_store_string, s1, "str_number_of_troops_killed_reg1"),
				(set_result_string, s1),
			(else_try),
				(eq, ":line_no", 1),
				(get_player_agent_kill_count, reg1, 1),
				(str_store_string, s1, "str_number_of_troops_wounded_reg1"),
				(set_result_string, s1),
			(else_try),
				(eq, ":line_no", 2),
				(get_player_agent_own_troop_kill_count, reg1),
				(str_store_string, s1, "str_number_of_own_troops_killed_reg1"),
				(set_result_string, s1),
			(else_try),
				(eq, ":line_no", 3),
				(get_player_agent_own_troop_kill_count, reg1, 1),
				(str_store_string, s1, "str_number_of_own_troops_wounded_reg1"),
				(set_result_string, s1),
			(try_end),
	])

#script_game_reset_player_party_name:
	# This script is called from the game engine when the player name is changed.
	# INPUT: none
	# OUTPUT: none
game_reset_player_party_name = 	(
		"game_reset_player_party_name",
		[(str_store_troop_name, s5, "trp_player"),
			(party_set_name, "p_main_party", s5),
	])

#script_initialize_scene_prop_slots
	# INPUT: arg1 = scene_prop_no
	# OUTPUT: none
initialize_scene_prop_slots =	(
	"initialize_scene_prop_slots",
		[
			(store_script_param, ":scene_prop_no", 1),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", ":scene_prop_no"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", ":scene_prop_no", ":cur_instance"),
				(try_for_range, ":cur_slot", 0, scene_prop_slots_end),
					(scene_prop_set_slot, ":cur_instance_id", ":cur_slot", 0),
				(try_end),
			(try_end),
	])

#script_game_get_cheat_mode
# WARNING: no documentation. perhaps it is used by the game engine
# INPUT: none
# OUTPUT: none
game_get_cheat_mode =	(
	"game_get_cheat_mode",
		[
			(assign, reg0, "$cheat_mode"),
	])

#script_game_on_disembark:
		# This script is called from the game engine when the player reaches the shore with a ship.
		# INPUT: pos0 = disembark position
		# OUTPUT: none
game_on_disembark =	(
	"game_on_disembark",
			[(jump_to_menu, "mnu_disembark"),
		])
		

	# script_custom_battle_end
	# Input: none
	# Output: none
custom_battle_end = (
	"custom_battle_end",
		[
		(assign, "$g_custom_battle_team1_death_count", 0),
		(assign, "$g_custom_battle_team2_death_count", 0),
		(get_player_agent_no, ":player_agent"),
		(agent_get_team, ":player_team", ":player_agent"),
		(try_for_agents, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(neg|agent_is_alive, ":cur_agent"),
			(agent_get_team, ":cur_team", ":cur_agent"),
			(try_begin),
			(eq, ":cur_team", ":player_team"),
			(val_add, "$g_custom_battle_team1_death_count", 1),
			(else_try),
			(val_add, "$g_custom_battle_team2_death_count", 1),
			(try_end),
		(try_end),
	])
	
	# script_debug_variables
	# Input: two variables which will be examined by coder, this script is only for debugging.
	# Output: none
debug_variables = (
	"debug_variables",
		[
		(store_script_param, ":unused", 1),
		(store_script_param, ":unused_2", 2),
	])


	# script_check_concilio_calradi_achievement
check_concilio_calradi_achievement = (
	"check_concilio_calradi_achievement",
		[
		(try_begin),
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(faction_get_slot, ":player_faction_king", "fac_player_supporters_faction", slot_faction_leader),
			(eq, ":player_faction_king", "trp_player"),
			(assign, ":number_of_vassals", 0),
			(try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":cur_faction", ":cur_troop"),
			(eq, ":cur_faction", "fac_player_supporters_faction"),
			(val_add, ":number_of_vassals", 1),
			(try_end),
			(ge, ":number_of_vassals", 3),
			(unlock_achievement, ACHIEVEMENT_CONCILIO_CALRADI),
		(try_end),
	])