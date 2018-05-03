from header import *


# script_game_get_upgrade_xp
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed exp for upgrade
game_get_upgrade_xp  = ( 
	"game_get_upgrade_xp",
		[
			(store_script_param_1, ":troop_id"),
			
			(assign, ":needed_upgrade_xp", 0),
			#formula : int needed_upgrade_xp = 2 * (30 + 0.006f * level_boundaries[troops[troop_id].level + 3]);
			(store_character_level, ":troop_level", ":troop_id"),
			(store_add, ":needed_upgrade_xp", ":troop_level", 3),
			(get_level_boundary, reg0, ":needed_upgrade_xp"),
			(val_mul, reg0, 6),
			(val_div, reg0, 1000),
			(val_add, reg0, 30),
			
			(try_begin),
				(ge, ":troop_id", bandits_begin),
				(lt, ":troop_id", bandits_end),
				(val_mul, reg0, 2),
			(try_end),
			
			(set_trigger_result, reg0),
	])

# script_game_get_troop_wage
	# This script is called from the game engine for calculating troop wages.
	# Input:
	# param1: troop_id, param2: party-id
	# Output: reg0: weekly wage
	
orig_game_get_troop_wage =	(
	"orig_game_get_troop_wage",
		[
			(store_script_param_1, ":troop_id"),
			(store_script_param_2, ":party_id"), #party id
			
			(assign, ":wage", 0),
			
			(troop_get_slot, ":o_val", ":troop_id", kt_slot_troop_o_val),
			(troop_get_slot, ":d_val", ":troop_id", kt_slot_troop_d_val),
			(troop_get_slot, ":h_val", ":troop_id", kt_slot_troop_h_val),
			(troop_get_slot, ":tr_type", ":troop_id", kt_slot_troop_type),
			
			(try_begin),
				(neg|troop_is_hero, ":troop_id"),
				(troop_get_slot, ":o_val", ":troop_id", kt_slot_troop_o_val),
				(troop_get_slot, ":d_val", ":troop_id", kt_slot_troop_d_val),
				(troop_get_slot, ":h_val", ":troop_id", kt_slot_troop_h_val),
				(troop_get_slot, ":tr_type", ":troop_id", kt_slot_troop_type),
			(try_end),
			
			(try_begin),
				(neg|troop_is_hero, ":troop_id"),
				(eq, ":tr_type", kt_troop_type_footsoldier),
				(store_character_level, ":level", ":troop_id"),
				(le, ":level", 12),
				(val_div, ":o_val", 9),
				(val_div, ":d_val", 9),
			(try_end),
			
			(try_begin),
				# mounted archers only get 50% more defense
				(eq, ":tr_type", kt_troop_type_mtdarcher),
				(val_mul, ":d_val", 3),
				(val_div, ":d_val", 2),
				(val_mul, ":o_val", 3),
				(val_div, ":o_val", 2),
				(val_add, ":o_val", ":h_val"), # rafi
			(else_try),
				# cavalry get 50% more attack and defense and add h_val to o_val
				(eq, ":tr_type", kt_troop_type_cavalry),
				(val_mul, ":o_val", 4),
				(val_div, ":o_val", 2),
				(val_add, ":o_val", ":h_val"),
				(val_mul, ":d_val", 3),
				(val_div, ":d_val", 2),
			(try_end),
			(val_add, ":o_val", ":h_val"),
			
			(assign, ":wage", ":o_val"),
			(val_div, ":wage", 2),
			(val_max, ":wage", 1),
			
			(try_begin),
				(is_between, ":troop_id", companions_begin, companions_end),
				(store_character_level, ":level", ":troop_id"),
				(store_mul, ":o_val", ":level", 3),
				(val_add, ":o_val", 50),
				(store_mul, ":d_val", ":level", 2),
				(val_add, ":d_val", 20),
			(try_end),
			
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


# script_game_get_total_wage
	# This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
	# Input: none
	# Output: reg0: weekly wage
game_get_total_wage = (
	"game_get_total_wage",
	[
		# (call_script, "script_kt_party_calculate_strength", "p_main_party", 1, 0),
		# (display_message, "@party strength {reg0} defensive strength {reg1} troops {reg2}"),
		
		(assign, ":total_wage", 0),
		(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
		(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
			(party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
			(call_script, "script_game_get_troop_wage", ":stack_troop", 0),
			(val_mul, reg0, ":stack_size"),
			(val_add, ":total_wage", reg0),
		(try_end),
		(assign, reg0, ":total_wage"),
		(set_trigger_result, reg0),
	])

# script_game_get_join_cost
	# This script is called from the game engine for calculating troop join cost.
	# Input:
	# param1: troop_id,
	# Output: reg0: weekly wage
game_get_join_cost = (
		"game_get_join_cost",
		[
			(store_script_param_1, ":troop_id"),
			
			(assign,":join_cost", 0),
			(try_begin),
				(troop_is_hero, ":troop_id"),
			(else_try),
				(store_character_level, ":troop_level", ":troop_id"),
				(assign, ":join_cost", ":troop_level"),
				(val_add, ":join_cost", 5),
				(val_mul, ":join_cost", ":join_cost"),
				(val_add, ":join_cost", 40),
				(val_div, ":join_cost", 5),
				(try_begin), #mounted troops cost %100 more than the normal cost
					(troop_is_mounted, ":troop_id"),
					(val_mul, ":join_cost", 2),
				(try_end),
			(try_end),
		#tom - feudal system, if not a lord - reduce the price
		(try_begin),
		(eq, "$use_feudal_lance", 1),
		(this_or_next|gt, "$g_player_crusading", 0),  
		(eq, "$use_feudal_lance", 1), #intented double check
		(assign, ":reduce", 0),
		(try_for_range, ":center_no", centers_begin, centers_end),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			(assign, ":reduce", 1),
		(try_end),
		(eq, ":reduce", 0),
		(val_div, ":join_cost", 3),
		(try_end),
		#tom
			(assign, reg0, ":join_cost"),
			(set_trigger_result, reg0),
	])

# script_game_get_upgrade_cost
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed cost for upgrade
game_get_upgrade_cost =	(
	"game_get_upgrade_cost",
		[
			(store_script_param_1, ":troop_id"),
			
			(store_character_level, ":troop_level", ":troop_id"),
			
			(try_begin),
				(is_between, ":troop_level", 0, 6),
				(assign, reg0, 10),
			(else_try),
				(is_between, ":troop_level", 6, 11),
				(assign, reg0, 20),
			(else_try),
				(is_between, ":troop_level", 11, 16),
				(assign, reg0, 40),
			(else_try),
				(is_between, ":troop_level", 16, 21),
				(assign, reg0, 80),
			(else_try),
				(is_between, ":troop_level", 21, 26),
				(assign, reg0, 120),
			(else_try),
				(is_between, ":troop_level", 26, 31),
				(assign, reg0, 160),
			(else_try),
				(assign, reg0, 200),
			(try_end),
			
			(set_trigger_result, reg0),
	])

# script_game_get_prisoner_price
	# This script is called from the game engine for calculating prisoner price
	# Input:
	# param1: troop_id,
	# Output: reg0
game_get_prisoner_price =	(
	"game_get_prisoner_price",
		[
			(store_script_param_1, ":troop_id"),
			
			(try_begin),
				(is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
				(store_character_level, ":troop_level", ":troop_id"),
				(assign, ":ransom_amount", ":troop_level"),
				(val_add, ":ransom_amount", 10),
				(val_mul, ":ransom_amount", ":ransom_amount"),
				(val_div, ":ransom_amount", 6),
			(else_try),
				(assign, ":ransom_amount", 50),
			(try_end),
			
			(assign, reg0, ":ransom_amount"),
			
			(set_trigger_result, reg0),
	])

# script_game_check_prisoner_can_be_sold
	# This script is called from the game engine for checking if a given troop can be sold.
	# Input:
	# param1: troop_id,
	# Output: reg0: 1= can be sold; 0= cannot be sold.
	
game_check_prisoner_can_be_sold =	(
		"game_check_prisoner_can_be_sold",
		[
			(store_script_param_1, ":troop_id"),
			(assign, reg0, 0),
			(try_begin),
				(neg|troop_is_hero, ":troop_id"),
				(assign, reg0, 1),
			(try_end),
			(set_trigger_result, reg0),
	])

# script_game_get_morale_of_troops_from_faction
	# This script is called from the game engine
	# Input:
	# param1: faction_no,
	# Output: reg0: extra morale x 100
	
game_get_morale_of_troops_from_faction = (
		"game_get_morale_of_troops_from_faction",
		[
			(store_script_param_1, ":troop_no"),
			
			(store_troop_faction, ":faction_no", ":troop_no"),
			
			(try_begin),
				(ge, ":faction_no", npc_kingdoms_begin),
				(lt, ":faction_no", npc_kingdoms_end),
				
				(faction_get_slot, reg0, ":faction_no",  slot_faction_morale_of_player_troops),
				
				#(assign, reg1, ":faction_no"),
				#(assign, reg2, ":troop_no"),
				#(assign, reg3, reg0),
				#(display_message, "@extra morale for troop {reg2} of faction {reg1} is {reg3}"),
			(else_try),
				(assign, reg0, 0),
			(try_end),
			
			(val_div, reg0, 100),
			
			(party_get_morale, reg1, "p_main_party"),
			
			(val_add, reg0, reg1),
			
			(set_trigger_result, reg0),
	])

#script_game_get_skill_modifier_for_troop
		# This script is called from the game engine when a skill's modifiers are needed
		# INPUT: arg1 = troop_no, arg2 = skill_no
		# OUTPUT: trigger_result = modifier_value
game_get_skill_modifier_for_troop =  (
	"game_get_skill_modifier_for_troop",
			[(store_script_param, ":troop_no", 1),
				(store_script_param, ":skill_no", 2),
				(assign, ":modifier_value", 0),
				(try_begin),
					(eq, ":skill_no", "skl_wound_treatment"),
					(call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_wound_treatment_reference"),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(else_try),
					(eq, ":skill_no", "skl_trainer"),
					(call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_training_reference"),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(else_try),
					(eq, ":skill_no", "skl_surgery"),
					(call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_surgery_reference"),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(try_end),
				(set_trigger_result, ":modifier_value"),
		])

		# script_npc_get_troop_wage
		# This script is called from module system to calculate troop wages for npc parties.
		# Input:
		# param1: troop_id
		# Output: reg0: weekly wage
		
npc_get_troop_wage =  (
	"npc_get_troop_wage",
			[
				(store_script_param_1, ":troop_id"),
				(assign,":wage", 0),
				(try_begin),
					(troop_is_hero, ":troop_id"),
				(else_try),
					(store_character_level, ":wage", ":troop_id"),
					(val_mul, ":wage", ":wage"),
					(val_add, ":wage", 50),
					(val_div, ":wage", 30),
					(troop_is_mounted, ":troop_id"),
					(val_mul, ":wage", 5),
					(val_div, ":wage", 4),
				(try_end),
				(assign, reg0, ":wage"),
		])


#script_print_troop_owned_centers_in_numbers_to_s0
		# INPUT:
		# param1: troop_no
		#OUTPUT:
		# string register 0.
print_troop_owned_centers_in_numbers_to_s0 = (
	"print_troop_owned_centers_in_numbers_to_s0",
			[
				(store_script_param_1, ":troop_no"),
				(str_store_string, s0, "@nothing"),
				(assign, ":owned_towns", 0),
				(assign, ":owned_castles", 0),
				(assign, ":owned_villages", 0),
				(try_for_range_backwards, ":cur_center", centers_begin, centers_end),
					(party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
					(try_begin),
						(party_slot_eq, ":cur_center", slot_party_type, spt_town),
						(val_add, ":owned_towns", 1),
					(else_try),
						(party_slot_eq, ":cur_center", slot_party_type, spt_castle),
						(val_add, ":owned_castles", 1),
					(else_try),
						(val_add, ":owned_villages", 1),
					(try_end),
				(try_end),
				(assign, ":num_types", 0),
				(try_begin),
					(gt, ":owned_villages", 0),
					(assign, reg0, ":owned_villages"),
					(store_sub, reg1, reg0, 1),
					(str_store_string, s0, "@{reg0} village{reg1?s:}"),
					(val_add, ":num_types", 1),
				(try_end),
				(try_begin),
					(gt, ":owned_castles", 0),
					(assign, reg0, ":owned_castles"),
					(store_sub, reg1, reg0, 1),
					(try_begin),
						(eq, ":num_types", 0),
						(str_store_string, s0, "@{reg0} castle{reg1?s:}"),
					(else_try),
						(str_store_string, s0, "@{reg0} castle{reg1?s:} and {s0}"),
					(try_end),
					(val_add, ":num_types", 1),
				(try_end),
				(try_begin),
					(gt, ":owned_towns", 0),
					(assign, reg0, ":owned_towns"),
					(store_sub, reg1, reg0, 1),
					(try_begin),
						(eq, ":num_types", 0),
						(str_store_string, s0, "@{reg0} town{reg1?s:}"),
					(else_try),
						(eq, ":num_types", 1),
						(str_store_string, s0, "@{reg0} town{reg1?s:} and {s0}"),
					(else_try),
						(str_store_string, s0, "@{reg0} town{reg1?s:}, {s0}"),
					(try_end),
				(try_end),
				(store_add, reg0, ":owned_villages", ":owned_castles"),
				(val_add, reg0, ":owned_towns"),
		])

# script_cf_troop_get_random_enemy_troop_with_occupation
		# Input: arg1 = troop_no,
		# Output: reg0 = enemy_troop_no (Can fail)
cf_troop_get_random_enemy_troop_with_occupation = (
	"cf_troop_get_random_enemy_troop_with_occupation",
			[
				(store_script_param_1, ":troop_no"),
				(store_script_param_2, ":occupation"),
				
				(assign, ":result", -1),
				(assign, ":count_enemies", 0),
				(try_for_range, ":enemy_troop_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, ":occupation"),
					(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":enemy_troop_no"),
					(lt, reg0, -10),
					(val_add, ":count_enemies", 1),
				(try_end),
				
				(gt, ":count_enemies", 0),
				(store_random_in_range,":random_enemy",0,":count_enemies"),
				
				(assign, ":count_enemies", 0),
				(try_for_range, ":enemy_troop_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, ":occupation"),
					(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":enemy_troop_no"),
					(lt, reg0, -10),
					(val_add, ":count_enemies", 1),
					(eq, ":random_enemy", ":count_enemies"),
					(assign, ":result", ":enemy_troop_no"),
				(try_end),
				
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		])
		
# script_get_number_of_hero_centers
		# Input: arg1 = troop_no
		# Output: reg0 = number of centers that are ruled by the hero
get_number_of_hero_centers	= (
	"get_number_of_hero_centers",
			[
				(store_script_param_1, ":troop_no"),
				(assign, ":result", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(val_add, ":result", 1),
				(try_end),
				(assign, reg0, ":result"),
		])
		
		# script_give_center_to_lord
		# WARNING: heavily modified by 1257AD devs
		# includes diplomacy!
		# Input: arg1 = center_no, arg2 = lord_troop, arg3 = add_garrison_to_center
give_center_to_lord	= (
	"give_center_to_lord",
			[
				(store_script_param, ":center_no", 1),
				(store_script_param, ":lord_troop_id", 2), #-1 only in the case of a player deferring ownership of a center
				(store_script_param, ":add_garrison", 3),
				##diplomacy begin
				(party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
				(try_begin),
					(party_slot_eq, ":center_no", slot_village_infested_by_bandits, "trp_peasant_woman"),
					(party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
				(try_end),
				##diplomacy end
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(ge, ":lord_troop_id", 0),
					(str_store_party_name, s4, ":center_no"),
					(str_store_troop_name, s5, ":lord_troop_id"),
					(display_message, "@{!}DEBUG -- {s4} awarded to {s5}"),
				(try_end),
				
				(try_begin),
					(eq, ":lord_troop_id", "trp_player"),
					(unlock_achievement, ACHIEVEMENT_ROYALITY_PAYMENT),
					
					(assign, ":number_of_fiefs_player_have", 1),
					(try_for_range, ":cur_center", centers_begin, centers_end),
						(neq, ":cur_center", ":center_no"),
						(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
						(val_add, ":number_of_fiefs_player_have", 1),
					(try_end),
					
					(ge, ":number_of_fiefs_player_have", 5),
					(unlock_achievement, ACHIEVEMENT_MEDIEVAL_EMLAK),
				(try_end),
				
				(party_get_slot, ":old_lord_troop_id", ":center_no", slot_town_lord),
				
				(try_begin), #This script is ONLY called with lord_troop_id = -1 when it is the player faction
					(eq, ":lord_troop_id", -1),
					(assign, ":lord_troop_faction", "fac_player_supporters_faction"),
					(party_set_banner_icon, ":center_no", 0),#Removing banner
					
				(else_try),
					(eq, ":lord_troop_id", "trp_player"),
					(assign, ":lord_troop_faction", "$players_kingdom"), #was changed on Apr 27 from fac_plyr_sup_fac
					
				(else_try),
					(store_troop_faction, ":lord_troop_faction", ":lord_troop_id"),
				(try_end),
				(faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
				
				(try_begin),
					(eq, ":faction_leader", ":old_lord_troop_id"),
					(call_script, "script_add_log_entry", logent_liege_grants_fief_to_vassal, ":faction_leader", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
					(troop_set_slot, ":lord_troop_id", slot_troop_promised_fief, 0),
				(try_end),
				
				(try_begin),
					(eq, ":lord_troop_id", -1), #Lord troop ID -1 is only used when a player is deferring assignment of a fief
					(party_set_faction, ":center_no", "$players_kingdom"),
				(else_try),
					(eq, ":lord_troop_id", "trp_player"),
					(gt, "$players_kingdom", 0),
					(party_set_faction, ":center_no", "$players_kingdom"),
				(else_try),
					(eq, ":lord_troop_id", "trp_player"),
					(neg|is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
					(party_set_faction, ":center_no", "fac_player_supporters_faction"),
				(else_try),
					(party_set_faction, ":center_no", ":lord_troop_faction"),
				(try_end),
				(party_set_slot, ":center_no", slot_town_lord, ":lord_troop_id"),
				
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":farmer_party_no", ":center_no", slot_village_farmer_party),
					(gt, ":farmer_party_no", 0),
					(party_is_active, ":farmer_party_no"),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(party_set_faction, ":farmer_party_no", ":center_faction"),
				(try_end),
				
				(try_begin),
					(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(gt, ":lord_troop_id", -1),
					
					#normal_banner_begin
					(troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
					(gt, ":cur_banner", 0),
					(val_sub, ":cur_banner", banner_scene_props_begin),
					(val_add, ":cur_banner", banner_map_icons_begin),
					(party_set_banner_icon, ":center_no", ":cur_banner"),
					# custom_banner_begin
					#        (troop_get_slot, ":flag_icon", ":lord_troop_id", slot_troop_custom_banner_map_flag_type),
					#        (ge, ":flag_icon", 0),
					#        (val_add, ":flag_icon", custom_banner_map_icons_begin),
					#        (party_set_banner_icon, ":center_no", ":flag_icon"),
				(try_end),
				
				#    (try_begin),
				#		(eq, 1, 0),
				#       (eq, ":lord_troop_id", "trp_player"),
				#       (neq, ":old_lord_troop_id", "trp_player"),
				#       (party_get_slot, ":center_relation", ":center_no", slot_center_player_relation),
				#       (is_between, ":center_relation", -4, 5),
				#       (call_script, "script_change_player_relation_with_center", ":center_no", 5),
				#       (gt, ":old_lord_troop_id", 0),
				#       (call_script, "script_change_player_relation_with_troop", ":old_lord_troop_id", -25),
				#   (try_end),
				(try_begin),
					(gt, ":lord_troop_id", -1),
					(call_script, "script_update_troop_notes", ":lord_troop_id"),
				(try_end),
				
				(call_script, "script_update_center_notes", ":center_no"),
				
				(try_begin),
					(gt, ":lord_troop_faction", 0),
					(call_script, "script_update_faction_notes", ":lord_troop_faction"),
				(try_end),
				
				(try_begin),
					(ge, ":old_lord_troop_id", 0),
					(call_script, "script_update_troop_notes", ":old_lord_troop_id"),
					(store_troop_faction, ":old_lord_troop_faction", ":old_lord_troop_id"),
					(call_script, "script_update_faction_notes", ":old_lord_troop_faction"),
				(try_end),
				
				(try_begin),
					(eq, ":add_garrison", 1),
					(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(assign, ":garrison_strength", 3),
					(try_begin),
						(party_slot_eq, ":center_no", slot_party_type, spt_town),
						(assign, ":garrison_strength", 9),
					(try_end),
					(try_for_range, ":unused", 0, ":garrison_strength"),
						(call_script, "script_cf_reinforce_party", ":center_no"),
					(try_end),
					## ADD some XP initially
					(try_for_range, ":unused", 0, 7),
						(store_mul, ":xp_range_min", 150, ":garrison_strength"),
						(store_mul, ":xp_range_max", 200, ":garrison_strength"),
						
						(store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
						(party_upgrade_with_xp, ":center_no", ":xp", 0),
					(try_end),
				(try_end),
				
				(faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
				(store_current_hours, ":hours"),
				
				#the next block handles gratitude, objections and jealousies
				(try_begin),
					(gt, ":hours", 0),
					(gt, ":lord_troop_id", 0),
					
					(call_script, "script_troop_change_relation_with_troop", ":lord_troop_id", ":faction_leader", 10),
					(val_add, "$total_promotion_changes", 10),
					
					#smaller factions are more dramatically influenced by internal jealousies
					#Disabled as of NOV 2010
					#		(try_begin),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 4),
					#			(assign, ":faction_size_multiplier", 6),
					#		(else_try),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 8),
					#			(assign, ":faction_size_multiplier", 5),
					#		(else_try),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 16),
					#			(assign, ":faction_size_multiplier", 4),
					#		(else_try),
					#			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 32),
					#			(assign, ":faction_size_multiplier", 3),
					#		(else_try),
					#			(assign, ":faction_size_multiplier", 2),
					#		(try_end),
					
					#factional politics -- each lord in the faction adjusts his relation according to the relation with the lord receiving the faction
					(try_for_range, ":other_lord", active_npcs_begin, active_npcs_end),
						(troop_slot_eq, ":other_lord", slot_troop_occupation, slto_kingdom_hero),
						(neq, ":other_lord", ":lord_troop_id"),
						
						(store_troop_faction, ":other_troop_faction", ":other_lord"),
						(eq, ":lord_troop_faction", ":other_troop_faction"),
						
						(neq, ":other_lord", ":faction_leader"),
						
						(call_script, "script_troop_get_relation_with_troop", ":other_lord", ":lord_troop_id"),
						(assign, ":relation_with_troop", reg0),
						#relation reduction = relation/10 minus 2. So,0 = -2, 8 = -1, 16+ = no change or bonus, 24+ gain one point
						(store_div, ":relation_with_liege_change", ":relation_with_troop", 8), #changed from 16
						(val_sub, ":relation_with_liege_change", 2),
						
						(val_clamp, ":relation_with_liege_change", -5, 3),
						
						(try_begin),
							#upstanding and goodnatured lords will not lose relation unless they actively dislike the other lord
							(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_upstanding),
							(troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_goodnatured),
							(ge, ":relation_with_troop", 0),
							(val_max, ":relation_with_liege_change", 0),
						(else_try),
							#penalty is increased for lords who have the more unpleasant reputation types
							(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_selfrighteous),
							(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_debauched),
							(troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_quarrelsome),
							(lt, ":relation_with_liege_change", 0),
							(val_mul, ":relation_with_liege_change", 3),
							(val_div, ":relation_with_liege_change", 2),
						(try_end),
						
						
						(neq, ":relation_with_liege_change", 0),
						#removed Nov 2010
						#		  	(val_mul, ":relation_reduction", ":faction_size_multiplier"),
						#		  	(val_div, ":relation_reduction", 2),
						#removed Nov 2010
						
						(try_begin),
							(troop_slot_eq, ":other_lord", slot_troop_stance_on_faction_issue, ":lord_troop_id"),
							(val_add, ":relation_with_liege_change", 1),
							(val_max, ":relation_with_liege_change", 1),
						(try_end),
						
						(call_script, "script_troop_change_relation_with_troop", ":other_lord", ":faction_leader", ":relation_with_liege_change"),
						(val_add, "$total_promotion_changes", ":relation_with_liege_change"),
						
						(try_begin),
							(this_or_next|le, ":relation_with_liege_change", -4), #Nov 2010 - changed from -8
							(this_or_next|troop_slot_eq, ":other_lord", slot_troop_promised_fief, 1), #1 is any fief
							(troop_slot_eq, ":other_lord", slot_troop_promised_fief, ":center_no"),
							(call_script, "script_add_log_entry", logent_troop_feels_cheated_by_troop_over_land, ":other_lord", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
						(try_end),
						
					(try_end),
				(try_end),
				
				#Villages from another faction will also be transferred along with a fortress
				(try_begin),
					(is_between, ":center_no", walled_centers_begin, walled_centers_end),
					(try_for_range, ":cur_village", villages_begin, villages_end),
						(party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),
						(store_faction_of_party, ":cur_village_faction", ":cur_village"),
						(neq, ":cur_village_faction", ":lord_troop_faction"),
						
						(call_script, "script_give_center_to_lord", ":cur_village", ":lord_troop_id", 0),
					(try_end),
				(try_end),
		])

		# script_get_troop_attached_party
		# Input: arg1 = troop_no
		# Output: reg0 = party_no (-1 if troop's party is not attached to a party)
get_troop_attached_party	= (
	"get_troop_attached_party",
			[
				(store_script_param_1, ":troop_no"),
				
				(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
				(assign, ":attached_party_no", -1),
				(try_begin),
					(ge, ":party_no", 0),
					(party_get_attached_to, ":attached_party_no", ":party_no"),
				(try_end),
				(assign, reg0, ":attached_party_no"),
		])
		

		# script_troop_get_player_relation
		# Input: arg1 = troop_no
		# Output: reg0 = effective relation (modified by troop reputation, honor, etc.)
troop_get_player_relation = (
	"troop_get_player_relation",
			[
				(store_script_param_1, ":troop_no"),
				(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
				(troop_get_slot, ":effective_relation", ":troop_no", slot_troop_player_relation),
				(assign, ":honor_bonus", 0),
				(try_begin),
					(eq,  ":reputation", lrep_quarrelsome),
					(val_add, ":effective_relation", -3),
				(try_end),
				(try_begin),
					(ge, "$player_honor", 0),
					(try_begin),
						(this_or_next|eq,  ":reputation", lrep_upstanding),
						(             eq,  ":reputation", lrep_goodnatured),
						(store_div, ":honor_bonus", "$player_honor", 3),
					(try_end),
				(try_end),
				(try_begin),
					(lt, "$player_honor", 0),
					(try_begin),
						(this_or_next|eq,  ":reputation", lrep_upstanding),
						(             eq,  ":reputation", lrep_goodnatured),
						(store_div, ":honor_bonus", "$player_honor", 3),
					(else_try),
						(eq,  ":reputation", lrep_martial),
						(store_div, ":honor_bonus", "$player_honor", 5),
					(try_end),
				(try_end),
				(val_add, ":effective_relation", ":honor_bonus"),
				(val_clamp, ":effective_relation", -100, 101),
				(assign, reg0, ":effective_relation"),
		])


		
		# script_get_information_about_troops_position
		# Input: arg1 = troop_no, arg2 = time (0 if present tense, 1 if past tense)
		# Output: s1 = String, reg0 = knows-or-not
get_information_about_troops_position = (
	"get_information_about_troops_position",
			[
				(store_script_param_1, ":troop_no"),
				(store_script_param_2, reg3),
				(troop_get_type, reg4, ":troop_no"),
				(str_store_troop_name, s2, ":troop_no"),
				
				(assign, ":found", 0),
				(troop_get_slot, ":center_no", ":troop_no", slot_troop_cur_center),
				(try_begin),
					(gt, ":center_no", 0),
					(is_between, ":center_no", centers_begin, centers_end),
					(str_store_party_name_link, s3, ":center_no"),
					(str_store_string, s1, "@{s2} {reg3?was:is currently} at {s3}."),
					(assign, ":found", 1),
				(else_try),
					(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
					(gt, ":party_no", 0),
					(call_script, "script_get_troop_attached_party", ":troop_no"),
					(assign, ":center_no", reg0),
					(try_begin),
						(is_between, ":center_no", centers_begin, centers_end),
						(str_store_party_name_link, s3, ":center_no"),
						(str_store_string, s1, "@{s2} {reg3?was:is currently} at {s3}."),
						(assign, ":found", 1),
					(else_try),
						(get_party_ai_behavior, ":ai_behavior", ":party_no"),
						(eq, ":ai_behavior", ai_bhvr_travel_to_party),
						(get_party_ai_object, ":ai_object", ":party_no"),
						(is_between, ":ai_object", centers_begin, centers_end),
						(call_script, "script_get_closest_center", ":party_no"),
						(str_store_party_name_link, s4, reg0),
						(str_store_party_name_link, s3, ":ai_object"),
						(str_store_string, s1, "@{s2} {reg3?was:is} travelling to {s3} and {reg4?she:he} {reg3?was:should be} close to {s4}{reg3?: at the moment}."),
						(assign, ":found", 1),
					(else_try),
						(call_script, "script_get_closest_center", ":party_no"),
						(str_store_party_name_link, s3, reg0),
						(str_store_string, s1, "@{s2} {reg3?was:is} in the field and {reg4?she:he} {reg3?was:should be} close to {s3}{reg3?: at the moment}."),
						(assign, ":found", 1),
					(try_end),
				(else_try),
					#(troop_slot_ge, ":troop_no", slot_troop_is_prisoner, 1),
					(troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
						(party_count_prisoners_of_type, ":num_prisoners", ":center_no", ":troop_no"),
						(gt, ":num_prisoners", 0),
						(assign, ":found", 1),
						(str_store_party_name_link, s3, ":center_no"),
						(str_store_string, s1, "@{s2} {reg3?was:is} being held captive at {s3}."),
					(try_end),
					(try_begin),
						(eq, ":found", 0),
						(str_store_string, s1, "@{s2} {reg3?was:has been} taken captive by {reg4?her:his} enemies."),
						(assign, ":found", 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":found", 0),
					(str_store_string, s1, "@{reg3?{s2}'s location was unknown:I don't know where {s2} is}."),
				(try_end),
				(assign, reg0, ":found"),
		])
		
		
		# script_search_troop_prisoner_of_party
		# Input: arg1 = troop_no
		# Output: reg0 = party_no (-1 if troop is not a prisoner.)
search_troop_prisoner_of_party = (
	"search_troop_prisoner_of_party",
			[
				(store_script_param_1, ":troop_no"),
				(assign, ":prisoner_of", -1),
				(try_for_parties, ":party_no"),
					(eq,  ":prisoner_of", -1),
					(this_or_next|eq, ":party_no", "p_main_party"),
					(ge, ":party_no", centers_begin),
					(party_count_prisoners_of_type, ":troop_found", ":party_no", ":troop_no"),
					(gt, ":troop_found", 0),
					(assign, ":prisoner_of", ":party_no"),
				(try_end),
				(assign, reg0, ":prisoner_of"),
		])
		
		
		# script_troop_get_leaded_center_with_index
		# Input: arg1 = troop_no, arg2 = center index within range between zero and the number of centers that troop owns
		# Output: reg0 = center_no
troop_get_leaded_center_with_index = (
	"troop_get_leaded_center_with_index",
			[
				(store_script_param_1, ":troop_no"),
				(store_script_param_2, ":random_center"),
				(assign, ":result", -1),
				(assign, ":center_count", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(eq, ":result", -1),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(val_add, ":center_count", 1),
					(gt, ":center_count", ":random_center"),
					(assign, ":result", ":center_no"),
				(try_end),
				(assign, reg0, ":result"),
		])

		# script_cf_troop_get_random_leaded_walled_center_with_less_strength_priority
		# Input: arg1 = troop_no, arg2 = preferred_center_no
		# Output: reg0 = center_no (Can fail)
cf_troop_get_random_leaded_walled_center_with_less_strength_priority = (
	"cf_troop_get_random_leaded_walled_center_with_less_strength_priority",
			[
				(store_script_param, ":troop_no", 1),
				(store_script_param, ":preferred_center_no", 2),
				
				(assign, ":num_centers", 0),
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
					(val_add, ":num_centers", 1),
					(try_begin),
						(eq, ":center_no", ":preferred_center_no"),
						(val_add, ":num_centers", 99),
					(try_end),
					##        (call_script, "script_party_calculate_regular_strength", ":center_no"),
					##        (assign, ":strength", reg0),
					##        (lt, ":strength", 80),
					##        (store_sub, ":strength", 100, ":strength"),
					##        (val_div, ":strength", 20),
					##        (val_add, ":num_centers", ":strength"),
				(try_end),
				(gt, ":num_centers", 0),
				(store_random_in_range, ":random_center", 0, ":num_centers"),
				(assign, ":result", -1),
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(eq, ":result", -1),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
					(val_sub, ":random_center", 1),
					(try_begin),
						(eq, ":center_no", ":preferred_center_no"),
						(val_sub, ":random_center", 99),
					(try_end),
					##        (try_begin),
					##          (call_script, "script_party_calculate_regular_strength", ":center_no"),
					##          (assign, ":strength", reg0),
					##          (lt, ":strength", 80),
					##          (store_sub, ":strength", 100, ":strength"),
					##          (val_div, ":strength", 20),
					##          (val_sub, ":random_center", ":strength"),
					##        (try_end),
					(lt, ":random_center", 0),
					(assign, ":result", ":center_no"),
				(try_end),
				(assign, reg0, ":result"),
		])
		
		# script_cf_troop_get_random_leaded_town_or_village_except_center
		# Input: arg1 = troop_no, arg2 = except_center_no
		# Output: reg0 = center_no (Can fail)
cf_troop_get_random_leaded_town_or_village_except_center = (
	"cf_troop_get_random_leaded_town_or_village_except_center",
			[
				(store_script_param_1, ":troop_no"),
				(store_script_param_2, ":except_center_no"),
				
				(assign, ":num_centers", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(neq, ":center_no", ":except_center_no"),
					(val_add, ":num_centers", 1),
				(try_end),
				
				(gt, ":num_centers", 0),
				(store_random_in_range, ":random_center", 0, ":num_centers"),
				(assign, ":end_cond", centers_end),
				(try_for_range, ":center_no", centers_begin, ":end_cond"),
					(neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(neq, ":center_no", ":except_center_no"),
					(val_sub, ":random_center", 1),
					(lt, ":random_center", 0),
					(assign, ":target_center", ":center_no"),
					(assign, ":end_cond", 0),
				(try_end),
				(assign, reg0, ":target_center"),
		])

				# script_write_family_relation_as_s3s_s2_to_s4
		# Inputs: arg1 = troop_no, arg2 = family_no (valid slot no after slot_troop_family_begin)
		# Outputs: s11 = what troop_1 is to troop_2, reg0 = strength of relationship. Normally, "$g_talk_troop" should be troop_2
troop_get_family_relation_to_troop = (
	"troop_get_family_relation_to_troop",
			[
				(store_script_param_1, ":troop_1"),
				(store_script_param_2, ":troop_2"),
				
				(troop_get_type, ":gender_1", ":troop_1"),
				(assign, ":relation_strength", 0),
				
				(troop_get_slot, ":spouse_of_1", ":troop_1", slot_troop_spouse),
				(troop_get_slot, ":spouse_of_2", ":troop_2", slot_troop_spouse),
				
				(try_begin),
					(gt, ":spouse_of_1", -1),
					(troop_get_slot, ":father_of_spouse_of_1", ":spouse_of_1", slot_troop_father),
				(else_try),
					(assign, ":father_of_spouse_of_1", -1),
				(try_end),
				
				(try_begin),
					(gt, ":spouse_of_2", -1),
					(troop_get_slot, ":father_of_spouse_of_2", ":spouse_of_2", slot_troop_father),
				(else_try),
					(assign, ":father_of_spouse_of_2", -1),
				(try_end),
				
				(try_begin),
					(gt, ":spouse_of_2", -1),
					(troop_get_slot, ":mother_of_spouse_of_2", ":spouse_of_2", slot_troop_mother),
				(else_try),
					(assign, ":mother_of_spouse_of_2", -1),
				(try_end),
				
				(troop_get_slot, ":father_of_1", ":troop_1", slot_troop_father),
				(troop_get_slot, ":father_of_2", ":troop_2", slot_troop_father),
				
				#For the sake of simplicity, we can assume that all male aristocrats in prior generations either married commoners or procured their brides from the Old Country, thus discounting intermarriage
				(troop_get_slot, ":mother_of_1", ":troop_1", slot_troop_mother),
				(troop_get_slot, ":mother_of_2", ":troop_2", slot_troop_mother),
				
				(try_begin),
					(is_between, ":father_of_1", companions_begin, kingdom_ladies_end),
					(troop_get_slot, ":paternal_grandfather_of_1", ":father_of_1", slot_troop_father),
				(else_try),
					(assign, ":paternal_grandfather_of_1", -1),
				(try_end),
				
				(try_begin),
					(is_between, ":father_of_2", companions_begin, kingdom_ladies_end),
					(troop_get_slot, ":paternal_grandfather_of_2", ":father_of_2", slot_troop_father),
				(else_try),
					(assign, ":paternal_grandfather_of_2", -1),
				(try_end),
				
				(troop_get_slot, ":guardian_of_1", ":troop_1", slot_troop_guardian),
				(troop_get_slot, ":guardian_of_2", ":troop_2", slot_troop_guardian),
				
				(str_store_string, s11, "str_no_relation"),
				
				(try_begin),
					(eq, ":troop_1", ":troop_2"),
					#self
				(else_try),
					(eq, ":spouse_of_1", ":troop_2"),
					(assign, ":relation_strength", 20),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_wife"),
					(else_try),
						(str_store_string, s11, "str_husband"),
					(try_end),
				(else_try),
					(eq, ":father_of_2", ":troop_1"),
					(assign, ":relation_strength", 15),
					(str_store_string, s11, "str_father"),
				(else_try),
					(eq, ":mother_of_2", ":troop_1"),
					(assign, ":relation_strength", 15),
					(str_store_string, s11, "str_mother"),
				(else_try),
					(this_or_next|eq, ":father_of_1", ":troop_2"),
					(eq, ":mother_of_1", ":troop_2"),
					(assign, ":relation_strength", 15),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_daughter"),
					(else_try),
						(str_store_string, s11, "str_son"),
					(try_end),
				(else_try),
					(gt, ":father_of_1", -1), #necessary, as some lords do not have the father registered
					(eq, ":father_of_1", ":father_of_2"),
					(assign, ":relation_strength", 10),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sister"),
					(else_try),
						(str_store_string, s11, "str_brother"),
					(try_end),
				(else_try),
					(eq, ":guardian_of_2", ":troop_1"),
					(assign, ":relation_strength", 10),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sister"),
					(else_try),
						(str_store_string, s11, "str_brother"),
					(try_end),
				(else_try),
					(eq, ":guardian_of_1", ":troop_2"),
					(assign, ":relation_strength", 10),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sister"),
					(else_try),
						(str_store_string, s11, "str_brother"),
					(try_end),
				(else_try),
					(gt, ":paternal_grandfather_of_1", -1),
					(eq, ":paternal_grandfather_of_1", ":father_of_2"),
					(assign, ":relation_strength", 4),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_niece"),
					(else_try),
						(str_store_string, s11, "str_nephew"),
					(try_end),
				(else_try), #specifically aunt and uncle by blood -- i assume that in a medieval society with lots of internal family conflicts, they would not include aunts and uncles by marriage
					(gt, ":paternal_grandfather_of_2", -1),
					(eq, ":paternal_grandfather_of_2", ":father_of_1"),
					(assign, ":relation_strength", 4),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_aunt"),
					(else_try),
						(str_store_string, s11, "str_uncle"),
					(try_end),
				(else_try),
					(gt, ":paternal_grandfather_of_1", 0),
					(eq, ":paternal_grandfather_of_2", ":paternal_grandfather_of_1"),
					(assign, ":relation_strength", 2),
					(str_store_string, s11, "str_cousin"),
				(else_try),
					(eq, ":father_of_spouse_of_1", ":troop_2"),
					(assign, ":relation_strength", 5),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_daughterinlaw"),
					(else_try),
						(str_store_string, s11, "str_soninlaw"),
					(try_end),
				(else_try),
					(eq, ":father_of_spouse_of_2", ":troop_1"),
					(assign, ":relation_strength", 5),
					(str_store_string, s11, "str_fatherinlaw"),
				(else_try),
					(eq, ":mother_of_spouse_of_2", ":troop_1"),
					(neq, ":mother_of_spouse_of_2", "trp_player"), #May be necessary if mother for troops not set to -1
					(assign, ":relation_strength", 5),
					(str_store_string, s11, "str_motherinlaw"),
					
				(else_try),
					(gt, ":father_of_spouse_of_1", -1), #necessary
					(eq, ":father_of_spouse_of_1", ":father_of_2"),
					(assign, ":relation_strength", 5),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sisterinlaw"),
					(else_try),
						(str_store_string, s11, "str_brotherinlaw"),
					(try_end),
				(else_try),
					(gt, ":father_of_spouse_of_2", -1), #necessary
					(eq, ":father_of_spouse_of_2", ":father_of_1"),
					(assign, ":relation_strength", 5),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sisterinlaw"),
					(else_try),
						(str_store_string, s11, "str_brotherinlaw"),
					(try_end),
				(else_try),
					(gt, ":spouse_of_2", -1), #necessary to avoid bug
					(troop_slot_eq, ":spouse_of_2", slot_troop_guardian, ":troop_1"),
					(assign, ":relation_strength", 5),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sisterinlaw"),
					(else_try),
						(str_store_string, s11, "str_brotherinlaw"),
					(try_end),
				(else_try),
					(gt, ":spouse_of_1", -1), #necessary to avoid bug
					(troop_slot_eq, ":spouse_of_1", slot_troop_guardian, ":troop_2"),
					(assign, ":relation_strength", 5),
					(try_begin),
						(eq, ":gender_1", 1),
						(str_store_string, s11, "str_sisterinlaw"),
					(else_try),
						(str_store_string, s11, "str_brotherinlaw"),
					(try_end),
				(try_end),
				
				(assign, reg4, ":gender_1"),
				(assign, reg0, ":relation_strength"),
		])
		
		
		# script_get_first_agent_with_troop_id
		# called during battle
		# Input: arg1 = troop_no
		# Output: agent_id
cf_get_first_agent_with_troop_id = (
	"cf_get_first_agent_with_troop_id",
			[
				(store_script_param_1, ":troop_no"),
				#      (store_script_param_2, ":agent_no_to_begin_searching_after"),
				(assign, ":result", -1),
				(try_for_agents, ":cur_agent"),
					(eq, ":result", -1),
					##        (try_begin),
					##          (eq, ":cur_agent", ":agent_no_to_begin_searching_after"),
					##          (assign, ":agent_no_to_begin_searching_after", -1),
					##        (try_end),
					##        (eq, ":agent_no_to_begin_searching_after", -1),
					(agent_get_troop_id, ":cur_troop_no", ":cur_agent"),
					(eq, ":cur_troop_no", ":troop_no"),
					(assign, ":result", ":cur_agent"),
				(try_end),
				(assign, reg0, ":result"),
				(neq, reg0, -1),
		])
		
		# script_troop_write_owned_centers_to_s2
		# Input: arg1 = troop_no
		# Output: s2
troop_write_owned_centers_to_s2 = (
	"troop_write_owned_centers_to_s2",
			[
				(store_script_param_1, ":troop_no"),
				
				(call_script, "script_get_number_of_hero_centers", ":troop_no"),
				(assign, ":no_centers", reg0),
				
				(str_store_troop_name, s5, ":troop_no"),
				
				(try_begin),
					(gt, ":no_centers", 1),
					(try_for_range, ":i_center", 1, ":no_centers"),
						(call_script, "script_troop_get_leaded_center_with_index", ":troop_no", ":i_center"),
						(str_store_party_name_link, s50, reg0),
						(try_begin),
							(eq, ":i_center", 1),
							(call_script, "script_troop_get_leaded_center_with_index", ":troop_no", 0),
							(str_store_party_name_link, s51, reg0),
							(str_store_string, s51, "str_s50_and_s51"),
						(else_try),
							(str_store_string, s51, "str_s50_comma_s51"),
						(try_end),
					(try_end),
					(str_store_string, s2, "str_s5_is_the_ruler_of_s51"),
				(else_try),
					(eq, ":no_centers", 1),
					(call_script, "script_troop_get_leaded_center_with_index", ":troop_no", 0),
					(str_store_party_name_link, s51, reg0),
					(str_store_string, s2, "str_s5_is_the_ruler_of_s51"),
				(else_try),
					(store_troop_faction, ":faction_no", ":troop_no"),
					(str_store_faction_name_link, s6, ":faction_no"),
					(str_store_string, s2, "str_s5_is_a_nobleman_of_s6"),
				(try_end),
		])


		
		# script_calculate_troop_score_for_center
		# Input: arg1 = troop_no, arg2 = center_no
		# Output: reg0 = score
calculate_troop_score_for_center = (
	"calculate_troop_score_for_center",
			[(store_script_param, ":troop_no", 1),
				(store_script_param, ":center_no", 2),
				(assign, ":num_center_points", 1),
				(try_for_range, ":cur_center", centers_begin, centers_end),
					(assign, ":center_owned", 0),
					(try_begin),
						(eq, ":troop_no", "trp_player"),
						(party_slot_eq, ":cur_center", slot_town_lord, stl_reserved_for_player),
						(assign, ":center_owned", 1),
					(try_end),
					(this_or_next|party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
					(eq, ":center_owned", 1),
					(try_begin),
						(party_slot_eq, ":cur_center", slot_party_type, spt_town),
						(val_add, ":num_center_points", 4),
					(else_try),
						(party_slot_eq, ":cur_center", slot_party_type, spt_castle),
						(val_add, ":num_center_points", 2),
					(else_try),
						(val_add, ":num_center_points", 1),
					(try_end),
				(try_end),
				(troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
				(store_add, ":score", 500, ":troop_renown"),
				(val_div, ":score", ":num_center_points"),
				(store_random_in_range, ":random", 50, 100),
				(val_mul, ":score", ":random"),
				(try_begin),
					(party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":troop_no"),
					(val_mul, ":score", 3),
					(val_div, ":score", 2),
				(try_end),
				(try_begin),
					(eq, ":troop_no", "trp_player"),
					(faction_get_slot, ":faction_leader", "$players_kingdom"),
					(call_script, "script_troop_get_player_relation", ":faction_leader"),
					(assign, ":leader_relation", reg0),
					#(troop_get_slot, ":leader_relation", ":faction_leader", slot_troop_player_relation),
					(val_mul, ":leader_relation", 2),
					(val_add, ":score", ":leader_relation"),
				(try_end),
				(assign, reg0, ":score"),
		])
		