from header import *

# script_battle_tactic_init
		# Input: none
		# Output: none
battle_tactic_init = (
	"battle_tactic_init",
			[
				(call_script, "script_battle_tactic_init_aux", "$ai_team_1", "$ai_team_1_battle_tactic"),
				(try_begin),
					(ge, "$ai_team_2", 0),
					(call_script, "script_battle_tactic_init_aux", "$ai_team_2", "$ai_team_2_battle_tactic"),
				(try_end),
				
				(try_for_agents, ":cur_agent"),
					(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0), #initially nobody is running away.
				(try_end),
		])
		
		# script_battle_tactic_init_aux
		# Input: team_no, battle_tactic
		# Output: none
orig_battle_tactic_init_aux = (
	"orig_battle_tactic_init_aux",
			[
				(store_script_param, ":team_no", 1),
				(store_script_param, ":battle_tactic", 2),
				(team_get_leader, ":ai_leader", ":team_no"),
				(try_begin),
					(eq, ":battle_tactic", btactic_hold),
					(agent_get_position, pos1, ":ai_leader"),
					(call_script, "script_find_high_ground_around_pos1", ":team_no", 30),
					(copy_position, pos1, pos52),
					(call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
					(copy_position, pos1, pos52),
					(call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
					(team_give_order, ":team_no", grc_everyone, mordr_hold),
					(team_set_order_position, ":team_no", grc_everyone, pos52),
					(team_give_order, ":team_no", grc_archers, mordr_advance),
					(team_give_order, ":team_no", grc_archers, mordr_advance),
				(else_try),
					(eq, ":battle_tactic", btactic_follow_leader),
					(team_get_leader, ":ai_leader", ":team_no"),
					(ge, ":ai_leader", 0),
					(agent_set_speed_limit, ":ai_leader", 8),
					(agent_get_position, pos60, ":ai_leader"),
					(team_give_order, ":team_no", grc_everyone, mordr_hold),
					(team_set_order_position, ":team_no", grc_everyone, pos60),
				(try_end),
		])
		
		# script_decide_run_away_or_not
		# Input: none
		# Output: none
orig_decide_run_away_or_not = (
		"orig_decide_run_away_or_not",
			[
				(store_script_param, ":cur_agent", 1),
				(store_script_param, ":mission_time", 2),
				
				(assign, ":force_retreat", 0),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(agent_get_division, ":agent_division", ":cur_agent"),
				(try_begin),
					(lt, ":agent_division", 9), #static classes
					(team_get_movement_order, ":agent_movement_order", ":agent_team", ":agent_division"),
					(eq, ":agent_movement_order", mordr_retreat),
					(assign, ":force_retreat", 1),
				(try_end),
				
				(agent_get_slot, ":is_cur_agent_running_away", ":cur_agent", slot_agent_is_running_away),
				(try_begin),
					(eq, ":is_cur_agent_running_away", 0),
					(try_begin),
						(eq, ":force_retreat", 1),
						(agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
						(agent_start_running_away, ":cur_agent"),
						(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
					(else_try),
						(ge, ":mission_time", 45), #first 45 seconds anyone does not run away whatever happens.
						(agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
						(store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
						(val_mul, ":agent_hit_points", 4),
						(try_begin),
							(agent_is_ally, ":cur_agent"),
							(val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
						(try_end),
						(val_mul, ":agent_hit_points", 10),
						(store_sub, ":start_running_away_courage_score_limit", 3500, ":agent_hit_points"),
						(lt, ":agent_courage_score", ":start_running_away_courage_score_limit"), #if (courage score < 3500 - (agent hit points * 40)) and (agent is not running away) then start running away, average hit points : 50, average running away limit = 1500
						
						(agent_get_troop_id, ":troop_id", ":cur_agent"), #for now do not let heroes to run away from battle
						(neg|troop_is_hero, ":troop_id"),
						
						(agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
						(agent_start_running_away, ":cur_agent"),
						(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
					(try_end),
				(else_try),
					(neq, ":force_retreat", 1),
					(agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
					(store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
					(val_mul, ":agent_hit_points", 4),
					(try_begin),
						(agent_is_ally, ":cur_agent"),
						(val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
					(try_end),
					(val_mul, ":agent_hit_points", 10),
					(store_sub, ":stop_running_away_courage_score_limit", 3700, ":agent_hit_points"),
					(ge, ":agent_courage_score", ":stop_running_away_courage_score_limit"), #if (courage score > 3700 - agent hit points) and (agent is running away) then stop running away, average hit points : 50, average running away limit = 1700
					(agent_stop_running_away, ":cur_agent"),
					(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
				(try_end),
		]) #ozan

		 # script_apply_death_effect_on_courage_scores
		# called during battle
		# WARNING: modified by 1257AD devs
		# Input: dead agent id, killer agent id
		# Output: none
apply_death_effect_on_courage_scores = (
	"apply_death_effect_on_courage_scores",
			[
				(store_script_param, ":dead_agent_no", 1),
				(store_script_param, ":killer_agent_no", 2),
				
				(try_begin),
					(agent_is_human, ":dead_agent_no"),
					
					(try_begin),
						(agent_is_ally, ":dead_agent_no"),
						(assign, ":is_dead_agent_ally", 1),
					(else_try),
						(assign, ":is_dead_agent_ally", 0),
					(try_end),
					
					(agent_get_position, pos0, ":dead_agent_no"),
					(assign, ":number_of_near_allies_to_dead_agent", 0),
					
					(try_for_agents, ":agent_no"),
						(agent_is_human, ":agent_no"),
						(agent_is_alive, ":agent_no"),
						
						(agent_get_position, pos1, ":agent_no"),
						(get_distance_between_positions, ":dist", pos0, pos1),
						
						(le, ":dist", 1300), # to count number of allies within 13 meters to dead agent.
						
						(try_begin),
							(agent_is_ally, ":agent_no"),
							(assign, ":is_agent_ally", 1),
						(else_try),
							(assign, ":is_agent_ally", 0),
						(try_end),
						
						(try_begin),
							(eq, ":is_dead_agent_ally", ":is_agent_ally"),
							(val_add, ":number_of_near_allies_to_dead_agent", 1), # (number_of_near_allies_to_dead_agent) is counted because if there are
						(try_end),                                              # many allies of dead agent around him, negative courage effect become less.
					(try_end),
					
					(try_for_agents, ":agent_no"),
						(agent_is_human, ":agent_no"),
						(agent_is_alive, ":agent_no"),
						
						(try_begin),
							(agent_is_ally, ":agent_no"),
							(assign, ":is_agent_ally", 1),
						(else_try),
							(assign, ":is_agent_ally", 0),
						(try_end),
						
						(try_begin), # each agent is effected by a killed agent positively if he is rival or negatively if he is ally.
							(neq, ":is_dead_agent_ally", ":is_agent_ally"),
							(assign, ":agent_delta_courage_score", 10),  # if killed agent is agent of rival side, add points to fear score
						(else_try),
							(assign, ":agent_delta_courage_score", -15), # if killed agent is agent of our side, decrease points from fear score
							(val_add, ":agent_delta_courage_score", ":number_of_near_allies_to_dead_agent"), # ":number_of_near_allies_to_dead_agent" is added because if there are many
							(try_begin),                                                                     # allies of dead agent around him, negative courage effect become less.
								(gt, ":agent_delta_courage_score", -5),
								(assign, ":agent_delta_courage_score", -5),
							(try_end),
							
							(agent_get_slot, ":dead_agent_was_running_away_or_not", ":dead_agent_no",  slot_agent_is_running_away), #look dead agent was running away or not.
							(try_begin),
								(eq, ":dead_agent_was_running_away_or_not", 1),
								(val_div, ":agent_delta_courage_score", 3),  # if killed agent was running away his negative effect on ally courage scores become very less. This added because
							(try_end),                                     # running away agents are easily killed and courage scores become very in a running away group after a time, and
						(try_end),                                       # they do not stop running away althought they pass near a new powerfull ally party.
						(agent_get_position, pos1, ":agent_no"),
						(get_distance_between_positions, ":dist", pos0, pos1),
						
						(try_begin),
							(eq, ":killer_agent_no", ":agent_no"),
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 20),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(try_end),
						
						(try_begin),
							(lt, ":dist", 100), #0-1 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 150),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 200), #2 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 120),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 300), #3 meter
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 100),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 400), #4 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 90),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 600), #5-6 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 80),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 800), #7-8 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 70),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 1000), #9-10 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 60),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 1500), #11-15 meter
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 50),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 2500), #16-25 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 40),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 4000), #26-40 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 30),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 6500), #41-65 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 20),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(else_try),
							(lt, ":dist", 10000), #61-100 meters
							(agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
							(val_mul, ":agent_delta_courage_score", 10),
							(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
							(agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
						(try_end),
					(try_end),
				(try_end),
		]) #ozan

		
 # script_battle_tactic_apply
    # Input: none
    # Output: none
battle_tactic_apply = (
	"battle_tactic_apply",
		[
			(call_script, "script_battle_tactic_apply_aux", "$ai_team_1", "$ai_team_1_battle_tactic"),
			(assign, "$ai_team_1_battle_tactic", reg0),
			(try_begin),
			(ge, "$ai_team_2", 0),
			(call_script, "script_battle_tactic_apply_aux", "$ai_team_2", "$ai_team_2_battle_tactic"),
			(assign, "$ai_team_2_battle_tactic", reg0),
			(try_end),
		])
    
		
		# script_select_battle_tactic
		# Input: none
		# Output: none
select_battle_tactic = (
	"select_battle_tactic",
			[
				(assign, "$ai_team_1_battle_tactic", 0),
				(get_player_agent_no, ":player_agent"),
				(agent_get_team, ":player_team", ":player_agent"),
				(try_begin),
					(num_active_teams_le, 2),
					(try_begin),
						(eq, ":player_team", 0),
						(assign, "$ai_team_1", 1),
					(else_try),
						(assign, "$ai_team_1", 0),
					(try_end),
					(assign, "$ai_team_2", -1),
				(else_try),
					(try_begin),
						(eq, ":player_team", 0),
						(assign, "$ai_team_1", 1),
					(else_try),
						(assign, "$ai_team_1", 0),
					(try_end),
					(store_add, "$ai_team_2", ":player_team", 2),
				(try_end),
				(call_script, "script_select_battle_tactic_aux", "$ai_team_1", 0),
				(assign, "$ai_team_1_battle_tactic", reg0),
				(try_begin),
					(ge, "$ai_team_2", 0),
					(assign, ":defense_not_an_option", 0),
					(try_begin),
						(eq, "$ai_team_1_battle_tactic", btactic_hold),
						(assign, ":defense_not_an_option", 1), #don't let two AI defend at the same time
					(try_end),
					(call_script, "script_select_battle_tactic_aux", "$ai_team_2", ":defense_not_an_option"),
					(assign, "$ai_team_2_battle_tactic", reg0),
				(try_end),
		])
		
		# script_apply_effect_of_other_people_on_courage_scores
		# called during battle
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
apply_effect_of_other_people_on_courage_scores = (
	"apply_effect_of_other_people_on_courage_scores",
			[
				(get_player_agent_no, ":player_agent"),
				
				(try_for_agents, ":centered_agent_no"),
					(agent_is_human, ":centered_agent_no"),
					(agent_is_alive, ":centered_agent_no"),
					(neq, ":centered_agent_no", ":player_agent"),
					(agent_get_position, pos0, ":centered_agent_no"),
					(try_begin),
						(agent_is_ally, ":centered_agent_no"),
						(assign, ":is_centered_agent_ally", 1),
					(else_try),
						(assign, ":is_centered_agent_ally", 0),
					(try_end),
					
					(try_for_agents, ":agent_no"),
						(agent_is_human, ":agent_no"),
						(agent_is_alive, ":agent_no"),
						(neq, ":centered_agent_no", ":agent_no"),
						
						(try_begin),
							(agent_is_ally, ":agent_no"),
							(assign, ":is_agent_ally", 1),
						(else_try),
							(assign, ":is_agent_ally", 0),
						(try_end),
						
						(eq, ":is_centered_agent_ally", ":is_agent_ally"), #if centered agent and other agent is at same team then continue.
						(agent_get_slot, ":agent_is_running_away_or_not", ":agent_no", slot_agent_is_running_away),
						
						(try_begin),
							(eq, ":agent_no", ":player_agent"),
							(assign, ":agent_delta_courage_score", 6),
						(else_try),
							(agent_get_troop_id, ":troop_id", ":agent_no"),
							(troop_is_hero, ":troop_id"),
							
							#Hero Agent : if near agent (hero, agent_no) is not running away his positive effect on centered agent (centered_agent_no) fighting at his side is effected by his hit points.
							(try_begin),
								(neq, ":agent_is_running_away_or_not", 1), #if agent is not running away
								(store_agent_hit_points, ":agent_hit_points", ":agent_no"),
								(try_begin),
									(eq, ":agent_hit_points", 100),
									(assign, ":agent_delta_courage_score", 6),
								(else_try),
									(ge, ":agent_hit_points", 75),
									(assign, ":agent_delta_courage_score", 5),
								(else_try),
									(ge, ":agent_hit_points", 60),
									(assign, ":agent_delta_courage_score", 4),
								(else_try),
									(ge, ":agent_hit_points", 45),
									(assign, ":agent_delta_courage_score", 3),
								(else_try),
									(ge, ":agent_hit_points", 30),
									(assign, ":agent_delta_courage_score", 2),
								(else_try),
									(ge, ":agent_hit_points", 15),
									(assign, ":agent_delta_courage_score", 1),
								(end_try),
							(else_try),
								(assign, ":agent_delta_courage_score", 4),
							(end_try),
						(else_try),
							#Normal Agent : if near agent (agent_no) is not running away his positive effect on centered agent (centered_agent_no) fighting at his side is effected by his hit points.
							(try_begin),
								(neq, ":agent_is_running_away_or_not", 1), # if agent is not running away
								(store_agent_hit_points, ":agent_hit_points", ":agent_no"),
								(try_begin),
									(eq, ":agent_hit_points", 100),
									(assign, ":agent_delta_courage_score", 4),
								(else_try),
									(ge, ":agent_hit_points", 75),
									(assign, ":agent_delta_courage_score", 3),
								(else_try),
									(ge, ":agent_hit_points", 50),
									(assign, ":agent_delta_courage_score", 2),
								(else_try),
									(ge, ":agent_hit_points", 25),
									(assign, ":agent_delta_courage_score", 1),
								(end_try),
								(try_begin), # to make our warrior run away easier we decrease one, because they have player_agent (+6) advantage.
									(agent_is_ally, ":agent_no"),
									(val_sub, ":agent_delta_courage_score", 1),
								(end_try),
							(else_try),
								(assign, ":agent_delta_courage_score", 2),
							(end_try),
						(try_end),
						
						(try_begin),
							(neq, ":agent_is_running_away_or_not", 1),
							(val_mul, ":agent_delta_courage_score", 1),
							(try_begin), # centered agent not running away cannot take positive courage score from one another agent not running away.
								(agent_get_slot, ":agent_is_running_away_or_not", ":centered_agent_no", slot_agent_is_running_away),
								(eq, ":agent_is_running_away_or_not", 0),
								(val_mul, ":agent_delta_courage_score", 0),
							(try_end),
						(else_try),
							(try_begin),
								(agent_get_slot, ":agent_is_running_away_or_not", ":agent_no", slot_agent_is_running_away),
								(eq, ":agent_is_running_away_or_not", 0),
								(val_mul, ":agent_delta_courage_score", -2), # running away agent fears not running away agent more.
							(else_try),
								(val_mul, ":agent_delta_courage_score", -1),
							(try_end),
						(try_end),
						
						(neq, ":agent_delta_courage_score", 0),
						
						(agent_get_position, pos1, ":agent_no"),
						(get_distance_between_positions, ":dist", pos0, pos1),
						
						(try_begin),
							(ge, ":agent_delta_courage_score", 0),
							(try_begin),
								(lt, ":dist", 2000), #0-20 meter
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 50),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 4000), #21-40 meter
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 40),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 7000), #41-70 meter
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 30),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 11000), #71-110 meter
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 20),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 16000), # 111-160 meter, assumed that eye can see agents friendly at most 160 meters far while fighting.
								# this is more than below limit (108 meters) because we hear that allies come from further.
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 10),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(try_end),
						(else_try),                                               # negative effect of running agent on other ally agents are lower then positive effects above, to avoid starting
							(try_begin),                                            # run away of all agents at a moment. I want to see agents running away one by one during battle, not all together.
								(lt, ":dist", 200), #1-2 meter,                       # this would create better game play.
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 15),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 400), #3-4 meter,
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 13),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 600), #5-6 meter
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 11),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 800), #7-8 meter
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 9),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 1200), #9-12 meters
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 7),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 2400), #13-24 meters
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 5),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 4800), #25-48 meters
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 3),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(else_try),
								(lt, ":dist", 9600), #49-98 meters, assumed that eye can see agents running away at most 98 meters far while fighting.
								(agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
								(val_mul, ":agent_delta_courage_score", 1),
								(val_add, ":agent_courage_score", ":agent_delta_courage_score"),
								(agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),
							(try_end),
						(try_end),
					(try_end),
				(try_end), # ozan
		]) 

		# script_check_friendly_kills
		# Input: none
		# Output: none (changes the morale of the player's party)
check_friendly_kills = (
	"check_friendly_kills",
			[(get_player_agent_own_troop_kill_count, ":count"),
				(try_begin),
					(neq, "$g_player_current_own_troop_kills", ":count"),
					(val_sub, ":count", "$g_player_current_own_troop_kills"),
					(val_add, "$g_player_current_own_troop_kills", ":count"),
					(val_mul, ":count", -1),
					(call_script, "script_change_player_party_morale", ":count"),
				(try_end),
		])

		# script_simulate_retreat
		# Input: arg1 = players_side_damage, arg2 = enemy_side_damage, arg3 = continue_battle s5 = title_string
		# Output: none
simulate_retreat = (
	"simulate_retreat",
			[
				(call_script, "script_music_set_situation_with_culture", mtf_sit_killed),
				(set_show_messages, 0),
				(store_script_param, ":players_side_damage", 1),
				(store_script_param, ":enemy_side_damage", 2),
				(store_script_param, ":continue_battle", 3),
				
				(assign, ":players_side_strength", 0),
				(assign, ":enemy_side_strength", 0),
				
				(assign, ":do_calculate", 1),
				(try_begin),
					(try_for_agents, ":cur_agent"),
						(agent_is_human, ":cur_agent"),
						(agent_is_alive, ":cur_agent"),
						(agent_set_slot, ":cur_agent", slot_agent_is_alive_before_retreat, 1),#needed for simulation
						
						(agent_get_troop_id, ":cur_troop", ":cur_agent"),
						(store_character_level, ":cur_level", ":cur_troop"),
						(val_add, ":cur_level", 5),
						(try_begin),
							(troop_is_hero, ":cur_troop"),
							(val_add, ":cur_level", 5),
						(try_end),
						(try_begin),
							(agent_is_ally, ":cur_agent"),
							(val_add, ":players_side_strength", ":cur_level"),
						(else_try),
							(val_add, ":enemy_side_strength", ":cur_level"),
						(try_end),
					(try_end),
					(eq, "$pin_player_fallen", 0),
					(lt, ":enemy_side_strength", ":players_side_strength"),
					(eq, ":continue_battle", 1),
					(assign, ":do_calculate", 0),
				(try_end),
				
				(try_begin),
					(eq, ":do_calculate", 1),
					
					(assign, "$g_last_mission_player_damage", 0),
					(party_clear, "p_temp_party"),
					(party_clear, "p_temp_party_2"),
					(call_script, "script_simulate_battle_with_agents_aux", 0, ":players_side_damage"),
					(call_script, "script_simulate_battle_with_agents_aux", 1, ":enemy_side_damage"),
					
					(assign, ":display_casualties", 0),
					
					(try_begin),
						(gt, "$g_last_mission_player_damage", 0),
						(assign, ":display_casualties", 1),
						(assign, reg1, "$g_last_mission_player_damage"),
						(str_store_string, s12, "str_casualty_display_hp"),
					(else_try),
						(str_clear, s12),
					(try_end),
					
					(call_script, "script_print_casualties_to_s0", "p_temp_party", 1),
					(try_begin),
						(party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
						(gt, ":num_stacks", 0),
						(assign, ":display_casualties", 1),
					(try_end),
					(str_store_string_reg, s10, s0),
					
					(call_script, "script_print_casualties_to_s0", "p_temp_party_2", 1),
					(try_begin),
						(party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
						(gt, ":num_stacks", 0),
						(assign, ":display_casualties", 1),
					(try_end),
					(str_store_string_reg, s11, s0),
					(try_begin),
						(eq, ":display_casualties", 1),
						(dialog_box,"str_casualty_display", s5),
					(try_end),
				(try_end),
				(set_show_messages, 1),
				
				#Calculating morale penalty (can be between 0-30)
				(assign, ":ally_casualties", 0),
				(assign, ":enemy_casualties", 0),
				(assign, ":total_allies", 0),
				
				(try_for_agents, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(try_begin),
						(agent_is_ally, ":cur_agent"),
						(val_add, ":total_allies", 1),
						(try_begin),
							(neg|agent_is_alive, ":cur_agent"),
							(val_add, ":ally_casualties", 1),
						(try_end),
					(else_try),
						(neg|agent_is_alive, ":cur_agent"),
						(val_add, ":enemy_casualties", 1),
					(try_end),
				(try_end),
				(store_add, ":total_casualties", ":ally_casualties", ":enemy_casualties"),
				(try_begin),
					(gt, ":total_casualties", 0),
					(store_mul, ":morale_adder", ":ally_casualties", 100),
					(val_div, ":morale_adder", ":total_casualties"),
					(val_mul, ":morale_adder", ":ally_casualties"),
					(val_div, ":morale_adder", ":total_allies"),
					(val_mul, ":morale_adder", -30),
					(val_div, ":morale_adder", 100),
					(call_script, "script_change_player_party_morale", ":morale_adder"),
				(try_end),
		])
		
		
		
		# script_simulate_battle_with_agents_aux
		# For internal use only
		# Input: arg1 = attacker_side (0 = ally, 1 = enemy), arg2 = damage amount
		# Output: none
simulate_battle_with_agents_aux = (
	"simulate_battle_with_agents_aux",
			[
				(store_script_param_1, ":attacker_side"),
				(store_script_param_2, ":damage"),
				
				(get_player_agent_no, ":player_agent"),
				(try_for_agents, ":cur_agent"),
					(neq, ":player_agent", ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					#do not check agent_is_alive, check slot_agent_is_alive_before_retreat instead, so that dead agents can still hit enemies
					(agent_slot_eq, ":cur_agent", slot_agent_is_alive_before_retreat, 1),
					(try_begin),
						(agent_is_ally, ":cur_agent"),
						(assign, ":cur_agents_side", 0),
					(else_try),
						(assign, ":cur_agents_side", 1),
					(try_end),
					(eq, ":cur_agents_side", ":attacker_side"),
					(agent_get_position, pos2, ":cur_agent"),
					(assign, ":closest_agent", -1),
					(assign, ":min_distance", 100000),
					(try_for_agents, ":cur_agent_2"),
						(agent_is_human, ":cur_agent_2"),
						(agent_is_alive, ":cur_agent_2"),
						(try_begin),
							(agent_is_ally, ":cur_agent_2"),
							(assign, ":cur_agents_side_2", 0),
						(else_try),
							(assign, ":cur_agents_side_2", 1),
						(try_end),
						(this_or_next|neq, ":cur_agent_2", ":player_agent"),
						(eq, "$pin_player_fallen", 0),
						(neq, ":attacker_side", ":cur_agents_side_2"),
						(agent_get_position, pos3, ":cur_agent_2"),
						(get_distance_between_positions, ":cur_distance", pos2, pos3),
						(lt, ":cur_distance", ":min_distance"),
						(assign, ":min_distance", ":cur_distance"),
						(assign, ":closest_agent", ":cur_agent_2"),
					(try_end),
					(ge, ":closest_agent", 0),
					#Fight
					(agent_get_class, ":agent_class", ":cur_agent"),
					(assign, ":agents_speed", 1),
					(assign, ":agents_additional_hit", 0),
					(try_begin),
						(eq, ":agent_class", grc_archers),
						(assign, ":agents_additional_hit", 2),
					(else_try),
						(eq, ":agent_class", grc_cavalry),
						(assign, ":agents_speed", 2),
					(try_end),
					(agent_get_class, ":agent_class", ":closest_agent"),
					(assign, ":agents_speed_2", 1),
					(try_begin),
						(eq, ":agent_class", grc_cavalry),
						(assign, ":agents_speed_2", 2),
					(try_end),
					(assign, ":agents_hit", 18000),
					(val_add, ":min_distance", 3000),
					(val_div, ":agents_hit", ":min_distance"),
					(val_mul, ":agents_hit", 2),# max 10, min 2 hits within 150 meters
					
					(val_mul, ":agents_hit", ":agents_speed"),
					(val_div, ":agents_hit", ":agents_speed_2"),
					(val_add, ":agents_hit", ":agents_additional_hit"),
					
					(assign, ":cur_damage", ":damage"),
					(agent_get_troop_id, ":closest_troop", ":closest_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
					(store_character_level, ":closest_level", ":closest_troop"),
					(store_character_level, ":cur_level", ":cur_troop"),
					(store_sub, ":level_dif", ":cur_level", ":closest_level"),
					(val_div, ":level_dif", 5),
					(val_add, ":cur_damage", ":level_dif"),
					
					(try_begin),
						(eq, ":closest_agent", ":player_agent"),
						(val_div, ":cur_damage", 2),
						(store_agent_hit_points, ":init_player_hit_points", ":player_agent", 1),
					(try_end),
					
					(try_for_range, ":unused", 0, ":agents_hit"),
						(store_random_in_range, ":random_damage", 0, 100),
						(lt, ":random_damage", ":cur_damage"),
						(agent_deliver_damage_to_agent, ":cur_agent", ":closest_agent"),
					(try_end),
					
					(try_begin),
						(eq, ":closest_agent", ":player_agent"),
						(store_agent_hit_points, ":final_player_hit_points", ":player_agent", 1),
						(store_sub, ":hit_points_difference", ":init_player_hit_points", ":final_player_hit_points"),
						(val_add, "$g_last_mission_player_damage", ":hit_points_difference"),
					(try_end),
					
					(neg|agent_is_alive, ":closest_agent"),
					(try_begin),
						(eq, ":attacker_side", 1),
						(party_add_members, "p_temp_party", ":closest_troop", 1),
						(try_begin),
							(agent_is_wounded, ":closest_agent"),
							(party_wound_members, "p_temp_party", ":closest_troop", 1),
						(try_end),
					(else_try),
						(party_add_members, "p_temp_party_2", ":closest_troop", 1),
						(try_begin),
							(agent_is_wounded, ":closest_agent"),
							(party_wound_members, "p_temp_party_2", ":closest_troop", 1),
						(try_end),
					(try_end),
				(try_end),
		])
		

		#script_agent_reassign_team
		# there are freelancer scripts resides here
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = agent_no
		# OUTPUT: none
agent_reassign_team = (
	"agent_reassign_team",
			[
				(store_script_param, ":agent_no", 1),
				(get_player_agent_no, ":player_agent"),
				(try_begin),
					(ge, ":player_agent", 0),
					(agent_is_human, ":agent_no"),
					(agent_is_ally, ":agent_no"),
					(agent_get_party_id, ":party_no", ":agent_no"),
					#(neq, ":party_no", "p_main_party"), #tom
			(gt, ":party_no", "p_main_party"), #tom
					(assign, ":continue", 1),
					(store_faction_of_party, ":party_faction", ":party_no"),
					(try_begin),
						(eq, ":party_faction", "$players_kingdom"),
						(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
						(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
						(assign, ":continue", 0),
					(else_try),
				(neq, "$freelancer_state", 1),	#Caba freelancer fixes chief
						(party_stack_get_troop_id, ":leader_troop_id", ":party_no", 0),
						(neg|is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end),
						(assign, ":continue", 0),
					(try_end),
					(eq, ":continue", 1),
					(agent_get_team, ":player_team", ":player_agent"),
					(val_add, ":player_team", 2),
					(agent_set_team, ":agent_no", ":player_team"),
				(try_end),
		])

#script_count_mission_casualties_from_agents
		# WARNING: heavily modified by 1257Ad devs
		# INPUT: none
		# OUTPUT: none
count_mission_casualties_from_agents = (
	"count_mission_casualties_from_agents",
			[(party_clear, "p_player_casualties"),
				(party_clear, "p_enemy_casualties"),
				(party_clear, "p_ally_casualties"),
				(assign, "$any_allies_at_the_last_battle", 0),
				#(assign, "$num_routed_us", 0), #these should not assign to 0 here to protect routed agents to spawn again in next turns.
				#(assign, "$num_routed_allies", 0),
				#(assign, "$num_routed_enemies", 0),
				
				#initialize all routed counts of troops
				(try_for_agents, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(agent_get_party_id, ":agent_party", ":cur_agent"),
					(agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
					(troop_set_slot, ":agent_troop_id", slot_troop_player_routed_agents, 0),
					(troop_set_slot, ":agent_troop_id", slot_troop_ally_routed_agents, 0),
					(troop_set_slot, ":agent_troop_id", slot_troop_enemy_routed_agents, 0),
				(try_end),
				
				(try_for_agents, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
			(neg|agent_slot_eq, ":cur_agent", slot_possessed, 1), #tom
					(agent_get_party_id, ":agent_party", ":cur_agent"),
					(try_begin),
						(neq, ":agent_party", "p_main_party"), #tom
			(agent_slot_eq, ":cur_agent", slot_possessed, 0), #tom
						(agent_is_ally, ":cur_agent"),
						(assign, "$any_allies_at_the_last_battle", 1),
					(try_end),
					#count routed agents in player party, ally parties and enemy parties
					(try_begin),
						(agent_is_routed, ":cur_agent"),
						(agent_get_slot, ":agent_was_running_away", ":cur_agent", slot_agent_is_running_away),
						(eq, ":agent_was_running_away", 1),
						(try_begin),
							(agent_get_troop_id, ":routed_ag_troop_id", ":cur_agent"),
							(agent_get_party_id, ":routed_ag_party_id", ":cur_agent"),
							#only enemies
							#only regulars
							(store_faction_of_party, ":faction_of_routed_agent_party", ":routed_ag_party_id"),
							
							(try_begin),
								(eq, ":agent_party", "p_main_party"),
								(val_add, "$num_routed_us", 1),
							(else_try),
								(agent_is_ally, ":cur_agent"),
								(val_add, "$num_routed_allies", 1),
							(else_try),
								#for now only count and include routed enemy agents in new routed party.
								(val_add, "$num_routed_enemies", 1),
								(faction_get_slot, ":num_routed_agents_in_this_faction", ":faction_of_routed_agent_party", slot_faction_num_routed_agents),
								(val_add, ":num_routed_agents_in_this_faction", 1),
								(faction_set_slot, ":faction_of_routed_agent_party", slot_faction_num_routed_agents, ":num_routed_agents_in_this_faction"),
								(party_add_members, "p_routed_enemies", ":routed_ag_troop_id", 1),
							(try_end),
						(try_end),
						(agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
						(try_begin),
							(eq, ":agent_party", "p_main_party"),
							(troop_get_slot, ":player_routed_agents", ":agent_troop_id", slot_troop_player_routed_agents),
							(val_add, ":player_routed_agents", 1),
							(troop_set_slot, ":agent_troop_id", slot_troop_player_routed_agents, ":player_routed_agents"),
							
						(else_try),
							(agent_is_ally, ":cur_agent"),
							(troop_get_slot, ":ally_routed_agents", ":agent_troop_id", slot_troop_ally_routed_agents),
							(val_add, ":ally_routed_agents", 1),
							(troop_set_slot, ":agent_troop_id", slot_troop_ally_routed_agents, ":ally_routed_agents"),
							
						(else_try),
							(troop_get_slot, ":enemy_routed_agents", ":agent_troop_id", slot_troop_enemy_routed_agents),
							(val_add, ":enemy_routed_agents", 1),
							(troop_set_slot, ":agent_troop_id", slot_troop_enemy_routed_agents, ":enemy_routed_agents"),
							
						(try_end),
					(try_end),
					#count and save killed agents in player party, ally parties and enemy parties
					(neg|agent_is_alive, ":cur_agent"),
					(agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
					(try_begin),
						(eq, ":agent_party", "p_main_party"),
						(party_add_members, "p_player_casualties", ":agent_troop_id", 1),
						(try_begin),
							(agent_is_wounded, ":cur_agent"),
							(party_wound_members, "p_player_casualties", ":agent_troop_id", 1),
						(try_end),
			#tom
			(else_try),
			(agent_slot_eq, ":cur_agent", slot_possessed, 2), #tom
			(agent_get_slot, ":player_troop", ":cur_agent", slot_real_troop),
			(party_add_members, "p_player_casualties", ":player_troop", 1),
						(try_begin),
							(agent_is_wounded, ":cur_agent"),
							(party_wound_members, "p_player_casualties", ":player_troop", 1),
						(try_end),
			#tom
					(else_try),
						(agent_is_ally, ":cur_agent"),
						(party_add_members, "p_ally_casualties", ":agent_troop_id", 1),
						(try_begin),
							(agent_is_wounded, ":cur_agent"),
							(party_wound_members, "p_ally_casualties", ":agent_troop_id", 1),
						(try_end),
					(else_try),
						(party_add_members, "p_enemy_casualties", ":agent_troop_id", 1),
						(try_begin),
							(agent_is_wounded, ":cur_agent"),
							(party_wound_members, "p_enemy_casualties", ":agent_troop_id", 1),
						(try_end),
					(try_end),
				(try_end),
				#for the troop traking for lances.
				(try_begin),
					(call_script, "script_check_agents_for_lances"), 
				(try_end),
		])