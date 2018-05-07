from header import *
#script_update_companion_candidates_in_taverns
		# WARNING: modified by 1257AD devs
		# INPUT: none
		# OUTPUT: none
update_companion_candidates_in_taverns = (
	"update_companion_candidates_in_taverns",
			[
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_shuffling_companion_locations"),
				(try_end),
				
				(try_for_range, ":troop_no", companions_begin, companions_end),
					(neg | troop_slot_eq, ":troop_no", slot_troop_traveling, 1), # rafi
					(troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
					(troop_slot_eq, ":troop_no", slot_troop_days_on_mission, 0),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
					
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(try_begin),
						(neg|troop_slot_eq, ":troop_no", slot_troop_home, ":town_no"),
						(neg|troop_slot_eq, ":troop_no", slot_troop_first_encountered, ":town_no"),
						(troop_set_slot, ":troop_no", slot_troop_cur_center, ":town_no"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, 4, ":troop_no"),
							(str_store_party_name, 5, ":town_no"),
							(display_message, "@{!}{s4} is in {s5}"),
						(try_end),
					(try_end),
				(try_end),
		])
		
		#script_update_ransom_brokers
		# INPUT: none
		# OUTPUT: none
update_ransom_brokers = (
	"update_ransom_brokers",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_ransom_broker, 0),
				(try_end),
				
				(try_for_range, ":troop_no", ransom_brokers_begin, ransom_brokers_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_ransom_broker, ":troop_no"),
				(try_end),
				
				#(party_set_slot,"p_town_2",slot_center_ransom_broker,"trp_ramun_the_slave_trader"),
		])
		
		#script_update_tavern_travellers
		# INPUT: none
		# OUTPUT: none
update_tavern_travellers = (
	"update_tavern_travellers",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_traveler, 0),
				(try_end),
				
				(try_for_range, ":troop_no", tavern_travelers_begin, tavern_travelers_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_traveler, ":troop_no"),
					(assign, ":end_cond", 15),
					(try_for_range, ":unused", 0, ":end_cond"),
						(store_random_in_range, ":info_faction", kingdoms_begin, kingdoms_end),
						(faction_slot_eq, ":info_faction", slot_faction_state, sfs_active),
						(neq, ":info_faction", "$players_kingdom"),
						(neq, ":info_faction", "fac_player_supporters_faction"),
						(party_set_slot, ":town_no", slot_center_traveler_info_faction, ":info_faction"),
						(assign, ":end_cond", 0),
					(try_end),
				(try_end),
				
				(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "p_town_1_1"),
		])

		
		#script_update_booksellers
		# INPUT: none
		# OUTPUT: none
update_booksellers = (
	"update_booksellers",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_bookseller, 0),
				(try_end),
				
				(try_for_range, ":troop_no", tavern_booksellers_begin, tavern_booksellers_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_bookseller, ":troop_no"),
				(try_end),
				
				
				
		])
		
		#script_update_tavern_minstels
		# INPUT: none
		# OUTPUT: none
update_tavern_minstrels = (
	"update_tavern_minstrels",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_minstrel, 0),
				(try_end),
				
				(try_for_range, ":troop_no", tavern_minstrels_begin, tavern_minstrels_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_minstrel, ":troop_no"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":troop_no"),
						(str_store_party_name, s5, ":town_no"),
						
						(display_message, "str_s4_is_at_s5"),
					(try_end),
				(try_end),
				
				
		])
		
update_other_taverngoers = (
	"update_other_taverngoers",
			[
				(store_random_in_range, ":fight_promoter_tavern", towns_begin, towns_end),
				(troop_set_slot, "trp_fight_promoter", slot_troop_cur_center, ":fight_promoter_tavern"),
				
				(store_random_in_range, ":belligerent_drunk_tavern", towns_begin, towns_end),
				(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, ":belligerent_drunk_tavern"),
		])
		
		#script_post_battle_personality_clash_check
		# NOTE: NPC companion personality clash
		# it is executed after battle. Quite annoying, frankly.
		# it is disabled. to enable it, post_battle_personality_clash_check := 1
		# INPUT: NONE
		# OUTPUT: NONE
post_battle_personality_clash_check = (
	"post_battle_personality_clash_check",
			[
				(try_for_range, ":npc", companions_begin, companions_end),
					(eq, "$disable_npc_complaints", 0),
					
					(main_party_has_troop, ":npc"),
					(neg|troop_is_wounded, ":npc"),
					
					(troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash2_object),
					(main_party_has_troop, ":other_npc"),
					(neg|troop_is_wounded, ":other_npc"),
					
					#                (store_random_in_range, ":random", 0, 3),
					(try_begin),
						(troop_slot_eq, ":npc", slot_troop_personalityclash2_state, 0),
						(try_begin),
							#                        (eq, ":random", 0),
							(assign, "$npc_with_personality_clash_2", ":npc"),
						(try_end),
					(try_end),
					
				(try_end),
				
				(try_for_range, ":npc", companions_begin, companions_end),
					(troop_slot_eq, ":npc", slot_troop_personalitymatch_state, 0),
					(eq, "$disable_npc_complaints", 0),
					
					(main_party_has_troop, ":npc"),
					(neg|troop_is_wounded, ":npc"),
					
					(troop_get_slot, ":other_npc", ":npc", slot_troop_personalitymatch_object),
					(main_party_has_troop, ":other_npc"),
					(neg|troop_is_wounded, ":other_npc"),
					(assign, "$npc_with_personality_match", ":npc"),
				(try_end),
				
				
				(try_begin),
					(gt, "$npc_with_personality_clash_2", 0),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(display_message, "str_personality_clash_conversation_begins"),
					(try_end),
					
					(try_begin),
						(main_party_has_troop, "$npc_with_personality_clash_2"),
						(assign, "$npc_map_talk_context", slot_troop_personalityclash2_state),
						(start_map_conversation, "$npc_with_personality_clash_2"),
					(else_try),
						(assign, "$npc_with_personality_clash_2", 0),
					(try_end),
				(else_try),
					(gt, "$npc_with_personality_match", 0),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(display_message, "str_personality_match_conversation_begins"),
					(try_end),
					
					(try_begin),
						(main_party_has_troop, "$npc_with_personality_match"),
						(assign, "$npc_map_talk_context", slot_troop_personalitymatch_state),
						(start_map_conversation, "$npc_with_personality_match"),
					(else_try),
						(assign, "$npc_with_personality_match", 0),
					(try_end),
				(try_end),
		])
		
		#script_retire_companion
		#NOTE: not sure what is this thing
		# INPUT npc, length (presumably time?)
retire_companion = (
	"retire_companion",
			[
				(store_script_param_1, ":npc"),
				(store_script_param_2, ":length"),
				
				(remove_member_from_party, ":npc", "p_main_party"),
				(troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
				(troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
				(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
				(store_add, ":return_renown", ":renown", ":length"),
				(troop_set_slot, ":npc", slot_troop_occupation, slto_retirement),
				(troop_set_slot, ":npc", slot_troop_return_renown, ":return_renown"),
		])

		#script_reduce_companion_morale_for_clash
		#script_calculate_ransom_amount_for_troop
		# INPUT: arg1 = troop_no for companion1 arg2 = troop_no for companion2 arg3 = slot_for_clash_state
		# slot_for_clash_state means: 1=give full penalty to companion1; 2=give full penalty to companion2; 3=give penalty equally
reduce_companion_morale_for_clash = (
	"reduce_companion_morale_for_clash",
			[
				(store_script_param, ":companion_1", 1),
				(store_script_param, ":companion_2", 2),
				(store_script_param, ":slot_for_clash_state", 3),
				
				(troop_get_slot, ":clash_state", ":companion_1", ":slot_for_clash_state"),
				(troop_get_slot, ":grievance_1", ":companion_1", slot_troop_personalityclash_penalties),
				(troop_get_slot, ":grievance_2", ":companion_2", slot_troop_personalityclash_penalties),
				(try_begin),
					(eq, ":clash_state", pclash_penalty_to_self),
					(val_add, ":grievance_1", 5),
				(else_try),
					(eq, ":clash_state", pclash_penalty_to_other),
					(val_add, ":grievance_2", 5),
				(else_try),
					(eq, ":clash_state", pclash_penalty_to_both),
					(val_add, ":grievance_1", 3),
					(val_add, ":grievance_2", 3),
				(try_end),
				(troop_set_slot, ":companion_1", slot_troop_personalityclash_penalties, ":grievance_1"),
				(troop_set_slot, ":companion_2", slot_troop_personalityclash_penalties, ":grievance_2"),
		])

#script_objectionable_action
		# WARNING: modified by 1257AD devs
		# NOTE: it is disabled.
		# NPC objection in player party for certain player action such as looting. modded2x: "I might enable this again lmao"
		# INPUT: action_type, action_string
		# OUTPUT : NONE
objectionable_action = (
	"objectionable_action",
			[
				(store_script_param_1, ":action_type"),
				(store_script_param_2, ":action_string"),
				
				(assign, ":grievance_minimum", -2),
				(try_for_range, ":npc", companions_begin, companions_end),
					(main_party_has_troop, ":npc"),
					(eq, 0, 1), #TOM DISABLE THIS
					###Primary morality check
					(try_begin),
						(troop_slot_eq, ":npc", slot_troop_morality_type, ":action_type"),
						(troop_get_slot, ":value", ":npc", slot_troop_morality_value),
						(try_begin),
							(troop_slot_eq, ":npc", slot_troop_morality_state, tms_acknowledged),
							# npc is betrayed, major penalty to player honor and morale
							(troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
							(val_mul, ":value", 2),
							(val_add, ":grievance", ":value"),
							(troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
						(else_try),
							(this_or_next|troop_slot_eq, ":npc", slot_troop_morality_state, tms_dismissed),
							(eq, "$disable_npc_complaints", 1),
							# npc is quietly disappointed
							(troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
							(val_add, ":grievance", ":value"),
							(troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
						(else_try),
							# npc raises the issue for the first time
							(troop_slot_eq, ":npc", slot_troop_morality_state, tms_no_problem),
							(gt, ":value", ":grievance_minimum"),
							(assign, "$npc_with_grievance", ":npc"),
							(assign, "$npc_grievance_string", ":action_string"),
							(assign, "$npc_grievance_slot", slot_troop_morality_state),
							(assign, ":grievance_minimum", ":value"),
							(assign, "$npc_praise_not_complaint", 0),
							(try_begin),
								(lt, ":value", 0),
								(assign, "$npc_praise_not_complaint", 1),
							(try_end),
						(try_end),
						
						###Secondary morality check
					(else_try),
						(troop_slot_eq, ":npc", slot_troop_2ary_morality_type, ":action_type"),
						(troop_get_slot, ":value", ":npc", slot_troop_2ary_morality_value),
						(try_begin),
							(troop_slot_eq, ":npc", slot_troop_2ary_morality_state, tms_acknowledged),
							# npc is betrayed, major penalty to player honor and morale
							(troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
							(val_mul, ":value", 2),
							(val_add, ":grievance", ":value"),
							(troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
						(else_try),
							(this_or_next|troop_slot_eq, ":npc", slot_troop_2ary_morality_state, tms_dismissed),
							(eq, "$disable_npc_complaints", 1),
							# npc is quietly disappointed
							(troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
							(val_add, ":grievance", ":value"),
							(troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
						(else_try),
							# npc raises the issue for the first time
							(troop_slot_eq, ":npc", slot_troop_2ary_morality_state, tms_no_problem),
							(gt, ":value", ":grievance_minimum"),
							(assign, "$npc_with_grievance", ":npc"),
							(assign, "$npc_grievance_string", ":action_string"),
							(assign, "$npc_grievance_slot", slot_troop_2ary_morality_state),
							(assign, ":grievance_minimum", ":value"),
							(assign, "$npc_praise_not_complaint", 0),
							(try_begin),
								(lt, ":value", 0),
								(assign, "$npc_praise_not_complaint", 1),
							(try_end),
						(try_end),
					(try_end),
					
					(try_begin),
						(gt, "$npc_with_grievance", 0),
						(eq, "$npc_praise_not_complaint", 0),
						(str_store_troop_name, 4, "$npc_with_grievance"),
						(display_message, "@{s4} looks upset."),
					(try_end),
				(try_end),
		])