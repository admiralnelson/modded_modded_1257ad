from header import *

## CC
game_start = (
	"game_start",prsntf_read_only,0,[
		(ti_on_presentation_load,
			[
		
				(presentation_set_duration, 999999),
				(set_fixed_point_multiplier, 1000),

				(create_text_overlay, "$g_presentation_credits_obj_1", "@Anno Domini 1257, modded2x", tf_double_space),
				#(str_store_string, s21, "@ad1257 version: "),
				(str_store_string, s22, "str_revision"),
				#(create_text_overlay, "$g_presentation_credits_obj_2", "@{s21}{s22}", tf_double_space),
				(create_text_overlay, "$g_presentation_credits_obj_2", "@{s22}", tf_double_space),
				(position_set_x, pos1, 1300),
				(position_set_y, pos1, 1300),
				(overlay_set_size, "$g_presentation_credits_obj_1", pos1),
				(overlay_set_size, "$g_presentation_credits_obj_2", pos1),
				(overlay_set_color, "$g_presentation_credits_obj_1", 0xFFFFFF),
				(overlay_set_color, "$g_presentation_credits_obj_2", 0xFFFFFF),

				(position_set_x, pos1, -300),
				(position_set_y, pos1, 650),
				(overlay_set_position, "$g_presentation_credits_obj_1", pos1),
				(position_set_x, pos1, 300),
				(position_set_y, pos1, 650),
				(overlay_animate_to_position, "$g_presentation_credits_obj_1", 600, pos1),

				(position_set_x, pos1, 1300),
				(position_set_y, pos1, 600),
				(overlay_set_position, "$g_presentation_credits_obj_2", pos1),
				(position_set_x, pos1, 350),
				(position_set_y, pos1, 600),
				(overlay_animate_to_position, "$g_presentation_credits_obj_2", 600, pos1),
				
				#modded2x begin
				(create_game_button_overlay, "$g_presentation_obj_1", "@About"),
		        (position_set_x, pos1, 930),
		        (position_set_y, pos1, 700),
		        (overlay_set_position, "$g_presentation_obj_1", pos1),
		        (position_set_x, pos1, 100),
		        (position_set_y, pos1, 30),
		        (overlay_set_size, "$g_presentation_obj_1", pos1),
		        (create_game_button_overlay, "$g_presentation_obj_2", "@Source Code Licence"),
		        (position_set_x, pos1, 750),
		        (position_set_y, pos1, 700),
		        (overlay_set_position, "$g_presentation_obj_2", pos1),
		        (position_set_x, pos1, 150),
		        (position_set_y, pos1, 30),
		        (overlay_set_size, "$g_presentation_obj_2", pos1),
		        (assign, "$temp2", 0),
				#modded2x end
			]),
				#modded2x begin			
			(ti_on_presentation_event_state_change,
		 	[
				(store_trigger_param_1, ":object"),
				(store_trigger_param_2, ":value"),
				(try_begin),
					(try_begin),
						(eq, ":object", "$g_presentation_obj_1"),						
							(str_clear, s0),
							(str_store_string, s0, "str_modded2x_AGPL"),
							(create_text_overlay, "$g_presentation_obj_4", "@{s0}"),
							(position_set_x, pos1, 850),
							(position_set_y, pos1, 850),
							(overlay_set_size, "$g_presentation_obj_4", pos1),
							(position_set_x, pos1, 300),
							(position_set_y, pos1, 650),
							(overlay_set_position, "$g_presentation_obj_4", pos1),
							(position_set_x, pos1, 360),
							(position_set_y, pos1, 130),
							(overlay_set_area_size, "$g_presentation_obj_4", pos1),
							
							
					(try_end),
					(try_begin),
						(eq, ":object", "$g_presentation_obj_2"),
							(presentation_set_duration, 0),
							(dialog_box, "@This mod source code available on github.^^ The source code must be used under AGPL v3.0", "@Source code"),
							#(start_presentation, "prsnt_game_credits"),
					(try_end),
				(try_end),
			]),
				#modded2x end
		])
	## CC
