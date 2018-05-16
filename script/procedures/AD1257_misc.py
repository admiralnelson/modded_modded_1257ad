from header import *

	#script_tom_command_cheer
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
tom_command_cheer =	(
	"tom_command_cheer", #tom made
	[
		(get_player_agent_no, ":player"),
		(agent_get_team, ":team", ":player"),
		(try_for_range, ":class", 0, 9),
		(try_begin),
			(class_is_listening_order, ":team", ":class"),
			(try_for_agents, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_is_human, ":agent"),
			(agent_get_class, ":agent_class", ":agent"),
			(eq, ":agent_class", ":class"),
			(agent_get_simple_behavior,":state",":agent"),
			(neq,":state",aisb_melee),
			(agent_play_sound, ":agent", "snd_man_victory"),
			(try_end),
			(assign, ":class", 11),
		(try_end),
	])