from header import *
		# script_setup_random_scene
		# used to generate battle scene! interesting stuffs
		# WARNING : HEAVILY modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = mission_template_no
		# Output: none
setup_random_scene = (
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
enter_dungeon = (
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
enter_court = (
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
setup_meet_lady = (
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
		

		# script_cf_turn_windmill_fans
		# Input: arg1 = instance_no (none = 0)
		# Output: none
cf_turn_windmill_fans = (
	"cf_turn_windmill_fans",
			[(store_script_param_1, ":instance_no"),
				(scene_prop_get_instance, ":windmill_fan_object", "spr_windmill_fan_turning", ":instance_no"),
				(ge, ":windmill_fan_object", 0),
				(prop_instance_get_position, pos1, ":windmill_fan_object"),
				(position_rotate_y, pos1, 10),
				(prop_instance_animate_to_position, ":windmill_fan_object", pos1, 100),
				(val_add, ":instance_no", 1),
				(call_script, "script_cf_turn_windmill_fans", ":instance_no"),
		])

		# script_remove_siege_objects
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
remove_siege_objects = (
	"remove_siege_objects",
			[
				(replace_scene_props, "spr_eastroman_wall_destroyed", "spr_eastroman_wall"),
				(replace_scene_props, "spr_battlement_a_destroyed", "spr_battlement_a"),
				(replace_scene_props, "spr_snowy_castle_battlement_a_destroyed", "spr_snowy_castle_battlement_a"),
				(replace_scene_props, "spr_castle_e_battlement_a_destroyed", "spr_castle_e_battlement_a"),
				(replace_scene_props, "spr_castle_battlement_a_destroyed", "spr_castle_battlement_a"),
				(replace_scene_props, "spr_castle_battlement_b_destroyed", "spr_castle_battlement_b"),
				(replace_scene_props, "spr_earth_wall_a2", "spr_earth_wall_a"),
				(replace_scene_props, "spr_earth_wall_b2", "spr_earth_wall_b"),
				(replace_scene_props, "spr_belfry_platform_b", "spr_empty"),
				(replace_scene_props, "spr_belfry_platform_a", "spr_empty"),
				(replace_scene_props, "spr_belfry_a", "spr_empty"),
				(replace_scene_props, "spr_belfry_wheel", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_move_6m", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_move_8m", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_move_10m", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_move_12m", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_move_14m", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_12m", "spr_empty"),
				(replace_scene_props, "spr_siege_ladder_14m", "spr_empty"),
				(replace_scene_props, "spr_mangonel", "spr_empty"),
				(replace_scene_props, "spr_trebuchet_old", "spr_empty"),
				(replace_scene_props, "spr_trebuchet_new", "spr_empty"),
				(replace_scene_props, "spr_stone_ball", "spr_empty"),
				(replace_scene_props, "spr_Village_fire_big", "spr_empty"),
				###tom 1257ad
				(replace_scene_props, "spr_1257_earth_gate", "spr_empty"),
				(replace_scene_props, "spr_1257_portcullis", "spr_empty"),
				(replace_scene_props, "spr_1257_tavern_door_a", "spr_empty"),
				(replace_scene_props, "spr_1257_tavern_door_b", "spr_empty"),
				(replace_scene_props, "spr_1257_castle_f_door_a", "spr_empty"),
		])
	

		# script_center_ambiance_sounds
		# Input: none
		# Output: none
		# to be called every two seconds
center_ambiance_sounds = (
	"center_ambiance_sounds",
			[
				(assign, ":sound_1", -1),
				(assign, ":sound_2", -1),
				(assign, ":sound_3", -1),
				(assign, ":sound_4", -1),
				(assign, ":sound_5", -1),
				(try_begin),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
					(try_begin),
						(neg|is_currently_night),
						(assign, ":sound_3", "snd_distant_dog_bark"),
						(assign, ":sound_3", "snd_distant_chicken"),
					(else_try),
						(assign, ":sound_1", "snd_distant_dog_bark"),
						(assign, ":sound_2", "snd_distant_owl"),
					(try_end),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(try_begin),
						(neg|is_currently_night),
						(assign, ":sound_1", "snd_distant_carpenter"),
						(assign, ":sound_2", "snd_distant_blacksmith"),
						(assign, ":sound_3", "snd_distant_dog_bark"),
					(else_try),
						(assign, ":sound_1", "snd_distant_dog_bark"),
					(try_end),
				(try_end),
				(try_begin),
					(store_random_in_range, ":r", 0, 7),
					(try_begin),
						(eq, ":r", 1),
						(ge, ":sound_1", 0),
						(play_sound, ":sound_1"),
					(else_try),
						(eq, ":r", 2),
						(ge, ":sound_2", 0),
						(play_sound, ":sound_2"),
					(else_try),
						(eq, ":r", 3),
						(ge, ":sound_3", 0),
						(play_sound, ":sound_3"),
					(else_try),
						(eq, ":r", 4),
						(ge, ":sound_4", 0),
						(play_sound, ":sound_4"),
					(else_try),
						(eq, ":r", 5),
						(ge, ":sound_5", 0),
						(play_sound, ":sound_5"),
					(try_end),
				(try_end),
		])
		
		# script_center_set_walker_to_type
		# Input: arg1 = center_no, arg2 = walker_no, arg3 = walker_type,
		# Output: none
center_set_walker_to_type = (
	"center_set_walker_to_type",
			[
				(store_script_param, ":center_no", 1),
				(store_script_param, ":walker_no", 2),
				(store_script_param, ":walker_type", 3),
				(store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
				(party_set_slot, ":center_no", ":type_slot", ":walker_type"),
				(party_get_slot, ":center_faction", ":center_no", slot_center_original_faction),
				(faction_get_slot, ":center_culture", ":center_faction", slot_faction_culture),
				(store_random_in_range, ":walker_troop_slot", 0, 2),
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(val_add, ":walker_troop_slot", slot_faction_village_walker_male_troop),
				(else_try),
					(val_add, ":walker_troop_slot", slot_faction_town_walker_male_troop),
				(try_end),
				(try_begin),
					(eq,":walker_type", walkert_spy),
					(assign,":original_walker_slot",":walker_troop_slot"),
					(val_add,":walker_troop_slot",4), # select spy troop id slot
				(try_end),
				(faction_get_slot, ":walker_troop_id", ":center_culture", ":walker_troop_slot"),
				(try_begin),
					(eq,":walker_type", walkert_spy),
					(faction_get_slot, ":original_walker", ":center_culture", ":original_walker_slot"),
					# restore spy inventory
					(try_for_range,":item_no","itm_horse_meat","itm_wooden_stick"),
						(store_item_kind_count,":num_items",":item_no",":original_walker"),
						(ge,":num_items",1),
						(store_item_kind_count,":num_items",":item_no",":walker_troop_id"),
						(lt,":num_items",1),
						(troop_add_items,":walker_troop_id",":item_no",1),
					(try_end),
					# determine spy recognition item
					(store_random_in_range,":spy_item_type",itp_type_head_armor,itp_type_hand_armor),
					(assign,":num",0),
					(try_for_range,":item_no","itm_horse_meat","itm_wooden_stick"),
						(store_item_kind_count,":num_items",":item_no",":walker_troop_id"),
						(ge,":num_items",1),
						(item_get_type, ":itp", ":item_no"),
						(eq,":itp",":spy_item_type"),
						(val_add,":num",1),
						(troop_remove_items,":walker_troop_id",":item_no",":num_items"),
					(try_end),
					(store_random_in_range,":random_item",0,":num"),
					(assign,":num",-1),
					(try_for_range,":item_no","itm_horse_meat","itm_wooden_stick"),
						(store_item_kind_count,":num_items",":item_no",":original_walker"),
						(ge,":num_items",1),
						(item_get_type, ":itp", ":item_no"),
						(eq,":itp",":spy_item_type"),
						(val_add,":num",1),
						(eq,":num",":random_item"),
						(troop_add_items,":walker_troop_id",":item_no",1),
						(assign,":spy_item",":item_no"),
					(try_end),
					(assign,"$spy_item_worn",":spy_item"),
					(assign,"$spy_quest_troop",":walker_troop_id"),
					(troop_equip_items,":walker_troop_id"),
				(try_end),
				(store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
				(party_set_slot, ":center_no", ":troop_slot", ":walker_troop_id"),
				(store_random_in_range, ":walker_dna", 0, 1000000),
				(store_add, ":dna_slot", slot_center_walker_0_dna, ":walker_no"),
				(party_set_slot, ":center_no", ":dna_slot", ":walker_dna"),
		])
		

		# script_init_town_walkers
		# Input: none
		# Output: none
init_town_walkers = (
	"init_town_walkers",
			[
				(try_begin),
					(eq, "$town_nighttime", 0),
					(try_for_range, ":walker_no", 0, num_town_walkers),
						(store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
						(party_get_slot, ":walker_troop_id", "$current_town", ":troop_slot"),
						(gt, ":walker_troop_id", 0),
						(store_add, ":entry_no", town_walker_entries_start, ":walker_no"),
						#(set_visitor, ":entry_no", ":walker_troop_id"),
						#tom
						(try_for_range, reg0, 0, 4),
							(set_visitor, ":entry_no", ":walker_troop_id"),
						(try_end),
					(try_end), 
				(try_end),
		])
		

		# script_init_town_agent
		# Input: none
		# Output: none
init_town_agent = (
	"init_town_agent",
			[
				(store_script_param, ":agent_no", 1),
				(agent_get_troop_id, ":troop_no", ":agent_no"),
				(set_fixed_point_multiplier, 100),
				(assign, ":stand_animation", -1),
				(try_begin),
					(this_or_next|is_between, ":troop_no", armor_merchants_begin, armor_merchants_end),
					(is_between, ":troop_no", weapon_merchants_begin, weapon_merchants_end),
					(try_begin),
						(troop_get_type, ":cur_troop_gender", ":troop_no"),
						(eq, ":cur_troop_gender", 0),
						(agent_set_animation, ":agent_no", "anim_stand_townguard"),
					(else_try),
						(agent_set_animation, ":agent_no", "anim_stand_townguard"),
					(end_try),
				(else_try),
					(is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
					(assign, ":stand_animation", "anim_stand_lady"),
				(else_try),
					(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
					(assign, ":stand_animation", "anim_stand_lord"),
				(else_try),
					(is_between, ":troop_no", soldiers_begin, soldiers_end),
					(assign, ":stand_animation", "anim_stand_townguard"),
				(try_end),
				(try_begin),
					(ge, ":stand_animation", 0),
					(agent_set_stand_animation, ":agent_no", ":stand_animation"),
					(agent_set_animation, ":agent_no", ":stand_animation"),
					(store_random_in_range, ":random_no", 0, 100),
					(agent_set_animation_progress, ":agent_no", ":random_no"),
				(try_end),
		])
		
		# script_init_town_walker_agents
		# Input: none
		# Output: none
init_town_walker_agents = (
	"init_town_walker_agents",
			[(assign, ":num_walkers", 0),
				(try_for_agents, ":cur_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
					(is_between, ":cur_troop", walkers_begin, walkers_end),
					(val_add, ":num_walkers", 1),
			(agent_get_position, pos1, ":cur_agent"),
					(try_for_range, ":i_e_p", 9, 40),#Entry points
						(entry_point_get_position, pos2, ":i_e_p"),
						(get_distance_between_positions, ":distance", pos1, pos2),
						(lt, ":distance", 200),
						(agent_set_slot, ":cur_agent", 0, ":i_e_p"),
					(try_end),
					(call_script, "script_set_town_walker_destination", ":cur_agent"),
				(try_end),
		])
		
		# script_tick_town_walkers
		# Input: none
		# Output: none
tick_town_walkers = (
	"tick_town_walkers",
			[(try_for_agents, ":cur_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
					(is_between, ":cur_troop", walkers_begin, walkers_end),
					(agent_get_slot, ":target_entry_point", ":cur_agent", 0),
					(entry_point_get_position, pos1, ":target_entry_point"),
					(try_begin),
						(lt, ":target_entry_point", 32),
						(init_position, pos2),
						(position_set_y, pos2, 250),
						(position_transform_position_to_parent, pos1, pos1, pos2),
					(try_end),
					(agent_get_position, pos2, ":cur_agent"),
					(get_distance_between_positions, ":distance", pos1, pos2),
					(lt, ":distance", 400),
					(assign, ":random_no", 0),
					(try_begin),
						(lt, ":target_entry_point", 32),
						(store_random_in_range, ":random_no", 0, 100),
					(try_end),
					(lt, ":random_no", 20),
					(call_script, "script_set_town_walker_destination", ":cur_agent"),
				(try_end),
		])

		# script_set_town_walker_destination
		# WARNING: modified by 1257AD devs
		# Input: arg1 = agent_no
		# Output: none
set_town_walker_destination = (
	"set_town_walker_destination",
			[
				#TOM
				(store_script_param_1, ":agent_no"),
				#(store_random_in_range, ":rand_dest", 32, 42),
		(store_random_in_range, ":rand_dest", 32, 40),
				(try_begin),
					# (eq, ":rand_dest", 41),
					# (assign, ":target_entry_point", 9),
				# (else_try),
					# (eq, ":rand_dest", 40),
					# (assign, ":target_entry_point", 10),
				# (else_try),
					# (eq, ":rand_dest", 39),
					# (assign, ":target_entry_point", 12),
				# (else_try),
					(assign, ":target_entry_point", ":rand_dest"),
				(try_end),
				
				(try_begin),
					(agent_set_slot, ":agent_no", 0, ":target_entry_point"),
					(entry_point_get_position, pos1, ":target_entry_point"),
					(try_begin),
						(init_position, pos2),
						(position_set_y, pos2, 250),
						(position_transform_position_to_parent, pos1, pos1, pos2),
					(try_end),
					(agent_set_scripted_destination, ":agent_no", pos1, 0),
					(agent_set_speed_limit, ":agent_no", 5),
				(try_end),
		])
		
		# script_town_init_doors
		# Input: door_state (-1 = closed, 1 = open, 0 = use $town_nighttime)
		# Output: none (required for siege mission templates)
town_init_doors = (
	"town_init_doors",
			[(store_script_param, ":door_state", 1),
				(try_begin),
					(assign, ":continue", 0),
					(try_begin),
						(eq, ":door_state", 1),
						(assign, ":continue", 1),
					(else_try),
						(eq, ":door_state", 0),
						(eq, "$town_nighttime", 0),
						(assign, ":continue", 1),
					(try_end),
					(eq, ":continue", 1),# open doors
					(assign, ":end_cond", 1),
					(try_for_range, ":i_instance", 0, ":end_cond"),
						(scene_prop_get_instance, ":object", "spr_towngate_door_left", ":i_instance"),
						(ge, ":object", 0),
						(val_add, ":end_cond", 1),
						(prop_instance_get_position, pos1, ":object"),
						(position_rotate_z, pos1, -100),
						(prop_instance_animate_to_position, ":object", pos1, 1),
					(try_end),
					(assign, ":end_cond", 1),
					(try_for_range, ":i_instance", 0, ":end_cond"),
						(scene_prop_get_instance, ":object", "spr_towngate_rectangle_door_left", ":i_instance"),
						(ge, ":object", 0),
						(val_add, ":end_cond", 1),
						(prop_instance_get_position, pos1, ":object"),
						(position_rotate_z, pos1, -80),
						(prop_instance_animate_to_position, ":object", pos1, 1),
					(try_end),
					(assign, ":end_cond", 1),
					(try_for_range, ":i_instance", 0, ":end_cond"),
						(scene_prop_get_instance, ":object", "spr_towngate_door_right", ":i_instance"),
						(ge, ":object", 0),
						(val_add, ":end_cond", 1),
						(prop_instance_get_position, pos1, ":object"),
						(position_rotate_z, pos1, 100),
						(prop_instance_animate_to_position, ":object", pos1, 1),
					(try_end),
					(assign, ":end_cond", 1),
					(try_for_range, ":i_instance", 0, ":end_cond"),
						(scene_prop_get_instance, ":object", "spr_towngate_rectangle_door_right", ":i_instance"),
						(ge, ":object", 0),
						(val_add, ":end_cond", 1),
						(prop_instance_get_position, pos1, ":object"),
						(position_rotate_z, pos1, 80),
						(prop_instance_animate_to_position, ":object", pos1, 1),
					(try_end),
				(try_end),
		])


		# script_change_banners_and_chest
		# Input: none
		# Output: none
change_banners_and_chest = (
	"change_banners_and_chest",
			[(party_get_slot, ":cur_leader", "$g_encountered_party", slot_town_lord),
				(try_begin),
					(ge, ":cur_leader", 0),
					#normal_banner_begin
					(troop_get_slot, ":troop_banner_object", ":cur_leader", slot_troop_banner_scene_prop),
					(gt, ":troop_banner_object", 0),
					(replace_scene_props, banner_scene_props_begin, ":troop_banner_object"),
				(else_try),
					(replace_scene_props, banner_scene_props_begin, "spr_empty"),
				(try_end),
				(try_begin),
					(neq, ":cur_leader", "trp_player"),
					(replace_scene_props, "spr_player_chest", "spr_locked_player_chest"),
				(try_end),
		])
		

		# script_place_player_banner_near_inventory
		# Input: none
		# Output: none
place_player_banner_near_inventory = (
	"place_player_banner_near_inventory",
			[
				#normal_banner_begin
				(troop_get_slot, ":troop_banner_object", "trp_player", slot_troop_banner_scene_prop),
				#custom_banner_begin
				#    	(troop_get_slot, ":flag_spr", "trp_player", slot_troop_custom_banner_flag_type),
				
				(try_begin),
					#normal_banner_begin
					(gt, ":troop_banner_object", 0),
					(scene_prop_get_instance, ":flag_object", ":troop_banner_object", 0),
					#custom_banner_begin
					#       (ge, ":flag_spr", 0),
					#       (val_add, ":flag_spr", custom_banner_flag_scene_props_begin),
					#       (scene_prop_get_instance, ":flag_object", ":flag_spr", 0),
					(try_begin),
						(ge, ":flag_object", 0),
						(get_player_agent_no, ":player_agent"),
						(agent_get_look_position, pos1, ":player_agent"),
						(position_move_y, pos1, -500),
						(position_rotate_z, pos1, 180),
						(position_set_z_to_ground_level, pos1),
						(position_move_z, pos1, 300),
						(prop_instance_set_position, ":flag_object", pos1),
					(try_end),
					(scene_prop_get_instance, ":pole_object", "spr_banner_pole", 0),
					(try_begin),
						(ge, ":pole_object", 0),
						(position_move_z, pos1, -320),
						(prop_instance_set_position, ":pole_object", pos1),
					(try_end),
				(else_try),
					(init_position, pos1),
					(position_move_z, pos1, -1000000),
					(scene_prop_get_instance, ":flag_object", banner_scene_props_begin, 0),
					(try_begin),
						(ge, ":flag_object", 0),
						(prop_instance_set_position, ":flag_object", pos1),
					(try_end),
					(scene_prop_get_instance, ":pole_object", "spr_banner_pole", 0),
					(try_begin),
						(ge, ":pole_object", 0),
						(prop_instance_set_position, ":pole_object", pos1),
					(try_end),
				(try_end),
		])
		
		# script_place_player_banner_near_inventory_bms
		# Input: none
		# Output: none
place_player_banner_near_inventory_bms = (
	"place_player_banner_near_inventory_bms",
			[
				#normal_banner_begin
				(troop_get_slot, ":troop_banner_object", "trp_player", slot_troop_banner_scene_prop),
				#custom_banner_begin
				#      (troop_get_slot, ":flag_spr", "trp_player", slot_troop_custom_banner_flag_type),
				(try_begin),
					#normal_banner_begin
					(gt, ":troop_banner_object", 0),
					(replace_scene_props, banner_scene_props_begin, ":troop_banner_object"),
					#custom_banner_begin
					#       (ge, ":flag_spr", 0),
					#       (val_add, ":flag_spr", custom_banner_flag_scene_props_begin),
					#       (replace_scene_props, banner_scene_props_begin, ":flag_spr"),
				(try_end),
		])