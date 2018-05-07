from header import *

		# script_change_player_party_morale
		# Input: arg1 = morale difference
		# Output: none
change_player_party_morale = (
	"change_player_party_morale",
			[
				(store_script_param_1, ":morale_dif"),
				(party_get_morale, ":cur_morale", "p_main_party"),
				(val_clamp, ":cur_morale", 0, 100),
				
				(store_add, ":new_morale", ":cur_morale", ":morale_dif"),
				(val_clamp, ":new_morale", 0, 100),
				
				(party_set_morale, "p_main_party", ":new_morale"),
				(try_begin),
					(lt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":cur_morale", ":new_morale"),
					(display_message, "str_party_lost_morale"),
				(else_try),
					(gt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":new_morale", ":cur_morale"),
					(display_message, "str_party_gained_morale"),
				(try_end),
		])
		

		# script_change_player_honor
		# prints "you gain/lose honour" if player honour changes
		# Input: arg1 = honor difference
		# Output: none
change_player_honor = (
	"change_player_honor",
			[
				(store_script_param_1, ":honor_dif"),
				(val_add, "$player_honor", ":honor_dif"),
				(try_begin),
					(gt, ":honor_dif", 0),
					(display_message, "@You gain honour."),
				(else_try),
					(lt, ":honor_dif", 0),
					(display_message, "@You lose honour."),
				(try_end),
				
				##      (val_mul, ":honor_dif", 1000),
				##      (assign, ":temp_honor", 0),
				##      (assign, ":num_nonlinear_steps", 10),
				##      (try_begin),
				##        (gt, "$player_honor", 0),
				##        (lt, ":honor_dif", 0),
				##        (assign, ":num_nonlinear_steps", 0),
				##      (else_try),
				##        (lt, "$player_honor", 0),
				##        (gt, ":honor_dif", 0),
				##        (assign, ":num_nonlinear_steps", 3),
				##      (try_end),
				##
				##      (try_begin),
				##        (ge, "$player_honor", 0),
				##        (assign, ":temp_honor", "$player_honor"),
				##      (else_try),
				##        (val_sub, ":temp_honor", "$player_honor"),
				##      (try_end),
				##      (try_for_range, ":unused",0,":num_nonlinear_steps"),
				##        (ge, ":temp_honor", 10000),
				##        (val_div, ":temp_honor", 2),
				##        (val_div, ":honor_dif", 2),
				##      (try_end),
				##      (val_add, "$player_honor", ":honor_dif"),
		])


		# script_change_player_party_morale
		# Input: arg1 = morale difference
		# Output: none
change_player_party_morale = (
	"change_player_party_morale",
			[
				(store_script_param_1, ":morale_dif"),
				(party_get_morale, ":cur_morale", "p_main_party"),
				(val_clamp, ":cur_morale", 0, 100),
				
				(store_add, ":new_morale", ":cur_morale", ":morale_dif"),
				(val_clamp, ":new_morale", 0, 100),
				
				(party_set_morale, "p_main_party", ":new_morale"),
				(try_begin),
					(lt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":cur_morale", ":new_morale"),
					(display_message, "str_party_lost_morale"),
				(else_try),
					(gt, ":new_morale", ":cur_morale"),
					(store_sub, reg1, ":new_morale", ":cur_morale"),
					(display_message, "str_party_gained_morale"),
				(try_end),
		])
		

#script_player_join_faction
		# WARNING : modified by 1257AD devs
		# INPUT: arg1 = faction_no
		# OUTPUT: none
player_join_faction = (
	"player_join_faction",
			[
				(store_script_param, ":faction_no", 1),
				(assign,"$players_kingdom",":faction_no"),
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_ai_state, sfai_default),
				(assign, "$players_oath_renounced_against_kingdom", 0),
				(assign, "$players_oath_renounced_given_center", 0),
				(assign, "$players_oath_renounced_begin_time", 0),
				
				#(display_message, "@You receive an item as a token of appreciation for joining this faction.", 0xFF00FF00),
				# assign some item for joining faction
		#(troop_add_gold,"trp_player",5000),
				# (try_begin),
					# (eq, ":faction_no", fac_kingdom_1),
					# (troop_add_item, "trp_player","itm_teu_postulant_a", imod_hardened),
					#(troop_add_item, "trp_player","itm_teu_warhorse_b",imod_lame),
					# (call_script, "script_set_player_relation_with_faction", "fac_prussians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_curonians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_yotvingians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_samogitians", -40),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_2),
					# (troop_add_item, "trp_player","itm_balt_padded_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_mon_lamellar_horse_a",imod_lame),
					# (call_script, "script_set_player_relation_with_faction", "fac_prussians", 40),
					# (call_script, "script_set_player_relation_with_faction", "fac_curonians", 40),
					# (call_script, "script_set_player_relation_with_faction", "fac_yotvingians", 40),
					# (call_script, "script_set_player_relation_with_faction", "fac_samogitians", 40),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_3),
					# (troop_add_item, "trp_player","itm_khergit_bow",0),
					# (troop_add_item, "trp_player","itm_steppe_horse",0),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_4),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_denmark_a",imod_lame),
					# (call_script, "script_set_player_relation_with_faction", "fac_prussians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_curonians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_yotvingians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_samogitians", -40),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_5),
					# (troop_add_item, "trp_player","itm_gambeson_c",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_poland_a",imod_lame),
					# (call_script, "script_set_player_relation_with_faction", "fac_prussians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_yotvingians", -40),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_6),
					# (troop_add_item, "trp_player","itm_gambeson_d",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_hre_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_7),
					# (troop_add_item, "trp_player","itm_gambeson_b",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_hungary_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_8),
					# (troop_add_item, "trp_player","itm_kau_rus_e",imod_hardened),
					#(troop_add_item, "trp_player","itm_mon_lamellar_horse_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_9),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_england_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_10),
					# (troop_add_item, "trp_player","itm_gambeson_c",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_france_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_11),
					# (troop_add_item, "trp_player","itm_gambeson_d",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_norway_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_12),
					# (troop_add_item, "trp_player","itm_gambeson_b",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_scotland_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_13),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_ireland_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_14),
					# (troop_add_item, "trp_player","itm_gambeson_c",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse_sweden_a",imod_lame),
					# (call_script, "script_set_player_relation_with_faction", "fac_prussians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_curonians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_yotvingians", -40),
					# (call_script, "script_set_player_relation_with_faction", "fac_samogitians", -40),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_15),
					# (troop_add_item, "trp_player","itm_kau_rus_e",imod_hardened),
					#(troop_add_item, "trp_player","itm_mon_lamellar_horse_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_16),
					# (troop_add_item, "trp_player","itm_gambeson_d",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_17),
					# (troop_add_item, "trp_player","itm_gambeson_b",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_18),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_19),
					# (troop_add_item, "trp_player","itm_gambeson_c",imod_hardened),
					# (troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_20),
					# (troop_add_item, "trp_player","itm_kau_arab_aketon",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_papacy),
				 # (call_script, "script_set_player_relation_with_faction", "fac_guelphs", 40),
			#(call_script, "script_set_player_relation_with_faction", "fac_ghibellines", -40),
					# (troop_add_item, "trp_player","itm_gambeson_d",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_22),
					# (troop_add_item, "trp_player","itm_kau_rus_e",imod_hardened),
					#(troop_add_item, "trp_player","itm_mon_lamellar_horse_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_23),
					# (troop_add_item, "trp_player","itm_gambeson_b",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
			# (this_or_next|eq, ":faction_no", fac_kingdom_38),
			# (this_or_next|eq, ":faction_no", fac_kingdom_39),
			# (this_or_next|eq, ":faction_no", fac_kingdom_40),	
			# (this_or_next|eq, ":faction_no", fac_kingdom_41),	
					# (eq, ":faction_no", fac_kingdom_24),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
					#(call_script, "script_set_player_relation_with_faction", "fac_guelphs", -40),
			#(call_script, "script_set_player_relation_with_faction", "fac_ghibellines", 40),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_25),
					# (troop_add_item, "trp_player","itm_kau_arab_aketon",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_26),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_27),
					# (troop_add_item, "trp_player","itm_khergit_bow",0),
					# (troop_add_item, "trp_player","itm_steppe_horse",0),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_28),
					# (troop_add_item, "trp_player","itm_kau_arab_aketon",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_29),
					# (troop_add_item, "trp_player","itm_kau_rus_e",imod_hardened),
					#(troop_add_item, "trp_player","itm_mon_lamellar_horse_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_30),
					# (troop_add_item, "trp_player","itm_kau_rus_e",imod_hardened),
					#(troop_add_item, "trp_player","itm_mon_lamellar_horse_a",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_31),
					# (troop_add_item, "trp_player","itm_kau_arab_aketon",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),
				# (else_try),
					# (eq, ":faction_no", fac_kingdom_32),
					# (troop_add_item, "trp_player","itm_gambeson_a",imod_hardened),
		# (else_try),
			# (this_or_next|eq, ":faction_no", fac_kingdom_36),
			# (this_or_next|eq, ":faction_no", fac_kingdom_34),
			# (this_or_next|eq, ":faction_no", fac_kingdom_35),		  
					# (eq, ":faction_no", fac_kingdom_33),
					# (troop_add_item, "trp_player","itm_balt_padded_a",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),  
		# (else_try),
					# (eq, ":faction_no", fac_kingdom_37),
					# (troop_add_item, "trp_player","itm_gambeson_d",imod_hardened),
					#(troop_add_item, "trp_player","itm_warhorse",imod_lame),  
				# (try_end),
				# ends
				(try_for_range,":other_kingdom",kingdoms_begin,kingdoms_end),
					(faction_slot_eq, ":other_kingdom", slot_faction_state, sfs_active),
					(neq, ":other_kingdom", "fac_player_supporters_faction"),
					(try_begin),
						(neq, ":other_kingdom", ":faction_no"),
						(store_relation, ":other_kingdom_reln", ":other_kingdom", ":faction_no"),
					(else_try),
						(store_relation, ":other_kingdom_reln", "fac_player_supporters_faction", ":other_kingdom"),
						(val_max, ":other_kingdom_reln", 12),
					(try_end),
					(call_script, "script_set_player_relation_with_faction", ":other_kingdom", ":other_kingdom_reln"),
				(try_end),
				
				(try_for_range, ":cur_center", centers_begin, centers_end),
					#Give center to kingdom if player is the owner
					(le, "$g_player_crusading", 0),
					(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
					(call_script, "script_give_center_to_faction_while_maintaining_lord", ":cur_center", ":faction_no"),
				(else_try),
					#Give center to kingdom if part of player faction
					(le, "$g_player_crusading", 0),
					(store_faction_of_party, ":cur_center_faction", ":cur_center"),
					(eq, ":cur_center_faction", "fac_player_supporters_faction"),
					(call_script, "script_give_center_to_faction_while_maintaining_lord", ":cur_center", ":faction_no"),
				(try_end),
				
				(try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
					(check_quest_active, ":quest_no"),
					(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					(store_troop_faction, ":quest_giver_faction", ":quest_giver_troop"),
					(store_relation, ":quest_giver_faction_relation", "fac_player_supporters_faction", ":quest_giver_faction"),
					(lt, ":quest_giver_faction_relation", 0),
					(call_script, "script_abort_quest", ":quest_no", 0),
				(try_end),
				(try_for_range, ":quest_no", lord_quests_begin_2, lord_quests_end_2),
					(check_quest_active, ":quest_no"),
					(quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
					(store_troop_faction, ":quest_giver_faction", ":quest_giver_troop"),
					(store_relation, ":quest_giver_faction_relation", "fac_player_supporters_faction", ":quest_giver_faction"),
					(lt, ":quest_giver_faction_relation", 0),
					(call_script, "script_abort_quest", ":quest_no", 0),
				(try_end),
				(try_begin),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
					(faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				(try_end),
				
				(try_begin),
					(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
					(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
					(try_begin),
						(ge, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":spouse"),
						(display_message, "@{!}DEBUG - {s4} faction changed by marriage, case 1"),
					(try_end),
					(troop_set_faction, ":spouse", "$players_kingdom"),
				(try_end),
				
				(try_for_range, ":center", centers_begin, centers_end),
					# rafi
					(store_faction_of_party, ":center_faction", ":faction_no"),
					(neq, ":center_faction", "$players_kingdom"),
					(party_slot_eq, ":center", slot_town_lord, stl_reserved_for_player),
					#		(party_set_slot, ":center", slot_town_lord, stl_unassigned),
				(try_end),
				
				(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
				
				#remove prisoners of player's faction if he was member of his own faction. And free companions which is prisoned in that faction.
				(try_for_parties, ":party_no"),
					(store_faction_of_party, ":party_faction", ":party_no"),
					(eq, ":party_faction", ":faction_no"),
					
					(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
					(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
						(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
						(store_troop_faction, ":cur_faction", ":cur_troop_id"),
						
						(this_or_next|eq, ":cur_faction", "fac_player_supporters_faction"),
						(this_or_next|eq, ":cur_faction", ":faction_no"),
						(is_between, ":cur_troop_id", companions_begin, companions_end),
						
						(try_begin),
							(troop_is_hero, ":cur_troop_id"),
							(call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
						(try_end),
						
						(party_prisoner_stack_get_size, ":stack_size", ":party_no", ":troop_iterator"),
						(party_remove_prisoners, ":party_no", ":cur_troop_id", ":stack_size"),
						
						(try_begin),
							(is_between, ":cur_troop_id", companions_begin, companions_end),
							
							(try_begin),
								(is_between, ":party_no", towns_begin, towns_end),
								(troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":party_no"),
							(else_try),
								(store_random_in_range, ":random_town_no", towns_begin, towns_end),
								(troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":random_town_no"),
							(try_end),
						(try_end),
					(try_end),
				(try_end),
				#remove prisoners end.
				
				#(call_script, "script_store_average_center_value_per_faction"),
				(call_script, "script_update_all_notes"),
				(assign, "$g_recalculate_ais", 1),
				# (call_script, "script_raf_set_ai_recalculation_flags", ":faction_no"),
				
		])


		#script_player_leave_faction
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = give_back_fiefs
		# OUTPUT: none
player_leave_faction = (
	"player_leave_faction",
			[
				(store_script_param, ":give_back_fiefs", 1),
				
				(call_script, "script_check_and_finish_active_army_quests_for_faction", "$players_kingdom"),
				(assign, ":old_kingdom", "$players_kingdom"),
				(assign, ":old_has_homage", "$player_has_homage"),
				(assign, "$players_kingdom", 0),
				(assign, "$player_has_homage", 0),
				
				(try_begin),
					(neq, ":give_back_fiefs", 0), #ie, give back fiefs = 1, thereby do it
					(try_for_range, ":cur_center", centers_begin, centers_end),
						(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
						(call_script, "script_give_center_to_faction", ":cur_center", ":old_kingdom"),
						
						#The following line also occurs when a lord is stripped of his fiefs by an indictment
						(party_set_slot, ":cur_center", slot_town_lord, stl_unassigned),
					(try_end),
				(else_try),
					# rafi
					(le, "$g_player_crusading", 0),
					# end rafi
					
					#If you retain the fiefs
					(try_for_range, ":cur_center", centers_begin, centers_end),
						(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
						(call_script, "script_give_center_to_faction", ":cur_center", "fac_player_supporters_faction"),
						(party_set_slot, ":cur_center", slot_town_lord, "trp_player"),
						(troop_get_slot, ":cur_banner", "trp_player", slot_troop_banner_scene_prop),
						(gt, ":cur_banner", 0),
						(val_sub, ":cur_banner", banner_scene_props_begin),
						(val_add, ":cur_banner", banner_map_icons_begin),
						(party_set_banner_icon, ":cur_center", ":cur_banner"),
					(try_end),
					
					(try_for_range, ":cur_center", villages_begin, villages_end),
						(party_get_slot, ":cur_bound_center", ":cur_center", slot_village_bound_center),
						(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
						(neg|party_slot_eq, ":cur_bound_center", slot_town_lord, "trp_player"),
						(call_script, "script_give_center_to_faction", ":cur_center", ":old_kingdom"),
					(try_end),
					
					(is_between, ":old_kingdom", kingdoms_begin, kingdoms_end),
					(neq, ":old_kingdom", "fac_player_supporters_faction"),
					(store_relation, ":reln", "fac_player_supporters_faction", ":old_kingdom"),
					(store_sub, ":req_dif", -40, ":reln"),
					(call_script, "script_change_player_relation_with_faction", ":old_kingdom", ":req_dif"),
				(try_end),
				
				(try_begin),
					(eq, ":old_has_homage", 1),
					(faction_get_slot, ":faction_leader", ":old_kingdom", slot_faction_leader),
					(call_script, "script_change_player_relation_with_troop", ":faction_leader", -20),
				(try_end),
				
				(try_begin),
					(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
					(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
					(troop_set_faction, ":spouse", "fac_player_supporters_faction"),
				(try_end),
				
				#Change relations with players_kingdom when player changes factions
				(try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
					(neq, ":kingdom", "fac_player_supporters_faction"),
					(store_relation, ":relation_with_old_faction", ":old_kingdom", ":kingdom"),
					(store_relation, ":relation_with_player_faction", "fac_player_faction", ":kingdom"),
					
					(try_begin),
						(eq, ":old_kingdom", ":kingdom"),
						(val_min, ":relation_with_player_faction", 0),
					(else_try),
						(lt, ":relation_with_old_faction", 0),
						(val_max, ":relation_with_player_faction", 0),
					(try_end),
					(set_relation, "fac_player_faction", ":kingdom", ":relation_with_player_faction"),
					(set_relation, "fac_player_supporters_faction", ":kingdom", ":relation_with_player_faction"),
				(try_end),
				
				(call_script, "script_update_all_notes"),
				(assign, "$g_recalculate_ais", 1),
				# (call_script, "script_raf_set_ai_recalculation_flags", ":old_kingdom"),
		])
		
		
deactivate_player_faction = (
	"deactivate_player_faction",
			[
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				(assign, "$players_kingdom", 0),
				(assign, "$players_oath_renounced_against_kingdom", 0),
				(assign, "$players_oath_renounced_given_center", 0),
				(assign, "$players_oath_renounced_begin_time", 0),
				#(call_script, "script_store_average_center_value_per_faction"),
				(call_script, "script_update_all_notes"),
				
				(try_begin),
					(is_between, "$g_player_minister", companions_begin, companions_end),
					(assign, "$npc_to_rejoin_party", "$g_player_minister"),
				(try_end),
				(assign, "$g_player_minister", -1),
				
				(call_script, "script_add_notification_menu", "mnu_notification_player_faction_deactive", 0, 0),
		])
		
		
		#script_activate_player_faction
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = last_interaction_with_faction
		# OUTPUT: none
		#When a player convinces her husband to rebel
		#When a player proclaims herself queen
		#When a player seizes control of a center
		#When a player recruits a lord through intrigue
		#When a player  modded2x anon: what?
activate_player_faction = (
	"activate_player_faction",
			[
				(store_script_param, ":liege", 1),
				
				#This moved to top, so that mnu_notification does not occur twice
				(try_begin),
					(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
					(neg|is_between, ":liege", pretenders_begin, pretenders_end),
					(call_script, "script_add_notification_menu", "mnu_notification_player_faction_active", 0, 0),
				(try_end),
				
				
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_active),
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, ":liege"),
				# rafi - religion
				(faction_set_slot, "fac_player_supporters_faction", slot_faction_religion, religion_catholic),
				# end rafi
				
				(assign, ":original_kingdom", "$players_kingdom"),
				
				(try_begin),
					(is_between, ":original_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
					(call_script, "script_player_leave_faction", 0), #Ends quests, transfers control of centers
				(try_end),
				
				#Name faction
				(try_begin),
					(is_between, ":liege", active_npcs_begin, active_npcs_end),
					(store_faction_of_troop, ":liege_faction"),
					(is_between, ":liege_faction", npc_kingdoms_begin, npc_kingdoms_end),
					(faction_get_slot, ":adjective_string", ":liege_faction", slot_faction_adjective),
					(str_store_string, s1, ":adjective_string"),
					(faction_set_name, "fac_player_supporters_faction", "@{s1} Rebels"),
				(else_try),
					(str_store_troop_name, s2, ":liege"),
					(str_store_string, s1, "str_s2s_rebellion"),
				(try_end),
				#(faction_set_color, "fac_player_supporters_faction", 0xFF0000), #rafi remove this
				
				(assign, "$players_kingdom", "fac_player_supporters_faction"),
				(assign, "$g_player_banner_granted", 1),
				
				
				
				#Any oaths renounced?
				(try_begin),
					(is_between, ":original_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
					
					(faction_get_slot, ":old_leader", ":original_kingdom", slot_faction_leader),
					(call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, ":old_leader", "$players_kingdom"),
					
					#Initializing renounce war variables
					(assign, "$players_oath_renounced_against_kingdom", ":original_kingdom"),
					(assign, "$players_oath_renounced_given_center", 0),
					(store_current_hours, "$players_oath_renounced_begin_time"),
					
					(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
						(store_faction_of_party, ":cur_center_faction", ":cur_center"),
						(party_set_slot, ":cur_center", slot_center_faction_when_oath_renounced, ":cur_center_faction"),
					(try_end),
					(party_set_slot, "$g_center_to_give_to_player", slot_center_faction_when_oath_renounced, "$players_oath_renounced_against_kingdom"),
					
					(store_relation, ":relation", ":original_kingdom", "fac_player_supporters_faction"),
					(ge, ":relation", 0),
					(call_script, "script_diplomacy_start_war_between_kingdoms", ":original_kingdom", "fac_player_supporters_faction", 1),
				(try_end),
				
				
				(try_begin),
					(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
					(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
					
					(try_begin),
						(ge, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":spouse"),
						(display_message, "@{!}DEBUG - {s4} faction changed by marriage, case 3"),
					(try_end),
					
					(troop_set_faction, ":spouse", "fac_player_supporters_faction"),
				(try_end),
				
				
				#(call_script, "script_store_average_center_value_per_faction"),
				(call_script, "script_update_all_notes"),
				(assign, "$g_recalculate_ais", 1),
				# (call_script, "script_raf_set_ai_recalculation_flags", "fac_player_supporters_faction"),
				
		])
		
		# script_event_hero_taken_prisoner_by_player
		# Input: arg1 = troop_no
		# Output: none
event_hero_taken_prisoner_by_player = (
	"event_hero_taken_prisoner_by_player",
			[
				(store_script_param_1, ":troop_no"),
				(try_begin),
					(check_quest_active, "qst_persuade_lords_to_make_peace"),
					(try_begin),
						(quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, ":troop_no"),
						(val_mul, ":troop_no", -1),
						(quest_set_slot, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, ":troop_no"),
						(val_mul, ":troop_no", -1),
					(else_try),
						(quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, ":troop_no"),
						(val_mul, ":troop_no", -1),
						(quest_set_slot, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, ":troop_no"),
						(val_mul, ":troop_no", -1),
					(try_end),
					(neg|check_quest_concluded, "qst_persuade_lords_to_make_peace"),
					(neg|quest_slot_ge, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, 0),
					(neg|quest_slot_ge, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, 0),
					(call_script, "script_succeed_quest", "qst_persuade_lords_to_make_peace"),
				(try_end),
				(call_script, "script_update_troop_location_notes", ":troop_no", 0),
		])

# script_stay_captive_for_hours
		# WARNING: modified by 1257AD devs
		# Input: arg1 = num_hours
		# Output: none
stay_captive_for_hours = (
	"stay_captive_for_hours",
			[
				(store_script_param, ":num_hours", 1),
				(store_current_hours, ":cur_hours"),
				(val_add, ":cur_hours", ":num_hours"),
				(val_max, "$g_check_autos_at_hour", ":cur_hours"),
				(val_add, ":num_hours", 1),
				#(rest_for_hours, ":num_hours", 0, 0),
				# rafi
				(rest_for_hours, ":num_hours", 3, 0),
				# end
		])


		# script_set_parties_around_player_ignore_player
		# Input: arg1 = ignore_range, arg2 = num_hours_to_ignore
		# Output: none
set_parties_around_player_ignore_player = (
	"set_parties_around_player_ignore_player",
			[(store_script_param, ":ignore_range", 1),
				(store_script_param, ":num_hours", 2),
				(try_for_parties, ":party_no"),
					(party_is_active, ":party_no"),
					(store_distance_to_party_from_party, ":dist", "p_main_party", ":party_no"),
					(lt, ":dist", ":ignore_range"),
					(party_ignore_player, ":party_no", ":num_hours"),
				(try_end),
		])

		
	#script_locate_player_minister
	# call this procedure to display where is player's minister located
	#INPUT: none
	#OUTPUT: none
locate_player_minister = (
	"locate_player_minister", #maybe deprecate this
		[
		
		(assign, ":walled_center_found", 0),
		(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(lt, ":walled_center_found", centers_begin),
			(store_faction_of_party, ":walled_center_faction", ":walled_center"),
			(eq, ":walled_center_faction", "fac_player_supporters_faction"),
			(neg|party_slot_ge, ":walled_center", slot_town_lord, active_npcs_begin), #ie, player or a reserved slot
			(assign, ":walled_center_found", ":walled_center"),
		(try_end),
		
		(troop_get_slot, ":old_location", "$g_player_minister", slot_troop_cur_center),
		(troop_set_slot, "$g_player_minister", slot_troop_cur_center, ":walled_center_found"),
		
		(try_begin),
			(neq, ":old_location", ":walled_center"),
			(str_store_party_name, s10, ":walled_center"),
			(str_store_troop_name, s11, "$g_player_minister"),
			(display_message, "str_s11_relocates_to_s10"),
		(try_end),
		
	])
	