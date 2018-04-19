from header import *


# script_game_get_upgrade_xp
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed exp for upgrade
game_get_upgrade_xp =( 
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
game_get_join_cost=(
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
		