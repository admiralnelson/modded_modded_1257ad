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

