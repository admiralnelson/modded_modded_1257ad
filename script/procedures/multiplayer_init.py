from header import *

#script_initialize_objects
	# INPUT: none
	# OUTPUT: none
initialize_objects =	("initialize_objects",
		[
			(assign, ":number_of_players", 0),
			(get_max_players, ":num_players"),
			(try_for_range, ":player_no", 0, ":num_players"),
				(player_is_active, ":player_no"),
				(val_add, ":number_of_players", 1),
			(try_end),
			
			#1 player = (Sqrt(1) - 1) * 200 + 1200 = 1200, 1800 (minimum)
			#4 player = (Sqrt(4) - 1) * 200 + 1200 = 1400, 2100
			#9 player = (Sqrt(9) - 1) * 200 + 1200 = 1600, 2400
			#16 player = (Sqrt(16) - 1) * 200 + 1200 = 1800, 2700 (general used)
			#25 player = (Sqrt(25) - 1) * 200 + 1200 = 2000, 3000 (average)
			#36 player = (Sqrt(36) - 1) * 200 + 1200 = 2200, 3300
			#49 player = (Sqrt(49) - 1) * 200 + 1200 = 2400, 3600
			#64 player = (Sqrt(49) - 1) * 200 + 1200 = 2600, 3900
			
			(set_fixed_point_multiplier, 100),
			(val_mul, ":number_of_players", 100),
			(store_sqrt, ":number_of_players", ":number_of_players"),
			(val_sub, ":number_of_players", 100),
			(val_max, ":number_of_players", 0),
			(store_mul, ":effect_of_number_of_players", ":number_of_players", 2),
			(store_add, ":health_catapult", multi_minimum_target_health, ":effect_of_number_of_players"),
			(store_mul, ":health_trebuchet", ":health_catapult", 15), #trebuchet's health is 1.5x of catapult's
			(val_div, ":health_trebuchet", 10),
			(store_mul, ":health_sally_door", ":health_catapult", 18), #sally door's health is 1.8x of catapult's
			(val_div, ":health_sally_door", 10),
			(store_mul, ":health_sally_door_double", ":health_sally_door", 2),
			
			(assign, "$g_number_of_targets_destroyed", 0),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_catapult_destructible"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_catapult_destructible", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_catapult"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_trebuchet_destructible"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_trebuchet_destructible", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_trebuchet"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_e_sally_door_a"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_e_sally_door_a", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_sally_door_a"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_sally_door_a", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_left"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_left", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_right"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_right", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_left"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_left", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_right"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_right", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(store_div, ":health_sally_door_div_3", ":health_sally_door", 3),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_a"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_a", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_b"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_b", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_stop_animating, ":cur_instance_id"),
				(prop_instance_set_position, ":cur_instance_id", pos0),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
			(try_end),
	])


#script_initialize_objects_clients
	# INPUT: none
	# OUTPUT: none
initialize_objects_clients =	("initialize_objects_clients",
		[
			(assign, ":number_of_players", 0),
			(get_max_players, ":num_players"),
			(try_for_range, ":player_no", 0, ":num_players"),
				(player_is_active, ":player_no"),
				(val_add, ":number_of_players", 1),
			(try_end),
			
			#1 player = (Sqrt(1) - 1) * 200 + 1200 = 1200, 1800 (minimum)
			#4 player = (Sqrt(4) - 1) * 200 + 1200 = 1400, 2100
			#9 player = (Sqrt(9) - 1) * 200 + 1200 = 1600, 2400
			#16 player = (Sqrt(16) - 1) * 200 + 1200 = 1800, 2700 (general used)
			#25 player = (Sqrt(25) - 1) * 200 + 1200 = 2000, 3000 (average)
			#36 player = (Sqrt(36) - 1) * 200 + 1200 = 2200, 3300
			#49 player = (Sqrt(49) - 1) * 200 + 1200 = 2400, 3600
			#64 player = (Sqrt(49) - 1) * 200 + 1200 = 2600, 3900
			
			(set_fixed_point_multiplier, 100),
			(val_mul, ":number_of_players", 100),
			(store_sqrt, ":number_of_players", ":number_of_players"),
			(val_sub, ":number_of_players", 100),
			(val_max, ":number_of_players", 0),
			(store_mul, ":effect_of_number_of_players", ":number_of_players", 2),
			(store_add, ":health_catapult", multi_minimum_target_health, ":effect_of_number_of_players"),
			(store_mul, ":health_trebuchet", ":health_catapult", 15), #trebuchet's health is 1.5x of catapult's
			(val_div, ":health_trebuchet", 10),
			(store_mul, ":health_sally_door", ":health_catapult", 18), #trebuchet's health is 1.8x of trebuchet's
			(val_div, ":health_sally_door", 10),
			(store_mul, ":health_sally_door_double", ":health_sally_door", 2),
			
			(assign, "$g_number_of_targets_destroyed", 0),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_catapult_destructible"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_catapult_destructible", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_catapult"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_trebuchet_destructible"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_trebuchet_destructible", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_trebuchet"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_e_sally_door_a"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_e_sally_door_a", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_sally_door_a"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_sally_door_a", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_left"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_left", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_right"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_right", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_left"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_left", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_right"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_right", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
			(try_end),
			
			(store_div, ":health_sally_door_div_3", ":health_sally_door", 3),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_a"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_a", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_b"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_b", ":cur_instance"),
				(prop_instance_enable_physics, ":cur_instance_id", 1),
				(scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
			(try_end),
	])

	#script_multiplayer_init_player_slots
	# Input: arg1 = player_no
	# Output: none
multiplayer_init_player_slots =	(
	"multiplayer_init_player_slots",
		[
			(store_script_param, ":player_no", 1),
			(call_script, "script_multiplayer_clear_player_selected_items", ":player_no"),
			(player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
			(player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, 0),
			(player_set_slot, ":player_no", slot_player_poll_disabled_until_time, 0),
			
			(player_set_slot, ":player_no", slot_player_bot_type_1_wanted, 0),
			(player_set_slot, ":player_no", slot_player_bot_type_2_wanted, 0),
			(player_set_slot, ":player_no", slot_player_bot_type_3_wanted, 0),
			(player_set_slot, ":player_no", slot_player_bot_type_4_wanted, 0),
	])

#script_multiplayer_initialize_belfry_wheel_rotations
		# Input: none
		# Output: none
multiplayer_initialize_belfry_wheel_rotations =	(
	"multiplayer_initialize_belfry_wheel_rotations",
			[
				##    (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
				##    (try_for_range, ":belfry_no", 0, ":num_belfries"),
				##      (store_mul, ":wheel_no", ":belfry_no", 3),
				##      (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
				##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_1_scene_prop_id"),
				##      #belfry wheel_2
				##      (val_add, ":wheel_no", 1),
				##      (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
				##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_2_scene_prop_id"),
				##      #belfry wheel_3
				##      (val_add, ":wheel_no", 1),
				##      (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
				##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_3_scene_prop_id"),
				##    (try_end),
				##
				##    (scene_prop_get_num_instances, ":num_belfries_a", "spr_belfry_a"),
				##
				##    (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
				##    (try_for_range, ":belfry_no", 0, ":num_belfries"),
				##      (store_add, ":wheel_no_plus_num_belfries_a", ":wheel_no", ":num_belfries_a"),
				##      (store_mul, ":wheel_no_plus_num_belfries_a", ":belfry_no", 3),
				##      (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no_plus_num_belfries_a"),
				##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_1_scene_prop_id"),
				##      #belfry wheel_2
				##      (val_add, ":wheel_no_plus_num_belfries_a", 1),
				##      (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no_plus_num_belfries_a"),
				##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_2_scene_prop_id"),
				##      #belfry wheel_3
				##      (val_add, ":wheel_no_plus_num_belfries_a", 1),
				##      (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no_plus_num_belfries_a"),
				##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_3_scene_prop_id"),
				##    (try_end),
				
				(scene_prop_get_num_instances, ":num_wheel", "spr_belfry_wheel"),
				(try_for_range, ":wheel_no", 0, ":num_wheel"),
					(scene_prop_get_instance, ":wheel_id", "spr_belfry_wheel", ":wheel_no"),
					(prop_instance_initialize_rotation_angles, ":wheel_id"),
				(try_end),
				
				(scene_prop_get_num_instances, ":num_winch", "spr_winch"),
				(try_for_range, ":winch_no", 0, ":num_winch"),
					(scene_prop_get_instance, ":winch_id", "spr_winch", ":winch_no"),
					(prop_instance_initialize_rotation_angles, ":winch_id"),
				(try_end),
				
				(scene_prop_get_num_instances, ":num_winch_b", "spr_winch_b"),
				(try_for_range, ":winch_b_no", 0, ":num_winch_b"),
					(scene_prop_get_instance, ":winch_b_id", "spr_winch_b", ":winch_b_no"),
					(prop_instance_initialize_rotation_angles, ":winch_b_id"),
				(try_end),
		])
		