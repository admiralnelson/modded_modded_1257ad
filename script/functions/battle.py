from header import *


		# script_calculate_battle_advantage
		# Output: reg0 = battle advantage
calculate_battle_advantage = (
	"calculate_battle_advantage",
			[
				(call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
				(assign, ":friend_count", reg(0)),
				
				(party_get_skill_level, ":player_party_tactics",  "p_main_party", skl_tactics),
				(party_get_skill_level, ":ally_party_tactics",  "p_collective_friends", skl_tactics),
				(val_max, ":player_party_tactics", ":ally_party_tactics"),
				
				(call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
				(assign, ":enemy_count", reg(0)),
				
				(party_get_skill_level, ":enemy_party_tactics",  "p_collective_enemy", skl_tactics),
				
				(val_add, ":friend_count", 1),
				(val_add, ":enemy_count", 1),
				
				(try_begin),
					(ge, ":friend_count", ":enemy_count"),
					(val_mul, ":friend_count", 100),
					(store_div, ":ratio", ":friend_count", ":enemy_count"),
					(store_sub, ":raw_advantage", ":ratio", 100),
				(else_try),
					(val_mul, ":enemy_count", 100),
					(store_div, ":ratio", ":enemy_count", ":friend_count"),
					(store_sub, ":raw_advantage", 100, ":ratio"),
				(try_end),
				(val_mul, ":raw_advantage", 2),
				
				(val_mul, ":player_party_tactics", 30),
				(val_mul, ":enemy_party_tactics", 30),
				(val_add, ":raw_advantage", ":player_party_tactics"),
				(val_sub, ":raw_advantage", ":enemy_party_tactics"),
				(val_div, ":raw_advantage", 100),
				
				
				(assign, reg0, ":raw_advantage"),
				(display_message, "@Battle Advantage = {reg0}.", 0xFFFFFFFF),
		])
		
		# script_find_high_ground_around_pos1
		# Input: pos1 should hold center_position_no
		#        arg1: team_no
		#        arg2: search_radius (in meters)
		# Output: pos52 contains highest ground within <search_radius> meters of team leader
		# Destroys position registers: pos10, pos11, pos15
find_high_ground_around_pos1 = (
	"find_high_ground_around_pos1",
			[
				(store_script_param, ":team_no", 1),
				(store_script_param, ":search_radius", 2),
				(val_mul, ":search_radius", 100),
				(get_scene_boundaries, pos10,pos11),
				(team_get_leader, ":ai_leader", ":team_no"),
				(agent_get_position, pos1, ":ai_leader"),
				(set_fixed_point_multiplier, 100),
				(position_get_x, ":o_x", pos1),
				(position_get_y, ":o_y", pos1),
				(store_sub, ":min_x", ":o_x", ":search_radius"),
				(store_sub, ":min_y", ":o_y", ":search_radius"),
				(store_add, ":max_x", ":o_x", ":search_radius"),
				(store_add, ":max_y", ":o_y", ":search_radius"),
				(position_get_x, ":scene_min_x", pos10),
				(position_get_x, ":scene_max_x", pos11),
				(position_get_y, ":scene_min_y", pos10),
				(position_get_y, ":scene_max_y", pos11),
				#do not find positions close to borders (20 m)
				(val_add, ":scene_min_x", 2000),
				(val_sub, ":scene_max_x", 2000),
				(val_add, ":scene_min_y", 2000),
				(val_sub, ":scene_max_y", 2000),
				(val_max, ":min_x", ":scene_min_x"),
				(val_max, ":min_y", ":scene_min_y"),
				(val_min, ":max_x", ":scene_max_x"),
				(val_min, ":max_y", ":scene_max_y"),
				
				(store_div, ":min_x_meters", ":min_x", 100),
				(store_div, ":min_y_meters", ":min_y", 100),
				(store_div, ":max_x_meters", ":max_x", 100),
				(store_div, ":max_y_meters", ":max_y", 100),
				
				(assign, ":highest_pos_z", -10000),
				(copy_position, pos52, pos1),
				(init_position, pos15),
				
				(try_for_range, ":i_x", ":min_x_meters", ":max_x_meters"),
					(store_mul, ":i_x_cm", ":i_x", 100),
					(try_for_range, ":i_y", ":min_y_meters", ":max_y_meters"),
						(store_mul, ":i_y_cm", ":i_y", 100),
						(position_set_x, pos15, ":i_x_cm"),
						(position_set_y, pos15, ":i_y_cm"),
						(position_set_z, pos15, 10000),
						(position_set_z_to_ground_level, pos15),
						(position_get_z, ":cur_pos_z", pos15),
						(try_begin),
							(gt, ":cur_pos_z", ":highest_pos_z"),
							(copy_position, pos52, pos15),
							(assign, ":highest_pos_z", ":cur_pos_z"),
						(try_end),
					(try_end),
				(try_end),
		])

		# script_select_battle_tactic_aux
		# Input: team_no
		# Output: battle_tactic
select_battle_tactic_aux = (
	"select_battle_tactic_aux",
			[
				(store_script_param, ":team_no", 1),
				(store_script_param, ":defense_not_an_option", 2),
				(assign, ":battle_tactic", 0),
				(get_player_agent_no, ":player_agent"),
				(agent_get_team, ":player_team", ":player_agent"),
				(try_begin),
					(eq, "$cant_leave_encounter", 1),
					(teams_are_enemies, ":team_no", ":player_team"),
					(assign, ":defense_not_an_option", 1),
				(try_end),
				(call_script, "script_team_get_class_percentages", ":team_no", 0),
				#      (assign, ":ai_perc_infantry", reg0),
				(assign, ":ai_perc_archers",  reg1),
				(assign, ":ai_perc_cavalry",  reg2),
				(call_script, "script_team_get_class_percentages", ":team_no", 1),#enemies of the ai_team
				#      (assign, ":enemy_perc_infantry", reg0),
				#      (assign, ":enemy_perc_archers",  reg1),
				#      (assign, ":enemy_perc_cavalry",  reg2),
				
				(store_random_in_range, ":rand", 0, 100),
				(try_begin),
					(assign, ":continue", 0),
					(try_begin),
						(teams_are_enemies, ":team_no", ":player_team"),
						(party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_hero_party),
						(assign, ":continue", 1),
					(else_try),
						(neg|teams_are_enemies, ":team_no", ":player_team"),
						(gt, "$g_ally_party", 0),
						(party_slot_eq, "$g_ally_party", slot_party_type, spt_kingdom_hero_party),
						(assign, ":continue", 1),
					(try_end),
					#(this_or_next|lt, ":rand", 20),
					(eq, ":continue", 1),
					(store_faction_of_party, ":enemy_faction_no", "$g_enemy_party"),
					(neq, ":enemy_faction_no", "fac_kingdom_3"), #don't let khergits use battle tactics
					(neq, ":enemy_faction_no", "fac_kingdom_27"), #don't let khergits use battle tactics
					(try_begin),
						(eq, ":defense_not_an_option", 0),
						(gt, ":ai_perc_archers", 50),
						(lt, ":ai_perc_cavalry", 35),
						(assign, ":battle_tactic", btactic_hold),
					(else_try),
						(lt, ":rand", 80),
						(assign, ":battle_tactic", btactic_follow_leader),
					(try_end),
				(try_end),
				(assign, reg0, ":battle_tactic"),
		])

		
		# script_calculate_team_powers
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: ally_power, enemy_power
calculate_team_powers = (
	"calculate_team_powers",
			[
				(store_script_param, ":agent_no", 1),
				
				(try_begin),
					(assign, ":agent_side", 0),
					(agent_is_ally, ":agent_no"),
					(assign, ":agent_side", 1),
				(try_end),
				
				(assign, ":ally_power", 0),
				(assign, ":enemy_power", 0),
				
				(try_for_agents, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(agent_is_alive, ":cur_agent"),
					
					(try_begin),
						(assign, ":agent_side_cur", 0),
						(agent_is_ally, ":cur_agent"),
						(assign, ":agent_side_cur", 1),
					(try_end),
					
					(try_begin),
						(agent_get_horse, ":agent_horse_id", ":cur_agent"),
						(neq, ":agent_horse_id", -1),
						(assign, ":agent_power", 2), #if this agent is horseman then his power effect is 2
					(else_try),
						(assign, ":agent_power", 1), #if this agent is walker then his power effect is 1
					(try_end),
					
					(try_begin),
						(eq, ":agent_side", ":agent_side_cur"),
						(val_add, ":ally_power", ":agent_power"),
					(else_try),
						(val_add, ":enemy_power", ":agent_power"),
					(try_end),
				(try_end),
				
				(assign, reg0, ":ally_power"),
				(assign, reg1, ":enemy_power"),
		]) #ozan

		
		# script_battle_tactic_apply_aux
		# Input: team_no, battle_tactic
		# Output: battle_tactic
orig_battle_tactic_apply_aux = (
	"orig_battle_tactic_apply_aux",
			[
				(store_script_param, ":team_no", 1),
				(store_script_param, ":battle_tactic", 2),
				(store_mission_timer_a, ":mission_time"),
				(try_begin),
					(eq, ":battle_tactic", btactic_hold),
					(copy_position, pos1, pos52),
					(call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no", 1),
					(assign, ":avg_dist", reg0),
					(assign, ":min_dist", reg1),
					(try_begin),
						(this_or_next|lt, ":min_dist", 1000),
						(lt, ":avg_dist", 4000),
						(assign, ":battle_tactic", 0),
						(team_give_order, ":team_no", grc_everyone, mordr_charge),
					(try_end),
				(else_try),
					(eq, ":battle_tactic", btactic_follow_leader),
					(team_get_leader, ":ai_leader", ":team_no"),
					(try_begin),
						(ge, ":ai_leader", 0),
						(agent_is_alive, ":ai_leader"),
						(agent_set_speed_limit, ":ai_leader", 9),
						(call_script, "script_team_get_average_position_of_enemies", ":team_no"),
						(copy_position, pos60, pos0),
						(agent_get_position, pos61, ":ai_leader"),
						(position_transform_position_to_local, pos62, pos61, pos60), #pos62 = vector to enemy w.r.t leader
						(position_normalize_origin, ":distance_to_enemy", pos62),
						(convert_from_fixed_point, ":distance_to_enemy"),
						(assign, reg17, ":distance_to_enemy"),
						(position_get_x, ":dir_x", pos62),
						(position_get_y, ":dir_y", pos62),
						(val_mul, ":dir_x", 23),
						(val_mul, ":dir_y", 23), #move 23 meters
						(position_set_x, pos62, ":dir_x"),
						(position_set_y, pos62, ":dir_y"),
						
						(position_transform_position_to_parent, pos63, pos61, pos62), #pos63 is 23m away from leader in the direction of the enemy.
						(position_set_z_to_ground_level, pos63),
						
						(team_give_order, ":team_no", grc_everyone, mordr_hold),
						(team_set_order_position, ":team_no", grc_everyone, pos63),
						(agent_get_position, pos1, ":ai_leader"),
						(try_begin),
							(lt, ":distance_to_enemy", 50),
							(ge, ":mission_time", 30),
							(assign, ":battle_tactic", 0),
							(team_give_order, ":team_no", grc_everyone, mordr_charge),
							(agent_set_speed_limit, ":ai_leader", 60),
						(try_end),
					(else_try),
						(assign, ":battle_tactic", 0),
						(team_give_order, ":team_no", grc_everyone, mordr_charge),
					(try_end),
				(try_end),
				
				(try_begin), # charge everyone after a while
					(neq, ":battle_tactic", 0),
					(ge, ":mission_time", 300),
					(assign, ":battle_tactic", 0),
					(team_give_order, ":team_no", grc_everyone, mordr_charge),
					(team_get_leader, ":ai_leader", ":team_no"),
					(agent_set_speed_limit, ":ai_leader", 60),
				(try_end),
				(assign, reg0, ":battle_tactic"),
		])