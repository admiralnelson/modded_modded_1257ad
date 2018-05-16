from header import *

# script_store_battlegroup_data by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
	# Input: none
	# Output: sets positions and globals to track data on ALL groups in a battle
	# Globals used: pos1, reg0, reg1, #CABA - NO LONGER USED: positions 24-45
store_battlegroup_data = ("store_battlegroup_data", [
	(assign, ":team0_leader", 0),
	(assign, ":team0_x_leader", 0),
	(assign, ":team0_y_leader", 0),
	(assign, ":team0_level_leader", 0),
	(assign, ":team1_leader", 0),
	(assign, ":team1_x_leader", 0),
	(assign, ":team1_y_leader", 0),
	(assign, ":team1_level_leader", 0),
	(assign, ":team2_leader", 0),
	(assign, ":team2_x_leader", 0),
	(assign, ":team2_y_leader", 0),
	(assign, ":team2_level_leader", 0),
	(assign, ":team3_leader", 0),
	(assign, ":team3_x_leader", 0),
	(assign, ":team3_y_leader", 0),
	(assign, ":team3_level_leader", 0),
	
	#Team Slots reset every mission, like agent slots, but just to be sure for when it gets called during the mission
	(try_for_range, ":team", 0, 4),
			(try_for_range, ":slot", reset_team_stats_begin, reset_team_stats_end), #Those within the "RESET GROUP" in formations_constants
				(team_set_slot, ":team", ":slot", 0),
		(try_end),
		(try_for_range, ":bgroup", 0, 9),
			(store_add, ":slot", slot_team_d0_first_member, ":bgroup"),
			(team_set_slot, ":team", ":slot", -1),
		(try_end),
	(try_end),

	(try_for_agents, ":cur_agent"),
		(agent_is_alive, ":cur_agent"),      
		(agent_is_human, ":cur_agent"), 
		(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
		(agent_get_team, ":bgteam", ":cur_agent"),
		#(call_script, "script_classify_agent", ":cur_agent"),
		#(assign, ":bgroup", reg0),
		(agent_get_division, ":bgroup", ":cur_agent"),
		(try_begin),
			(team_get_leader, ":leader", ":bgteam"),
				(eq, ":leader", ":cur_agent"),
			(assign, ":bgroup", -1),
		(try_end),
		(agent_get_troop_id, ":cur_troop", ":cur_agent"),
		(store_character_level, ":cur_level", ":cur_troop"),
		(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
		(assign, ":cur_weapon_type", 0),
		(assign, ":cur_weapon_length", 0),
		(agent_get_wielded_item, reg0, ":cur_agent", 0),
		(try_begin),
			(gt, reg0, itm_no_item),
			(item_get_type, ":cur_weapon_type", reg0),
			(this_or_next|eq, ":cur_weapon_type", itp_type_one_handed_wpn),
			(this_or_next|eq, ":cur_weapon_type", itp_type_two_handed_wpn),
			(this_or_next|eq, ":cur_weapon_type", itp_type_polearm),
			(eq, ":cur_weapon_type", itp_type_thrown),
			(item_get_slot, ":cur_weapon_length", reg0, slot_item_length),
		(try_end),
		(agent_get_position, pos1, ":cur_agent"),
		(position_get_x, ":x_value", pos1),
		(position_get_y, ":y_value", pos1),
		(try_begin),
				(eq, ":bgroup", -1), #Leaders
			(try_begin),
				(eq, ":bgteam", 0),
				(assign, ":team0_leader", 1),
				(assign, ":team0_x_leader", ":x_value"),
				(assign, ":team0_y_leader", ":y_value"),
				(assign, ":team0_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 1),
				(assign, ":team1_leader", 1),
				(assign, ":team1_x_leader", ":x_value"),
				(assign, ":team1_y_leader", ":y_value"),
				(assign, ":team1_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 2),
				(assign, ":team2_leader", 1),
				(assign, ":team2_x_leader", ":x_value"),
				(assign, ":team2_y_leader", ":y_value"),
				(assign, ":team2_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 3),
				(assign, ":team3_leader", 1),
				(assign, ":team3_x_leader", ":x_value"),
				(assign, ":team3_y_leader", ":y_value"),
				(assign, ":team3_level_leader", ":cur_level"),
			(try_end),
		(else_try),
			(try_begin),	#First Agent
				(store_add, ":slot", slot_team_d0_first_member, ":bgroup"),
				(neg|team_slot_ge, ":bgteam", ":slot", 0),
				(team_set_slot, ":bgteam", ":slot", ":cur_agent"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_size, ":bgroup"), #Division Count
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(try_begin),
				(gt, ":cur_ammo", 0),
				(store_add, ":slot", slot_team_d0_percent_ranged, ":bgroup"), #Division Percentage are Archers
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(else_try),
				(store_add, ":slot", slot_team_d0_low_ammo, ":bgroup"), #Division Running out of Ammo Flag
				(team_set_slot, ":bgteam", ":slot", 1),
			(try_end),
			
			(try_begin),
				(eq, ":cur_weapon_type", itp_type_thrown),
				(store_add, ":slot", slot_team_d0_percent_throwers, ":bgroup"), #Division Percentage are Throwers
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_level, ":bgroup"), #Division Level
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_level"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_weapon_length, ":bgroup"), #Division Weapon Length
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_weapon_length"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_x, ":bgroup"), #Position X
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":x_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_y, ":bgroup"), #Position Y
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":y_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
		(try_end), #Leader vs Regular
	(try_end), #Agent Loop

	#calculate team sizes, sum positions; within calculate battle group averages
	(try_for_range, ":team", 0, 4),
			(assign, ":team_size", 0),
		(assign, ":team_level", 0),
		(assign, ":team_x", 0),
		(assign, ":team_y", 0),
		
		(assign, ":num_infantry", 0),
		(assign, ":num_archers", 0),
		(assign, ":num_cavalry", 0),
		
			(try_for_range, ":division", 0, 9),
				#sum for team averages
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_get_slot, ":division_size", ":team", ":slot"),
			(gt, ":division_size", 0),
			(val_add, ":team_size", ":division_size"),
			
			(store_add, ":slot", slot_team_d0_level, ":division"),
				(team_get_slot, ":division_level", ":team", ":slot"),
			(val_add, ":team_level", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_x, ":division"),
				(team_get_slot, ":division_x", ":team", ":slot"),
			(val_add, ":team_x", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_y, ":division"),
				(team_get_slot, ":division_y", ":team", ":slot"),
			(val_add, ":team_y", ":division_y"),
			
						#calculate battle group averages
			(store_add, ":slot", slot_team_d0_level, ":division"),
			(val_div, ":division_level", ":division_size"),			
			(team_set_slot, ":team", ":slot", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_percent_ranged, ":division"),
			(team_get_slot, ":value", ":team", ":slot"),
			(val_mul, ":value", 100),
			(val_div, ":value", ":division_size"), 
			(team_set_slot, ":team", ":slot", ":value"),	

			(store_add, ":slot", slot_team_d0_percent_throwers, ":division"),
			(team_get_slot, ":value", ":team", ":slot"),
			(val_mul, ":value", 100),
			(val_div, ":value", ":division_size"), 
			(team_set_slot, ":team", ":slot", ":value"),	
		
			(store_add, ":slot", slot_team_d0_weapon_length, ":division"),
				(team_get_slot, ":value", ":team", ":slot"),
			(val_div, ":value", ":division_size"),
			(team_set_slot, ":team", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_x, ":division"),
			(val_div, ":division_x", ":division_size"),
				(team_set_slot, ":team", ":slot", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_y, ":division"),
			(val_div, ":division_y", ":division_size"),
				(team_set_slot, ":team", ":slot", ":division_y"),
			
			#(try_begin),
			#    (lt, ":division", 3), #CABA - This works right now, as only the player has other divisions enabled...NEED TO RECONSIDER LATER
			#    (store_mul, ":team_shift", ":team", 4),
				#    (store_add, ":position_number", Team0_Infantry_Pos, ":team_shift"),
			#    (val_add, ":position_number", ":division"),
			#(else_try),
			#    (store_sub, ":team_shift", ":division", 3),
			#	(store_add, ":position_number", Player_Battle_Group3_Pos, ":team_shift"),
			#(try_end),			    
				#(init_position, ":position_number"), #CABA - REMOVED AUTOMATIC initialization of positions...problem?
			
			#(val_div, ":division_x", ":division_size"),
			#(position_set_x, ":position_number", ":division_x"),
			#(val_div, ":division_y", ":division_size"),
			#(position_set_y, ":position_number", ":division_y"),
			#(position_set_z_to_ground_level, ":position_number"),

			(store_add, ":slot", slot_team_d0_type, ":division"),
			(team_get_slot, reg0, ":team", ":slot"),
			(try_begin),
				(neg|is_between, reg0, 0, 8),	#TODO reset on reinforcements
								(call_script, "script_store_battlegroup_type", ":team", ":division"),
			(try_end),
						(try_begin),
								(this_or_next|eq, reg0, sdt_infantry),
				(eq, reg0, sdt_polearm),
				(val_add, ":num_infantry", ":division_size"),
			(else_try),
					(this_or_next|eq, reg0, sdt_archer),
				(eq, reg0, sdt_skirmisher),
				(val_add, ":num_archers", ":division_size"),
			(else_try),
					(this_or_next|eq, reg0, sdt_cavalry),
				(eq, reg0, sdt_harcher),
				(val_add, ":num_cavalry", ":division_size"),
			(try_end),
		(try_end), #Division Loop
		
		(team_set_slot, ":team", slot_team_num_infantry, ":num_infantry"),
		(team_set_slot, ":team", slot_team_num_archers, ":num_archers"),
		(team_set_slot, ":team", slot_team_num_cavalry, ":num_cavalry"),

		#Team Leader Additions
		(try_begin),
				(eq, ":team", 0),
			(val_add, ":team_size", ":team0_leader"),
			(val_add, ":team_level", ":team0_level_leader"),
			(val_add, ":team_x", ":team0_x_leader"),
			(val_add, ":team_y", ":team0_y_leader"),
		(else_try),
				(eq, ":team", 1),
			(val_add, ":team_size", ":team1_leader"),
			(val_add, ":team_level", ":team1_level_leader"),
			(val_add, ":team_x", ":team1_x_leader"),
			(val_add, ":team_y", ":team1_y_leader"),
		(else_try),
			(eq, ":team", 2),
			(val_add, ":team_size", ":team2_leader"),
			(val_add, ":team_level", ":team2_level_leader"),
			(val_add, ":team_x", ":team2_x_leader"),
			(val_add, ":team_y", ":team2_y_leader"),
		(else_try),
			(eq, ":team", 3),
			(val_add, ":team_size", ":team3_leader"),
			(val_add, ":team_level", ":team3_level_leader"),
			(val_add, ":team_x", ":team3_x_leader"),
			(val_add, ":team_y", ":team3_y_leader"),		
		(try_end),
		
		#calculate team averages 
		(gt, ":team_size", 0),
		(team_set_slot, ":team", slot_team_size, ":team_size"),
		(val_div, ":team_level", ":team_size"),
		(team_set_slot, ":team", slot_team_level, ":team_level"),	
			
		(val_div, ":team_x", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_x, ":team_x"),
		(val_div, ":team_y", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_y, ":team_y"),
		
		#(store_mul, ":team_shift", ":team", 4),
		#(store_add, ":position_number", Team0_Average_Pos, ":team_shift"),
		# (store_add, ":position_number", Team0_Average_Pos, ":team"),
		# (init_position, ":position_number"),		
		# (val_div, ":team_x", ":team_size"),
		# (position_set_x, ":position_number", ":team_x"),
		# (val_div, ":team_y", ":team_size"),
		# (position_set_y, ":position_number", ":team_y"),
		# (position_set_z_to_ground_level, ":position_number"),
	(try_end), #Team Loop
	])