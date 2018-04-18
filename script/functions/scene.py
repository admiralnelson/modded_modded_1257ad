from header import *

#script_game_get_scene_name
	# This script is called from the game engine when a name for the scene is needed.
	# INPUT: arg1 = scene_no
	# OUTPUT: s0 = name
game_get_scene_name =	("game_get_scene_name",
		[
			(store_script_param, ":scene_no", 1),
			(try_begin),
				(is_between, ":scene_no", multiplayer_scenes_begin, multiplayer_scenes_end),
				(store_sub, ":string_id", ":scene_no", multiplayer_scenes_begin),
				(val_add, ":string_id", multiplayer_scene_names_begin),
				(str_store_string, s0, ":string_id"),
			(try_end),
	])

#script_game_get_mission_template_name
	# This script is called from the game engine when a name for the mission template is needed.
	# INPUT: arg1 = mission_template_no
	# OUTPUT: s0 = name
game_get_mission_template_name = (
	"game_get_mission_template_name",
		[
			(store_script_param, ":mission_template_no", 1),
			(call_script, "script_multiplayer_get_mission_template_game_type", ":mission_template_no"),
			(assign, ":game_type", reg0),
			(try_begin),
				(is_between, ":game_type", 0, multiplayer_num_game_types),
				(store_add, ":string_id", ":game_type", multiplayer_game_type_names_begin),
				(str_store_string, s0, ":string_id"),
			(try_end),
	])

#script_get_meeting_scene:
		# INPUT: none
		# OUTPUT: reg0 contain suitable scene_no
		
get_meeting_scene =	(
	"get_meeting_scene",
			[
				(party_get_current_terrain, ":terrain_type", "p_main_party"),
				(assign, ":scene_to_use", "scn_random_scene"),
				(try_begin),
					(eq, ":terrain_type", rt_steppe),
					(assign, ":scene_to_use", "scn_meeting_scene_steppe"),
				(else_try),
					(eq, ":terrain_type", rt_plain),
					(assign, ":scene_to_use", "scn_meeting_scene_plain"),
				(else_try),
					(eq, ":terrain_type", rt_snow),
					(assign, ":scene_to_use", "scn_meeting_scene_snow"),
				(else_try),
					(eq, ":terrain_type", rt_desert),
					(assign, ":scene_to_use", "scn_meeting_scene_desert"),
				(else_try),
					(eq, ":terrain_type", rt_steppe_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_steppe"),
				(else_try),
					(eq, ":terrain_type", rt_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_plain"),
				(else_try),
					(eq, ":terrain_type", rt_snow_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_snow"),
				(else_try),
					(eq, ":terrain_type", rt_desert_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_desert"),
				(else_try),
					(call_script, "script_cf_is_party_on_water", "p_main_party"),
					(assign, ":scene_to_use", "scn_meeting_scene_sea"),
				(else_try),
					(assign, ":scene_to_use", "scn_meeting_scene_plain"),
				(try_end),
				(assign, reg0, ":scene_to_use"),
		])
		