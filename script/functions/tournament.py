from header import *

# script_get_num_tournament_participants
		# Input: none
		# Output: reg0 = num_participants
get_num_tournament_participants = (
	"get_num_tournament_participants",
			[(assign, ":num_participants", 0),
				(try_for_range, ":cur_slot", 0, 64),
					(troop_slot_ge, "trp_tournament_participants", ":cur_slot", 0),
					(val_add, ":num_participants", 1),
				(try_end),
				(assign, reg0, ":num_participants"),
		])
		
		# script_get_random_tournament_participant
		# Input: none
		# Output: reg0 = troop_no
get_random_tournament_participant = (
	"get_random_tournament_participant",
			[(call_script, "script_get_num_tournament_participants"),
				(assign, ":num_participants", reg0),
				(store_random_in_range, ":random_troop", 0, ":num_participants"),
				(assign, ":continue", 1),
				(try_for_range, ":cur_slot", 0, 64),
					(eq, ":continue", 1),
					(troop_slot_ge, "trp_tournament_participants", ":cur_slot", 0),
					(val_sub, ":random_troop", 1),
					(lt, ":random_troop", 0),
					(assign, ":continue", 0),
					(troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
					(troop_set_slot, "trp_tournament_participants", ":cur_slot", -1),
				(try_end),
				(assign, reg0, ":troop_no"),
		])
		

		# script_get_random_tournament_team_amount_and_size
		# Input: none
		# Output: reg0 = number_of_teams, reg1 = team_size
get_random_tournament_team_amount_and_size = (
	"get_random_tournament_team_amount_and_size",
			[
				(call_script, "script_get_num_tournament_participants"),
				(assign, ":num_participants", reg0),
				(party_get_slot, ":town_max_teams", "$current_town", slot_town_tournament_max_teams),
				(val_add, ":town_max_teams", 1),
				(party_get_slot, ":town_max_team_size", "$current_town", slot_town_tournament_max_team_size),
				(val_add, ":town_max_team_size", 1),
				(assign, ":max_teams", ":num_participants"),
				(val_min, ":max_teams", ":town_max_teams"),
				(assign, ":max_size", ":num_participants"),
				(val_min, ":max_size", ":town_max_team_size"),
				(assign, ":min_size", 1),
				(try_begin),
					(ge, ":num_participants", 32),
					(assign, ":min_size", 2),
					(val_min, ":min_size", ":town_max_team_size"),
				(try_end),
				(assign, ":end_cond", 500),
				(try_for_range, ":unused", 0, ":end_cond"),
					(store_random_in_range, ":random_teams", 2, ":max_teams"),
					(store_random_in_range, ":random_size", ":min_size", ":max_size"),
					(store_mul, ":total_men", ":random_teams", ":random_size"),
					(le, ":total_men", ":num_participants"),
					(store_sub, ":left_men", ":num_participants", ":total_men"),
					(neq, ":left_men", 1),
					(assign, ":end_cond", 0),
				(try_end),
				(try_begin),
					(gt, ":end_cond", 0),
					(assign, ":random_teams", 2),
					(assign, ":random_size", 1),
				(try_end),
				(assign, reg0, ":random_teams"),
				(assign, reg1, ":random_size"),
		])
		
		# script_get_troop_priority_point_for_tournament
		# Input: arg1 = troop_no
		# Output: reg0 = troop_point
get_troop_priority_point_for_tournament = (
	"get_troop_priority_point_for_tournament",
			[(store_script_param, ":troop_no", 1),
				(assign, ":troop_point", 0),
				(try_begin),
					(ge, ":troop_no", 0),
					(val_add, ":troop_point", 40000),
					(try_begin),
						(eq, ":troop_no", "trp_player"),
						(val_add, ":troop_point", 80000),
					(try_end),
					(try_begin),
						(troop_is_hero, ":troop_no"),
						(val_add, ":troop_point", 20000),
					(try_end),
					(try_begin),
						(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_player_companion),
						(val_add, ":troop_point", 10000),
					(else_try),
						(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
						(troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
						(val_add, ":troop_point", ":renown"),
						(val_add, ":troop_point", 1000), #in order to make it more prior than tournament heroes with higher levels
					(else_try),
						(store_character_level, ":level", ":troop_no"),
						(val_add, ":troop_point", ":level"),
					(try_end),
				(try_end),
				(assign, reg0, ":troop_point"),
		])
		
		
		
		# script_get_win_amount_for_tournament_bet
		# Input: none
		# Output: reg0 = win_amount_with_100_denars
get_win_amount_for_tournament_bet = (
	"get_win_amount_for_tournament_bet",
			[
				(party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
				(try_begin),
					(eq, "$g_tournament_cur_tier", 0),
					(assign, ":win_amount", 120),
				(else_try),
					(eq, "$g_tournament_cur_tier", 1),
					(assign, ":win_amount", 90),
				(else_try),
					(eq, "$g_tournament_cur_tier", 2),
					(assign, ":win_amount", 60),
				(else_try),
					(eq, "$g_tournament_cur_tier", 3),
					(assign, ":win_amount", 40),
				(else_try),
					(eq, "$g_tournament_cur_tier", 4),
					(assign, ":win_amount", 20),
				(else_try),
					(assign, ":win_amount", 8),
				(try_end),
				(val_mul, ":win_amount", ":player_odds"),
				(val_div, ":win_amount", 100),
				(val_add, ":win_amount", 100), #win amount when 100 denars is placed
				(assign, reg0, ":win_amount"),
		])