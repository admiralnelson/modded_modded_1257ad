from header import *


# #Utilities used by formations
	# script_point_y_toward_position by motomataru
	# Input: from position, to position
	# Output: reg0 fixed point distance
point_y_toward_position =	(
	"point_y_toward_position", [
	(store_script_param, ":from_position", 1),
	(store_script_param, ":to_position", 2),
	(position_get_x, ":dist_x_to_cosine", ":to_position"),
	(position_get_x, ":from_coord", ":from_position"),
	(val_sub, ":dist_x_to_cosine", ":from_coord"),
	(store_mul, ":sum_square", ":dist_x_to_cosine", ":dist_x_to_cosine"),
	(position_get_y, ":dist_y_to_sine", ":to_position"),
	(position_get_y, ":from_coord", ":from_position"),
	(val_sub, ":dist_y_to_sine", ":from_coord"),
	(store_mul, reg0, ":dist_y_to_sine", ":dist_y_to_sine"),
	(val_add, ":sum_square", reg0),
	(convert_from_fixed_point, ":sum_square"),
	(store_sqrt, ":distance_between", ":sum_square"),
	(convert_to_fixed_point, ":dist_x_to_cosine"),
	(val_div, ":dist_x_to_cosine", ":distance_between"),
	(convert_to_fixed_point, ":dist_y_to_sine"),
	(val_div, ":dist_y_to_sine", ":distance_between"),
	(try_begin),
		(lt, ":dist_x_to_cosine", 0),
		(assign, ":bound_a", 90),
		(assign, ":bound_b", 270),
		(assign, ":theta", 180),
	(else_try),
		(assign, ":bound_a", 90),
		(assign, ":bound_b", -90),
		(assign, ":theta", 0),
	(try_end),
	(assign, ":sine_theta", 0),	#avoid error on compile
	(convert_to_fixed_point, ":theta"),
	(convert_to_fixed_point, ":bound_a"),
	(convert_to_fixed_point, ":bound_b"),
	(try_for_range, reg0, 0, 6),	#precision 90/2exp6 (around 2 degrees)
		(store_sin, ":sine_theta", ":theta"),
		(try_begin),
			(gt, ":sine_theta", ":dist_y_to_sine"),
			(assign, ":bound_a", ":theta"),
		(else_try),
			(lt, ":sine_theta", ":dist_y_to_sine"),
			(assign, ":bound_b", ":theta"),
		(try_end),
		(store_add, ":angle_sum", ":bound_b", ":bound_a"),
		(store_div, ":theta", ":angle_sum", 2),
	(try_end),
	(convert_from_fixed_point, ":theta"),
	(position_get_rotation_around_z, reg0, ":from_position"),
	(val_sub, ":theta", reg0),
	(val_sub, ":theta", 90),	#point y-axis at destination
	(position_rotate_z, ":from_position", ":theta"),
	(assign, reg0, ":distance_between"),
	])

	# script_store_battlegroup_type by Caba'drin   ##NEEDS EDIT per PMs with moto
	# Input: team, division
	# Output: reg0 and slot_team_dx_type with sdt_* value
	# Automatically called from store_battlegroup_data
store_battlegroup_type =	(
	"store_battlegroup_type", [
		(store_script_param_1, ":fteam"),
	(store_script_param_2, ":fdivision"),
	
	#hard-code the traditional three
	(try_begin),
		(eq, ":fdivision", grc_infantry),
		(assign, ":div_type", sdt_infantry),
	(else_try),
		(eq, ":fdivision", grc_archers),
		(assign, ":div_type", sdt_archer),
	(else_try),
		(eq, ":fdivision", grc_cavalry),
		(assign, ":div_type", sdt_cavalry),
		
	#attempt to type the rest
	(else_try),
		(assign, ":count_infantry", 0),
		(assign, ":count_archer", 0),
		(assign, ":count_cavalry", 0),
		(assign, ":count_harcher", 0),
		(assign, ":count_polearms", 0),
		(assign, ":count_skirmish", 0),
		(assign, ":count_support", 0),
		(assign, ":count_bodyguard", 0),	

		(try_for_agents, ":cur_agent"),
			(agent_is_alive, ":cur_agent"),      
			(agent_is_human, ":cur_agent"), 
			(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
			(agent_get_team, ":bgteam", ":cur_agent"),
			(eq, ":bgteam", ":fteam"),
			#(call_script, "script_classify_agent", ":cur_agent"),
			#(assign, ":bgroup", reg0),
			(team_get_leader, ":leader", ":fteam"),
			(neq, ":leader", ":cur_agent"),
			(agent_get_division, ":bgroup", ":cur_agent"),
			(eq, ":bgroup", ":fdivision"),
			(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
			(agent_get_wielded_item, reg0, ":cur_agent", 0),
			
			(try_begin),
				(lt, reg0, 0),
				(assign, ":cur_weapon_type", 0),
			(else_try),
				(item_get_type, ":cur_weapon_type", reg0), 
			(try_end),
			
			(try_begin),
				(neg|troop_is_hero, ":cur_troop"),
				(try_begin), #Cavalry	
					(agent_get_horse, reg0, ":cur_agent"),
					(ge, reg0, 0),
					(try_begin),				
						(gt, ":cur_ammo", 0),
						(val_add, ":count_harcher", 1),
					(else_try),
						(val_add, ":count_cavalry", 1),
					(try_end),
				(else_try), #Archers
					(gt, ":cur_ammo", 0),
					(try_begin),
						(eq, ":cur_weapon_type", itp_type_thrown),
						(val_add, ":count_skirmish", 1),
					(else_try),
						(val_add, ":count_archer", 1),
					(try_end),
				(else_try), #Infantry
					(try_begin),
						(eq, ":cur_weapon_type", itp_type_polearm),
						(val_add, ":count_polearms", 1),
					(else_try),
						(val_add, ":count_infantry", 1),
					(try_end),			    
				(try_end),
			(else_try), #Heroes
				(assign, ":support_skills", 0), #OPEN TO SUGGESTIONS HERE    ?skl_trade, skl_spotting, skl_pathfinding, skl_tracking?
				(store_skill_level, reg0, skl_engineer, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_first_aid, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_surgery, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_wound_treatment, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(try_begin),
					(gt, ":support_skills", 5),
					(val_add, ":count_support", 1),
				(else_try),
					(val_add, ":count_bodyguard", 1),
				(try_end),		
			(try_end), #Regular v Hero		
		(try_end), #Agent Loop	
			
		#Do Comparisons With Counts, set ":div_type"
		(assign, ":slot", slot_team_d0_type),
		(team_set_slot, 7, ":slot", ":count_infantry"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_archer"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_cavalry"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_polearms"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_skirmish"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_harcher"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_support"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_bodyguard"),

		(assign, ":count_to_beat", 0),
		(assign, ":count_total", 0),
		(try_for_range, ":type", sdt_infantry, sdt_infantry + 8), #only 8 sdt_types at the moment
			(store_add, ":slot", slot_team_d0_type, ":type"),
			(team_get_slot, ":count", 7, ":slot"),
			(val_add, ":count_total", ":count"),
			(lt, ":count_to_beat", ":count"),
			(assign, ":count_to_beat", ":count"),
			(assign, ":div_type", ":type"),
		(try_end),
		
		(val_mul, ":count_to_beat", 2),
		(try_begin),
			(lt, ":count_to_beat", ":count_total"), #Less than half of this division
			(assign, ":count_to_beat", 0),
			(assign, ":div_type", -1),
			(try_for_range, ":type", sdt_infantry, sdt_infantry + 3), #check main types for a majority
				(store_add, ":slot", slot_team_d0_type, ":type"),
				(team_get_slot, ":count", 7, ":slot"),
				(val_add, ":slot", 3),	#subtype is three more than main type
				(team_get_slot, reg0, 7, ":slot"),
				(val_add, ":count", reg0),
				(lt, ":count_to_beat", ":count"),
				(assign, ":count_to_beat", ":count"),
				(assign, ":div_type", ":type"),
			(try_end),
		
			(val_mul, ":count_to_beat", 2),
			(lt, ":count_to_beat", ":count_total"), #Less than half of this division
			(assign, ":div_type", sdt_unknown), #Or 0
		(try_end),
	(try_end),	#divisions 3-8
	
	(store_add, ":slot", slot_team_d0_type, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":div_type"),
	(assign, reg0, ":div_type"),  
	])

	
	# script_team_get_position_of_enemies by motomataru
	# Input: destination position, team, troop class/division
	# Output: destination position: average position if reg0 > 0
	#			reg0: number of enemies
	# WARNING: Run script_store_battlegroup_data before calling!
team_get_position_of_enemies =	(
	"team_get_position_of_enemies", [
	(store_script_param, ":enemy_position", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":troop_type", 3),
	(assign, ":pos_x", 0),
	(assign, ":pos_y", 0),
	(assign, ":total_size", 0),
	
	(try_for_range, ":other_team", 0, 4),
		(teams_are_enemies, ":other_team", ":team_no"),
		(try_begin),
			(eq, ":troop_type", grc_everyone),
			(team_get_slot, ":team_size", ":other_team", slot_team_size),
			(try_begin),
				(gt, ":team_size", 0),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", grc_everyone),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(else_try),	#MOTO: this doesn't work -- for multiple divisions, should find the CLOSEST of a given type
			(assign, ":team_size", 0),
			(try_for_range, ":enemy_battle_group", 0, 9),
				(eq, ":enemy_battle_group", ":troop_type"),
				(store_add, ":slot", slot_team_d0_size, ":troop_type"),
							(team_get_slot, ":troop_count", ":other_team", ":slot"),
				(gt, ":troop_count", 0),
				(val_add, ":team_size", ":troop_count"),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", ":troop_type"),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(try_end),
		(val_add, ":total_size", ":team_size"),
	(try_end),
	
	(try_begin),
		(eq, ":total_size", 0),
		(init_position, ":enemy_position"),
	(else_try),
		(val_div, ":pos_x", ":total_size"),
		(position_set_x, ":enemy_position", ":pos_x"),
		(val_div, ":pos_y", ":total_size"),
		(position_set_y, ":enemy_position", ":pos_y"),
		(position_set_z_to_ground_level, ":enemy_position"),
	(try_end),

	(assign, reg0, ":total_size"),
	])

			
	# script_get_nearest_enemy_battlegroup_location by motomataru
	# Input: destination position, fron team, from position
	# Output:	destination position, reg0 with distance
	# Run script_store_battlegroup_data before calling!
get_nearest_enemy_battlegroup_location =  (
	"get_nearest_enemy_battlegroup_location", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":from_pos", 3),
	(assign, ":distance_to_nearest_enemy_battlegoup", Far_Away),
	(try_for_range, ":enemy_team_no", 0, 4),
		(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
		(teams_are_enemies, ":enemy_team_no", ":team_no"),
		(try_for_range, ":enemy_battle_group", 0, 9),
			(store_add, ":slot", slot_team_d0_size, ":enemy_battle_group"),
			(team_slot_ge, ":enemy_team_no", ":slot", 1),
			(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_battle_group"),
			(get_distance_between_positions, reg0, pos0, ":from_pos"),
			(try_begin),
				(gt, ":distance_to_nearest_enemy_battlegoup", reg0),
				(assign, ":distance_to_nearest_enemy_battlegoup", reg0),
				(copy_position, ":bgposition", pos0),
			(try_end),
		(try_end),
	(try_end),
	(assign, reg0, ":distance_to_nearest_enemy_battlegoup")
	])