from header import *

##script_tom_agent_skirmish
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		##description: sets the agent to skirmish
		###input: agent, closest_agent id, nearest_enemy, radius, skrimish_start, skrimish_angle
		###output: none
tom_agent_skirmish = (
	"tom_agent_skirmish",
			[
			(store_script_param, ":agent", 1),
			(store_script_param, ":closest_agent", 2),
			(store_script_param, ":nearest_enemy", 3),
			(store_script_param, ":radious", 4), #8500 
			(store_script_param, ":skrimish_start", 5), #9000
			(store_script_param, ":skrimish_angle", 6), #12
			 
				(try_begin),
					(assign, ":r", ":radious"), #50m. 8500
				(gt, ":closest_agent", 0),
			
				(agent_get_position,pos0,":agent"),
				(agent_get_position,pos1,":closest_agent"),
			
				(agent_get_slot, ":direction",":agent", slot_agent_direction),
				(agent_get_slot, ":rotation",":agent", slot_agent_rotation), #slot -random for now
				(try_begin),
					(eq, ":direction", 0),
					(store_random_in_range, ":direction", 1, 3),
					(agent_set_slot, ":agent", slot_agent_direction, ":direction"),
				(try_end),
				(try_begin),
					(le, ":nearest_enemy", ":skrimish_start"), #when the enemy is close enough, rotate
					(val_add, ":rotation", ":skrimish_angle"), #12
						(try_begin),
						(ge, ":rotation", 360),
						(assign, ":rotation", 0),
					(try_end),
				(agent_set_slot, ":agent", slot_agent_rotation, ":rotation"),
				(try_begin),
					(eq, ":direction", 1),
					(val_mul, ":rotation", -1),
					(val_sub, ":r", 1500),
				(try_end),
					
					(position_get_rotation_around_z, reg1,pos1),
					(store_sub, reg0, 360, reg1), 
					(val_add, ":rotation", reg0),
					(position_rotate_z, pos1, ":rotation"), 
					(position_move_x, pos1, ":r", 0),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(agent_set_slot, ":agent", slot_agent_scripted_mode, 1),
				(else_try),
					(agent_clear_scripted_mode, ":agent"),
				(agent_set_slot, ":agent", slot_agent_scripted_mode, 0),
				(try_end),
				#(agent_force_rethink, ":agent"),
			(try_end),
			])