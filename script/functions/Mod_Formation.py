from header import *

# script_battlegroup_place_around_leader by motomataru
	# WARNING: some part of this script are disabled.
	# Input: team, division
	# Output: pos61 division position
battlegroup_place_around_leader = (
	"battlegroup_place_around_leader", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(team_get_leader, ":fleader", ":fteam"),
	(try_begin),
		(gt, ":fleader", -1),	#any team members left?
		
		(agent_get_position, pos1, ":fleader"),
		(try_begin),
			(eq, "$autorotate_at_player", 1),
			(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
			(neq, reg0, 0),	#more than 0 enemies still alive?
			(call_script, "script_point_y_toward_position", pos1, pos60),
		(try_end),

		(store_add, ":slot", slot_team_d0_type, ":fdivision"),
		(team_get_slot, ":sd_type", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(team_get_slot, ":fformation", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
	# (assign, reg1, ":sd_type"),
	# (assign, reg0, ":num_troops"),
	# (assign, reg2, ":fteam"),
	# (assign, reg3, ":fdivision"),
	# (position_get_x, reg4, pos1),
	# (position_get_y, reg5, pos1),
	# (assign, reg6, ":fformation"),
	# (display_message, "@Team {reg2} Division {reg3} type {reg1} numbers {reg0} leader at {reg4},{reg5} formation {reg6}"),
		(try_begin),
			(this_or_next|eq, ":sd_type", sdt_cavalry),
			(eq, ":sd_type", sdt_harcher),
			(position_move_x, pos1, "$next_cavalry_place", 0),
			(try_begin),	#handle Native's way of doing things
				(eq, ":fformation", formation_none),
				(try_begin),
					(ge, ":formation_extra_spacing", 0),
					(store_mul, ":troop_space", ":formation_extra_spacing", 133),
					(val_add, ":troop_space", 150),
				(else_try),	#handle Native multi-ranks
					(assign, ":troop_space", 200),
					(val_mul, ":formation_extra_spacing", -1),
					(val_add, ":formation_extra_spacing", 1),
					(val_div, ":num_troops", ":formation_extra_spacing"),
				(try_end),
				(store_mul, ":formation_width", ":num_troops", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(position_move_x, pos1, reg0, 0),	#cavalry set up RIGHT of leader
# (display_message, "@Cavalry move {reg0}"),
				(copy_position, pos61, pos1),
			(else_try),
				(store_mul, ":troop_space", ":formation_extra_spacing", 50),
				(val_add, ":troop_space", formation_minimum_spacing_horse_width),
				(convert_to_fixed_point, ":num_troops"),
				(store_sqrt, ":formation_width", ":num_troops"),
				(val_mul, ":formation_width", ":troop_space"),
				(convert_from_fixed_point, ":formation_width"),
				(val_sub, ":formation_width", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(position_move_x, pos1, reg0, 0),	#cavalry set up RIGHT of leader
# (display_message, "@Cavalry move {reg0}"),
				(copy_position, pos61, pos1),
				(call_script, "script_form_cavalry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing"),
			(try_end),
			(val_add, "$next_cavalry_place", ":formation_width"),
			(val_add, "$next_cavalry_place", formation_minimum_spacing_horse_width),

		(else_try),
			(eq, ":sd_type", sdt_archer),
			(position_move_y, pos1, "$next_archer_place"),	#archers set up FRONT of leader
			(copy_position, pos61, pos1),
			(try_begin),
				(neq, ":fformation", formation_none),
				(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
				(val_mul, reg0, -1),
				(position_move_x, pos1, reg0, 0),
				(call_script, "script_form_archers", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			(try_end),
			(val_add, "$next_archer_place", 500),	#next archers 5m FRONT of these
			
		(else_try),
			(eq, ":sd_type", sdt_skirmisher),
			(position_move_y, pos1, "$next_archer_place"),	#skirmishers set up FRONT of leader
			(copy_position, pos61, pos1),
			(try_begin),
				(neq, ":fformation", formation_none),
				(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
				(position_move_x, pos1, reg0, 0),
				(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			(try_end),
			(val_add, "$next_archer_place", 500),	#next archers 5m FRONT of these
			
		(else_try),
			(position_move_x, pos1, "$next_infantry_place", 0),
			(copy_position, pos61, pos1),
			(try_begin),	#handle Native's way of doing things
				(eq, ":fformation", formation_none),
				(try_begin),
					(ge, ":formation_extra_spacing", 0),
					(store_mul, ":troop_space", ":formation_extra_spacing", 75),	#Native minimum spacing not consistent but less than this
					(val_add, ":troop_space", 100),
				(else_try),	#handle Native multi-ranks
					(assign, ":troop_space", 150),
					(val_mul, ":formation_extra_spacing", -1),
					(val_add, ":formation_extra_spacing", 1),
					(val_div, ":num_troops", ":formation_extra_spacing"),
				(try_end),
				(store_mul, ":formation_width", ":num_troops", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(val_mul, reg0, -1),	#infantry set up LEFT of leader
# (display_message, "@Infantry unformed move {reg0}"),
				(position_move_x, pos61, reg0, 0),
			(else_try),
				(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
				(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
				(store_mul, ":formation_width", 2, reg0),
				(store_mul, ":troop_space", ":formation_extra_spacing", 50),
				(val_add, ":troop_space", formation_minimum_spacing),
				(val_add, ":formation_width", ":troop_space"),
				(val_mul, reg0, -1),	#infantry set up LEFT of leader
# (display_message, "@Infantry formation move {reg0}"),
				(position_move_x, pos61, reg0, 0),
			(try_end),
			(val_sub, "$next_infantry_place", ":formation_width"),	#next infantry 1m LEFT of these
			(val_sub, "$next_infantry_place", 100),
# (assign, reg0, "$next_infantry_place"),
# (display_message, "@Next infantry {reg0}"),
		(try_end),
		
		(store_add, ":slot", slot_team_d0_move_order, ":fdivision"),
		(team_set_slot, ":fteam", ":slot", mordr_hold),
		(set_show_messages, 0),
		(team_get_movement_order, reg0, ":fteam", ":fdivision"),
		(try_begin),
			(neq, reg0, mordr_hold),
			(team_give_order, ":fteam", ":fdivision", mordr_hold),
		(try_end),
		# (team_set_order_position, ":fteam", ":fdivision", pos61),
		(call_script, "script_set_formation_position", ":fteam", ":fdivision", pos61),
		(set_show_messages, 1),
	(try_end),
	])
	
	# script_get_default_formation by motomataru
	# WARNING: some part of this script are disabled.
	# Input: team id
	# Output: reg0 default formation
get_default_formation = (
	"get_default_formation", [
	(store_script_param, ":fteam", 1),
	(team_get_slot, ":ffaction", ":fteam", slot_team_faction),
	(try_begin),
			(this_or_next|eq, ":ffaction", fac_player_supporters_faction),
		(eq, ":ffaction", fac_player_faction),
		(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		(neq, "$players_kingdom", fac_player_supporters_faction),
		(assign, ":ffaction", "$players_kingdom"),
	(try_end),
	(faction_get_slot, ":culture", ":ffaction", slot_faction_culture),
	(try_begin), #wall
		(this_or_next|eq, ":culture", "fac_culture_finnish"),
		(this_or_next|eq, ":culture", "fac_culture_mazovian"),
		(this_or_next|eq, ":culture", "fac_culture_welsh"),
		(this_or_next|eq, ":culture", "fac_culture_rus"),
		(this_or_next|eq, ":culture", "fac_culture_nordic"),
		(this_or_next|eq, ":culture", "fac_culture_baltic"),
		(this_or_next|eq, ":culture", "fac_culture_gaelic"),
		(eq, ":culture", "fac_culture_scotish"),
		(assign, reg0, formation_shield),
	(else_try),
		(this_or_next|eq, ":ffaction", "fac_player_supporters_faction"),
		(this_or_next|is_between, ":ffaction", kingdoms_begin, kingdoms_end),
		(is_between, ":culture", fac_culture_finnish, fac_culture_mongol +1),
		(assign, reg0, formation_ranks),
	(try_end),
	
	#assign default formation
	
	#(call_script, "script_raf_aor_faction_to_region", ":ffaction"),
	# (str_store_faction_name, s21, ":ffaction"),
	# (display_message, "@Faction: {s21}"),
	# (try_begin),
		# (eq, reg0, region_baltic),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_nordic),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_eastern),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_balkan),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_mongol),
		# (assign, reg0, formation_none),
	# (else_try),
		# (eq, reg0, region_european),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_latin),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_teutonic),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_crusaders),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_byzantine),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_andalusian),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_north_african),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_anatolian),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_mamluk),
		# (assign, reg0, formation_ranks),
	# (else_try), #TOM
		# (eq, reg0, region_scot),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, ":ffaction", fac_player_faction),	#independent player
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (assign, reg0, formation_none),	#riffraff don't use formations
	# (try_end),
	])

	# script_formation_current_position by motomataru
	# Input: destination position (not pos0), team, division
	# Output: in destination position
formation_current_position = (
	"formation_current_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fdivision", 3),
	(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
	(team_get_slot, ":first_agent_in_formation", ":fteam", ":slot"),
	(call_script, "script_get_formation_position", pos0, ":fteam", ":fdivision"),
	(try_begin),
		(eq, ":first_agent_in_formation", -1),
		(copy_position, ":fposition", pos0),
	(else_try),
		(agent_get_position, ":fposition", ":first_agent_in_formation"),
		(position_copy_rotation, ":fposition", pos0),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
		(try_begin),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(team_slot_eq, ":fteam", ":slot", sdt_archer),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(team_get_slot, ":fformation", ":fteam", ":slot"),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, ":fposition", reg0, 0),
	(try_end),
	])


	# script_get_centering_amount by motomataru
	# Input: formation type, number of troops, extra spacing
	#        Use formation type formation_default to use script for archer line
	# Output: reg0 number of centimeters to adjust x-position to center formation
get_centering_amount = (
	"get_centering_amount", [
	(store_script_param, ":troop_formation", 1),
	(store_script_param, ":num_troops", 2),
	(store_script_param, ":extra_spacing", 3),
	(store_mul, ":troop_space", ":extra_spacing", 50),
	(val_add, ":troop_space", formation_minimum_spacing),
	(assign, reg0, 0),
	(try_begin),
		(eq, ":troop_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, reg0, ":num_troops"),
		(val_mul, reg0, ":troop_space"),
		(convert_from_fixed_point, reg0),
		(val_sub, reg0, ":troop_space"),
	(else_try),
		(this_or_next|eq, ":troop_formation", formation_ranks),
		(eq, ":troop_formation", formation_shield),
		(store_div, reg0, ":num_troops", 3),
		(try_begin),
			(store_mod, reg1, ":num_troops", 3),
			(eq, reg1, 0),
			(val_sub, reg0, 1),
		(try_end),
		(val_mul, reg0, ":troop_space"),
	(else_try),
		(eq, ":troop_formation", formation_default),	#assume these are archers in a line
		(store_mul, reg0, ":num_troops", ":troop_space"),
	(try_end),
	(val_div, reg0, 2),
	])

# script_formation_move_position by motomataru
	# Input: team, division, formation current position, (1 to advance or -1 to withdraw or 0 to redirect)
	# Output: pos1 (offset for centering)
formation_move_position = (
	"formation_move_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fcurrentpos", 3),
	(store_script_param, ":direction", 4),
	(copy_position, pos1, ":fcurrentpos"),
	(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
	(try_begin),
		(neq, reg0, 0),	#more than 0 enemies still alive?
		(copy_position, pos1, ":fcurrentpos"),	#restore current formation "position"
		(call_script, "script_point_y_toward_position", pos1, pos60),	#record angle from center to enemy
		(assign, ":distance_to_enemy", reg0),
#		(team_get_order_position, pos61, ":fteam", ":fdivision"),
		(call_script, "script_get_formation_position", pos61, ":fteam", ":fdivision"),
		(get_distance_between_positions, ":move_amount", pos1, pos61),	#distance already moving from previous orders
		(val_add, ":move_amount", 1000),
		(try_begin),
			(gt, ":direction", 0),	#moving forward?
			(gt, ":move_amount", ":distance_to_enemy"),
			(assign, ":move_amount", ":distance_to_enemy"),
		(try_end),
		(val_mul, ":move_amount", ":direction"),
		(position_move_y, pos1, ":move_amount", 0),
		(try_begin),
			(lt, ":distance_to_enemy", 1000),	#less than a move away?
			(position_copy_rotation, pos1, pos61),	#avoid rotating formation
		(try_end),
#		(team_set_order_position, ":fteam", ":fdivision", pos1),
		(call_script, "script_set_formation_position", ":fteam", ":fdivision", pos1),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
		(try_begin),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(neg|team_slot_eq, ":fteam", ":slot", sdt_archer),
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(team_get_slot, ":fformation", ":fteam", ":slot"),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, pos1, reg0, 0),
	(try_end),
	])

	# script_get_formation_position by motomataru
	# Input: position, team, troop class
	# Output: input position (pos0 used)
	# Kluge around buggy *_order_position functions for teams 0-3
get_formation_position = (
	"get_formation_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fdivision", 3),
	(init_position, ":fposition"),
	(try_begin),
			(is_between, ":fteam", 0, 4),
		(store_add, ":slot", slot_team_d0_formation_x, ":fdivision"),
		(team_get_slot, ":x", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_y, ":fdivision"),
		(team_get_slot, ":y", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_zrot, ":fdivision"),
		(team_get_slot, ":zrot", ":fteam", ":slot"),
		
		(position_set_x, ":fposition", ":x"),
		(position_set_y, ":fposition", ":y"),
		(position_rotate_z, ":fposition", ":zrot"),
	(else_try), #CABA - When would this ever be called?
		(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
		(team_get_slot, reg0, ":fteam", ":slot"),
		(try_begin),	  # "launder" team_get_order_position shutting down position_move_x
			(gt, reg0, -1),
			(team_get_order_position, ":fposition", ":fteam", ":fdivision"),
			(agent_get_position, pos0, reg0),
			(agent_set_position, reg0, ":fposition"),
			(agent_get_position, ":fposition", reg0),
			(agent_set_position, reg0, pos0),
		(try_end),
	(try_end),
	(position_set_z_to_ground_level, ":fposition"),
	])	

# script_battlegroup_get_position by motomataru #CABA - EDITED TO USE SLOTS, NOT STORED POS NUMBERS
#MOTO need rotation?
	# Input: destination position, team, battle group (troop class)
	# Output:	battle group position
	#			average team position if "troop class" input NOT set to 0-8
	# NB: Assumes that battle groups beyond 2 are PLAYER team
	# Positions 24-45 reserved (!)  NOW none are reserved...all calculated with slots
battlegroup_get_position =	(
	"battlegroup_get_position", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":bgteam", 2),
	(store_script_param, ":bgroup", 3),
	
	(assign, ":x", 0),
	(assign, ":y", 0),
	(init_position, ":bgposition"),
	(try_begin),
		(neg|is_between, ":bgroup", 0, 9),
		(team_slot_ge, ":bgteam", slot_team_size, 1),
		(team_get_slot, ":x", ":bgteam", slot_team_avg_x),
		(team_get_slot, ":y", ":bgteam", slot_team_avg_y),
	(else_try),
		(is_between, ":bgroup", 0, 9),
		(store_add, ":slot", slot_team_d0_size, ":bgroup"),
		(team_slot_ge, ":bgteam", ":slot", 1),
		
		(store_add, ":slot", slot_team_d0_x, ":bgroup"),
		(team_get_slot, ":x", ":bgteam", ":slot"),
		
		(store_add, ":slot", slot_team_d0_y, ":bgroup"),
		(team_get_slot, ":y", ":bgteam", ":slot"),
	(try_end),
	(position_set_x, ":bgposition", ":x"),
	(position_set_y, ":bgposition", ":y"),
	(position_set_z_to_ground_level, ":bgposition"),
	])