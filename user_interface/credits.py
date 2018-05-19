from header import *


game_credits =	(
	"game_credits",prsntf_read_only,mesh_load_window,[
			(ti_on_presentation_load,
			 [(assign, "$g_presentation_credits_obj_1", -1),
				(assign, "$g_presentation_credits_obj_2", -1),
				(assign, "$g_presentation_credits_obj_3", -1),
				(assign, "$g_presentation_credits_obj_4", -1),
				(assign, "$g_presentation_credits_obj_5", -1),
				(assign, "$g_presentation_credits_obj_6", -1),
				(assign, "$g_presentation_credits_obj_7", -1),
				(assign, "$g_presentation_credits_obj_8", -1),
				(assign, "$g_presentation_credits_obj_9", -1),
				(assign, "$g_presentation_credits_obj_10", -1),
				(assign, "$g_presentation_credits_obj_11", -1),
				(assign, "$g_presentation_credits_obj_12", -1),
				(assign, "$g_presentation_credits_obj_1_alpha", 0),
				(assign, "$g_presentation_credits_obj_2_alpha", 0),
				(assign, "$g_presentation_credits_obj_3_alpha", 0),
				(assign, "$g_presentation_credits_obj_4_alpha", 0),
				(assign, "$g_presentation_credits_obj_5_alpha", 0),
				(assign, "$g_presentation_credits_obj_6_alpha", 0),
				(assign, "$g_presentation_credits_obj_7_alpha", 0),
				(assign, "$g_presentation_credits_obj_8_alpha", 0),
				(assign, "$g_presentation_credits_obj_9_alpha", 0),
				]),
			(ti_on_presentation_run,
			 [
				(store_trigger_param_1, ":cur_time"),
				(set_fixed_point_multiplier, 1000),
				(presentation_set_duration, 1000000),
				(try_begin),
					(this_or_next|key_clicked, key_space),
					(this_or_next|key_clicked, key_enter),
					(this_or_next|key_clicked, key_escape),
					(this_or_next|key_clicked, key_back_space),
					(this_or_next|key_clicked, key_left_mouse_button),
			(this_or_next|key_clicked, key_right_mouse_button),
					(this_or_next|key_clicked, key_xbox_ltrigger),
			(key_clicked, key_xbox_rtrigger),
					(presentation_set_duration, 0),
				(try_end),
				(try_begin),
					(lt, "$g_presentation_credits_obj_1", 0),
					(str_store_string, s1, "str_credits_1"),
					(create_text_overlay, "$g_presentation_credits_obj_1", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_1", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_1", 0),
					(position_set_x, pos1, 1500),
					(position_set_y, pos1, 1500),
					(overlay_set_size, "$g_presentation_credits_obj_1", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_1", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_1", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 2000),
					(eq, "$g_presentation_credits_obj_1_alpha", 0),
					(assign, "$g_presentation_credits_obj_1_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_1", 1000, 0x00),
				(else_try),
					(gt, ":cur_time", 3500),
					(lt, "$g_presentation_credits_obj_2", 0),
					(str_store_string, s1, "str_credits_2"),
					(create_text_overlay, "$g_presentation_credits_obj_2", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_2", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_2", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_2", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_2", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_2", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 5500),
					(eq, "$g_presentation_credits_obj_2_alpha", 0),
					(assign, "$g_presentation_credits_obj_2_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_2", 1000, 0x00),
				(else_try),
					(gt, ":cur_time", 7000),
					(lt, "$g_presentation_credits_obj_3", 0),
					(str_store_string, s1, "str_credits_3"),
					(create_text_overlay, "$g_presentation_credits_obj_3", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_3", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_3", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_3", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_3", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_3", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 9000),
					(eq, "$g_presentation_credits_obj_3_alpha", 0),
					(assign, "$g_presentation_credits_obj_3_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_3", 1000, 0),
				(else_try),
					(gt, ":cur_time", 10500),
					(lt, "$g_presentation_credits_obj_4", 0),
					(str_store_string, s1, "str_credits_4"),
					(create_text_overlay, "$g_presentation_credits_obj_4", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_4", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_4", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_4", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_4", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_4", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 12500),
					(eq, "$g_presentation_credits_obj_4_alpha", 0),
					(assign, "$g_presentation_credits_obj_4_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_4", 1000, 0),
				(else_try),
					(gt, ":cur_time", 14000),
					(lt, "$g_presentation_credits_obj_5", 0),
					(str_store_string, s1, "str_credits_5"),
					(create_text_overlay, "$g_presentation_credits_obj_5", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_5", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_5", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_5", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_5", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_5", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 16000),
					(eq, "$g_presentation_credits_obj_5_alpha", 0),
					(assign, "$g_presentation_credits_obj_5_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_5", 1000, 0),
				(else_try),
					(gt, ":cur_time", 17500),
					(lt, "$g_presentation_credits_obj_6", 0),
					(str_store_string, s1, "str_credits_6"),
					(create_text_overlay, "$g_presentation_credits_obj_6", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_6", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_6", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_6", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_6", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_6", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 19500),
					(eq, "$g_presentation_credits_obj_6_alpha", 0),
					(assign, "$g_presentation_credits_obj_6_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_6", 1000, 0),
				(else_try),
					(gt, ":cur_time", 21000),
					(lt, "$g_presentation_credits_obj_7", 0),
					(str_store_string, s1, "str_credits_7"),
					(create_text_overlay, "$g_presentation_credits_obj_7", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_7", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_7", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_7", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_7", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_7", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 23000),
					(eq, "$g_presentation_credits_obj_7_alpha", 0),
					(assign, "$g_presentation_credits_obj_7_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_7", 1000, 0),
				(else_try),
					(gt, ":cur_time", 24500),
					(lt, "$g_presentation_credits_obj_8", 0),
					(str_store_string, s1, "str_credits_8"),
					(create_text_overlay, "$g_presentation_credits_obj_8", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_8", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_8", 0),
					(position_set_x, pos1, 1750),
					(position_set_y, pos1, 1750),
					(overlay_set_size, "$g_presentation_credits_obj_8", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 375),
					(overlay_set_position, "$g_presentation_credits_obj_8", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_8", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 26500),
					(eq, "$g_presentation_credits_obj_8_alpha", 0),
					(assign, "$g_presentation_credits_obj_8_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_8", 1000, 0),
				(else_try),
					(gt, ":cur_time", 28000),
					(lt, "$g_presentation_credits_obj_9", 0),
					(str_store_string, s1, "str_credits_10"),
					(create_text_overlay, "$g_presentation_credits_obj_9", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_9", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_9", 0),
					(position_set_x, pos1, 750),
					(position_set_y, pos1, 750),
					(overlay_set_size, "$g_presentation_credits_obj_9", pos1),
					(position_set_x, pos1, 250),
					(position_set_y, pos1, 485),
					(overlay_set_position, "$g_presentation_credits_obj_9", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_9", 1000, 0xFF),

					(str_store_string, s1, "str_credits_11"),
					(create_text_overlay, "$g_presentation_credits_obj_10", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_10", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_10", 0),
					(position_set_x, pos1, 750),
					(position_set_y, pos1, 750),
					(overlay_set_size, "$g_presentation_credits_obj_10", pos1),
					(position_set_x, pos1, 750),
					(position_set_y, pos1, 470),
					(overlay_set_position, "$g_presentation_credits_obj_10", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_10", 1000, 0xFF),

					(str_store_string, s1, "str_credits_12"),
					(create_text_overlay, "$g_presentation_credits_obj_11", s1, tf_center_justify|tf_double_space|tf_vertical_align_center),
					(overlay_set_color, "$g_presentation_credits_obj_11", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_11", 0),
					(position_set_x, pos1, 750),
					(position_set_y, pos1, 750),
					(overlay_set_size, "$g_presentation_credits_obj_11", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 105),
					(overlay_set_position, "$g_presentation_credits_obj_11", pos1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_11", 1000, 0xFF),
				(else_try),
					(gt, ":cur_time", 34000),
					(eq, "$g_presentation_credits_obj_9_alpha", 0),
					(assign, "$g_presentation_credits_obj_9_alpha", 1),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_9", 1000, 0),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_10", 1000, 0),
					(overlay_animate_to_alpha, "$g_presentation_credits_obj_11", 1000, 0),
				(else_try),
					(gt, ":cur_time", 35500),
					(lt, "$g_presentation_credits_obj_12", 0),
					(str_store_string, s1, "str_credits_9"),
					(create_text_overlay, "$g_presentation_credits_obj_12", s1, tf_center_justify|tf_double_space),
					(overlay_set_color, "$g_presentation_credits_obj_12", 0),
					(overlay_set_alpha, "$g_presentation_credits_obj_12", 0xFF),
					(position_set_x, pos1, 1000),
					(position_set_y, pos1, 1000),
					(overlay_set_size, "$g_presentation_credits_obj_12", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, -4800),
					(overlay_set_position, "$g_presentation_credits_obj_12", pos1),
					(position_set_x, pos1, 500),
					(position_set_y, pos1, 760),
					(overlay_animate_to_position, "$g_presentation_credits_obj_12", 70000, pos1),
				(else_try),
					(gt, ":cur_time", 105500),
					(presentation_set_duration, 0),
				(try_end),
				]),
		])