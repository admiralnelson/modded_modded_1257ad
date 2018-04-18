from header import *

#script_setup_talk_info
		# INPUT: $g_talk_troop, $g_talk_troop_relation
setup_talk_info	= (
	"setup_talk_info",
			[
				(talk_info_set_relation_bar, "$g_talk_troop_relation"),
				(str_store_troop_name, s61, "$g_talk_troop"),
				(str_store_string, s61, "@{!} {s61}"),
				(assign, reg1, "$g_talk_troop_relation"),
				(str_store_string, s62, "str_relation_reg1"),
				(talk_info_set_line, 0, s61),
				(talk_info_set_line, 1, s62),
				(call_script, "script_describe_relation_to_s63", "$g_talk_troop_relation"),
				(talk_info_set_line, 3, s63),
		])

		#NPC companion changes begin
		#script_setup_talk_info_companions
setup_talk_info_companions	= (
	"setup_talk_info_companions",
			[
				(call_script, "script_npc_morale", "$g_talk_troop"),
				(assign, ":troop_morale", reg0),
				
				(talk_info_set_relation_bar, ":troop_morale"),
				
				(str_store_troop_name, s61, "$g_talk_troop"),
				(str_store_string, s61, "@{!} {s61}"),
				(assign, reg1, ":troop_morale"),
				(str_store_string, s62, "str_morale_reg1"),
				(talk_info_set_line, 0, s61),
				(talk_info_set_line, 1, s62),
				(talk_info_set_line, 3, s63),
		])

		#script_setup_troop_meeting:
		# INPUT:
		# param1: troop_id with which meeting will be made.
		# param2: troop_dna (optional)
		
setup_troop_meeting	= (
	"setup_troop_meeting",
			[
				(store_script_param_1, ":meeting_troop"),
				(store_script_param_2, ":troop_dna"),
				(call_script, "script_get_meeting_scene"),
				(assign, ":meeting_scene", reg0),
				(modify_visitors_at_site,":meeting_scene"),
				(reset_visitors),
				(set_visitor,0,"trp_player"),
				(try_begin),
					(gt, ":troop_dna", -1),
					(set_visitor,17,":meeting_troop",":troop_dna"),
				(else_try),
					(set_visitor,17,":meeting_troop"),
				(try_end),
				(set_jump_mission,"mt_conversation_encounter"),
				(jump_to_scene,":meeting_scene"),
				(change_screen_map_conversation, ":meeting_troop"),
		])