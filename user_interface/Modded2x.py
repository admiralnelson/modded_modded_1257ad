from header import *

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

