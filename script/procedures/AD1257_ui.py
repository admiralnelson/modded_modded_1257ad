from header import *


		# script_set_town_picture
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
set_town_picture = (
	"set_town_picture",
			[

		(party_get_slot, ":culture", "$current_town", slot_center_culture),
			(try_begin), #WEST
			(this_or_next|eq, ":culture", fac_culture_finnish),
			(this_or_next|eq, ":culture", fac_culture_mazovian),
			(this_or_next|eq, ":culture", fac_culture_welsh),
			(this_or_next|eq, ":culture", fac_culture_iberian),
			(this_or_next|eq, ":culture", fac_culture_italian),
			(this_or_next|eq, ":culture", fac_culture_nordic),
			(this_or_next|eq, ":culture", fac_culture_gaelic),
			(this_or_next|eq, ":culture", fac_culture_anatolian_christian),
			(this_or_next|eq, ":culture", fac_culture_scotish),
			(eq, ":culture", fac_culture_western),
			(try_begin),
				(is_between, "$current_town", villages_begin, villages_end),
				(set_background_mesh, "mesh_pic_cataholic_village"),
			(else_try),
				(is_between, "$current_town", castles_begin, castles_end),
				(set_background_mesh, "mesh_pic_cataholic_castle"),
			(else_try),
				(set_background_mesh, "mesh_pic_cataholic_town"),
			(try_end),
		(else_try), #BALTIC  
			(this_or_next|eq, ":culture", fac_culture_baltic),
			(eq, ":culture", fac_culture_teutonic),
			(try_begin),
				(is_between, "$current_town", villages_begin, villages_end),
				(set_background_mesh, "mesh_pic_baltic_village"),
			(else_try),
				(is_between, "$current_town", castles_begin, castles_end),
				(set_background_mesh, "mesh_pic_baltic_castle"),
			(else_try),
				(set_background_mesh, "mesh_pic_baltic_town"),
			(try_end),
		(else_try), #ORTHODOX
			(this_or_next|eq, ":culture", fac_culture_serbian),
			(this_or_next|eq, ":culture", fac_culture_balkan),
			(this_or_next|eq, ":culture", fac_culture_rus),
			(this_or_next|eq, ":culture", fac_culture_byzantium),
			(eq, ":culture", fac_culture_mongol),
			(try_begin),
				(is_between, "$current_town", villages_begin, villages_end),
				(set_background_mesh, "mesh_pic_orthodox_village"),
			(else_try),
				(is_between, "$current_town", castles_begin, castles_end),
				(set_background_mesh, "mesh_pic_orthodox_castle"),
			(else_try),
				(set_background_mesh, "mesh_pic_orthodox_town"),
			(try_end),
		(else_try), #MUSLIM  
			(this_or_next|eq, ":culture", fac_culture_marinid),
			(this_or_next|eq, ":culture", fac_culture_mamluke),
			(this_or_next|eq, ":culture", fac_culture_andalus),
			(eq, ":culture", fac_culture_anatolian),
			(try_begin),
				(is_between, "$current_town", villages_begin, villages_end),
				(set_background_mesh, "mesh_pic_muslim_village"),
			(else_try),
				(is_between, "$current_town", castles_begin, castles_end),
				(set_background_mesh, "mesh_pic_muslim_castle"),
			(else_try),
				(set_background_mesh, "mesh_pic_muslim_town"),
			(try_end),
		(else_try),
			(try_begin),
				(is_between, "$current_town", villages_begin, villages_end),
				(set_background_mesh, "mesh_pic_cataholic_village"),
			(else_try),
				(is_between, "$current_town", castles_begin, castles_end),
				(set_background_mesh, "mesh_pic_cataholic_castle"),
			(else_try),
				(set_background_mesh, "mesh_pic_cataholic_town"),
			(try_end),
		(try_end),
		
		#####old
				# (try_begin),
					# (party_get_current_terrain, ":cur_terrain", "$current_town"),
					# (party_slot_eq,"$current_town",slot_party_type, spt_town),
					# (try_begin),
						# (this_or_next|eq, ":cur_terrain", rt_steppe),
						# (this_or_next|eq, ":cur_terrain", rt_steppe_forest),
						# (this_or_next|eq, ":cur_terrain", rt_desert),
						# (             eq, ":cur_terrain", rt_desert_forest),
						# (set_background_mesh, "mesh_pic_towndes"),
					# (else_try),
						# (this_or_next|eq, ":cur_terrain", rt_snow),
						# (             eq, ":cur_terrain", rt_snow_forest),
						# (set_background_mesh, "mesh_pic_townsnow"),
					# (else_try),
						# (set_background_mesh, "mesh_pic_town1"),
					# (try_end),
				# (else_try),
					# (try_begin),
						# (this_or_next|eq, ":cur_terrain", rt_steppe),
						# (this_or_next|eq, ":cur_terrain", rt_steppe_forest),
						# (this_or_next|eq, ":cur_terrain", rt_desert),
						# (             eq, ":cur_terrain", rt_desert_forest),
						# (set_background_mesh, "mesh_pic_castledes"),
					# (else_try),
						# (this_or_next|eq, ":cur_terrain", rt_snow),
						# (             eq, ":cur_terrain", rt_snow_forest),
						# (set_background_mesh, "mesh_pic_castlesnow"),
					# (else_try),
						# (set_background_mesh, "mesh_pic_castle1"),
					# (try_end),
				# (try_end),
		])

	# script_prsnt_lines
	# NOTE: draws a black line
	# INPUT	: size_x, size_y, pos_x, pos_y
	# OUTPUT : NONE
prsnt_lines =	(
	"prsnt_lines",
		[
		(store_script_param, ":size_x", 1),
		(store_script_param, ":size_y", 2),
		(store_script_param, ":pos_x", 3),
		(store_script_param, ":pos_y", 4),
		
		(create_mesh_overlay, reg1, "mesh_white_plane"),
		(val_mul, ":size_x", 50),
		(val_mul, ":size_y", 50),
		(position_set_x, pos1, ":size_x"),
		(position_set_y, pos1, ":size_y"),
		(overlay_set_size, reg1, pos1),
		(position_set_x, pos1, ":pos_x"),
		(position_set_y, pos1, ":pos_y"),
		(overlay_set_position, reg1, pos1),
		(overlay_set_color, reg1, 0x000000),
	])


		#script_prsnt_upgrade_tree_switch
		# WARNING: some part of this script are disabled.
		# INPUT: object, value
		# OUTPUT: NONE	
prsnt_upgrade_tree_switch =	(
		"prsnt_upgrade_tree_switch",
		[
			(store_trigger_param_1, ":object"),
			(store_trigger_param_2, ":value"),
			
			(try_begin),
			# (eq, ":object", "$g_presentation_obj_1"),
			# (store_sub, "$temp_2", 9, ":value"),
			# (store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_10"),
			# (start_presentation, ":cur_presentation"),
			# (else_try),
			(eq, ":object", "$g_presentation_obj_5"),
			(presentation_set_duration, 0),
			(try_end),
		])

		
		#script_prsnt_upgrade_tree_ready
		# WARNING: some part of this script are disabled.
		# INPUT: NONE
		# OUTPUT: NONE	
prsnt_upgrade_tree_ready =	(
		"prsnt_upgrade_tree_ready",
		[
			## next presentation
			(assign, "$g_presentation_next_presentation", -1),
			
			# (create_combo_button_overlay, "$g_presentation_obj_1"),
			# (position_set_x, pos1, 500),
			# (position_set_y, pos1, 680),
			# (overlay_set_position, "$g_presentation_obj_1", pos1),
			# # factions
			# (try_for_range_backwards, ":i_upgrade_tree", 0, 10),
			# (store_add, ":faction_no", ":i_upgrade_tree", "fac_kingdom_1"),
			# ## faction name
			# (try_begin),
			# (eq, ":faction_no", "fac_kingdoms_end"),
			# (str_store_string, s0, "@Mercenaries"),
			# (else_try),
			# (eq, ":faction_no", "fac_robber_knights"),
			# (str_store_string, s0, "@Outlaws"),
			# (else_try),
			# (eq, ":faction_no", "fac_khergits"),
			# (str_store_string, s0, "@Personal Guards"),
			# (else_try),
			# (eq, ":faction_no", "fac_manhunters"),
			# (str_store_string, s0, "@Others"),
			# (else_try),
			# (str_store_faction_name, s0, ":faction_no"),
			# (try_end),
			# (overlay_add_item, "$g_presentation_obj_1", s0),
			# (try_end),
			# (store_sub, ":presentation_obj_val", 9, "$temp_2"),
			# (overlay_set_val, "$g_presentation_obj_1", ":presentation_obj_val"),
			
			## back
			(create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
			(position_set_x, pos1, 900),
			(position_set_y, pos1, 25),
			(overlay_set_position, "$g_presentation_obj_5", pos1),
		])
		
		#script_prsnt_upgrade_tree_troop_and_name
		# INPUT: NONE
		# OUTPUT: NONE	
prsnt_upgrade_tree_troop_and_name =	(
		"prsnt_upgrade_tree_troop_and_name",
		[
			(store_script_param, ":slot_no", 1),
			(store_script_param, ":troop_no", 2),
			(store_script_param, ":pos_x", 3),
			(store_script_param, ":pos_y", 4),
			
			
			(str_store_troop_name, s1, ":troop_no"),
			(create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_vertical_align_center),
			(position_set_x, pos1, 800),
			(position_set_y, pos1, 800),
			(overlay_set_size, reg1, pos1),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			
			(val_sub, ":pos_x", 70),
			(val_add, ":pos_y", 5),
			(store_mul, ":cur_troop", ":troop_no", 2), #with weapons
			(create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
			#(position_set_x, pos1, 600),
			#(position_set_y, pos1, 600),
			(position_set_x, pos1, 450),
			(position_set_y, pos1, 450),
			
			(overlay_set_size, reg1, pos1),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
			(troop_set_slot, "trp_temp_array_b", ":slot_no", ":troop_no"),
			
		])
		
		#script_prsnt_upgrade_tree_troop_cost
		# INPUT: NONE
		# OUTPUT: NONE
prsnt_upgrade_tree_troop_cost =	(
		"prsnt_upgrade_tree_troop_cost",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			
			(call_script, "script_game_get_upgrade_cost", ":troop_no"),
			
			(create_text_overlay, reg1, "@{reg0}", tf_center_justify|tf_vertical_align_center),
			(position_set_x, pos1, 800),
			(position_set_y, pos1, 800),
			(overlay_set_size, reg1, pos1),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
		])
		
