from header import *

license_window = ( 
	"license_window",0,0,[
	(ti_on_presentation_load, 
		[
			(try_begin),	
					(str_clear, s0),
					(str_store_string, s0, "str_modded2x_AGPL"),
					(create_text_overlay, "$g_presentation_obj_4", "@LALALALALLALALALALA{s0}", tf_scrollable),
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
		]),
	])

fizzbuzz = (
	"fizzbuzz",prsntf_read_only,mesh_load_window,[
		(ti_on_presentation_load,
			[
				(set_fixed_point_multiplier, 1000),
				(try_begin),
					(create_game_button_overlay, "$g_presentation_obj_3", "@Back"),
		        	(position_set_x, pos1, 500),
		        	(position_set_y, pos1, 500),
		        	(overlay_set_position, "$g_presentation_obj_3", pos1),
				(try_end),
			]),
		(ti_on_presentation_event_state_change,
		 	[
				(store_trigger_param_1, ":object"),
				(store_trigger_param_2, ":value"),
				(try_begin),
					(try_begin),
						(eq, ":object", "$g_presentation_obj_3"),
							(try_begin),
								#(start_presentation, "prsnt_game_start"),
								(presentation_set_duration, 0),
								(start_presentation, "prsnt_game_start"),
							(try_end),
					(try_end),
				(try_end),
		]),
])

