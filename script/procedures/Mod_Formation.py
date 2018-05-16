from header import * 

# #Formations Scripts	  
	# script_division_reset_places by motomataru
	# Input: none
	# Output: none
	# Resets globals for placing divisions around player for script_battlegroup_place_around_leader
division_reset_places = (
	"division_reset_places", [
	(assign, "$next_cavalry_place", formation_minimum_spacing_horse_width),	#first spot RIGHT of the player
	(assign, "$next_archer_place", 1000),	#first spot 10m FRONT of the player
	(assign, "$next_infantry_place", -1 * formation_minimum_spacing_horse_width),	#first spot LEFT of the player
	])
	 
	 # script_form_cavalry by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing
	# Output: none
	# Form in wedge, (now not) excluding horse archers
	# Creates formation starting at pos1
form_cavalry = (
	"form_cavalry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":x_distance", formation_minimum_spacing_horse_width, ":extra_space"),
	(store_add, ":y_distance", formation_minimum_spacing_horse_length, ":extra_space"),
	(assign, ":max_level", 0),
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
		(agent_get_troop_id, ":troop_id", ":agent"),
		(store_character_level, ":troop_level", ":troop_id"),
		(gt, ":troop_level", ":max_level"),
		(assign, ":max_level", ":troop_level"),
	(end_try),
	(assign, ":column", 1),
	(assign, ":rank_dimension", 1),
	(store_mul, ":neg_y_distance", ":y_distance", -1),
	(store_mul, ":neg_x_distance", ":x_distance", -1),
	(store_div, ":wedge_adj", ":x_distance", 2),
	(store_div, ":neg_wedge_adj", ":neg_x_distance", 2),
	(val_add, ":max_level", 1),
	(assign, ":form_left", 1),
	(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
		(try_for_agents, ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(eq, ":troop_level", ":rank_level"),				
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_x_distance", 0),
			(else_try),
				(position_move_x, pos1, ":x_distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":rank_dimension"),
			(position_move_y, pos1, ":neg_y_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_wedge_adj", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":wedge_adj", 0),
			(try_end),			
			(assign, ":column", 1),
			(val_add, ":rank_dimension", 1),
		(end_try),
	(end_try),
	])
		 
	# script_form_archers by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing, formation
	# Output: none
	# Form in line, staggered if formation = formation_ranks
	# Creates formation starting at pos1
form_archers = (
	"form_archers", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":archers_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops
	(assign, ":total_move_y", 0),	#staggering variable	
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
		(agent_set_scripted_destination, ":agent", pos1, 1),
		(position_move_x, pos1, ":distance", 0),
		(try_begin),
			(eq, ":archers_formation", formation_ranks),
			(val_add, ":total_move_y", 75),
			(try_begin),
				(le, ":total_move_y", 150),
				(position_move_y, pos1, 75, 0),
			(else_try),
				(position_move_y, pos1, -150, 0),
				(assign, ":total_move_y", 0),
			(try_end),
		(try_end),
	(try_end),
	])
		 
	# script_form_infantry by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing, formation
	# Output: none
	# If input "formation" is formation_default, will select a formation based on faction
	# Creates formation starting at pos1
form_infantry = (
	"form_infantry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":infantry_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops	
	(store_mul, ":neg_distance", ":distance", -1),
	(store_add, ":slot", slot_team_d0_size, ":fdivision"),
	(team_get_slot, ":num_troops", ":fteam", ":slot"),
	(try_begin),
		(eq, ":infantry_formation", formation_default),
		(call_script, "script_get_default_formation", ":fteam"),
		(assign, ":infantry_formation", reg0),
	(try_end),
	(team_get_weapon_usage_order, ":weapon_order", ":fteam", grc_infantry),
	(assign, ":form_left", 1),
	(assign, ":column", 1),
	(assign, ":rank", 1),

	(try_begin),
		(eq, ":infantry_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, ":square_dimension", ":num_troops"),
		(convert_from_fixed_point, ":square_dimension"),
		(val_add, ":square_dimension", 1),

		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),
				(eq, formation_reequip, 1),
				(eq, ":weapon_order", wordr_use_any_weapon),
				(try_begin),
					(this_or_next|eq, ":rank", 1),
					(this_or_next|ge, ":rank", ":square_dimension"),
					(this_or_next|eq, ":column", 1),
					(ge, ":column", ":square_dimension"),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
				(else_try),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(position_move_x, pos1, ":distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":square_dimension"),
			(position_move_y, pos1, ":neg_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":distance", 0),
			(try_end),			
			(assign, ":column", 1),		
			(val_add, ":rank", 1),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_wedge),
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),

		(assign, ":rank_dimension", 1),
		(store_div, ":wedge_adj", ":distance", 2),
		(store_div, ":neg_wedge_adj", ":neg_distance", 2),
		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(try_begin),
						(this_or_next|eq, ":column", 1),
						(ge, ":column", ":rank_dimension"),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
					(else_try),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				(gt, ":column", ":rank_dimension"),
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_wedge_adj", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":wedge_adj", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank_dimension", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_ranks),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),		
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),


		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(try_begin),
						(eq, ":rank", 1),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
					(else_try),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),

				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_shield),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),
		(assign, ":first_second_rank_agent", -1),
		(assign, ":min_len_non_shielded", -1),
		(try_for_range, ":weap_group", 0, 3),
			(store_mul, ":min_len", ":weap_group", Third_Max_Weapon_Length),
			(store_add, ":max_len", ":min_len", Third_Max_Weapon_Length),
			(try_begin),
				(gt, ":min_len_non_shielded", -1),	#looped through agents at least once since rank 2
				(assign, ":min_len_non_shielded", ":min_len"),
			(try_end),
			(try_for_agents, ":agent"),
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
				(try_begin),
					(gt, ":agent_weapon", itm_no_item),
					(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
				(else_try),
					(assign, ":weapon_length", 0),
				(try_end),
				(try_begin),
					(gt, ":rank", 1),
					(try_begin),
						(eq, ":first_second_rank_agent", ":agent"),	#looped through agents at least once since rank 2
						(assign, ":min_len_non_shielded", ":min_len"),
					(else_try),
						(eq, ":first_second_rank_agent", -1),
						(assign, ":first_second_rank_agent", ":agent"),
					(try_end),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(ge, ":weapon_length", ":min_len"),	#avoid reequipping agents that are already in formation
					(eq, ":min_len_non_shielded", -1),	#haven't looped through agents at least once since rank 2
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),	#longest weapon, including two-handed
					(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
					(try_begin),
						(gt, ":agent_weapon", itm_no_item),
						(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
					(else_try),
						(assign, ":weapon_length", 0),
					(try_end),
				(try_end),
				
				(assign, ":form_up", 0),
				(agent_get_wielded_item, ":agent_shield", ":agent", 1),
				(try_begin),
					(gt, ":agent_shield", itm_no_item),
					(item_get_type, reg0, ":agent_shield"),
					(eq, reg0, itp_type_shield),
					(try_begin),
						(is_between, ":weapon_length", ":min_len", ":max_len"),
						(assign, ":form_up", 1),
					(try_end),
				(else_try),
					(gt, ":rank", 1),
					(is_between, ":weapon_length", ":min_len_non_shielded", ":max_len"),
					(assign, ":form_up", 1),
				(try_end),

				(eq, ":form_up", 1),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(eq, ":rank", 1),
					(call_script, "script_equip_best_melee_weapon", ":agent", 1, 0),	#best weapon, force shield
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				
				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(try_end),
		(try_end),
	(try_end),
	])

# script_equip_best_melee_weapon by motomataru
	# WARNING: THIS MIGHT ALSO SOURCE OF GLITCHY SIEGE AI!
	# Input: agent id, flag to force shield, flag to force for length ALONE
	# Output: none
equip_best_melee_weapon = (
	"equip_best_melee_weapon", [
	(store_script_param, ":agent", 1),
	(store_script_param, ":force_shield", 2),
	(store_script_param, ":force_length", 3),

	#priority items
	(assign, ":shield", itm_no_item),
	(assign, ":weapon", itm_no_item),
	(try_for_range, ":item_slot", ek_item_0, ek_head),
		(agent_get_item_slot, ":item", ":agent", ":item_slot"),
		(gt, ":item", itm_no_item),
		(item_get_type, ":weapon_type", ":item"),
		(try_begin),
			(eq, ":weapon_type", itp_type_shield),
			(assign, ":shield", ":item"),
		(else_try),
			(eq, ":weapon_type", itp_type_thrown),
			# (agent_get_ammo, ":ammo", ":agent", 0),	#assume infantry would have no other kind of ranged weapon
			# (gt, ":ammo", 0),
			(assign, ":weapon", ":item"),	#use thrown weapons first
		(try_end),
	(try_end),

	#select weapon
	(try_begin),
		(eq, ":weapon", itm_no_item),
		(assign, ":cur_score", 0),
		(try_for_range, ":item_slot", ek_item_0, ek_head),
			(agent_get_item_slot, ":item", ":agent", ":item_slot"),
			(gt, ":item", itm_no_item),
			(item_get_type, ":weapon_type", ":item"),
			(neq, ":weapon_type", itp_type_shield),

			(item_get_slot, reg0, ":item", slot_item_needs_two_hands),
			(this_or_next|eq, reg0, 0),
			(this_or_next|eq, ":force_shield", 0),
			(eq, ":shield", itm_no_item),
			
			(try_begin),
				(neq, ":force_length", 0),
				(item_get_slot, ":item_length", ":item", slot_item_length),
				(try_begin),
					(lt, ":cur_score", ":item_length"),
					(assign, ":cur_score", ":item_length"),
					(assign, ":weapon", ":item"),
				(try_end),
			(else_try),
				(assign, ":imod", imodbit_plain),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(try_begin),    #only heroes have item modifications
					(troop_is_hero, ":troop_id"),
					(try_for_range, ":troop_item_slot",  ek_item_0, ek_head),    # heroes have only 4 possible weapons (equipped)
						(troop_get_inventory_slot, reg0, ":troop_id", ":troop_item_slot"),  #Find Item Slot with same item ID as Equipped Weapon
						(eq, reg0, ":item"),
						(troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":troop_item_slot"),
					(try_end),
				(try_end), 

				(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
				(lt, ":cur_score", reg0),
				(assign, ":cur_score", reg0),
				(assign, ":weapon", ":item"),
			(try_end),
		(try_end),
	(try_end),

	#equip selected items if needed
	(agent_get_wielded_item, reg0, ":agent", 0),
	(try_begin),
		(neq, reg0, ":weapon"),
		(try_begin),
			(gt, ":shield", itm_no_item),
			(agent_get_wielded_item, reg0, ":agent", 1),
			(neq, reg0, ":shield"),	#reequipping secondary will UNequip (from experience)
			(agent_set_wielded_item, ":agent", ":shield"),
		(try_end),
		(gt, ":weapon", itm_no_item),
		(agent_set_wielded_item, ":agent", ":weapon"),
	(try_end),
	])


	# script_formation_end
	# Input: team, division
	# Output: none
formation_end = (
	"formation_end", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(try_begin),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(neg|team_slot_eq, ":fteam", ":slot", formation_none),
		(team_set_slot, ":fteam", ":slot", formation_none),
		(team_get_leader, ":leader", ":fteam"),
		
		(try_for_agents, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_is_human, ":agent"),
			(agent_get_team, ":team", ":agent"),
			(eq, ":team", ":fteam"),
			(neq, ":leader", ":agent"),
			(agent_get_division, ":bgroup", ":agent"),
			(eq, ":bgroup", ":fdivision"),
			(agent_clear_scripted_mode, ":agent"),
		(try_end),
		
		(try_begin),
			(eq, ":fteam", "$fplayer_team_no"),
			(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			#adjust for differences between the two systems of spreading out
			(set_show_messages, 0),
			(try_begin),
				(gt, ":div_spacing", 3),
				(assign, ":div_spacing", 2),	#Native maximum spread out
			(else_try),
				(gt, ":div_spacing", 0),
				(team_give_order, "$fplayer_team_no", ":fdivision", mordr_stand_closer),
				(try_begin),
					(gt, ":div_spacing", 1),
					(assign, ":div_spacing", 1),
				(else_try),
					(assign, ":div_spacing", 0),
				(try_end),
			(try_end),
			(set_show_messages, 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
		(try_end),
	(try_end),
	])


	# script_set_formation_position by motomataru
	# Input: team, troop class, position
	# Output: none
	# Kluge around buggy *_order_position functions for teams 0-3
set_formation_position = (
	"set_formation_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fposition", 3),
	
	(position_get_x, ":x", ":fposition"),
	(position_get_y, ":y", ":fposition"),
	(position_get_rotation_around_z, ":zrot", ":fposition"),
	
	(store_add, ":slot", slot_team_d0_formation_x, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":x"),	
	(store_add, ":slot", slot_team_d0_formation_y, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":y"),	
	(store_add, ":slot", slot_team_d0_formation_zrot, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":zrot"),
	
	(team_set_order_position, ":fteam", ":fdivision", ":fposition"),
	])	

# #Player team formations functions
	# script_player_attempt_formation
	# Inputs:	arg1: division
	#			arg2: formation identifier (formation_*)
	# Output: none
player_attempt_formation = (
	"player_attempt_formation", [
	(store_script_param, ":fdivision", 1),
	(store_script_param, ":fformation", 2),
	(set_fixed_point_multiplier, 100),
	(try_begin),
		(eq, ":fformation", formation_ranks),
		(str_store_string, s1, "@ranks"),
	(else_try),
		(eq, ":fformation", formation_shield),
		(str_store_string, s1, "@shield wall"),
	(else_try),
		(eq, ":fformation", formation_wedge),
		(str_store_string, s1, "@wedge"),
	(else_try),
		(eq, ":fformation", formation_square),
		(str_store_string, s1, "@square"),
	(else_try),
		(str_store_string, s1, "@up"),
	(try_end),
	(str_store_class_name, s2, ":fdivision"),

	(try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", "$fplayer_team_no", ":fdivision", ":fformation"),
		(try_begin),	#new formation?
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", ":fformation"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":fformation"),
			(display_message, "@{!}{s2} forming {s1}."),
			(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			#bring unformed divisions into sync with formations' minimum
			(set_show_messages, 0),
			(assign, reg0, ":div_spacing"),
			(try_for_range, reg1, reg0, formation_start_spread_out),	#spread out for ease of forming up	
				(team_give_order, "$fplayer_team_no", ":fdivision", mordr_spread_out),
				(val_add, ":div_spacing", 1),
			(try_end),
			(set_show_messages, 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
		(try_end),
		
	(else_try),
		(assign, ":return_val", reg0),
		(call_script, "script_formation_end", "$fplayer_team_no", ":fdivision"),
		(neq, ":fformation", formation_none),
		(try_begin),
			(gt, ":return_val", 0),
			(display_message, "@Not enough troops in {s2} to form {s1}, but holding."),
		(else_try),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(team_get_slot, reg0, "$fplayer_team_no", ":slot"),
			(call_script, "script_str_store_division_type_name", s3, reg0),
			(display_message, "@{!}{s2} is an {s3} division and cannot form {s1}, so is holding."),
		(try_end),
	(try_end),
	(call_script, "script_battlegroup_place_around_leader", "$fplayer_team_no", ":fdivision"),
	])

	# script_str_store_division_type_name by motomataru
	# Input:	destination, division type (sdt_*)
	# Output: none
str_store_division_type_name = (
	"str_store_division_type_name", [
	(store_script_param, ":str_reg", 1),
	(store_script_param, ":division_type", 2),
	(try_begin),
		(eq, ":division_type", sdt_infantry),
		(str_store_string, ":str_reg", "@infantry"),
	(else_try),
		(eq, ":division_type", sdt_archer),
		(str_store_string, ":str_reg", "@archer"),
	(else_try),
		(eq, ":division_type", sdt_cavalry),
		(str_store_string, ":str_reg", "@cavalry"),
	(else_try),
		(eq, ":division_type", sdt_polearm),
		(str_store_string, ":str_reg", "@polearm"),
	(else_try),
		(eq, ":division_type", sdt_skirmisher),
		(str_store_string, ":str_reg", "@skirmisher"),
	(else_try),
		(eq, ":division_type", sdt_harcher),
		(str_store_string, ":str_reg", "@mounted archer"),
	(else_try),
		(eq, ":division_type", sdt_support),
		(str_store_string, ":str_reg", "@support"),
	(else_try),
		(eq, ":division_type", sdt_bodyguard),
		(str_store_string, ":str_reg", "@bodyguard"),
	(else_try),
		(str_store_string, ":str_reg", "@undetermined type of"),
	(try_end),
	])
	
	# script_player_order_formations by motomataru
	# Inputs:	arg1: order to formation (mordr_*)
	# Output: none
player_order_formations = (
	"player_order_formations", [
	(store_script_param, ":forder", 1),
	(set_fixed_point_multiplier, 100),
	
	(try_begin), #On hold, any formations reform in new location		
		(eq, ":forder", mordr_hold),
		(call_script, "script_division_reset_places"),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_size, ":division"),	#apply to all divisions (not just formations)
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation"),
		(try_end),
		
	(else_try),	#Follow is hold	repeated frequently
		(eq, ":forder", mordr_follow),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_size, ":division"),	#apply to all divisions (not just formations)
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),	#update formations
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation"),

			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),
		(try_end),
		
	(else_try),	#charge or retreat ends formation
		(this_or_next|eq, ":forder", mordr_charge),
		(eq, ":forder", mordr_retreat),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(store_add, reg0, ":division", 1),
			(try_begin),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(display_message, "@Division {reg0}: infantry formation disassembled."),
			(else_try),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(display_message, "@Division {reg0}: archer formation disassembled."),
			(else_try),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
				(display_message, "@Division {reg0}: skirmisher formation disassembled."),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(display_message, "@Division {reg0}: cavalry formation disassembled."),
			(else_try),
				(display_message, "@Division {reg0}: formation disassembled."),			
			(try_end),
		(try_end),
		
	(else_try),	#dismount ends formation
		(eq, ":forder", mordr_dismount),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
			(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			(display_message, "@Cavalry formation disassembled."),
				(try_end),
			
	(else_try), 
		(eq, ":forder", mordr_advance),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(try_begin),
				(neq, ":prev_order", mordr_advance),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, 1),

			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
				(try_end),			

	(else_try),
		(eq, ":forder", mordr_fall_back),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(try_begin),
				(neq, ":prev_order", mordr_fall_back),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, -1),			

			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
				(try_end),		

	(else_try),
		(eq, ":forder", mordr_stand_closer),		
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(gt, ":div_spacing", -3),	#Native formations go down to four ranks
			(val_sub, ":div_spacing", 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(try_begin),	#bring unformed divisions into sync with formations' minimum
				(lt, ":div_spacing", 0),
				(set_show_messages, 0),
				(assign, reg0, ":div_spacing"),
				(try_for_range, reg1, reg0, 0),
					(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
					(val_add, ":div_spacing", 1),
				(try_end),
				(set_show_messages, 1),
				(store_add, ":slot", slot_team_d0_formation_space, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
				
			(else_try),
				(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_type, ":division"),
				(try_begin),
					(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
					(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
				(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
					(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
					(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
				(else_try),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
					(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
				(try_end),
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_spread_out),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(try_begin),
				(this_or_next|neq, ":formation", formation_none),
				(lt, ":div_spacing", 2),	#Native maxes at 2
				(val_add, ":div_spacing", 1),
			(try_end),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			
			(neq, ":formation", formation_none),

			#bring unformed divisions into sync with formations' minimum
			(set_show_messages, 0),
			(assign, reg0, ":div_spacing"),
			(try_for_range, reg1, reg0, 1),
				(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
				(val_add, ":div_spacing", 1),
			(try_end),
			(set_show_messages, 1),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),

			(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(store_add, ":slot", slot_team_d0_size, ":division"), 
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"), 
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_stand_ground),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(copy_position, pos1, pos63),		
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(store_add, ":slot", slot_team_d0_size, ":division"),
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),	
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
			(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
		(try_end),			
	(try_end)
	])