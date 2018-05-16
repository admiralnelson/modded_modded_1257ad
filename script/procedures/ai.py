from header import *

# script_init_ai_calculation
		# Input: none
		# Output: none
init_ai_calculation = (
	"init_ai_calculation",
			[
				(try_for_range, ":cur_troop", heroes_begin, heroes_end),
					(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
					(troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
					(party_is_active, ":cur_party"),
					(store_troop_faction, ":fac", ":cur_troop"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_strength", ":cur_party", 0), #will update slot_party_cached_strength
				(try_end),
				
				(call_script, "script_party_calculate_strength", "p_main_party", 0), #will update slot_party_cached_strength
				
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":fac", ":cur_center"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_strength", ":cur_center", 0), #will update slot_party_cached_strength
				(try_end),
				
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":fac", ":cur_center"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", ":cur_center"),
				(try_end),
				
				(try_for_range, ":cur_troop", heroes_begin, heroes_end),
					(troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
					(gt, ":cur_troop_party", 0),
					(party_is_active, ":cur_troop_party"),
					(store_troop_faction, ":fac", ":cur_troop"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", ":cur_troop_party"),
				(try_end),
				(call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", "p_main_party"),
		])

		
		# script_recalculate_ais
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		#When a lord changes factions
		#When a center changes factions
		#When a center is captured
		#When a marshal is defeated
		#Every 23 hours
recalculate_ais = (
	"recalculate_ais",
			[
				# rafi
				# (assign, ":max_recalculations", 3), #tom was 3
				# (assign, ":recalculations_done", 0),
				
				#(assign, ":recalculate_all", 1), #tom no need?
				
				#(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
				# (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
				# (faction_slot_eq, ":cur_kingdom", slot_faction_recalculate_ai, 0),
				
				# (faction_get_slot, ":last_calculation", ":cur_kingdom", slot_faction_last_ai_calculation),
				# (try_begin),
				# (lt, ":last_calculation", 0),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
				# (try_end),
				
				# (store_current_hours, ":time"),
				# (val_sub, ":time", ":last_calculation"),
				
				# (try_begin),
				# (gt, ":time", 6),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
				# (str_store_faction_name, s21, ":cur_kingdom"),
				# (assign, reg21, ":time"),
				# #(display_message, "@faction {s21} overdue for recalculation {reg21}, adding"),
				# (try_end),
				# (try_end),
				
				# (try_begin),
				# (eq, ":recalculate_all", 255),
				# (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
				# (try_end),
				# (try_end),
				
				(call_script, "script_init_ai_calculation"),
				
				#(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
				(assign, ":faction_no", "$g_ai_kingdom"),
				(try_begin),
					(assign, reg8, ":faction_no"),
					(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
					
					# (val_add, ":recalculations_done", 1),
					# (le, ":recalculations_done", ":max_recalculations"),
					
					(store_current_hours, ":time"),
					(faction_set_slot, ":faction_no", slot_faction_last_ai_calculation, ":time"),
					
					#(str_store_faction_name, s21, ":faction_no"),
					#(display_message, "@AI recalculated for {s21}"),
					#(neg|faction_slot_eq, ":faction_no",  slot_faction_marshall, "trp_player"),
					(call_script, "script_decide_faction_ai", ":faction_no"),
				(try_end),
				
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
					(store_troop_faction, ":faction_no", ":troop_no"),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(eq, ":faction_no", "$g_ai_kingdom"),
					(call_script, "script_calculate_troop_ai", ":troop_no"),
				(try_end),
				
				# (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 0),
				# (try_end),
		])
		
		# script_calculate_troop_ai
		# Input: troop_no
		# Output: none
		#Now called directly from scripts
calculate_troop_ai = (
	"calculate_troop_ai",
			[
				(store_script_param, ":troop_no", 1),
				(try_begin),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
					(gt, ":party_no", 0),
					(party_is_active, ":party_no"),
					
					(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
					(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
				(try_end),
		])
		
		# script_decide_run_away_or_not
	# Input: none
	# Output: none
decide_run_away_or_not = (
	"decide_run_away_or_not",
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
	]) 
#ozan
		