from header import  *
#script_training_ground_sub_routine_2_for_melee_details
		# INPUT:
		# value
		#OUTPUT:
		# none
training_ground_sub_routine_2_for_melee_details = (
	"training_ground_sub_routine_2_for_melee_details",
			[
				(store_script_param, ":value", 1),
				(val_sub, ":value", 1),
				(try_begin),
					(lt, ":value", 0),
					(call_script, "script_remove_random_fit_party_member_from_stack_selection"),
				(else_try),
					(call_script, "script_remove_fit_party_member_from_stack_selection", ":value"),
				(try_end),
				(assign, ":troop_id", reg0),
				(store_sub, ":slot_index", "$temp_2", 1),
				(troop_set_slot, "trp_temp_array_a", ":slot_index", ":troop_id"),
				(try_begin),
					(eq, "$temp", "$temp_2"),
					(call_script, "script_start_training_at_training_ground", -1, "$temp"),
				(else_try),
					(val_add, "$temp_2", 1),
					(jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
				(try_end),
		])

		#script_start_training_at_training_ground
		# INPUT:
		# param1: training_weapon_type, param2: training_param
start_training_at_training_ground = (
	"start_training_at_training_ground",
			[
				(val_add, "$g_training_ground_training_count", 1),
				(store_script_param, ":mission_weapon_type", 1),
				(store_script_param, ":training_param", 2),
				
				(set_jump_mission, "mt_training_ground_training"),
				
				(assign, ":training_default_weapon_1", -1),
				(assign, ":training_default_weapon_2", -1),
				(assign, ":training_default_weapon_3", -1),
				(assign, "$scene_num_total_gourds_destroyed", 0),
				(try_begin),
					(eq, ":mission_weapon_type", itp_type_bow),
					(assign, "$g_training_ground_used_weapon_proficiency", wpt_archery),
					(assign, ":training_default_weapon_1", "itm_practice_bow"),
					(try_begin),
						(eq, "$g_mt_mode", ctm_mounted),
						(assign, ":training_default_weapon_2", "itm_practice_arrows_100_amount"),
					(else_try),
						(assign, ":training_default_weapon_2", "itm_practice_arrows_10_amount"),
					(try_end),
				(else_try),
					(eq, ":mission_weapon_type", itp_type_crossbow),
					(assign, "$g_training_ground_used_weapon_proficiency", wpt_crossbow),
					(assign, ":training_default_weapon_1", "itm_practice_crossbow"),
					(assign, ":training_default_weapon_2", "itm_practice_bolts_9_amount"),
				(else_try),
					(eq, ":mission_weapon_type", itp_type_thrown),
					(assign, "$g_training_ground_used_weapon_proficiency", wpt_throwing),
					(try_begin),
						(eq, "$g_mt_mode", ctm_mounted),
						(assign, ":training_default_weapon_2", "itm_practice_throwing_daggers_100_amount"),
					(else_try),
						(assign, ":training_default_weapon_2", "itm_practice_throwing_daggers"),
					(try_end),
				(else_try),
					(eq, ":mission_weapon_type", itp_type_one_handed_wpn),
					(assign, "$g_training_ground_used_weapon_proficiency", wpt_one_handed_weapon),
					(assign, ":training_default_weapon_1", "itm_practice_sword"),
				(else_try),
					(eq, ":mission_weapon_type", itp_type_polearm),
					(assign, "$g_training_ground_used_weapon_proficiency", wpt_polearm),
					(assign, ":training_default_weapon_1", "itm_practice_lance"),
				(else_try),
					#weapon_type comes as -1 when melee training is selected
					(assign, "$g_training_ground_used_weapon_proficiency", wpt_one_handed_weapon),
					(call_script, "script_get_random_melee_training_weapon"),
					(assign, ":training_default_weapon_1", reg0),
					(assign, ":training_default_weapon_2", reg1),
				(try_end),
				
				##     (assign, "$g_training_ground_training_troop_stack_index", ":stack_index"),
				(try_begin),
					(eq, "$g_mt_mode", ctm_mounted),
					(assign, ":training_default_weapon_3", "itm_practice_horse"),
					(store_add, "$g_training_ground_training_scene", "scn_training_ground_horse_track_1", "$g_encountered_party"),
					(val_sub, "$g_training_ground_training_scene", training_grounds_begin),
				(else_try),
					(store_add, "$g_training_ground_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
					(val_sub, "$g_training_ground_training_scene", training_grounds_begin),
				(try_end),
				
				(modify_visitors_at_site, "$g_training_ground_training_scene"),
				(reset_visitors),
				(set_visitor, 0, "trp_player"),
				
				(assign, ":selected_weapon", -1),
				(try_for_range, ":cur_slot", 0, 4),#equipment slots
					(troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
					(ge, ":cur_item", 0),
					(item_get_type, ":item_type", ":cur_item"),
					(try_begin),
						(eq, ":item_type", ":mission_weapon_type"),
						(eq, ":selected_weapon", -1),
						(assign, ":selected_weapon", ":cur_item"),
					(try_end),
				(try_end),
				(mission_tpl_entry_clear_override_items, "mt_training_ground_training", 0),
				(mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, "itm_practice_boots"),
				(try_begin),
					(ge, ":training_default_weapon_1", 0),
					(try_begin),
						(ge, ":selected_weapon", 0),
						(mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":selected_weapon"),
					(else_try),
						(mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_1"),
					(try_end),
				(try_end),
				(try_begin),
					(ge, ":training_default_weapon_2", 0),
					(mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_2"),
				(try_end),
				(try_begin),
					(ge, ":training_default_weapon_3", 0),
					(mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_3"),
				(try_end),
				
				(assign, ":cur_visitor_point", 5),
				(troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
				(store_add, ":end_cond", 5, ":num_fit"),
				(val_min, ":end_cond", 13),
				(try_for_range, ":cur_visitor_point", 5, ":end_cond"),
					(call_script, "script_remove_random_fit_party_member_from_stack_selection"),
					(set_visitor, ":cur_visitor_point", reg0),
					(val_add, ":cur_visitor_point", 1),
				(try_end),
				(try_begin),
					(eq, "$g_mt_mode", ctm_melee),
					(assign, ":total_difficulty", 0),
					(try_for_range, ":i", 0, ":training_param"),
						(troop_get_slot, ":cur_troop", "trp_temp_array_a", ":i"),
						(store_add, ":cur_entry_point", ":i", 1),
						(set_visitor, ":cur_entry_point", ":cur_troop"),
						#(mission_tpl_entry_clear_override_items, "mt_training_ground_training", ":cur_entry_point"),
						#(mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", "itm_practice_boots"),
						#(call_script, "script_get_random_melee_training_weapon"),
						#(mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", reg0),
						(try_begin),
							(ge, reg1, 0),
							#(mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", reg1),
						(try_end),
						(store_character_level, ":cur_troop_level", ":cur_troop"),
						(val_add, ":cur_troop_level", 10),
						(val_mul, ":cur_troop_level", ":cur_troop_level"),
						(val_add, ":total_difficulty", ":cur_troop_level"),
					(try_end),
					
					(assign, "$g_training_ground_training_num_enemies", ":training_param"),
					(assign, "$g_training_ground_training_hardness",  ":total_difficulty"),
					(store_add, ":number_multiplier", "$g_training_ground_training_num_enemies", 4),
					(val_mul, "$g_training_ground_training_hardness", ":number_multiplier"),
					(val_div, "$g_training_ground_training_hardness", 2400),
					(str_store_string, s0, "@Your opponents are ready for the fight."),
				(else_try),
					(eq, "$g_mt_mode", ctm_mounted),
					(try_begin),
						(eq, ":mission_weapon_type", itp_type_bow),
						(assign, "$g_training_ground_training_hardness", 350),
						(assign, "$g_training_ground_training_num_gourds_to_destroy", 30),
					(else_try),
						(eq, ":mission_weapon_type", itp_type_thrown),
						(assign, "$g_training_ground_training_hardness", 400),
						(assign, "$g_training_ground_training_num_gourds_to_destroy", 30),
					(else_try),
						(eq, ":mission_weapon_type", itp_type_one_handed_wpn),
						(assign, "$g_training_ground_training_hardness", 200),
						(assign, "$g_training_ground_training_num_gourds_to_destroy", 45),
					(else_try),
						(eq, ":mission_weapon_type", itp_type_polearm),
						(assign, "$g_training_ground_training_hardness", 280),
						(assign, "$g_training_ground_training_num_gourds_to_destroy", 35),
					(try_end),
					(str_store_string, s0, "@Try to destroy as many targets as you can. You have two and a half minutes to clear the track."),
				(else_try),
					(eq, "$g_mt_mode", ctm_ranged),
					(store_mul, "$g_training_ground_ranged_distance", ":training_param", 100),
					(assign, ":hardness_modifier", ":training_param"),
					(val_mul, ":hardness_modifier", ":hardness_modifier"),
					(try_begin),
						(eq, ":mission_weapon_type", itp_type_bow),
						(val_mul, ":hardness_modifier", 3),
						(val_div, ":hardness_modifier", 2),
					(else_try),
						(eq, ":mission_weapon_type", itp_type_thrown),
						(val_mul, ":hardness_modifier", 5),
						(val_div, ":hardness_modifier", 2),
						(val_mul, ":hardness_modifier", ":training_param"),
						(val_div, ":hardness_modifier", 2),
					(try_end),
					(store_mul, "$g_training_ground_training_hardness", 100, ":hardness_modifier"),
					(val_div, "$g_training_ground_training_hardness", 6000),
					(str_store_string, s0, "@Stay behind the line on the ground and shoot the targets. Try not to waste any shots."),
				(try_end),
				(jump_to_menu, "mnu_training_ground_description"),
		])
		