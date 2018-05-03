from header import *

		#script_troop_agent_set_banner
		# INPUT: agent_no
		# OUTPUT: none
troop_agent_set_banner = (
	"troop_agent_set_banner",
			[
				(store_script_param, ":tableau_no",1),
				(store_script_param, ":agent_no", 2),
				(store_script_param, ":troop_no", 3),
				(call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
				(cur_agent_set_banner_tableau_material, ":tableau_no", reg0),
		])

		#script_shield_item_set_banner
		#script_shield_item_set_banner_old
		# INPUT: agent_no
		# OUTPUT: none
shield_item_set_banner_old = (
	"shield_item_set_banner_old",
			[
				(store_script_param, ":tableau_no",1),
				(store_script_param, ":agent_no", 2),
				(store_script_param, ":troop_no", 3),
				(call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
				(cur_item_set_tableau_material, ":tableau_no", reg0),
		])
	
	#script_shield_item_set_banner_new
		# INPUT: agent_no
		# OUTPUT: none
shield_item_set_banner = (
	"shield_item_set_banner",
			[
				(store_script_param, ":tableau_no",1),
				(store_script_param, ":agent_no", 2),
				(store_script_param, ":troop_no", 3),
				#(store_script_param, ":item_no", 4),
		#(agent_get_item_slot, ":item", ":agent_no", 5),
		(try_begin),
			(eq, "$historical_banners", 1),
			(call_script, "script_agent_troop_get_historical_mesh", ":agent_no", ":troop_no"),
		(else_try),  
					(call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
		(try_end),  
				(cur_item_set_tableau_material, ":tableau_no", reg0),
		])
		