from header import *

# script_change_player_relation_with_faction
		# Input: arg1 = faction_no, arg2 = relation difference
		# Output: none
change_player_relation_with_faction = (
	"change_player_relation_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(store_script_param_2, ":difference"),
				
				(store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
				(assign, reg1, ":player_relation"),
				(val_add, ":player_relation", ":difference"),
				(assign, reg2, ":player_relation"),
				(set_relation, ":faction_no", "fac_player_faction", ":player_relation"),
				(set_relation, ":faction_no", "fac_player_supporters_faction", ":player_relation"),
				
				(try_begin),
					(le, ":player_relation", -50),
					(unlock_achievement, ACHIEVEMENT_OLD_DIRTY_SCOUNDREL),
				(try_end),
				
				
				(str_store_faction_name_link, s1, ":faction_no"),
				(try_begin),
					(gt, ":difference", 0),
					(display_message, "str_faction_relation_increased"),
				(else_try),
					(lt, ":difference", 0),
					(display_message, "str_faction_relation_detoriated"),
				(try_end),
				(call_script, "script_update_all_notes"),
		])
		

		# script_set_player_relation_with_faction
		# Input: arg1 = faction_no, arg2 = relation
		# Output: none
set_player_relation_with_faction = (
	"set_player_relation_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(store_script_param_2, ":relation"),
				
				(store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
				(store_sub, ":reln_dif", ":relation", ":player_relation"),
				(call_script, "script_change_player_relation_with_faction", ":faction_no", ":reln_dif"),
		])


		# script_change_player_relation_with_faction_ex
		# changes relations with other factions also (according to their relations between each other)
		# Input: arg1 = faction_no, arg2 = relation difference
		# Output: none
change_player_relation_with_faction_ex = (
	"change_player_relation_with_faction_ex",
			[
				(store_script_param_1, ":faction_no"),
				(store_script_param_2, ":difference"),
				
				(store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
				(assign, reg1, ":player_relation"),
				(val_add, ":player_relation", ":difference"),
				(assign, reg2, ":player_relation"),
				(set_relation, ":faction_no", "fac_player_faction", ":player_relation"),
				(set_relation, ":faction_no", "fac_player_supporters_faction", ":player_relation"),
				
				(str_store_faction_name_link, s1, ":faction_no"),
				(try_begin),
					(gt, ":difference", 0),
					(display_message, "str_faction_relation_increased"),
				(else_try),
					(lt, ":difference", 0),
					(display_message, "str_faction_relation_detoriated"),
				(try_end),
				
				(try_for_range, ":other_faction", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":other_faction", slot_faction_state, sfs_active),
					(neq, ":faction_no", ":other_faction"),
					(store_relation, ":other_faction_relation", ":faction_no", ":other_faction"),
					(store_relation, ":player_relation", ":other_faction", "fac_player_supporters_faction"),
					(store_mul, ":relation_change", ":difference", ":other_faction_relation"),
					(val_div, ":relation_change", 100),
					(val_add, ":player_relation", ":relation_change"),
					(set_relation, ":other_faction", "fac_player_faction", ":player_relation"),
					(set_relation, ":other_faction", "fac_player_supporters_faction", ":player_relation"),
				(try_end),
				(try_begin),
					(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
					(try_for_range, ":kingdom_no", kingdoms_begin, kingdoms_end),
						(faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active),
						(call_script, "script_update_faction_notes", ":kingdom_no"),
					(try_end),
				(try_end),
		])

		
		# script_make_kingdom_hostile_to_player
		# Input: arg1 = faction_no, arg2 = relation difference
		# Output: none
make_kingdom_hostile_to_player = (
	"make_kingdom_hostile_to_player",
			[
				(store_script_param_1, ":kingdom_no"),
				(store_script_param_2, ":difference"),
				
				(try_begin),
					(lt, ":difference", 0),
					(store_relation, ":player_relation", ":kingdom_no", "fac_player_supporters_faction"),
					(val_min, ":player_relation", 0),
					(val_add, ":player_relation", ":difference"),
					(call_script, "script_set_player_relation_with_faction", ":kingdom_no", ":player_relation"),
				(try_end),
		])
		
		
		# script_exchange_prisoners_between_factions
		# Input: arg1 = faction_no_1, arg2 = faction_no_2
exchange_prisoners_between_factions = (
	"exchange_prisoners_between_factions",
			[
				(store_script_param_1, ":faction_no_1"),
				(store_script_param_2, ":faction_no_2"),
				(assign, ":faction_no_3", -1),
				(assign, ":faction_no_4", -1),
				(assign, ":free_companions_too", 0),
				(try_begin),
					(this_or_next|eq, "$players_kingdom", ":faction_no_1"),
					(eq, "$players_kingdom", ":faction_no_2"),
					(assign, ":faction_no_3", "fac_player_faction"),
					(assign, ":faction_no_4", "fac_player_supporters_faction"),
					(assign, ":free_companions_too", 1),
				(try_end),
				
				(try_for_parties, ":party_no"),
					(store_faction_of_party, ":party_faction", ":party_no"),
					(this_or_next|eq, ":party_faction", ":faction_no_1"),
					(this_or_next|eq, ":party_faction", ":faction_no_2"),
					(this_or_next|eq, ":party_faction", ":faction_no_3"),
					(eq, ":party_faction", ":faction_no_4"),
					(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
					(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
						(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
						
						(assign, ":continue", 0),
						(try_begin),
							(is_between, ":cur_troop_id", companions_begin, companions_end),
							(eq, ":free_companions_too", 1),
							(assign, ":continue", 1),
						(else_try),
							(neg|is_between, ":cur_troop_id", companions_begin, companions_end),
							(store_troop_faction, ":cur_faction", ":cur_troop_id"),
							(this_or_next|eq, ":cur_faction", ":faction_no_1"),
							(this_or_next|eq, ":cur_faction", ":faction_no_2"),
							(this_or_next|eq, ":cur_faction", ":faction_no_3"),
							(eq, ":cur_faction", ":faction_no_4"),
							(assign, ":continue", 1),
						(try_end),
						(eq, ":continue", 1),
						
						(try_begin),
							(troop_is_hero, ":cur_troop_id"),
							(call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
						(try_end),
						(party_prisoner_stack_get_size, ":stack_size", ":party_no", ":troop_iterator"),
						(party_remove_prisoners, ":party_no", ":cur_troop_id", ":stack_size"),
					(try_end),
				(try_end),
				
		])


	#script_evaluate_realm_stability
	#NOTE: this calculates the average number of rivalries per lord, giving a rough indication of how easily a faction may be divided
	#	   fairly expensive in terms of CPU
	#INPUT: realm 
	#OUTPUT: none
evaluate_realm_stability = (
	"evaluate_realm_stability",
		
		[
		(store_script_param, ":realm", 1),
		
		(assign, ":total_lords", 0),
		(assign, ":total_restless_lords", 0),
		(assign, ":total_disgruntled_lords", 0),
		
		(faction_get_slot, ":liege", ":realm", slot_faction_leader),
		
		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_troop_faction, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":realm"),
			(val_add, ":total_lords", 1),
			
			(call_script, "script_calculate_troop_political_factors_for_liege", ":lord", ":liege"),
			(try_begin),
			(le, reg3, -10),
			(val_add, ":total_disgruntled_lords", 1),
			(else_try),
			(le, reg3, 10),
			(val_add, ":total_restless_lords", 1),
			(try_end),
		(try_end),
		
		(try_begin),
			(gt, ":total_lords", 0),
			(store_mul, ":instability_quotient", ":total_disgruntled_lords", 100),
			(val_div, ":instability_quotient", ":total_lords"),
			
			(store_mul, ":restless_quotient", ":total_restless_lords", 100),
			(val_div, ":restless_quotient", ":total_lords"),
			
			(store_mul, ":combined_quotient", ":instability_quotient", 2),
			(val_add, ":combined_quotient", ":restless_quotient"),
			(faction_set_slot, ":realm", slot_faction_instability, ":combined_quotient"),
			
			(assign, reg0, ":instability_quotient"),
			(assign, reg1, ":restless_quotient"),
			(assign, reg1, ":restless_quotient"),
		(else_try),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_faction_name, s1, ":realm"),
			(display_message, "str_s1_has_no_lords"),
			(try_end),
			(assign, reg0, 0),
			(assign, reg1, 0),
		(try_end),
		
	])

	#script_appoint_faction_marshall
	#INPUT: faction_no, faction_marshall
	#OUTPUT: NONE
appoint_faction_marshall = (
	"appoint_faction_marshall",
		[
		(store_script_param, ":faction_no", 1),
		(store_script_param, ":faction_marshall", 2),
		
		
		(faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
		(faction_get_slot, ":old_marshall", ":faction_no", slot_faction_marshall),
		
		(faction_set_slot, ":faction_no", slot_faction_marshall, ":faction_marshall"),
		
		(try_begin),
			(ge, ":old_marshall", 0),
			(troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
			(party_is_active, ":old_marshall_party"),
			(party_set_marshall, ":old_marshall_party", 0),
		(try_end),
		
		
		(try_begin),
			(ge, ":faction_marshall", 0),
			(troop_get_slot, ":new_marshall_party", ":faction_marshall", slot_troop_leaded_party),
			(party_is_active, ":new_marshall_party"),
			(party_set_marshall,":new_marshall_party", 1),
		(try_end),
		
		
		(try_begin),
			(neq, ":faction_marshall", ":faction_leader"),
			(neq, ":faction_marshall", ":old_marshall"),
			(this_or_next|eq, ":faction_marshall", "trp_player"),
			(is_between, ":faction_marshall", active_npcs_begin, active_npcs_end),
			
			(this_or_next|neq, ":faction_no", "fac_player_supporters_faction"),
			(neg|check_quest_active, "qst_rebel_against_kingdom"),
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_faction_name, s15, ":faction_no"),
			(display_message, "str_checking_lord_reactions_in_s15"),
			(try_end),
			
			
			(call_script, "script_troop_change_relation_with_troop", ":faction_marshall", ":faction_leader", 5),
			(val_add, "$total_promotion_changes", 5),
			
			(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":faction_no"),
			
			(neq, ":lord", ":faction_marshall"),
			(neq, ":lord", ":faction_leader"),
			
			(call_script, "script_troop_get_relation_with_troop", ":faction_marshall", ":lord"),
			#			(try_begin),
			#				(eq, "$cheat_mode", 1),
			#				(str_store_troop_name, s14, ":lord"),
			#				(str_store_troop_name, s17, ":faction_marshall"),
			#				(display_message, "@{!}{s14}'s relation with {s17} is {reg0}"),
			#			(try_end),
			(store_sub, ":adjust_relations", reg0, 10),
			(val_div, ":adjust_relations", 15),
			(neq, ":adjust_relations", 0),
			
			#Not negatively affected if they favored the lord
			(try_begin),
				(troop_slot_eq, ":lord", slot_troop_stance_on_faction_issue, ":faction_marshall"),
				(val_add, ":adjust_relations", 1),
				(val_max, ":adjust_relations", 0),
			(try_end),
			
			(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", ":adjust_relations"),
			(val_add, "$total_promotion_changes", ":adjust_relations"),
			
			(lt, ":adjust_relations", -2),
			(store_random_in_range, ":random", 1, 10),
			
			(val_add, ":adjust_relations", ":random"),
			
			(lt, ":adjust_relations", 0),
			
			(str_store_troop_name, s14, ":lord"),
			(str_store_troop_name, s15, ":faction_marshall"),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(display_message, "str_s14_protests_the_appointment_of_s15_as_marshall"),
			(try_end),
			
			(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", -10),
			(call_script, "script_troop_change_relation_with_troop", ":faction_marshall", ":lord", -5),
			(val_add, "$total_promotion_changes", -15),
			
			(call_script, "script_add_log_entry", logent_lord_protests_marshall_appointment, ":lord",  ":faction_marshall", ":faction_leader", "$g_encountered_party_faction"),
			
			(try_end),
		(try_end),
		
	])
	