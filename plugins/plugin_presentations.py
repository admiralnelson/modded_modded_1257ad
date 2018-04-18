from compiler import *
register_plugin()

ui_position = pos127


# Uncomment whatever meshes you actually need in your mod.

meshes = [

	# Backgrounds for entire presentations

	# core_ui_meshes.brf
	#("ui_bg_quests", 0, "quests_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Two vertical parts, left is a big black rectangle
	#("ui_bg_inventory_old", 0, "inventory_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Left and right panels plus equipment area
	#("ui_bg_dialog", 0, "conversation_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Smaller transparent area top-left, text area top-right, dialog options area bottom
	#("ui_bg_message", 0, "message_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # One big area, decorated left/right, lighter
	#("ui_bg_debrief", 0, "debrief_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # One big area, decorated left/right, darker
	#("ui_bg_meeting", 0, "meeting_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # One big area, lighter
	#("ui_bg_options_old", 0, "options_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # One big area, darker
	#("ui_bg_2a", 0, "bg2a", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Very dark reddish bg, large area top, narrow black bottom
	# user_interface_b.brf
	#("ui_bg_character", 0, "character_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Background for character window, with areas for portrait, attributes, skills, proficiencies etc
	#("ui_bg_facegen", 0, "face_gen_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Background for facegen, with transparent area for portrait
	#("ui_bg_inventory", 0, "inventory_window_b", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Background for inventory and equipment window
	#("ui_bg_party", 0, "party_window_b", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Background for party window, with central area for interface elements
	#("ui_bg_notes", 0, "note_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Parchment sheet on wooden boards, parchment split into two areas: wider left and narrower right
	#("ui_bg_game_logs", 0, "game_log_window", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Parchment sheet on wooden boards, single big area
	#("ui_bg_mp_host", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Parchment sheet, one big area, some area on top is left transparent
	#("ui_bg_mp_profile", 0, "mp_ui_profile", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Screen split into two areas, each has a header placeholder, nice borders
	#("ui_bg_mp_bg", 0, "mp_ui_bg", 0, 0, 0, 0, 0, 0, 1, 1, 1), # One big area, nice borders
	# user_interface_c.brf
	#("ui_bg_parchdoor", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Parchment w/o borders, weird door with staircase in bottom-center
	#("ui_bg_options", 0, "ui_options_bg", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Three areas, small top-right, small transparent bottom-right and big remaining, plain borders

	# Large panels

	# core_ui_meshes.brf
	#("ui_panel_facegen", 0, "facegen_board", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Half-screen area (0.5 * 0.7).
	# user_interface_b.brf
	#("ui_panel_mp_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1), # semi-transparent, (0,0.5),(0,0.59),(0,0)
	#("ui_panel_mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1), # semi-transparent, (0,0.786684),(0,0.59),(0,0)
	#("ui_panel_mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1), # semi-transparent, (0,0.393342),(0,0.59),(0,0)
	#("ui_panel_mp_inv_left", 0, "mp_inventory_left",  0, 0, 0, 0, 0, 0, 1, 1, 1), # transparent with 5 slots, (0,0.133),(0,0.90396),(0,0)
	#("ui_panel_mp_inv_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1), # transparent with 4 slots, (0,0.133),(0,0.77696),(0,0)
	#("ui_panel_mp_welcome", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1), # semi-transparent, (0,0.599999),(0,0.2),(0,0)
	#("ui_panel_mp_order", 0, "mp_ui_order_button", 0, 0, 0, 0, 0, 0, 1, 1, 1), # semi-transparent, (0,0.399982),(0,0.04),(0,0)
	# user_interface_c.brf
	#("ui_panel_quickbattle", 0, "ui_quick_battle_a", 0, 0, 0, 0, 0, 0, 1, 1, 1), # reddish, (0,0.35),(0,0.75),(0,0)
	#("ui_panel_title", 0, "cb_ui_title_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1), # white, (0,0.6),(0,0.1),(0,0)

	# Buttons

	# core_ui_meshes.brf
	#("ui_btn_dialog_u", 0, "dlg_button",      0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.009827,0.962631),(-0.007161,0.043302),(0,0)
	#("ui_btn_dialog_d", 0, "dlg_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_medium_u", 0, "medium_button",      0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.015689,0.285534),(-0.018568,0.079553),(0,0)
	#("ui_btn_medium_d", 0, "medium_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_short_u", 0, "short_button",      0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.014919,0.239568),(-0.019886,0.083876),(0,0)
	#("ui_btn_short_d", 0, "short_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_long_u", 0, "longer_button",      0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.011017,0.722294),(-0.015044,0.080305),(0,0)
	#("ui_btn_long_d", 0, "longer_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_party_u", 0, "party_button",      0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.009763,0.57704),(-0.009225,0.067976),(0,0)
	#("ui_btn_party_d", 0, "party_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_1_u", 0, "button1_up",   0, 0, 0, 0, 0, 0, 1, 1, 1), # (2e-06,0.074053),(1e-06,0.073358),(0,0)
	#("ui_btn_1_d", 0, "button1_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_1_h", 0, "button1_hl",   0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_2_u", 0, "button2_up",   0, 0, 0, 0, 0, 0, 1, 1, 1), # (2e-06,0.133476),(1e-06,0.073358),(0,0)
	#("ui_btn_2_d", 0, "button2_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_2_h", 0, "button2_hl",   0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_3_u", 0, "button3_up",   0, 0, 0, 0, 0, 0, 1, 1, 1), # (2e-06,0.193311),(1e-06,0.073358),(0,0)
	#("ui_btn_3_d", 0, "button3_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_3_h", 0, "button3_hl",   0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_4_u", 0, "button4_up",   0, 0, 0, 0, 0, 0, 1, 1, 1), # (2e-06,0.253934),(1e-06,0.073358),(0,0)
	#("ui_btn_4_d", 0, "button4_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_4_h", 0, "button4_hl",   0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_5_u", 0, "button5_up",   0, 0, 0, 0, 0, 0, 1, 1, 1), # (2e-06,0.310907),(1e-06,0.073358),(0,0)
	#("ui_btn_5_d", 0, "button5_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_5_h", 0, "button5_hl",   0, 0, 0, 0, 0, 0, 1, 1, 1),
	# user_interface_b.brf
	#("ui_btn_member_u", 0, "party_member_button",      0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.067433,0.533963),(-0.010751,0.058116),(0.000942,0.000942)
	#("ui_btn_member_d", 0, "party_member_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_loadgame_u", 0, "restore_game_panel",      0, 0, 0, 0, 0, 0, 1, 1, 1), # semi-transparent, (0,0.601396),(0,0.386578),(0.000942,0.000942)
	#("ui_btn_loadgame_d", 0, "restore_game_panel_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_drop_u", 0, "button_drop",         0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.017586,0.236414),(0,0.073),(0,0)
	#("ui_btn_drop_d", 0, "button_drop_clicked", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_drop_h", 0, "button_drop_hl",      0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_dropchild_u", 0, "button_drop_child",         0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.004735,0.221721),(0,0.058312),(0,0)
	#("ui_btn_dropchild_d", 0, "button_drop_child_clicked", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_dropchild_h", 0, "button_drop_child_hl",      0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_uparrow_u", 0, "small_arrow_up",         0, 0, 0, 0, 0, 0, 1, 1, 1), # (0,0.088293),(0,0.094),(0,0)
	#("ui_btn_uparrow_d", 0, "small_arrow_up_clicked", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_uparrow_h", 0, "small_arrow_up_hl",      0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_downarrow_u", 0, "small_arrow_down",         0, 0, 0, 0, 0, 0, 1, 1, 1), # (0,0.088293),(0,0.094),(0,0)
	#("ui_btn_downarrow_d", 0, "small_arrow_down_clicked", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_btn_downarrow_h", 0, "small_arrow_down_hl",      0, 0, 0, 0, 0, 0, 1, 1, 1),

	# Other interface elements and components of them

	# core_ui_meshes.brf
	#("ui_slider_panel",  0, "slider_hor", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.009398,0.260111),(0.002459,0.024835),(0,0)
	#("ui_slider_handle", 0, "handle_hor", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.010753,0.013258),(-0.007538,0.037135),(0,0)
	#("ui_scrollbar_panel",  0, "scrollbar",        0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.002323,0.025361),(-0.013153,0.651827),(0,0)
	#("ui_scrollbar_handle", 0, "scrollbar_handle", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (0.004206,0.01845),(-0.004966,0.312926),(0,0)
	#("ui_progressbar_panel",  0, "progressbar",        0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.013153,0.651827),(-0.000956,0.026729),(0,0)
	#("ui_progressbar_handle", 0, "progressbar_handle", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.006251,0.6433),(0.005296,0.01954),(0,0)
	#("ui_relationbar_panel",  0, "talk_relation_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (9.3e-05,0.190265),(3.3e-05,0.019447),(0,0)
	#("ui_relationbar_handle", 0, "talk_reln_pointer", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.011035,0.012976),(-0.007538,0.037135),(0,0)
	# user_interface_b.brf
	#("ui_status_player_panel", 0, "status_background_player", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (0,0.176193),(0,0.051532),(0.0002,0.0002)
	#("ui_status_horse_panel", 0, "status_background_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (0,0.173771),(0,0.051532),(0.0002,0.0002)
	#("ui_status_healthbar", 0, "status_health_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (0,0.103666),(0,0.004613),(0,0)
	#("ui_shield_100", 0, "status_shield_100", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (-0.018475,0.02292),(-0.025124,0.026726),(0.000236,0.000236)
	#("ui_shield_80",  0, "status_shield_80",  0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_shield_60",  0, "status_shield_60",  0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_shield_40",  0, "status_shield_40",  0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_shield_20",  0, "status_shield_20",  0, 0, 0, 0, 0, 0, 1, 1, 1),
	#("ui_checkbox_off", 0, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1), # (0,0.022162),(0,0.023176),(0,0)
	#("ui_checkbox_on",  0, "checkbox_on",  0, 0, 0, 0, 0, 0, 1, 1, 1),
	# other
	#("ui_gold_icon", 0, "mp_ico_gold", 0, 0, 0, 0, 0, 0, 1, 1, 1),

]


def ui_create_label(destination, text, x, y, alignment = 0, scale = None, rotation = None, *argl):
	result = [
		(create_text_overlay, destination, text, alignment),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
	]
	if scale is not None:
		result.extend([
			(position_set_x, ui_position, scale),
			(position_set_y, ui_position, scale),
			(overlay_set_size, destination, ui_position),
		])
	if rotation is not None:
		result.extend([
			(position_rotate_z, ui_position, rotation),
			(overlay_set_mesh_rotation, destination, ui_position),
		])
	return result

def ui_create_mesh(destination, mesh, x, y, scale_x = None, scale_y = None, *argl):
	result = [
		(create_mesh_overlay, destination, mesh),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
	]
	if scale_x is not None:
		result.append((position_set_x, ui_position, scale_x))
		if scale_y is None:
			result.append((position_set_y, ui_position, scale_x))
		else:
			result.append((position_set_y, ui_position, scale_y))
		result.append((overlay_set_size, destination, ui_position))
	return result

def ui_create_game_button(destination, caption, x, y, scale_x = None, scale_y = None, *argl):
	result = [
		(create_game_button_overlay, destination, caption),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
	]
	if scale_x is not None:
		result.append((position_set_x, ui_position, scale_x))
		if scale_y is None:
			result.append((position_set_y, ui_position, scale_x))
		else:
			result.append((position_set_y, ui_position, scale_y))
		result.append((overlay_set_size, destination, ui_position))
	return result

def ui_create_image_button(destination, mesh, mesh_pressed, x, y, scale_x = None, scale_y = None, *argl):
	result = [
		(create_image_button_overlay, destination, mesh, mesh_pressed),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
	]
	if scale_x is not None:
		result.append((position_set_x, ui_position, scale_x))
		if scale_y is None:
			result.append((position_set_y, ui_position, scale_x))
		else:
			result.append((position_set_y, ui_position, scale_y))
		result.append((overlay_set_size, destination, ui_position))
	return result

def ui_create_checkbox(destination, mesh_off, mesh_on, x, y, value = 0, scale = None, *argl):
	result = [
		(create_check_box_overlay, destination, mesh_off, mesh_on),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
		(overlay_set_val, destination, value),
	]
	if scale is not None:
		result.extend([
			(position_set_x, ui_position, scale),
			(position_set_y, ui_position, scale),
			(overlay_set_size, destination, ui_position),
		])
	return result

def ui_create_container(destination, x, y, width, height, *argl):
	result = [
		(create_text_overlay, destination, "str_empty_string", tf_scrollable),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
		(position_set_x, ui_position, width),
		(position_set_y, ui_position, height),
		(overlay_set_area_size, destination, ui_position),
	]
	return result

def ui_create_textbox(destination, x, y, scale_x = None, scale_y = None, *argl):
	result = [
		(create_simple_text_box_overlay, destination),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
	]
	if scale_x is not None:
		result.append((position_set_x, ui_position, scale_x))
		if scale_y is None:
			result.append((position_set_y, ui_position, scale_x))
		else:
			result.append((position_set_y, ui_position, scale_y))
		result.append((overlay_set_size, destination, ui_position))
	return result

def ui_create_combobox(destination, x, y, scale_x = None, scale_y = None, *argl):
	result = [
		(create_combo_button_overlay, destination),
		(init_position, ui_position),
		(position_set_x, ui_position, x),
		(position_set_y, ui_position, y),
		(overlay_set_position, destination, ui_position),
	]
	if scale_x is not None:
		result.append((position_set_x, ui_position, scale_x))
		if scale_y is None:
			result.append((position_set_y, ui_position, scale_x))
		else:
			result.append((position_set_y, ui_position, scale_y))
		result.append((overlay_set_size, destination, ui_position))
	result.extend([(overlay_add_item, destination, item) for item in argl])
	return result



extend_syntax(ui_create_label)        # (ui_create_label, <destination>, <string>, <x>, <y>, [<alignment>], [<scale>], [<rotation>]),
                                      # See header_presentations.py file for text alignment constants.
extend_syntax(ui_create_mesh)         # (ui_create_mesh, <destination>, <mesh>, <x>, <y>, [<scale_x>], [<scale_y>]),
                                      # If only <scale_x> is provided, it will be used for both dimensions.
extend_syntax(ui_create_game_button)  # (ui_create_game_button, <destination>, <string>, <x>, <y>, [<scale_x>], [<scale_y>]),
                                      # If only <scale_x> is provided, it will be used for both dimensions.
extend_syntax(ui_create_image_button) # (ui_create_image_button, <destination>, <mesh_base>, <mesh_clicked>, <x>, <y>, [<scale_x>], [<scale_y>]),
                                      # If only <scale_x> is provided, it will be used for both dimensions.
extend_syntax(ui_create_checkbox)     # (ui_create_checkbox, <destination>, <mesh_off_state>, <mesh_on_state>, <x>, <y>, [<start_value>], [<scale>]),
                                      # Typically "mesh_checkbox_off", "mesh_checkbox_on" are used as checkbox meshes. Checkbox is not checked by default.
extend_syntax(ui_create_container)    # (ui_create_container, <destination>, <x>, <y>, <width>, <height>),
                                      # Creates a scrollable area with specified dimensions.
extend_syntax(ui_create_textbox)      # (ui_create_textbox, <destination>, <x>, <y>, [<scale_x>], [<scale_y>]),
                                      # Normal empty textbox.
extend_syntax(ui_create_combobox)     # (ui_create_combobox, <destination>, <x>, <y>, [<scale_x>], [<scale_y>], [<list_item>,...]),
                                      # You can add any number of combobox items in this operation instead of using (overlay_add_item).
