from header import *


# script_convert_3d_pos_to_map_pos
# Input: pos1 = 3d_pos, pos2 = map_size_pos
# Output: pos0 = map_pos
convert_3d_pos_to_map_pos = (
	"convert_3d_pos_to_map_pos",
			[(set_fixed_point_multiplier, 1000),
				(position_transform_position_to_local, pos3, pos2, pos1),
				(position_get_x, ":agent_x_pos", pos3),
				(position_get_y, ":agent_y_pos", pos3),
				(val_div, ":agent_x_pos", "$g_battle_map_scale"),
				(val_div, ":agent_y_pos", "$g_battle_map_scale"),
				(set_fixed_point_multiplier, 1000),
				(store_sub, ":map_x", 980, "$g_battle_map_width"),
				(store_sub, ":map_y", 730, "$g_battle_map_height"),
				(val_add, ":agent_x_pos", ":map_x"),
				(val_add, ":agent_y_pos", ":map_y"),
				(position_set_x, pos0, ":agent_x_pos"),
				(position_set_y, pos0, ":agent_y_pos"),
		])

		
# script_store_movement_order_name_to_s1
# Input: arg1 = team_no, arg2 = class_no
# Output: s1 = order_name
store_movement_order_name_to_s1 = (
	"store_movement_order_name_to_s1",
			[(store_script_param_1, ":team_no"),
				(store_script_param_2, ":class_no"),
				(team_get_movement_order, ":cur_order", ":team_no", ":class_no"),
				(try_begin),
					(eq, ":cur_order", mordr_hold),
					(str_store_string, s1, "@Holding"),
				(else_try),
					(eq, ":cur_order", mordr_follow),
					(str_store_string, s1, "@Following"),
				(else_try),
					(eq, ":cur_order", mordr_charge),
					(str_store_string, s1, "@Charging"),
				(else_try),
					(eq, ":cur_order", mordr_advance),
					(str_store_string, s1, "@Advancing"),
				(else_try),
					(eq, ":cur_order", mordr_fall_back),
					(str_store_string, s1, "@Falling Back"),
				(else_try),
					(eq, ":cur_order", mordr_stand_closer),
					(str_store_string, s1, "@Standing Closer"),
				(else_try),
					(eq, ":cur_order", mordr_spread_out),
					(str_store_string, s1, "@Spreading Out"),
				(else_try),
					(eq, ":cur_order", mordr_stand_ground),
					(str_store_string, s1, "@Standing"),
				(else_try),
					(str_store_string, s1, "@N/A"),
				(try_end),
		])
		
# script_store_riding_order_name_to_s1
# Input: arg1 = team_no, arg2 = class_no
# Output: s1 = order_name
store_riding_order_name_to_s1 = (
	"store_riding_order_name_to_s1",
			[(store_script_param_1, ":team_no"),
				(store_script_param_2, ":class_no"),
				(team_get_riding_order, ":cur_order", ":team_no", ":class_no"),
				(try_begin),
					(eq, ":cur_order", rordr_free),
					(str_store_string, s1, "@Free"),
				(else_try),
					(eq, ":cur_order", rordr_mount),
					(str_store_string, s1, "@Mount"),
				(else_try),
					(eq, ":cur_order", rordr_dismount),
					(str_store_string, s1, "@Dismount"),
				(else_try),
					(str_store_string, s1, "@N/A"),
				(try_end),
		])
		
# script_store_weapon_usage_order_name_to_s1
# Input: arg1 = team_no, arg2 = class_no
# Output: s1 = order_name
store_weapon_usage_order_name_to_s1 = (
	"store_weapon_usage_order_name_to_s1",
			[(store_script_param_1, ":team_no"),
				(store_script_param_2, ":class_no"),
				(team_get_weapon_usage_order, ":cur_order", ":team_no", ":class_no"),
				(team_get_hold_fire_order, ":cur_hold_fire", ":team_no", ":class_no"),
				(try_begin),
					(eq, ":cur_order", wordr_use_any_weapon),
					(eq, ":cur_hold_fire", aordr_fire_at_will),
					(str_store_string, s1, "@Any Weapon"),
				(else_try),
					(eq, ":cur_order", wordr_use_blunt_weapons),
					(eq, ":cur_hold_fire", aordr_fire_at_will),
					(str_store_string, s1, "@Blunt Weapons"),
				(else_try),
					(eq, ":cur_order", wordr_use_any_weapon),
					(eq, ":cur_hold_fire", aordr_hold_your_fire),
					(str_store_string, s1, "str_hold_fire"),
				(else_try),
					(eq, ":cur_order", wordr_use_blunt_weapons),
					(eq, ":cur_hold_fire", aordr_hold_your_fire),
					(str_store_string, s1, "str_blunt_hold_fire"),
				(else_try),
					(str_store_string, s1, "@N/A"),
				(try_end),
		])
		