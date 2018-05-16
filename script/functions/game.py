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

		#script_game_get_troop_wage
		# WARNING : HEAVILY Modified by 1257AD devs
		# INPUT: troop_id, party_id
		# OUTPUT: wage set trigger register reg0
game_get_troop_wage = (
	"game_get_troop_wage",
			[
			(store_script_param, ":troop_id", 1),
			(store_script_param_2, ":party_id"), #party id
			
			#TOM
			(assign, ":value", 0), #the thing to compare to others
			# (assign, ":value2", 0), #the thing to compare to others
			# (assign, ":meele", 0),
			# (assign, ":range", 0),
			# (assign, ":ammo", 0),
			(assign, ":head", 0),
			(assign, ":body", 0),
			(assign, ":foot", 0),
			# (assign, ":hand", 0),
			# (assign, ":shield", 0),
			(assign, ":mount", 1), #NO NEED?
			(try_begin),
				(neg|troop_is_hero, ":troop_id"),
				(troop_get_inventory_capacity,":cap",":troop_id"),
				(try_for_range, ":inventory", 0, ":cap"), #lets get troop inventory capacity
				(troop_get_inventory_slot,":item",":troop_id",":inventory"), #lets get it's item
				(gt, ":item", 0), #it's not nothing
				(item_get_type, ":item_type", ":item"), #lets get it type
				(try_begin), #meele weapon
					# (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
					# (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
					# (eq, ":item_type", itp_type_polearm),
					# (item_get_slot, ":value", ":item", slot_item_thrust_damage),
					# (item_get_slot, ":value2", ":item", slot_item_swing_damage),
					# (val_add, ":value", ":value2"),
					# (gt, ":value", ":meele"),
					# (assign, ":meele", ":value"),
					# (else_try), #range
					# (this_or_next|eq, ":item_type", itp_type_bow),
					# (this_or_next|eq, ":item_type", itp_type_crossbow),
					# (eq, ":item_type", itp_type_thrown),
					# (item_get_slot, ":value", ":item", slot_item_thrust_damage),
					# (item_get_slot, ":value2", ":item", slot_item_swing_damage),
					# (val_add, ":value", ":value2"),
					# (gt, ":value", ":meele"),
					# (assign, ":meele", ":value"),
					# (else_try), #ammo
					# (this_or_next|eq, ":item_type", itp_type_arrows),
					# (eq, ":item_type", itp_type_bolts),
					# (item_get_slot, ":value", ":item", slot_item_thrust_damage),
					# (item_get_slot, ":value2", ":item", slot_item_swing_damage),
					# (val_add, ":value", ":value2"),
					# (gt, ":value", ":ammo"),
					# (assign, ":ammo", ":value"),
					#(else_try), #shield
					#(eq, ":item_type", itp_type_shield),
					#(item_get_slot, ":value", ":item", slot_item_body_armor), #no idea which
					# (item_get_slot, ":value2", ":item", slot_item_head_armor), #should give the proper value
					#(val_add, ":value", ":value2"),
					#(item_get_slot, ":value2", ":item", slot_item_leg_armor), #so lets check them all
					#(val_add, ":value", ":value2"),
					#(gt, ":value", ":shield"),
					#(assign, ":shield", ":value"),
					#(else_try), #head armor
					(eq, ":item_type", itp_type_head_armor),
					(item_get_slot, ":value", ":item", slot_item_head_armor),
					(gt, ":value", ":head"),
					(assign, ":head", ":value"),
				(else_try), #body armor
					(eq, ":item_type", itp_type_body_armor),
					(item_get_slot, ":value", ":item", slot_item_body_armor),
					(gt, ":value", ":body"),
					(assign, ":body", ":value"),
				(else_try), #foot armor
					(eq, ":item_type", itp_type_foot_armor),
					(item_get_slot, ":value", ":item", slot_item_leg_armor),
					(gt, ":value", ":foot"),
					(assign, ":foot", ":value"),
					# (else_try), #hand armor
					# (eq, ":item_type", itp_type_hand_armor),
					# (item_get_slot, ":value", ":item", slot_item_body_armor), #presume it's this?
					# (gt, ":value", ":hand"),
					# (assign, ":hand", ":value"),
				(else_try),
					(eq, ":item_type", itp_type_horse),
					(assign, ":mount", 2),
				(try_end),
				(try_end),
				#(store_add, ":offense", ":meele", ":range"),
				#(val_add, ":offense", ":ammo"),
				#(store_add, ":defense", ":head", ":body"),
				#(val_add, ":defense", ":shield"),
				#(val_add, ":defense", ":foot"),
				#(val_add, ":defense", ":hand"),
				#(assign, ":offense", 0),
				#(val_mul, ":defense", ":mount"),
				#(store_add, ":wage", ":offense", ":defense"),
				(store_add, ":wage", ":head", ":body"),
				(val_div, ":wage", 4),
				#(val_mul, ":wage", 2),
				
				
				(try_begin),
				(store_character_level,":troop_lvl",":troop_id"),
				(neg|ge, ":troop_lvl", 6),
				#(val_mul, ":wage", 3),
				(val_div, ":wage", 3),
				(val_mul, ":wage", 2),
				(else_try),
				(val_sub, ":wage", 3),
				(try_end),
				
				(try_begin),
				#(else_try),
				(store_character_level,":troop_lvl",":troop_id"),
				(ge, ":troop_lvl", 19),
				(val_add, ":wage", 3),
				(val_mul, ":wage", 2),
				
				(try_begin),
					(ge, ":troop_lvl", 30),
					(val_add, ":wage", 210), #60
				(else_try),
					(ge, ":troop_lvl", 27),
					(val_add, ":wage", 110), #30
				(else_try),
					(ge, ":troop_lvl", 24),
					(val_add, ":wage", 10),
					#(else_try),
					
					#(val_div, ":wage", 2),
				(try_end),
				(try_end),
				(try_begin),
				(eq, ":mount", 2),
				(val_mul, ":wage", 5), #5
				(val_div, ":wage", 4), #4
				(try_end),
			(try_end),
			#(val_max, ":wage", 8),
			#TOM
			
			#TOM - this was original
			# (try_begin),
			# (neg|troop_is_hero, ":troop_id"),
			# (troop_get_slot, ":offense", ":troop_id", kt_slot_troop_o_val),
			# (troop_get_slot, ":defense", ":troop_id", kt_slot_troop_d_val),
			# (store_add, ":wage", ":offense", ":defense"),
			# (try_end),
			#TOM
			
			(try_begin),
				(is_between, ":troop_id", companions_begin, companions_end),
				(store_character_level, ":level", ":troop_id"),
				(store_mul, ":offense", ":level", 3),
				(val_add, ":offense", 50),
				(store_mul, ":defense", ":level", 2),
				(val_add, ":defense", 20),
				(store_add, ":wage", ":offense", ":defense"),
				
				(val_div, ":wage", 2),
				
				(val_max, ":wage", 1),
				(val_sub, ":wage", 31),
				(val_max, ":wage", 1),
				(store_mul, reg0, ":wage", ":wage"),
				
				(assign, ":wage", reg0),
				
				(val_div, ":wage", 200),
				
				(try_begin),
				(lt, ":wage", 80),
				(val_mul, ":wage", 3),
				(try_end),
				
				(val_mul, ":wage", 2),
				(val_div, ":wage", 3),
				
			(try_end),
			
			(party_get_template_id, ":template", ":party_id"),
			#tom
			##this one for lance system - player only
			#troop upkeep whitout a fief is super low
			(try_begin),
				(eq, "$use_feudal_lance", 1),
				(this_or_next|gt, "$g_player_crusading", 0),  
				(eq, "$use_feudal_lance", 1), #intented double check
				(eq, ":template", "p_main_party"),
				(assign, ":reduce", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(assign, ":reduce", 1),
				(assign, ":center_no", -1),
				(try_end),
				(eq, ":reduce", 0),
				(val_mul, ":wage", 2),
				(val_div, ":wage", 3),
				
				(val_max, ":wage", 3),
			(else_try), #in times of peace, as a lord - increase upkeep.
				(eq, "$use_feudal_lance", 1),
				(this_or_next|gt, "$g_player_crusading", 0),  
				(eq, "$use_feudal_lance", 1), #intented double check
				(eq, ":template", "p_main_party"),
				(assign, ":lord", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(assign, ":lord", 1),
				(store_faction_of_party, ":faction", ":center_no"),
				(assign, ":center_no", -1),
				(try_end),
				(eq, ":lord", 1),
				(call_script, "script_check_if_faction_is_at_war", ":faction"),
				(eq, reg0, 0), #at peace
				(val_mul, ":wage", 3),
				(val_div, ":wage", 2),
			(try_end),
			#tom end
			#tom
			#(game_get_reduce_campaign_ai, ":reduce_campaign_ai"), mod options now
			 
				
			(try_begin), #player only
				(this_or_next|eq, ":party_id", "p_main_party"),
				(eq, ":template", "pt_merc_party"),
				(try_begin),
				(eq, "$tom_difficulty_wages", 0), #hard (1x or 2x reinforcing)
				(val_mul, ":wage", 3),
				(val_div, ":wage", 2),
				(else_try),
				(eq, "$tom_difficulty_wages", 1), #moderate (1x reinforcing)
				(else_try),
				(eq, "$tom_difficulty_wages", 2), #easy (none or 1x reinforcing)
				(val_div, ":wage", 2),
				(try_end),
				(val_max, ":wage", 3),
			(try_end),
			
			
			
			# (val_div, ":wage", 2),
			
			# (val_max, ":wage", 1),
			# (val_sub, ":wage", 31),
			# (val_max, ":wage", 1),
			# (store_mul, reg0, ":wage", ":wage"),
			
			# (assign, ":wage", reg0),
			
			# (val_div, ":wage", 200),
			
			# (try_begin),
			# (lt, ":wage", 80),
			# (val_mul, ":wage", 3),
			# (try_end),
			
			# (val_mul, ":wage", 2),
			# (val_div, ":wage", 3),
			
			(try_begin),
				(neq, ":troop_id", "trp_player"),
				(neq, ":troop_id", "trp_kidnapped_girl"),
				(neg|is_between, ":troop_id", pretenders_begin, pretenders_end),
				(val_max, ":wage", 1),
			(try_end),
			
			(assign, ":troop_leadership", -1),
			(try_begin),
				(ge, ":party_id", 0),
				(try_begin),
				(this_or_next | party_slot_eq, ":party_id", slot_party_type, spt_town),
				(party_slot_eq, ":party_id", slot_party_type, spt_castle),
				(party_get_slot, ":troop_leadership", ":party_id", slot_town_lord),
				(else_try),
				(eq, ":party_id", "p_main_party"),
				(assign, ":troop_leadership", "trp_player"),
				(else_try),
				(party_stack_get_troop_id, ":troop_leadership", ":party_id", 0),
				(try_end),
			(try_end),
			
			(try_begin),
				(ge, ":troop_leadership", 0),
				(store_skill_level, ":leadership_level", "skl_leadership", ":troop_leadership"),
				(store_mul, ":leadership_bonus", 5, ":leadership_level"),
				(store_sub, ":leadership_factor", 100, ":leadership_bonus"),
				(val_mul, ":wage", ":leadership_factor"),  #wage = wage * (100 - 5*leadership)/100
				(val_div, ":wage", 100),
			(try_end),
			
			(assign, reg0, ":wage"),
			(set_trigger_result, reg0),
			])