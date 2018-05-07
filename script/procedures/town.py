from header import *


		# script_get_heroes_attached_to_center_aux
		# For internal use only
get_heroes_attached_to_center_aux	= (
	"get_heroes_attached_to_center_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_get_num_companion_stacks, ":num_stacks",":center_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
					(call_script, "script_get_heroes_attached_to_center_aux", ":attached_party", ":party_no_to_collect_heroes"),
				(try_end),
		])

		# script_get_heroes_attached_to_center
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
get_heroes_attached_to_center	= (
	"get_heroes_attached_to_center",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_clear, ":party_no_to_collect_heroes"),
				(call_script, "script_get_heroes_attached_to_center_aux", ":center_no", ":party_no_to_collect_heroes"),
				
				#rebellion changes begin -Arma
				(try_for_range, ":pretender", pretenders_begin, pretenders_end),
					(neq, ":pretender", "$supported_pretender"),
					(troop_slot_eq, ":pretender", slot_troop_cur_center, ":center_no"),
					(party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
				(try_end),
				
				#     (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
				#        (faction_slot_eq, ":rebel_faction", slot_faction_state, sfs_inactive_rebellion),
				#        (faction_slot_eq, ":rebel_faction", slot_faction_inactive_leader_location, ":center_no"),
				#        (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
				#        (party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
				#     (try_end),
				#rebellion changes end
				
				
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner_aux
		# For internal use only
get_heroes_attached_to_center_as_prisoner_aux	= (
	"get_heroes_attached_to_center_as_prisoner_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_get_num_prisoner_stacks, ":num_stacks",":center_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
					(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":attached_party", ":party_no_to_collect_heroes"),
				(try_end),
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
get_heroes_attached_to_center_as_prisoner	= (
	"get_heroes_attached_to_center_as_prisoner",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_clear, ":party_no_to_collect_heroes"),
				(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":center_no", ":party_no_to_collect_heroes"),
		])
		
		# script_give_center_to_faction
		# added dimplomacy
		# WARNING: modified by 1257dev
		# Input: arg1 = center_no, arg2 = faction
give_center_to_faction	= (
	"give_center_to_faction",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":faction_no"),
				
				##diplomacy begin
				(party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
				(try_begin),
					(party_slot_eq, ":center_no", slot_village_infested_by_bandits, "trp_peasant_woman"),
					(party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
				(try_end),
				(try_begin),
					(eq, "$g_constable_training_center", ":center_no"),
					(assign, "$g_constable_training_center", -1),
				(try_end),
				##diplomacy end
				(try_begin),
					(eq, ":faction_no", "fac_player_supporters_faction"),
					(faction_get_slot, ":player_faction_king", "fac_player_supporters_faction", slot_faction_leader),
					(eq, ":player_faction_king", "trp_player"),
					
					(try_begin),
						(is_between, ":center_no", walled_centers_begin, walled_centers_end),
						(assign, ":number_of_walled_centers_players_kingdom_has", 1),
					(else_try),
						(assign, ":number_of_walled_centers_players_kingdom_has", 0),
					(try_end),
					
					(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
						(store_faction_of_party, ":owner_faction_no", ":walled_center"),
						(eq, ":owner_faction_no", "fac_player_supporters_faction"),
						(val_add, ":number_of_walled_centers_players_kingdom_has", 1),
					(try_end),
					
					(ge, ":number_of_walled_centers_players_kingdom_has", 10),
					(unlock_achievement, ACHIEVEMENT_VICTUM_SEQUENS),
				(try_end),
				
				(try_begin),
					(check_quest_active, "qst_join_siege_with_army"),
					(quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, ":center_no"),
					(call_script, "script_abort_quest", "qst_join_siege_with_army", 0),
					#Reactivating follow army quest
					(faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
					(str_store_troop_name_link, s9, ":faction_marshall"),
					(setup_quest_text, "qst_follow_army"),
					(str_store_string, s2, "@{s9} wants you to resume following his army until further notice."),
					(call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
					(assign, "$g_player_follow_army_warnings", 0),
				(try_end),
				
				#(store_faction_of_party, ":old_faction", ":center_no"),
				(call_script, "script_give_center_to_faction_aux", ":center_no", ":faction_no"),
				(call_script, "script_update_village_market_towns"),
				
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(call_script, "script_faction_recalculate_strength", ":cur_faction"),
				(try_end),
				(assign, "$g_recalculate_ais", 1),
				#(call_script, "script_raf_set_ai_recalculation_flags", ":faction_no"),
				
				(try_begin),
					(eq, ":faction_no", "fac_player_supporters_faction"),
					(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
					(call_script, "script_activate_player_faction", "trp_player"),
				(try_end),
				
				#(call_script, "script_activate_deactivate_player_faction", ":old_faction"),
				#(try_begin),
				#(eq, ":faction_no", "fac_player_supporters_faction"),
				#(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				#(call_script, "script_give_center_to_lord", ":center_no", "trp_player", 0),
				
				#check with Armagan -- what is this here for?
				#(try_for_range, ":cur_village", villages_begin, villages_end),
				#(store_faction_of_party, ":cur_village_faction", ":cur_village"),
				#(eq, ":cur_village_faction", "fac_player_supporters_faction"),
				#(neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
				#(call_script, "script_give_center_to_lord", ":cur_village", "trp_player", 0),
				#(try_end),
				#(try_end),
		])
		
		# script_give_center_to_faction_aux
		# Input: arg1 = center_no, arg2 = faction
give_center_to_faction_aux	= (
	"give_center_to_faction_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":faction_no"),
				
				#(try_begin), #tom
				#(neq, ":center_no", -1), #tom extra check
				
				(store_faction_of_party, ":old_faction", ":center_no"),
				(party_set_faction, ":center_no", ":faction_no"),
				
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
					(gt, ":farmer_party", 0),
					(party_is_active, ":farmer_party"),
					(party_set_faction, ":farmer_party", ":faction_no"),
				(try_end),
				
				(try_begin),
					#This bit of seemingly redundant code (the neq condition) is designed to prevent a bug that occurs when a player first conquers a center -- apparently this script is called again AFTER it is handed to a lord
					#Without this line, then the player's dialog selection does not have any affect, because town_lord is set again to stl_unassigned after the player makes his or her choice
					(neq, ":faction_no", ":old_faction"),
					
					(party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
					(party_get_slot, ":old_town_lord", ":center_no", slot_town_lord),
					(party_set_slot, ":center_no", slot_town_lord, stl_unassigned),
					(party_set_banner_icon, ":center_no", 0),#Removing banner
					(call_script, "script_update_faction_notes", ":old_faction"),
				(try_end),
				
				(call_script, "script_update_faction_notes", ":faction_no"),
				(call_script, "script_update_center_notes", ":center_no"),
				
				(try_begin),
					(ge, ":old_town_lord", 0),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(call_script, "script_update_troop_notes", ":old_town_lord"),
				(try_end),
				
				(try_for_range, ":other_center", centers_begin, centers_end),
					(party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
					(call_script, "script_give_center_to_faction_aux", ":other_center", ":faction_no"),
				(try_end),
				# (else_try), #tom
				# (assign, reg0, ":faction_no"),
				# (display_message, "@{reg0} bugova"),
				# (try_end), #tom
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner_aux
		# For internal use only
get_heroes_attached_to_center_as_prisoner_aux	= (
	"get_heroes_attached_to_center_as_prisoner_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_get_num_prisoner_stacks, ":num_stacks",":center_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
				(try_end),
				(party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
				(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
					(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
					(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":attached_party", ":party_no_to_collect_heroes"),
				(try_end),
		])
		
		
		# script_get_heroes_attached_to_center_as_prisoner
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
get_heroes_attached_to_center_as_prisoner	= (
	"get_heroes_attached_to_center_as_prisoner",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":party_no_to_collect_heroes"),
				(party_clear, ":party_no_to_collect_heroes"),
				(call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":center_no", ":party_no_to_collect_heroes"),
		])


		# script_give_center_to_faction_aux
		# WARNING modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = faction
give_center_to_faction_aux	= (
	"give_center_to_faction_aux",
			[
				(store_script_param_1, ":center_no"),
				(store_script_param_2, ":faction_no"),
				
				#(try_begin), #tom
				#(neq, ":center_no", -1), #tom extra check
				
				(store_faction_of_party, ":old_faction", ":center_no"),
				(party_set_faction, ":center_no", ":faction_no"),
				
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_village),
					(party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
					(gt, ":farmer_party", 0),
					(party_is_active, ":farmer_party"),
					(party_set_faction, ":farmer_party", ":faction_no"),
				(try_end),
				
				(try_begin),
					#This bit of seemingly redundant code (the neq condition) is designed to prevent a bug that occurs when a player first conquers a center -- apparently this script is called again AFTER it is handed to a lord
					#Without this line, then the player's dialog selection does not have any affect, because town_lord is set again to stl_unassigned after the player makes his or her choice
					(neq, ":faction_no", ":old_faction"),
					
					(party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
					(party_get_slot, ":old_town_lord", ":center_no", slot_town_lord),
					(party_set_slot, ":center_no", slot_town_lord, stl_unassigned),
					(party_set_banner_icon, ":center_no", 0),#Removing banner
					(call_script, "script_update_faction_notes", ":old_faction"),
				(try_end),
				
				(call_script, "script_update_faction_notes", ":faction_no"),
				(call_script, "script_update_center_notes", ":center_no"),
				
				(try_begin),
					(ge, ":old_town_lord", 0),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(call_script, "script_update_troop_notes", ":old_town_lord"),
				(try_end),
				
				(try_for_range, ":other_center", centers_begin, centers_end),
					(party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
					(call_script, "script_give_center_to_faction_aux", ":other_center", ":faction_no"),
				(try_end),
				# (else_try), #tom
				# (assign, reg0, ":faction_no"),
				# (display_message, "@{reg0} bugova"),
				# (try_end), #tom
		])

# script_refresh_village_merchant_inventory
# Input: arg1 = village_no
# Output: none
refresh_village_merchant_inventory = (
	"refresh_village_merchant_inventory",
		[
			(store_script_param_1, ":village_no"),
			(party_get_slot, ":merchant_troop", ":village_no", slot_town_elder),
			(reset_item_probabilities,0),

		(assign, ":total_probability", 0),
			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
		
			(call_script, "script_center_get_production", ":village_no", ":cur_goods"),
		(assign, ":cur_probability", reg0),

		(val_max, ":cur_probability", 5),
				
		(val_add, ":total_probability", ":cur_probability"),
			(try_end),
		
		(try_begin),
		(party_get_slot, ":prosperity", ":village_no", slot_town_prosperity),
		(val_div, ":prosperity", 15), #up to 6
		(store_add, ":number_of_items_in_village", ":prosperity", 1),
		(try_end),

			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
			(call_script, "script_center_get_production", ":village_no", ":cur_goods"),
		(assign, ":cur_probability", reg0),

		(val_max, ":cur_probability", 5),

				(val_mul, ":cur_probability", ":number_of_items_in_village"),
		(val_mul, ":cur_probability", 100),
		(val_div, ":cur_probability", ":total_probability"),

				(set_item_probability_in_merchandise, ":cur_goods", ":cur_probability"),
			(try_end),

			(troop_clear_inventory, ":merchant_troop"),
			(troop_add_merchandise, ":merchant_troop", itp_type_goods, ":number_of_items_in_village"),
			(troop_ensure_inventory_space, ":merchant_troop", 80),

			#Adding 1 prosperity to the village while reducing each 3000 gold from the elder
			(store_troop_gold, ":gold",":merchant_troop"),
			(try_begin),
				(gt, ":gold", 3500),
				(store_div, ":prosperity_added", ":gold", 3000),
				(store_mul, ":gold_removed", ":prosperity_added", 3000),
				(troop_remove_gold, ":merchant_troop", ":gold_removed"),
				(call_script, "script_change_center_prosperity", ":village_no", ":prosperity_added"),
			(try_end),
	])
		

# script_refresh_village_defenders
# Input: arg1 = village_no
# Output: none
refresh_village_defenders = (
		"refresh_village_defenders",
			[
				(store_script_param_1, ":village_no"),
				
				(assign, ":ideal_size", 50),
				(try_begin),
					(party_get_num_companions, ":party_size", ":village_no"),
					(lt, ":party_size", ":ideal_size"),
					(party_add_template, ":village_no", "pt_village_defenders"),
				(try_end),
		])



#script_update_mercenary_units_of_towns
# WARNING: heavily modified by 1257AD devs
# INPUT: none
# OUTPUT: none
update_mercenary_units_of_towns = (
	"update_mercenary_units_of_towns",
			[
		 (try_for_range, ":town_no", towns_begin, towns_end),
			 #(party_get_slot, ":regional_mercs", ":town_no", slot_regional_mercs),
			 (party_get_slot, ":special1", ":town_no", slot_spec_mercs1),
			 (party_get_slot, ":special2", ":town_no", slot_spec_mercs2),
		 
		 (assign, ":merc_slot", slot_regional_mercs),
		 (try_begin),
			 (gt, ":special1", 0),
			 (gt, ":special2", 0),
			 (store_random_in_range, ":random", 0, 3),
			 (try_begin),
				 (eq, ":random", 1),
			 (assign, ":merc_slot", slot_spec_mercs1),
			 (else_try),
			 (eq, ":random", 2),
			 (assign, ":merc_slot", slot_spec_mercs2),
			 (try_end),
		 (else_try),
			 (gt, ":special1", 0),
			 (store_random_in_range, ":random", 0, 2),
			 (try_begin),
				 (eq, ":random", 1),
			 (assign, ":merc_slot", slot_spec_mercs1),
			 (try_end),	 
		 (else_try),
			 (gt, ":special2", 0),
			 (store_random_in_range, ":random", 0, 2),
			 (try_begin),
				 (eq, ":random", 1),
			 (assign, ":merc_slot", slot_spec_mercs2),
			 (try_end),  
		 (try_end),

		 (assign, ":troop_no", "trp_merc_euro_spearman"),
		 (try_begin),
			(party_slot_eq, ":town_no", ":merc_slot", generic_euro),
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_balt),
			(store_random_in_range, ":troop_no", "trp_merc_balt_spearman", "trp_merc_mamluke_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_maghreb),
			(store_random_in_range, ":troop_no", "trp_merc_maghreb_spearman", "trp_merc_rus_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_rus),
			(store_random_in_range, ":troop_no", "trp_merc_rus_spearman", "trp_merc_latin_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_latin),
			(store_random_in_range, ":troop_no", "trp_merc_latin_spearman", "trp_merc_balkan_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_balkan),
			(store_random_in_range, ":troop_no", "trp_merc_balkan_spearman", "trp_merc_scan_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_scandinavian),
			(store_random_in_range, ":troop_no", "trp_merc_scan_spearman", "trp_merc_gaelic_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_gaelic),
			(store_random_in_range, ":troop_no", "trp_merc_gaelic_spearman", "trp_genoese_crossbowman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", generic_mamluk),
			(store_random_in_range, ":troop_no", "trp_merc_mamluke_spearman", "trp_merc_maghreb_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_barbantine),
			(store_random_in_range, ":troop_no", "trp_merc_brabantine_spearman", "trp_merc_welsh_bowman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_georgians),
			(store_random_in_range, ":troop_no", "trp_georgian_lancer", "trp_mercenaries_end"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_sicily_muslims),
			(store_random_in_range, ":troop_no", "trp_merc_sicily_foot_archer_1", "trp_cuman_tribesman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_turkopoles),
			(assign, ":troop_no", "trp_crusader_turkopole"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_cumans),
			(store_random_in_range, ":troop_no", "trp_cuman_skirmisher", "trp_farmer"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_kwarezmians),
			(store_random_in_range, ":troop_no", "trp_kwarezmian_range", "trp_mordovian_foot"),	
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_mordovians),
			(store_random_in_range, ":troop_no", "trp_mordovian_foot", "trp_kipchak_range"),	
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_kipchaks),	
			(store_random_in_range, ":troop_no", "trp_kipchak_range", "trp_finn_village_recruit"),	
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_geonese),
			(store_random_in_range, ":troop_no", "trp_genoese_crossbowman", "trp_merc_brabantine_spearman"),	
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_teutons),
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_hospitaliers),	
		 (store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_templars),	
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_lazarus),
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_santiago),
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_calatrava),	
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_saint_thomas),	
			(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
		(else_try),
			(party_slot_eq, ":town_no", ":merc_slot", merc_varangians),	
			(assign, ":troop_no", "trp_varangian_guard"),
		(try_end),
			(party_set_slot, ":town_no", slot_center_mercenary_troop_type, ":troop_no"),
		(store_random_in_range, ":amount", 3, 10), #tom was 3, 8
		(party_set_slot, ":town_no", slot_center_mercenary_troop_amount, ":amount"),
		(try_end),
		])


		#script_update_volunteer_troops_in_village
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = center_no
		# OUTPUT: none
update_volunteer_troops_in_village = (
	"update_volunteer_troops_in_village",
			[
				(store_script_param, ":center_no", 1),
				(party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
				(party_get_slot, ":center_culture", ":center_no", slot_center_culture),
				
		##tom
				#(call_script, "script_raf_get_aor_culture", ":center_no"),
		(party_get_slot, ":orig_faction", ":center_no", slot_center_original_faction),
		(store_faction_of_party, ":cur_faction", ":center_no"),
		
				(call_script, "script_get_orig_culture", ":orig_faction", ":cur_faction", ":center_culture"),
				(assign, ":center_culture", reg0),
				
		#if not a teutonic knight - set it to native culture
		(try_begin),
			(neq, "$players_kingdom", fac_kingdom_1),
			(eq, ":center_culture", fac_culture_teutonic),
			(party_get_slot, ":center_culture", ":center_no", slot_center_culture),
		(try_end),
		##tom
		
				(try_begin),
					(party_slot_eq, ":center_no", slot_party_type, spt_town),
					#(faction_get_slot, ":center_culture", "$players_kingdom", slot_faction_culture),
					(faction_get_slot, ":volunteer_troop", ":center_culture", slot_faction_tier_1_town_troop),
				(else_try),
					(party_slot_eq, ":center_no", slot_party_type, spt_castle),
					#(faction_get_slot, ":center_culture", "$players_kingdom", slot_faction_culture),
					(faction_get_slot, ":volunteer_troop", ":center_culture", slot_faction_tier_1_castle_troop),
				(else_try),
					#(faction_get_slot, ":center_culture", "$players_kingdom", slot_faction_culture),
					(faction_get_slot, ":volunteer_troop", ":center_culture", slot_faction_tier_1_troop),
				(try_end),
				
				#(try_end),
				# end
				
				#(faction_get_slot, ":volunteer_troop", ":center_culture", slot_faction_tier_1_troop),
				
				# rafi hospitallers/templars
				# (store_faction_of_party, ":faction", ":center_no"),
				# (try_begin),
				# (eq, ":faction", "fac_kingdom_23"),
				# (try_begin),
				# (party_slot_eq, ":center_no", slot_party_type, spt_village),
				# (party_get_slot, ":town", ":center_no", slot_village_bound_center),
				# (else_try),
				# (assign, ":town", ":center_no"),
				# (try_end),
				
				# (party_get_slot, ":leader", ":town", slot_town_lord),
				# (try_begin),
				# (eq, ":leader", "trp_knight_23_1"),
				# (try_begin),
				# (party_slot_eq, ":center_no", slot_party_type, spt_village),
				# (assign, ":volunteer_troop", "trp_hospitaller_village_recruit"),
				# (else_try),
				# (party_slot_eq, ":center_no", slot_party_type, spt_castle),
				# (assign, ":volunteer_troop", "trp_hospitaller_postulant"),
				# (else_try),
				# (party_slot_eq, ":center_no", slot_party_type, spt_town),
				# (assign, ":volunteer_troop", "trp_hospitaller_town_recruit"),
				# (try_end),
				# (else_try),
				# (eq, ":leader", "trp_knight_23_2"),
				# (try_begin),
				# (party_slot_eq, ":center_no", slot_party_type, spt_village),
				# (assign, ":volunteer_troop", "trp_iberian_village_recruit"),
				# (else_try),
				# (party_slot_eq, ":center_no", slot_party_type, spt_castle),
				# (assign, ":volunteer_troop", "trp_crusader_turkopole"),
				# (else_try),
				# (party_slot_eq, ":center_no", slot_party_type, spt_town),
				# (assign, ":volunteer_troop", "trp_templar_town_recruit"),
				# (try_end),
				# (else_try),
				# (eq, ":leader", "trp_knight_23_6"),
				# (try_begin),
				# (party_slot_eq, ":center_no", slot_party_type, spt_village),
				# (assign, ":volunteer_troop", "trp_teutonic_village_recruit"),
				# (else_try),
				# (party_slot_eq, ":center_no", slot_party_type, spt_castle),
				# (assign, ":volunteer_troop", "trp_teutonic_postulant"),
				# (else_try),
				# (party_slot_eq, ":center_no", slot_party_type, spt_town),
				# (assign, ":volunteer_troop", "trp_teutonic_town_recruit"),
				# (try_end),
				# (try_end),
				# (try_end),
				# end rafi
				
				(assign, ":volunteer_troop_tier", 1),
				(store_div, ":tier_upgrades", ":player_relation", 10),
				(try_for_range, ":unused", 0, ":tier_upgrades"),
					(store_random_in_range, ":random_no", 0, 100),
					(lt, ":random_no", 10),
					(store_random_in_range, ":random_no", 0, 2),
					(troop_get_upgrade_troop, ":upgrade_troop_no", ":volunteer_troop", ":random_no"),
					(try_begin),
						(le, ":upgrade_troop_no", 0),
						(troop_get_upgrade_troop, ":upgrade_troop_no", ":volunteer_troop", 0),
					(try_end),
					(gt, ":upgrade_troop_no", 0),
					(val_add, ":volunteer_troop_tier", 1),
					(assign, ":volunteer_troop", ":upgrade_troop_no"),
				(try_end),
				
				(assign, ":upper_limit", 14), # rafi double this shit
				(try_begin),
					(ge, ":player_relation", 5),
					(assign, ":upper_limit", ":player_relation"),
					(val_div, ":upper_limit", 2),
					(val_add, ":upper_limit", 10),
				(else_try),
					(lt, ":player_relation", 0),
					(assign, ":upper_limit", 0),
				(try_end),
				
				(val_mul, ":upper_limit", 3),
				(store_add, ":amount_random_divider", 2, ":volunteer_troop_tier"),
				(val_div, ":upper_limit", ":amount_random_divider"),
				
				(store_random_in_range, ":amount", 0, ":upper_limit"),
				(party_set_slot, ":center_no", slot_center_volunteer_troop_type, ":volunteer_troop"),
				(party_set_slot, ":center_no", slot_center_volunteer_troop_amount, ":amount"),
		])
		
	
		#script_update_npc_volunteer_troops_in_village - tom rewriten
		# no longer behaves like in native!
		# WARNING: heavily modified by 1257AD devs
		# INPUT: arg1 = center_no
		# OUTPUT: none
update_npc_volunteer_troops_in_village = (
	"update_npc_volunteer_troops_in_village",
			[
				(store_script_param, ":center_no", 1),
			 
		(call_script, "script_select_mercenary_troop", ":center_no"),
		(assign,  ":volunteer_troop", reg0),

				(assign, ":upper_limit", 12),
		
				(store_random_in_range, ":amount", 0, ":upper_limit"),
				(party_set_slot, ":center_no", slot_center_npc_volunteer_troop_type, ":volunteer_troop"),
				(party_set_slot, ":center_no", slot_center_npc_volunteer_troop_amount, ":amount"),
		])
		

		#script_update_villages_infested_by_bandits
		# INPUT: none
		# OUTPUT: none
update_villages_infested_by_bandits = (
	"update_villages_infested_by_bandits",
			[(try_for_range, ":village_no", villages_begin, villages_end),
					(try_begin),
						(check_quest_active, "qst_eliminate_bandits_infesting_village"),
						(quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, ":village_no"),
						(quest_get_slot, ":cur_state", "qst_eliminate_bandits_infesting_village", slot_quest_current_state),
						(val_add, ":cur_state", 1),
						(try_begin),
							(lt, ":cur_state", 3),
							(quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_current_state, ":cur_state"),
						(else_try),
							(party_set_slot, ":village_no", slot_village_infested_by_bandits, 0),
							(call_script, "script_abort_quest", "qst_eliminate_bandits_infesting_village", 2),
						(try_end),
					(else_try),
						(check_quest_active, "qst_deal_with_bandits_at_lords_village"),
						(quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, ":village_no"),
						(quest_get_slot, ":cur_state", "qst_deal_with_bandits_at_lords_village", slot_quest_current_state),
						(val_add, ":cur_state", 1),
						(try_begin),
							(lt, ":cur_state", 3),
							(quest_set_slot, "qst_deal_with_bandits_at_lords_village", slot_quest_current_state, ":cur_state"),
						(else_try),
							(party_set_slot, ":village_no", slot_village_infested_by_bandits, 0),
							(call_script, "script_abort_quest", "qst_deal_with_bandits_at_lords_village", 2),
						(try_end),
					(else_try),
						(party_set_slot, ":village_no", slot_village_infested_by_bandits, 0),
						(store_random_in_range, ":random_no", 0, 100),
						(assign, ":continue", 1),
						(try_begin),
							(check_quest_active, "qst_collect_taxes"),
							(quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, ":village_no"),
							(assign, ":continue", 0),
						(else_try),
							(check_quest_active, "qst_train_peasants_against_bandits"),
							(quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, ":village_no"),
							(assign, ":continue", 0),
						(try_end),
						(eq, ":continue", 1),
						(lt, ":random_no", 3),
						(store_random_in_range, ":random_no", 0, 3),
						(try_begin),
							(eq, ":random_no", 0),
							(assign, ":bandit_troop", "trp_bandit"),
						(else_try),
							(eq, ":random_no", 1),
							(assign, ":bandit_troop", "trp_mountain_bandit"),
						(else_try),
							(assign, ":bandit_troop", "trp_forest_bandit"),
						(try_end),
						(party_set_slot, ":village_no", slot_village_infested_by_bandits, ":bandit_troop"),
						#Reduce prosperity of the village by 3: reduce to -1
						(call_script, "script_change_center_prosperity", ":village_no", -1),
						(val_add, "$newglob_total_prosperity_from_bandits", -1),
						(try_begin),
							(eq, "$cheat_mode", 2),
							(str_store_party_name, s1, ":village_no"),
							(display_message, "@{!}DEBUG --{s1} is infested by bandits."),
						(try_end),
					(try_end),
				(try_end),
		])



		#script_village_recruit_volunteers_recruit
		# INPUT: none
		# OUTPUT: none
village_recruit_volunteers_recruit = (
	"village_recruit_volunteers_recruit",
			[
				(store_script_param, ":recruit_amount", 1),
				
				(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
				(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
				
				(try_begin),
					(gt, ":recruit_amount", 0),
					(lt, ":recruit_amount", ":volunteer_amount"),
					(assign, ":volunteer_amount", ":recruit_amount"),
				(try_end),
				
				(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
				(val_min, ":volunteer_amount", ":free_capacity"),
				(store_troop_gold, ":gold", "trp_player"),
				
				(assign, ":divisor", recruitment_cost_village),
				
				(try_begin),
					(party_slot_eq, "$current_town", slot_party_type, spt_castle),
					(assign, ":divisor", recruitment_cost_castle),
				(else_try),
					(party_slot_eq, "$current_town", slot_party_type, spt_town),
					(assign, ":divisor", recruitment_cost_town),
				(try_end),
				
				(store_div, ":gold_capacity", ":gold", ":divisor"),#10 denars per man
				
				(val_min, ":volunteer_amount", ":gold_capacity"),
				(party_add_members, "p_main_party", ":volunteer_troop", ":volunteer_amount"),
				
				(try_begin),
					(gt, ":recruit_amount", 0),
					(party_get_slot, ":volunteers", "$current_town", slot_center_volunteer_troop_amount),
					(val_sub, ":volunteers", ":recruit_amount"),
					(try_begin),
						(le, ":volunteers", 0),
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
					(else_try),
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, ":volunteers"),
					(try_end),
				(else_try),
					(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
				(try_end),
				
				(store_mul, ":cost", ":volunteer_amount", ":divisor"),#10 denars per man
				
				(troop_remove_gold, "trp_player", ":cost"),
		])		

#script_center_get_item_consumption
	#STUB SCRIPT
	#it might be easier to monitor whether prices are following an intuitive pattern if we separate production from consumption
	#the current system still works very well, however
center_get_item_consumption =  (
	"center_get_item_consumption",
		[
	])

#script_change_center_prosperity
		# INPUT: arg1 = center_no, arg2 = difference
		# OUTPUT: none
change_center_prosperity = (
	"change_center_prosperity",
			[(store_script_param, ":center_no", 1),
				(store_script_param, ":difference", 2),
				(party_get_slot, ":old_prosperity", ":center_no", slot_town_prosperity),
				(store_add, ":new_prosperity", ":old_prosperity", ":difference"),
				(val_clamp, ":new_prosperity", 0, 100),
				(store_div, ":old_state", ":old_prosperity", 20),
				(store_div, ":new_state", ":new_prosperity", 20),
				
				(try_begin),
					(neq, ":old_state", ":new_state"),
					(neg|is_between, ":center_no", castles_begin, castles_end),
					
					(str_store_party_name_link, s2, ":center_no"),
					(call_script, "script_get_prosperity_text_to_s50", ":center_no"),
					(str_store_string, s3, s50),
					(party_set_slot, ":center_no", slot_town_prosperity, ":new_prosperity"),
					(call_script, "script_get_prosperity_text_to_s50", ":center_no"),
					(str_store_string, s4, s50),
					(try_begin),
						(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
						(display_message, "@Prosperity of {s2} has changed from {s3} to {s4}."),
					(try_end),
					(call_script, "script_update_center_notes", ":center_no"),
				(else_try),
					(party_set_slot, ":center_no", slot_town_prosperity, ":new_prosperity"),
				(try_end),
				
				(try_begin),
					(store_current_hours, ":hours"),
					(gt, ":hours", 1),
					(store_sub, ":actual_difference", ":new_prosperity", ":old_prosperity"),
					(try_begin),
						(lt, ":actual_difference", 0),
						(val_add, "$newglob_total_prosperity_losses", ":actual_difference"),
					(else_try),
						(gt, ":actual_difference", 0),
						(val_add, "$newglob_total_prosperity_gains", ":actual_difference"),
					(try_end),
				(try_end),
				
				#This will add up all non-trade prosperity
				(try_begin),
					(eq, "$cheat_mode", 3),
					(assign, reg4, "$newglob_total_prosperity_from_bandits"),
					(assign, reg5, "$newglob_total_prosperity_from_caravan_trade"),
					(assign, reg7, "$newglob_total_prosperity_from_villageloot"),
					(assign, reg8, "$newglob_total_prosperity_from_townloot"),
					(assign, reg9, "$newglob_total_prosperity_from_village_trade"),
					(assign, reg10, "$newglob_total_prosperity_from_convergence"),
					(assign, reg11, "$newglob_total_prosperity_losses"),
					(assign, reg12, "$newglob_total_prosperity_gains"),
					(display_message, "@{!}DEBUG: Total prosperity actual losses: {reg11}"),
					(display_message, "@{!}DEBUG: Total prosperity actual gains: {reg12}"),
					
					(display_message, "@{!}DEBUG: Prosperity changes from random bandits: {reg4}"),
					(display_message, "@{!}DEBUG: Prosperity changes from caravan trades: {reg5}"),
					(display_message, "@{!}DEBUG: Prosperity changes from farmer trades: {reg9}"),
					(display_message, "@{!}DEBUG: Prosperity changes from looted villages: {reg7}"),
					(display_message, "@{!}DEBUG: Prosperity changes from sieges: {reg8}"),
					(display_message, "@{!}DEBUG: Theoretical prosperity changes from convergence: {reg10}"),
				(try_end),
				
		])