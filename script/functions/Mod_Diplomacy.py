from header import *

#script_dplmc_describe_prosperity_to_s4
	#INPUT: number_of_recruits, faction_of_recruits,recruit_type
	#OUTPUT: s4 prosperity string
dplmc_describe_prosperity_to_s4 = (
	"dplmc_describe_prosperity_to_s4",
		[
		(store_script_param_1, ":center_no"),
		
		(str_store_party_name, s60,":center_no"),
		(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
		(str_store_string, s4, "str_empty_string"),
		(try_begin),
			(is_between, ":center_no", towns_begin, towns_end),
			(try_begin),
			(eq, ":prosperity", 0),
			(str_store_string, s4, "str_town_prosperity_0"),
			(else_try),
			(is_between, ":prosperity", 1, 11),
			(str_store_string, s4, "str_town_prosperity_10"),
			(else_try),
			(is_between, ":prosperity", 11, 21),
			(str_store_string, s4, "str_town_prosperity_20"),
			(else_try),
			(is_between, ":prosperity", 21, 31),
			(str_store_string, s4, "str_town_prosperity_30"),
			(else_try),
			(is_between, ":prosperity", 31, 41),
			(str_store_string, s4, "str_town_prosperity_40"),
			(else_try),
			(is_between, ":prosperity", 41, 51),
			(str_store_string, s4, "str_town_prosperity_50"),
			(else_try),
			(is_between, ":prosperity", 51, 61),
			(str_store_string, s4, "str_town_prosperity_60"),
			(else_try),
			(is_between, ":prosperity", 61, 71),
			(str_store_string, s4, "str_town_prosperity_70"),
			(else_try),
			(is_between, ":prosperity", 71, 81),
			(str_store_string, s4, "str_town_prosperity_80"),
			(else_try),
			(is_between, ":prosperity", 81, 91),
			(str_store_string, s4, "str_town_prosperity_90"),
			(else_try),
			(is_between, ":prosperity", 91, 101),
			(str_store_string, s4, "str_town_prosperity_100"),
			(try_end),
		(else_try),
			(is_between, ":center_no", villages_begin, villages_end),
			(try_begin),
			(eq, ":prosperity", 0),
			(str_store_string, s4, "str_village_prosperity_0"),
			(else_try),
			(is_between, ":prosperity", 1, 11),
			(str_store_string, s4, "str_village_prosperity_10"),
			(else_try),
			(is_between, ":prosperity", 11, 21),
			(str_store_string, s4, "str_village_prosperity_20"),
			(else_try),
			(is_between, ":prosperity", 21, 31),
			(str_store_string, s4, "str_village_prosperity_30"),
			(else_try),
			(is_between, ":prosperity", 31, 41),
			(str_store_string, s4, "str_village_prosperity_40"),
			(else_try),
			(is_between, ":prosperity", 41, 51),
			(str_store_string, s4, "str_village_prosperity_50"),
			(else_try),
			(is_between, ":prosperity", 51, 61),
			(str_store_string, s4, "str_village_prosperity_60"),
			(else_try),
			(is_between, ":prosperity", 61, 71),
			(str_store_string, s4, "str_village_prosperity_70"),
			(else_try),
			(is_between, ":prosperity", 71, 81),
			(str_store_string, s4, "str_village_prosperity_80"),
			(else_try),
			(is_between, ":prosperity", 81, 91),
			(str_store_string, s4, "str_village_prosperity_90"),
			(else_try),
			(is_between, ":prosperity", 91, 101),
			(str_store_string, s4, "str_village_prosperity_100"),
			(try_end),
		(try_end),
	])


	#script_dplmc_describe_tax_rate_to_s50
	# WARNING: modified by 1257AD devs
	#INPUT: tax_rate
	#OUTPUT: s50 str_id
dplmc_describe_tax_rate_to_s50 = (
	"dplmc_describe_tax_rate_to_s50",
		[
		(store_script_param_1, ":tax_rate"),
		#(val_div, ":tax_rate", 25), #tom
		(store_add, ":str_id","str_dplmc_tax_normal", ":tax_rate"),
		(str_store_string, s50, ":str_id"),
	])

	#script_dplmc_player_troops_leave
	#INPUT: percent
	#OUTPUT: deserters
dplmc_player_troops_leave = (
	"dplmc_player_troops_leave",
		[
		(store_script_param_1, ":percent"),
		
		(try_begin),#debug
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":percent"),
			(display_message, "@{!}DEBUG : removing player troops: {reg0}%"),
		(try_end),
		
		(assign, ":deserters", 0),
		(try_for_parties, ":party_no"),
			(assign, ":remove_troops", 0),
			(try_begin),
			(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
			(party_slot_eq|party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
			(assign, ":remove_troops", 1),
			(else_try),
			(eq, "p_main_party", ":party_no"),
			(assign, ":remove_troops", 1),
			(try_end),
			
			(eq, ":remove_troops", 1),
			(party_get_num_companion_stacks, ":num_stacks",":party_no"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_size, ":stack_size",":party_no",":i_stack"),
			(val_mul, ":stack_size", ":percent"),
			(val_div, ":stack_size", 100),
			(party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
			(party_remove_members, ":party_no", ":troop_id", ":stack_size"),
			(val_add, ":deserters", ":stack_size"),
			(try_end),
		(try_end),
		(assign, reg0, ":deserters"),
		])
	
	#script_dplmc_party_calculate_strength
	#INPUT: party, party_leader_exclusion
	#OUTPUT: sum
dplmc_party_calculate_strength = (
	"dplmc_party_calculate_strength",
		[
		(store_script_param_1, ":party"), #Party_id
		(store_script_param_2, ":exclude_leader"), #Party_id
		
		(assign, reg0,0),
		(party_get_num_companion_stacks, ":num_stacks", ":party"),
		(assign, ":first_stack", 0),
		(try_begin),
			(neq, ":exclude_leader", 0),
			(assign, ":first_stack", 1),
		(try_end),
		
		(assign, ":sum", 0),
		(try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
			
			(try_begin),
			(neg|troop_is_hero, ":stack_troop"),
			(party_stack_get_size, ":stack_size",":party",":i_stack"),
			(try_end),
			(val_add, ":sum", ":stack_size"),
		(try_end),
		(assign, reg0, ":sum"),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : sum: {reg0}"),
		(try_end),
	])

	#script_dplmc_troop_political_notes_to_s47
	#INPUT: troop_no
	#OUTPUT: s47
dplmc_troop_political_notes_to_s47 = (
	"dplmc_troop_political_notes_to_s47",
		[
		(store_script_param, ":troop_no", 1),
		(try_begin),
			(str_clear, s47),
			
			(store_faction_of_troop, ":troop_faction", ":troop_no"),
			
			(faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
			
			(str_clear, s40),
			(assign, ":logged_a_rivalry", 0),
			(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_hero"),
			(lt, reg0, -10),
			
			(str_store_troop_name_link, s39, ":kingdom_hero"),
			(try_begin),
				(eq, ":logged_a_rivalry", 0),
				(str_store_string, s40, "str_dplmc_s39_rival"),
				(assign, ":logged_a_rivalry", 1),
			(else_try),
				(str_store_string, s41, "str_s40"),
				(str_store_string, s40, "str_dplmc_s41_s39_rival"),
			(try_end),
			
			(try_end),
			
			(str_clear, s46),
			(str_store_troop_name, s46,":troop_no"),
			(try_begin),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_martial"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_debauched"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_pitiless"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_calculating"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_quarrelsome"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_goodnatured"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_upstanding"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_conventional"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_adventurous),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_adventurous"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_otherworldly),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_romantic"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_moralist"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_ambitious),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_ambitious"),
			(else_try),
			(troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_reg11"),
			(try_end),
			
			(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
			(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
			(str_store_troop_name, s39, ":love_interest"),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":love_interest"),
			(str_store_string, s45, "str_dplmc_s40_love_interest_s39"),
			(try_begin),
				(troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
				(str_store_string, s45, "str_dplmc_s40_betrothed_s39"),
			(try_end),
			(try_end),
			
			(str_clear, s44),
			(try_begin),
			(neq, ":troop_no", ":faction_leader"),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			
			(assign, ":relation", reg0),
			(store_add, ":normalized_relation", ":relation", 100),
			(val_add, ":normalized_relation", 5),
			(store_div, ":str_offset", ":normalized_relation", 10),
			(val_clamp, ":str_offset", 0, 20),
			(store_add, ":str_id", "str_dplmc_relation_mnus_100_ns",  ":str_offset"),
			(try_begin),
				(eq, ":faction_leader", "trp_player"),
				(str_store_string, s59, "@you"),
			(else_try),
				(str_store_troop_name, s59, ":faction_leader"),
			(try_end),
			(str_store_string, s59, ":str_id"),
			(str_store_string, s44, "@{!}^{s59}"),
			(try_end),
			
			(str_clear, s48),
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(store_current_hours, ":hours"),
			(gt, ":hours", 0),
			(call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),
			(str_store_string, s48, "str_sense_of_security_military_reg1_court_position_reg3_"),
			(try_end),
			
			(str_store_string, s47, "str_s46s45s44s48"),
			
		(try_end),
	])