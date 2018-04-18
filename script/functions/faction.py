from header import *

# script_faction_get_number_of_armies
		# Input: arg1 = faction_no
		# Output: reg0 = number_of_armies
		("faction_get_number_of_armies",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":num_armies", 0),
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(store_troop_faction, ":hero_faction_no", ":troop_no"),
					(eq, ":hero_faction_no", ":faction_no"),
					(troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
					(ge, ":hero_party", 0),
					(party_is_active, ":hero_party"),
					(call_script, "script_party_count_fit_regulars", ":hero_party"),
					(assign, ":party_size", reg0),
					(call_script, "script_party_get_ideal_size", ":hero_party"),
					(assign, ":ideal_size", reg0),
					(val_mul, ":ideal_size", 60),
					(val_div, ":ideal_size", 100),
					(gt, ":party_size", ":ideal_size"),
					(val_add, ":num_armies", 1),
				(try_end),
				(assign, reg0, ":num_armies"),
		]),

		# script_faction_recalculate_strength
		# Input: arg1 = faction_no
		# Output: reg0 = strength
		("faction_recalculate_strength",
			[
				(store_script_param_1, ":faction_no"),
				
				(call_script, "script_faction_get_number_of_armies", ":faction_no"),
				(assign, ":num_armies", reg0),
				(assign, ":num_castles", 0),
				(assign, ":num_towns", 0),
				
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(eq, ":center_faction", ":faction_no"),
					(try_begin),
						(party_slot_eq, ":center_no", slot_party_type, spt_castle),
						(val_add, ":num_castles", 1),
					(else_try),
						(party_slot_eq, ":center_no", slot_party_type, spt_town),
						(val_add, ":num_towns", 1),
					(try_end),
				(try_end),
				
				(faction_set_slot, ":faction_no", slot_faction_num_armies, ":num_armies"),
				(faction_set_slot, ":faction_no", slot_faction_num_castles, ":num_castles"),
				(faction_set_slot, ":faction_no", slot_faction_num_towns, ":num_towns"),
				
		]),

# script_cf_faction_get_random_enemy_faction
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (Can fail)
		("cf_faction_get_random_enemy_faction",
			[
				(store_script_param_1, ":faction_no"),
				
				(assign, ":result", -1),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(le, ":cur_relation", -1),
					(val_add, ":count_factions", 1),
				(try_end),
				(store_random_in_range,":random_faction",0,":count_factions"),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(eq, ":result", -1),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(le, ":cur_relation", -1),
					(val_add, ":count_factions", 1),
					(gt, ":count_factions", ":random_faction"),
					(assign, ":result", ":cur_faction"),
				(try_end),
				
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		]),
		
		# script_cf_faction_get_random_friendly_faction
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (Can fail)
		("cf_faction_get_random_friendly_faction",
			[
				(store_script_param_1, ":faction_no"),
				
				(assign, ":result", -1),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(neq, ":cur_faction", ":faction_no"),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(ge, ":cur_relation", 0),
					(val_add, ":count_factions", 1),
				(try_end),
				(store_random_in_range,":random_faction",0,":count_factions"),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(eq, ":result", -1),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(neq, ":cur_faction", ":faction_no"),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(ge, ":cur_relation", 0),
					(val_add, ":count_factions", 1),
					(gt, ":count_factions", ":random_faction"),
					(assign, ":result", ":cur_faction"),
				(try_end),
				
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		]),


		
		# script_cf_get_random_lord_in_a_center_with_faction
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
		("cf_get_random_lord_in_a_center_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
				(try_end),
				(store_random_in_range, ":random_lord", 0, ":count_lords"),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(eq, ":result", -1),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
					(lt, ":random_lord", ":count_lords"),
					(assign, ":result", ":lord_no"),
				(try_end),
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		]),
		
		# script_cf_get_random_lord_except_king_with_faction
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
		("cf_get_random_lord_except_king_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(val_add, ":count_lords", 1),
				(try_end),
				(store_random_in_range, ":random_lord", 0, ":count_lords"),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(eq, ":result", -1),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(val_add, ":count_lords", 1),
					(lt, ":random_lord", ":count_lords"),
					(assign, ":result", ":lord_no"),
				(try_end),
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		]),
		
		
		# script_cf_get_random_lord_from_another_faction_in_a_center
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
		("cf_get_random_lord_from_another_faction_in_a_center",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(neq, ":lord_faction_no", ":faction_no"),
					(store_relation, ":our_relation", ":lord_faction_no", "fac_player_supporters_faction"),
					(store_relation, ":lord_relation", ":lord_faction_no", ":faction_no"),
					(lt, ":lord_relation", 0),
					(ge, ":our_relation", 0),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
				(try_end),
				(store_random_in_range, ":random_lord", 0, ":count_lords"),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(eq, ":result", -1),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(neq, ":lord_faction_no", ":faction_no"),
					(store_relation, ":our_relation", ":lord_faction_no", "fac_player_supporters_faction"),
					(store_relation, ":lord_relation", ":lord_faction_no", ":faction_no"),
					(lt, ":lord_relation", 0),
					(ge, ":our_relation", 0),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
					(lt, ":random_lord", ":count_lords"),
					(assign, ":result", ":lord_no"),
				(try_end),
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		]),