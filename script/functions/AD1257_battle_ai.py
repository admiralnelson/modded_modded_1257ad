from header import *
# script_get_closest_enemy_distance - tom
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: agent to find from
		# Output: reg1: distance in cms, reg4 glosest agent
get_closest_enemy_distance =	(
	"get_closest_enemy_distance",
			[
			(store_script_param, ":input_agent", 1),
			
			(assign, ":min_distance", 100000),
			(assign, ":closest_agent", -1), #tom
			
			(agent_get_position, pos1, ":input_agent"),
			(agent_get_team, ":team_no", ":input_agent"),
			(try_for_agents,":cur_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_active, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(lt, ":cur_dist", ":min_distance"),
				(assign, ":min_distance", ":cur_dist"),
				(assign, ":closest_agent", ":cur_agent"),
			(try_end),
			
			(assign, reg1, ":min_distance"),
			(assign, reg4, ":closest_agent"), #tom
		])
		
		# script_get_first_closest_enemy_distance - tom
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: agent to find from
		# Output: reg1: distance in cms, reg4 glosest agent
get_first_closest_enemy_distance =	(
	"get_first_closest_enemy_distance",
			[
			(store_script_param, ":input_agent", 1),
			(store_script_param, ":team_no", 2),
			(store_script_param, ":minimum_distance", 3),
			
			(assign, ":min_distance", 100000),
			(assign, ":closest_agent", -1), #tom
			
			(agent_get_position, pos1, ":input_agent"),
			(try_for_agents,":cur_agent"),
				(gt, ":min_distance", ":minimum_distance"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_active, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(lt, ":cur_dist", ":min_distance"),
				(assign, ":closest_agent", ":cur_agent"),
				(assign, ":min_distance", ":cur_dist"),
			(try_end),
			
			(assign, reg1, ":min_distance"),
			(assign, reg4, ":closest_agent"), #tom
		])
		
		# script_get_closest_enemy_distance_new - tom
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: agent to find from, team, minimum distance in cms to find
		# Output: reg1: distance in cms, reg4 glosest agent
get_closest_enemy_distance_new =	(
	"get_closest_enemy_distance_new",
			[
			(store_script_param, ":input_agent", 1),
			(store_script_param, ":team_no", 2),
			(store_script_param, ":minimum_distance", 3),
			
			(assign, ":min_distance", 100000),
			
			(agent_get_position, pos1, ":input_agent"),
			(try_for_agents,":cur_agent"),
				(gt, ":min_distance", ":minimum_distance"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_active, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(lt, ":cur_dist", ":min_distance"),
				(assign, ":min_distance", ":cur_dist"),
			(try_end),
			
			(assign, reg1, ":min_distance"),
		])

