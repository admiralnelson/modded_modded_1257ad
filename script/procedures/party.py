from header import *

		#script_party_calculate_regular_strength:
		# INPUT:
		# param1: Party-id
party_calculate_regular_strength	= (
	"party_calculate_regular_strength",
			[
				(store_script_param_1, ":party"), #Party_id
				
				(assign, reg0,0),
				(party_get_num_companion_stacks, ":num_stacks",":party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
					(neg|troop_is_hero, ":stack_troop"),
					(store_character_level, ":stack_strength", ":stack_troop"),
					(val_add, ":stack_strength", 12),
					(val_mul, ":stack_strength", ":stack_strength"),
					(val_div, ":stack_strength", 100),
					(party_stack_get_size, ":stack_size",":party",":i_stack"),
					(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
					(val_sub, ":stack_size", ":num_wounded"),
					(val_mul, ":stack_strength", ":stack_size"),
					(val_add,reg0, ":stack_strength"),
				(try_end),
		])

		#script_loot_player_items:
		# INPUT: arg1 = enemy_party_no
		# Output: none
loot_player_items	= (
	"loot_player_items",
			[
				(store_script_param, ":enemy_party_no", 1),
				
				(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
				(try_for_range, ":i_slot", 0, ":inv_cap"),
					(troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
					(ge, ":item_id", 0),
					(troop_get_inventory_slot_modifier, ":item_modifier", "trp_player", ":i_slot"),
					(try_begin),
						(is_between, ":item_id", trade_goods_begin, trade_goods_end),
						(assign, ":randomness", 20),
					(else_try),
						(this_or_next|is_between, ":item_id", horses_begin, horses_end),
						(this_or_next|eq, ":item_id", "itm_warhorse_sarranid"),
						(eq, ":item_id", "itm_warhorse_steppe"),
						(assign, ":randomness", 15),
					(else_try),
						(this_or_next|is_between, ":item_id", weapons_begin, weapons_end),
						(is_between, ":item_id", ranged_weapons_begin, ranged_weapons_end),
						(assign, ":randomness", 5),
					(else_try),
						(this_or_next|is_between, ":item_id", armors_begin, armors_end),
						#(this_or_next|eq, ":item_id", "itm_balt_helmet_b"), #added to the end because of not breaking the save games
						(is_between, ":item_id", shields_begin, shields_end),
						(assign, ":randomness", 5),
					(try_end),
					(store_random_in_range, ":random_no", 0, 100),
					(lt, ":random_no", ":randomness"),
					(troop_remove_item, "trp_player", ":item_id"),
					
					(try_begin),
						(gt, ":enemy_party_no", 0),
						(party_get_slot, ":cur_loot_slot", ":enemy_party_no", slot_party_next_looted_item_slot),
						(val_add, ":cur_loot_slot", slot_party_looted_item_1),
						(party_set_slot, ":enemy_party_no", ":cur_loot_slot", ":item_id"),
						(val_sub, ":cur_loot_slot", slot_party_looted_item_1),
						(val_add, ":cur_loot_slot", slot_party_looted_item_1_modifier),
						(party_set_slot, ":enemy_party_no", ":cur_loot_slot", ":item_modifier"),
						(val_sub, ":cur_loot_slot", slot_party_looted_item_1_modifier),
						(val_add, ":cur_loot_slot", 1),
						(val_mod, ":cur_loot_slot", num_party_loot_slots),
						(party_set_slot, ":enemy_party_no", slot_party_next_looted_item_slot, ":cur_loot_slot"),
					(try_end),
				(try_end),
				(store_troop_gold, ":cur_gold", "trp_player"),
				(store_div, ":max_lost", ":cur_gold", 5),
				(store_div, ":min_lost", ":cur_gold", 10),
				(store_random_in_range, ":lost_gold", ":min_lost", ":max_lost"),
				(troop_remove_gold, "trp_player", ":lost_gold"),
		])
		
		#script_party_give_xp_and_gold:
		# INPUT:
		# param1: destroyed Party-id
		# calculates and gives player paty's share of gold and xp.
		
party_give_xp_and_gold	= (
	"party_give_xp_and_gold",
			[
				(store_script_param_1, ":enemy_party"), #Party_id
				
				(call_script, "script_calculate_main_party_shares"),
				(assign, ":num_player_party_shares", reg0),
				
				(assign, ":total_gain", 0),
				(party_get_num_companion_stacks, ":num_stacks",":enemy_party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id,     ":stack_troop",":enemy_party",":i_stack"),
					(neg|troop_is_hero, ":stack_troop"),
					(party_stack_get_size, ":stack_size",":enemy_party",":i_stack"),
					(store_character_level, ":level", ":stack_troop"),
					(store_add, ":gain", ":level", 10),
					(val_mul, ":gain", ":gain"),
					(val_div, ":gain", 10),
					(store_mul, ":stack_gain", ":gain", ":stack_size"),
					(val_add, ":total_gain", ":stack_gain"),
				(try_end),
				
				(val_mul, ":total_gain", "$g_strength_contribution_of_player"),
				(val_div, ":total_gain", 100),
				
				(val_min, ":total_gain", 40000), #eliminate negative results
				
				(assign, ":player_party_xp_gain", ":total_gain"),
				(store_random_in_range, ":r", 50, 100),
				(val_mul, ":player_party_xp_gain", ":r"),
				(val_div, ":player_party_xp_gain", 100),
				
				(party_add_xp, "p_main_party", ":player_party_xp_gain"),
				
				(store_mul, ":player_gold_gain", ":total_gain", player_loot_share),
				(val_min, ":player_gold_gain", 60000), #eliminate negative results
				(store_random_in_range, ":r", 50, 100),
				(val_mul, ":player_gold_gain", ":r"),
				(val_div, ":player_gold_gain", 100),
				(val_div, ":player_gold_gain", ":num_player_party_shares"),
				
				#add gold now
				(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(call_script, "script_troop_add_gold", ":stack_troop", ":player_gold_gain"),
					(try_end),
				(try_end),
		])
		

		#script_setup_party_meeting:
		# INPUT:
		# param1: Party-id with which meeting will be made.
		
setup_party_meeting	= (
	"setup_party_meeting",
			[
				(store_script_param_1, ":meeting_party"),
				(try_begin),
					(lt, "$g_encountered_party_relation", 0), #hostile
					#        (call_script, "script_music_set_situation_with_culture", mtf_sit_encounter_hostile),
				(try_end),
				(call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
				(modify_visitors_at_site,":meeting_scene"),(reset_visitors),
				(set_visitor,0,"trp_player"),
				(party_stack_get_troop_id, ":meeting_troop",":meeting_party",0),
				(party_stack_get_troop_dna,":troop_dna",":meeting_party",0),
				(set_visitor,17,":meeting_troop",":troop_dna"),
				(set_jump_mission,"mt_conversation_encounter"),
				(jump_to_scene,":meeting_scene"),
				(change_screen_map_conversation, ":meeting_troop"),
		])


		#script_party_remove_all_companions:
		# INPUT:
		# param1: Party-id from which  companions will be removed.
		# "$g_move_heroes" : controls if heroes will also be removed.
party_remove_all_companions = (
	"party_remove_all_companions",
			[
				(store_script_param_1, ":party"), #Source Party_id
				(party_get_num_companion_stacks, ":num_companion_stacks",":party"),
				(try_for_range_backwards, ":stack_no", 0, ":num_companion_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":party",":stack_no"),
					
					(party_stack_get_size, ":stack_size", ":party", ":stack_no"),
					
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(neg|is_between, ":stack_troop", pretenders_begin, pretenders_end),
						(neq, ":stack_troop", "trp_player"),
						(eq, "$g_prison_heroes", 1),
						(eq, ":party", "p_main_party"),
						(store_random_in_range, ":succeed_escaping", 0, 4),
						(neq, ":succeed_escaping", 0), #25% chance companion stays with us.
						(troop_set_health, ":stack_troop", 100), #heal before leaving
						(store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
						(assign, ":minimum_distance", 99999),
						(assign, ":prison_center", -1),
						(try_for_range, ":center", walled_centers_begin, walled_centers_end),
							(store_faction_of_party, ":center_faction", ":center"),
							(eq, ":center_faction", ":enemy_faction"),
							(store_distance_to_party_from_party, ":dist", ":center", "p_main_party"),
							(lt, ":dist", ":minimum_distance"),
							(assign, ":minimum_distance", ":dist"),
							(assign, ":prison_center", ":center"),
						(try_end),
						(assign, reg1, ":prison_center"),
						#(display_message, "@{!}DEBUG : prison center is {reg1}"),
						(try_begin),
							(ge, ":prison_center", 0),
							(store_random_in_range, ":succeed_escaping", 0, 4),
							(neq, ":succeed_escaping", 0), #50% chance companion escapes to a tavern.
							(party_add_prisoners, ":prison_center", ":stack_troop", ":stack_size"),
							(troop_set_slot, ":stack_troop", slot_troop_prisoner_of_party, ":prison_center"),
							(troop_set_slot, ":stack_troop", slot_troop_playerparty_history, pp_history_scattered),
							(troop_set_slot, ":stack_troop", slot_troop_turned_down_twice, 0),
							(troop_set_slot, ":stack_troop", slot_troop_occupation, 0),
							(party_remove_members, ":party", ":stack_troop", ":stack_size"),
							(try_begin),
								(eq, "$cheat_mode", 1),
								(str_store_party_name, s1, ":prison_center"),
								(display_message, "str_your_hero_prisoned_at_s1"),
							(try_end),
						(else_try),
							#bandits or deserters won and captured companion. So place it randomly in a town's tavern.
							(assign, ":end_condition", 1000),
							(try_for_range, ":unused", 0, ":end_condition"),
								(store_random_in_range, ":town_no", towns_begin, towns_end),
								(neg|troop_slot_eq, ":stack_troop", slot_troop_home, ":town_no"),
								(neg|troop_slot_eq, ":stack_troop", slot_troop_first_encountered, ":town_no"),
								(assign, ":end_condition", -1),
							(try_end),
							(troop_set_slot, ":stack_troop", slot_troop_cur_center, ":town_no"),
							(troop_set_slot, ":stack_troop", slot_troop_playerparty_history, pp_history_scattered),
							(troop_set_slot, ":stack_troop", slot_troop_turned_down_twice, 0),
							(troop_set_slot, ":stack_troop", slot_troop_occupation, 0),
							(party_remove_members, ":party", ":stack_troop", ":stack_size"),
							(try_begin),
								(eq, "$cheat_mode", 1),
								(str_store_troop_name, 4, ":stack_troop"),
								(str_store_party_name, 5, ":town_no"),
								(display_message, "@{!}{s4} is sent to {s5} after defeat"),
							(try_end),
						(try_end),
					(else_try),
						(this_or_next|neg|troop_is_hero, ":stack_troop"),
						(eq, "$g_move_heroes", 1),
						(party_remove_members, ":party", ":stack_troop", ":stack_size"),
					(try_end),
				(try_end),
		])
		
		#script_party_remove_all_prisoners:
		# INPUT:
		# param1: Party-id from which  prisoners will be removed.
		# "$g_move_heroes" : controls if heroes will also be removed.
		
party_remove_all_prisoners = (
	"party_remove_all_prisoners",
			[
				(store_script_param_1, ":party"), #Source Party_id
				(party_get_num_prisoner_stacks, ":num_prisoner_stacks",":party"),
				(try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":party",":stack_no"),
					(this_or_next|neg|troop_is_hero, ":stack_troop"),
					(eq, "$g_move_heroes", 1),
					(party_prisoner_stack_get_size, ":stack_size",":party",":stack_no"),
					(party_remove_prisoners, ":party", ":stack_troop", ":stack_size"),
				(try_end),
		])
		
		#script_party_add_party_companions:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
party_add_party_companions = (
	"party_add_party_companions",
			[
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(party_get_num_companion_stacks, ":num_stacks",":source_party"),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
					(this_or_next|neg|troop_is_hero, ":stack_troop"),
					(eq, "$g_move_heroes", 1),
					(party_stack_get_size, ":stack_size",":source_party",":stack_no"),
					(party_add_members, ":target_party", ":stack_troop", ":stack_size"),
					(party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack_no"),
					(party_wound_members, ":target_party", ":stack_troop", ":num_wounded"),
				(try_end),
		])
		
		#script_party_add_party_prisoners:
		# INPUT:
		# param1: Party-id to add the second party
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
party_add_party_prisoners = (
	"party_add_party_prisoners",
			[
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
					(this_or_next|neg|troop_is_hero, ":stack_troop"),
					(eq, "$g_move_heroes", 1),
					(party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
					(party_add_members, ":target_party", ":stack_troop", ":stack_size"),
				(try_end),
		])
		
		#script_party_prisoners_add_party_companions:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
party_prisoners_add_party_companions = (
	"party_prisoners_add_party_companions",
			[
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(party_get_num_companion_stacks, ":num_stacks",":source_party"),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
					(this_or_next|neg|troop_is_hero, ":stack_troop"),
					(eq, "$g_move_heroes", 1),
					(party_stack_get_size, ":stack_size",":source_party",":stack_no"),
					(party_add_prisoners, ":target_party", ":stack_troop", ":stack_size"),
				(try_end),
		])
		
		#script_party_prisoners_add_party_prisoners:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
party_prisoners_add_party_prisoners = (
	"party_prisoners_add_party_prisoners",
			[
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
					(this_or_next|neg|troop_is_hero, ":stack_troop"),
					(eq, "$g_move_heroes", 1),
					(party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
					(party_add_prisoners, ":target_party", ":stack_troop", ":stack_size"),
				(try_end),
		])
		
		# script_party_add_party:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
party_add_party = (
	"party_add_party",
			[
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(call_script, "script_party_add_party_companions",          ":target_party", ":source_party"),
				(call_script, "script_party_prisoners_add_party_prisoners", ":target_party", ":source_party"),
		])
		
		
		#script_party_copy:
		# INPUT:
		# param1: Party-id to copy the second party
		# param2: Party-id which will be copied to the first one.
		
party_copy = (
	"party_copy",
			[
				(assign, "$g_move_heroes", 1),
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(party_clear, ":target_party"),
				(call_script, "script_party_add_party", ":target_party", ":source_party"),
		])
		
		
		#script_clear_party_group:
		# INPUT:
		# param1: Party-id of the root of the group.
		# This script will clear the root party and all parties attached to it recursively.
		
clear_party_group = (
	"clear_party_group",
			[
				(store_script_param_1, ":root_party"),
				
				(party_clear, ":root_party"),
				(party_get_num_attached_parties, ":num_attached_parties", ":root_party"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":root_party", ":attached_party_rank"),
					(call_script, "script_clear_party_group", ":attached_party"),
				(try_end),
		])
		
		
		#script_party_add_wounded_members_as_prisoners:
		# INPUT:
		# param1: Party-id to add the second party
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
party_add_wounded_members_as_prisoners = (
	"party_add_wounded_members_as_prisoners",
			[
				(store_script_param_1, ":target_party"), #Target Party_id
				(store_script_param_2, ":source_party"), #Source Party_id
				(party_get_num_companion_stacks, ":num_stacks", ":source_party"),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack_no"),
					(ge, ":num_wounded", 1),
					(party_stack_get_troop_id, ":stack_troop", ":source_party", ":stack_no"),
					(this_or_next|neg|troop_is_hero, ":stack_troop"),
					(eq, "$g_move_heroes", 1),
					#(party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
					(party_add_prisoners, ":target_party", ":stack_troop", ":num_wounded"),
				(try_end),
		])
		
		
		#script_collect_prisoners_from_empty_parties:
		# INPUT:
		# param1: Party-id of the root of the group.
		# param2: Party to collect prisoners in.
		# make sure collection party is cleared before calling this.
		
collect_prisoners_from_empty_parties = (
	"collect_prisoners_from_empty_parties",
			[
				(store_script_param_1, ":party_no"),
				(store_script_param_2, ":collection_party"),
				
				(party_get_num_companions, ":num_companions", ":party_no"),
				(try_begin),
					(eq, ":num_companions", 0), #party is empty (has no companions). Collect its prisoners.
					(party_get_num_prisoner_stacks, ":num_stacks",":party_no"),
					(try_for_range, ":stack_no", 0, ":num_stacks"),
						(party_prisoner_stack_get_troop_id, ":stack_troop", ":party_no", ":stack_no"),
						(troop_is_hero, ":stack_troop"),
						(party_add_members, ":collection_party", ":stack_troop", 1),
					(try_end),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
					(call_script, "script_collect_prisoners_from_empty_parties", ":attached_party", ":collection_party"),
				(try_end),
		])
		
		#script_change_party_morale:
		# INPUT: party_no, morale_gained
		# OUTPUT: none
		
change_party_morale = (
	"change_party_morale",
			[
				(store_script_param_1, ":party_no"),
				(store_script_param_2, ":morale_dif"),
				
				(party_get_morale, ":cur_morale", ":party_no"),
				(store_add, ":new_morale", ":cur_morale", ":morale_dif"),
				(val_clamp, ":new_morale", 0, 100),
				(party_set_morale, ":party_no", ":new_morale"),
				(str_store_party_name, s1, ":party_no"),
				
				(try_begin),
					(lt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":cur_morale", ":new_morale"),
				(else_try),
					(gt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":new_morale", ":cur_morale"),
				(try_end),
		])
		

		#script_count_casualties_and_adjust_morale:
		# INPUT: none
		# OUTPUT: none
		
count_casualties_and_adjust_morale = (
	"count_casualties_and_adjust_morale",
			[
				(call_script, "script_calculate_main_party_shares"),
				(assign, ":num_player_party_shares", reg0),
				
				(assign, ":our_loss_score", 0),
				(party_get_num_companion_stacks, ":num_stacks","p_player_casualties"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop", "p_player_casualties", ":i_stack"),
					(party_stack_get_size, ":stack_size", "p_player_casualties", ":i_stack"),
					
					(party_stack_get_num_wounded, ":num_wounded", "p_player_casualties", ":i_stack"),
					(store_mul, ":stack_size_mul_2", ":stack_size", 2),
					(store_sub, ":stack_size_mul_2_sub_wounded", ":num_wounded"),
					
					(store_character_level, ":level", ":stack_troop"),
					(store_add, ":gain", ":level", 3),
					
					#if died/wounded troop is player troop then give its level +30 while calculating troop die effect on morale
					(try_begin),
						(eq, ":stack_troop", "trp_player"),
						(val_add, ":level", 75),
					(else_try),
						(troop_is_hero, ":stack_troop"),
						(val_add, ":level", 50),
					(try_end),
					
					(val_mul, ":gain", ":gain"),
					(val_div, ":gain", 10),
					(assign, reg0, ":gain"),
					(val_mul, ":gain", ":stack_size"),
					
					(try_begin),
						(neg|troop_is_hero, ":stack_troop"),
						(val_mul, ":gain", ":stack_size_mul_2_sub_wounded"),
						(val_div, ":gain", ":stack_size_mul_2"),
					(try_end),
					
					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg1, ":stack_size"),
						(assign, reg2, ":gain"),
						(display_message, "str_our_per_person__reg0_num_people__reg1_total_gain__reg2"),
					(try_end),
					(val_add, ":our_loss_score", ":gain"),
				(try_end),
				
				(assign, ":died_enemy_population", 0),
				(assign, ":enemy_loss_score", 0),
				(party_get_num_companion_stacks, ":num_stacks","p_enemy_casualties"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop", "p_enemy_casualties", ":i_stack"),
					(party_stack_get_size, ":stack_size", "p_enemy_casualties", ":i_stack"),
					
					(party_stack_get_num_wounded, ":num_wounded", "p_enemy_casualties", ":i_stack"),
					(store_mul, ":stack_size_mul_2", ":stack_size", 2),
					(store_sub, ":stack_size_mul_2_sub_wounded", ":stack_size_mul_2", ":num_wounded"),
					
					(store_character_level, ":level", ":stack_troop"),
					(store_add, ":gain", ":level", 3),
					
					#if troop is hero give extra +15 level while calculating troop die effect on morale
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(val_add, ":level", 50),
					(try_end),
					
					(val_mul, ":gain", ":gain"),
					(val_div, ":gain", 10),
					(assign, reg0, ":gain"),
					(val_mul, ":gain", ":stack_size"),
					
					(try_begin),
						(neg|troop_is_hero, ":stack_troop"),
						(val_mul, ":gain", ":stack_size_mul_2_sub_wounded"),
						(val_div, ":gain", ":stack_size_mul_2"),
					(try_end),
					
					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg1, ":stack_size"),
						(assign, reg2, ":gain"),
						(display_message, "str_ene_per_person__reg0_num_people__reg1_total_gain__reg2"),
					(try_end),
					(val_add, ":enemy_loss_score", ":gain"),
					(val_add, ":died_enemy_population", ":stack_size"),
				(try_end),
				
				(assign, ":ally_loss_score", 0),
				(try_begin),
					(eq, "$any_allies_at_the_last_battle", 1),
					(party_get_num_companion_stacks, ":num_stacks","p_ally_casualties"),
					(try_for_range, ":i_stack", 0, ":num_stacks"),
						(party_stack_get_troop_id, ":stack_troop", "p_ally_casualties", ":i_stack"),
						(party_stack_get_size, ":stack_size", "p_ally_casualties", ":i_stack"),
						
						(party_stack_get_num_wounded, ":num_wounded", "p_ally_casualties", ":i_stack"),
						(store_mul, ":stack_size_mul_2", ":stack_size", 2),
						(store_sub, ":stack_size_mul_2_sub_wounded", ":num_wounded"),
						
						(store_character_level, ":level", ":stack_troop"),
						(store_add, ":gain", ":level", 3),
						
						#if troop is hero give extra +15 level while calculating troop die effect on morale
						(try_begin),
							(troop_is_hero, ":stack_troop"),
							(val_add, ":level", 50),
						(try_end),
						
						(val_mul, ":gain", ":gain"),
						(val_div, ":gain", 10),
						(assign, reg0, ":gain"),
						(val_mul, ":gain", ":stack_size"),
						
						(try_begin),
							(neg|troop_is_hero, ":stack_troop"),
							(val_mul, ":gain", ":stack_size_mul_2_sub_wounded"),
							(val_div, ":gain", ":stack_size_mul_2"),
						(try_end),
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(assign, reg1, ":stack_size"),
							(assign, reg2, ":gain"),
							(display_message, "str_all_per_person__reg0_num_people__reg1_total_gain__reg2"),
						(try_end),
						(val_add, ":ally_loss_score", ":gain"),
					(try_end),
				(try_end),
				
				(store_add, ":our_losses", ":our_loss_score", ":ally_loss_score"),
				(assign, ":enemy_losses", ":enemy_loss_score"),
				(val_mul, ":our_losses", 100),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":enemy_losses"),
					(display_message, "@{!}DEBUGS : enemy_loses : {reg0}"),
				(try_end),
				
				(try_begin),
					(gt, ":enemy_losses", 0),
					(store_div, ":loss_ratio", ":our_losses", ":enemy_losses"),
				(else_try),
					(assign, ":loss_ratio", 1000),
				(try_end),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(assign, reg1, ":loss_ratio"),
					(display_message, "str_loss_ratio_is_reg1"),
				(try_end),
				
				(try_begin),
					(neg|is_between, "$g_enemy_party", centers_begin, centers_end),
					(store_sub, ":total_gain", 60, ":loss_ratio"),
				(else_try),
					(store_sub, ":total_gain", 100, ":loss_ratio"),
				(try_end),
				
				(try_begin),
					(lt, ":total_gain", 0),
					(val_div, ":total_gain", 2),
				(try_end),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":total_gain"),
					(display_message, "@{!}DEBUGS1 : total_gain : {reg0}"),
				(try_end),
				
				(val_max, ":total_gain", -60), #total gain changes between -60(1.8+ loss ratio) and 60(0 loss ratio). We assumed average loss ratio is 0.6
				(val_mul, ":total_gain", ":enemy_losses"),
				(val_div, ":total_gain", 100),
				
				(store_mul, ":total_enemy_morale_gain", ":total_gain", -1), #enemies get totally negative of the morale we get
				(val_mul, ":total_gain", "$g_strength_contribution_of_player"),
				(val_div, ":total_gain", 100),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":total_gain"),
					(display_message, "@{!}DEBUGS2 : total_gain : {reg0}"),
				(try_end),
				
				(try_begin),
					(party_is_active, "$g_enemy_party"), #change enemy morale if and only if there is a valid enemy party
					
					#main enemy party
					(assign, ":total_enemy_population", 0),
					(val_add, ":total_enemy_population", 10), #every part effect total population by number of agents they have plus 10
					(party_get_num_companion_stacks, ":num_stacks", "$g_enemy_party"),
					(try_for_range, ":i_stack", 0, ":num_stacks"),
						(party_stack_get_troop_id, ":stack_troop", "$g_enemy_party", ":i_stack"),
						(party_stack_get_size, ":stack_size", "$g_enemy_party", ":i_stack"),
						(val_add, ":total_enemy_population", ":stack_size"),
					(try_end),
					(assign, ":main_enemy_party_population", ":total_enemy_population"),
					
					#enemy attachers
					(party_get_num_attached_parties, ":num_attached_parties",  "$g_enemy_party"),
					(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
						(val_add, ":total_enemy_population", 10), #every part effect total population by number of agents they have plus 10
						(party_get_attached_party_with_rank, ":attached_party", "$g_enemy_party", ":attached_party_rank"),
						(party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
						(try_for_range, ":i_stack", 0, ":num_stacks"),
							(party_stack_get_troop_id, ":stack_troop", ":attached_party", ":i_stack"),
							(party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
							(val_add, ":total_enemy_population", ":stack_size"),
						(try_end),
					(try_end),
					
					#(assign, reg3, ":total_enemy_population"),
					#(assign, reg4, ":died_enemy_population"),
					#(store_sub, ":remaining_enemy_population", ":total_enemy_population", ":died_enemy_population"),
					#(val_add, ":remaining_enemy_population", 10),
					#(assign, reg5, ":remaining_enemy_population"),
					#(display_message, "@total : {reg3}, died : {reg4}, remaining : {reg5}"),
					
					#remaining enemy population has 10+remaining soldiers in enemy party
					(assign, ":remaining_enemy_population", ":total_enemy_population"),
					
					(assign, reg5, ":remaining_enemy_population"),
					(assign, reg6, ":total_enemy_morale_gain"),
					
					(set_fixed_point_multiplier, 100),
					(val_mul, ":remaining_enemy_population", 100),
					(store_sqrt, ":sqrt_remaining_enemy_population", ":remaining_enemy_population"),
					(val_div, ":sqrt_remaining_enemy_population", 100),
					(val_div, ":total_enemy_morale_gain", ":sqrt_remaining_enemy_population"),
					(val_div, ":total_enemy_morale_gain", 4),
					
					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg7, ":total_enemy_morale_gain"),
						(display_message, "str_total_enemy_morale_gain__reg6_last_total_enemy_morale_gain__reg7_remaining_enemy_population__reg5"),
					(try_end),
					
					(store_mul, ":party_morale_gain", ":total_enemy_morale_gain", ":main_enemy_party_population"),
					(val_div, ":party_morale_gain", ":total_enemy_population"),
					
					(try_begin),
						(party_is_active, "$g_enemy_party"),
						
						(call_script, "script_change_party_morale", "$g_enemy_party", ":party_morale_gain"),
						
						(party_get_num_attached_parties, ":num_attached_parties", "$g_enemy_party"),
						(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
							(party_get_attached_party_with_rank, ":attached_party", "$g_enemy_party", ":attached_party_rank"),
							(party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
							(assign, ":party_population", 0),
							(try_for_range, ":i_stack", 0, ":num_stacks"),
								(party_stack_get_troop_id, ":stack_troop", ":attached_party", ":i_stack"),
								(party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
								(val_add, ":party_population", ":stack_size"),
							(try_end),
							#(store_div, ":party_ratio", ":total_enemy_population_multiplied_by_100", ":party_population"), #party ratio changes between 0..100, shows population ratio of that party among all enemy parties
							(store_mul, ":party_morale_gain", ":total_enemy_morale_gain", ":party_population"),
							(val_div, ":party_morale_gain", ":total_enemy_population"),
							(call_script, "script_change_party_morale", ":attached_party", ":party_morale_gain"),
						(try_end),
					(try_end),
				(try_end),
				
				#Add morale
				(assign, ":morale_gain", ":total_gain"),
				(val_div, ":morale_gain", ":num_player_party_shares"),#if there are lots of soldiers in my party there will be less morale increase.
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":num_player_party_shares"),
					(assign, reg1, ":total_gain"),
					(display_message, "@{!}DEBUGS3 : num_player_party_shares:{reg0}, total_gain:{reg1}"),
				(try_end),
				
				(call_script, "script_change_player_party_morale", ":morale_gain"),
				
				(store_mul, ":killed_enemies_by_our_soldiers", ":died_enemy_population", "$g_strength_contribution_of_player"),
				(store_div, ":faction_morale_change", ":killed_enemies_by_our_soldiers", 8), #each 8 killed agent with any faction decreases morale of troops belong to that faction in our party by 1.
				(try_begin),
					(gt, ":faction_morale_change", 2000),
					(assign, ":faction_morale_change", 2000),
				(try_end),
				
				(try_begin), #here we give positive morale to our troops of with same faction of ally party with 2/3x multipication.
					(ge, "$g_ally_party", 0),
					
					(store_div, ":ally_faction_morale_change", ":faction_morale_change", 3), #2/3x multipication (less than normal)
					(val_mul, ":ally_faction_morale_change", 2),
					(store_faction_of_party, ":ally_faction", "$g_ally_party"),
					(faction_get_slot, ":faction_morale", ":ally_faction",  slot_faction_morale_of_player_troops),
					(val_add, ":faction_morale", ":ally_faction_morale_change"),
					# rafi (faction_set_slot, ":ally_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
				(try_end),
				
				(try_begin), #here we give positive morale to our troops of owner of rescued village's faction after saving village from bandits by x3 bonus.
					(neg|party_is_active, "$g_enemy_party"),
					(ge, "$current_town", 0),
					
					(val_mul, ":faction_morale_change", 2), #2x bonus (more than normal)
					(store_faction_of_party, ":ally_faction", "$current_town"),
					(faction_get_slot, ":faction_morale", ":ally_faction",  slot_faction_morale_of_player_troops),
					(val_add, ":faction_morale", ":faction_morale_change"),
					# rafi (faction_set_slot, ":ally_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
				(else_try),
					(party_is_active, "$g_enemy_party"),
					(assign, ":currently_in_rebellion", 0),
					(try_begin),
						(eq, "$players_kingdom", "fac_player_supporters_faction"),
						(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
						(assign, ":currently_in_rebellion", 1),
					(try_end),
					(eq, ":currently_in_rebellion", 0),
					
					(store_div, ":faction_morale_change", ":faction_morale_change", 3), #2/3x multipication (less than normal)
					(val_mul, ":faction_morale_change", 2),
					(store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
					(faction_get_slot, ":faction_morale", ":enemy_faction",  slot_faction_morale_of_player_troops),
					(val_sub, ":faction_morale", ":faction_morale_change"),
					# rafi (faction_set_slot, ":enemy_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
				(try_end),
				
		])
		

		#script_add_routed_party
		#INPUT: none
		#OUTPUT: none
add_routed_party = (
	"add_routed_party",
			[
				(party_get_num_companion_stacks, ":num_stacks", "p_routed_enemies"), #question, I changed (total_enemy_casualties) with (p_routed_enemies) because this is not prisoner in p_routed_enemies party.
				(assign, ":num_regulars", 0),
				(assign, ":deleted_stacks", 0),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(store_sub, ":difference", ":num_stacks", ":stack_no"),
					(ge, ":difference", ":deleted_stacks"),
					(store_sub, ":stack_no_minus_deleted", ":stack_no", ":deleted_stacks"),
					(party_stack_get_troop_id, ":stack_troop", "p_routed_enemies", ":stack_no_minus_deleted"),
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(party_stack_get_size, ":stack_size", "p_routed_enemies", ":stack_no_minus_deleted"),
						(party_remove_members, "p_routed_enemies", ":stack_troop", 1),
						(try_begin),
							(le, ":stack_size", 1),
							(val_add, ":deleted_stacks", 1), #if deleted hero is the only one in his troop, now we have one less stacks
						(try_end),
					(else_try),
						(val_add, ":num_regulars", 1),
					(try_end),
				(try_end),
				
				#add new party to map if there is at least one routed agent. (new party name : routed_party, template : routed_warriors)
				(try_begin),
					(ge, ":num_regulars", 1),
					
					(set_spawn_radius, 2),
					(spawn_around_party, "p_main_party", "pt_routed_warriors"),
					(assign, ":routed_party", reg0),
					
					(party_set_slot, ":routed_party", slot_party_commander_party, -1), #we need this because 0 is player's party!
					
					(assign, ":max_routed_agents", 0),
					(assign, ":routed_party_faction", "fac_neutral"),
					(try_for_range, ":cur_faction", fac_kingdom_1, fac_kingdoms_end),
						(faction_get_slot, ":num_routed_agents_in_this_faction", ":cur_faction", slot_faction_num_routed_agents),
						(gt, ":num_routed_agents_in_this_faction", ":max_routed_agents"),
						(assign, ":max_routed_agents", ":num_routed_agents_in_this_faction"),
						(assign, ":routed_party_faction", ":cur_faction"),
					(try_end),
					
					(party_set_faction, ":routed_party", ":routed_party_faction"),
					
					(party_set_ai_behavior, ":routed_party", ai_bhvr_travel_to_party),
					
					(assign, ":minimum_distance", 1000000),
					(try_for_parties, ":party_no"),
						(party_is_active, ":party_no"),
						(party_get_slot, ":cur_party_type", ":party_no", slot_party_type),
						(this_or_next|eq, ":cur_party_type", spt_town),
						(eq, ":cur_party_type", spt_castle),
						(store_faction_of_party, ":cur_faction", ":party_no"),
						(this_or_next|eq, ":routed_party_faction", "fac_neutral"),
						(eq, ":cur_faction", ":routed_party_faction"),
						(party_get_position, pos1, ":party_no"),
						(store_distance_to_party_from_party, ":dist", ":party_no", "p_main_party"),
						(try_begin),
							(lt, ":dist", ":minimum_distance"),
							(assign, ":minimum_distance", ":dist"),
							(assign, ":nearest_ally_city", ":party_no"),
						(try_end),
					(try_end),
					
					(party_get_position, pos1, "p_main_party"), #store position information of main party in pos1
					(party_get_position, pos2, ":nearest_ally_city"), #store position information of target city in pos2
					
					(assign, ":minimum_distance", 1000000),
					(try_for_range, ":unused", 0, 10),
						(map_get_random_position_around_position, pos3, pos1, 2), #store position of found random position (possible placing position for new routed party) around battle position in pos3
						(get_distance_between_positions, ":dist", pos2, pos3), #store distance between found position and target city in ":dist".
						(try_begin),
							(lt, ":dist", ":minimum_distance"),
							(assign, ":minimum_distance", ":dist"),
							(copy_position, pos63, pos3),
						(try_end),
					(end_try),
					
					(party_set_position, ":routed_party", pos63),
					
					(party_set_ai_object, ":routed_party", ":nearest_ally_city"),
					(party_set_flags, ":routed_party", pf_default_behavior, 1),
					
					#adding party members of p_routed_enemies to routed_party
					(party_clear, ":routed_party"),
					(party_get_num_companion_stacks, ":num_stacks", "p_routed_enemies"), #question, I changed (total_enemy_casualties) with (p_routed_enemies) because this is not prisoner in p_routed_enemies party.
					(try_for_range, ":stack_no", 0, ":num_stacks"),
						(party_stack_get_troop_id, ":stack_troop", "p_routed_enemies", ":stack_no"),
						(try_begin),
							(neg|troop_is_hero, ":stack_troop"), #do not add routed heroes to (new created) routed party for now.
							
							(party_stack_get_size, ":stack_size", "p_routed_enemies", ":stack_no"),
							(party_add_members, ":routed_party", ":stack_troop", ":stack_size"),
						(try_end),
					(try_end),
				(try_end),
		]) #ozan
		
		#script_inflict_casualties_to_party:
		# INPUT:
		# param1: Party-id
		# param2: number of rounds
		
		#OUTPUT:
		# This script doesn't return a value but populates the parties p_temp_wounded and p_temp_killed with the wounded and killed.
		#Example:
		#  (script_inflict_casualties_to_party, "_p_main_party" ,50),
		#  Simulate 50 rounds of casualties to main_party.
		
inflict_casualties_to_party = (
	"inflict_casualties_to_party",
			[
				(party_clear, "p_temp_casualties"),
				(store_script_param_1, ":party"), #Party_id
				(call_script, "script_party_count_fit_regulars", ":party"),
				(assign, ":num_fit", reg(0)), #reg(47) = number of fit regulars.
				(store_script_param_2, ":num_attack_rounds"), #number of attacks
				(try_for_range, ":unused", 0, ":num_attack_rounds"),
					(gt, ":num_fit", 0),
					(store_random_in_range, ":attacked_troop_rank", 0 , ":num_fit"), #attack troop with rank reg(46)
					(assign, reg1, ":attacked_troop_rank"),
					(call_script, "script_get_stack_with_rank", ":party", ":attacked_troop_rank"),
					(assign, ":attacked_stack", reg(0)), #reg(53) = stack no to attack.
					(party_stack_get_troop_id,     ":attacked_troop",":party",":attacked_stack"),
					(store_character_level, ":troop_toughness", ":attacked_troop"),
					(val_add, ":troop_toughness", 5),  #troop-toughness = level + 5
					(assign, ":casualty_chance", 10000),
					(val_div, ":casualty_chance", ":troop_toughness"), #dying chance
					(try_begin),
						(store_random_in_range, ":rand_num", 0 ,10000),
						(lt, ":rand_num", ":casualty_chance"), #check chance to be a casualty
						(store_random_in_range, ":rand_num2", 0, 2), #check if this troop will be wounded or killed
						(try_begin),
							(troop_is_hero,":attacked_troop"), #currently troop can't be a hero, but no harm in keeping this.
							(store_troop_health, ":troop_hp",":attacked_troop"),
							(val_sub, ":troop_hp", 45),
							(val_max, ":troop_hp", 1),
							(troop_set_health, ":attacked_troop", ":troop_hp"),
						(else_try),
							(lt, ":rand_num2", 1), #wounded
							(party_add_members, "p_temp_casualties", ":attacked_troop", 1),
							(party_wound_members, "p_temp_casualties", ":attacked_troop", 1),
							(party_wound_members, ":party", ":attacked_troop", 1),
						(else_try), #killed
							(party_add_members, "p_temp_casualties", ":attacked_troop", 1),
							(party_remove_members, ":party", ":attacked_troop", 1),
						(try_end),
						(val_sub, ":num_fit", 1), #adjust number of fit regulars.
					(try_end),
				(try_end),
		])


		#script_move_members_with_ratio:
		# INPUT:
		# param1: Source Party-id
		# param2: Target Party-id
		# pin_number = ratio of members to move, multiplied by 1000
		
		#OUTPUT:
		# This script doesn't return a value but moves some of the members of source party to target party according to the given ratio.
move_members_with_ratio = (
	"move_members_with_ratio",
			[
				(store_script_param_1, ":source_party"), #Source Party_id
				(store_script_param_2, ":target_party"), #Target Party_id
				(party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
				(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id,     ":stack_troop",":source_party",":stack_no"),
					(party_prisoner_stack_get_size,    ":stack_size",":source_party",":stack_no"),
					(store_mul, ":number_to_move",":stack_size","$pin_number"),
					(val_div, ":number_to_move", 1000),
					(party_remove_prisoners, ":source_party", ":stack_troop", ":number_to_move"),
					(assign, ":number_moved", reg0),
					(party_add_prisoners, ":target_party", ":stack_troop", ":number_moved"),
				(try_end),
				(party_get_num_companion_stacks, ":num_stacks",":source_party"),
				(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
					(party_stack_get_troop_id,     ":stack_troop",":source_party",":stack_no"),
					(party_stack_get_size,    ":stack_size",":source_party",":stack_no"),
					(store_mul, ":number_to_move",":stack_size","$pin_number"),
					(val_div, ":number_to_move", 1000),
					(party_remove_members, ":source_party", ":stack_troop", ":number_to_move"),
					(assign, ":number_moved", reg0),
					(party_add_members, ":target_party", ":stack_troop", ":number_moved"),
				(try_end),
		])
		
		# script_let_nearby_parties_join_current_battle
		# no longer behaves like native
		# WARNING : modified by 1257AD devs
		# Input: arg1 = besiege_mode, arg2 = dont_add_friends_other_than_accompanying
		# Output: none
let_nearby_parties_join_current_battle = (
	"let_nearby_parties_join_current_battle",
			[
				(store_script_param, ":besiege_mode", 1),
				(store_script_param, ":dont_add_friends_other_than_accompanying", 2),
				
				(store_character_level, ":player_level", "trp_player"),
				(try_for_parties, ":party_no"),
					# (neq, ":party_no", "$g_battle_preparation"),
					(party_is_active, ":party_no"),
					(party_get_battle_opponent, ":opponent",":party_no"),
					(lt, ":opponent", 0), #party is not itself involved in a battle
					(party_get_attached_to, ":attached_to",":party_no"),
					(lt, ":attached_to", 0), #party is not attached to another party
					(get_party_ai_behavior, ":behavior", ":party_no"),
					(neq, ":behavior", ai_bhvr_in_town),
					
					(party_stack_get_troop_id, ":stack_troop", ":party_no", 0),
					(try_begin),
						(neg|is_between, ":stack_troop", "trp_looter", "trp_black_khergit_horseman"),
						(assign, ":join_distance", 5), #day/not bandit - rafi reduced
						(try_begin),
							(is_currently_night),
							(assign, ":join_distance", 3), #nigh/not bandit - rafi reduced
						(try_end),
					(else_try),
						(assign, ":join_distance", 3), #day/bandit
						(try_begin),
							(is_currently_night),
							(assign, ":join_distance", 2), #night/bandit
						(try_end),
					(try_end),
					
					#Quest bandits do not join battle
					(this_or_next|neg|check_quest_active, "qst_track_down_bandits"),
					(neg|quest_slot_eq, "qst_track_down_bandits", slot_quest_target_party, ":party_no"),
					(this_or_next|neg|check_quest_active, "qst_troublesome_bandits"),
					(neg|quest_slot_eq, "qst_troublesome_bandits", slot_quest_target_party, ":party_no"),
					
					(store_distance_to_party_from_party, ":distance", ":party_no", "p_main_party"),
					(lt, ":distance", ":join_distance"),
					# (party_slot_eq, ":party_no", slot_party_battle_preparation, 1),
					# (try_begin),
					# (eq, "$g_battle_preparation_phase", 3),
					# (party_slot_eq, ":party_no", slot_party_battle_preparation, 1),
					# (party_set_slot, ":party_no", slot_party_battle_preparation, -1),
					# (try_end),
					
					(store_faction_of_party, ":faction_no", ":party_no"),
					(store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
					(try_begin),
						(eq, ":faction_no", "fac_player_supporters_faction"),
						(assign, ":reln_with_player", 100),
					(else_try),
						(store_relation, ":reln_with_player", ":faction_no", "fac_player_supporters_faction"),
					(try_end),
					(try_begin),
						(eq, ":faction_no", ":enemy_faction"),
						(assign, ":reln_with_enemy", 100),
					(else_try),
						(store_relation, ":reln_with_enemy", ":faction_no", ":enemy_faction"),
					(try_end),
					
					(assign, ":enemy_side", 1),
					(try_begin),
						(neq, "$g_enemy_party", "$g_encountered_party"),
						(assign, ":enemy_side", 2),
					(try_end),
					
					(try_begin),
						(eq, ":besiege_mode", 0),
						(lt, ":reln_with_player", 0),
						(gt, ":reln_with_enemy", 0),
						(party_get_slot, ":party_type", ":party_no"),
						
						(assign, ":enemy_is_bandit_party_and_level_is_greater_than_6", 0),
						(try_begin),
							(party_stack_get_troop_id, ":stack_troop", ":party_no", 0),
							(is_between, ":stack_troop", "trp_looter", "trp_black_khergit_horseman"),
							(gt, ":player_level", 6),
							(assign, ":enemy_is_bandit_party_and_level_is_greater_than_6", 1),
						(try_end),
						(party_get_template_id, ":template", ":party_no"),
						(this_or_next|eq, ":party_type", spt_kingdom_hero_party),
			(this_or_next|eq, ":party_type", spt_patrol), # tom
				(this_or_next|eq, ":template", "pt_mongolian_camp"),
				(this_or_next|eq, ":template", "pt_welsh"),
				(this_or_next|eq, ":template", "pt_guelphs"),
				(this_or_next|eq, ":template", "pt_ghibellines"),
				(this_or_next|eq, ":template", "pt_crusaders"),
				(this_or_next|eq, ":template", "pt_crusader_raiders"),
				(this_or_next|eq, ":template", "pt_jihadist_raiders"),
				(this_or_next|eq, ":template", "pt_teutonic_raiders"),
				(this_or_next|eq, ":template", "pt_curonians"),
				(this_or_next|eq, ":template", "pt_prussians"),
				(this_or_next|eq, ":template", "pt_samogitians"),
				(this_or_next|eq, ":template", "pt_yotvingians"),
				(this_or_next|eq, ":party_type", spt_merc_party),
						(eq, ":enemy_is_bandit_party_and_level_is_greater_than_6", 1),
						
						(get_party_ai_behavior, ":ai_bhvr", ":party_no"),
						(neq, ":ai_bhvr", ai_bhvr_avoid_party),
						#rafi
						(party_relocate_near_party, ":party_no", "p_main_party", 3),
						#rafi
						(party_quick_attach_to_current_battle, ":party_no", ":enemy_side"), #attach as enemy
						(str_store_party_name, s1, ":party_no"),
						(display_message, "str_s1_joined_battle_enemy"),
					(else_try),
						(try_begin),
							(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
							(party_slot_eq, ":party_no", slot_party_ai_object, "trp_player"),
							(assign, ":party_is_accompanying_player", 1),
						(else_try),
							(assign, ":party_is_accompanying_player", 0),
						(try_end),
						
						(this_or_next|eq, ":dont_add_friends_other_than_accompanying", 0),
						(eq, ":party_is_accompanying_player", 1),
						(gt, ":reln_with_player", 0),
						(lt, ":reln_with_enemy", 0),
						
						(assign, ":following_player", 0),
						(try_begin),
							(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
							(party_slot_eq, ":party_no", slot_party_ai_object, "p_main_party"),
							(assign, ":following_player", 1),
						(try_end),
						
						(assign, ":do_join", 1),
						(try_begin),
							(eq, ":besiege_mode", 1),
							(eq, ":following_player", 0),
							(assign, ":do_join", 0),
							(eq, ":faction_no", "$players_kingdom"),
							(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
							(assign, ":do_join", 1),
						(try_end),
						(eq, ":do_join", 1),
						
						(party_get_slot, ":party_type", ":party_no"),
						(eq, ":party_type", spt_kingdom_hero_party),
						(party_stack_get_troop_id, ":leader", ":party_no", 0),
						#(troop_get_slot, ":player_relation", ":leader", slot_troop_player_relation),
						(call_script, "script_troop_get_player_relation", ":leader"),
						(assign, ":player_relation", reg0),
						
						(assign, ":join_even_you_do_not_like_player", 0),
						(try_begin),
							(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"), #new added, if player is marshal and if he is accompanying then join battle even lord do not like player
							(eq, ":following_player", 1),
							(assign, ":join_even_you_do_not_like_player", 1),
						(try_end),
						
						(this_or_next|ge, ":player_relation", 0),
						(eq, ":join_even_you_do_not_like_player", 1),
						#rafi
						(party_relocate_near_party, ":party_no", "p_main_party", 3),
						#rafi
						(party_quick_attach_to_current_battle, ":party_no", 0), #attach as friend
						(str_store_party_name, s1, ":party_no"),
						(display_message, "str_s1_joined_battle_friend"),
			(else_try), ## various parties join in
			
				(party_get_template_id, ":template", ":party_no"),
			(this_or_next|eq, ":party_type", spt_patrol), # tom
				(this_or_next|eq, ":template", "pt_mongolian_camp"),
				(this_or_next|eq, ":template", "pt_welsh"),
				(this_or_next|eq, ":template", "pt_guelphs"),
				(this_or_next|eq, ":template", "pt_ghibellines"),
				(this_or_next|eq, ":template", "pt_crusaders"),
				(this_or_next|eq, ":template", "pt_crusader_raiders"),
				(this_or_next|eq, ":template", "pt_jihadist_raiders"),
				(this_or_next|eq, ":template", "pt_teutonic_raiders"),
				(this_or_next|eq, ":template", "pt_curonians"),
				(this_or_next|eq, ":template", "pt_prussians"),
				(this_or_next|eq, ":template", "pt_samogitians"),
				(this_or_next|eq, ":template", "pt_yotvingians"),
				(eq, ":party_type", spt_merc_party),
			
			(try_begin),
							(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
							(party_slot_eq, ":party_no", slot_party_ai_object, "trp_player"),
							(assign, ":party_is_accompanying_player", 1),
						(else_try),
							(assign, ":party_is_accompanying_player", 0),
						(try_end),
						
						(this_or_next|eq, ":dont_add_friends_other_than_accompanying", 0),
						(eq, ":party_is_accompanying_player", 1),
						(gt, ":reln_with_player", 0),
						(lt, ":reln_with_enemy", 0),
			(party_relocate_near_party, ":party_no", "p_main_party", 3),
			(party_quick_attach_to_current_battle, ":party_no", 0), #attach as friend
						(str_store_party_name, s1, ":party_no"),
						(display_message, "str_s1_joined_battle_friend"),
					(try_end),
			
				(try_end),
		])
		
		# script_party_wound_all_members_aux
		# Input: arg1 = party_no
party_wound_all_members_aux = (
	"party_wound_all_members_aux",
			[
				(store_script_param_1, ":party_no"),
				
				(party_get_num_companion_stacks, ":num_stacks",":party_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
					(try_begin),
						(neg|troop_is_hero, ":stack_troop"),
						(party_stack_get_size, ":stack_size",":party_no",":i_stack"),
						(party_wound_members, ":party_no", ":stack_troop", ":stack_size"),
					(else_try),
						(troop_set_health, ":stack_troop", 0),
					(try_end),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
					(call_script, "script_party_wound_all_members_aux", ":attached_party"),
				(try_end),
		])
		
		# script_party_wound_all_members
		# Input: arg1 = party_no
party_wound_all_members = (
	"party_wound_all_members",
			[
				(store_script_param_1, ":party_no"),
				
				(call_script, "script_party_wound_all_members_aux", ":party_no"),
		])
		
		# script_cf_reinforce_party 
		# new tom  should no longer be used for lord parties reinforcement.
		# Can fail.
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = party_no,
		# Output: none
		# Adds reinforcement to party according to its type and faction
		# Called from several places, simple_triggers for centers, script_hire_men_to_kingdom_hero_party for hero parties
cf_reinforce_party = (
	"cf_reinforce_party",
		[
			(store_script_param_1, ":party_no"),
			(store_faction_of_party, ":party_faction", ":party_no"),
			#(party_get_slot, ":party_type",":party_no", slot_party_type),
			(party_get_slot, ":party_faction", ":party_no", slot_center_original_faction),
			# (try_begin),
				# (eq, ":party_faction", "fac_player_supporters_faction"),
				# (try_begin),
					# (is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
					# (assign, ":party_faction", "$g_player_culture"),
				# (else_try),
					# (party_get_slot, ":party_faction", ":party_no", slot_center_original_faction),
				# (try_end),
			# (try_end),
			(try_begin),
				(eq, ":party_no", "p_main_party"),
				(assign, ":party_faction", "fac_kingdom_31"),
			(try_end),
			(faction_get_slot, ":party_template_a", ":party_faction", slot_faction_reinforcements_a),
				(faction_get_slot, ":party_template_b", ":party_faction", slot_faction_reinforcements_b),
				(faction_get_slot, ":party_template_c", ":party_faction", slot_faction_reinforcements_c),
		
			(try_begin), #town/castle
				(is_between, ":party_no", centers_begin, centers_end),
					(party_get_slot, ":company_template", ":party_no", slot_regional_party_template),
					(party_get_slot, ":special1", ":party_no", slot_spec_mercs1),
					(party_get_slot, ":special2", ":party_no", slot_spec_mercs2),
					(store_random_in_range, ":random", 0, 3),
					(try_begin),
						(eq, ":random", 1),
						(gt, ":special1", 0),
							(party_get_slot, ":company_template", ":party_no", slot_spec_mercs1_party_template),
					(else_try),
						(eq, ":random", 2),
						(gt, ":special2", 0),
							(party_get_slot, ":company_template", ":party_no", slot_spec_mercs2_party_template),
					(try_end),
			(try_end), 
		
			(try_begin),
				(is_between, ":party_no", centers_begin, centers_end),
					(store_random_in_range, ":recruit_what", 0, 2),
					(try_begin), 
						(eq, ":recruit_what", 0),
							# (party_add_template, ":party_no", ":party_template_a"),
							# (party_add_template, ":party_no", ":party_template_b"),
							# (party_add_template, ":party_no", ":party_template_c"),
							(call_script, "script_fill_lance", ":party_no", ":party_no"),
					(else_try),#template
						(eq, ":recruit_what", 1),
							(party_add_template, ":party_no", ":company_template"),
					# (else_try), #lance
						# (eq, ":recruit_what", 2),
							# (call_script, "script_fill_lance", ":party_no", ":party_no"),
					(try_end),
			(else_try), #if regular party just add shit
				(party_add_template, ":party_no", ":party_template_a"),
				(party_add_template, ":party_no", ":party_template_b"),
				(party_add_template, ":party_no", ":party_template_c"),
			(try_end),
				(call_script, "script_party_calculate_strength", ":party_no", 1, 0),
		])

		
		#script_kill_cattle_from_herd
		# Input: arg1 = party_no, arg2 = amount
		# Output: none (fills trp_temp_troop's inventory)
kill_cattle_from_herd = (
	"kill_cattle_from_herd",
			[
				(store_script_param_1, ":party_no"),
				(store_script_param_2, ":amount"),
				
				(troop_clear_inventory, "trp_temp_troop"),
				(store_mul, ":meat_amount", ":amount", 2),
				(troop_add_items, "trp_temp_troop", "itm_cattle_meat", ":meat_amount"),
				
				(troop_get_inventory_capacity, ":inv_size", "trp_temp_troop"),
				(try_for_range, ":i_slot", 0, ":inv_size"),
					(troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
					(eq, ":item_id", "itm_cattle_meat"),
					(troop_set_inventory_slot_modifier, "trp_temp_troop", ":i_slot", imod_fresh),
				(try_end),
				
				(party_get_num_companions, ":num_cattle", ":party_no"),
				(try_begin),
					(ge, ":amount", ":num_cattle"),
					(remove_party, ":party_no"),
				(else_try),
					(party_remove_members, ":party_no", "trp_cattle", ":amount"),
				(try_end),
		])
		
		# script_party_set_ai_state
		# sets party AI state
		# Redone somewhat on Feb 18 to make sure that initative is set properly
		# WARNING: modified by 1257AD devs
		# Input: arg1 = party_no, arg2 = new_ai_state, arg3 = action_object (if necessary)
		# Output: none (Can fail)
party_set_ai_state = (
	"party_set_ai_state",
			[
		 
				(store_script_param, ":party_no", 1),
				(store_script_param, ":new_ai_state", 2),
				(store_script_param, ":new_ai_object", 3),
		
				(party_get_slot, ":old_ai_state", ":party_no", slot_party_ai_state),
				(party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
				(party_get_attached_to, ":attached_to_party", ":party_no"),
				(assign, ":party_is_in_town", 0),
				(try_begin),
					(is_between, ":attached_to_party", centers_begin, centers_end),
					(assign, ":party_is_in_town", ":attached_to_party"),
				(try_end),
				
				(assign, ":commander", -1),
				(try_begin),
					(party_is_active, ":party_no"),
					(party_stack_get_troop_id, ":commander", ":party_no", 0),
					(store_faction_of_party, ":faction_no", ":party_no"),
				(try_end),
				
				(try_begin),
					(lt, ":commander", 0),
					#sometimes 0 sized parties enter "party_set_ai_state" script. So only discard them
					#(try_begin),
					#  (eq, "$cheat_mode", 1),
					#  (str_store_troop_name, s6, ":party_no"),
					#  (party_get_num_companions, reg6, ":party_no"),
					#  (display_message, "@{!}DEBUGS : party name is : {s6}, party size is : {reg6}, new ai discarded."),
					#(try_end),
				(else_try),
					#Party does any business in town
					(try_begin),
						(is_between, ":party_is_in_town", walled_centers_begin, walled_centers_end),
						(party_slot_eq, ":party_is_in_town", slot_center_is_besieged_by, -1),
						(call_script, "script_troop_does_business_in_center", ":commander", ":party_is_in_town"),
					(else_try),
						(party_slot_eq, ":party_no", slot_party_ai_state, spai_visiting_village),
						(party_get_slot, ":party_is_in_village", ":party_no", slot_party_ai_object),
						(is_between, ":party_is_in_village", villages_begin, villages_end),
						#(party_slot_eq, ":party_is_in_village", slot_center_is_looted_by, -1),
						(neg|party_slot_eq, ":party_is_in_village", slot_village_state, svs_being_raided),
						(neg|party_slot_eq, ":party_is_in_village", slot_village_state, svs_looted),
						(store_distance_to_party_from_party, ":distance", ":party_no", ":party_is_in_village"),
						(lt, ":distance", 3),
						(call_script, "script_troop_does_business_in_center", ":commander", ":party_is_in_village"),
					(try_end),
					
					(party_set_slot, ":party_no", slot_party_follow_me, 0),
					
					(try_begin),
						(eq, ":old_ai_state", ":new_ai_state"),
						(eq, ":old_ai_object", ":new_ai_object"),
						#do nothing. Nothing is changed.
					(else_try),
						(assign, ":initiative", 100),
						(assign, ":aggressiveness", 8),
						(assign, ":courage", 8),
						
						(try_begin),
							(this_or_next|eq, ":new_ai_state", spai_accompanying_army),
							(eq, ":new_ai_state", spai_screening_army),
							(party_set_ai_behavior, ":party_no", ai_bhvr_escort_party),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(party_detach, ":party_no"),
							(try_end),
							
							(try_begin),
								(eq, ":new_ai_state", spai_screening_army),
								(assign, ":aggressiveness", 9),
								(assign, ":courage", 9),
								(assign, ":initiative", 80),
							(else_try),
								(assign, ":aggressiveness", 6),
								(assign, ":courage", 9),
								(assign, ":initiative", 10),
							(try_end),
						(else_try),
							(eq, ":new_ai_state", spai_besieging_center),
							(party_get_position, pos1, ":new_ai_object"),
							(map_get_random_position_around_position, pos2, pos1, 2),
							(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
							(party_set_ai_target_position, ":party_no", pos2),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							(party_set_slot, ":party_no", slot_party_follow_me, 1),
							(party_set_slot, ":party_no", slot_party_ai_substate, 0),
							
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(neq, ":party_is_in_town", ":new_ai_object"),
								(party_detach, ":party_no"),
							(try_end),
							
							(assign, ":aggressiveness", 1),
							(assign, ":courage", 9),
							(assign, ":initiative", 20),
							#(assign, ":initiative", 100),
						(else_try),
							(eq, ":new_ai_state", spai_holding_center),
							(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(neq, ":party_is_in_town", ":new_ai_object"),
								(party_detach, ":party_no"),
							(try_end),
							
							(assign, ":aggressiveness", 7),
							(assign, ":courage", 9),
							(assign, ":initiative", 100),
							#(party_set_ai_initiative, ":party_no", 99),
						(else_try),
							(eq, ":new_ai_state", spai_patrolling_around_center),
							(party_get_position, pos1, ":new_ai_object"),
							(map_get_random_position_around_position, pos2, pos1, 1),
							(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
							(party_set_ai_target_position, ":party_no", pos2),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							
							(try_begin),
								(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
								(party_set_ai_patrol_radius, ":party_no", 1), #line 100
							(else_try),
								(party_set_ai_patrol_radius, ":party_no", 5), #line 100
							(try_end),
							
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							(party_set_slot, ":party_no", slot_party_follow_me, 1),
							(party_set_slot, ":party_no", slot_party_ai_substate, 0),
							
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(party_detach, ":party_no"),
							(try_end),
							
							(try_begin),
								#new to avoid losing time of marshal with attacking unimportant targets while there is a threat in our centers.
								(ge, ":commander", 0),
								(faction_slot_eq, ":faction_no", slot_faction_marshall, ":commander"),
								(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
								
								(party_get_position, pos3, ":party_no"),
								(get_distance_between_positions, ":distance_to_center", pos1, pos3),
								(try_begin),
									(ge, ":distance_to_center", 800), #added new (1.122)
									(assign, ":initiative", 10),
									(assign, ":aggressiveness", 1),
									(assign, ":courage", 8),
								(else_try), #below added new (1.122)
									(assign, ":initiative", 100),
									(assign, ":aggressiveness", 8),
									(assign, ":courage", 8),
								(try_end),
							(else_try),
								(assign, ":aggressiveness", 8),
								(assign, ":courage", 8),
								(assign, ":initiative", 100),
							(try_end),
						(else_try),
							(eq, ":new_ai_state", spai_visiting_village),
							(party_get_position, pos1, ":new_ai_object"),
							(map_get_random_position_around_position, pos2, pos1, 2),
							(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
							(party_set_ai_target_position, ":party_no", pos2),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							(party_set_slot, ":party_no", slot_party_ai_substate, 0),
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(neq, ":party_is_in_town", ":new_ai_object"),
								(party_detach, ":party_no"),
							(try_end),
							
							(assign, ":aggressiveness", 8),
							(assign, ":courage", 8),
							(assign, ":initiative", 100),
						(else_try), #0.660: this is where the 1625/1640 bugs happen with an improper ai_object
							(eq, ":new_ai_state", spai_raiding_around_center),
							(party_get_position, pos1, ":new_ai_object"),
							(map_get_random_position_around_position, pos2, pos1, 1),
							(party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
							(party_set_ai_patrol_radius, ":party_no", 10),
							(party_set_ai_target_position, ":party_no", pos2),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							(party_set_slot, ":party_no", slot_party_follow_me, 1),
							(party_set_slot, ":party_no", slot_party_ai_substate, 0),
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(neq, ":party_is_in_town", ":new_ai_object"),
								(party_detach, ":party_no"),
							(try_end),
							
							(try_begin),
								(ge, ":commander", 0),
								(faction_slot_eq, ":faction_no", slot_faction_marshall, ":commander"),
								(assign, ":aggressiveness", 1),
								(assign, ":courage", 8),
								(assign, ":initiative", 20),
							(else_try),
								(assign, ":aggressiveness", 7),
								(assign, ":courage", 8),
								(assign, ":initiative", 100),
							(try_end),
						(else_try),
							(eq, ":new_ai_state", spai_engaging_army),
							(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(party_detach, ":party_no"),
							(try_end),
							
							(try_begin),
								#new to avoid losing time of marshal with attacking unimportant targets while there is a threat in our centers.
								(ge, ":commander", 0),
								(faction_slot_eq, ":faction_no", slot_faction_marshall, ":commander"),
								(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
								(assign, ":initiative", 10),
								(assign, ":aggressiveness", 1),
								(assign, ":courage", 8),
							(else_try),
								(assign, ":aggressiveness", 8),
								(assign, ":courage", 8),
								(assign, ":initiative", 100),
							(try_end),
						(else_try),
							(eq, ":new_ai_state", spai_retreating_to_center),
							(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
							(party_set_ai_object, ":party_no", ":new_ai_object"),
							(party_set_flags, ":party_no", pf_default_behavior, 1),
							(party_set_slot, ":party_no", slot_party_commander_party, -1),
							(try_begin),
								(gt, ":party_is_in_town", 0),
								(neq, ":party_is_in_town", ":new_ai_object"),
								(party_detach, ":party_no"),
							(try_end),
							
							(assign, ":aggressiveness", 3),
							(assign, ":courage", 4),
							(assign, ":initiative", 100),
						(else_try),
							(eq, ":new_ai_state", spai_undefined),
							(party_set_ai_behavior, ":party_no", ai_bhvr_hold),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
						(try_end),
						
						(try_begin),
							(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_martial),
							(val_add, ":aggressiveness", 2),
							(val_add, ":courage", 2),
						(else_try),
							(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_debauched),
							(val_sub, ":aggressiveness", 1),
							(val_sub, ":courage", 1),
						(try_end),
			
						(party_set_slot, ":party_no", slot_party_ai_state, ":new_ai_state"),
						(party_set_slot, ":party_no", slot_party_ai_object, ":new_ai_object"),
						(party_set_aggressiveness, ":party_no", ":aggressiveness"), 
						(party_set_courage, ":party_no", ":courage"), 

						(party_set_ai_initiative, ":party_no", ":initiative"),
					(try_end),
				(try_end),
				
				#Helpfulness
				(try_begin),
					(ge, ":commander", 0),
					
					(party_set_helpfulness, ":party_no", 101),
					(try_begin), #tom below check is from bellow
						(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
						(party_set_helpfulness, ":party_no", 10000), #tom 110
					(else_try),
						(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_martial),
						(party_set_helpfulness, ":party_no", 200),
					(else_try),
						(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_upstanding),
						(party_set_helpfulness, ":party_no", 150),
					# (else_try), #tom this is now a priority in the begining
						# (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
						# (party_set_helpfulness, ":party_no", 110), 
					(else_try),
						(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_quarrelsome),
						(party_set_helpfulness, ":party_no", 90),
					(else_try),
						(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_selfrighteous),
						(party_set_helpfulness, ":party_no", 80),
					(else_try),
						(troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_debauched),
						(party_set_helpfulness, ":party_no", 50),
					(try_end),
				(try_end),
		])
		
		
		# script_change_player_relation_with_center
		# Input: arg1 = party_no, arg2 = relation difference
		# Output: none
change_player_relation_with_center = (
	"change_player_relation_with_center",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":difference"),
				
				(party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
				(assign, reg1, ":player_relation"),
				(val_add, ":player_relation", ":difference"),
				(val_clamp, ":player_relation", -100, 100),
				(assign, reg2, ":player_relation"),
				(party_set_slot, ":center_no", slot_center_player_relation, ":player_relation"),
				
				(try_begin),
					(le, ":player_relation", -50),
					(unlock_achievement, ACHIEVEMENT_OLD_DIRTY_SCOUNDREL),
				(try_end),
				
				
				(str_store_party_name_link, s1, ":center_no"),
				(try_begin),
					(gt, ":difference", 0),
					(display_message, "@Your relation with {s1} has improved."),
				(else_try),
					(lt, ":difference", 0),
					(display_message, "@Your relation with {s1} has deteriorated."),
				(try_end),
				(try_begin),
			(eq, "$use_feudal_lance", 0), #lance recruitment thing
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(call_script, "script_update_volunteer_troops_in_village", ":center_no"),
				(try_end),
				
				(try_begin),
					(this_or_next|is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
					(is_between, "$g_talk_troop", mayors_begin, mayors_end),
					(assign, "$g_talk_troop_relation", ":player_relation"),
					(call_script, "script_setup_talk_info"),
				(try_end),
		])
		

		# script_party_calculate_and_set_nearby_friend_enemy_follower_strengths
		# WARNING: modified by 1257AD faction
		# Input: party_no
		# Output: none
party_calculate_and_set_nearby_friend_enemy_follower_strengths = (
	"party_calculate_and_set_nearby_friend_enemy_follower_strengths",
			[
				(store_script_param, ":party_no", 1),
				(assign, ":follower_strength", 0),
				(assign, ":friend_strength", 0),
				(assign, ":enemy_strength", 0),
				(store_faction_of_party, ":party_faction", ":party_no"),
				
				(store_add, ":end_cond", active_npcs_end, 1),
				(try_for_range, ":iteration", active_npcs_begin, ":end_cond"),
					(try_begin),
						(eq, ":iteration", active_npcs_end),
						(assign, ":cur_troop", "trp_player"),
					(else_try),
						(assign, ":cur_troop", ":iteration"),
					(try_end),
					
					(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
					(troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
					(ge, ":cur_troop_party", 0),
					(party_is_active, ":cur_troop_party"),
					
					
					#I moved these lines here from (*1) to faster process, ozan.
					(store_troop_faction, ":army_faction", ":cur_troop"),
					(store_relation, ":relation", ":army_faction", ":party_faction"),
					(this_or_next|neq, ":relation", 0),
					(eq, ":army_faction", ":party_faction"),
					#ozan end
					
					
					(neq, ":party_no", ":cur_troop_party"),
					(party_get_slot, ":str", ":cur_troop_party", slot_party_cached_strength),
					(try_begin),
						(neg|is_between, ":party_no", centers_begin, centers_end),
						(party_slot_eq, ":cur_troop_party", slot_party_ai_state, spai_accompanying_army),
						(party_get_slot, ":commander_party", ":cur_troop_party", slot_party_ai_object),
						(eq, ":commander_party", ":party_no"),
						(val_add, ":follower_strength", ":str"),
					(else_try),
						(store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":party_no"),
						(lt, ":distance", 20),
						
						#(*1)
						
						(try_begin),
							(lt, ":distance", 5),
							(assign, ":str_divided", ":str"),
						(else_try),
							(lt, ":distance", 10),
							(store_div, ":str_divided", ":str", 2),
						(else_try),
							(lt, ":distance", 15),
							(store_div, ":str_divided", ":str", 4),
						(else_try),
							(store_div, ":str_divided", ":str", 8),
						(try_end),
						
						(try_begin),
							(this_or_next|eq, ":army_faction", ":party_faction"),
							(gt, ":relation", 0),
							(val_add, ":friend_strength", ":str_divided"),
						(else_try),
							(lt, ":relation", 0),
							(val_add, ":enemy_strength", ":str_divided"),
						(try_end),
					(try_end),
				(try_end),
				
				(party_set_slot, ":party_no", slot_party_follower_strength, ":follower_strength"),
				(party_set_slot, ":party_no", slot_party_nearby_friend_strength, ":friend_strength"),
				(party_set_slot, ":party_no", slot_party_nearby_enemy_strength, ":enemy_strength"),
		])


		#script_upgrade_hero_party
		# INPUT: arg1 = party_id, arg2 = xp_amount
upgrade_hero_party = (
	"upgrade_hero_party",
			[
				(store_script_param, ":party_no", 1),
				(store_script_param, ":xp_amount", 2),
				(party_upgrade_with_xp, ":party_no", ":xp_amount", 0),
		])


		# script_randomly_make_prisoner_heroes_escape_from_party
		# Input: arg1 = party_no, arg2 = escape_chance_mul_1000
		# Output: none
randomly_make_prisoner_heroes_escape_from_party = (
	"randomly_make_prisoner_heroes_escape_from_party",
			[(store_script_param, ":party_no", 1),
				(store_script_param, ":escape_chance", 2),
				(assign, ":quest_troop_1", -1),
				(assign, ":quest_troop_2", -1),
				(try_begin),
					(check_quest_active, "qst_rescue_lord_by_replace"),
					(quest_get_slot, ":quest_troop_1", "qst_rescue_lord_by_replace", slot_quest_target_troop),
				(try_end),
				(try_begin),
					(check_quest_active, "qst_deliver_message_to_prisoner_lord"),
					(quest_get_slot, ":quest_troop_2", "qst_deliver_message_to_prisoner_lord", slot_quest_target_troop),
				(try_end),
				(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
				(try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(neq, ":stack_troop", ":quest_troop_1"),
					(neq, ":stack_troop", ":quest_troop_2"),
					(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
					(store_random_in_range, ":random_no", 0, 1000),
					(lt, ":random_no", ":escape_chance"),
					(party_remove_prisoners, ":party_no", ":stack_troop", 1),
					(call_script, "script_remove_troop_from_prison", ":stack_troop"),
					(str_store_troop_name_link, s1, ":stack_troop"),
					(try_begin),
						(eq, ":party_no", "p_main_party"),
						(str_store_string, s2, "@your party"),
					(else_try),
						(str_store_party_name, s2, ":party_no"),
					(try_end),
					(assign, reg0, 0),
					(try_begin),
						(this_or_next|eq, ":party_no", "p_main_party"),
						(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
						(assign, reg0, 1),
					(try_end),
					(store_troop_faction, ":troop_faction", ":stack_troop"),
					(str_store_faction_name_link, s3, ":troop_faction"),
					(display_message, "@{reg0?One of your prisoners, :}{s1} of {s3} has escaped from captivity!"),
				(try_end),
		])