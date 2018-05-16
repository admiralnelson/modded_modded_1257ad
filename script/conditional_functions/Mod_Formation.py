from header import *

	# script_cf_battlegroup_valid_formation by Caba'drin
	# Input: team, division, formation
	# Output: reg0: troop count/1 if too few troops/0 if wrong type
cf_battlegroup_valid_formation = (
	"cf_battlegroup_valid_formation", [
		(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fformation", 3),
	
	(assign, ":valid_type", 0),
	(store_add, ":slot", slot_team_d0_type, ":fdivision"),
	(team_get_slot, ":sd_type", ":fteam", ":slot"),
	(try_begin), #Eventually make this more complex with the sub-divisions
		(this_or_next|eq, ":sd_type", sdt_cavalry),
		(eq, ":sd_type", sdt_harcher),
		(assign, ":size_minimum", formation_min_cavalry_troops),
		(try_begin),
			(eq, ":fformation", formation_wedge),
			(assign, ":valid_type", 1),
		(try_end),
	(else_try),
		(eq, ":sd_type", sdt_archer),
		(assign, ":size_minimum", formation_min_foot_troops),
		(try_begin),
			(this_or_next|eq, ":fformation", formation_ranks),
			(eq, ":fformation", formation_default),
			(assign, ":valid_type", 1),
		(try_end),
	(else_try),
		(assign, ":size_minimum", formation_min_foot_troops),
		(neq, ":fformation", formation_none),
		(assign, ":valid_type", 1), #all types valid
	(try_end),
	
	(try_begin),
			(eq, ":valid_type", 0),
		(assign, ":num_troops", 0),
	(else_try),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
			(team_get_slot, ":num_troops", ":fteam", ":slot"),
			(le, ":num_troops", ":size_minimum"),
		(assign, ":num_troops", 1),
	(try_end),
	
	(assign, reg0, ":num_troops"),
	(gt, ":num_troops", 1),
	])

	# script_cf_valid_formation_member by motomataru #CABA - Modified for Classify_agent phase out
	# Input: team, division, agent number of team leader, test agent
	# Output: failure indicates agent is not member of formation
cf_valid_formation_member = (
	"cf_valid_formation_member", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":agent", 4),
	(neq, ":fleader", ":agent"),
	(agent_get_division, ":bgroup", ":agent"),
	(eq, ":bgroup", ":fdivision"),
	#(call_script, "script_classify_agent", ":agent"),
	#(eq, reg0, ":fdivision"),
	(agent_get_team, ":team", ":agent"),
	(eq, ":team", ":fteam"),
	(agent_is_alive, ":agent"),
	(agent_is_human, ":agent"),
	(agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
	])

# script_cf_count_casualties by motomataru
	# Input: none
	# Output: evalates T/F, reg0 num casualties
cf_count_casualties =	(
	"cf_count_casualties", [
		(assign, ":num_casualties", 0),
	(try_for_agents,":cur_agent"),
			(try_begin),
			(this_or_next|agent_is_wounded, ":cur_agent"),
			(this_or_next|agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 1),
			(neg|agent_is_alive, ":cur_agent"),
			(val_add, ":num_casualties", 1),
		(try_end),
	(try_end),
	(assign, reg0, ":num_casualties"),
	(gt, ":num_casualties", 0),
	])
	