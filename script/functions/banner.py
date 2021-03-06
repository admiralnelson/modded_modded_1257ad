from header import *

#script_agent_troop_get_historical_mesh
# NOTE: modified by 1257AD devs
# INPUT: agent_no, troop_no
# OUTPUT: banner_mesh
agent_troop_get_historical_mesh = (
	"agent_troop_get_historical_mesh",
			[
				(store_script_param, ":agent_no", 1),
				(store_script_param, ":troop_no", 2),
				(assign, ":banner_troop", -1), 
				#(assign, ":banner_mesh", "mesh_banners_default_b"),
		#(store_random_in_range, ":banner_mesh", "mesh_banners_default_a", "mesh_troop_label_banner"),
		
				(try_begin), 
					(ge, ":agent_no", 0),
					(agent_get_item_slot, ":item", ":agent_no", 5),
					(gt, ":item", 0),
					(item_get_slot, ":slot_mesh", ":item", slot_item_banner),
				(try_end),
		
				##default players, random or items default
				(store_random_in_range, ":random", 0, 3),
				(try_begin),
					(eq, ":troop_no", "trp_player"),
					(neq, "$randomize_player_shield", 1),
					(assign, ":banner_mesh", "mesh_banners_default_b"),  
				(else_try), 
					(gt, ":slot_mesh", 0),
					(assign, ":banner_mesh", ":slot_mesh"),
				(else_try), #somewhat more leather then paint meshes
					(neq, ":random", 0),
					(store_random_in_range, ":banner_mesh", "mesh_banner_t15", "mesh_banner_u01"),
						(else_try),
					(store_random_in_range, ":banner_mesh", "mesh_banners_default_a", "mesh_troop_label_banner"),
				(try_end),
				
				##find specific banner
				(try_begin),
					(ge, ":troop_no", 0),
					(troop_slot_ge, ":troop_no", slot_troop_banner_scene_prop, 1),
					(assign, ":banner_troop", ":troop_no"),
				(else_try),
					(assign, ":continue", 0),
					(try_begin), #check if player is a crusader on freelancer
						(gt, "$freelancer_state", 0),
					(is_between, "$player_cur_troop", "trp_teu_village_recruit", "trp_tatar_tribesman"),
					(neg|is_between, "$player_cur_troop", "trp_teu_balt_1", "trp_teu_ger_1"),
					(assign, ":continue", 1),
					(try_end),
					(this_or_next|eq, ":continue", 1),
					(is_between, ":troop_no", "trp_teu_village_recruit", "trp_tatar_tribesman"), #teutonic
					(try_begin), #knight
						(is_between, ":troop_no", "trp_teu_horse_1", "trp_tatar_tribesman"),
					(store_random_in_range, ":banner_mesh", "mesh_banner_q01", "mesh_banner_r01"),
					(else_try),
						(store_random_in_range, ":random", 0, 2),
					(eq, ":random", 0),
					(store_random_in_range, ":banner_mesh", "mesh_banner_q01", "mesh_banner_r01"),
					(try_end),
				(else_try),  
					(assign, ":continue", 0),
					(try_begin), #check if player is a crusader on freelancer
						(gt, "$freelancer_state", 0),
					(is_between, "$player_cur_troop", "trp_templar_half_brother", "trp_mercenaries_end"),
					(assign, ":continue", 1),
					(try_end),
					(this_or_next|eq, ":continue", 1),
					(is_between, ":troop_no", "trp_templar_half_brother", "trp_mercenaries_end"), # a crusader
					(try_begin),
								(is_between, ":troop_no", "trp_templar_half_brother", "trp_hospitaller_half_brother"),
					(assign, ":banner_mesh", "mesh_banner_x18"),
					(assign, ":banner_troop", -1),
							(else_try),
								(is_between, ":troop_no", "trp_hospitaller_half_brother", "trp_saint_lazarus_half_brother"),
								(assign, ":banner_mesh", "mesh_banner_x17"),
								(assign, ":banner_troop", -1),
							(else_try),
								(is_between, ":troop_no", "trp_saint_lazarus_half_brother", "trp_santiago_half_brother"),
								(assign, ":banner_mesh", "mesh_banner_o07"),
								(assign, ":banner_troop", -1),
							(else_try),
								(is_between, ":troop_no", "trp_santiago_half_brother", "trp_calatrava_half_brother"),
								(assign, ":banner_mesh", "mesh_banner_e21"),
								(assign, ":banner_troop", -1),
							(else_try),
								(is_between, ":troop_no", "trp_calatrava_half_brother", "trp_saint_thomas_half_brother"),
								(assign, ":banner_mesh", "mesh_banner_e18"),
								(assign, ":banner_troop", -1),
							(else_try),
								(is_between, ":troop_no", "trp_saint_thomas_half_brother", "trp_varangian_guard"),
								(assign, ":banner_mesh", "mesh_banner_o08"),
								(assign, ":banner_troop", -1),
							(try_end),
						(else_try),
					(gt, ":agent_no", 0),
					(agent_get_party_id, ":agent_party", ":agent_no"),
							(ge, ":agent_party", 0),
							(party_get_template_id, ":party_template", ":agent_party"),
							(this_or_next|eq, ":party_template", "pt_crusaders"),
							(eq, ":party_template", "pt_crusader_raiders"),
							(store_random_in_range, ":random", 0, 2),
							(assign, ":banner_troop", -1),
							(try_begin),
								(eq,":random", 0),
								(assign, ":banner_mesh", "mesh_banner_f21"),
							(else_try),
								(store_random_in_range, ":banner_mesh", "mesh_banner_x17", "mesh_banner_x19"),
							(try_end),
						(try_end),
						#tom
						(try_begin),
							(ge, ":banner_troop", 0),
					(troop_slot_ge, ":banner_troop", slot_troop_banner_scene_prop, 1),
							(try_begin),
								(troop_get_slot, ":banner_spr", ":banner_troop", slot_troop_banner_scene_prop),
								(store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
								(is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
								(val_sub, ":banner_spr", banner_scene_props_begin),
								(store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),
							(try_end),
						(try_end),
				
				##extra check, as this thing goes off from the bounds sometimes...
				(try_begin),
					(neg|is_between, ":banner_mesh", "mesh_banner_a01", "mesh_troop_label_banner"),
					(store_random_in_range, ":banner_mesh", "mesh_banner_t15", "mesh_banner_u01"),
				(try_end),
				
						(assign, reg0, ":banner_mesh"),
		])


#script_agent_troop_get_banner_mesh
# part of freelancer script resides here
# WARNING: heavily modified by 1257AD devs
# INPUT: agent_no, troop_no
# OUTPUT: banner_mesh
agent_troop_get_banner_mesh = (
	"agent_troop_get_banner_mesh",
			[
				(store_script_param, ":agent_no", 1),
				(store_script_param, ":troop_no", 2),
				(assign, ":banner_troop", -1),
				(assign, ":banner_mesh", "mesh_banners_default_b"),
				(try_begin),
					(lt, ":agent_no", 0),
					(try_begin),
						(ge, ":troop_no", 0),
						(this_or_next|troop_slot_ge, ":troop_no", slot_troop_banner_scene_prop, 1),
						(eq, ":troop_no", "trp_player"),
						(assign, ":banner_troop", ":troop_no"),
					(else_try),
						(is_between, ":troop_no", companions_begin, companions_end),
						(assign, ":banner_troop", "trp_player"),
					(else_try),
						(assign, ":banner_mesh", "mesh_banners_default_a"),
					(try_end),
				(else_try),
					(eq, "$g_is_quick_battle", 1),
					(agent_get_team, ":agent_team", ":agent_no"),
					(try_begin),
						(eq, ":agent_team", 0),
						(assign, ":banner_mesh", "$g_quick_battle_team_0_banner"),
					(else_try),
						(assign, ":banner_mesh", "$g_quick_battle_team_1_banner"),
					(try_end),
				(else_try),
					(game_in_multiplayer_mode),
					(agent_get_group, ":agent_group", ":agent_no"),
					(try_begin),
						(neg|player_is_active, ":agent_group"),
						(agent_get_player_id, ":agent_group", ":agent_no"),
					(try_end),
					(try_begin),
						#if player banners are not allowed, use the default banner mesh
						(eq, "$g_multiplayer_allow_player_banners", 1),
						(player_is_active, ":agent_group"),
						(player_get_banner_id, ":player_banner", ":agent_group"),
						(ge, ":player_banner", 0),
						(store_add, ":banner_mesh", ":player_banner", arms_meshes_begin),
						(assign, ":already_used", 0),
						(try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end), #wrong client data check
							(faction_slot_eq, ":cur_faction", slot_faction_banner, ":banner_mesh"),
							(assign, ":already_used", 1),
						(try_end),
						(eq, ":already_used", 0), #otherwise use the default banner mesh
					(else_try),
						(agent_get_team, ":agent_team", ":agent_no"),
						(team_get_faction, ":team_faction_no", ":agent_team"),
						
						(try_begin),
							(agent_is_human, ":agent_no"),
							(faction_get_slot, ":banner_mesh", ":team_faction_no", slot_faction_banner),
						(else_try),
							(agent_get_rider, ":rider_agent_no", ":agent_no"),
							#(agent_get_position, pos1, ":agent_no"),
							#(position_get_x, ":pos_x", pos1),
							#(position_get_y, ":pos_y", pos1),
							#(assign, reg0, ":pos_x"),
							#(assign, reg1, ":pos_y"),
							#(assign, reg2, ":agent_no"),
							#(display_message, "@{!}agent_no:{reg2}, pos_x:{reg0} , posy:{reg1}"),
							(try_begin),
								(ge, ":rider_agent_no", 0),
								(agent_is_active, ":rider_agent_no"),
								(agent_get_team, ":rider_agent_team", ":rider_agent_no"),
								(team_get_faction, ":rider_team_faction_no", ":rider_agent_team"),
								(faction_get_slot, ":banner_mesh", ":rider_team_faction_no", slot_faction_banner),
							(else_try),
								(assign, ":banner_mesh", "mesh_banners_default_c"),
							(try_end),
						(try_end),
					(try_end),
				(else_try),
					(agent_get_troop_id, ":troop_id", ":agent_no"),
					(this_or_next|troop_slot_ge,  ":troop_id", slot_troop_banner_scene_prop, 1),
					(eq, ":troop_no", "trp_player"),
					(assign, ":banner_troop", ":troop_id"),
				(else_try),
					(agent_get_party_id, ":agent_party", ":agent_no"),
					(try_begin),
						(lt, ":agent_party", 0),
						(is_between, ":troop_id", companions_begin, companions_end),
						(main_party_has_troop, ":troop_id"),
						(assign, ":agent_party", "p_main_party"),
					(try_end),
					(ge, ":agent_party", 0),
					(party_get_template_id, ":party_template", ":agent_party"),
					(try_begin),
						(eq, ":party_template", "pt_deserters"),
						(assign, ":banner_mesh", "mesh_banners_default_c"),
					(else_try),
						(is_between, ":agent_party", centers_begin, centers_end),
						(is_between, ":troop_id", companions_begin, companions_end),
						(neq, "$talk_context", tc_tavern_talk),
						#this should be a captured companion in prison
						(assign, ":banner_troop", "trp_player"),
					(else_try),
						(is_between, ":agent_party", centers_begin, centers_end),
						(party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
						(ge, ":town_lord", 0),
						(assign, ":banner_troop", ":town_lord"),
					(else_try),
						(this_or_next|party_slot_eq, ":agent_party", slot_party_type, spt_kingdom_hero_party),
						(eq, ":agent_party", "p_main_party"),
						(party_get_num_companion_stacks, ":num_stacks", ":agent_party"),
						(gt, ":num_stacks", 0),
						(party_stack_get_troop_id, ":leader_troop_id", ":agent_party", 0),
						(this_or_next|troop_slot_ge,  ":leader_troop_id", slot_troop_banner_scene_prop, 1),
						(eq, ":leader_troop_id", "trp_player"),
						(assign, ":banner_troop", ":leader_troop_id"),
					(try_end),
				(else_try), #Check if we are in a tavern
					(eq, "$talk_context", tc_tavern_talk),
					(neq, ":troop_no", "trp_player"),
					(assign, ":banner_mesh", "mesh_banners_default_d"),
				(else_try), #can't find party, this can be a town guard
					(neq, ":troop_no", "trp_player"),
					(is_between, "$g_encountered_party", walled_centers_begin, walled_centers_end),
					(party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
					(ge, ":town_lord", 0),
					(assign, ":banner_troop", ":town_lord"),
				(try_end),
				#tom - caravans and crusaders
				(try_begin),
					(neq, ":troop_no", "trp_player"),
			(neg|is_between, ":troop_no", "trp_templar_half_brother", "trp_mercenaries_end"), #not a crusader
					(ge, ":agent_no", 0),
					(agent_get_party_id, ":agent_party", ":agent_no"),
					(ge, ":agent_party", 0),
					(party_get_template_id, ":party_template", ":agent_party"),
					(try_begin),
						(this_or_next|eq, ":party_template", "pt_patrol_party"),
						(eq, ":party_template", "pt_kingdom_caravan_party"),
						(party_get_slot, ":home_center",":agent_party",slot_party_home_center),
						(party_get_slot, ":town_lord", ":home_center", slot_town_lord),
						(ge, ":town_lord", 0),
						(assign, ":banner_troop", ":town_lord"),
			(else_try),
						(eq, ":party_template", "pt_guelphs"),
			(assign, ":banner_mesh", "mesh_banner_a20"),
						(assign, ":banner_troop", -1),
			(else_try),	
						(eq, ":party_template", "pt_ghibellines"),
			(assign, ":banner_mesh", "mesh_banner_a19"),
						(assign, ":banner_troop", -1),
					(else_try),
				#(this_or_next|eq, ":party_template", "pt_teutonic_raiders"),
						(this_or_next|eq, ":party_template", "pt_crusaders"),
						(eq, ":party_template", "pt_crusader_raiders"),
						(store_random_in_range, ":random", 0, 2),
						(assign, ":banner_troop", -1),
						(try_begin),
							(eq,":random", 0),
							(assign, ":banner_mesh", "mesh_banner_f21"),
						(else_try),
							(store_random_in_range, ":banner_mesh", "mesh_banner_x17", "mesh_banner_x19"),
						(try_end),
					(try_end),
				(else_try),
					#(neq, ":troop_no", "trp_player"),
			##freelancing as a crusader #TOM
			(try_begin),
				(eq, ":troop_no", "trp_player"),
				(gt, "$freelancer_state", 0),
			(assign, ":troop_no", "$player_cur_troop"),
			(try_end),
			##TOm end
			(is_between, ":troop_no", "trp_templar_half_brother", "trp_mercenaries_end"), # a crusader
					(try_begin),
						(is_between, ":troop_no", "trp_templar_half_brother", "trp_hospitaller_half_brother"),
			(assign, ":banner_mesh", "mesh_banner_x18"),
			(assign, ":banner_troop", -1),
					(else_try),
						(is_between, ":troop_no", "trp_hospitaller_half_brother", "trp_saint_lazarus_half_brother"),
						(assign, ":banner_mesh", "mesh_banner_x17"),
						(assign, ":banner_troop", -1),
					(else_try),
						(is_between, ":troop_no", "trp_saint_lazarus_half_brother", "trp_santiago_half_brother"),
						(assign, ":banner_mesh", "mesh_banner_o07"),
						(assign, ":banner_troop", -1),
					(else_try),
						(is_between, ":troop_no", "trp_santiago_half_brother", "trp_calatrava_half_brother"),
						(assign, ":banner_mesh", "mesh_banner_e21"),
						(assign, ":banner_troop", -1),
					(else_try),
						(is_between, ":troop_no", "trp_calatrava_half_brother", "trp_saint_thomas_half_brother"),
						(assign, ":banner_mesh", "mesh_banner_e18"),
						(assign, ":banner_troop", -1),
					(else_try),
						(is_between, ":troop_no", "trp_saint_thomas_half_brother", "trp_varangian_guard"),
						(assign, ":banner_mesh", "mesh_banner_o08"),
						(assign, ":banner_troop", -1),
					(try_end),
				(try_end),
				#tom
				(try_begin),
					(ge, ":banner_troop", 0),
					(try_begin),
						(neg|troop_slot_ge, ":banner_troop", slot_troop_banner_scene_prop, 1),
						(assign, ":banner_mesh", "mesh_banners_default_b"),
					(else_try),
						(troop_get_slot, ":banner_spr", ":banner_troop", slot_troop_banner_scene_prop),
						(store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
						(is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
						(val_sub, ":banner_spr", banner_scene_props_begin),
						(store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),
					(try_end),
				(try_end),
				(assign, reg0, ":banner_mesh"),
		])


		# script_get_troop_custom_banner_num_positionings
		# Input: arg1 = troop_no
		# Output: reg0 = num_positionings
get_troop_custom_banner_num_positionings = (
	"get_troop_custom_banner_num_positionings",
			[
				(store_script_param, ":troop_no", 1),
				(troop_get_slot, ":num_charges", ":troop_no", slot_troop_custom_banner_num_charges),
				(try_begin),
					(eq, ":num_charges", 1),
					(assign, ":num_positionings", 2),
				(else_try),
					(eq, ":num_charges", 2),
					(assign, ":num_positionings", 4),
				(else_try),
					(eq, ":num_charges", 3),
					(assign, ":num_positionings", 6),
				(else_try),
					(assign, ":num_positionings", 2),
				(try_end),
				(assign, reg0, ":num_positionings"),
		])
		

		# script_get_custom_banner_charge_type_position_scale_color
		# Input: arg1 = troop_no, arg2 = positioning_index
		# Output: reg0 = type_1
		#         reg1 = scale_1
		#         reg2 = color_1
		#         reg3 = type_2
		#         reg4 = scale_2
		#         reg5 = color_2
		#         reg6 = type_3
		#         reg7 = scale_3
		#         reg8 = color_3
		#         reg9 = type_4
		#         reg10 = scale_4
		#         reg11 = color_4
get_custom_banner_charge_type_position_scale_color = (
	"get_custom_banner_charge_type_position_scale_color",
			[
				(store_script_param, ":troop_no", 1),
				(store_script_param, ":positioning", 2),
				(troop_get_slot, ":num_charges", ":troop_no", slot_troop_custom_banner_num_charges),
				(init_position, pos0),
				(init_position, pos1),
				(init_position, pos2),
				(init_position, pos3),
				
				(troop_get_slot, reg0, ":troop_no", slot_troop_custom_banner_charge_type_1),
				(val_add, reg0, custom_banner_charges_begin),
				(troop_get_slot, reg2, ":troop_no", slot_troop_custom_banner_charge_color_1),
				(troop_get_slot, reg3, ":troop_no", slot_troop_custom_banner_charge_type_2),
				(val_add, reg3, custom_banner_charges_begin),
				(troop_get_slot, reg5, ":troop_no", slot_troop_custom_banner_charge_color_2),
				(troop_get_slot, reg6, ":troop_no", slot_troop_custom_banner_charge_type_3),
				(val_add, reg6, custom_banner_charges_begin),
				(troop_get_slot, reg8, ":troop_no", slot_troop_custom_banner_charge_color_3),
				(troop_get_slot, reg9, ":troop_no", slot_troop_custom_banner_charge_type_4),
				(val_add, reg9, custom_banner_charges_begin),
				(troop_get_slot, reg11, ":troop_no", slot_troop_custom_banner_charge_color_4),
				
				(try_begin),
					(eq, ":num_charges", 1),
					(try_begin),
						(eq, ":positioning", 0),
						(assign, reg1, 100),
					(else_try),
						(assign, reg1, 50),
					(try_end),
				(else_try),
					(eq, ":num_charges", 2),
					(try_begin),
						(eq, ":positioning", 0),
						(position_set_y, pos0, 25),
						(position_set_y, pos1, -25),
						(assign, reg1, 40),
						(assign, reg4, 40),
					(else_try),
						(eq, ":positioning", 1),
						(position_set_x, pos0, -25),
						(position_set_x, pos1, 25),
						(assign, reg1, 40),
						(assign, reg4, 40),
					(else_try),
						(eq, ":positioning", 2),
						(position_set_x, pos0, -25),
						(position_set_y, pos0, 25),
						(position_set_x, pos1, 25),
						(position_set_y, pos1, -25),
						(assign, reg1, 50),
						(assign, reg4, 50),
					(else_try),
						(position_set_x, pos0, -25),
						(position_set_y, pos0, -25),
						(position_set_x, pos1, 25),
						(position_set_y, pos1, 25),
						(assign, reg1, 50),
						(assign, reg4, 50),
					(try_end),
				(else_try),
					(eq, ":num_charges", 3),
					(try_begin),
						(eq, ":positioning", 0),
						(position_set_y, pos0, 33),
						(position_set_y, pos2, -33),
						(assign, reg1, 30),
						(assign, reg4, 30),
						(assign, reg7, 30),
					(else_try),
						(eq, ":positioning", 1),
						(position_set_x, pos0, -33),
						(position_set_x, pos2, 33),
						(assign, reg1, 30),
						(assign, reg4, 30),
						(assign, reg7, 30),
					(else_try),
						(eq, ":positioning", 2),
						(position_set_x, pos0, -30),
						(position_set_y, pos0, 30),
						(position_set_x, pos2, 30),
						(position_set_y, pos2, -30),
						(assign, reg1, 35),
						(assign, reg4, 35),
						(assign, reg7, 35),
					(else_try),
						(eq, ":positioning", 3),
						(position_set_x, pos0, -30),
						(position_set_y, pos0, -30),
						(position_set_x, pos2, 30),
						(position_set_y, pos2, 30),
						(assign, reg1, 35),
						(assign, reg4, 35),
						(assign, reg7, 35),
					(else_try),
						(eq, ":positioning", 4),
						(position_set_x, pos0, -25),
						(position_set_y, pos0, -25),
						(position_set_y, pos1, 25),
						(position_set_x, pos2, 25),
						(position_set_y, pos2, -25),
						(assign, reg1, 50),
						(assign, reg4, 50),
						(assign, reg7, 50),
					(else_try),
						(position_set_x, pos0, -25),
						(position_set_y, pos0, 25),
						(position_set_y, pos1, -25),
						(position_set_x, pos2, 25),
						(position_set_y, pos2, 25),
						(assign, reg1, 50),
						(assign, reg4, 50),
						(assign, reg7, 50),
					(try_end),
				(else_try),
					(try_begin),
						(eq, ":positioning", 0),
						(position_set_x, pos0, -25),
						(position_set_y, pos0, 25),
						(position_set_x, pos1, 25),
						(position_set_y, pos1, 25),
						(position_set_x, pos2, -25),
						(position_set_y, pos2, -25),
						(position_set_x, pos3, 25),
						(position_set_y, pos3, -25),
						(assign, reg1, 50),
						(assign, reg4, 50),
						(assign, reg7, 50),
						(assign, reg10, 50),
					(else_try),
						(position_set_y, pos0, 30),
						(position_set_x, pos1, -30),
						(position_set_x, pos2, 30),
						(position_set_y, pos3, -30),
						(assign, reg1, 35),
						(assign, reg4, 35),
						(assign, reg7, 35),
						(assign, reg10, 35),
					(try_end),
				(try_end),
		])
		
		# script_get_custom_banner_color_from_index
		# Input: arg1 = color_index
		# Output: reg0 = color
get_custom_banner_color_from_index = (
	"get_custom_banner_color_from_index",
			[
				(store_script_param, ":color_index", 1),
				
				(assign, ":cur_color", 0xFF000000),
				(assign, ":red", 0x00),
				(assign, ":green", 0x00),
				(assign, ":blue", 0x00),
				(store_mod, ":mod_i_color", ":color_index", 7),
				(try_begin),
					(eq, ":mod_i_color", 0),
					(assign, ":blue", 0xFF),
				(else_try),
					(eq, ":mod_i_color", 1),
					(assign, ":red", 0xEE),
				(else_try),
					(eq, ":mod_i_color", 2),
					(assign, ":red", 0xFB),
					(assign, ":green", 0xAC),
				(else_try),
					(eq, ":mod_i_color", 3),
					(assign, ":red", 0x5F),
					(assign, ":blue", 0xFF),
				(else_try),
					(eq, ":mod_i_color", 4),
					(assign, ":red", 0x05),
					(assign, ":green", 0x44),
				(else_try),
					(eq, ":mod_i_color", 5),
					(assign, ":red", 0xEE),
					(assign, ":green", 0xEE),
					(assign, ":blue", 0xEE),
				(else_try),
					(assign, ":red", 0x22),
					(assign, ":green", 0x22),
					(assign, ":blue", 0x22),
				(try_end),
				(store_div, ":cur_tone", ":color_index", 7),
				(store_sub, ":cur_tone", 8, ":cur_tone"),
				(val_mul, ":red", ":cur_tone"),
				(val_div, ":red", 8),
				(val_mul, ":green", ":cur_tone"),
				(val_div, ":green", 8),
				(val_mul, ":blue", ":cur_tone"),
				(val_div, ":blue", 8),
				(val_mul, ":green", 0x100),
				(val_mul, ":red", 0x10000),
				(val_add, ":cur_color", ":blue"),
				(val_add, ":cur_color", ":green"),
				(val_add, ":cur_color", ":red"),
				(assign, reg0, ":cur_color"),
		])
		