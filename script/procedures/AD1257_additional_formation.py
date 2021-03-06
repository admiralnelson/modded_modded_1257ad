from header import *

		#script_first_formation_member_sound_horn
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#tom-script
		#input: team, group, formation_type
		#output: none
		#first formation member sounds the horn. Used mainly for player armies(ai use them diffrently)
first_formation_member_sound_horn = (
	"first_formation_member_sound_horn",
		[
			#(store_script_param, ":team", 1),
			#(store_script_param, ":group", 2),
			#(store_script_param, ":formation_type", 3),
			(get_player_agent_no,":player_agent"),
			(agent_get_team, ":team", ":player_agent"),
			(try_for_range, ":cur_group", 0, 9),
			#(try_begin),
			(class_is_listening_order, ":team", ":cur_group"),
			(assign, ":agent_to_play_sound", -1),
			(try_for_agents, ":agent"),
				(neq, ":agent", ":player_agent"),
				(agent_is_alive, ":agent"), 
				(agent_is_human, ":agent"),
				(agent_get_division, ":division", ":agent"),
				(eq, ":division", ":cur_group"),
				(agent_get_team, ":p_team", ":agent"),
				(eq, ":p_team", ":team"),
				(assign, ":agent_to_play_sound" ,":agent"),
			(try_end),
			
			#(call_script, "script_get_first_formation_member", ":team", ":cur_group", 0),
			(try_begin),
				(gt, ":agent_to_play_sound", -1),
				(agent_play_sound, ":agent_to_play_sound", "snd_horn"),
			(try_end),
			(try_end),
		])

		#script_set_flag_carriers
		#tom-script
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#input: nothing
		#output: nothing
set_flag_carriers = (
	"set_flag_carriers",
		[
			(try_for_range, ":team", 0, 4),
				(team_get_slot, ":team_size", ":team", slot_team_size),
			#(try_begin),
			(gt, ":team_size", 0),
			(neq, "$fplayer_team_no", 0),
			(store_div, ":flags", ":team_size", 35),
			(gt, ":flags", 0),
			(assign, ":flags", 1),
			(try_for_agents, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_is_non_player, ":cur_agent"),
				(agent_get_troop_id, ":cur_troop", ":cur_agent"),
				(neg|troop_is_guarantee_ranged, ":cur_troop"),
				(neg|troop_is_guarantee_horse, ":cur_troop"),
				(neg|troop_is_hero,":cur_troop"),
				(agent_get_team, ":cur_team", ":cur_agent"),
				(eq, ":cur_team", 0),
				(gt, ":flags", 0),
				(try_begin),
					(agent_get_party_id, ":party", ":cur_agent"),
				(gt, ":party", 0),
				(store_faction_of_party, ":faction", ":party"),
				(eq, ":faction", "fac_kingdom_23"),
				(party_stack_get_troop_id, ":party_leader", ":party", 0),
				(eq, ":party_leader", "trp_kingdom_23_lord"),
				(assign, ":item", "itm_cross"),
				(else_try),
					(store_random_in_range, ":item", "itm_flag_pole_1", "itm_cross"),
				(try_end),	
				(agent_equip_item, ":cur_agent", ":item"),
				(agent_set_wielded_item, ":cur_agent", ":item"),
				(agent_set_slot, ":cur_agent",slot_agent_banner, 1),
				(val_sub, ":flags", 1),
			(try_end),
			(try_end),
			
			#player team - flag carriers
			(assign, ":group0", 0),
			(assign, ":group1", 0),
			(assign, ":group2", 0),
			(assign, ":group3", 0),
			(assign, ":group4", 0),
			(assign, ":group5", 0),
			(assign, ":group6", 0),
			(assign, ":group7", 0),
			(assign, ":group8", 0),
			#count the amount of agents
			(try_for_agents, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_is_non_player, ":cur_agent"),
			(agent_get_team, ":cur_team", ":cur_agent"),
			(eq, ":cur_team", "$fplayer_team_no"),
			(agent_get_division, ":cur_group", ":cur_agent"),
			(try_begin),
				(eq, ":cur_group", 0),
				(val_add, ":group0", 1),
			(else_try),
				(eq, ":cur_group", 1),
				(val_add, ":group1", 1),
			(else_try),
				(eq, ":cur_group", 2),
				(val_add, ":group2", 1),
			(else_try),
				(eq, ":cur_group", 3),
				(val_add, ":group3", 1),
			(else_try),
				(eq, ":cur_group", 4),
				(val_add, ":group4", 1),
			(else_try),
				(eq, ":cur_group", 5),
				(val_add, ":group5", 1),
			(else_try),
				(eq, ":cur_group", 6),
				(val_add, ":group6", 1),
			(else_try),
				(eq, ":cur_group", 7),
				(val_add, ":group7", 1),
			(else_try),
				(eq, ":cur_group", 8),
				(val_add, ":group8", 1),
			(try_end),
			(try_end),
			
			(try_for_range, reg1, 0, 9),
			(assign, ":head_count", 0),
			(assign, ":group", reg1),
			(try_begin),
				(eq, reg1, 0),
				(val_add, ":head_count", ":group0"),
			(else_try),
				(eq, reg1, 1),
				(val_add, ":head_count", ":group1"),
			(else_try),
				(eq, reg1, 2),
				(val_add, ":head_count", ":group2"),
			(else_try),
				(eq, reg1, 3),
				(val_add, ":head_count", ":group3"),
			(else_try),
				(eq, reg1, 4),
				(val_add, ":head_count", ":group4"),
			(else_try),
				(eq, reg1, 5),
				(val_add, ":head_count", ":group5"),
			(else_try),
				(eq, reg1, 6),
				(val_add, ":head_count", ":group6"),
			(else_try),
				(eq, reg1, 7),
				(val_add, ":head_count", ":group7"),
			(else_try),
				(eq, reg1, 8),
				(val_add, ":head_count", ":group8"),
			(try_end),
			(store_div, ":flags", ":head_count", 20),
			(gt, ":flags", 0),
			(assign, ":flags", 1),
			(try_for_agents, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_is_non_player, ":cur_agent"),
				(agent_get_troop_id, ":cur_troop", ":cur_agent"),
				(neg|is_between, ":cur_troop", active_npcs_begin, active_npcs_end), #not a lord or a companion
				(neg|troop_is_guarantee_ranged, ":cur_troop"),
				(neg|troop_is_guarantee_horse, ":cur_troop"),
				(neg|troop_is_hero,":cur_troop"),
				(agent_get_team, ":cur_team", ":cur_agent"),
				(eq, ":cur_team", "$fplayer_team_no"),
				(agent_get_division, ":cur_group", ":cur_agent"),
				(eq, ":cur_group", ":group"),
				(gt, ":flags", 0),
				# (init_position, pos8),
				(agent_get_position, pos8, ":cur_agent"),
				(set_spawn_position, pos8),
				#(spawn_agent, ":cur_troop"),
				#(display_message, "@spawning"),
				#(assign, ":agent", reg0),
				(assign, ":agent", ":cur_agent"),
				(agent_set_team, ":agent", ":cur_team"),
				#(agent_set_division, ":agent", ":cur_group"),
				(store_random_in_range, ":item", "itm_flag_pole_1", "itm_cross"),
				(agent_equip_item, ":agent", ":item"),
				(agent_equip_item, ":agent", ":item"),
				(agent_equip_item, ":agent", ":item"),
				(agent_set_wielded_item, ":agent", ":item"),
				(agent_set_slot, ":agent",slot_agent_banner, 1),
				(val_sub, ":flags", 1),
			(try_end),
			(try_end),
		])