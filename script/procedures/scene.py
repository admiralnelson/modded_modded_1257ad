from header import *
		# script_setup_random_scene
		# used to generate battle scene! interesting stuffs
		# WARNING : HEAVILY modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = mission_template_no
		# Output: none
setup_random_scene=(
	"setup_random_scene",
			[
				(party_get_current_terrain, ":terrain_type", "p_main_party"),
				(assign, ":scene_to_use", "scn_random_scene"),
				
				(call_script, "script_get_closest_center", "p_main_party"),
				(party_get_slot, ":faction_no", reg0, slot_center_original_faction), #TOM Othr put this here?
				
				(try_begin),
					(eq, ":terrain_type", rt_steppe),
					(assign, ":scene_to_use", "scn_random_scene_steppe"),
				(else_try),
					(eq, ":terrain_type", rt_plain),
					(assign, ":scene_to_use", "scn_random_scene_plain"),
				(else_try),
					(eq, ":terrain_type", rt_snow),
					(assign, ":scene_to_use", "scn_random_scene_snow"),
				(else_try),
					(eq, ":terrain_type", rt_desert),
					(assign, ":scene_to_use", "scn_random_scene_desert"),
				(else_try),
					(eq, ":terrain_type", rt_steppe_forest),
					(assign, ":scene_to_use", "scn_random_scene_steppe_forest"),
				(else_try),
					(eq, ":terrain_type", rt_forest),
					(assign, ":scene_to_use", "scn_random_scene_plain_forest"),
				(else_try),
					(eq, ":terrain_type", rt_snow_forest),
					(assign, ":scene_to_use", "scn_random_scene_snow_forest"),
				(else_try),
					(eq, ":terrain_type", rt_desert_forest),
					(assign, ":scene_to_use", "scn_random_scene_desert_forest"),
				(else_try),
					(eq, ":terrain_type", rt_water),
					(assign, ":scene_to_use", "scn_water"),
				(else_try),
					(eq, ":terrain_type", rt_bridge),
					(assign, ":scene_to_use", "scn_scene_sea"),
					#tom
					# (else_try),
					
					# (eq, ":terrain_type", rt_mountain),
					# (assign, "$tom_generate_iberian", 1),
					# (assign, ":scene_to_use", "scn_1257_combat_iberian_hillside_0"),
				(try_end),
				
				#TOM
				
				
				(try_begin),
					(assign, "$tom_generate_swamp", 0),
					(assign, "$tom_generate_desert", 0),
					(assign, "$tom_generate_desertv2", 0),
					(assign, "$tom_generate_desertv3", 0),
					(assign, "$tom_generate_iberian", 0),
					(assign, "$tom_generate_iberian2", 0),
					(assign, "$tom_generate_snow", 0),
					#(assign, "$tom_generate_euro_forest", 0),
					(eq, "$tom_use_battlefields", 1),
					(try_begin), #extra check for custom field
						(eq, ":terrain_type", rt_forest),
						(store_random_in_range, ":random", 0, 101),
						(ge, ":random", 60),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_swamp_0", "scn_1257_combat_rocky_desert_0"),
						(assign, "$tom_generate_swamp", 1),
						#resourcehungry forests
						# (else_try),
						# (eq, ":terrain_type", rt_forest),
						# (lt, ":random", 40),
						# (assign, ":scene_to_use", "scn_1257_combat_forest_0"),
						# (store_random_in_range, ":random", 1, 3),
						# (assign, "$tom_generate_euro_forest", ":random"),
					(try_end),
					
			(try_begin),
				(eq, ":terrain_type", rt_snow),
			
			(store_random_in_range, ":random", 0, 101),
						(ge, ":random", 20),
			
			(assign, "$tom_generate_snow", 1),
			(store_random_in_range, ":scene_to_use", "scn_1257_combat_snow_0", "scn_manor"),
			(try_end),
			
			(try_begin),
				(eq, ":terrain_type", rt_snow_forest),
			
			(store_random_in_range, ":random", 0, 101),
						(ge, ":random", 20),
			
			(assign, "$tom_generate_snow", 2),
			(store_random_in_range, ":scene_to_use", "scn_1257_combat_snow_0", "scn_manor"),
			(try_end),
			
					(try_begin), #extra check for custom field
						(eq, ":terrain_type", rt_plain),
						(store_random_in_range, ":random", 0, 101),
						(ge, ":random", 80),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_euro_0", "scn_1257_combat_iberian_hillside_0"),
						#(assign, "$tom_generate_swamp", 1),
					(try_end),
					
					(try_begin),
						(this_or_next|eq, ":terrain_type", rt_desert),
						(eq, ":terrain_type", rt_desert_forest),
						(store_random_in_range, ":random", 0, 101),
						(try_begin),
							(ge, ":random", 80),
							(assign, "$tom_generate_desert", 1),
							(assign, ":scene_to_use", "scn_1257_combat_rocky_desert_0"),
						(else_try),
							(ge, ":random", 30),
							(assign, "$tom_generate_desertv2", 1),
							(assign, ":scene_to_use", "scn_1257_combat_rocky_desert_0"),
						(try_end),
					(try_end),
					
					(try_begin),
						(this_or_next|eq, ":terrain_type", rt_steppe_forest),
						(eq, ":terrain_type", rt_steppe),
						(try_begin),
							#is this in ukraine? if so its steppe
							(this_or_next | eq, ":faction_no", "fac_kingdom_3"),
							(this_or_next | eq, ":faction_no", "fac_kingdom_5"),
							(eq, ":faction_no", "fac_kingdom_15"),
							(store_random_in_range, ":scene_to_use", "scn_1257_combat_steppe_0", "scn_1257_combat_euro_0"),
						(else_try), #forest?
							(eq, ":terrain_type", rt_steppe_forest),
							(assign, "$tom_generate_iberian2", 1),
							(assign, ":scene_to_use", "scn_1257_combat_iberian_0"),
						(else_try),  #id not its mediterranian
							(assign, "$tom_generate_iberian", 1),
							(assign, ":scene_to_use", "scn_1257_combat_iberian_0"),
						(try_end),
					(try_end),
					
					# (try_begin), #scotland mountains!
					# (eq, ":terrain_type", rt_snow),
					# (eq, ":faction_no", "fac_kingdom_12"),
					# (assign, "$tom_generate_euro_hillside", 1),
					# (store_random_in_range, ":scene_to_use", "scn_1257_combat_euro_hillside_0", "scn_1257_combat_euro_hillside_4"),
					# (try_end),
					
					#mountain and hillside placement
					(set_fixed_point_multiplier, 100),
					(party_get_position, pos15, "p_main_party"),
					
					(position_get_x, ":x", pos15),
					(position_get_y, ":y", pos15),
					
					# (assign, reg10, ":x"),
					# (assign, reg11, ":y"),
					# (display_message, "@position x:{reg10}, y:{reg11}"),
					(try_begin), #nile 
				(assign, ":continue", 0),
			(try_begin),
					(lt, ":x", 18036),
							(lt, ":y", -20834),
							(gt, ":x", 15890),
							(gt, ":y", -25502),
				(assign, ":continue", 1),
			(else_try),
				(lt, ":x", 22720),
							(lt, ":y", -18627),
							(gt, ":x", 21597),
							(gt, ":y", -20013),
				(assign, ":continue", 1),
			(try_end),
			(eq, ":continue", 1),
				(store_random_in_range, ":scene_to_use", "scn_sitd_battle_nile_1", "scn_1257_combat_snow_0"),
				(assign, "$tom_generate_desertv3", 1),
			(else_try), #scotland
						(lt, ":x", -18195),
						(lt, ":y", 13475),
						(gt, ":x", -19389),
						(gt, ":y", 10326),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_euro_hillside_0", "scn_1257_combat_euro_hillside_4"),
						(assign, "$tom_generate_euro_hillside", 1),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
					(else_try),#turkey east of anitoch
						(lt, ":x", 21714),
						(lt, ":y", -13331),
						(gt, ":x", 14265),
						(gt, ":y", -14667),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_mountain_0", "scn_1257_combat_river_0"),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
					(else_try),#greece - turkey
						(lt, ":x", 27256),
						(lt, ":y", -7255),
						(gt, ":x", 4818),
						(gt, ":y", -14562),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
							(assign, "$tom_generate_iberian", 0),
							(assign, "$tom_generate_swamp", 0),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
							(assign, "$tom_generate_iberian2", 0),
							(assign, "$tom_generate_swamp", 0),
						(try_end),
					(else_try),#alps hillpoint
						(lt, ":x", -1149),
						(lt, ":y", -2543),
						(gt, ":x", -5458),
						(gt, ":y", -5934),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
							(assign, "$tom_generate_iberian", 0),
							(assign, "$tom_generate_swamp", 0),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
							(assign, "$tom_generate_iberian2", 0),
							(assign, "$tom_generate_swamp", 0),
						(try_end),
					(else_try),#alps
						(lt, ":x", 1953),
						(lt, ":y", 405),
						(gt, ":x", -8779),
						(gt, ":y", -6290),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_mountain_0", "scn_1257_combat_river_0"),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
						#(display_message, "@ALPS!"),
					(else_try), #alps 2
						(lt, ":x", -9696),
						(lt, ":y", -2732),
						(gt, ":x", -11853),
						(gt, ":y", -4263),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_mountain_0", "scn_1257_combat_river_0"),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
						#(display_message, "@ALPS2!"),
					(else_try), #frence-spain mountain
						(lt, ":x", -11549),
						(lt, ":y", -5660),
						(gt, ":x", -16034),
						(gt, ":y", -6883),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_mountain_0", "scn_1257_combat_river_0"),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
						#(display_message, "@France-spain!"),
					(else_try), #hungary 1
						(lt, ":x", 10894),
						(lt, ":y", 2023),
						(gt, ":x", 4719),
						(gt, ":y", 450),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_mountain_0", "scn_1257_combat_river_0"),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
						#(display_message, "@HUN1!"),
					(else_try), #hungary 2
						(lt, ":x", 11784),
						(lt, ":y", 253),
						(gt, ":x", 8089),
						(gt, ":y", -3882),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_mountain_3", "scn_1257_combat_mountain_4"),
						(assign, "$tom_generate_iberian2", 0),
						(assign, "$tom_generate_iberian", 0),
						(assign, "$tom_generate_swamp", 0),
						#(display_message, "@HUN2!"),
					(else_try), #spain-north
						(lt, ":x", -17860),
						(lt, ":y", -5638),
						(gt, ":x", -21620),
						(gt, ":y", -7779),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
							(assign, "$tom_generate_iberian", 0),
							(assign, "$tom_generate_swamp", 0),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
							(assign, "$tom_generate_iberian2", 0),
							(assign, "$tom_generate_swamp", 0),
						(try_end),
						#(display_message, "@SPAIN NORTH!"),
					(else_try), #italian island
						(lt, ":x", -4636),
						(lt, ":y", -6318),
						(gt, ":x", -5807),
						(gt, ":y", -8170),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
							(assign, "$tom_generate_iberian", 0),
							(assign, "$tom_generate_swamp", 0),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
							(assign, "$tom_generate_iberian2", 0),
							(assign, "$tom_generate_swamp", 0),
						(try_end),
						#(display_message, "@ISTALIAN ISLAND!"),
					(else_try), #italy-rome
						(lt, ":x", 439),
						(lt, ":y", -5315),
						(gt, ":x", -1729),
						(gt, ":y", -8618),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
						(try_end),
						#(display_message, "@ROME!"),
					(else_try), #italy-south
						(lt, ":x", 2532),
						(lt, ":y", -8630),
						(gt, ":x", 1002),
						(gt, ":y", -11365),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
							(assign, "$tom_generate_iberian", 0),
							(assign, "$tom_generate_swamp", 0),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
							(assign, "$tom_generate_iberian2", 0),
							(assign, "$tom_generate_swamp", 0),
						(try_end),
						#(display_message, "@ITALY SOUTH!"),
					(else_try), #italy-south island
						(lt, ":x", 954),
						(lt, ":y", -12249),
						(gt, ":x", -537),
						(gt, ":y", -13150),
						(store_random_in_range, ":scene_to_use", "scn_1257_combat_iberian_hillside_0", "scn_1257_combat_euro_hillside_0"),
						(try_begin),
							(this_or_next|eq, ":terrain_type", rt_steppe_forest),
							(eq, ":terrain_type", rt_forest),
							(assign, "$tom_generate_iberian2", 1),
						(else_try),
							(assign, "$tom_generate_iberian", 1),
						(try_end),
						#(display_message, "@ITALY SOUTH ISLAND!"),
					(try_end),
				(try_end),
				#(set_fixed_point_multiplier, 100),
				#debug
				# (assign, "$tom_generate_iberian", 1),
				# (assign, "$tom_generate_iberian2", 1),
				# (assign, "$tom_generate_swamp", 0),
				# (assign, "$tom_generate_desert", 0),
				# (assign, "$tom_generate_desertv2", 0),
				# (assign, ":scene_to_use", "scn_1257_combat_iberian_hillside_1"),
				
				#(assign, ":scene_to_use", "scn_1257_combat_steppe_0"),
				
				#other put this here?
				#(try_begin),
				#(this_or_next | eq, ":faction_no", "fac_kingdom_1"),
				#(eq, ":faction_no", "fac_kingdom_2"),
				#(assign, ":scene_to_use", "scn_1257_combat_steppe_1"),
				#(try_end),
				#TOM END
				
				(jump_to_scene,":scene_to_use"),
		])
		

		# script_enter_dungeon
		# Input: arg1 = center_no, arg2 = mission_template_no
		# Output: none
enter_dungeon=(
	"enter_dungeon",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":mission_template_no"),
				
				(set_jump_mission,":mission_template_no"),
				#new added...
				(mission_tpl_entry_set_override_flags, ":mission_template_no", 0, af_override_horse),
				(try_begin),
					(eq, "$sneaked_into_town", 1),
					(mission_tpl_entry_set_override_flags, ":mission_template_no", 0, af_override_all),
					
					(mission_tpl_entry_clear_override_items, ":mission_template_no", 0),
					(mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_pilgrim_hood"),
					(mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_pilgrim_disguise"),
					(mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_practice_staff"),
					(mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_throwing_daggers"),
				(try_end),
				#new added end
				
				(party_get_slot, ":dungeon_scene", ":center_no", slot_town_prison),
				
				(modify_visitors_at_site,":dungeon_scene"),
				(reset_visitors),
				(assign, ":cur_pos", 16),
				
				
				(call_script, "script_get_heroes_attached_to_center_as_prisoner", ":center_no", "p_temp_party"),
				(party_get_num_companion_stacks, ":num_stacks","p_temp_party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),
					
		 ## (neg|is_between, ":stack_troop", commoners_begin, commoners_end), #tom retinue
					(assign, ":prisoner_offered_parole", 0),
					(try_begin),
						(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(else_try),
						(call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
						(assign, ":prisoner_offered_parole", 1),
					(else_try),
						(assign, ":prisoner_offered_parole", 0),
					(try_end),
					(eq, ":prisoner_offered_parole", 0),
					
					(lt, ":cur_pos", 32), # spawn up to entry point 32
					(set_visitor, ":cur_pos", ":stack_troop"),
					(val_add,":cur_pos", 1),
				(try_end),
				
				#	  (set_visitor, ":cur_pos", "trp_npc3"),
				#	  (troop_set_slot, "trp_npc3", slot_troop_prisoner_of_party, "$g_encountered_party"),
				
				(set_jump_entry, 0),
				(jump_to_scene,":dungeon_scene"),
				(scene_set_slot, ":dungeon_scene", slot_scene_visited, 1),
				(change_screen_mission),
		])
		

		# script_enter_court
		# other search term: setup_court
		# includes diplomacy mod
		# WARNING: heavily modified by 1257AD
		# Input: arg1 = center_no
		# Output: none
enter_court=(
	"enter_court",
			[
				(store_script_param_1, ":center_no"),
				
				(assign, "$talk_context", tc_court_talk),
				
				(set_jump_mission,"mt_visit_town_castle"),
				
				(mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
				#(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_all),
				
				(party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
				(modify_visitors_at_site,":castle_scene"),
				(reset_visitors),
				#Adding guards
				(store_faction_of_party, ":center_faction", ":center_no"),
				(faction_get_slot, ":guard_troop", ":center_faction", slot_faction_guard_troop),
				(try_begin),
					(le, ":guard_troop", 0),
					(assign, ":guard_troop", "trp_euro_spearman_3"),
				(try_end),
				(set_visitor, 6, ":guard_troop"),
				(set_visitor, 7, ":guard_troop"),
				
				(assign, ":cur_pos", 16),
				
				(try_begin),
					(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
					(gt, ":player_spouse", 0),
					(troop_slot_eq, ":player_spouse", slot_troop_cur_center, ":center_no"),
					(set_visitor, ":cur_pos", ":player_spouse"),
					(val_add,":cur_pos", 1),
				(else_try),
					(troop_get_slot, ":player_betrothed", "trp_player", slot_troop_betrothed),
					(gt, ":player_betrothed", 0),
					(troop_slot_eq, ":player_betrothed", slot_troop_cur_center, ":center_no"),
					(set_visitor, ":cur_pos", ":player_betrothed"),
					(val_add,":cur_pos", 1),
				(try_end),
				
				(try_begin),
					(eq, "$g_player_court", ":center_no"),
					(gt, "$g_player_minister", 0),
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_player_minister"),
					(set_visitor, ":cur_pos", "$g_player_minister"),
					(val_add,":cur_pos", 1),
				(try_end),
				##diplomacy begin
				(try_begin),
					(gt, "$g_player_chamberlain", 0),
					(assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),  #fix for wrong troops after update
					(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
					(eq, ":town_lord", "trp_player"),
					(set_visitor, ":cur_pos", "$g_player_chamberlain"),
					(val_add,":cur_pos", 1),
				(try_end),
				
				(try_begin),
					(gt, "$g_player_constable", 0),
					(assign, "$g_player_constable", "trp_dplmc_constable"),  #fix for wrong troops after update
					(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
					(eq, ":town_lord", "trp_player"),
					(set_visitor, ":cur_pos", "$g_player_constable"),
					(val_add,":cur_pos", 1),
				(try_end),
				
				(try_begin),
					(gt, "$g_player_chancellor", 0),
					(assign, "$g_player_chancellor", "trp_dplmc_chancellor"), #fix for wrong troops after update
					(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
					(eq, ":town_lord", "trp_player"),
					(set_visitor, ":cur_pos", "$g_player_chancellor"),
					(val_add,":cur_pos", 1),
				(try_end),
				##diplomacy end
				
				#Lords wishing to pledge allegiance - inactive, but part of player faction
				(try_begin),
					(eq, "$g_player_court", ":center_no"),
					(faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"),
					(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
						(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
						(eq, ":active_npc_faction", "fac_player_supporters_faction"),
						(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
						(neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
						(neq, ":active_npc", "$g_player_minister"),
						(set_visitor, ":cur_pos", ":active_npc"),
						(val_add,":cur_pos", 1),
					(try_end),
				(try_end),
				
				(call_script, "script_get_heroes_attached_to_center", ":center_no", "p_temp_party"),
				(party_get_num_companion_stacks, ":num_stacks","p_temp_party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),
			(gt, ":stack_troop", 0), ####BUGFIX LINE freelancer chief
					(lt, ":cur_pos", 32), # spawn up to entry point 32 - is it possible to add another 10 spots?
					(set_visitor, ":cur_pos", ":stack_troop"),
					(val_add,":cur_pos", 1),
				(try_end),
				(try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
					(neq, ":cur_troop", "trp_knight_1_1_wife"), #The one who should not appear in game
					#(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
					(troop_slot_eq, ":cur_troop", slot_troop_cur_center, ":center_no"),
					
					(assign, ":lady_meets_visitors", 0),
					(try_begin),
						(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":cur_troop"), #player spouse goes in position of honor
						(this_or_next|troop_slot_eq, "trp_player", slot_troop_betrothed, ":cur_troop"), #player spouse goes in position of honor
						(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_spouse, "trp_player"), #player spouse goes in position of honor
						(troop_slot_eq, ":cur_troop", slot_troop_betrothed, "trp_player"),
						
						(assign, ":lady_meets_visitors", 0), #She is already in the place of honor
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, s4, ":cur_troop"),
							(display_message, "str_s4_is_present_at_the_center_and_in_place_of_honor"),
						(try_end),
						
					(else_try), #lady is troop
						(store_faction_of_troop, ":lady_faction", ":cur_troop"),
						(neq, ":lady_faction", ":center_faction"),
						
						(assign, ":lady_meets_visitors", 1),
						
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, s4, ":cur_troop"),
							(display_message, "str_s4_is_present_at_the_center_as_a_refugee"),
						(try_end),
						
					(else_try),
						(troop_slot_ge, ":cur_troop", slot_troop_spouse, 1),
						
						(try_begin),
							#married ladies at a feast will not mingle - this is ahistorical, as married women and widows probably had much more freedom than unmarried ones, at least in the West, but the game needs to leave slots for them to show off their unmarried daughters
							(faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
							(faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
							(assign, ":lady_meets_visitors", 0),
							
							(try_begin),
								(eq, "$cheat_mode", 1),
								(str_store_troop_name, s4, ":cur_troop"),
								(display_message, "str_s4_is_present_at_the_center_and_not_attending_the_feast"),
							(try_end),
						(else_try),
							(assign, ":lady_meets_visitors", 1),
							
							(try_begin),
								(eq, "$cheat_mode", 1),
								(str_store_troop_name, s4, ":cur_troop"),
								(display_message, "str_s4_is_present_at_the_center_and_is_married"),
							(try_end),
						(try_end),
						
					(else_try), #feast is in progress
						(faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
						(faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
						(assign, ":lady_meets_visitors", 1),
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, s4, ":cur_troop"),
							(display_message, "@{!}DEBUG -- {s4} is present at the center and is attending the feast"),
						(try_end),
						
					(else_try), #already met - awaits in private
						(troop_slot_ge, ":cur_troop", slot_troop_met, 2),
						(assign, ":lady_meets_visitors", 0),
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, s4, ":cur_troop"),
							(display_message, "@{!}DEBUG -- {s4} is present at the center and is awaiting the player in private"),
						(try_end),
						
					(else_try),
						(call_script, "script_get_kingdom_lady_social_determinants", ":cur_troop"),
						(call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", reg0, "trp_player"),
						(gt, reg0, 0),
						(assign, ":lady_meets_visitors", 1),
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, s4, ":cur_troop"),
							(display_message, "@{!}DEBUG -- {s4} is_present_at_the_center_and_is_allowed_to_meet_the_player"),
						(try_end),
						
					(else_try),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, s4, ":cur_troop"),
							(display_message, "@{!}DEBUG -- {s4}is_present_at_the_center_and_is_not_allowed_to_meet_the_player"),
						(try_end),
						
					(try_end),
					
					(eq, ":lady_meets_visitors", 1),
					
					(lt, ":cur_pos", 32), # spawn up to entry point 32
					(set_visitor, ":cur_pos", ":cur_troop"),
					(val_add,":cur_pos", 1),
				(try_end),
				
				(set_jump_entry, 0),
				
				(jump_to_scene,":castle_scene"),
				(scene_set_slot, ":castle_scene", slot_scene_visited, 1),
				(change_screen_mission),
		])
		

		#script_setup_meet_lady
		# sets up a scene to meet player with lady
		# INPUT: lady_no, center_no
		# OUTPUT: none
setup_meet_lady=(
	"setup_meet_lady",
			[
				(store_script_param_1, ":lady_no"),
				(store_script_param_2, ":center_no"),
				
				#(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_horse),
				(troop_set_slot, ":lady_no", slot_lady_last_suitor, "trp_player"),
				
				(set_jump_mission,"mt_visit_town_castle"),
				(party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
				(modify_visitors_at_site,":castle_scene"),
				(reset_visitors),
				
				(troop_set_age, "trp_nurse_for_lady", 100),
				(set_visitor, 7, "trp_nurse_for_lady"),
				
				(assign, ":cur_pos", 16),
				(set_visitor, ":cur_pos", ":lady_no"),
				
				(assign, "$talk_context", tc_garden),
				
				(jump_to_scene,":castle_scene"),
				(scene_set_slot, ":castle_scene", slot_scene_visited, 1),
				(change_screen_mission),
		])
		