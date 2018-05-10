from header import *

# deathcam #############################
	# script_dmod_cycle_forwards
	# Output: New $dmod_current_agent
	# Used to cycle forwards through valid agents
dmod_cycle_forwards= (
	"dmod_cycle_forwards",
		[
		
		(assign, ":agent_moved", 0),
		(assign, ":first_agent", -1),
		(get_player_agent_no, ":player_agent"),
		#(agent_get_team, ":player_team", ":player_agent"),
		
		(try_for_agents, ":agent_no"),
			(ge, ":agent_no", 0),
			(neq, ":agent_moved", 1),
			(neq, ":agent_no", ":player_agent"),
			(agent_is_human, ":agent_no"),
			(agent_is_alive, ":agent_no"),
			#(agent_get_team, ":cur_team", ":agent_no"),
			#(eq, ":cur_team", ":player_team"), #tom
			#                (agent_get_troop_id, ":agent_troop", ":agent_no"),
			(try_begin),
			(lt, ":first_agent", 0),
			(assign, ":first_agent", ":agent_no"),
			(try_end),
			(gt, ":agent_no", "$dmod_current_agent"),
			(assign, "$dmod_current_agent", ":agent_no"),
			(assign, ":agent_moved", 1),
		(try_end),
		
		(try_begin),
			(eq, ":agent_moved", 0),
			(neq, ":first_agent", -1),
			(assign, "$dmod_current_agent", ":first_agent"),
			(assign, ":agent_moved", 1),
		(else_try),
			(eq, ":agent_moved", 0),
			(eq, ":first_agent", -1),
			(display_message, "@No Troops Left."),
		(try_end),
		
		(try_begin),
			(eq, ":agent_moved", 1),
			(str_store_agent_name, 1, "$dmod_current_agent"),
			(display_message, "@Selected Troop: {s1}"),
		(try_end),
		(assign, "$dmod_move_camera", 1),
	])
	
	# script_dmod_cycle_backwards
	# Output: New $dmod_current_agent
	# Used to cycle backwards through valid agents
dmod_cycle_backwards= (
	"dmod_cycle_backwards",[
		
		(assign, ":new_agent", -1),
		(assign, ":last_agent", -1),
		(get_player_agent_no, ":player_agent"),
		#(agent_get_team, ":player_team", ":player_agent"),
		
		(try_for_agents, ":agent_no"),
			(gt, ":agent_no", -1),
			(neq, ":agent_no", ":player_agent"),
			(agent_is_human, ":agent_no"),
			(agent_is_alive, ":agent_no"),
			#(agent_get_team, ":cur_team", ":agent_no"),
			#(eq, ":cur_team", ":player_team"), #tom
			#               (agent_get_troop_id, ":agent_troop", ":agent_no"),
			(assign, ":last_agent", ":agent_no"),
			(lt, ":agent_no", "$dmod_current_agent"),
			(assign, ":new_agent", ":agent_no"),
		(try_end),
		
		(try_begin),
			(eq, ":new_agent", -1),
			(neq, ":last_agent", -1),
			(assign, ":new_agent", ":last_agent"),
		(else_try),
			(eq, ":new_agent", -1),
			(eq, ":last_agent", -1),
			(display_message, "@No Troops Left."),
		(try_end),
		
		(try_begin),
			(neq, ":new_agent", -1),
			(assign, "$dmod_current_agent", ":new_agent"),
			(str_store_agent_name, 1, "$dmod_current_agent"),
			(display_message, "@Selected Troop: {s1}"),
		(try_end),
		(assign, "$dmod_move_camera", 1),
	])
	