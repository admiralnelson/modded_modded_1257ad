from header import *


	# script_formation_battle_tactic_apply_aux #CABA - OK; Need expansion when new AI divisions to work with
	# Input: team_no, battle_tactic
	# Output: battle_tactic
formation_battle_tactic_apply_aux = (
	"formation_battle_tactic_apply_aux",
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
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
					(team_give_order, ":team_no", grc_everyone, mordr_charge),
				(try_end),
			(else_try),
				(eq, ":battle_tactic", btactic_follow_leader),
				(team_get_leader, ":ai_leader", ":team_no"),
				(try_begin),
					(agent_is_alive, ":ai_leader"),
					(agent_set_speed_limit, ":ai_leader", 9),
					(call_script, "script_team_get_average_position_of_enemies", ":team_no"),
					(copy_position, pos60, pos0),
					(ge, ":ai_leader", 0),
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
#formations code
			(call_script, "script_point_y_toward_position", pos63, pos60),
			(agent_get_position, pos49, ":ai_leader"),
			(agent_set_position, ":ai_leader", pos63),	#fake out script_battlegroup_place_around_leader
			(call_script, "script_division_reset_places"),
			(call_script, "script_get_default_formation", ":team_no"),
			(assign, ":fformation", reg0),
			
			(try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":fformation"),
			(store_add, ":slot", slot_team_d0_formation, grc_infantry),
			(team_set_slot, ":team_no", ":slot", ":fformation"),
			(store_add, ":slot", slot_team_d0_formation_space, grc_infantry),
			(team_set_slot, ":team_no", ":slot", 0),
			(else_try),
			(call_script, "script_formation_end", ":team_no", grc_infantry),
			(try_end),
			(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_infantry),
			
			(try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_archers, formation_default),
			(store_add, ":slot", slot_team_d0_formation, grc_archers),
			(team_set_slot, ":team_no", ":slot", formation_default),
			(store_add, ":slot", slot_team_d0_formation_space, grc_archers),
			(team_set_slot, ":team_no", ":slot", 2),
			(else_try),
			(call_script, "script_formation_end", ":team_no", grc_archers),
			(try_end),
			(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_archers),
			
			(try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
			(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
			(team_set_slot, ":team_no", ":slot", formation_wedge),
			(store_add, ":slot", slot_team_d0_formation_space, grc_cavalry),
			(team_set_slot, ":team_no", ":slot", 0),
			(else_try),
			(call_script, "script_formation_end", ":team_no", grc_cavalry),
			(try_end),
			(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_cavalry),
		
			(agent_set_position, ":ai_leader", pos49),
#end formations code
					(agent_get_position, pos1, ":ai_leader"),
					(try_begin),
						(lt, ":distance_to_enemy", 50),
						(ge, ":mission_time", 30),
						(assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
						(team_give_order, ":team_no", grc_everyone, mordr_charge),
						(agent_set_speed_limit, ":ai_leader", 60),
					(try_end),
				(else_try),
					(assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
					(team_give_order, ":team_no", grc_everyone, mordr_charge),
				(try_end),
			(try_end),
			
			(try_begin), # charge everyone after a while
				(neq, ":battle_tactic", 0),
				(ge, ":mission_time", 300),
				(assign, ":battle_tactic", 0),
		(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
		(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
		(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
				(team_give_order, ":team_no", grc_everyone, mordr_charge),
				(team_get_leader, ":ai_leader", ":team_no"),
				(agent_set_speed_limit, ":ai_leader", 60),
			(try_end),
			(assign, reg0, ":battle_tactic"),
	])


	# Replacement script for battle_tactic_init_aux to switch between using
	# M&B Standard AI with changes for formations and original based on
	# NOTE: original script "battle_tactic_apply_aux" should be renamed to "orig_battle_tactic_apply_aux"
	# constant formation_native_ai_use_formation ( 0: original, 1: use formation )
	# script_battle_tactic_apply_aux
	# Input: team_no, battle_tactic
	# Output: battle_tactic
battle_tactic_apply_aux = (
	"battle_tactic_apply_aux",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":battle_tactic", 2),
		(try_begin),
		(eq, formation_native_ai_use_formation, 1),
		(call_script, "script_formation_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
		(else_try),
		(call_script, "script_orig_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
		(try_end),
	])

	# # AI with Formations Scripts
	# script_calculate_decision_numbers by motomataru
	# Input: AI team, size relative to battle in %
	# Output: reg0 - battle presence plus level bump, reg1 - level bump (team avg level / 3)
calculate_decision_numbers = (
	"calculate_decision_numbers", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":battle_presence", 2),
	(try_begin),
		(team_get_slot, reg0, ":team_no", slot_team_level),
		(store_div, reg1, reg0, 3),
		(store_add, reg0, ":battle_presence", reg1),	#decision w.r.t. all enemy teams
	(try_end)
	])
	
	
		
	# script_find_high_ground_around_pos1_corrected by motomataru
	# Input:	arg1: destination position
	#			arg2: search_radius (in meters)
	#			pos1 should hold center_position_no
	# Output:	destination contains highest ground within a <search_radius> meter square around pos1
	# Also uses position registers: pos0
find_high_ground_around_pos1_corrected = (
	"find_high_ground_around_pos1_corrected", [
	(store_script_param, ":destination_pos", 1),
	(store_script_param, ":search_radius", 2),
	(assign, ":fixed_point_multiplier", 1),
	(convert_to_fixed_point, ":fixed_point_multiplier"),
	(set_fixed_point_multiplier, 1),
	
	(position_get_x, ":o_x", pos1),
	(position_get_y, ":o_y", pos1),
	(store_sub, ":min_x", ":o_x", ":search_radius"),
	(store_sub, ":min_y", ":o_y", ":search_radius"),
	(store_add, ":max_x", ":o_x", ":search_radius"),
	(store_add, ":max_y", ":o_y", ":search_radius"),
	
	(get_scene_boundaries, ":destination_pos", pos0),
	(position_get_x, ":scene_min_x", ":destination_pos"),
	(position_get_x, ":scene_max_x", pos0),
	(position_get_y, ":scene_min_y", ":destination_pos"),
	(position_get_y, ":scene_max_y", pos0),
	(val_max, ":min_x", ":scene_min_x"),
	(val_max, ":min_y", ":scene_min_y"),
	(val_min, ":max_x", ":scene_max_x"),
	(val_min, ":max_y", ":scene_max_y"),

	(assign, ":highest_pos_z", -100),
	(copy_position, ":destination_pos", pos1),
	(init_position, pos0),

	(try_for_range, ":i_x", ":min_x", ":max_x"),
		(try_for_range, ":i_y", ":min_y", ":max_y"),
			(position_set_x, pos0, ":i_x"),
			(position_set_y, pos0, ":i_y"),
			(position_set_z_to_ground_level, pos0),
			(position_get_z, ":cur_pos_z", pos0),
			(try_begin),
				(gt, ":cur_pos_z", ":highest_pos_z"),
				(copy_position, ":destination_pos", pos0),
				(assign, ":highest_pos_z", ":cur_pos_z"),
			(try_end),
		(try_end),
	(try_end),
	
	(set_fixed_point_multiplier, ":fixed_point_multiplier"),
	])
		