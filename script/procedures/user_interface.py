from header import *


		#script_game_context_menu_get_buttons:
		# This script is called from the game engine when the player clicks the right mouse button over a party on the map.
		# INPUT: arg1 = party_no
		# OUTPUT: none, fills the menu buttons
game_context_menu_get_buttons =	(
	"game_context_menu_get_buttons",
			[
				(store_script_param, ":party_no", 1),
				(try_begin),
					(neq, ":party_no", "p_main_party"),
					(context_menu_add_item, "@Move here", cmenu_move),
				(try_end),
				
				(try_begin),
					(is_between, ":party_no", centers_begin, centers_end),
					(context_menu_add_item, "@View notes", 1),
				(else_try),
					(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
					(gt, ":num_stacks", 0),
					(party_stack_get_troop_id, ":troop_no", ":party_no", 0),
					(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
					(context_menu_add_item, "@View notes", 2),
				(try_end),
				
				(try_begin),
					(neq, ":party_no", "p_main_party"),
					(store_faction_of_party, ":party_faction", ":party_no"),
					
					(store_relation, ":rel", ":party_faction", "fac_player_supporters_faction"),
					(this_or_next | ge, ":rel", 0),
					# rafi - accompany whoever I wish (this_or_next|eq, ":party_faction", "$players_kingdom"),
					# rafi - accompany whoever I wish (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
					(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
					
					(neg|is_between, ":party_no", centers_begin, centers_end),
					
					(context_menu_add_item, "@Accompany", cmenu_follow),
				(try_end),
		])
		
		#script_game_event_context_menu_button_clicked:
		# This script is called from the game engine when the player clicks on a button at the right mouse menu.
		# INPUT: arg1 = party_no, arg2 = button_value
		# OUTPUT: none
game_event_context_menu_button_clicked = (
	"game_event_context_menu_button_clicked",
			[(store_script_param, ":party_no", 1),
				(store_script_param, ":button_value", 2),
				(try_begin),
					(eq, ":button_value", 1),
					(change_screen_notes, 3, ":party_no"),
				(else_try),
					(eq, ":button_value", 2),
					(party_stack_get_troop_id, ":troop_no", ":party_no", 0),
					(change_screen_notes, 1, ":troop_no"),
				(try_end),
		])


		# script_add_notification_menu
		# Input: arg1 = menu_no, arg2 = menu_var_1, arg3 = menu_var_2
		# Output: none
add_notification_menu = (
	"add_notification_menu",
			[
				(try_begin),
					(eq, "$g_infinite_camping", 0),
					(store_script_param, ":menu_no", 1),
					(store_script_param, ":menu_var_1", 2),
					(store_script_param, ":menu_var_2", 3),
					(assign, ":end_cond", 1),
					(try_for_range, ":cur_slot", 0, ":end_cond"),
						(try_begin),
							(troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
							(val_add, ":end_cond", 1),
						(else_try),
							(troop_set_slot, "trp_notification_menu_types", ":cur_slot", ":menu_no"),
							(troop_set_slot, "trp_notification_menu_var1", ":cur_slot", ":menu_var_1"),
							(troop_set_slot, "trp_notification_menu_var2", ":cur_slot", ":menu_var_2"),
						(try_end),
					(try_end),
				(try_end),
		])
		
		
		#script_add_troop_to_cur_tableau
		# INPUT: troop_no
		# OUTPUT: none
add_troop_to_cur_tableau = (
	"add_troop_to_cur_tableau",
			[
				(store_script_param, ":troop_no",1),
				
				(set_fixed_point_multiplier, 100),
				(assign, ":banner_mesh", -1),
				(troop_get_slot, ":banner_spr", ":troop_no", slot_troop_banner_scene_prop),
				(store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
				(try_begin),
					(is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
					(val_sub, ":banner_spr", banner_scene_props_begin),
					(store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
				(try_end),
				
				(cur_tableau_clear_override_items),
				
				#       (cur_tableau_set_override_flags, af_override_fullhelm),
				(cur_tableau_set_override_flags, af_override_head|af_override_weapons),
				
				(init_position, pos2),
				(cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
				
				(init_position, pos5),
				(assign, ":eye_height", 162),
				(store_mul, ":camera_distance", ":troop_no", 87323),
				#       (val_mod, ":camera_distance", 5),
				(assign, ":camera_distance", 139),
				(store_mul, ":camera_yaw", ":troop_no", 124337),
				(val_mod, ":camera_yaw", 50),
				(val_add, ":camera_yaw", -25),
				(store_mul, ":camera_pitch", ":troop_no", 98123),
				(val_mod, ":camera_pitch", 20),
				(val_add, ":camera_pitch", -14),
				(assign, ":animation", "anim_stand_man"),
				
				##       (troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
				##       (try_begin),
				##         (gt, ":horse_item", 0),
				##         (assign, ":eye_height", 210),
				##         (cur_tableau_add_horse, ":horse_item", pos2, anim_horse_stand, 0),
				##         (assign, ":animation", anim_ride_0),
				##         (position_set_z, pos5, 125),
				##         (try_begin),
				##           (is_between, ":camera_yaw", -10, 10), #make sure horse head doesn't obstruct face.
				##           (val_min, ":camera_pitch", -5),
				##         (try_end),
				##       (try_end),
				(position_set_z, pos5, ":eye_height"),
				
				# camera looks towards -z axis
				(position_rotate_x, pos5, -90),
				(position_rotate_z, pos5, 180),
				
				# now apply yaw and pitch
				(position_rotate_y, pos5, ":camera_yaw"),
				(position_rotate_x, pos5, ":camera_pitch"),
				(position_move_z, pos5, ":camera_distance", 0),
				(position_move_x, pos5, 5, 0),
				
				(try_begin),
					(ge, ":banner_mesh", 0),
					
					(init_position, pos1),
					(position_set_z, pos1, -1500),
					(position_set_x, pos1, 265),
					(position_set_y, pos1, 400),
					(position_transform_position_to_parent, pos3, pos5, pos1),
					(cur_tableau_add_mesh, ":banner_mesh", pos3, 400, 0),
				(try_end),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation" , 0),
				
				(cur_tableau_set_camera_position, pos5),
				
				(copy_position, pos8, pos5),
				(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
				(position_rotate_z, pos8, 30),
				(position_rotate_x, pos8, -60),
				(cur_tableau_add_sun_light, pos8, 175,150,125),
		])
		

		#script_add_troop_to_cur_tableau_for_character
		# INPUT: troop_no
		# OUTPUT: none
add_troop_to_cur_tableau_for_character = (
	"add_troop_to_cur_tableau_for_character",
			[
				(store_script_param, ":troop_no",1),
				
				(set_fixed_point_multiplier, 100),
				
				(cur_tableau_clear_override_items),
				(cur_tableau_set_override_flags, af_override_fullhelm),
				##       (cur_tableau_set_override_flags, af_override_head|af_override_weapons),
				
				(init_position, pos2),
				(cur_tableau_set_camera_parameters, 1, 4, 8, 10, 10000),
				
				(init_position, pos5),
				(assign, ":cam_height", 150),
				#       (val_mod, ":camera_distance", 5),
				(assign, ":camera_distance", 360),
				(assign, ":camera_yaw", -15),
				(assign, ":camera_pitch", -18),
				(assign, ":animation", anim_stand_man),
				
				(position_set_z, pos5, ":cam_height"),
				
				# camera looks towards -z axis
				(position_rotate_x, pos5, -90),
				(position_rotate_z, pos5, 180),
				
				# now apply yaw and pitch
				(position_rotate_y, pos5, ":camera_yaw"),
				(position_rotate_x, pos5, ":camera_pitch"),
				(position_move_z, pos5, ":camera_distance", 0),
				(position_move_x, pos5, 5, 0),
				
				(try_begin),
					(troop_is_hero, ":troop_no"),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
				(else_try),
					(store_mul, ":random_seed", ":troop_no", 126233),
					(val_mod, ":random_seed", 1000),
					(val_add, ":random_seed", 1),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
				(try_end),
				(cur_tableau_set_camera_position, pos5),
				
				(copy_position, pos8, pos5),
				(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
				(position_rotate_z, pos8, 30),
				(position_rotate_x, pos8, -60),
				(cur_tableau_add_sun_light, pos8, 175,150,125),
		])


		#script_add_troop_to_cur_tableau_for_inventory
		# INPUT: troop_no
		# OUTPUT: none
add_troop_to_cur_tableau_for_inventory = (
	"add_troop_to_cur_tableau_for_inventory",
			[
				(store_script_param, ":troop_no",1),
				(store_mod, ":side", ":troop_no", 4), #side flag is inside troop_no value
				(val_div, ":troop_no", 4), #removing the flag bit
				(val_mul, ":side", 90), #to degrees
				
				(set_fixed_point_multiplier, 100),
				
				(cur_tableau_clear_override_items),
				
				(init_position, pos2),
				(position_rotate_z, pos2, ":side"),
				(cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),
				
				(init_position, pos5),
				(assign, ":cam_height", 105),
				#       (val_mod, ":camera_distance", 5),
				(assign, ":camera_distance", 380),
				(assign, ":camera_yaw", -15),
				(assign, ":camera_pitch", -18),
				(assign, ":animation", anim_stand_man),
				
				(position_set_z, pos5, ":cam_height"),
				
				# camera looks towards -z axis
				(position_rotate_x, pos5, -90),
				(position_rotate_z, pos5, 180),
				
				# now apply yaw and pitch
				(position_rotate_y, pos5, ":camera_yaw"),
				(position_rotate_x, pos5, ":camera_pitch"),
				(position_move_z, pos5, ":camera_distance", 0),
				(position_move_x, pos5, 5, 0),
				
				(try_begin),
					(troop_is_hero, ":troop_no"),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
				(else_try),
					(store_mul, ":random_seed", ":troop_no", 126233),
					(val_mod, ":random_seed", 1000),
					(val_add, ":random_seed", 1),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
				(try_end),
				(cur_tableau_set_camera_position, pos5),
				
				(copy_position, pos8, pos5),
				(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
				(position_rotate_z, pos8, 30),
				(position_rotate_x, pos8, -60),
				(cur_tableau_add_sun_light, pos8, 175,150,125),
		])
		
		#script_add_troop_to_cur_tableau_for_profile
		# INPUT: troop_no
		# OUTPUT: none
add_troop_to_cur_tableau_for_profile = (
	"add_troop_to_cur_tableau_for_profile",
			[
				(store_script_param, ":troop_no",1),
				
				(set_fixed_point_multiplier, 100),
				
				(cur_tableau_clear_override_items),
				
				(cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),
				
				(init_position, pos5),
				(assign, ":cam_height", 105),
				#       (val_mod, ":camera_distance", 5),
				(assign, ":camera_distance", 380),
				(assign, ":camera_yaw", -15),
				(assign, ":camera_pitch", -18),
				(assign, ":animation", anim_stand_man),
				
				(position_set_z, pos5, ":cam_height"),
				
				# camera looks towards -z axis
				(position_rotate_x, pos5, -90),
				(position_rotate_z, pos5, 180),
				
				# now apply yaw and pitch
				(position_rotate_y, pos5, ":camera_yaw"),
				(position_rotate_x, pos5, ":camera_pitch"),
				(position_move_z, pos5, ":camera_distance", 0),
				(position_move_x, pos5, 5, 0),
				
				(profile_get_banner_id, ":profile_banner"),
				(try_begin),
					(ge, ":profile_banner", 0),
					(init_position, pos2),
					(val_add, ":profile_banner", banner_meshes_begin),
					(position_set_x, pos2, -175),
					(position_set_y, pos2, -300),
					(position_set_z, pos2, 180),
					(position_rotate_x, pos2, 90),
					(position_rotate_y, pos2, -15),
					(cur_tableau_add_mesh, ":profile_banner", pos2, 0, 0),
				(try_end),
				
				(init_position, pos2),
				(try_begin),
					(troop_is_hero, ":troop_no"),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
				(else_try),
					(store_mul, ":random_seed", ":troop_no", 126233),
					(val_mod, ":random_seed", 1000),
					(val_add, ":random_seed", 1),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
				(try_end),
				(cur_tableau_set_camera_position, pos5),
				
				(copy_position, pos8, pos5),
				(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
				(position_rotate_z, pos8, 30),
				(position_rotate_x, pos8, -60),
				(cur_tableau_add_sun_light, pos8, 175,150,125),
		])
		
		#script_add_troop_to_cur_tableau_for_retirement
		# INPUT: type
		# OUTPUT: none
add_troop_to_cur_tableau_for_retirement = (
	"add_troop_to_cur_tableau_for_retirement", [
				(store_script_param, ":type", 1),
				(cur_tableau_set_override_flags, af_override_everything),
				
				(try_begin),
					(eq, ":type", 0),
					(cur_tableau_add_override_item, "itm_pilgrim_hood"),
					(cur_tableau_add_override_item, "itm_pilgrim_disguise"),
					(cur_tableau_add_override_item, "itm_wrapping_boots"),
					(assign, ":animation", "anim_pose_1"),
				(else_try),
					(eq, ":type", 1),
					(cur_tableau_add_override_item, "itm_pilgrim_hood"),
					#(cur_tableau_add_override_item, "itm_red_tunic"),
					(cur_tableau_add_override_item, "itm_wrapping_boots"),
					(cur_tableau_add_override_item, "itm_dagger"),
					(assign, ":animation", "anim_pose_1"),
				(else_try),
					(eq, ":type", 2),
					(cur_tableau_add_override_item, "itm_linen_tunic"),
					(cur_tableau_add_override_item, "itm_wrapping_boots"),
					(assign, ":animation", "anim_pose_2"),
				(else_try),
					(eq, ":type", 3),
					(cur_tableau_add_override_item, "itm_nomad_vest"),
					(cur_tableau_add_override_item, "itm_nomad_boots"),
					(assign, ":animation", "anim_pose_2"),
				(else_try),
					(eq, ":type", 4),
					(cur_tableau_add_override_item, "itm_tunic_with_green_cape"),
					(cur_tableau_add_override_item, "itm_leather_boots"),
					(assign, ":animation", "anim_pose_3"),
				(else_try),
					(eq, ":type", 5),
					(cur_tableau_add_override_item, "itm_red_shirt"),
					(cur_tableau_add_override_item, "itm_woolen_hose"),
					(cur_tableau_add_override_item, "itm_fur_hat"),
					(assign, ":animation", "anim_pose_3"),
				(else_try),
					(eq, ":type", 6),
					(cur_tableau_add_override_item, "itm_gambeson_a"),
					(cur_tableau_add_override_item, "itm_leather_boots"),
					(cur_tableau_add_override_item, "itm_sword_type_xiiib"),
					(assign, ":animation", "anim_pose_4"),
				(else_try),
					(eq, ":type", 7),
					(cur_tableau_add_override_item, "itm_merchant_outfit"),
					(cur_tableau_add_override_item, "itm_blue_hose"),
					(cur_tableau_add_override_item, "itm_sword_type_xiiib"),
					(assign, ":animation", "anim_pose_4"),
				(else_try),
					(eq, ":type", 8),
					(cur_tableau_add_override_item, "itm_merchant_outfit"),
					(cur_tableau_add_override_item, "itm_woolen_hose"),
					(cur_tableau_add_override_item, "itm_sword_type_xiiib"),
					(assign, ":animation", "anim_pose_4"),
				(else_try),
					##      (eq, ":type", 9),
					(cur_tableau_add_override_item, "itm_heraldic_mail_with_surcoat_for_tableau"),
					#(cur_tableau_add_override_item, "itm_mail_boots_for_tableau"),
					(cur_tableau_add_override_item, "itm_mail_boots"),
					(cur_tableau_add_override_item, "itm_sword_type_xiiib"),
					(assign, ":animation", "anim_pose_5"),
					##    (else_try), #not used
					##      (cur_tableau_add_override_item, "itm_heraldic_mail_with_tabard"),
					##      (cur_tableau_add_override_item, "itm_iron_greaves"),
					##      (cur_tableau_add_override_item, "itm_sword_type_xiiib"),
					##      (assign, ":animation", "anim_pose_5"),
				(try_end),
				
				##    (set_fixed_point_multiplier, 100),
				##    (cur_tableau_set_background_color, 0x00000000),
				##    (cur_tableau_set_ambient_light, 10,11,15),
				
				##     (init_position, pos8),
				##     (position_set_x, pos8, -210),
				##     (position_set_y, pos8, 200),
				##     (position_set_z, pos8, 300),
				##     (cur_tableau_add_point_light, pos8, 550,500,450),
				
				
				(set_fixed_point_multiplier, 100),
				(cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
				(assign, ":cam_height", 155),
				(assign, ":camera_distance", 575),
				(assign, ":camera_yaw", -5),
				(assign, ":camera_pitch", 10),
				
				(init_position, pos5),
				(position_set_z, pos5, ":cam_height"),
				# camera looks towards -z axis
				(position_rotate_x, pos5, -90),
				(position_rotate_z, pos5, 180),
				# now apply yaw and pitch
				(position_rotate_y, pos5, ":camera_yaw"),
				(position_rotate_x, pos5, ":camera_pitch"),
				(position_move_z, pos5, ":camera_distance", 0),
				(position_move_x, pos5, 60, 0),
				
				(init_position, pos2),
				(cur_tableau_add_troop, "trp_player", pos2, ":animation", 0),
				(cur_tableau_set_camera_position, pos5),
				
				(copy_position, pos8, pos5),
				(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
				(position_rotate_z, pos8, 30),
				(position_rotate_x, pos8, -60),
				(cur_tableau_add_sun_light, pos8, 175,150,125),
		])
		
		#script_add_troop_to_cur_tableau_for_party
		# INPUT: troop_no
		# OUTPUT: none
add_troop_to_cur_tableau_for_party = (
	"add_troop_to_cur_tableau_for_party",
			[
				(store_script_param, ":troop_no",1),
				(store_mod, ":hide_weapons", ":troop_no", 2), #hide_weapons flag is inside troop_no value
				(val_div, ":troop_no", 2), #removing the flag bit
				
				(set_fixed_point_multiplier, 100),
				
				(cur_tableau_clear_override_items),
				(try_begin),
					(eq, ":hide_weapons", 1),
					(cur_tableau_set_override_flags, af_override_fullhelm|af_override_head|af_override_weapons),
				(try_end),
				
				(init_position, pos2),
				(cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
				
				(init_position, pos5),
				(assign, ":cam_height", 105),
				#       (val_mod, ":camera_distance", 5),
				(assign, ":camera_distance", 450),
				(assign, ":camera_yaw", 15),
				(assign, ":camera_pitch", -18),
				(assign, ":animation", anim_stand_man),
				
				(troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
				(try_begin),
					(gt, ":horse_item", 0),
					(eq, ":hide_weapons", 0),
					(cur_tableau_add_horse, ":horse_item", pos2, "anim_horse_stand", 0),
					(assign, ":animation", "anim_ride_0"),
					(assign, ":camera_yaw", 23),
					(assign, ":cam_height", 150),
					(assign, ":camera_distance", 550),
				(try_end),
				(position_set_z, pos5, ":cam_height"),
				
				# camera looks towards -z axis
				(position_rotate_x, pos5, -90),
				(position_rotate_z, pos5, 180),
				
				# now apply yaw and pitch
				(position_rotate_y, pos5, ":camera_yaw"),
				(position_rotate_x, pos5, ":camera_pitch"),
				(position_move_z, pos5, ":camera_distance", 0),
				(position_move_x, pos5, 5, 0),
				
				(try_begin),
					(troop_is_hero, ":troop_no"),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
				(else_try),
					(store_mul, ":random_seed", ":troop_no", 126233),
					(val_mod, ":random_seed", 1000),
					(val_add, ":random_seed", 1),
					(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
				(try_end),
				(cur_tableau_set_camera_position, pos5),
				
				(copy_position, pos8, pos5),
				(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
				(position_rotate_z, pos8, 30),
				(position_rotate_x, pos8, -60),
				(cur_tableau_add_sun_light, pos8, 175,150,125),
		])
		