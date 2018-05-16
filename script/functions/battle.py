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

# script_orig_battle_tactic_apply_aux
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

		# script_team_get_class_percentages
		# Input: arg1: team_no, arg2: try for team's enemies
		# Output: reg0: percentage infantry, reg1: percentage archers, reg2: percentage cavalry
team_get_class_percentages = (
	"team_get_class_percentages",
			[
				(assign, ":num_infantry", 0),
				(assign, ":num_archers", 0),
				(assign, ":num_cavalry", 0),
				(assign, ":num_total", 0),
				(store_script_param, ":team_no", 1),
				(store_script_param, ":negate", 2),
				(try_for_agents,":cur_agent"),
					(agent_is_alive, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(agent_get_team, ":agent_team", ":cur_agent"),
					(assign, ":continue", 0),
					(try_begin),
						(eq, ":negate", 1),
						(teams_are_enemies, ":agent_team", ":team_no"),
						(assign, ":continue", 1),
					(else_try),
						(eq, ":agent_team", ":team_no"),
						(assign, ":continue", 1),
					(try_end),
					(eq, ":continue", 1),
					(val_add, ":num_total", 1),
					(agent_get_class, ":agent_class", ":cur_agent"),
					(try_begin),
						(eq, ":agent_class", grc_infantry),
						(val_add,  ":num_infantry", 1),
					(else_try),
						(eq, ":agent_class", grc_archers),
						(val_add,  ":num_archers", 1),
					(else_try),
						(eq, ":agent_class", grc_cavalry),
						(val_add,  ":num_cavalry", 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq,  ":num_total", 0),
					(assign,  ":num_total", 1),
				(try_end),
				(store_mul, ":perc_infantry",":num_infantry",100),
				(val_div, ":perc_infantry",":num_total"),
				(store_mul, ":perc_archers",":num_archers",100),
				(val_div, ":perc_archers",":num_total"),
				(store_mul, ":perc_cavalry",":num_cavalry",100),
				(val_div, ":perc_cavalry",":num_total"),
				(assign, reg0, ":perc_infantry"),
				(assign, reg1, ":perc_archers"),
				(assign, reg2, ":perc_cavalry"),
		])
		
		# script_get_closest3_distance_of_enemies_at_pos1
		# Input: arg1: team_no, pos1
		# Output: reg0: distance in cms. tom: reg4 - the closest agent id
get_closest3_distance_of_enemies_at_pos1 = (
	"get_closest3_distance_of_enemies_at_pos1",
			[
				(assign, ":min_distance_1", 100000),
				(assign, ":min_distance_2", 100000),
				(assign, ":min_distance_3", 100000),
				(assign, ":closest_agent", -1), #tom
		
				(store_script_param, ":team_no", 1),
				(try_for_agents,":cur_agent"),
					(agent_is_alive, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(agent_get_team, ":agent_team", ":cur_agent"),
					(teams_are_enemies, ":agent_team", ":team_no"),
					
					(agent_get_position, pos2, ":cur_agent"),
					(get_distance_between_positions,":cur_dist",pos2,pos1),
					(try_begin),
						(lt, ":cur_dist", ":min_distance_1"),
						(assign, ":min_distance_3", ":min_distance_2"),
						(assign, ":min_distance_2", ":min_distance_1"),
						(assign, ":min_distance_1", ":cur_dist"),
			(assign, ":closest_agent", ":cur_agent"), #tom
					(else_try),
						(lt, ":cur_dist", ":min_distance_2"),
						(assign, ":min_distance_3", ":min_distance_2"),
						(assign, ":min_distance_2", ":cur_dist"),
					(else_try),
						(lt, ":cur_dist", ":min_distance_3"),
						(assign, ":min_distance_3", ":cur_dist"),
					(try_end),
				(try_end),
				
				(assign, ":total_distance", 0),
				(assign, ":total_count", 0),
				(try_begin),
					(lt, ":min_distance_1", 100000),
					(val_add, ":total_distance", ":min_distance_1"),
					(val_add, ":total_count", 1),
				(try_end),
				(try_begin),
					(lt, ":min_distance_2", 100000),
					(val_add, ":total_distance", ":min_distance_2"),
					(val_add, ":total_count", 1),
				(try_end),
				(try_begin),
					(lt, ":min_distance_3", 100000),
					(val_add, ":total_distance", ":min_distance_3"),
					(val_add, ":total_count", 1),
				(try_end),
				(assign, ":average_distance", 100000),
				(try_begin),
					(gt, ":total_count", 0),
					(store_div, ":average_distance", ":total_distance", ":total_count"),
				(try_end),
				(assign, reg0, ":average_distance"),
				(assign, reg1, ":min_distance_1"),
				(assign, reg2, ":min_distance_2"),
				(assign, reg3, ":min_distance_3"),
				(assign, reg4, ":closest_agent"), #tom
		])

		# script_team_get_average_position_of_enemies
		# Input: arg1: team_no,
		# Output: pos0: average position.
team_get_average_position_of_enemies = (
	"team_get_average_position_of_enemies",
			[
				(store_script_param_1, ":team_no"),
				(init_position, pos0),
				(assign, ":num_enemies", 0),
				(assign, ":accum_x", 0),
				(assign, ":accum_y", 0),
				(assign, ":accum_z", 0),
				(try_for_agents,":enemy_agent"),
					(agent_is_alive, ":enemy_agent"),
					(agent_is_human, ":enemy_agent"),
					(agent_get_team, ":enemy_team", ":enemy_agent"),
					(teams_are_enemies, ":team_no", ":enemy_team"),
					
					(agent_get_position, pos62, ":enemy_agent"),
					
					(position_get_x, ":x", pos62),
					(position_get_y, ":y", pos62),
					(position_get_z, ":z", pos62),
					
					(val_add, ":accum_x", ":x"),
					(val_add, ":accum_y", ":y"),
					(val_add, ":accum_z", ":z"),
					(val_add, ":num_enemies", 1),
				(try_end),
				
				(try_begin), #to avoid division by zeros at below division part.
					(le, ":num_enemies", 0),
					(assign, ":num_enemies", 1),
				(try_end),
				
				(store_div, ":average_x", ":accum_x", ":num_enemies"),
				(store_div, ":average_y", ":accum_y", ":num_enemies"),
				(store_div, ":average_z", ":accum_z", ":num_enemies"),
				
				(position_set_x, pos0, ":average_x"),
				(position_set_y, pos0, ":average_y"),
				(position_set_z, pos0, ":average_z"),
				
				(assign, reg0, ":num_enemies"),
		])

		# script_cf_team_get_average_position_of_agents_with_type_to_pos1
		# Input: arg1 = team_no, arg2 = class_no (grc_everyone, grc_infantry, grc_cavalry, grc_archers, grc_heroes)
		# Output: none, pos1 = average_position (0,0,0 if there are no matching agents)
cf_team_get_average_position_of_agents_with_type_to_pos1 = (
	"cf_team_get_average_position_of_agents_with_type_to_pos1",
			[
				(store_script_param_1, ":team_no"),
				(store_script_param_2, ":division_no"),
				(assign, ":total_pos_x", 0),
				(assign, ":total_pos_y", 0),
				(assign, ":total_pos_z", 0),
				(assign, ":num_agents", 0),
				(set_fixed_point_multiplier, 100),
				(try_for_agents, ":cur_agent"),
					(agent_is_alive, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(agent_get_team, ":cur_team_no", ":cur_agent"),
					(eq, ":cur_team_no", ":team_no"),
					(agent_get_division, ":cur_agent_division", ":cur_agent"),
					(this_or_next|eq, ":division_no", grc_everyone),
					(eq, ":division_no", ":cur_agent_division"),
					(agent_get_position, pos1, ":cur_agent"),
					(position_get_x, ":cur_pos_x", pos1),
					(val_add, ":total_pos_x", ":cur_pos_x"),
					(position_get_y, ":cur_pos_y", pos1),
					(val_add, ":total_pos_y", ":cur_pos_y"),
					(position_get_z, ":cur_pos_z", pos1),
					(val_add, ":total_pos_z", ":cur_pos_z"),
					(val_add, ":num_agents", 1),
				(try_end),
				(gt, ":num_agents", 1),
				(val_div, ":total_pos_x", ":num_agents"),
				(val_div, ":total_pos_y", ":num_agents"),
				(val_div, ":total_pos_z", ":num_agents"),
				(init_position, pos1),
				(position_move_x, pos1, ":total_pos_x"),
				(position_move_y, pos1, ":total_pos_y"),
				(position_move_z, pos1, ":total_pos_z"),
		])


	#script_neutral_behavior_in_fight
	#WARNING: modified by 1257AD devs
	#INPUT: none
	#OUTPUT: none
neutral_behavior_in_fight = (
	"neutral_behavior_in_fight",
		[
		(get_player_agent_no, ":player_agent"),
		(agent_get_position, pos3, ":player_agent"),
		(agent_get_team, ":player_team", ":player_agent"),
		
		(try_begin),
			(gt, "$g_main_attacker_agent", 0),
			(agent_get_team, ":attacker_team_no", "$g_main_attacker_agent"),
			(agent_get_position, pos5, "$g_main_attacker_agent"),
		(else_try),
			(eq, ":attacker_team_no", -1),
			(agent_get_position, pos5, ":player_agent"),
		(try_end),
		
		(set_fixed_point_multiplier, 100),
		
		(try_for_agents, ":agent"),
			(agent_get_team, ":other_team", ":agent"),
			(neq, ":other_team", ":attacker_team_no"),
			(neq, ":other_team", ":player_team"),
			
			(agent_get_troop_id, ":troop_id", ":agent"),
			(neg|is_between, ":troop_id", "trp_teu_village_recruit", "trp_looter"),
			
			(agent_get_position, pos4, ":agent"),
			
			(assign, ":best_position_score", 0),
			(assign, ":best_position", -1),
			
			(try_begin),
			(neg|agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #if agent is running away
			(agent_get_slot, ":target_entry_point_plus_one",  ":agent", slot_agent_is_running_away),
			(store_sub, ":target_entry_point", ":target_entry_point_plus_one", 1),
			(entry_point_get_position, pos6, ":target_entry_point"),
			(get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
			(lt, ":agent_distance_to_target", 100),
			(agent_set_slot, ":agent", slot_agent_is_running_away, 0),
			(try_end),
			
			(agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #if agent is not already running away
			
			(try_begin), #stand in place
			(get_distance_between_positions, ":distance", pos4, pos5),
			(get_distance_between_positions, ":distance_to_player", pos4, pos3),
			
			(val_min, ":distance", ":distance_to_player"),
			
			(this_or_next|gt, ":distance", 700), #7 meters away from main belligerents
			(main_hero_fallen),
			
			(agent_set_scripted_destination, ":agent", pos4),
			(else_try), #get out of the way
			(try_for_range, ":target_entry_point", 0, 64),
				(neg|entry_point_is_auto_generated, ":target_entry_point"),
				(entry_point_get_position, pos6, ":target_entry_point"),
				(get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
				(get_distance_between_positions, ":player_distance_to_target", pos6, pos3),
				(store_sub, ":position_score", ":player_distance_to_target", ":agent_distance_to_target"),
				(ge, ":position_score", 0),
				(try_begin),
				(ge, ":agent_distance_to_target", 2000),
				(store_sub, ":extra_distance", ":agent_distance_to_target", 2000),
				(val_min, ":extra_distance", 1000),
				(val_min, ":agent_distance_to_target", 2000), #if more than 10 meters assume it is 10 meters far while calculating best run away target
				(val_sub, ":agent_distance_to_target", ":extra_distance"),
				(try_end),
				(val_mul, ":position_score", ":agent_distance_to_target"),
				(try_begin),
				(ge, ":position_score", ":best_position_score"),
				(assign, ":best_position_score", ":position_score"),
				(assign, ":best_position", ":target_entry_point"),
				(try_end),
			(try_end),
			
			(try_begin),
				(ge, ":best_position", 0),
				(entry_point_get_position, pos6, ":best_position"),
				(agent_set_speed_limit, ":agent", 10),
				(agent_set_scripted_destination, ":agent", pos6),
				(store_add, ":best_position_plus_one", ":best_position", 1),
				(agent_set_slot, ":agent", slot_agent_is_running_away, ":best_position_plus_one"),
			(try_end),
			(try_end),
		(try_end),
	])

	