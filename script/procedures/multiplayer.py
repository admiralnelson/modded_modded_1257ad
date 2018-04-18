from header import *

#script_game_set_multiplayer_mission_end
# This script is called from the game engine when a multiplayer map is ended in clients (not in server).
# INPUT:
# none
# OUTPUT:
# none
game_set_multiplayer_mission_end = (
	"game_set_multiplayer_mission_end",
		[
			(assign, "$g_multiplayer_mission_end_screen", 1),
	])

#script_add_kill_death_counts
	# INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
	# OUTPUT: none
add_kill_death_counts =	("add_kill_death_counts",
		[
			(store_script_param, ":killer_agent_no", 1),
			(store_script_param, ":dead_agent_no", 2),
			
			(try_begin),
				(ge, ":killer_agent_no", 0),
				(agent_get_team, ":killer_agent_team", ":killer_agent_no"),
			(else_try),
				(assign, ":killer_agent_team", -1),
			(try_end),
			
			(try_begin),
				(ge, ":dead_agent_no", 0),
				(agent_get_team, ":dead_agent_team", ":dead_agent_no"),
			(else_try),
				(assign, ":dead_agent_team", -1),
			(try_end),
			
			#adjusting kill counts of players/bots
			(try_begin),
				(try_begin),
					(ge, ":killer_agent_no", 0),
					(ge, ":dead_agent_no", 0),
					(agent_is_human, ":killer_agent_no"),
					(agent_is_human, ":dead_agent_no"),
					(neq, ":killer_agent_no", ":dead_agent_no"),
					
					(this_or_next|neq, ":killer_agent_team", ":dead_agent_team"),
					(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
					
					(agent_get_player_id, ":killer_agent_player", ":killer_agent_no"),
					(try_begin),
						(agent_is_non_player, ":killer_agent_no"), #if killer agent is bot then increase bot kill counts of killer agent's team by one.
						(agent_get_team, ":killer_agent_team", ":killer_agent_no"),
						(team_get_bot_kill_count, ":killer_agent_team_bot_kill_count", ":killer_agent_team"),
						(val_add, ":killer_agent_team_bot_kill_count", 1),
						(team_set_bot_kill_count, ":killer_agent_team", ":killer_agent_team_bot_kill_count"),
					(else_try), #if killer agent is not bot then increase kill counts of killer agent's player by one.
						(player_is_active, ":killer_agent_player"),
						(player_get_kill_count, ":killer_agent_player_kill_count", ":killer_agent_player"),
						(val_add, ":killer_agent_player_kill_count", 1),
						(player_set_kill_count, ":killer_agent_player", ":killer_agent_player_kill_count"),
					(try_end),
				(try_end),
				
				(try_begin),
					(ge, ":dead_agent_no", 0),
					(agent_is_human, ":dead_agent_no"),
					(try_begin),
						(agent_is_non_player, ":dead_agent_no"), #if dead agent is bot then increase bot kill counts of dead agent's team by one.
						(agent_get_team, ":dead_agent_team", ":dead_agent_no"),
						(team_get_bot_death_count, ":dead_agent_team_bot_death_count", ":dead_agent_team"),
						(val_add, ":dead_agent_team_bot_death_count", 1),
						(team_set_bot_death_count, ":dead_agent_team", ":dead_agent_team_bot_death_count"),
					(else_try), #if dead agent is not bot then increase death counts of dead agent's player by one.
						(agent_get_player_id, ":dead_agent_player", ":dead_agent_no"),
						(player_is_active, ":dead_agent_player"),
						(player_get_death_count, ":dead_agent_player_death_count", ":dead_agent_player"),
						(val_add, ":dead_agent_player_death_count", 1),
						(player_set_death_count, ":dead_agent_player", ":dead_agent_player_death_count"),
					(try_end),
					
					(try_begin),
						(assign, ":continue", 0),
						
						(try_begin),
							(this_or_next|lt, ":killer_agent_no", 0), #if he killed himself (1a(team change) or 1b(self kill)) then decrease kill counts of killer player by one.
							(eq, ":killer_agent_no", ":dead_agent_no"),
							(assign, ":continue", 1),
						(try_end),
						
						(try_begin),
							(eq, ":killer_agent_team", ":dead_agent_team"), #if he killed a teammate and game mod is not deathmatch then decrease kill counts of killer player by one.
							(neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
							(neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
							(assign, ":continue", 1),
						(try_end),
						
						(eq, ":continue", 1),
						
						(try_begin),
							(ge, ":killer_agent_no", 0),
							(assign, ":responsible_agent", ":killer_agent_no"),
						(else_try),
							(assign, ":responsible_agent", ":dead_agent_no"),
						(try_end),
						
						(try_begin),
							(ge, ":responsible_agent", 0),
							(neg|agent_is_non_player, ":responsible_agent"),
							(agent_get_player_id, ":responsible_player", ":responsible_agent"),
							(ge, ":responsible_player", 0),
							(player_get_kill_count, ":dead_agent_player_kill_count", ":responsible_player"),
							(val_add, ":dead_agent_player_kill_count", -1),
							(player_set_kill_count, ":responsible_player", ":dead_agent_player_kill_count"),
						(try_end),
					(try_end),
				(try_end),
			(try_end),
	])
	
#script_warn_player_about_auto_team_balance
# INPUT: none
# OUTPUT: none
warn_player_about_auto_team_balance = ("warn_player_about_auto_team_balance",
		[
			(assign, "$g_multiplayer_message_type", multiplayer_message_type_auto_team_balance_next),
			(start_presentation, "prsnt_multiplayer_message_2"),
	])

#script_check_team_balance
# INPUT: none
# OUTPUT: none
check_team_balance = ("check_team_balance",
		[
			(try_begin),
				(multiplayer_is_server),
				
				(assign, ":number_of_players_at_team_1", 0),
				(assign, ":number_of_players_at_team_2", 0),
				(get_max_players, ":num_players"),
				(try_for_range, ":cur_player", 0, ":num_players"),
					(player_is_active, ":cur_player"),
					(player_get_team_no, ":player_team", ":cur_player"),
					(try_begin),
						(eq, ":player_team", 0),
						(val_add, ":number_of_players_at_team_1", 1),
					(else_try),
						(eq, ":player_team", 1),
						(val_add, ":number_of_players_at_team_2", 1),
					(try_end),
				(try_end),
				
				(store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
				(assign, ":number_of_players_will_be_moved", 0),
				(try_begin),
					(try_begin),
						(store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
						(le, ":difference_of_number_of_players", ":checked_value"),
						(store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
						(assign, ":team_with_more_players", 1),
						(assign, ":team_with_less_players", 0),
					(else_try),
						(ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
						(store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
						(assign, ":team_with_more_players", 0),
						(assign, ":team_with_less_players", 1),
					(try_end),
				(try_end),
				#team balance checks are done
				(try_begin),
					(gt, ":number_of_players_will_be_moved", 0),
					(try_begin),
						(eq, "$g_team_balance_next_round", 1), #if warning is given
						
						#auto team balance starts
						(try_for_range, ":unused", 0, ":number_of_players_will_be_moved"),
							(assign, ":max_player_join_time", 0),
							(assign, ":latest_joined_player_no", -1),
							(get_max_players, ":num_players"),
							(try_for_range, ":player_no", 0, ":num_players"),
								(player_is_active, ":player_no"),
								(player_get_team_no, ":player_team", ":player_no"),
								(eq, ":player_team", ":team_with_more_players"),
								(player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
								(try_begin),
									(gt, ":player_join_time", ":max_player_join_time"),
									(assign, ":max_player_join_time", ":player_join_time"),
									(assign, ":latest_joined_player_no", ":player_no"),
								(try_end),
							(try_end),
							(try_begin),
								(ge, ":latest_joined_player_no", 0),
								(try_begin),
									#if player is living add +1 to his kill count because he will get -1 because of team change while living.
									(player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"),
									(ge, ":latest_joined_agent_id", 0),
									(agent_is_alive, ":latest_joined_agent_id"),
									
									(player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
									(val_add, ":player_kill_count", 1),
									(player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),
									
									(player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
									(val_sub, ":player_death_count", 1),
									(player_set_death_count, ":latest_joined_player_no", ":player_death_count"),
									
									(player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
									(val_add, ":player_score", 1),
									(player_set_score, ":latest_joined_player_no", ":player_score"),
									
									(try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
										(player_is_active, ":player_no"),
										(multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
									(try_end),
									
									(player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
									(player_get_gold, ":player_gold", ":latest_joined_player_no"),
									(val_add, ":player_gold", ":old_items_value"),
									(player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
								(end_try),
								
								(player_set_troop_id, ":latest_joined_player_no", -1),
								(player_set_team_no, ":latest_joined_player_no", ":team_with_less_players"),
								(multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
							(try_end),
						(try_end),
						
						#for only server itself-----------------------------------------------------------------------------------------------
						(call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), #0 is useless here
						#for only server itself-----------------------------------------------------------------------------------------------
						(get_max_players, ":num_players"),
						(try_for_range, ":player_no", 1, ":num_players"),
							(player_is_active, ":player_no"),
							(multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
						(try_end),
						(assign, "$g_team_balance_next_round", 0),
						#auto team balance done
					(else_try),
						#tutorial message (next round there will be auto team balance)
						(assign, "$g_team_balance_next_round", 1),
						
						#for only server itself-----------------------------------------------------------------------------------------------
						(call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
						#for only server itself-----------------------------------------------------------------------------------------------
						(get_max_players, ":num_players"),
						(try_for_range, ":player_no", 1, ":num_players"),
							(player_is_active, ":player_no"),
							(multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
						(try_end),
					(try_end),
				(else_try),
					(assign, "$g_team_balance_next_round", 0),
				(try_end),
			(try_end),
	])
	
	#script_money_management_after_agent_death
	# INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
	# OUTPUT: none
money_management_after_agent_death =	("money_management_after_agent_death",
		[
			(store_script_param, ":killer_agent_no", 1),
			(store_script_param, ":dead_agent_no", 2),
			
			(assign, ":dead_agent_player_id", -1),
			
			(try_begin),
				(multiplayer_is_server),
				(ge, ":killer_agent_no", 0),
				(ge, ":dead_agent_no", 0),
				(agent_is_human, ":dead_agent_no"), #if dead agent is not horse
				(agent_is_human, ":killer_agent_no"), #if killer agent is not horse
				(agent_get_team, ":killer_agent_team", ":killer_agent_no"),
				(agent_get_team, ":dead_agent_team", ":dead_agent_no"),
				
				(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
				(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
				(neq, ":killer_agent_team", ":dead_agent_team"), #if these agents are enemies
				
				(neq, ":dead_agent_no", ":killer_agent_no"), #if agents are different, do not remove it is needed because in deathmatch mod, self killing passes here because of this or next.
				
				(try_begin),
					(neg|agent_is_non_player, ":dead_agent_no"),
					(agent_get_player_id, ":dead_player_no", ":dead_agent_no"),
					(player_get_slot, ":dead_agent_equipment_value", ":dead_player_no", slot_player_total_equipment_value),
				(else_try),
					(assign, ":dead_agent_equipment_value", 0),
				(try_end),
				
				(assign, ":dead_agent_team_human_players_count", 0),
				(get_max_players, ":num_players"),
				(try_for_range, ":player_no", 0, ":num_players"),
					(player_is_active, ":player_no"),
					(player_get_team_no, ":player_team", ":player_no"),
					(eq, ":player_team", ":dead_agent_team"),
					(val_add, ":dead_agent_team_human_players_count", 1),
				(try_end),
				
				(try_for_range, ":player_no", 0, ":num_players"),
					(player_is_active, ":player_no"),
					
					(try_begin),
						(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
						(eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
						(assign, ":one_spawn_per_round_game_type", 1),
					(else_try),
						(assign, ":one_spawn_per_round_game_type", 0),
					(try_end),
					
					(this_or_next|eq, ":one_spawn_per_round_game_type", 0),
					(this_or_next|player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),
					(player_slot_eq, ":player_no", slot_player_spawned_this_round, 1),
					
					(player_get_agent_id, ":agent_no", ":player_no"),
					(try_begin),
						(eq, ":agent_no", ":dead_agent_no"), #if this agent is dead agent then get share from total loot. (20% of total equipment value)
						(player_get_gold, ":player_gold", ":player_no"),
						
						(assign, ":dead_agent_player_id", ":player_no"),
						
						#dead agent loot share (32%-48%-64%, norm : 48%)
						(store_mul, ":share_of_dead_agent", ":dead_agent_equipment_value", multi_dead_agent_loot_percentage_share),
						(val_div, ":share_of_dead_agent", 100),
						(val_mul, ":share_of_dead_agent", "$g_multiplayer_battle_earnings_multiplier"),
						(val_div, ":share_of_dead_agent", 100),
						(try_begin),
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #(4/3x) share if current mod is deathmatch
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #(4/3x) share if current mod is duel
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #(4/3x) share if current mod is team_deathmatch
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag), #(4/3x) share if current mod is capture the flag
							(eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #(4/3x) share if current mod is headquarters
							(val_mul, ":share_of_dead_agent", 4),
							(val_div, ":share_of_dead_agent", 3),
							(val_add, ":player_gold", ":share_of_dead_agent"),
						(else_try),
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #(2/3x) share if current mod is battle
							(eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #(2/3x) share if current mod is fight and destroy
							(val_mul, ":share_of_dead_agent", 2),
							(val_div, ":share_of_dead_agent", 3),
							(val_add, ":player_gold", ":share_of_dead_agent"),
						(else_try),
							(val_add, ":player_gold", ":share_of_dead_agent"), #(3/3x) share if current mod is siege
						(try_end),
						(player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
					(else_try),
						(eq, ":agent_no", ":killer_agent_no"), #if this agent is killer agent then get share from total loot. (10% of total equipment value)
						(player_get_gold, ":player_gold", ":player_no"),
						
						#killer agent standart money (100-150-200, norm : 150)
						(assign, ":killer_agent_standard_money_addition", multi_killer_agent_standard_money_add),
						(val_mul, ":killer_agent_standard_money_addition", "$g_multiplayer_battle_earnings_multiplier"),
						(val_div, ":killer_agent_standard_money_addition", 100),
						(try_begin),
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #(4/3x) share if current mod is deathmatch
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #(4/3x) share if current mod is duel
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #(4/3x) share if current mod is team_deathmatch
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag), #(4/3x) share if current mod is capture the flag
							(eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #(4/3x) share if current mod is headquarters
							(val_mul, ":killer_agent_standard_money_addition", 4),
							(val_div, ":killer_agent_standard_money_addition", 3),
							(val_add, ":player_gold", ":killer_agent_standard_money_addition"),
						(else_try),
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #(2/3x) share if current mod is battle
							(eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #(2/3x) share if current mod is fight and destroy
							(val_mul, ":killer_agent_standard_money_addition", 2),
							(val_div, ":killer_agent_standard_money_addition", 3),
							(val_add, ":player_gold", ":killer_agent_standard_money_addition"),
						(else_try),
							(val_add, ":player_gold", ":killer_agent_standard_money_addition"), #(3/3x) share if current mod is siege
						(try_end),
						
						#killer agent loot share (8%-12%-16%, norm : 12%)
						(store_mul, ":share_of_killer_agent", ":dead_agent_equipment_value", multi_killer_agent_loot_percentage_share),
						(val_div, ":share_of_killer_agent", 100),
						(val_mul, ":share_of_killer_agent", "$g_multiplayer_battle_earnings_multiplier"),
						(val_div, ":share_of_killer_agent", 100),
						(try_begin),
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #(4/3x) share if current mod is deathmatch
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #(4/3x) share if current mod is duel
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #(4/3x) share if current mod is team_deathmatch
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag), #(4/3x) share if current mod is capture the flag
							(eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #(4/3x) share if current mod is headquarters
							(val_mul, ":share_of_killer_agent", 4),
							(val_div, ":share_of_killer_agent", 3),
							(val_add, ":player_gold", ":share_of_killer_agent"),
						(else_try),
							(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #(2/3x) share if current mod is battle
							(eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #(2/3x) share if current mod is fight and destroy
							(val_mul, ":share_of_killer_agent", 2),
							(val_div, ":share_of_killer_agent", 3),
							(val_add, ":player_gold", ":share_of_killer_agent"),
						(else_try),
							(val_add, ":player_gold", ":share_of_killer_agent"), #(3/3x) share if current mod is siege
						(try_end),
						(player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
					(try_end),
				(try_end),
			(try_end),
			
			#(below lines added new at 25.11.09 after Armagan decided new money system)
			(try_begin),
				(multiplayer_is_server),
				(neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
				(neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
				
				(ge, ":dead_agent_no", 0),
				(agent_is_human, ":dead_agent_no"), #if dead agent is not horse
				(agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
				(ge, ":dead_agent_player_id", 0),
				
				(player_get_gold, ":player_gold", ":dead_agent_player_id"),
				(try_begin),
					(store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
					(lt, ":player_gold", ":minimum_gold"),
					(assign, ":player_gold", ":minimum_gold"),
				(try_end),
				(player_set_gold, ":dead_agent_player_id", ":player_gold"),
			(try_end),
			#new money system addition end
	])
	
#script_use_item
	# INPUT: arg1 = agent_id, arg2 = instance_id
	# OUTPUT: none
use_item =	("use_item",
		[
			(store_script_param, ":instance_id", 1),
			(store_script_param, ":user_id", 2),
			
			(try_begin),
				(game_in_multiplayer_mode),
				(prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
				(eq, ":scene_prop_id", "spr_winch_b"),
				
				(multiplayer_get_my_player, ":my_player_no"),
				
				(this_or_next|gt, ":my_player_no", 0),
				(neg|multiplayer_is_dedicated_server),
				
				(ge, ":my_player_no", 0),
				(player_get_agent_id, ":my_agent_id", ":my_player_no"),
				(ge, ":my_agent_id", 0),
				(agent_is_active, ":my_agent_id"),
				(agent_get_team, ":my_team_no", ":my_agent_id"),
				(eq, ":my_team_no", 0),
				
				(scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
				(ge, ":user_id", 0),
				(agent_is_active, ":user_id"),
				(agent_get_player_id, ":user_player", ":user_id"),
				(str_store_player_username, s7, ":user_player"),
				
				(try_begin),
					(eq, ":opened_or_closed", 0),
					(display_message, "@{s7} opened the gate"),
				(else_try),
					(display_message, "@{s7} closed the gate"),
				(try_end),
			(try_end),
			
			(prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
			
			(try_begin),
				(this_or_next|eq, ":scene_prop_id", "spr_winch_b"),
				(eq, ":scene_prop_id", "spr_winch"),
				(assign, ":effected_object", "spr_portcullis"),
			(else_try),
				(this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
				(this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
				(this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
				(this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
				(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
				(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
				(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
				(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
				(this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
				(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
				(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
				(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
				(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
				(eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
				(assign, ":effected_object", ":scene_prop_id"),
			(try_end),
			
			(assign, ":smallest_dist", -1),
			(prop_instance_get_position, pos0, ":instance_id"),
			(scene_prop_get_num_instances, ":num_instances_of_effected_object", ":effected_object"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_effected_object"),
				(scene_prop_get_instance, ":cur_instance_id", ":effected_object", ":cur_instance"),
				(prop_instance_get_position, pos1, ":cur_instance_id"),
				(get_sq_distance_between_positions, ":dist", pos0, pos1),
				(this_or_next|eq, ":smallest_dist", -1),
				(lt, ":dist", ":smallest_dist"),
				(assign, ":smallest_dist", ":dist"),
				(assign, ":effected_object_instance_id", ":cur_instance_id"),
			(try_end),
			
			(try_begin),
				(ge, ":instance_id", 0),
				(ge, ":smallest_dist", 0),
				
				(try_begin),
					(eq, ":effected_object", "spr_portcullis"),
					(scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
					
					(try_begin),
						(eq, ":opened_or_closed", 0), #open gate
						
						(scene_prop_enable_after_time, ":instance_id", 400), #4 seconds
						(try_begin),
							(this_or_next|multiplayer_is_server),
							(neg|game_in_multiplayer_mode),
							(prop_instance_get_position, pos0, ":effected_object_instance_id"),
							(position_move_z, pos0, 375),
							(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 400),
						(try_end),
						(scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 1),
						
						(try_begin),
							(eq, ":scene_prop_id", "spr_winch_b"),
							(this_or_next|multiplayer_is_server),
							(neg|game_in_multiplayer_mode),
							(prop_instance_get_position, pos1, ":instance_id"),
							(prop_instance_rotate_to_position, ":instance_id", pos1, 400, 72000),
						(try_end),
					(else_try), #close gate
						(scene_prop_enable_after_time, ":instance_id", 400), #4 seconds
						(try_begin),
							(this_or_next|multiplayer_is_server),
							(neg|game_in_multiplayer_mode),
							(prop_instance_get_position, pos0, ":effected_object_instance_id"),
							(position_move_z, pos0, -375),
							(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 400),
						(try_end),
						(scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 0),
						
						(try_begin),
							(eq, ":scene_prop_id", "spr_winch_b"),
							(this_or_next|multiplayer_is_server),
							(neg|game_in_multiplayer_mode),
							(prop_instance_get_position, pos1, ":instance_id"),
							(prop_instance_rotate_to_position, ":instance_id", pos1, 400, -72000),
						(try_end),
					(try_end),
				(else_try),
					(this_or_next|eq, ":effected_object", "spr_siege_ladder_move_6m"),
					(this_or_next|eq, ":effected_object", "spr_siege_ladder_move_8m"),
					(this_or_next|eq, ":effected_object", "spr_siege_ladder_move_10m"),
					(this_or_next|eq, ":effected_object", "spr_siege_ladder_move_12m"),
					(eq, ":effected_object", "spr_siege_ladder_move_14m"),
					
					(try_begin),
						(eq, ":effected_object", "spr_siege_ladder_move_6m"),
						(assign, ":animation_time_drop", 120),
						(assign, ":animation_time_elevate", 240),
					(else_try),
						(eq, ":effected_object", "spr_siege_ladder_move_8m"),
						(assign, ":animation_time_drop", 140),
						(assign, ":animation_time_elevate", 280),
					(else_try),
						(eq, ":effected_object", "spr_siege_ladder_move_10m"),
						(assign, ":animation_time_drop", 160),
						(assign, ":animation_time_elevate", 320),
					(else_try),
						(eq, ":effected_object", "spr_siege_ladder_move_12m"),
						(assign, ":animation_time_drop", 190),
						(assign, ":animation_time_elevate", 360),
					(else_try),
						(eq, ":effected_object", "spr_siege_ladder_move_14m"),
						(assign, ":animation_time_drop", 230),
						(assign, ":animation_time_elevate", 400),
					(try_end),
					
					(scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
					
					(try_begin),
						(scene_prop_enable_after_time, ":effected_object_instance_id", ":animation_time_elevate"), #3 seconds in average
						(eq, ":opened_or_closed", 0), #ladder at ground
						(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
						(prop_instance_enable_physics, ":effected_object_instance_id", 0),
						(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 300),
						(scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 1),
					(else_try), #ladder at wall
						(scene_prop_enable_after_time, ":effected_object_instance_id", ":animation_time_drop"), #1.5 seconds in average
						(prop_instance_get_position, pos0, ":instance_id"),
						
						(assign, ":smallest_dist", -1),
						(try_for_range, ":entry_point_no", multi_entry_points_for_usable_items_start, multi_entry_points_for_usable_items_end),
							(entry_point_get_position, pos1, ":entry_point_no"),
							(get_sq_distance_between_positions, ":dist", pos0, pos1),
							(this_or_next|eq, ":smallest_dist", -1),
							(lt, ":dist", ":smallest_dist"),
							(assign, ":smallest_dist", ":dist"),
							(assign, ":nearest_entry_point", ":entry_point_no"),
						(try_end),
						
						(try_begin),
							(ge, ":smallest_dist", 0),
							(lt, ":smallest_dist", 22500), #max 15m distance
							(entry_point_get_position, pos1, ":nearest_entry_point"),
							(position_rotate_x, pos1, -90),
							(scene_prop_set_slot, ":effected_object_instance_id", scene_prop_smoke_effect_done, 0),
							(prop_instance_enable_physics, ":effected_object_instance_id", 0),
							(prop_instance_animate_to_position, ":effected_object_instance_id", pos1, 130),
						(try_end),
						
						(scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 0),
					(try_end),
				(else_try),
					(this_or_next|eq, ":effected_object", "spr_door_destructible"),
					(this_or_next|eq, ":effected_object", "spr_castle_f_door_b"),
					(this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
					(this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
					(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
					(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
					(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
					(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
					(eq, ":scene_prop_id", "spr_castle_f_door_a"),
					
					(assign, ":effected_object_instance_id", ":instance_id"),
					(scene_prop_get_slot, ":opened_or_closed", ":effected_object_instance_id", scene_prop_open_or_close_slot),
					
					(try_begin),
						(eq, ":opened_or_closed", 0),
						
						(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
						
						(scene_prop_enable_after_time, ":effected_object_instance_id", 100),
						
						(try_begin),
							(neg|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
							(neg|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
							
							(position_rotate_z, pos0, -85),
						(else_try),
							(position_rotate_z, pos0, 85),
						(try_end),
						
						(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 100),
						
						(scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 1),
					(else_try),
						(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
						
						(scene_prop_enable_after_time, ":effected_object_instance_id", 100),
						
						(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 100),
						
						(scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 0),
					(try_end),
				(try_end),
			(try_end),
	])

#script_determine_team_flags
	# INPUT: none
	# OUTPUT: none
determine_team_flags =	("determine_team_flags",
		[
			(store_script_param, ":team_no", 1),
			
			(try_begin),
				(eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
				
				(try_begin),
					(eq, ":team_no", 0),
					
					(team_get_faction, ":team_faction_no", 0),
					(try_begin),
						(eq, ":team_faction_no", "fac_kingdom_1"),
						(assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_1"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_2"),
						(assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_2"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_3"),
						(assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_3"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_4"),
						(assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_4"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_5"),
						(assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_5"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_6"),
						(assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_6"),
					(try_end),
				(else_try),
					(team_get_faction, ":team_faction_no", 1),
					(try_begin),
						(eq, ":team_faction_no", "fac_kingdom_1"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_1"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_2"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_2"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_3"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_3"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_4"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_4"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_5"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_5"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_6"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_6"),
					(try_end),
					
					(try_begin),
						(eq, "$team_1_flag_scene_prop", "$team_2_flag_scene_prop"),
						(assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_7"),
					(try_end),
				(try_end),
			(else_try),
				(try_begin),
					(eq, ":team_no", 0),
					
					(team_get_faction, ":team_faction_no", 0),
					(try_begin),
						(eq, ":team_faction_no", "fac_kingdom_1"),
						(assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_swadian"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_2"),
						(assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_vaegir"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_3"),
						(assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_khergit"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_4"),
						(assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_nord"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_5"),
						(assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_rhodok"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_6"),
						(assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_sarranid"),
					(try_end),
				(else_try),
					(team_get_faction, ":team_faction_no", 1),
					(try_begin),
						(eq, ":team_faction_no", "fac_kingdom_1"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_swadian"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_2"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_vaegir"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_3"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_khergit"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_4"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_nord"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_5"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_rhodok"),
					(else_try),
						(eq, ":team_faction_no", "fac_kingdom_6"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_sarranid"),
					(try_end),
					
					(try_begin),
						(eq, "$team_1_flag_scene_prop", "$team_2_flag_scene_prop"),
						(assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_rebel"),
					(try_end),
				(try_end),
			(try_end),
	])

#script_calculate_flag_move_time
	# INPUT: arg1 = number_of_total_agents_around_flag, arg2 = dist_between_flag_and_its_pole
	# OUTPUT: reg0 = flag move time
calculate_flag_move_time =	("calculate_flag_move_time",
		[
			(store_script_param, ":number_of_total_agents_around_flag", 1),
			(store_script_param, ":dist_between_flag_and_its_target", 2),
			
			(try_begin), #(if no one is around flag it again moves to its current owner situation but 5 times slower than normal)
				(eq, ":number_of_total_agents_around_flag", 0),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 2500),#5.00 * 1.00 * (500 stable) = 2000
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 1),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 500), #1.00 * (500 stable) = 500
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 2),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 300), #0.60(0.60) * (500 stable) = 300
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 3),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 195), #0.39(0.60 * 0.65) * (500 stable) = 195
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 4),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 137), #0.273(0.60 * 0.65 * 0.70) * (500 stable) = 136.5 >rounding> 137
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 5),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 102), #0.20475(0.60 * 0.65 * 0.70 * 0.75) * (500 stable) = 102.375 >rounding> 102
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 6),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 82),  #0.1638(0.60 * 0.65 * 0.70 * 0.75 * 0.80) * (500 stable) = 81.9 >rounding> 82
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 7),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 66),  #0.13104(0.60 * 0.65 * 0.70 * 0.75 * 0.80 * 0.85) * (500 stable) = 65.52 >rounding> 66
			(else_try),
				(eq, ":number_of_total_agents_around_flag", 8),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 59),  #0.117936(0.60 * 0.65 * 0.70 * 0.75 * 0.80 * 0.85 * 0.90) * (500 stable) = 58.968 >rounding> 59
			(else_try),
				(store_mul, reg0, ":dist_between_flag_and_its_target", 56),  #0.1120392(0.60 * 0.65 * 0.70 * 0.75 * 0.80 * 0.85 * 0.90 * 0.95) * (500 stable) = 56.0196 >rounding> 56
			(try_end),
			
			(assign, ":number_of_players", 0),
			(get_max_players, ":num_players"),
			(try_for_range, ":cur_player", 0, ":num_players"),
				(player_is_active, ":cur_player"),
				(val_add, ":number_of_players", 1),
			(try_end),
			
			(try_begin),
				(lt, ":number_of_players", 10),
				(val_mul, reg0, 50),
			(else_try),
				(lt, ":number_of_players", 35),
				(store_sub, ":number_of_players_multipication", 35, ":number_of_players"),
				(val_mul, ":number_of_players_multipication", 2),
				(store_sub, ":number_of_players_multipication", 100, ":number_of_players_multipication"),
				(val_mul, reg0, ":number_of_players_multipication"),
			(else_try),
				(val_mul, reg0, 100),
			(try_end),
			
			(try_begin),
				(eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
				(val_mul, reg0, 2),
			(try_end),
			
			(val_div, reg0, 10000), #100x for number of players around flag, 100x for number of players in game
	])

#script_move_death_mode_flags_down
	# INPUT: none
	# OUTPUT: none
move_death_mode_flags_down = ("move_death_mode_flags_down",
		[
			(try_begin),
				(scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
				(prop_instance_get_position, pos0, ":pole_1_id"),
				(position_move_z, pos0, -2000),
				(prop_instance_set_position, ":pole_1_id", pos0),
			(try_end),
			
			(try_begin),
				(scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
				(prop_instance_get_position, pos1, ":pole_2_id"),
				(position_move_z, pos1, -2000),
				(prop_instance_set_position, ":pole_2_id", pos1),
			(try_end),
			
			(try_begin),
				(scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
				(prop_instance_get_position, pos0, ":pole_1_id"),
				(scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
				(prop_instance_stop_animating, ":flag_1_id"),
				(position_move_z, pos0, multi_headquarters_flag_initial_height),
				(prop_instance_set_position, ":flag_1_id", pos0),
			(try_end),
			
			(try_begin),
				(scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
				(prop_instance_get_position, pos1, ":pole_2_id"),
				(scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),
				(prop_instance_stop_animating, ":flag_2_id"),
				(position_move_z, pos1, multi_headquarters_flag_initial_height),
				(prop_instance_set_position, ":flag_2_id", pos1),
			(try_end),
	])

#script_move_flag
	# INPUT: arg1 = shown_flag_id, arg2 = move time in seconds, pos0 = target position
	# OUTPUT: none
move_flag=	("move_flag",
		[
			(store_script_param, ":shown_flag_id", 1),
			(store_script_param, ":shown_flag_move_time", 2),
			
			(try_begin),
				(multiplayer_is_server), #added after auto-animating
				
				(try_begin),
					(eq, ":shown_flag_move_time", 0), #stop
					(prop_instance_stop_animating, ":shown_flag_id"),
				(else_try),
					(prop_instance_animate_to_position, ":shown_flag_id", pos0, ":shown_flag_move_time"),
				(try_end),
			(try_end),
	])

#script_move_headquarters_flags
	# INPUT: arg1 = current_owner, arg2 = number_of_agents_around_flag_team_1, arg3 = number_of_agents_around_flag_team_2
	# OUTPUT: none
move_headquarters_flags =	("move_headquarters_flags",
		[
			(store_script_param, ":flag_no", 1),
			(store_script_param, ":number_of_agents_around_flag_team_1", 2),
			(store_script_param, ":number_of_agents_around_flag_team_2", 3),
			
			(store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":flag_no"),
			(troop_get_slot, ":current_owner", "trp_multiplayer_data", ":cur_flag_slot"),
			
			(scene_prop_get_num_instances, ":num_instances", "spr_headquarters_flag_gray_code_only"),
			(try_begin),
				(assign, ":visibility", 0),
				(lt, ":flag_no", ":num_instances"),
				(scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
				(scene_prop_get_visibility, ":visibility", ":flag_id"),
			(try_end),
			
			(try_begin),
				(eq, ":visibility", 1),
				(assign, ":shown_flag", 0),
				(assign, ":shown_flag_id", ":flag_id"),
			(else_try),
				(scene_prop_get_num_instances, ":num_instances", "$team_1_flag_scene_prop"),
				(try_begin),
					(assign, ":visibility", 0),
					(lt, ":flag_no", ":num_instances"),
					(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
					(scene_prop_get_visibility, ":visibility", ":flag_id"),
				(try_end),
				
				#(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
				#(scene_prop_get_visibility, ":visibility", ":flag_id"),
				(try_begin),
					(eq, ":visibility", 1),
					(assign, ":shown_flag", 1),
					(assign, ":shown_flag_id", ":flag_id"),
				(else_try),
					(scene_prop_get_num_instances, ":num_instances", "$team_2_flag_scene_prop"),
					(try_begin),
						(assign, ":visibility", 0),
						(lt, ":flag_no", ":num_instances"),
						(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
						(scene_prop_get_visibility, ":visibility", ":flag_id"),
					(try_end),
					
					#(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
					#(scene_prop_get_visibility, ":visibility", ":flag_id"),
					(try_begin),
						(eq, ":visibility", 1),
						(assign, ":shown_flag", 2),
						(assign, ":shown_flag_id", ":flag_id"),
					(try_end),
				(try_end),
			(try_end),
			
			(try_begin),
				(scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
			(try_end),
			
			(try_begin),
				(eq, ":shown_flag", ":current_owner"), #situation 1 : (current owner is equal shown flag)
				(try_begin),
					(ge, ":number_of_agents_around_flag_team_1", 1),
					(ge, ":number_of_agents_around_flag_team_2", 1),
					(assign, ":flag_movement", 0), #0:stop
				(else_try),
					(eq, ":number_of_agents_around_flag_team_1", 0),
					(eq, ":number_of_agents_around_flag_team_2", 0),
					(assign, ":flag_movement", 1), #1:rise (slow)
				(else_try),
					(try_begin),
						(ge, ":number_of_agents_around_flag_team_1", 1),
						(eq, ":number_of_agents_around_flag_team_2", 0),
						(eq, ":current_owner", 1),
						(assign, ":flag_movement", 1), #1:rise (fast)
					(else_try),
						(eq, ":number_of_agents_around_flag_team_1", 0),
						(ge, ":number_of_agents_around_flag_team_2", 1),
						(eq, ":current_owner", 2),
						(assign, ":flag_movement", 1), #1:rise (fast)
					(else_try),
						(assign, ":flag_movement", -1), #-1:drop (fast)
					(try_end),
				(try_end),
			(else_try), #situation 2 : (current owner is different than shown flag)
				(try_begin),
					(ge, ":number_of_agents_around_flag_team_1", 1),
					(ge, ":number_of_agents_around_flag_team_2", 1),
					(assign, ":flag_movement", 0), #0:stop
				(else_try),
					(eq, ":number_of_agents_around_flag_team_1", 0),
					(eq, ":number_of_agents_around_flag_team_2", 0),
					(assign, ":flag_movement", -1), #-1:drop (slow)
				(else_try),
					(try_begin),
						(ge, ":number_of_agents_around_flag_team_1", 1),
						(eq, ":number_of_agents_around_flag_team_2", 0),
						(try_begin),
							(eq, ":shown_flag", 1),
							(assign, ":flag_movement", 1), #1:rise (fast)
						(else_try),
							(neq, ":current_owner", 1),
							(assign, ":flag_movement", -1), #-1:drop (fast)
						(try_end),
					(else_try),
						(eq, ":number_of_agents_around_flag_team_1", 0),
						(ge, ":number_of_agents_around_flag_team_2", 1),
						(try_begin),
							(eq, ":shown_flag", 2),
							(assign, ":flag_movement", 1), #1:rise (fast)
						(else_try),
							(neq, ":current_owner", 2),
							(assign, ":flag_movement", -1), #-1:drop (fast)
						(try_end),
					(try_end),
				(try_end),
			(try_end),
			
			(store_add, ":number_of_total_agents_around_flag", ":number_of_agents_around_flag_team_1", ":number_of_agents_around_flag_team_2"),
			
			(try_begin),
				(eq, ":flag_movement", 0),
				(assign, reg0, 0),
			(else_try),
				(eq, ":flag_movement", 1),
				(prop_instance_get_position, pos1, ":shown_flag_id"),
				(prop_instance_get_position, pos0, ":pole_id"),
				(position_move_z, pos0, multi_headquarters_pole_height),
				(get_distance_between_positions, ":dist_between_flag_and_its_target", pos0, pos1),
				(call_script, "script_calculate_flag_move_time", ":number_of_total_agents_around_flag", ":dist_between_flag_and_its_target"),
			(else_try),
				(eq, ":flag_movement", -1),
				(prop_instance_get_position, pos1, ":shown_flag_id"),
				(prop_instance_get_position, pos0, ":pole_id"),
				(get_distance_between_positions, ":dist_between_flag_and_its_target", pos0, pos1),
				(call_script, "script_calculate_flag_move_time", ":number_of_total_agents_around_flag", ":dist_between_flag_and_its_target"),
			(try_end),
			
			(call_script, "script_move_flag", ":shown_flag_id", reg0), #pos0 : target position
	])

#script_set_num_agents_around_flag
	# INPUT: arg1 = flag_no, arg2 = owner_code
	# OUTPUT: none
set_num_agents_around_flag =	("set_num_agents_around_flag",
		[
			(store_script_param, ":flag_no", 1),
			(store_script_param, ":current_owner_code", 2),
			
			(store_div, ":number_of_agents_around_flag_team_1", ":current_owner_code", 100),
			(store_mod, ":number_of_agents_around_flag_team_2", ":current_owner_code", 100),
			
			(store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
			(troop_set_slot, "trp_multiplayer_data", ":cur_flag_owner_counts_slot", ":current_owner_code"),
			
			(call_script, "script_move_headquarters_flags", ":flag_no", ":number_of_agents_around_flag_team_1", ":number_of_agents_around_flag_team_2"),
	])

#script_change_flag_owner
	# INPUT: arg1 = flag_no, arg2 = owner_code
	# OUTPUT: none
change_flag_owner = ("change_flag_owner",
		[
			(store_script_param, ":flag_no", 1),
			(store_script_param, ":owner_code", 2),
			
			(try_begin),
				(lt, ":owner_code", 0),
				(val_add, ":owner_code", 1),
				(val_mul, ":owner_code", -1),
			(try_end),
			
			(store_div, ":owner_team_no", ":owner_code", 100),
			(store_mod, ":shown_flag_no", ":owner_code", 100),
			
			(store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":flag_no"),
			(troop_get_slot, ":older_owner_team_no", "trp_multiplayer_data", ":cur_flag_slot"),
			
			(store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":flag_no"),
			(troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", ":owner_team_no"),
			
			#senchronizing flag positions
			(try_begin),
				#(this_or_next|eq, ":initial_flags", 0), #moved after auto-animating
				(multiplayer_is_server),
				
				(scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
				(try_begin),
					(eq, ":owner_team_no", 0), #if new owner team is 0 then flags are at bottom
					(neq, ":older_owner_team_no", -1), #clients
					(assign, ":continue", 1),
					(try_begin),
						(multiplayer_is_server),
						(eq, "$g_placing_initial_flags", 1),
						(assign, ":continue", 0),
					(try_end),
					(eq, ":continue", 1),
					(prop_instance_get_position, pos0, ":pole_id"),
					(position_move_z, pos0, multi_headquarters_distance_to_change_flag),
				(else_try),
					(prop_instance_get_position, pos0, ":pole_id"), #if new owner team is not 0 then flags are at top
					(position_move_z, pos0, multi_headquarters_pole_height),
				(try_end),
				
				(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
				(prop_instance_stop_animating, ":flag_id"),
				(prop_instance_set_position, ":flag_id", pos0),
				
				(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
				(prop_instance_stop_animating, ":flag_id"),
				(prop_instance_set_position, ":flag_id", pos0),
				
				(scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
				(prop_instance_stop_animating, ":flag_id"),
				(prop_instance_set_position, ":flag_id", pos0),
			(try_end),
			
			#setting visibilities of flags
			(try_begin),
				(eq, ":shown_flag_no", 0),
				(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 0),
				(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 0),
				(scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 1),
			(else_try),
				(eq, ":shown_flag_no", 1),
				(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 1),
				(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 0),
				(scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 0),
			(else_try),
				(eq, ":shown_flag_no", 2),
				(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 0),
				(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 1),
				(scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
				(scene_prop_set_visibility, ":flag_id", 0),
			(try_end),
			
			#other
			(store_add, ":cur_flag_players_around_slot", multi_data_flag_players_around_begin, ":flag_no"),
			(troop_get_slot, ":players_around_code", "trp_multiplayer_data", ":cur_flag_players_around_slot"),
			
			(store_div, ":number_of_agents_around_flag_team_1", ":players_around_code", 100),
			(store_mod, ":number_of_agents_around_flag_team_2", ":players_around_code", 100),
			
			(call_script, "script_move_headquarters_flags", ":flag_no", ":number_of_agents_around_flag_team_1", ":number_of_agents_around_flag_team_2"),
	])

#script_move_object_to_nearest_entry_point
	# INPUT: none
	# OUTPUT: none
move_object_to_nearest_entry_point =	("move_object_to_nearest_entry_point",
		[
			(store_script_param, ":scene_prop_no", 1),
			
			(scene_prop_get_num_instances, ":num_instances", ":scene_prop_no"),
			
			(try_for_range, ":instance_no", 0, ":num_instances"),
				(scene_prop_get_instance, ":instance_id", ":scene_prop_no", ":instance_no"),
				(prop_instance_get_position, pos0, ":instance_id"),
				
				(assign, ":smallest_dist", -1),
				(try_for_range, ":entry_point_no", multi_entry_points_for_usable_items_start, multi_entry_points_for_usable_items_end),
					(entry_point_get_position, pos1, ":entry_point_no"),
					(get_sq_distance_between_positions, ":dist", pos0, pos1),
					(this_or_next|eq, ":smallest_dist", -1),
					(lt, ":dist", ":smallest_dist"),
					(assign, ":smallest_dist", ":dist"),
					(assign, ":nearest_entry_point", ":entry_point_no"),
				(try_end),
				
				(try_begin),
					(ge, ":smallest_dist", 0),
					(lt, ":smallest_dist", 22500), #max 15m distance
					(entry_point_get_position, pos1, ":nearest_entry_point"),
					(position_rotate_x, pos1, -90),
					(prop_instance_animate_to_position, ":instance_id", pos1, 1),
				(try_end),
			(try_end),
	])

	#script_multiplayer_server_on_agent_spawn_common
	# INPUT: arg1 = agent_no
	# OUTPUT: none
multiplayer_server_on_agent_spawn_common =	("multiplayer_server_on_agent_spawn_common",
		[
			(store_script_param, ":agent_no", 1),
			(agent_set_slot, ":agent_no", slot_agent_in_duel_with, -1),
			(try_begin),
				(agent_is_non_player, ":agent_no"),
				(assign, "$g_multiplayer_ready_for_spawning_agent", 1),
			(try_end),
	])

#script_multiplayer_server_player_joined_common
	# INPUT: arg1 = player_no
	# OUTPUT: none
multiplayer_server_player_joined_common =	(
	"multiplayer_server_player_joined_common",
		[
			(store_script_param, ":player_no", 1),
			(try_begin),
				(this_or_next|player_is_active, ":player_no"),
				(eq, ":player_no", 0),
				(call_script, "script_multiplayer_init_player_slots", ":player_no"),
				(store_mission_timer_a, ":player_join_time"),
				(player_set_slot, ":player_no", slot_player_join_time, ":player_join_time"),
				(player_set_slot, ":player_no", slot_player_first_spawn, 1),
				#fight and destroy only
				(player_set_slot, ":player_no", slot_player_damage_given_to_target_1, 0),
				(player_set_slot, ":player_no", slot_player_damage_given_to_target_2, 0),
				#fight and destroy only end
				(try_begin),
					(multiplayer_is_server),
					(assign, ":initial_gold", multi_initial_gold_value),
					(val_mul, ":initial_gold", "$g_multiplayer_initial_gold_multiplier"),
					(val_div, ":initial_gold", 100),
					(player_set_gold, ":player_no", ":initial_gold"),
					(call_script, "script_multiplayer_send_initial_information", ":player_no"),
				(try_end),
			(try_end),
	])

#script_multiplayer_server_before_mission_start_common
	# INPUT: none
	# OUTPUT: none
multiplayer_server_before_mission_start_common =	(
	"multiplayer_server_before_mission_start_common",
		[
			(try_begin),
				(scene_allows_mounted_units),
				(assign, "$g_horses_are_avaliable", 1),
			(else_try),
				(assign, "$g_horses_are_avaliable", 0),
			(try_end),
			(scene_set_day_time, 15),
			(assign, "$g_multiplayer_mission_end_screen", 0),
			
			(get_max_players, ":num_players"),
			(try_for_range, ":player_no", 0, ":num_players"),
				(player_is_active, ":player_no"),
				(call_script, "script_multiplayer_init_player_slots", ":player_no"),
				(assign, ":initial_gold", multi_initial_gold_value),
				(val_mul, ":initial_gold", "$g_multiplayer_initial_gold_multiplier"),
				(val_div, ":initial_gold", 100),
				(player_set_gold, ":player_no", ":initial_gold"),
				(player_set_slot, ":player_no", slot_player_first_spawn, 1), #not required in siege, bt, fd
			(try_end),
	])

#script_multiplayer_server_on_agent_killed_or_wounded_common
	# INPUT: arg1 = dead_agent_no, arg2 = killer_agent_no
	# OUTPUT: none
multiplayer_server_on_agent_killed_or_wounded_common =	("multiplayer_server_on_agent_killed_or_wounded_common",
		[
			(store_script_param, ":dead_agent_no", 1),
			(store_script_param, ":killer_agent_no", 2),
			
			(call_script, "script_multiplayer_event_agent_killed_or_wounded", ":dead_agent_no", ":killer_agent_no"),
			#adding 1 score points to agent which kills enemy agent at server
			(try_begin),
				(multiplayer_is_server),
				(try_begin), #killing myself because of some reason (friend hit, fall, team change)
					(lt, ":killer_agent_no", 0),
					(ge, ":dead_agent_no", 0),
					(neg|agent_is_non_player, ":dead_agent_no"),
					(agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
					(player_is_active, ":dead_agent_player_id"),
					(player_get_score, ":dead_agent_player_score", ":dead_agent_player_id"),
					(val_add, ":dead_agent_player_score", -1),
					(player_set_score, ":dead_agent_player_id", ":dead_agent_player_score"),
				(else_try), #killing teammate
					(ge, ":killer_agent_no", 0),
					(ge, ":dead_agent_no", 0),
					(agent_get_team, ":killer_team_no", ":killer_agent_no"),
					(agent_get_team, ":dead_team_no", ":dead_agent_no"),
					(eq, ":killer_team_no", ":dead_team_no"),
					(neg|agent_is_non_player, ":killer_agent_no"),
					(agent_get_player_id, ":killer_agent_player_id", ":killer_agent_no"),
					(player_is_active, ":killer_agent_player_id"),
					(player_get_score, ":killer_agent_player_score", ":killer_agent_player_id"),
					(val_add, ":killer_agent_player_score", -1),
					(player_set_score, ":killer_agent_player_id", ":killer_agent_player_score"),
					#(player_get_kill_count, ":killer_agent_player_kill_count", ":killer_agent_player_id"),
					#(val_add, ":killer_agent_player_kill_count", -2),
					#(player_set_kill_count, ":killer_agent_player_id", ":killer_agent_player_kill_count"),
				(else_try), #killing enemy
					(ge, ":killer_agent_no", 0),
					(ge, ":dead_agent_no", 0),
					(agent_is_human, ":dead_agent_no"),
					(agent_is_human, ":killer_agent_no"),
					(try_begin),
						(eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
						(try_begin),
							(eq, "$g_battle_death_mode_started", 1),
							(neq, ":dead_agent_no", ":killer_agent_no"),
							(call_script, "script_calculate_new_death_waiting_time_at_death_mod"),
						(try_end),
					(try_end),
					(try_begin),
						(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
						(eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
						(agent_get_player_id, ":dead_player_no", ":dead_agent_no"),
						(try_begin),
							(ge, ":dead_player_no", 0),
							(player_is_active, ":dead_player_no"),
							(neg|agent_is_non_player, ":dead_agent_no"),
							(try_for_agents, ":cur_agent"),
								(agent_is_non_player, ":cur_agent"),
								(agent_is_human, ":cur_agent"),
								(agent_is_alive, ":cur_agent"),
								(agent_get_group, ":agent_group", ":cur_agent"),
								(try_begin),
									(eq, ":dead_player_no", ":agent_group"),
									(agent_set_group, ":cur_agent", -1),
								(try_end),
							(try_end),
						(try_end),
					(try_end),
					(neg|agent_is_non_player, ":killer_agent_no"),
					(agent_get_player_id, ":killer_agent_player_id", ":killer_agent_no"),
					(player_is_active, ":killer_agent_player_id"),
					(player_get_score, ":killer_agent_player_score", ":killer_agent_player_id"),
					(agent_get_team, ":killer_agent_team", ":killer_agent_no"),
					(agent_get_team, ":dead_agent_team", ":dead_agent_no"),
					(try_begin),
						(neq, ":killer_agent_team", ":dead_agent_team"),
						(val_add, ":killer_agent_player_score", 1),
					(else_try),
						(val_add, ":killer_agent_player_score", -1),
					(try_end),
					(player_set_score, ":killer_agent_player_id", ":killer_agent_player_score"),
				(try_end),
			(try_end),
			
			(call_script, "script_add_kill_death_counts", ":killer_agent_no", ":dead_agent_no"),
			#money management
			(call_script, "script_money_management_after_agent_death", ":killer_agent_no", ":dead_agent_no"),
	])

#script_multiplayer_close_gate_if_it_is_open
# INPUT: none
# OUTPUT: none
multiplayer_close_gate_if_it_is_open =	(
	"multiplayer_close_gate_if_it_is_open",
		[
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_winch_b"),
			(try_for_range, ":cur_prop_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":prop_instance_id", "spr_winch_b", ":cur_prop_instance"),
				(scene_prop_slot_eq, ":prop_instance_id", scene_prop_open_or_close_slot, 1),
				(scene_prop_get_instance, ":effected_object_instance_id", "spr_portcullis", ":cur_prop_instance"),
				(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
				(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
			(try_end),
	])

#script_multiplayer_move_moveable_objects_initial_positions
# INPUT: none
# OUTPUT: none
multiplayer_move_moveable_objects_initial_positions =	("multiplayer_move_moveable_objects_initial_positions",
		[
			(call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_6m"),
			(call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_8m"),
			(call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_10m"),
			(call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_12m"),
			(call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_14m"),
	])

#script_team_set_score
# INPUT: arg1 = team_no, arg2 = score
# OUTPUT: none
team_set_score =(
	"team_set_score",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":score", 2),
			
			(team_set_score, ":team_no", ":score"),
	])

#script_player_set_score
# INPUT: arg1 = player_no, arg2 = score
# OUTPUT: none
player_set_score = ("player_set_score",
		[
			(store_script_param, ":player_no", 1),
			(store_script_param, ":score", 2),
			
			(player_set_score, ":player_no", ":score"),
	])

#script_player_set_kill_count
# INPUT: arg1 = player_no, arg2 = score
# OUTPUT: none
player_set_kill_count =	("player_set_kill_count",
		[
			(store_script_param, ":player_no", 1),
			(store_script_param, ":score", 2),
			
			(player_set_kill_count, ":player_no", ":score"),
	])

#script_player_set_death_count
# INPUT: arg1 = player_no, arg2 = score
# OUTPUT: none
player_set_death_count =	("player_set_death_count",
		[
			(store_script_param, ":player_no", 1),
			(store_script_param, ":score", 2),
			
			(player_set_death_count, ":player_no", ":score"),
	])

#script_set_attached_scene_prop
# INPUT: arg1 = agent_id, arg2 = flag_id
# OUTPUT: none
set_attached_scene_prop =	("set_attached_scene_prop",
		[
			(store_script_param, ":agent_id", 1),
			(store_script_param, ":flag_id", 2),
			
			(try_begin), #if current mod is capture the flag and attached scene prop is flag then change flag situation of flag owner team.
				(scene_prop_get_instance, ":red_flag_id", "spr_tutorial_flag_red", 0),
				(scene_prop_get_instance, ":blue_flag_id", "spr_tutorial_flag_blue", 0),
				(assign, ":flag_owner_team", -1),
				(try_begin),
					(ge, ":red_flag_id", 0),
					(eq, ":flag_id", ":red_flag_id"),
					(assign, ":flag_owner_team", 0),
				(else_try),
					(ge, ":blue_flag_id", 0),
					(eq, ":flag_id", ":blue_flag_id"),
					(assign, ":flag_owner_team", 1),
				(try_end),
				(ge, ":flag_owner_team", 0),
				(team_set_slot, ":flag_owner_team", slot_team_flag_situation, 1), #1-stolen flag
			(try_end),
			
			(agent_set_attached_scene_prop, ":agent_id", ":flag_id"),
			(agent_set_attached_scene_prop_x, ":agent_id", 20),
			(agent_set_attached_scene_prop_z, ":agent_id", 50),
	])

#script_set_team_flag_situation
# INPUT: arg1 = team_no, arg2 = score
# OUTPUT: none
set_team_flag_situation =	("set_team_flag_situation",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":flag_situation", 2),
			
			(team_set_slot, ":team_no", slot_team_flag_situation, ":flag_situation"),
	])


#script_start_death_mode
	# INPUT: none
	# OUTPUT: none
start_death_mode =	("start_death_mode",
		[
			(assign, "$g_multiplayer_message_type", multiplayer_message_type_start_death_mode),
			(start_presentation, "prsnt_multiplayer_message_1"),
	])

#script_calculate_new_death_waiting_time_at_death_mod
	# INPUT: none
	# OUTPUT: none
calculate_new_death_waiting_time_at_death_mod =	("calculate_new_death_waiting_time_at_death_mod",
		[
			(assign, ":num_living_players", 0), #count number of living players to find out death wait time
			(try_begin),
				(try_for_agents, ":agent_no"),
					(agent_is_human, ":agent_no"),
					(agent_is_alive, ":agent_no"),
					(val_add, ":num_living_players", 1),
				(try_end),
			(try_end),
			
			(val_add, ":num_living_players", multiplayer_battle_formula_value_a),
			(set_fixed_point_multiplier, 100),
			(store_mul, ":num_living_players", ":num_living_players", 100),
			(store_sqrt, ":sqrt_num_living_players", ":num_living_players"),
			(store_div, "$g_battle_waiting_seconds", multiplayer_battle_formula_value_b, ":sqrt_num_living_players"),
			(store_mission_timer_a, "$g_death_mode_part_1_start_time"),
	])

#script_calculate_number_of_targets_destroyed
	# INPUT: none
	# OUTPUT: none
calculate_number_of_targets_destroyed =	("calculate_number_of_targets_destroyed",
		[
			(assign, "$g_number_of_targets_destroyed", 0),
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_catapult_destructible"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_catapult_destructible", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_get_position, pos1, ":cur_instance_id"),
				(get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1),
				(gt, ":dist", 2), #this can be 0 or 1 too.
				(val_add, "$g_number_of_targets_destroyed", 1),
			(try_end),
			
			(scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_trebuchet_destructible"),
			(try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
				(scene_prop_get_instance, ":cur_instance_id", "spr_trebuchet_destructible", ":cur_instance"),
				(prop_instance_get_starting_position, pos0, ":cur_instance_id"),
				(prop_instance_get_position, pos1, ":cur_instance_id"),
				(get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1),
				(gt, ":dist", 2), #this can be 0 or 1 too.
				(val_add, "$g_number_of_targets_destroyed", 1),
			(try_end),
	])


	#script_show_multiplayer_message
	# INPUT: arg1 = multiplayer_message_type
	# OUTPUT: none
show_multiplayer_message =	("show_multiplayer_message",
		[
			(store_script_param, ":multiplayer_message_type", 1),
			(store_script_param, ":value", 2),
			
			(assign, "$g_multiplayer_message_type", ":multiplayer_message_type"),
			
			(try_begin),
				(eq, ":multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
				
				(try_begin), #end of round in clients
					(neg|multiplayer_is_server),
					(assign, "$g_battle_death_mode_started", 0),
				(try_end),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_auto_team_balance_done),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_2"),
				(assign, "$g_team_balance_next_round", 0),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_auto_team_balance_next),
				(assign, "$g_team_balance_next_round", 1),
				(call_script, "script_warn_player_about_auto_team_balance"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_auto_team_balance_no_need),
				(assign, "$g_team_balance_next_round", 0),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_capture_the_flag_score),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_flag_returned_home),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_capture_the_flag_stole),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_poll_result),
				(assign, "$g_multiplayer_message_value_3", ":value"),
				(start_presentation, "prsnt_multiplayer_message_3"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_flag_neutralized),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_flag_captured),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_flag_is_pulling),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_round_draw),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_target_destroyed),
				
				(try_begin), #destroy score (condition : a target destroyed)
					(eq, "$g_defender_team", 0),
					(assign, ":attacker_team_no", 1),
				(else_try),
					(assign, ":attacker_team_no", 0),
				(try_end),
				
				(team_get_score, ":team_score", ":attacker_team_no"),
				(val_add, ":team_score", 1),
				(call_script, "script_team_set_score", ":attacker_team_no", ":team_score"), #destroy score end
				
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_defenders_saved_n_targets),
				(assign, "$g_multiplayer_message_value_1", ":value"),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(else_try),
				(eq, ":multiplayer_message_type", multiplayer_message_type_attackers_won_the_round),
				(try_begin),
					(eq, "$g_defender_team", 0),
					(assign, "$g_multiplayer_message_value_1", 1),
				(else_try),
					(assign, "$g_multiplayer_message_value_1", 0),
				(try_end),
				(start_presentation, "prsnt_multiplayer_message_1"),
			(try_end),
	])
	
	#script_get_headquarters_scores
	# INPUT: none
	# OUTPUT: reg0 = team_1_num_flags, reg1 = team_2_num_flags
get_headquarters_scores =	("get_headquarters_scores",
		[
			(assign, ":team_1_num_flags", 0),
			(assign, ":team_2_num_flags", 0),
			(try_for_range, ":flag_no", 0, "$g_number_of_flags"),
				(store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
				(troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),
				(neq, ":cur_flag_owner", 0),
				(try_begin),
					(eq, ":cur_flag_owner", 1),
					(val_add, ":team_1_num_flags", 1),
				(else_try),
					(val_add, ":team_2_num_flags", 1),
				(try_end),
			(try_end),
			(assign, reg0, ":team_1_num_flags"),
			(assign, reg1, ":team_2_num_flags"),
	])

	
#script_draw_this_round
# INPUT: arg1 = value
draw_this_round =("draw_this_round",
   [
    (store_script_param, ":value", 1),
    (try_begin),
      (eq, ":value", -9), #destroy mod round end
      (assign, "$g_round_ended", 1),
      (store_mission_timer_a, "$g_round_finish_time"),
      #(assign, "$g_multiplayer_message_value_1", -1),
      #(assign, "$g_multiplayer_message_type", multiplayer_message_type_round_draw),
      #(start_presentation, "prsnt_multiplayer_message_1"),
    (else_try),
      (eq, ":value", -1), #draw
      (assign, "$g_round_ended", 1),
      (store_mission_timer_a, "$g_round_finish_time"),
      (assign, "$g_multiplayer_message_value_1", -1),
      (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_draw),
      (start_presentation, "prsnt_multiplayer_message_1"),
    (else_try), 
      (eq, ":value", 0), #defender wins
      #THIS_IS_OUR_LAND achievement
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
        (multiplayer_get_my_player, ":my_player_no"),
        (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
        (player_get_agent_id, ":my_player_agent", ":my_player_no"),
        (ge, ":my_player_agent", 0),
        (agent_is_alive, ":my_player_agent"),
        (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
        (eq, ":my_player_agent_team_no", 0), #defender
        (unlock_achievement, ACHIEVEMENT_THIS_IS_OUR_LAND),
      (try_end),
      #THIS_IS_OUR_LAND achievement end
      (assign, "$g_round_ended", 1),
      (store_mission_timer_a, "$g_round_finish_time"),
        
      (team_get_faction, ":faction_of_winner_team", 0),
      (team_get_score, ":team_1_score", 0),
      (val_add, ":team_1_score", 1),
      (team_set_score, 0, ":team_1_score"),
      (assign, "$g_winner_team", 0),
      (str_store_faction_name, s1, ":faction_of_winner_team"),

      (assign, "$g_multiplayer_message_value_1", ":value"),
      (try_begin),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),    
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_siege_mode),
      (else_try),
        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
      (try_end),
      (start_presentation, "prsnt_multiplayer_message_1"),
    (else_try), 
      (eq, ":value", 1), #attacker wins
      (assign, "$g_round_ended", 1),
      (store_mission_timer_a, "$g_round_finish_time"),
  
      (team_get_faction, ":faction_of_winner_team", 1),
      (team_get_score, ":team_2_score", 1),
      (val_add, ":team_2_score", 1),
      (team_set_score, 1, ":team_2_score"),
      (assign, "$g_winner_team", 1),
      (str_store_faction_name, s1, ":faction_of_winner_team"),

      (assign, "$g_multiplayer_message_value_1", ":value"),
      (try_begin),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),    
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_siege_mode),
      (else_try),
        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
      (try_end),
      (start_presentation, "prsnt_multiplayer_message_1"),
    (try_end),
    #LAST_MAN_STANDING achievement
    (try_begin),
      (is_between, ":value", 0, 2), #defender or attacker wins
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (multiplayer_get_my_player, ":my_player_no"),
        (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
        (player_get_agent_id, ":my_player_agent", ":my_player_no"),
        (ge, ":my_player_agent", 0),
        (agent_is_alive, ":my_player_agent"),
        (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
        (eq, ":my_player_agent_team_no", ":value"), #winner team
        (unlock_achievement, ACHIEVEMENT_LAST_MAN_STANDING),
      (try_end),
    (try_end),
    #LAST_MAN_STANDING achievement end
    ])   
	
	#script_check_achievement_last_man_standing
	#INPUT: arg1 = value
check_achievement_last_man_standing =	("check_achievement_last_man_standing",
		[
			#LAST_MAN_STANDING achievement
			(try_begin),
				(store_script_param, ":value", 1),
				(is_between, ":value", 0, 2), #defender or attacker wins
				(try_begin),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
					(multiplayer_get_my_player, ":my_player_no"),
					(is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
					(player_get_agent_id, ":my_player_agent", ":my_player_no"),
					(ge, ":my_player_agent", 0),
					(agent_is_alive, ":my_player_agent"),
					(agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
					(eq, ":my_player_agent_team_no", ":value"), #winner team
					(unlock_achievement, ACHIEVEMENT_LAST_MAN_STANDING),
				(try_end),
			(try_end),
			#LAST_MAN_STANDING achievement end
	])
	
	
	#script_find_most_suitable_bot_to_control
	# INPUT: arg1 = value
find_most_suitable_bot_to_control =	("find_most_suitable_bot_to_control",
		[
			(set_fixed_point_multiplier, 100),
			(store_script_param, ":player_no", 1),
			(player_get_team_no, ":player_team", ":player_no"),
			
			(player_get_slot, ":x_coor", ":player_no", slot_player_death_pos_x),
			(player_get_slot, ":y_coor", ":player_no", slot_player_death_pos_y),
			(player_get_slot, ":z_coor", ":player_no", slot_player_death_pos_z),
			
			(init_position, pos0),
			(position_set_x, pos0, ":x_coor"),
			(position_set_y, pos0, ":y_coor"),
			(position_set_z, pos0, ":z_coor"),
			
			(assign, ":most_suitable_bot", -1),
			(assign, ":max_bot_score", -1),
			
			(try_for_agents, ":cur_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_is_non_player, ":cur_agent"),
				(agent_get_team ,":cur_team", ":cur_agent"),
				(eq, ":cur_team", ":player_team"),
				(agent_get_position, pos1, ":cur_agent"),
				
				#getting score for distance of agent to death point (0..3000)
				(get_distance_between_positions_in_meters, ":dist", pos0, pos1),
				
				(try_begin),
					(lt, ":dist", 500),
					(store_sub, ":bot_score", 500, ":dist"),
				(else_try),
					(assign, ":bot_score", 0),
				(try_end),
				(val_mul, ":bot_score", 6),
				
				#getting score for distance of agent to enemy & friend agents (0..300 x agents)
				(try_for_agents, ":cur_agent_2"),
					(agent_is_alive, ":cur_agent_2"),
					(agent_is_human, ":cur_agent_2"),
					(neq, ":cur_agent", ":cur_agent_2"),
					(agent_get_team ,":cur_team_2", ":cur_agent_2"),
					(try_begin),
						(neq, ":cur_team_2", ":player_team"),
						(agent_get_position, pos1, ":cur_agent_2"),
						(get_distance_between_positions, ":dist_2", pos0, pos1),
						(try_begin),
							(lt, ":dist_2", 300),
							(assign, ":enemy_near_score", ":dist_2"),
						(else_try),
							(assign, ":enemy_near_score", 300),
						(try_end),
						(val_add, ":bot_score", ":enemy_near_score"),
					(else_try),
						(agent_get_position, pos1, ":cur_agent_2"),
						(get_distance_between_positions, ":dist_2", pos0, pos1),
						(try_begin),
							(lt, ":dist_2", 300),
							(assign, ":friend_near_score", 300, ":dist_2"),
						(else_try),
							(assign, ":friend_near_score", 0),
						(try_end),
						(val_add, ":bot_score", ":friend_near_score"),
					(try_end),
				(try_end),
				
				#getting score for health (0..200)
				(store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
				(val_mul, ":agent_hit_points", 2),
				(val_add, ":bot_score", ":agent_hit_points"),
				
				(ge, ":bot_score", ":max_bot_score"),
				(assign, ":max_bot_score", ":bot_score"),
				(assign, ":most_suitable_bot", ":cur_agent"),
			(try_end),
			
			(assign, reg0, ":most_suitable_bot"),
	])
	
	#script_game_receive_url_response
	#response format should be like this:
	#  [a number or a string]|[another number or a string]|[yet another number or a string] ...
	# here is an example response:
	# 12|Player|100|another string|142|323542|34454|yet another string
	# INPUT: arg1 = num_integers, arg2 = num_strings
	# reg0, reg1, reg2, ... up to 128 registers contain the integer values
	# s0, s1, s2, ... up to 128 strings contain the string values
game_receive_url_response =	("game_receive_url_response",
		[
			#here is an example usage
			##      (store_script_param, ":num_integers", 1),
			##      (store_script_param, ":num_strings", 2),
			##      (try_begin),
			##        (gt, ":num_integers", 4),
			##        (display_message, "@{reg0}, {reg1}, {reg2}, {reg3}, {reg4}"),
			##      (try_end),
			##      (try_begin),
			##        (gt, ":num_strings", 4),
			##        (display_message, "@{s0}, {s1}, {s2}, {s3}, {s4}"),
			##      (try_end),
	])

#script_game_receive_network_message
# This script is called from the game engine when a new network message is received.
# INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
game_receive_network_message = (
	"game_receive_network_message",
		[
			(store_script_param, ":player_no", 1),
			(store_script_param, ":event_type", 2),
			(try_begin),
				###############
				#SERVER EVENTS#
				###############
				(eq, ":event_type", multiplayer_event_set_item_selection),
				(store_script_param, ":slot_no", 3),
				(store_script_param, ":value", 4),
				(try_begin),
					#valid slot check
					(is_between, ":slot_no", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
					#valid item check
					(assign, ":valid_item", 0),
					(try_begin),
						(eq, ":value", -1),
						(assign, ":valid_item", 1),
					(else_try),
						(ge, ":value", 0),
						(player_get_troop_id, ":player_troop_no", ":player_no"),
						(is_between, ":player_troop_no", multiplayer_troops_begin, multiplayer_troops_end),
						(store_sub, ":troop_index", ":player_troop_no", multiplayer_troops_begin),
						(val_add, ":troop_index", slot_item_multiplayer_availability_linked_list_begin),
						(item_get_slot, ":prev_next_item_ids", ":value", ":troop_index"),
						(gt, ":prev_next_item_ids", 0), #0 if the item is not valid for the multiplayer mode
						(assign, ":valid_item", 1),
						(try_begin),
							(neq, "$g_horses_are_avaliable", 1),
							(item_get_slot, ":item_class", ":value", slot_item_multiplayer_item_class),
							(is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
							(assign, ":valid_item", 0),
						(try_end),
						
						(try_begin),
							(eq, "$g_multiplayer_disallow_ranged_weapons", 1),
							(item_get_slot, ":item_class", ":value", slot_item_multiplayer_item_class),
							(is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
							(assign, ":valid_item", 0),
						(try_end),
					(try_end),
					(eq, ":valid_item", 1),
					#condition checks are done
					(player_set_slot, ":player_no", ":slot_no", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_set_bot_selection),
				(store_script_param, ":slot_no", 3),
				(store_script_param, ":value", 4),
				(try_begin),
					#condition check
					(is_between, ":slot_no", slot_player_bot_type_1_wanted, slot_player_bot_type_4_wanted + 1),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(player_set_slot, ":player_no", ":slot_no", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_change_team_no),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_get_team_no, ":player_team", ":player_no"),
					(neq, ":player_team", ":value"),
					
					#condition checks are done
					(try_begin),
						#check if available
						(call_script, "script_cf_multiplayer_team_is_available", ":player_no", ":value"),
						#reset troop_id to -1
						(player_set_troop_id, ":player_no", -1),
						(player_set_team_no, ":player_no", ":value"),
						(try_begin),
							(neq, ":value", multi_team_spectator),
							(neq, ":value", multi_team_unassigned),
							
							(store_mission_timer_a, ":player_last_team_select_time"),
							(player_set_slot, ":player_no", slot_player_last_team_select_time, ":player_last_team_select_time"),
							
							(multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_confirmation),
						(try_end),
					(else_try),
						#reject request
						(multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_rejection),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_change_troop_id),
				(store_script_param, ":value", 3),
				#troop-faction validity check
				(try_begin),
					(eq, ":value", -1),
					(player_set_troop_id, ":player_no", -1),
				(else_try),
					(is_between, ":value", multiplayer_troops_begin, multiplayer_troops_end),
					(player_get_team_no, ":player_team", ":player_no"),
					(is_between, ":player_team", 0, multi_team_spectator),
					(team_get_faction, ":team_faction", ":player_team"),
					(store_troop_faction, ":new_troop_faction", ":value"),
					(eq, ":new_troop_faction", ":team_faction"),
					(player_set_troop_id, ":player_no", ":value"),
					(call_script, "script_multiplayer_clear_player_selected_items", ":player_no"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_start_map),
				(store_script_param, ":value", 3),
				(store_script_param, ":value_2", 4),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", multiplayer_scenes_begin, multiplayer_scenes_end),
					(is_between, ":value_2", 0, multiplayer_num_game_types),
					(server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
					(this_or_next|eq, "$g_multiplayer_changing_game_type_allowed", 1),
					(eq, "$g_multiplayer_game_type", ":value_2"),
					(call_script, "script_multiplayer_fill_map_game_types", ":value_2"),
					(assign, ":num_maps", reg0),
					(assign, ":is_valid", 0),
					(store_add, ":end_cond", multi_data_maps_for_game_type_begin, ":num_maps"),
					(try_for_range, ":i_map", multi_data_maps_for_game_type_begin, ":end_cond"),
						(troop_slot_eq, "trp_multiplayer_data", ":i_map", ":value"),
						(assign, ":is_valid", 1),
						(assign, ":end_cond", 0),
					(try_end),
					(eq, ":is_valid", 1),
					#condition checks are done
					(assign, "$g_multiplayer_game_type", ":value_2"),
					(assign, "$g_multiplayer_selected_map", ":value"),
					(team_set_faction, 0, "$g_multiplayer_next_team_1_faction"),
					(team_set_faction, 1, "$g_multiplayer_next_team_2_faction"),
					(call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
					(start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 1),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_max_num_players),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 2, 201),
					#condition checks are done
					(server_set_max_num_players, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_num_bots_in_team),
				(store_script_param, ":value", 3),
				(store_script_param, ":value_2", 4),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 1, 3),
					(is_between, ":value_2", 0, "$g_multiplayer_max_num_bots"),
					#condition checks are done
					(try_begin),
						(eq, ":value", 1),
						(assign, "$g_multiplayer_num_bots_team_1", ":value_2"),
					(else_try),
						(assign, "$g_multiplayer_num_bots_team_2", ":value_2"),
					(try_end),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, ":value", ":value_2"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_anti_cheat),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(server_set_anti_cheat, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_friendly_fire),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(server_set_friendly_fire, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_melee_friendly_fire),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(server_set_melee_friendly_fire, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_friendly_fire_damage_self_ratio),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 101),
					#condition checks are done
					(server_set_friendly_fire_damage_self_ratio, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_friendly_fire_damage_friend_ratio),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 101),
					#condition checks are done
					(server_set_friendly_fire_damage_friend_ratio, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_ghost_mode),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 4),
					#condition checks are done
					(server_set_ghost_mode, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_control_block_dir),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(server_set_control_block_dir, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_combat_speed),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 5),
					#condition checks are done
					(server_set_combat_speed, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_respawn_count),
				(store_script_param, ":value", 3),
				#validity check
				(player_is_admin, ":player_no"),
				(is_between, ":value", 0, 6),
				#condition checks are done
				(assign, "$g_multiplayer_number_of_respawn_count", ":value"),
				(get_max_players, ":num_players"),
				(try_for_range, ":cur_player", 1, ":num_players"),
					(player_is_active, ":cur_player"),
					(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_count, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_add_to_servers_list),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					#condition checks are done
					(server_set_add_to_game_servers_list, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_respawn_period),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 3, 31),
					#condition checks are done
					(assign, "$g_multiplayer_respawn_period", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_period, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_game_max_minutes),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 5, 121),
					#condition checks are done
					(assign, "$g_multiplayer_game_max_minutes", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_round_max_seconds),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 60, 901),
					#condition checks are done
					(assign, "$g_multiplayer_round_max_seconds", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_round_max_seconds, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_player_respawn_as_bot),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_player_respawn_as_bot", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_player_respawn_as_bot, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_game_max_points),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 3, 1001),
					#condition checks are done
					(assign, "$g_multiplayer_game_max_points", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_point_gained_from_flags),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 25, 401),
					#condition checks are done
					(assign, "$g_multiplayer_point_gained_from_flags", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_point_gained_from_capturing_flag),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 11),
					#condition checks are done
					(assign, "$g_multiplayer_point_gained_from_capturing_flag", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_initial_gold_multiplier),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 1001),
					#condition checks are done
					(assign, "$g_multiplayer_initial_gold_multiplier", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_battle_earnings_multiplier),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 1001),
					#condition checks are done
					(assign, "$g_multiplayer_battle_earnings_multiplier", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_round_earnings_multiplier),
				(store_script_param, ":value", 3),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 1001),
					#condition checks are done
					(assign, "$g_multiplayer_round_earnings_multiplier", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_server_name),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
					(eq, "$g_multiplayer_renaming_server_allowed", 1),
					#condition checks are done
					(server_set_name, s0), #validity is checked inside this function
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_game_password),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					#condition checks are done
					(server_set_password, s0), #validity is checked inside this function
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_welcome_message),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					#condition checks are done
					(server_set_welcome_message, s0), #validity is checked inside this function
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_team_faction),
				(store_script_param, ":value", 3),
				(store_script_param, ":value_2", 4),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 1, 3),
					(is_between, ":value_2", npc_kingdoms_begin, npc_kingdoms_end),
					##          (assign, ":is_valid", 0),
					##          (try_begin),
					##            (eq, ":value", 1),
					##            (neq, ":value_2", "$g_multiplayer_next_team_2_faction"),
					##            (assign, ":is_valid", 1),
					##          (else_try),
					##            (neq, ":value_2", "$g_multiplayer_next_team_1_faction"),
					##            (assign, ":is_valid", 1),
					##          (try_end),
					##          (eq, ":is_valid", 1),
					#condition checks are done
					(try_begin),
						(eq, ":value", 1),
						(assign, "$g_multiplayer_next_team_1_faction", ":value_2"),
					(else_try),
						(assign, "$g_multiplayer_next_team_2_faction", ":value_2"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_open_game_rules),
				(try_begin),
					#no validity check
					(server_get_max_num_players, ":max_num_players"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 1, "$g_multiplayer_next_team_1_faction"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 2, "$g_multiplayer_next_team_2_faction"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
					(server_get_anti_cheat, ":server_anti_cheat"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
					(server_get_friendly_fire, ":server_friendly_fire"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
					(server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
					(server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
					(server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
					(server_get_ghost_mode, ":server_ghost_mode"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
					(server_get_control_block_dir, ":server_control_block_dir"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
					(server_get_combat_speed, ":server_combat_speed"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
					(server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_minutes, "$g_multiplayer_game_max_minutes"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_points, "$g_multiplayer_game_max_points"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_flags, "$g_multiplayer_point_gained_from_flags"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_capturing_flag, "$g_multiplayer_point_gained_from_capturing_flag"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_initial_gold_multiplier, "$g_multiplayer_initial_gold_multiplier"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_battle_earnings_multiplier, "$g_multiplayer_battle_earnings_multiplier"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_earnings_multiplier, "$g_multiplayer_round_earnings_multiplier"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
					(str_store_server_name, s0),
					(multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
					(multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_open_game_rules),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_open_admin_panel),
				(try_begin),
					#validity check
					(player_is_admin, ":player_no"),
					#condition checks are done
					(server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
					(server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
					(server_get_max_num_players, ":max_num_players"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 1, "$g_multiplayer_next_team_1_faction"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 2, "$g_multiplayer_next_team_2_faction"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
					(server_get_anti_cheat, ":server_anti_cheat"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
					(server_get_friendly_fire, ":server_friendly_fire"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
					(server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
					(server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
					(server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
					(server_get_ghost_mode, ":server_ghost_mode"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
					(server_get_control_block_dir, ":server_control_block_dir"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
					(server_get_combat_speed, ":server_combat_speed"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
					(server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_minutes, "$g_multiplayer_game_max_minutes"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_points, "$g_multiplayer_game_max_points"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_flags, "$g_multiplayer_point_gained_from_flags"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_capturing_flag, "$g_multiplayer_point_gained_from_capturing_flag"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_initial_gold_multiplier, "$g_multiplayer_initial_gold_multiplier"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_battle_earnings_multiplier, "$g_multiplayer_battle_earnings_multiplier"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_earnings_multiplier, "$g_multiplayer_round_earnings_multiplier"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_bots, "$g_multiplayer_max_num_bots"),
					(str_store_server_name, s0),
					(multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
					(str_store_server_password, s0),
					(multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_game_password, s0),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_start_new_poll),
				(try_begin),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					#validity check
					(eq, "$g_multiplayer_poll_running", 0),
					(store_mission_timer_a, ":mission_timer"),
					(player_get_slot, ":poll_disable_time", ":player_no", slot_player_poll_disabled_until_time),
					(ge, ":mission_timer", ":poll_disable_time"),
					(assign, ":continue", 0),
					(try_begin),
						(eq, ":value", 1), # kicking a player
						(try_begin),
							(eq, "$g_multiplayer_kick_voteable", 1),
							(player_is_active, ":value_2"),
							(assign, ":continue", 1),
						(try_end),
					(else_try),
						(eq, ":value", 2), # banning a player
						(try_begin),
							(eq, "$g_multiplayer_ban_voteable", 1),
							(player_is_active, ":value_2"),
							(save_ban_info_of_player, ":value_2"),
							(assign, ":continue", 1),
						(try_end),
					(else_try), # vote for map
						(eq, ":value", 0),
						(try_begin),
							(eq, "$g_multiplayer_maps_voteable", 1),
							(call_script, "script_multiplayer_fill_map_game_types", "$g_multiplayer_game_type"),
							(assign, ":num_maps", reg0),
							(try_for_range, ":i_map", 0, ":num_maps"),
								(store_add, ":map_slot", ":i_map", multi_data_maps_for_game_type_begin),
								(troop_slot_eq, "trp_multiplayer_data", ":map_slot", ":value_2"),
								(assign, ":continue", 1),
								(assign, ":num_maps", 0), #break
							(try_end),
						(try_end),
					(else_try),
						(eq, ":value", 3), #vote for map and factions
						(try_begin),
							(eq, "$g_multiplayer_factions_voteable", 1),
							(store_script_param, ":value_3", 5),
							(store_script_param, ":value_4", 6),
							(call_script, "script_multiplayer_fill_map_game_types", "$g_multiplayer_game_type"),
							(assign, ":num_maps", reg0),
							(try_for_range, ":i_map", 0, ":num_maps"),
								(store_add, ":map_slot", ":i_map", multi_data_maps_for_game_type_begin),
								(troop_slot_eq, "trp_multiplayer_data", ":map_slot", ":value_2"),
								(assign, ":continue", 1),
								(assign, ":num_maps", 0), #break
							(try_end),
							(try_begin),
								(eq, ":continue", 1),
								(this_or_next|neg|is_between, ":value_3", npc_kingdoms_begin, npc_kingdoms_end),
								(this_or_next|neg|is_between, ":value_4", npc_kingdoms_begin, npc_kingdoms_end),
								(eq, ":value_3", ":value_4"),
								(assign, ":continue", 0),
							(try_end),
						(try_end),
					(else_try),
						(eq, ":value", 4), #vote for number of bots
						(store_script_param, ":value_3", 5),
						(store_add, ":upper_limit", "$g_multiplayer_num_bots_voteable", 1),
						(is_between, ":value_2", 0, ":upper_limit"),
						(is_between, ":value_3", 0, ":upper_limit"),
						(assign, ":continue", 1),
					(try_end),
					(eq, ":continue", 1),
					#condition checks are done
					(str_store_player_username, s0, ":player_no"),
					(try_begin),
						(eq, ":value", 1), #kicking a player
						(str_store_player_username, s1, ":value_2"),
						(server_add_message_to_log, "str_poll_kick_player_s1_by_s0"),
					(else_try),
						(eq, ":value", 2), #banning a player
						(str_store_player_username, s1, ":value_2"),
						(server_add_message_to_log, "str_poll_ban_player_s1_by_s0"),
					(else_try),
						(eq, ":value", 0), #vote for map
						(store_sub, ":string_index", ":value_2", multiplayer_scenes_begin),
						(val_add, ":string_index", multiplayer_scene_names_begin),
						(str_store_string, s1, ":string_index"),
						(server_add_message_to_log, "str_poll_change_map_to_s1_by_s0"),
					(else_try),
						(eq, ":value", 3), #vote for map and factions
						(store_sub, ":string_index", ":value_2", multiplayer_scenes_begin),
						(val_add, ":string_index", multiplayer_scene_names_begin),
						(str_store_string, s1, ":string_index"),
						(str_store_faction_name, s2, ":value_3"),
						(str_store_faction_name, s3, ":value_4"),
						(server_add_message_to_log, "str_poll_change_map_to_s1_and_factions_to_s2_and_s3_by_s0"),
					(else_try),
						(eq, ":value", 4), #vote for number of bots
						(assign, reg0, ":value_2"),
						(assign, reg1, ":value_3"),
						(server_add_message_to_log, "str_poll_change_number_of_bots_to_reg0_and_reg1_by_s0"),
					(try_end),
					(assign, "$g_multiplayer_poll_running", 1),
					(assign, "$g_multiplayer_poll_ended", 0),
					(assign, "$g_multiplayer_poll_num_sent", 0),
					(assign, "$g_multiplayer_poll_yes_count", 0),
					(assign, "$g_multiplayer_poll_no_count", 0),
					(assign, "$g_multiplayer_poll_to_show", ":value"),
					(assign, "$g_multiplayer_poll_value_to_show", ":value_2"),
					(try_begin),
						(eq, ":value", 3),
						(assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
						(assign, "$g_multiplayer_poll_value_3_to_show", ":value_4"),
					(else_try),
						(eq, ":value", 4),
						(assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
						(assign, "$g_multiplayer_poll_value_3_to_show", -1),
					(else_try),
						(assign, "$g_multiplayer_poll_value_2_to_show", -1),
						(assign, "$g_multiplayer_poll_value_3_to_show", -1),
					(try_end),
					(store_add, ":poll_disable_until", ":mission_timer", multiplayer_poll_disable_period),
					(player_set_slot, ":player_no", slot_player_poll_disabled_until_time, ":poll_disable_until"),
					(store_add, "$g_multiplayer_poll_end_time", ":mission_timer", 60),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 0, ":num_players"),
						(player_is_active, ":cur_player"),
						(player_set_slot, ":cur_player", slot_player_can_answer_poll, 1),
						(val_add, "$g_multiplayer_poll_num_sent", 1),
						(multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_ask_for_poll, "$g_multiplayer_poll_to_show", "$g_multiplayer_poll_value_to_show", "$g_multiplayer_poll_value_2_to_show", "$g_multiplayer_poll_value_3_to_show"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_answer_to_poll),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(eq, "$g_multiplayer_poll_running", 1),
					(is_between, ":value", 0, 2),
					(player_slot_eq, ":player_no", slot_player_can_answer_poll, 1),
					#condition checks are done
					(player_set_slot, ":player_no", slot_player_can_answer_poll, 0),
					(try_begin),
						(eq, ":value", 0),
						(val_add, "$g_multiplayer_poll_no_count", 1),
					(else_try),
						(eq, ":value", 1),
						(val_add, "$g_multiplayer_poll_yes_count", 1),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_kick_player),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(player_is_active, ":value"),
					#condition checks are done
					(kick_player, ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_ban_player),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(player_is_active, ":value"),
					#condition checks are done
					(ban_player, ":value", 0, ":player_no"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_valid_vote_ratio),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 50, 101),
					#condition checks are done
					(assign, "$g_multiplayer_valid_vote_ratio", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_auto_team_balance_limit),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(this_or_next|is_between, ":value", 2, 7),
					(eq, ":value", 1000),
					#condition checks are done
					(assign, "$g_multiplayer_auto_team_balance_limit", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_num_bots_voteable),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 51),
					(is_between, ":value", "$g_multiplayer_max_num_bots"),
					#condition checks are done
					(assign, "$g_multiplayer_num_bots_voteable", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_num_bots_voteable, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_factions_voteable),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_factions_voteable", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_factions_voteable, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_maps_voteable),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_maps_voteable", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_maps_voteable, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_kick_voteable),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_kick_voteable", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_kick_voteable, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_ban_voteable),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_ban_voteable", ":value"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_ban_voteable, ":value"),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_allow_player_banners),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_allow_player_banners", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_force_default_armor),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_force_default_armor", ":value"),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_offer_duel),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
					(agent_is_active, ":value"),
					(agent_is_alive, ":value"),
					(agent_is_human, ":value"),
					(player_get_agent_id, ":player_agent_no", ":player_no"),
					(agent_is_active, ":player_agent_no"),
					(agent_is_alive, ":player_agent_no"),
					(agent_get_position, pos0, ":player_agent_no"),
					(agent_get_position, pos1, ":value"),
					(get_sq_distance_between_positions_in_meters, ":agent_dist_sq", pos0, pos1),
					(le, ":agent_dist_sq", 49),
					#allow duelists to receive new offers
					(this_or_next|agent_check_offer_from_agent, ":player_agent_no", ":value"),
					(agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, -1),
					(neg|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, ":value"), #don't allow spamming duel offers during countdown
					#condition checks are done
					(try_begin),
						#accepting a duel
						(agent_check_offer_from_agent, ":player_agent_no", ":value"),
						(call_script, "script_multiplayer_accept_duel", ":player_agent_no", ":value"),
					(else_try),
						#sending a duel request
						(assign, ":display_notification", 1),
						(try_begin),
							(agent_check_offer_from_agent, ":value", ":player_agent_no"),
							(assign, ":display_notification", 0),
						(try_end),
						(agent_add_offer_with_timeout, ":value", ":player_agent_no", 10000), #10 second timeout
						(agent_get_player_id, ":value_player", ":value"),
						(try_begin),
							(player_is_active, ":value_player"), #might be AI
							(try_begin),
								(eq, ":display_notification", 1),
								(multiplayer_send_int_to_player, ":value_player", multiplayer_event_show_duel_request, ":player_agent_no"),
							(try_end),
						(else_try),
							(call_script, "script_multiplayer_accept_duel", ":value", ":player_agent_no"),
						(try_end),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":event_type", multiplayer_event_admin_set_disallow_ranged_weapons),
				(try_begin),
					(store_script_param, ":value", 3),
					#validity check
					(player_is_admin, ":player_no"),
					(is_between, ":value", 0, 2),
					#condition checks are done
					(assign, "$g_multiplayer_disallow_ranged_weapons", ":value"),
				(try_end),
			(else_try),
				###############
				#CLIENT EVENTS#
				###############
				(neg|multiplayer_is_dedicated_server),
				(try_begin),
					(eq, ":event_type", multiplayer_event_return_renaming_server_allowed),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_renaming_server_allowed", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_changing_game_type_allowed),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_changing_game_type_allowed", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_max_num_players),
					(store_script_param, ":value", 3),
					(server_set_max_num_players, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_next_team_faction),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(try_begin),
						(eq, ":value", 1),
						(assign, "$g_multiplayer_next_team_1_faction", ":value_2"),
					(else_try),
						(assign, "$g_multiplayer_next_team_2_faction", ":value_2"),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_num_bots_in_team),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(try_begin),
						(eq, ":value", 1),
						(assign, "$g_multiplayer_num_bots_team_1", ":value_2"),
					(else_try),
						(assign, "$g_multiplayer_num_bots_team_2", ":value_2"),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_anti_cheat),
					(store_script_param, ":value", 3),
					(server_set_anti_cheat, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_friendly_fire),
					(store_script_param, ":value", 3),
					(server_set_friendly_fire, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_melee_friendly_fire),
					(store_script_param, ":value", 3),
					(server_set_melee_friendly_fire, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_friendly_fire_damage_self_ratio),
					(store_script_param, ":value", 3),
					(server_set_friendly_fire_damage_self_ratio, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_friendly_fire_damage_friend_ratio),
					(store_script_param, ":value", 3),
					(server_set_friendly_fire_damage_friend_ratio, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_ghost_mode),
					(store_script_param, ":value", 3),
					(server_set_ghost_mode, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_control_block_dir),
					(store_script_param, ":value", 3),
					(server_set_control_block_dir, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_add_to_servers_list),
					(store_script_param, ":value", 3),
					(server_set_add_to_game_servers_list, ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_respawn_period),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_respawn_period", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_game_max_minutes),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_game_max_minutes", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_round_max_seconds),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_round_max_seconds", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_player_respawn_as_bot),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_player_respawn_as_bot", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_game_max_points),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_game_max_points", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_point_gained_from_flags),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_point_gained_from_flags", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_point_gained_from_capturing_flag),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_point_gained_from_capturing_flag", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_initial_gold_multiplier),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_initial_gold_multiplier", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_battle_earnings_multiplier),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_battle_earnings_multiplier", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_round_earnings_multiplier),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_round_earnings_multiplier", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_respawn_count),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_number_of_respawn_count", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_server_name),
					(server_set_name, s0),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_game_password),
					(server_set_password, s0),
					#this is the last option in admin panel, so start the presentation
					(start_presentation, "prsnt_game_multiplayer_admin_panel"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_open_game_rules),
					#this is the last message for game rules, so start the presentation
					(assign, "$g_multiplayer_show_server_rules", 1),
					(start_presentation, "prsnt_multiplayer_welcome_message"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_game_type),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_game_type", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_valid_vote_ratio),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_valid_vote_ratio", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_max_num_bots),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_max_num_bots", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_server_mission_timer_while_player_joined),
					(store_script_param, ":value", 3),
					(assign, "$server_mission_timer_while_player_joined", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_auto_team_balance_limit),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_auto_team_balance_limit", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_num_bots_voteable),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_num_bots_voteable", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_factions_voteable),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_factions_voteable", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_maps_voteable),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_maps_voteable", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_kick_voteable),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_kick_voteable", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_ban_voteable),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_ban_voteable", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_allow_player_banners),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_allow_player_banners", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_force_default_armor),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_force_default_armor", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_disallow_ranged_weapons),
					(store_script_param, ":value", 3),
					(assign, "$g_multiplayer_disallow_ranged_weapons", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_confirmation),
					(assign, "$g_confirmation_result", 1),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_rejection),
					(assign, "$g_confirmation_result", -1),
				(else_try),
					(eq, ":event_type", multiplayer_event_show_multiplayer_message),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(call_script, "script_show_multiplayer_message", ":value", ":value_2"),
				(else_try),
					(eq, ":event_type", multiplayer_event_draw_this_round),
					(store_script_param, ":value", 3),
					(call_script, "script_draw_this_round", ":value"),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_attached_scene_prop),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(call_script, "script_set_attached_scene_prop", ":value", ":value_2"),
					(try_begin),
						(eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
						(try_begin),
							(neq, ":value_2", -1),
							(agent_set_horse_speed_factor, ":value", 75),
						(else_try),
							(agent_set_horse_speed_factor, ":value", 100),
						(try_end),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_team_flag_situation),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(call_script, "script_set_team_flag_situation", ":value", ":value_2"),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_team_score),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(call_script, "script_team_set_score", ":value", ":value_2"),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_player_score_kill_death),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(store_script_param, ":value_3", 5),
					(store_script_param, ":value_4", 6),
					(call_script, "script_player_set_score", ":value", ":value_2"),
					(call_script, "script_player_set_kill_count", ":value", ":value_3"),
					(call_script, "script_player_set_death_count", ":value", ":value_4"),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_num_agents_around_flag),
					(store_script_param, ":flag_no", 3),
					(store_script_param, ":current_owner_code", 4),
					(call_script, "script_set_num_agents_around_flag", ":flag_no", ":current_owner_code"),
				(else_try),
					(eq, ":event_type", multiplayer_event_ask_for_poll),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(store_script_param, ":value_3", 5),
					(store_script_param, ":value_4", 6),
					(assign, ":continue_to_poll", 0),
					(try_begin),
						(this_or_next|eq, ":value", 1),
						(eq, ":value", 2),
						(player_is_active, ":value_2"), #might go offline before here
						(assign, ":continue_to_poll", 1),
					(else_try),
						(assign, ":continue_to_poll", 1),
					(try_end),
					(try_begin),
						(eq, ":continue_to_poll", 1),
						(assign, "$g_multiplayer_poll_to_show", ":value"),
						(assign, "$g_multiplayer_poll_value_to_show", ":value_2"),
						(assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
						(assign, "$g_multiplayer_poll_value_3_to_show", ":value_4"),
						(store_mission_timer_a, ":mission_timer"),
						(store_add, "$g_multiplayer_poll_client_end_time", ":mission_timer", 60),
						(start_presentation, "prsnt_multiplayer_poll"),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_change_flag_owner),
					(store_script_param, ":flag_no", 3),
					(store_script_param, ":owner_code", 4),
					(call_script, "script_change_flag_owner", ":flag_no", ":owner_code"),
				(else_try),
					(eq, ":event_type", multiplayer_event_use_item),
					(store_script_param, ":value", 3),
					(store_script_param, ":value_2", 4),
					(call_script, "script_use_item", ":value", ":value_2"),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_scene_prop_open_or_close),
					(store_script_param, ":instance_id", 3),
					
					(scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 1),
					
					(prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
					
					(try_begin),
						(eq, ":scene_prop_id", "spr_winch_b"),
						(assign, ":effected_object", "spr_portcullis"),
					(else_try),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
						(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
						(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
						(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
						(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
						(this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
						(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
						(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
						(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
						(this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
						(eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
						(assign, ":effected_object", ":scene_prop_id"),
					(try_end),
					
					(try_begin),
						(eq, ":effected_object", "spr_portcullis"),
						
						(assign, ":smallest_dist", -1),
						(prop_instance_get_position, pos0, ":instance_id"),
						(scene_prop_get_num_instances, ":num_instances_of_effected_object", ":effected_object"),
						(try_for_range, ":cur_instance", 0, ":num_instances_of_effected_object"),
							(scene_prop_get_instance, ":cur_instance_id", ":effected_object", ":cur_instance"),
							(prop_instance_get_position, pos1, ":cur_instance_id"),
							(get_sq_distance_between_positions, ":dist", pos0, pos1),
							(this_or_next|eq, ":smallest_dist", -1),
							(lt, ":dist", ":smallest_dist"),
							(assign, ":smallest_dist", ":dist"),
							(assign, ":effected_object_instance_id", ":cur_instance_id"),
						(try_end),
						
						(ge, ":smallest_dist", 0),
						(prop_instance_is_animating, ":is_animating", ":effected_object_instance_id"),
						(eq, ":is_animating", 0),
						
						(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
						(position_move_z, pos0, 375),
						(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
					(else_try),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
						(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
						(this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
						(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
						(this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
						(this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
						(this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
						(eq, ":scene_prop_id", "spr_castle_f_door_b"),
						(assign, ":effected_object_instance_id", ":instance_id"),
						(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
						(position_rotate_z, pos0, -80),
						(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
					(else_try),
						(assign, ":effected_object_instance_id", ":instance_id"),
						(prop_instance_is_animating, ":is_animating", ":effected_object_instance_id"),
						(eq, ":is_animating", 0),
						(prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
						(prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_set_round_start_time),
					(store_script_param, ":value", 3),
					
					(try_begin),
						(neq, ":value", -9999),
						(assign, "$g_round_start_time", ":value"),
					(else_try),
						(store_mission_timer_a, "$g_round_start_time"),
						
						#if round start time is assigning to current time (so new round is starting) then also initialize moveable object slots too.
						(call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_6m"),
						(call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_8m"),
						(call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_10m"),
						(call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_12m"),
						(call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_14m"),
						(call_script, "script_initialize_scene_prop_slots", "spr_winch_b"),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_force_start_team_selection),
					(try_begin),
						(is_presentation_active, "prsnt_multiplayer_item_select"),
						(assign, "$g_close_equipment_selection", 1),
					(try_end),
					(start_presentation, "prsnt_multiplayer_troop_select"),
				(else_try),
					(eq, ":event_type", multiplayer_event_start_death_mode),
					(assign, "$g_battle_death_mode_started", 2),
					(start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
					(call_script, "script_start_death_mode"),
				(else_try),
					(eq, ":event_type", multiplayer_event_return_player_respawn_spent),
					(store_script_param, ":value", 3),
					(try_begin),
						(gt, "$g_my_spawn_count", 0),
						(store_add, "$g_my_spawn_count", "$g_my_spawn_count", ":value"),
					(else_try),
						(assign, "$g_my_spawn_count", ":value"),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_show_duel_request),
					(store_script_param, ":value", 3),
					(try_begin),
						(agent_is_active, ":value"),
						(agent_get_player_id, ":value_player_no", ":value"),
						(try_begin),
							(player_is_active, ":value_player_no"),
							(str_store_player_username, s0, ":value_player_no"),
						(else_try),
							(str_store_agent_name, s0, ":value"),
						(try_end),
						(display_message, "str_s0_offers_a_duel_with_you"),
						(try_begin),
							(get_player_agent_no, ":player_agent"),
							(agent_is_active, ":player_agent"),
							(agent_add_offer_with_timeout, ":player_agent", ":value", 10000), #10 second timeout
						(try_end),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_start_duel),
					(store_script_param, ":value", 3),
					(store_mission_timer_a, ":mission_timer"),
					(try_begin),
						(agent_is_active, ":value"),
						(get_player_agent_no, ":player_agent"),
						(agent_is_active, ":player_agent"),
						(agent_get_player_id, ":value_player_no", ":value"),
						(try_begin),
							(player_is_active, ":value_player_no"),
							(str_store_player_username, s0, ":value_player_no"),
						(else_try),
							(str_store_agent_name, s0, ":value"),
						(try_end),
						(display_message, "str_a_duel_between_you_and_s0_will_start_in_3_seconds"),
						(assign, "$g_multiplayer_duel_start_time", ":mission_timer"),
						(start_presentation, "prsnt_multiplayer_duel_start_counter"),
						(agent_set_slot, ":player_agent", slot_agent_in_duel_with, ":value"),
						(agent_set_slot, ":value", slot_agent_in_duel_with, ":player_agent"),
						(agent_set_slot, ":player_agent", slot_agent_duel_start_time, ":mission_timer"),
						(agent_set_slot, ":value", slot_agent_duel_start_time, ":mission_timer"),
						(agent_clear_relations_with_agents, ":player_agent"),
						(agent_clear_relations_with_agents, ":value"),
						##            (agent_add_relation_with_agent, ":player_agent", ":value", -1),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_cancel_duel),
					(store_script_param, ":value", 3),
					(try_begin),
						(agent_is_active, ":value"),
						(agent_get_player_id, ":value_player_no", ":value"),
						(try_begin),
							(player_is_active, ":value_player_no"),
							(str_store_player_username, s0, ":value_player_no"),
						(else_try),
							(str_store_agent_name, s0, ":value"),
						(try_end),
						(display_message, "str_your_duel_with_s0_is_cancelled"),
					(try_end),
					(try_begin),
						(get_player_agent_no, ":player_agent"),
						(agent_is_active, ":player_agent"),
						(agent_set_slot, ":player_agent", slot_agent_in_duel_with, -1),
						(agent_clear_relations_with_agents, ":player_agent"),
					(try_end),
				(else_try),
					(eq, ":event_type", multiplayer_event_show_server_message),
					(display_message, "str_server_s0", 0xFFFF6666),
				(try_end),
		])

		# script_multiplayer_accept_duel
		# Input: arg1 = agent_no, arg2 = agent_no_offerer
		# Output: none
multiplayer_accept_duel =	(
	"multiplayer_accept_duel",
			[
				(store_script_param, ":agent_no", 1),
				(store_script_param, ":agent_no_offerer", 2),
				(try_begin),
					(agent_slot_ge, ":agent_no", slot_agent_in_duel_with, 0),
					(agent_get_slot, ":ex_duelist", ":agent_no", slot_agent_in_duel_with),
					(agent_is_active, ":ex_duelist"),
					(agent_clear_relations_with_agents, ":ex_duelist"),
					(agent_set_slot, ":ex_duelist", slot_agent_in_duel_with, -1),
					(agent_get_player_id, ":player_no", ":ex_duelist"),
					(try_begin),
						(player_is_active, ":player_no"), #might be AI
						(multiplayer_send_int_to_player, ":player_no", multiplayer_event_cancel_duel, ":agent_no"),
					(else_try),
						(agent_force_rethink, ":ex_duelist"),
					(try_end),
				(try_end),
				(try_begin),
					(agent_slot_ge, ":agent_no_offerer", slot_agent_in_duel_with, 0),
					(agent_get_slot, ":ex_duelist", ":agent_no_offerer", slot_agent_in_duel_with),
					(agent_is_active, ":ex_duelist"),
					(agent_clear_relations_with_agents, ":ex_duelist"),
					(agent_set_slot, ":ex_duelist", slot_agent_in_duel_with, -1),
					(try_begin),
						(player_is_active, ":player_no"), #might be AI
						(multiplayer_send_int_to_player, ":player_no", multiplayer_event_cancel_duel, ":agent_no_offerer"),
					(else_try),
						(agent_force_rethink, ":ex_duelist"),
					(try_end),
				(try_end),
				(agent_set_slot, ":agent_no", slot_agent_in_duel_with, ":agent_no_offerer"),
				(agent_set_slot, ":agent_no_offerer", slot_agent_in_duel_with, ":agent_no"),
				(agent_clear_relations_with_agents, ":agent_no"),
				(agent_clear_relations_with_agents, ":agent_no_offerer"),
				##     (agent_add_relation_with_agent, ":agent_no", ":agent_no_offerer", -1),
				##     (agent_add_relation_with_agent, ":agent_no_offerer", ":agent_no", -1),
				(agent_get_player_id, ":player_no", ":agent_no"),
				(store_mission_timer_a, ":mission_timer"),
				(try_begin),
					(player_is_active, ":player_no"), #might be AI
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_start_duel, ":agent_no_offerer"),
				(else_try),
					(agent_force_rethink, ":agent_no"),
				(try_end),
				(agent_set_slot, ":agent_no", slot_agent_duel_start_time, ":mission_timer"),
				(agent_get_player_id, ":agent_no_offerer_player", ":agent_no_offerer"),
				(try_begin),
					(player_is_active, ":agent_no_offerer_player"), #might be AI
					(multiplayer_send_int_to_player, ":agent_no_offerer_player", multiplayer_event_start_duel, ":agent_no"),
				(else_try),
					(agent_force_rethink, ":agent_no_offerer"),
				(try_end),
				(agent_set_slot, ":agent_no_offerer", slot_agent_duel_start_time, ":mission_timer"),
		])
	
		# script_game_multiplayer_event_duel_offered
		# Input: arg1 = agent_no
		# Output: none
game_multiplayer_event_duel_offered = (
	"game_multiplayer_event_duel_offered",
			[
				(store_script_param, ":agent_no", 1),
				(get_player_agent_no, ":player_agent_no"),
				(try_begin),
					(agent_is_active, ":player_agent_no"),
					(this_or_next|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, -1),
					(agent_check_offer_from_agent, ":player_agent_no", ":agent_no"),
					(neg|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, ":agent_no"), #don't allow spamming duel offers during countdown
					(multiplayer_send_int_to_server, multiplayer_event_offer_duel, ":agent_no"),
					(agent_get_player_id, ":player_no", ":agent_no"),
					(try_begin),
						(player_is_active, ":player_no"),
						(str_store_player_username, s0, ":player_no"),
					(else_try),
						(str_store_agent_name, s0, ":agent_no"),
					(try_end),
					(display_message, "str_a_duel_request_is_sent_to_s0"),
				(try_end),
		])
		
		# script_multiplayer_fill_available_factions_combo_button
		# Input: arg1 = overlay_id, arg2 = selected_faction_no, arg3 = opposite_team_selected_faction_no
		# Output: none
multiplayer_fill_available_factions_combo_button =	(
	"multiplayer_fill_available_factions_combo_button",
			[
				(store_script_param, ":overlay_id", 1),
				(store_script_param, ":selected_faction_no", 2),
				##     (store_script_param, ":opposite_team_selected_faction_no", 3),
				##     (try_for_range, ":cur_faction", "fac_kingdom_1", "fac_kingdoms_end"),
				##       (try_begin),
				##         (eq, ":opposite_team_selected_faction_no", ":cur_faction"),
				##         (try_begin),
				##           (gt, ":selected_faction_no", ":opposite_team_selected_faction_no"),
				##           (val_sub, ":selected_faction_no", 1),
				##         (try_end),
				##       (else_try),
				##         (str_store_faction_name, s0, ":cur_faction"),
				##         (overlay_add_item, ":overlay_id", s0),
				##       (try_end),
				##     (try_end),
				##     (val_sub, ":selected_faction_no", "fac_kingdom_1"),
				##     (overlay_set_val, ":overlay_id", ":selected_faction_no"),
				(try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
					(str_store_faction_name, s0, ":cur_faction"),
					(overlay_add_item, ":overlay_id", s0),
				(try_end),
				(val_sub, ":selected_faction_no", "fac_kingdom_1"),
				(overlay_set_val, ":overlay_id", ":selected_faction_no"),
		])
		
		
		#script_multiplayer_clear_player_selected_items
		# Input: arg1 = player_no
		# Output: none
multiplayer_clear_player_selected_items = (
	"multiplayer_clear_player_selected_items",
			[
				(store_script_param, ":player_no", 1),
				(try_for_range, ":slot_no", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
					(player_set_slot, ":player_no", ":slot_no", -1),
				(try_end),
		])
		
		#script_send_open_close_information_of_object
		# Input: arg1 = mission_object_id
		# Output: none
send_open_close_information_of_object =	(
	"send_open_close_information_of_object",
			[
				(store_script_param, ":player_no", 1),
				(store_script_param, ":scene_prop_no", 2),
				
				(scene_prop_get_num_instances, ":num_instances", ":scene_prop_no"),
				
				(try_for_range, ":instance_no", 0, ":num_instances"),
					(scene_prop_get_instance, ":instance_id", ":scene_prop_no", ":instance_no"),
					(scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
					(try_begin),
						(eq, ":opened_or_closed", 1),
						(multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_scene_prop_open_or_close, ":instance_id"),
					(try_end),
				(try_end),
		])
		
		#script_multiplayer_send_initial_information
		# Input: arg1 = player_no
		# Output: none
multiplayer_send_initial_information =	(
	"multiplayer_send_initial_information",
			[
				(store_script_param, ":player_no", 1),
				
				(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
				(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_auto_team_balance_limit, "$g_multiplayer_auto_team_balance_limit"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_num_bots_voteable, "$g_multiplayer_num_bots_voteable"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_factions_voteable, "$g_multiplayer_factions_voteable"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_maps_voteable, "$g_multiplayer_maps_voteable"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_kick_voteable, "$g_multiplayer_kick_voteable"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ban_voteable, "$g_multiplayer_ban_voteable"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_allow_player_banners, "$g_multiplayer_allow_player_banners"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_force_default_armor, "$g_multiplayer_force_default_armor"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_disallow_ranged_weapons, "$g_multiplayer_disallow_ranged_weapons"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_type, "$g_multiplayer_game_type"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
				
				(store_mission_timer_a, ":mission_timer"),
				(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_server_mission_timer_while_player_joined, ":mission_timer"),
				
				(try_begin),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_count, "$g_multiplayer_number_of_respawn_count"),
				(try_end),
				
				(try_for_agents, ":cur_agent"), #send if any agent is carrying any scene object
					(agent_is_human, ":cur_agent"),
					(agent_get_attached_scene_prop, ":attached_scene_prop", ":cur_agent"),
					(ge, ":attached_scene_prop", 0),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_attached_scene_prop, ":cur_agent", ":attached_scene_prop"),
				(try_end),
				
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_6m"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_8m"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_10m"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_12m"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_14m"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_winch_b"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_e_sally_door_a"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_f_sally_door_a"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_earth_sally_gate_left"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_earth_sally_gate_right"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_viking_keep_destroy_sally_door_left"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_viking_keep_destroy_sally_door_right"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_f_door_a"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_door_destructible"),
				(call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_f_door_b"),
				
				(try_begin),
					(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
					(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
					
					(store_mission_timer_a, ":current_time"),
					(val_sub, ":current_time", "$g_round_start_time"),
					(val_mul, ":current_time", -1),
					
					(multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, ":current_time"),
				(else_try),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
					#if game type is capture the flag send current flag situations to each player.
					(team_get_slot, ":flag_situation_team_1", 0, slot_team_flag_situation),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, 0, ":flag_situation_team_1"),
					(team_get_slot, ":flag_situation_team_2", 1, slot_team_flag_situation),
					(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, 1, ":flag_situation_team_2"),
				(else_try),
					(this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
					#if game type is headquarters send number of agents placed around each pole's around to player.
					(try_for_range, ":flag_no", 0, "$g_number_of_flags"),
						(assign, ":number_of_agents_around_flag_team_1", 0),
						(assign, ":number_of_agents_around_flag_team_2", 0),
						
						(scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
						(prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.
						
						(try_for_agents, ":cur_agent"),
							(agent_is_human, ":cur_agent"),
							(agent_is_alive, ":cur_agent"),
							(neg|agent_is_non_player, ":cur_agent"),
							(agent_get_team, ":cur_agent_team", ":cur_agent"),
							(agent_get_position, pos1, ":cur_agent"), #pos1 holds agent's position.
							(get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
							(get_sq_distance_between_position_heights, ":squared_height_dist", pos0, pos1),
							(val_add, ":squared_dist", ":squared_height_dist"),
							(lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
							(try_begin),
								(eq, ":cur_agent_team", 0),
								(val_add, ":number_of_agents_around_flag_team_1", 1),
							(else_try),
								(eq, ":cur_agent_team", 1),
								(val_add, ":number_of_agents_around_flag_team_2", 1),
							(try_end),
						(try_end),
						
						(store_mul, ":current_owner_code", ":number_of_agents_around_flag_team_1", 100),
						(val_add, ":current_owner_code", ":number_of_agents_around_flag_team_2"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_num_agents_around_flag, ":flag_no", ":current_owner_code"),
					(try_end),
					
					#if game type is headquarters send owners of each pole to player.
					(assign, "$g_placing_initial_flags", 1),
					(try_for_range, ":cur_flag", 0, "$g_number_of_flags"),
						(store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":cur_flag"),
						(troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_slot"),
						(store_mul, ":cur_flag_owner_code", ":cur_flag_owner", 100),
						(val_add, ":cur_flag_owner_code", ":cur_flag_owner"),
						(val_add, ":cur_flag_owner_code", 1),
						(val_mul, ":cur_flag_owner_code", -1),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_change_flag_owner, ":cur_flag", ":cur_flag_owner_code"),
					(try_end),
					(assign, "$g_placing_initial_flags", 0),
				(try_end),
				
				#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_day_time, "$g_round_day_time"),
		])
		
		#script_multiplayer_remove_headquarters_flags
		# Input: none
		# Output: none
multiplayer_remove_headquarters_flags =	(
	"multiplayer_remove_headquarters_flags",
			[
				(store_add, ":end_cond", "spr_headquarters_flag_gray", 1),
				(try_for_range, ":headquarters_flag_no", "spr_headquarters_flag_red", ":end_cond"),
					(replace_scene_props, ":headquarters_flag_no", "spr_empty"),
				(try_end),
		])
		
		#script_multiplayer_remove_destroy_mod_targets
		# Input: none
		# Output: none
multiplayer_remove_destroy_mod_targets =	(
	"multiplayer_remove_destroy_mod_targets",
			[
				(replace_scene_props, "spr_catapult_destructible", "spr_empty"),
				(replace_scene_props, "spr_trebuchet_destructible", "spr_empty"),
		])
		
		#script_multiplayer_init_mission_variables
multiplayer_init_mission_variables =	(
	"multiplayer_init_mission_variables",
			[
				(assign, "$g_multiplayer_team_1_first_spawn", 1),
				(assign, "$g_multiplayer_team_2_first_spawn", 1),
				(assign, "$g_multiplayer_poll_running", 0),
				##     (assign, "$g_multiplayer_show_poll_when_suitable", 0),
				(assign, "$g_waiting_for_confirmation_to_terminate", 0),
				(assign, "$g_confirmation_result", 0),
				(assign, "$g_team_balance_next_round", 0),
				(team_get_faction, "$g_multiplayer_team_1_faction", 0),
				(team_get_faction, "$g_multiplayer_team_2_faction", 1),
				(assign, "$g_multiplayer_next_team_1_faction", "$g_multiplayer_team_1_faction"),
				(assign, "$g_multiplayer_next_team_2_faction", "$g_multiplayer_team_2_faction"),
				
				(assign, "$g_multiplayer_bot_type_1_wanted", 0),
				(assign, "$g_multiplayer_bot_type_2_wanted", 0),
				(assign, "$g_multiplayer_bot_type_3_wanted", 0),
				(assign, "$g_multiplayer_bot_type_4_wanted", 0),
				
				(call_script, "script_music_set_situation_with_culture", mtf_sit_multiplayer_fight),
		])
		
		#script_multiplayer_event_mission_end
		# Input: none
		# Output: none
multiplayer_event_mission_end =	(
	"multiplayer_event_mission_end",
			[
				#EVERY_BREATH_YOU_TAKE achievement
				(try_begin),
					(multiplayer_get_my_player, ":my_player_no"),
					(is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
					(player_get_kill_count, ":kill_count", ":my_player_no"),
					(player_get_death_count, ":death_count", ":my_player_no"),
					(gt, ":kill_count", ":death_count"),
					(unlock_achievement, ACHIEVEMENT_EVERY_BREATH_YOU_TAKE),
				(try_end),
				#EVERY_BREATH_YOU_TAKE achievement end
		])
		
		
		#script_multiplayer_event_agent_killed_or_wounded
		# Input: arg1 = dead_agent_no, arg2 = killer_agent_no
		# Output: none
multiplayer_event_agent_killed_or_wounded =	(
	"multiplayer_event_agent_killed_or_wounded",
			[
				(store_script_param, ":dead_agent_no", 1),
				(store_script_param, ":killer_agent_no", 2),
				
				(multiplayer_get_my_player, ":my_player_no"),
				(try_begin),
					(is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
					(player_get_agent_id, ":my_player_agent", ":my_player_no"),
					(ge, ":my_player_agent", 0),
					(try_begin),
						(eq, ":my_player_agent", ":dead_agent_no"),
						(store_mission_timer_a, "$g_multiplayer_respawn_start_time"),
					(try_end),
					(try_begin),
						(eq, ":my_player_agent", ":killer_agent_no"),
						(neq, ":my_player_agent", ":dead_agent_no"),
						(agent_is_human, ":dead_agent_no"),
						(agent_is_alive, ":my_player_agent"),
						(neg|agent_is_ally, ":dead_agent_no"),
						(agent_get_horse, ":my_horse_agent", ":my_player_agent"),
						(agent_get_wielded_item, ":my_wielded_item", ":my_player_agent", 0),
						(assign, ":my_item_class", -1),
						(try_begin),
							(ge, ":my_wielded_item", 0),
							(item_get_slot, ":my_item_class", ":my_wielded_item", slot_item_multiplayer_item_class),
						(try_end),
						#SPOIL_THE_CHARGE achievement
						(try_begin),
							(lt, ":my_horse_agent", 0),
							(agent_get_horse, ":dead_agent_horse_agent", ":dead_agent_no"),
							(ge, ":dead_agent_horse_agent", 0),
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_SPOIL_THE_CHARGE, 0),
							(lt, ":achievement_stat", 50),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_SPOIL_THE_CHARGE, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 50),
							(unlock_achievement, ACHIEVEMENT_SPOIL_THE_CHARGE),
						(try_end),
						#SPOIL_THE_CHARGE achievement end
						#HARASSING_HORSEMAN achievement
						(try_begin),
							(ge, ":my_horse_agent", 0),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_bow),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_crossbow),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_throwing),
							(eq, ":my_item_class", multi_item_class_type_throwing_axe),
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_HARASSING_HORSEMAN, 0),
							(lt, ":achievement_stat", 100),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_HARASSING_HORSEMAN, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 100),
							(unlock_achievement, ACHIEVEMENT_HARASSING_HORSEMAN),
						(try_end),
						#HARASSING_HORSEMAN achievement end
						#THROWING_STAR achievement
						(try_begin),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_throwing),
							(eq, ":my_item_class", multi_item_class_type_throwing_axe),
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_THROWING_STAR, 0),
							(lt, ":achievement_stat", 25),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_THROWING_STAR, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 25),
							(unlock_achievement, ACHIEVEMENT_THROWING_STAR),
						(try_end),
						#THROWING_STAR achievement end
						#SHISH_KEBAB achievement
						(try_begin),
							(ge, ":my_horse_agent", 0),
							(eq, ":my_item_class", multi_item_class_type_lance),
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_SHISH_KEBAB, 0),
							(lt, ":achievement_stat", 25),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_SHISH_KEBAB, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 25),
							(unlock_achievement, ACHIEVEMENT_SHISH_KEBAB),
						(try_end),
						#SHISH_KEBAB achievement end
						#CHOPPY_CHOP_CHOP achievement
						(try_begin),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_sword),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_axe),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_cleavers),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_two_handed_sword),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_two_handed_axe),
							(this_or_next|eq, ":my_wielded_item", "itm_sarranid_axe_a"), #sarranid item exception
							(eq, ":my_wielded_item", "itm_sarranid_axe_b"), #sarranid item exception
							#(neq, ":my_wielded_item", "itm_sarranid_two_handed_mace_1"), #sarranid item exception
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_CHOPPY_CHOP_CHOP, 0),
							(lt, ":achievement_stat", 50),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_CHOPPY_CHOP_CHOP, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 50),
							(unlock_achievement, ACHIEVEMENT_CHOPPY_CHOP_CHOP),
						(try_end),
						#CHOPPY_CHOP_CHOP achievement end
						#MACE_IN_YER_FACE achievement
						(try_begin),
							(this_or_next|eq, ":my_item_class", multi_item_class_type_blunt),
							#(eq, ":my_wielded_item", "itm_sarranid_two_handed_mace_1"), #sarranid item exception
							(neq, ":my_wielded_item", "itm_sarranid_axe_b"), #sarranid item exception
							(neq, ":my_wielded_item", "itm_sarranid_axe_a"), #sarranid item exception
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_MACE_IN_YER_FACE, 0),
							(lt, ":achievement_stat", 25),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_MACE_IN_YER_FACE, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 25),
							(unlock_achievement, ACHIEVEMENT_MACE_IN_YER_FACE),
						(try_end),
						#MACE_IN_YER_FACE achievement end
						#THE_HUSCARL achievement
						(try_begin),
							(eq, ":my_item_class", multi_item_class_type_throwing_axe),
							(get_achievement_stat, ":achievement_stat", ACHIEVEMENT_THE_HUSCARL, 0),
							(lt, ":achievement_stat", 50),
							(val_add, ":achievement_stat", 1),
							(set_achievement_stat, ACHIEVEMENT_THE_HUSCARL, 0, ":achievement_stat"),
							(ge, ":achievement_stat", 50),
							(unlock_achievement, ACHIEVEMENT_THE_HUSCARL),
						(try_end),
						#THE_HUSCARL achievement end
					(try_end),
				(try_end),
				
				(try_begin),
					(is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
					(player_get_agent_id, ":player_agent", ":my_player_no"),
					(eq, ":dead_agent_no", ":player_agent"),
					
					(assign, ":show_respawn_counter", 0),
					(try_begin),
						#TODO: add other game types with no respawns here
						(neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
						(neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
						(assign, ":show_respawn_counter", 1),
					(else_try),
						(eq, "$g_multiplayer_player_respawn_as_bot", 1),
						(player_get_team_no, ":my_player_team", ":my_player_no"),
						(assign, ":is_found", 0),
						(try_for_agents, ":cur_agent"),
							(eq, ":is_found", 0),
							(agent_is_alive, ":cur_agent"),
							(agent_is_human, ":cur_agent"),
							(agent_is_non_player, ":cur_agent"),
							(agent_get_team ,":cur_team", ":cur_agent"),
							(eq, ":cur_team", ":my_player_team"),
							(assign, ":is_found", 1),
						(try_end),
						(eq, ":is_found", 1),
						(assign, ":show_respawn_counter", 1),
					(try_end),
					
					(try_begin),
						#(player_get_slot, ":spawn_count", ":player_no", slot_player_spawn_count),
						(eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
						(gt, "$g_multiplayer_number_of_respawn_count", 0),
						
						(ge, "$g_my_spawn_count", "$g_multiplayer_number_of_respawn_count"),
						
						(multiplayer_get_my_player, ":my_player_no"),
						(player_get_team_no, ":my_player_team", ":my_player_no"),
						
						(this_or_next|eq, ":my_player_team", 0),
						(ge, "$g_my_spawn_count", 999),
						
						(assign, "$g_show_no_more_respawns_remained", 1),
					(else_try),
						(assign, "$g_show_no_more_respawns_remained", 0),
					(try_end),
					
					(eq, ":show_respawn_counter", 1),
					
					(start_presentation, "prsnt_multiplayer_respawn_time_counter"),
				(try_end),
		])
		

#script_multiplayer_set_item_available_for_troop
		# Input: arg1 = item_no, arg2 = troop_no
		# Output: none
multiplayer_set_item_available_for_troop =	(
	"multiplayer_set_item_available_for_troop",
			[
				(store_script_param, ":item_no", 1),
				(store_script_param, ":troop_no", 2),
				(store_sub, ":item_troop_slot", ":troop_no", multiplayer_troops_begin),
				(val_add, ":item_troop_slot", slot_item_multiplayer_availability_linked_list_begin),
				(item_set_slot, ":item_no", ":item_troop_slot", 1),
		])
		
		#script_multiplayer_send_item_selections
		# Input: none
		# Output: none
multiplayer_send_item_selections =	(
	"multiplayer_send_item_selections",
			[
				(multiplayer_get_my_player, ":my_player_no"),
				(try_for_range, ":i_item", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
					(player_get_slot, ":item_id", ":my_player_no", ":i_item"),
					(multiplayer_send_2_int_to_server, multiplayer_event_set_item_selection, ":i_item", ":item_id"),
				(try_end),
		])
		
		#script_multiplayer_set_default_item_selections_for_troop
		# Input: arg1 = troop_no
		# Output: none
multiplayer_set_default_item_selections_for_troop =	(
	"multiplayer_set_default_item_selections_for_troop",
			[
				(store_script_param, ":troop_no", 1),
				(multiplayer_get_my_player, ":my_player_no"),
				(call_script, "script_multiplayer_clear_player_selected_items", ":my_player_no"),
				(assign, ":cur_weapon_slot", 0),
				(troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
				(try_for_range, ":i_slot", 0, ":inv_cap"),
					(troop_get_inventory_slot, ":item_id", ":troop_no", ":i_slot"),
					(ge, ":item_id", 0),
					(item_get_slot, ":item_class", ":item_id", slot_item_multiplayer_item_class),
					(try_begin),
						(is_between, ":item_class", multi_item_class_type_weapons_begin, multi_item_class_type_weapons_end),
						(this_or_next|eq, "$g_multiplayer_disallow_ranged_weapons", 0),
						(neg|is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
						(store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, ":cur_weapon_slot"),
						(player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
						(val_add, ":cur_weapon_slot", 1),
					(else_try),
						(is_between, ":item_class", multi_item_class_type_heads_begin, multi_item_class_type_heads_end),
						(store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 4),
						(player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
					(else_try),
						(is_between, ":item_class", multi_item_class_type_bodies_begin, multi_item_class_type_bodies_end),
						(store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 5),
						(player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
					(else_try),
						(is_between, ":item_class", multi_item_class_type_feet_begin, multi_item_class_type_feet_end),
						(store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 6),
						(player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
					(else_try),
						(is_between, ":item_class", multi_item_class_type_gloves_begin, multi_item_class_type_gloves_end),
						(store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 7),
						(player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
					(else_try),
						(is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
						(eq, "$g_horses_are_avaliable", 1),
						(store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 8),
						(player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
					(try_end),
				(try_end),
		])
		
		#script_multiplayer_display_available_items_for_troop_and_item_classes
		# Input: arg1 = troop_no, arg2 = item_classes_begin, arg3 = item_classes_end, arg4 = pos_x_begin, arg5 = pos_y_begin
		# Output: none
multiplayer_display_available_items_for_troop_and_item_classes =	(
	"multiplayer_display_available_items_for_troop_and_item_classes",
			[
				(store_script_param, ":troop_no", 1),
				(store_script_param, ":item_classes_begin", 2),
				(store_script_param, ":item_classes_end", 3),
				(store_script_param, ":pos_x_begin", 4),
				(store_script_param, ":pos_y_begin", 5),
				
				(assign, ":x_adder", 100),
				(try_begin),
					(gt, ":pos_x_begin", 500),
					(assign, ":x_adder", -100),
				(try_end),
				
				(store_sub, ":item_troop_slot", ":troop_no", multiplayer_troops_begin),
				(val_add, ":item_troop_slot", slot_item_multiplayer_availability_linked_list_begin),
				
				(try_for_range, ":cur_slot", multi_data_item_button_indices_begin, multi_data_item_button_indices_end),
					(troop_set_slot, "trp_multiplayer_data", ":cur_slot", -1),
				(try_end),
				
				(assign, ":num_available_items", 0),
				
				(try_for_range, ":item_no", all_items_begin, all_items_end),
					(item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
					(is_between, ":item_class", ":item_classes_begin", ":item_classes_end"),
					(this_or_next|eq, "$g_multiplayer_disallow_ranged_weapons", 0),
					(neg|is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
					(item_slot_ge, ":item_no", ":item_troop_slot", 1),
					(store_add, ":cur_slot_index", ":num_available_items", multi_data_item_button_indices_begin),
					#using the result array for item_ids
					(troop_set_slot, "trp_multiplayer_data", ":cur_slot_index", ":item_no"),
					(val_add, ":num_available_items", 1),
				(try_end),
				
				#sorting
				(store_add, ":item_slots_end", ":num_available_items", multi_data_item_button_indices_begin),
				(store_sub, ":item_slots_end_minus_one", ":item_slots_end", 1),
				(try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end_minus_one"),
					(store_add, ":cur_slot_2_begin", ":cur_slot", 1),
					(try_for_range, ":cur_slot_2", ":cur_slot_2_begin", ":item_slots_end"),
						(troop_get_slot, ":item_1", "trp_multiplayer_data", ":cur_slot"),
						(troop_get_slot, ":item_2", "trp_multiplayer_data", ":cur_slot_2"),
						(call_script, "script_multiplayer_get_item_value_for_troop", ":item_1", ":troop_no"),
						(assign, ":item_1_point", reg0),
						(call_script, "script_multiplayer_get_item_value_for_troop", ":item_2", ":troop_no"),
						(assign, ":item_2_point", reg0),
						(item_get_slot, ":item_1_class", ":item_1", slot_item_multiplayer_item_class),
						(item_get_slot, ":item_2_class", ":item_2", slot_item_multiplayer_item_class),
						(val_mul, ":item_1_class", 1000000), #assuming maximum item price is 1000000
						(val_mul, ":item_2_class", 1000000), #assuming maximum item price is 1000000
						(val_add, ":item_1_point", ":item_1_class"),
						(val_add, ":item_2_point", ":item_2_class"),
						(lt, ":item_2_point", ":item_1_point"),
						(troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":item_2"),
						(troop_set_slot, "trp_multiplayer_data", ":cur_slot_2", ":item_1"),
					(try_end),
				(try_end),
				
				(troop_get_slot, ":last_item_no", "trp_multiplayer_data", multi_data_item_button_indices_begin),
				(assign, ":num_item_classes", 0),
				(try_begin),
					(ge, ":last_item_no", 0),
					(item_get_slot, ":last_item_class", ":last_item_no", slot_item_multiplayer_item_class),
					
					(try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end"),
						(troop_get_slot, ":item_no", "trp_multiplayer_data", ":cur_slot"),
						(item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
						(neq, ":item_class", ":last_item_class"),
						(val_add, ":num_item_classes", 1),
						(assign, ":last_item_class", ":item_class"),
					(try_end),
					
					(try_begin),
						(store_mul, ":required_y", ":num_item_classes", 100),
						(gt, ":required_y", ":pos_y_begin"),
						(store_sub, ":dif", ":required_y", ":pos_y_begin"),
						(val_div, ":dif", 100),
						(val_add, ":dif", 1),
						(val_mul, ":dif", 100),
						(val_add, ":pos_y_begin", ":dif"),
					(try_end),
					
					(item_get_slot, ":last_item_class", ":last_item_no", slot_item_multiplayer_item_class),
				(try_end),
				(assign, ":cur_x", ":pos_x_begin"),
				(assign, ":cur_y", ":pos_y_begin"),
				(try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end"),
					(troop_get_slot, ":item_no", "trp_multiplayer_data", ":cur_slot"),
					(item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
					(try_begin),
						(neq, ":item_class", ":last_item_class"),
						(val_sub, ":cur_y", 100),
						(assign, ":cur_x", ":pos_x_begin"),
						(assign, ":last_item_class", ":item_class"),
					(try_end),
					(create_image_button_overlay, ":cur_obj", "mesh_mp_inventory_choose", "mesh_mp_inventory_choose"),
					(position_set_x, pos1, 800),
					(position_set_y, pos1, 800),
					(overlay_set_size, ":cur_obj", pos1),
					(position_set_x, pos1, ":cur_x"),
					(position_set_y, pos1, ":cur_y"),
					(overlay_set_position, ":cur_obj", pos1),
					(create_mesh_overlay_with_item_id, reg0, ":item_no"),
					(store_add, ":item_x", ":cur_x", 50),
					(store_add, ":item_y", ":cur_y", 50),
					(position_set_x, pos1, ":item_x"),
					(position_set_y, pos1, ":item_y"),
					(overlay_set_position, reg0, pos1),
					(val_add, ":cur_x", ":x_adder"),
				(try_end),
		])
		
				# script_multiplayer_count_players_bots
		# Input: none
		# Output: none
multiplayer_count_players_bots =	(
	"multiplayer_count_players_bots",
			[
				(get_max_players, ":num_players"),
				(try_for_range, ":cur_player", 0, ":num_players"),
					(player_is_active, ":cur_player"),
					(player_set_slot, ":cur_player", slot_player_last_bot_count, 0),
				(try_end),
				
				(try_for_agents, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					(agent_is_alive, ":cur_agent"),
					(agent_get_player_id, ":agent_player", ":cur_agent"),
					(lt, ":agent_player", 0), #not a player
					(agent_get_group, ":agent_group", ":cur_agent"),
					(player_is_active, ":agent_group"),
					(player_get_slot, ":bot_count", ":agent_group", slot_player_last_bot_count),
					(val_add, ":bot_count", 1),
					(player_set_slot, ":agent_group", slot_player_last_bot_count, ":bot_count"),
				(try_end),
		])
		
		
		# script_multiplayer_change_leader_of_bot
		# Input: arg1 = agent_no
		# Output: none
multiplayer_change_leader_of_bot =	(
	"multiplayer_change_leader_of_bot",
			[
				(store_script_param, ":agent_no", 1),
				(agent_get_team, ":team_no", ":agent_no"),
				(call_script, "script_multiplayer_find_player_leader_for_bot", ":team_no", 1),
				(assign, ":leader_player", reg0),
				(agent_set_group, ":agent_no", ":leader_player"),
		])
		
		# script_multiplayer_find_spawn_point
		# Input: arg1 = team_no, arg2 = examine_all_spawn_points, arg3 = is_horseman
		# Output: none
multiplayer_find_spawn_point =	(
	"multiplayer_find_spawn_point",
			[
				(store_script_param, ":team_no", 1),
				(store_script_param, ":examine_all_spawn_points", 2), #0-dm, 1-tdm, 2-cf, 3-hq, 4-sg
				(store_script_param, ":is_horseman", 3), #0:no, 1:yes, -1:do not care
				
				(set_fixed_point_multiplier, 100),
				
				(assign, ":flags", 0),
				
				(try_begin),
					(eq, ":examine_all_spawn_points", 1),
					(val_or, ":flags", spf_examine_all_spawn_points),
				(try_end),
				
				(try_begin),
					(eq, ":is_horseman", 1),
					(val_or, ":flags", spf_is_horseman),
				(try_end),
				
				(try_begin),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
					(val_or, ":flags", spf_all_teams_are_enemy),
					(val_or, ":flags", spf_try_to_spawn_close_to_at_least_one_enemy),
				(else_try),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
					(val_or, ":flags", spf_try_to_spawn_close_to_at_least_one_enemy),
				(else_try),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
					(val_or, ":flags", spf_team_1_spawn_far_from_entry_66), #team 1 agents will not spawn 70 meters around of entry 0
					(val_or, ":flags", spf_team_0_walkers_spawn_at_high_points),
					(val_or, ":flags", spf_team_0_spawn_near_entry_66),
					(val_or, ":flags", spf_care_agent_to_agent_distances_less),
				(else_try),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
					(val_or, ":flags", spf_team_1_spawn_far_from_entry_0), #team 1 agents will not spawn 70 meters around of entry 0
					(val_or, ":flags", spf_team_0_spawn_far_from_entry_32), #team 0 agents will not spawn 70 meters around of entry 32
					(val_or, ":flags", spf_try_to_spawn_close_to_at_least_one_enemy),
				(else_try),
					(eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
					(assign, ":assigned_flag_count", 0),
					
					(store_sub, ":maximum_moved_flag_distance", multi_headquarters_pole_height, 50), #900 - 50 = 850
					(store_mul, ":maximum_moved_flag_distance_sq", ":maximum_moved_flag_distance", ":maximum_moved_flag_distance"),
					(val_div, ":maximum_moved_flag_distance_sq", 100), #dividing 100, because fixed point multiplier is 100 and it is included twice, look above line.
					
					(try_for_range, ":flag_no", 0, "$g_number_of_flags"),
						(store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
						(troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),
						
						(scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
						(prop_instance_get_position, pos0, ":pole_id"),
						
						(try_begin),
							(eq, ":cur_flag_owner", 1),
							(scene_prop_get_instance, ":flag_of_team_1", "$team_1_flag_scene_prop", ":flag_no"),
							
							(prop_instance_get_position, pos1, ":flag_of_team_1"),
							(get_sq_distance_between_positions, ":flag_height_sq", pos0, pos1),
							(ge, ":flag_height_sq", ":maximum_moved_flag_distance_sq"),
							
							(set_spawn_effector_scene_prop_id, ":assigned_flag_count", ":flag_of_team_1"),
							(val_add, ":assigned_flag_count", 1),
						(else_try),
							(eq, ":cur_flag_owner", 2),
							(scene_prop_get_instance, ":flag_of_team_2", "$team_2_flag_scene_prop", ":flag_no"),
							
							(prop_instance_get_position, pos1, ":flag_of_team_2"),
							(get_sq_distance_between_positions, ":flag_height_sq", pos0, pos1),
							(ge, ":flag_height_sq", ":maximum_moved_flag_distance_sq"),
							
							(set_spawn_effector_scene_prop_id, ":assigned_flag_count", ":flag_of_team_2"),
							(val_add, ":assigned_flag_count", 1),
						(try_end),
					(try_end),
					(set_spawn_effector_scene_prop_id, ":assigned_flag_count", -1),
				(try_end),
				
				(multiplayer_find_spawn_point, reg0, ":team_no", ":flags"),
		])
		
		
		
		#script_multiplayer_buy_agent_equipment
		# Input: arg1 = player_no
		# Output: none
multiplayer_buy_agent_equipment =	(
	"multiplayer_buy_agent_equipment",
			[
				(store_script_param, ":player_no", 1),
				(player_get_troop_id, ":player_troop", ":player_no"),
				(player_get_gold, ":player_gold", ":player_no"),
				(player_get_slot, ":added_gold", ":player_no", slot_player_last_rounds_used_item_earnings),
				(player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, 0),
				(val_add, ":player_gold", ":added_gold"),
				(assign, ":armor_bought", 0),
				
				#moving original values to temp slots
				(try_for_range, ":i_item", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
					(player_get_slot, ":selected_item_index", ":player_no", ":i_item"),
					(store_sub, ":i_cur_selected_item", ":i_item", slot_player_selected_item_indices_begin),
					(try_begin),
						(player_item_slot_is_picked_up, ":player_no", ":i_cur_selected_item"),
						(assign, ":selected_item_index", -1),
					(try_end),
					(val_add, ":i_cur_selected_item", slot_player_cur_selected_item_indices_begin),
					(player_set_slot, ":player_no", ":i_cur_selected_item", ":selected_item_index"),
				(try_end),
				(assign, ":end_cond", 1000),
				(try_for_range, ":unused", 0, ":end_cond"),
					(call_script, "script_multiplayer_calculate_cur_selected_items_cost", ":player_no", 0),
					(assign, ":total_cost", reg0),
					(try_begin),
						(gt, ":total_cost", ":player_gold"),
						#downgrade one of the selected items
						#first normalize the prices
						#then prioritize some of the weapon classes for specific troop classes
						(call_script, "script_multiplayer_get_troop_class", ":player_troop"),
						(assign, ":player_troop_class", reg0),
						
						(assign, ":max_cost_value", 0),
						(assign, ":max_cost_value_index", -1),
						(try_for_range, ":i_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
							(player_get_slot, ":item_id", ":player_no", ":i_item"),
							(ge, ":item_id", 0), #might be -1 for horses etc.
							(call_script, "script_multiplayer_get_item_value_for_troop", ":item_id", ":player_troop"),
							(assign, ":item_value", reg0),
							(store_sub, ":item_type", ":i_item", slot_player_cur_selected_item_indices_begin),
							(try_begin), #items
								(this_or_next|eq, ":item_type", 0),
								(this_or_next|eq, ":item_type", 1),
								(this_or_next|eq, ":item_type", 2),
								(eq, ":item_type", 3),
								(val_mul, ":item_value", 5),
							(else_try), #head
								(eq, ":item_type", 4),
								(val_mul, ":item_value", 4),
							(else_try), #body
								(eq, ":item_type", 5),
								(val_mul, ":item_value", 2),
							(else_try), #foot
								(eq, ":item_type", 6),
								(val_mul, ":item_value", 8),
							(else_try), #gloves
								(eq, ":item_type", 7),
								(val_mul, ":item_value", 8),
							(else_try), #horse
								#base value (most expensive)
							(try_end),
							(item_get_slot, ":item_class", ":item_id", slot_item_multiplayer_item_class),
							(try_begin),
								(eq, ":player_troop_class", multi_troop_class_infantry),
								(this_or_next|eq, ":item_class", multi_item_class_type_sword),
								(this_or_next|eq, ":item_class", multi_item_class_type_axe),
								(this_or_next|eq, ":item_class", multi_item_class_type_blunt),
								(this_or_next|eq, ":item_class", multi_item_class_type_war_picks),
								(this_or_next|eq, ":item_class", multi_item_class_type_two_handed_sword),
								(this_or_next|eq, ":item_class", multi_item_class_type_small_shield),
								(eq, ":item_class", multi_item_class_type_two_handed_axe),
								(val_div, ":item_value", 2),
							(else_try),
								(eq, ":player_troop_class", multi_troop_class_spearman),
								(this_or_next|eq, ":item_class", multi_item_class_type_spear),
								(eq, ":item_class", multi_item_class_type_large_shield),
								(val_div, ":item_value", 2),
							(else_try),
								(eq, ":player_troop_class", multi_troop_class_cavalry),
								(this_or_next|eq, ":item_class", multi_item_class_type_lance),
								(this_or_next|eq, ":item_class", multi_item_class_type_sword),
								(eq, ":item_class", multi_item_class_type_horse),
								(val_div, ":item_value", 2),
							(else_try),
								(eq, ":player_troop_class", multi_troop_class_archer),
								(this_or_next|eq, ":item_class", multi_item_class_type_bow),
								(eq, ":item_class", multi_item_class_type_arrow),
								(val_div, ":item_value", 2),
							(else_try),
								(eq, ":player_troop_class", multi_troop_class_crossbowman),
								(this_or_next|eq, ":item_class", multi_item_class_type_crossbow),
								(eq, ":item_class", multi_item_class_type_bolt),
								(val_div, ":item_value", 2),
							(else_try),
								(eq, ":player_troop_class", multi_troop_class_mounted_archer),
								(this_or_next|eq, ":item_class", multi_item_class_type_bow),
								(this_or_next|eq, ":item_class", multi_item_class_type_arrow),
								(eq, ":item_class", multi_item_class_type_horse),
								(val_div, ":item_value", 2),
							(else_try),
								(eq, ":player_troop_class", multi_troop_class_mounted_crossbowman),
								(this_or_next|eq, ":item_class", multi_item_class_type_crossbow),
								(this_or_next|eq, ":item_class", multi_item_class_type_bolt),
								(eq, ":item_class", multi_item_class_type_horse),
								(val_div, ":item_value", 2),
							(try_end),
							
							(try_begin),
								(gt, ":item_value", ":max_cost_value"),
								(assign, ":max_cost_value", ":item_value"),
								(assign, ":max_cost_value_index", ":i_item"),
							(try_end),
						(try_end),
						
						#max_cost_value and max_cost_value_index will definitely be valid
						#unless no items are left (therefore some items must cost 0 gold)
						(player_get_slot, ":item_id", ":player_no", ":max_cost_value_index"),
						(call_script, "script_multiplayer_get_previous_item_for_item_and_troop", ":item_id", ":player_troop"),
						(assign, ":item_id", reg0),
						(player_set_slot, ":player_no", ":max_cost_value_index", ":item_id"),
					(else_try),
						(assign, ":end_cond", 0),
						(val_sub, ":player_gold", ":total_cost"),
						(player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
						(try_for_range, ":i_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
							(player_get_slot, ":item_id", ":player_no", ":i_item"),
							#checking if different class default item replace is needed for weapons
							(try_begin),
								(ge, ":item_id", 0),
								#then do nothing
							(else_try),
								(store_sub, ":base_index_slot", ":i_item", slot_player_cur_selected_item_indices_begin),
								(store_add, ":selected_item_index_slot", ":base_index_slot", slot_player_selected_item_indices_begin),
								(player_get_slot, ":selected_item_index", ":player_no", ":selected_item_index_slot"),
								(this_or_next|eq, ":selected_item_index", -1),
								(player_item_slot_is_picked_up, ":player_no", ":base_index_slot"),
								#then do nothing
							(else_try),
								#an item class without a default value is -1, then find a default weapon
								(item_get_slot, ":item_class", ":selected_item_index", slot_item_multiplayer_item_class),
								(is_between, ":item_class", multi_item_class_type_weapons_begin, multi_item_class_type_weapons_end),
								(assign, ":dc_replaced_item", -1),
								(try_for_range, ":i_dc_item_class", multi_item_class_type_melee_weapons_begin, multi_item_class_type_melee_weapons_end),
									(lt, ":dc_replaced_item", 0),
									(assign, ":dc_item_class_used", 0),
									(try_for_range, ":i_dc_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
										(player_get_slot, ":dc_cur_item", ":player_no", ":i_dc_item"),
										(ge, ":dc_cur_item", 0),
										(item_get_slot, ":dc_item_class", ":dc_cur_item", slot_item_multiplayer_item_class),
										(eq, ":dc_item_class", ":i_dc_item_class"),
										(assign, ":dc_item_class_used", 1),
									(try_end),
									(eq, ":dc_item_class_used", 0),
									(assign, ":dc_end_cond", all_items_end),
									(try_for_range, ":i_dc_new_item", all_items_begin, ":dc_end_cond"),
										(item_slot_eq, ":i_dc_new_item", slot_item_multiplayer_item_class, ":i_dc_item_class"),
										(call_script, "script_cf_multiplayer_is_item_default_for_troop", ":i_dc_new_item", ":player_troop"),
										(assign, ":dc_end_cond", 0), #break
										(assign, ":dc_replaced_item", ":i_dc_new_item"),
									(try_end),
								(try_end),
								(ge, ":dc_replaced_item", 0),
								(player_set_slot, ":player_no", ":i_item", ":dc_replaced_item"),
								(assign, ":item_id", ":dc_replaced_item"),
							(try_end),
							
							#finally, add the item to agent
							(try_begin),
								(ge, ":item_id", 0), #might be -1 for horses etc.
								(store_sub, ":item_slot", ":i_item", slot_player_cur_selected_item_indices_begin),
								(player_add_spawn_item, ":player_no", ":item_slot", ":item_id"),
								(try_begin),
									(eq, ":item_slot", ek_body), #ek_body is the slot for armor
									(assign, ":armor_bought", 1),
								(try_end),
							(try_end),
						(try_end),
						
						(player_set_slot, ":player_no", slot_player_total_equipment_value, ":total_cost"),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":armor_bought", 0),
					(eq, "$g_multiplayer_force_default_armor", 1),
					(assign, ":end_cond", all_items_end),
					(try_for_range, ":i_new_item", all_items_begin, ":end_cond"),
						(this_or_next|item_slot_eq, ":i_new_item", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
						(this_or_next|item_slot_eq, ":i_new_item", slot_item_multiplayer_item_class, multi_item_class_type_medium_armor),
						(item_slot_eq, ":i_new_item", slot_item_multiplayer_item_class, multi_item_class_type_heavy_armor),
						(call_script, "script_cf_multiplayer_is_item_default_for_troop", ":i_new_item", ":player_troop"),
						(assign, ":end_cond", 0), #break
						(player_add_spawn_item, ":player_no", ek_body, ":i_new_item"), #ek_body is the slot for armor
					(try_end),
				(try_end),
		])