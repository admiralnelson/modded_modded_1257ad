from header import *

		# script_change_player_party_morale
		# Input: arg1 = morale difference
		# Output: none
change_player_party_morale=(
	"change_player_party_morale",
			[
				(store_script_param_1, ":morale_dif"),
				(party_get_morale, ":cur_morale", "p_main_party"),
				(val_clamp, ":cur_morale", 0, 100),
				
				(store_add, ":new_morale", ":cur_morale", ":morale_dif"),
				(val_clamp, ":new_morale", 0, 100),
				
				(party_set_morale, "p_main_party", ":new_morale"),
				(try_begin),
					(lt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":cur_morale", ":new_morale"),
					(display_message, "str_party_lost_morale"),
				(else_try),
					(gt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":new_morale", ":cur_morale"),
					(display_message, "str_party_gained_morale"),
				(try_end),
		])
		

		# script_change_player_honor
		# prints "you gain/lose honour" if player honour changes
		# Input: arg1 = honor difference
		# Output: none
change_player_honor=(
	"change_player_honor",
			[
				(store_script_param_1, ":honor_dif"),
				(val_add, "$player_honor", ":honor_dif"),
				(try_begin),
					(gt, ":honor_dif", 0),
					(display_message, "@You gain honour."),
				(else_try),
					(lt, ":honor_dif", 0),
					(display_message, "@You lose honour."),
				(try_end),
				
				##      (val_mul, ":honor_dif", 1000),
				##      (assign, ":temp_honor", 0),
				##      (assign, ":num_nonlinear_steps", 10),
				##      (try_begin),
				##        (gt, "$player_honor", 0),
				##        (lt, ":honor_dif", 0),
				##        (assign, ":num_nonlinear_steps", 0),
				##      (else_try),
				##        (lt, "$player_honor", 0),
				##        (gt, ":honor_dif", 0),
				##        (assign, ":num_nonlinear_steps", 3),
				##      (try_end),
				##
				##      (try_begin),
				##        (ge, "$player_honor", 0),
				##        (assign, ":temp_honor", "$player_honor"),
				##      (else_try),
				##        (val_sub, ":temp_honor", "$player_honor"),
				##      (try_end),
				##      (try_for_range, ":unused",0,":num_nonlinear_steps"),
				##        (ge, ":temp_honor", 10000),
				##        (val_div, ":temp_honor", 2),
				##        (val_div, ":honor_dif", 2),
				##      (try_end),
				##      (val_add, "$player_honor", ":honor_dif"),
		])


		# script_change_player_party_morale
		# Input: arg1 = morale difference
		# Output: none
change_player_party_morale=(
	"change_player_party_morale",
			[
				(store_script_param_1, ":morale_dif"),
				(party_get_morale, ":cur_morale", "p_main_party"),
				(val_clamp, ":cur_morale", 0, 100),
				
				(store_add, ":new_morale", ":cur_morale", ":morale_dif"),
				(val_clamp, ":new_morale", 0, 100),
				
				(party_set_morale, "p_main_party", ":new_morale"),
				(try_begin),
					(lt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":cur_morale", ":new_morale"),
					(display_message, "str_party_lost_morale"),
				(else_try),
					(gt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":new_morale", ":cur_morale"),
					(display_message, "str_party_gained_morale"),
				(try_end),
		])
		