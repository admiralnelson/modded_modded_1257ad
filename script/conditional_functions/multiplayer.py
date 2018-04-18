from header import *

# script_cf_multiplayer_evaluate_poll
# Input: none
# Output: none (can fail)
cf_multiplayer_evaluate_poll =	(
	"cf_multiplayer_evaluate_poll",
			[
				(assign, ":result", 0),
				(assign, "$g_multiplayer_poll_ended", 1),
				(store_add, ":total_votes", "$g_multiplayer_poll_yes_count", "$g_multiplayer_poll_no_count"),
				(store_sub, ":abstain_votes", "$g_multiplayer_poll_num_sent", ":total_votes"),
				(store_mul, ":nos_from_abstains", 3, ":abstain_votes"),
				(val_div, ":nos_from_abstains", 10), #30% of abstains are counted as no
				(val_add, ":total_votes", ":nos_from_abstains"),
				(val_max, ":total_votes", 1), #if someone votes and only 1-3 abstain occurs?
				(store_mul, ":vote_ratio", 100, "$g_multiplayer_poll_yes_count"),
				(val_div, ":vote_ratio", ":total_votes"),
				(try_begin),
					(ge, ":vote_ratio", "$g_multiplayer_valid_vote_ratio"),
					(assign, ":result", 1),
					(try_begin),
						(eq, "$g_multiplayer_poll_to_show", 1), #kick player
						(try_begin),
							(player_is_active, "$g_multiplayer_poll_value_to_show"),
							(kick_player, "$g_multiplayer_poll_value_to_show"),
						(try_end),
					(else_try),
						(eq, "$g_multiplayer_poll_to_show", 2), #ban player
						(ban_player_using_saved_ban_info), #already loaded at the beginning of the poll
					(else_try),
						(eq, "$g_multiplayer_poll_to_show", 3), #change map with factions
						(team_set_faction, 0, "$g_multiplayer_poll_value_2_to_show"),
						(team_set_faction, 1, "$g_multiplayer_poll_value_3_to_show"),
					(else_try),
						(eq, "$g_multiplayer_poll_to_show", 4), #change number of bots
						(assign, "$g_multiplayer_num_bots_team_1", "$g_multiplayer_poll_value_to_show"),
						(assign, "$g_multiplayer_num_bots_team_2", "$g_multiplayer_poll_value_2_to_show"),
						(get_max_players, ":num_players"),
						(try_for_range, ":cur_player", 1, ":num_players"),
							(player_is_active, ":cur_player"),
							(multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
							(multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
						(try_end),
					(try_end),
				(else_try),
					(assign, "$g_multiplayer_poll_running", 0), #end immediately if poll fails. but end after some time if poll succeeds (apply the results first)
				(try_end),
				(get_max_players, ":num_players"),
				#for only server itself-----------------------------------------------------------------------------------------------
				(call_script, "script_show_multiplayer_message", multiplayer_message_type_poll_result, ":result"), #0 is useless here
				#for only server itself-----------------------------------------------------------------------------------------------
				(try_for_range, ":cur_player", 1, ":num_players"),
					(player_is_active, ":cur_player"),
					(multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_show_multiplayer_message, multiplayer_message_type_poll_result, ":result"),
				(try_end),
				(eq, ":result", 1),
		])

		# script_cf_multiplayer_team_is_available
		# Input: arg1 = player_no, arg2 = team_no
		# Output: none, true or false
cf_multiplayer_team_is_available =	(
	"cf_multiplayer_team_is_available",
			[
				(store_script_param, ":player_no", 1),
				(store_script_param, ":team_no", 2),
				(assign, ":continue_change_team", 1),
				(try_begin),
					(neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
					(neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
					(is_between, ":team_no", 0, multi_team_spectator),
					(neg|teams_are_enemies, ":team_no", ":team_no"), #checking if it is a deathmatch or not
					(assign, ":continue_change_team", 0),
					#counting number of players for team balance checks
					(assign, ":number_of_players_at_team_1", 0),
					(assign, ":number_of_players_at_team_2", 0),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 0, ":num_players"),
						(player_is_active, ":cur_player"),
						(neq, ":cur_player", ":player_no"),
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
					
					(try_begin),
						(ge, ":difference_of_number_of_players", 0),
						(val_add, ":difference_of_number_of_players", 1),
					(else_try),
						(val_add, ":difference_of_number_of_players", -1),
					(try_end),
					
					(try_begin),
						(eq, ":team_no", 0),
						(lt, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
						(assign, ":continue_change_team", 1),
					(else_try),
						(eq, ":team_no", 1),
						(store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
						(gt, ":difference_of_number_of_players", ":checked_value"),
						(assign, ":continue_change_team", 1),
					(try_end),
				(try_end),
				(eq, ":continue_change_team", 1),
		])

#script_cf_multiplayer_is_item_default_for_troop
		# Input: arg1 = item_no, arg2 = troop_no
		# Output: reg0: total_cost
cf_multiplayer_is_item_default_for_troop =	(
	"cf_multiplayer_is_item_default_for_troop",
			[
				(store_script_param, ":item_no", 1),
				(store_script_param, ":troop_no", 2),
				(assign, ":default_item", 0),
				(try_begin),
					(neg|is_between, ":item_no", horses_begin, horses_end),
					(neq, ":item_no", "itm_warhorse_sarranid"),
					(neq, ":item_no", "itm_warhorse_steppe"),
					
					(troop_get_inventory_capacity, ":end_cond", ":troop_no"), #troop no can come -1 here error occured at friday
					(try_for_range, ":i_slot", 0, ":end_cond"),
						(troop_get_inventory_slot, ":default_item_id", ":troop_no", ":i_slot"),
						(eq, ":item_no", ":default_item_id"),
						(assign, ":default_item", 1),
						(assign, ":end_cond", 0), #break
					(try_end),
				(try_end),
				(eq, ":default_item", 1),
		])