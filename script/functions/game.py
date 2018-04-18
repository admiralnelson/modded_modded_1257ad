from header import *

#script_game_get_use_string
# This script is called from the game engine for getting using information text
# INPUT: used_scene_prop_id
# OUTPUT: s0
game_get_use_string = (
	"game_get_use_string",
		[
			(store_script_param, ":instance_id", 1),
			
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
			
			(scene_prop_get_slot, ":item_situation", ":instance_id", scene_prop_open_or_close_slot),
			
			(try_begin), #opening/closing portcullis
				(eq, ":effected_object", "spr_portcullis"),
				
				(try_begin),
					(eq, ":item_situation", 0),
					(str_store_string, s0, "str_open_gate"),
				(else_try),
					(str_store_string, s0, "str_close_gate"),
				(try_end),
			(else_try), #opening/closing door
				(this_or_next|eq, ":effected_object", "spr_door_destructible"),
				(this_or_next|eq, ":effected_object", "spr_castle_f_door_b"),
				(this_or_next|eq, ":effected_object", "spr_castle_e_sally_door_a"),
				(this_or_next|eq, ":effected_object", "spr_castle_f_sally_door_a"),
				(this_or_next|eq, ":effected_object", "spr_earth_sally_gate_left"),
				(this_or_next|eq, ":effected_object", "spr_earth_sally_gate_right"),
				(this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_left"),
				(this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_right"),
				(eq, ":effected_object", "spr_castle_f_door_a"),
				
				(try_begin),
					(eq, ":item_situation", 0),
					(str_store_string, s0, "str_open_door"),
				(else_try),
					(str_store_string, s0, "str_close_door"),
				(try_end),
			(else_try), #raising/dropping ladder
				(try_begin),
					(eq, ":item_situation", 0),
					(str_store_string, s0, "str_raise_ladder"),
				(else_try),
					(str_store_string, s0, "str_drop_ladder"),
				(try_end),
			(try_end),
	])


#script_game_get_date_text:
	# This script is called from the game engine when the date needs to be displayed.
	# INPUT: arg1 = number of days passed since the beginning of the game
	# OUTPUT: result string = date
game_get_date_text =	(
		"game_get_date_text",
		[
			(store_script_param_2, ":num_hours"),
			(store_div, ":num_days", ":num_hours", 24),
			(store_add, ":cur_day", ":num_days", 23),
			(assign, ":cur_month", 3),
			(assign, ":cur_year", 1257),
			(assign, ":try_range", 99999),
			(try_for_range, ":unused", 0, ":try_range"),
				(try_begin),
					(this_or_next|eq, ":cur_month", 1),
					(this_or_next|eq, ":cur_month", 3),
					(this_or_next|eq, ":cur_month", 5),
					(this_or_next|eq, ":cur_month", 7),
					(this_or_next|eq, ":cur_month", 8),
					(this_or_next|eq, ":cur_month", 10),
					(eq, ":cur_month", 12),
					(assign, ":month_day_limit", 31),
				(else_try),
					(this_or_next|eq, ":cur_month", 4),
					(this_or_next|eq, ":cur_month", 6),
					(this_or_next|eq, ":cur_month", 9),
					(eq, ":cur_month", 11),
					(assign, ":month_day_limit", 30),
				(else_try),
					(try_begin),
						(store_div, ":cur_year_div_4", ":cur_year", 4),
						(val_mul, ":cur_year_div_4", 4),
						(eq, ":cur_year_div_4", ":cur_year"),
						(assign, ":month_day_limit", 29),
					(else_try),
						(assign, ":month_day_limit", 28),
					(try_end),
				(try_end),
				(try_begin),
					(gt, ":cur_day", ":month_day_limit"),
					(val_sub, ":cur_day", ":month_day_limit"),
					(val_add, ":cur_month", 1),
					(try_begin),
						(gt, ":cur_month", 12),
						(val_sub, ":cur_month", 12),
						(val_add, ":cur_year", 1),
					(try_end),
				(else_try),
					(assign, ":try_range", 0),
				(try_end),
			(try_end),
			(assign, reg1, ":cur_day"),
			(assign, reg2, ":cur_year"),
			(try_begin),
				(eq, ":cur_month", 1),
				(str_store_string, s1, "str_january_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 2),
				(str_store_string, s1, "str_february_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 3),
				(str_store_string, s1, "str_march_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 4),
				(str_store_string, s1, "str_april_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 5),
				(str_store_string, s1, "str_may_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 6),
				(str_store_string, s1, "str_june_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 7),
				(str_store_string, s1, "str_july_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 8),
				(str_store_string, s1, "str_august_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 9),
				(str_store_string, s1, "str_september_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 10),
				(str_store_string, s1, "str_october_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 11),
				(str_store_string, s1, "str_november_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 12),
				(str_store_string, s1, "str_december_reg1_reg2"),
			(try_end),
			(set_result_string, s1),
	])

#script_game_get_party_companion_limit:
	# This script is called from the game engine when the companion limit is needed for a party.
	# NOTE: modified by tom "#tom party size here!"
	# INPUT: arg1 = none
	# OUTPUT: reg0 = companion_limit
game_get_party_companion_limit =	("game_get_party_companion_limit",
		[
			(assign, ":troop_no", "trp_player"),
			
			#rafi -increase limit (assign, ":limit", 30),
			(assign, ":limit", 100), #tom was 70
			
			(store_skill_level, ":skill", "skl_leadership", ":troop_no"),
			(store_attribute_level, ":charisma", ":troop_no", ca_charisma),
			(val_mul, ":skill", 5), #tom was 5
			(val_add, ":limit", ":skill"),
			(val_add, ":limit", ":charisma"),
			
			(troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
			(store_div, ":renown_bonus", ":troop_renown", 25),
			(val_add, ":limit", ":renown_bonus"),
			
			(assign, reg0, ":limit"),
			(set_trigger_result, reg0),
	])
	
#script_game_get_money_text:
# This script is called from the game engine when an amount of money needs to be displayed.
# INPUT: arg1 = amount in units
# OUTPUT: result string s1 = money in text
game_get_money_text =	(
	"game_get_money_text",
		[
			(store_script_param_1, ":amount"),
			(try_begin),
				(eq, ":amount", 1),
				(str_store_string, s1, "str_1_denar"),
			(else_try),
				(assign, reg1, ":amount"),
				(str_store_string, s1, "str_reg1_denars"),
			(try_end),
			(set_result_string, s1),
	])