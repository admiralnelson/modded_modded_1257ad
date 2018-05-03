from header import *

#script_game_get_console_command
# This script is called from the game engine when a console command is entered from the dedicated server.
# INPUT: anything
# OUTPUT: s0 = result text
game_get_console_command  = (
	"game_get_console_command",
		[
			(store_script_param, ":input", 1),
			(store_script_param, ":val1", 2),
			(try_begin),
				#getting val2 for some commands
				(eq, ":input", 2),
				(store_script_param, ":val2", 3),
			(end_try),
			(try_begin),
				(eq, ":input", 1),
				(assign, reg0, ":val1"),
				(try_begin),
					(eq, ":val1", 1),
					(assign, reg1, "$g_multiplayer_num_bots_team_1"),
					(str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
				(else_try),
					(eq, ":val1", 2),
					(assign, reg1, "$g_multiplayer_num_bots_team_2"),
					(str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 2),
				(assign, reg0, ":val1"),
				(assign, reg1, ":val2"),
				(try_begin),
					(eq, ":val1", 1),
					(ge, ":val2", 0),
					(assign, "$g_multiplayer_num_bots_team_1", ":val2"),
					(str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
				(else_try),
					(eq, ":val1", 2),
					(ge, ":val2", 0),
					(assign, "$g_multiplayer_num_bots_team_2", ":val2"),
					(str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 3),
				(assign, reg0, "$g_multiplayer_round_max_seconds"),
				(str_store_string, s0, "str_maximum_seconds_for_round_is_reg0"),
			(else_try),
				(eq, ":input", 4),
				(assign, reg0, ":val1"),
				(try_begin),
					(is_between, ":val1", multiplayer_round_max_seconds_min, multiplayer_round_max_seconds_max),
					(assign, "$g_multiplayer_round_max_seconds", ":val1"),
					(str_store_string, s0, "str_maximum_seconds_for_round_is_reg0"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_round_max_seconds, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 5),
				(assign, reg0, "$g_multiplayer_respawn_period"),
				(str_store_string, s0, "str_respawn_period_is_reg0_seconds"),
			(else_try),
				(eq, ":input", 6),
				(assign, reg0, ":val1"),
				(try_begin),
					(is_between, ":val1", multiplayer_respawn_period_min, multiplayer_respawn_period_max),
					(assign, "$g_multiplayer_respawn_period", ":val1"),
					(str_store_string, s0, "str_respawn_period_is_reg0_seconds"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 7),
				(assign, reg0, "$g_multiplayer_num_bots_voteable"),
				(str_store_string, s0, "str_bots_upper_limit_for_votes_is_reg0"),
			(else_try),
				(eq, ":input", 8),
				(try_begin),
					(is_between, ":val1", 0, 51),
					(assign, "$g_multiplayer_num_bots_voteable", ":val1"),
					(store_add, "$g_multiplayer_max_num_bots", ":val1", 1),
					(assign, reg0, "$g_multiplayer_num_bots_voteable"),
					(str_store_string, s0, "str_bots_upper_limit_for_votes_is_reg0"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_num_bots_voteable, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 9),
				(try_begin),
					(eq, "$g_multiplayer_maps_voteable", 1),
					(str_store_string, s0, "str_map_is_voteable"),
				(else_try),
					(str_store_string, s0, "str_map_is_not_voteable"),
				(try_end),
			(else_try),
				(eq, ":input", 10),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_maps_voteable", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_map_is_voteable"),
					(else_try),
						(str_store_string, s0, "str_map_is_not_voteable"),
					(try_end),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_maps_voteable, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 11),
				(try_begin),
					(eq, "$g_multiplayer_factions_voteable", 1),
					(str_store_string, s0, "str_factions_are_voteable"),
				(else_try),
					(str_store_string, s0, "str_factions_are_not_voteable"),
				(try_end),
			(else_try),
				(eq, ":input", 12),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_factions_voteable", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_factions_are_voteable"),
					(else_try),
						(str_store_string, s0, "str_factions_are_not_voteable"),
					(try_end),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_factions_voteable, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 13),
				(try_begin),
					(eq, "$g_multiplayer_player_respawn_as_bot", 1),
					(str_store_string, s0, "str_players_respawn_as_bot"),
				(else_try),
					(str_store_string, s0, "str_players_do_not_respawn_as_bot"),
				(try_end),
			(else_try),
				(eq, ":input", 14),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_player_respawn_as_bot", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_players_respawn_as_bot"),
					(else_try),
						(str_store_string, s0, "str_players_do_not_respawn_as_bot"),
					(try_end),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_player_respawn_as_bot, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 15),
				(try_begin),
					(eq, "$g_multiplayer_kick_voteable", 1),
					(str_store_string, s0, "str_kicking_a_player_is_voteable"),
				(else_try),
					(str_store_string, s0, "str_kicking_a_player_is_not_voteable"),
				(try_end),
			(else_try),
				(eq, ":input", 16),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_kick_voteable", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_kicking_a_player_is_voteable"),
					(else_try),
						(str_store_string, s0, "str_kicking_a_player_is_not_voteable"),
					(try_end),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_kick_voteable, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 17),
				(try_begin),
					(eq, "$g_multiplayer_ban_voteable", 1),
					(str_store_string, s0, "str_banning_a_player_is_voteable"),
				(else_try),
					(str_store_string, s0, "str_banning_a_player_is_not_voteable"),
				(try_end),
			(else_try),
				(eq, ":input", 18),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_ban_voteable", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_banning_a_player_is_voteable"),
					(else_try),
						(str_store_string, s0, "str_banning_a_player_is_not_voteable"),
					(try_end),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_ban_voteable, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 19),
				(assign, reg0, "$g_multiplayer_valid_vote_ratio"),
				(str_store_string, s0, "str_percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0"),
			(else_try),
				(eq, ":input", 20),
				(try_begin),
					(is_between, ":val1", 50, 101),
					(assign, "$g_multiplayer_valid_vote_ratio", ":val1"),
					(assign, reg0, ":val1"),
					(str_store_string, s0, "str_percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 21),
				(assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
				(str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
			(else_try),
				(eq, ":input", 22),
				(try_begin),
					(is_between, ":val1", 2, 7),
					(assign, "$g_multiplayer_auto_team_balance_limit", ":val1"),
					(assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
					(str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":val1"),
					(try_end),
				(else_try),
					(ge, ":val1", 7),
					(assign, "$g_multiplayer_auto_team_balance_limit", 1000),
					(assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
					(str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 23),
				(assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
				(str_store_string, s0, "str_starting_gold_ratio_is_reg0"),
			(else_try),
				(eq, ":input", 24),
				(try_begin),
					(is_between, ":val1", 0, 1001),
					(assign, "$g_multiplayer_initial_gold_multiplier", ":val1"),
					(assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
					(str_store_string, s0, "str_starting_gold_ratio_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 25),
				(assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
				(str_store_string, s0, "str_combat_gold_bonus_ratio_is_reg0"),
			(else_try),
				(eq, ":input", 26),
				(try_begin),
					(is_between, ":val1", 0, 1001),
					(assign, "$g_multiplayer_battle_earnings_multiplier", ":val1"),
					(assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
					(str_store_string, s0, "str_combat_gold_bonus_ratio_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 27),
				(assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
				(str_store_string, s0, "str_round_gold_bonus_ratio_is_reg0"),
			(else_try),
				(eq, ":input", 28),
				(try_begin),
					(is_between, ":val1", 0, 1001),
					(assign, "$g_multiplayer_round_earnings_multiplier", ":val1"),
					(assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
					(str_store_string, s0, "str_round_gold_bonus_ratio_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 29),
				(try_begin),
					(eq, "$g_multiplayer_allow_player_banners", 1),
					(str_store_string, s0, "str_player_banners_are_allowed"),
				(else_try),
					(str_store_string, s0, "str_player_banners_are_not_allowed"),
				(try_end),
			(else_try),
				(eq, ":input", 30),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_allow_player_banners", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_player_banners_are_allowed"),
					(else_try),
						(str_store_string, s0, "str_player_banners_are_not_allowed"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 31),
				(try_begin),
					(eq, "$g_multiplayer_force_default_armor", 1),
					(str_store_string, s0, "str_default_armor_is_forced"),
				(else_try),
					(str_store_string, s0, "str_default_armor_is_not_forced"),
				(try_end),
			(else_try),
				(eq, ":input", 32),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_force_default_armor", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_default_armor_is_forced"),
					(else_try),
						(str_store_string, s0, "str_default_armor_is_not_forced"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 33),
				(assign, reg0, "$g_multiplayer_point_gained_from_flags"),
				(str_store_string, s0, "str_point_gained_from_flags_is_reg0"),
			(else_try),
				(eq, ":input", 34),
				(try_begin),
					(is_between, ":val1", 25, 401),
					(assign, "$g_multiplayer_point_gained_from_flags", ":val1"),
					(assign, reg0, "$g_multiplayer_point_gained_from_flags"),
					(str_store_string, s0, "str_point_gained_from_flags_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 35),
				(assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
				(str_store_string, s0, "str_point_gained_from_capturing_flag_is_reg0"),
			(else_try),
				(eq, ":input", 36),
				(try_begin),
					(is_between, ":val1", 0, 11),
					(assign, "$g_multiplayer_point_gained_from_capturing_flag", ":val1"),
					(assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
					(str_store_string, s0, "str_point_gained_from_capturing_flag_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 37),
				(assign, reg0, "$g_multiplayer_game_max_minutes"),
				(str_store_string, s0, "str_map_time_limit_is_reg0"),
			(else_try),
				(eq, ":input", 38),
				(try_begin),
					(is_between, ":val1", 5, 121),
					(assign, "$g_multiplayer_game_max_minutes", ":val1"),
					(assign, reg0, "$g_multiplayer_game_max_minutes"),
					(str_store_string, s0, "str_map_time_limit_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 39),
				(assign, reg0, "$g_multiplayer_game_max_points"),
				(str_store_string, s0, "str_team_points_limit_is_reg0"),
			(else_try),
				(eq, ":input", 40),
				(try_begin),
					(is_between, ":val1", 3, 1001),
					(assign, "$g_multiplayer_game_max_points", ":val1"),
					(assign, reg0, "$g_multiplayer_game_max_points"),
					(str_store_string, s0, "str_team_points_limit_is_reg0"),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 41),
				(assign, reg0, "$g_multiplayer_number_of_respawn_count"),
				(try_begin),
					(eq, reg0, 0),
					(str_store_string, s1, "str_unlimited"),
				(else_try),
					(str_store_string, s1, "str_reg0"),
				(try_end),
				(str_store_string, s0, "str_defender_spawn_count_limit_is_s1"),
			(else_try),
				(eq, ":input", 42),
				(try_begin),
					(is_between, ":val1", 0, 6),
					(assign, "$g_multiplayer_number_of_respawn_count", ":val1"),
					(assign, reg0, "$g_multiplayer_number_of_respawn_count"),
					(try_begin),
						(eq, reg0, 0),
						(str_store_string, s1, "str_unlimited"),
					(else_try),
						(str_store_string, s1, "str_reg0"),
					(try_end),
					(str_store_string, s0, "str_defender_spawn_count_limit_is_s1"),
					(get_max_players, ":num_players"),
					(try_for_range, ":cur_player", 1, ":num_players"),
						(player_is_active, ":cur_player"),
						(multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_count, ":val1"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(eq, ":input", 43),
				(try_begin),
					(eq, "$g_multiplayer_disallow_ranged_weapons", 1),
					(str_store_string, s0, "str_ranged_weapons_are_disallowed"),
				(else_try),
					(str_store_string, s0, "str_ranged_weapons_are_allowed"),
				(try_end),
			(else_try),
				(eq, ":input", 44),
				(try_begin),
					(is_between, ":val1", 0, 2),
					(assign, "$g_multiplayer_disallow_ranged_weapons", ":val1"),
					(try_begin),
						(eq, ":val1", 1),
						(str_store_string, s0, "str_ranged_weapons_are_disallowed"),
					(else_try),
						(str_store_string, s0, "str_ranged_weapons_are_allowed"),
					(try_end),
				(else_try),
					(str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
				(try_end),
			(else_try),
				(str_store_string, s0, "@{!}DEBUG : SYSTEM ERROR!"),
			(try_end),
	])