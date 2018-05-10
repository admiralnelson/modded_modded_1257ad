from header import *

#script_dplmc_send_recruiter
	#INPUT: number_of_recruits, faction_of_recruits,recruit_type
	#OUTPUT: none
dplmc_send_recruiter =	(
	"dplmc_send_recruiter",
		[
		(store_script_param, ":number_of_recruits", 1),
		#daedalus begin
		(store_script_param, ":faction_of_recruits", 2),
		(store_script_param, ":recruit_type", 3),
		#daedalus end
		(assign, ":expenses", ":number_of_recruits"),
		#(val_mul, ":expenses", 20),
		(val_mul, ":expenses", reg22),
		#(val_add, ":expenses", 10),
		(val_add, ":expenses", 250),
		(call_script, "script_dplmc_withdraw_from_treasury", ":expenses"),
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_dplmc_recruiter"),
		(assign,":spawned_party",reg0),
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_hold),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_recruiter),
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits, ":number_of_recruits"),
		#daedalus begin
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits_faction, ":faction_of_recruits"),
		#daedalus end
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_origin, "$current_town"),
		(assign, ":faction", "$players_kingdom"),
		(party_set_faction, ":spawned_party", ":faction"),
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_recruitment_type, ":recruit_type"),
	])

	
	#script_dplmc_withdraw_from_treasury
	#INPUT: amount
	#OUTPUT:none
dplmc_withdraw_from_treasury =	(
	"dplmc_withdraw_from_treasury",
		[
		(store_script_param_1, ":amount"),
		(troop_remove_gold, "trp_household_possessions", ":amount"),
		(assign, reg0, ":amount"),
		(play_sound, "snd_money_paid"),
		(display_message, "@{reg0} denars removed from treasury."),
	])
	

	#script_dplmc_start_alliance_between_kingdoms, 20 days alliance, 40 days truce after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
dplmc_start_alliance_between_kingdoms =	(
	"dplmc_start_alliance_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 15),
		(val_max, ":relation", 40),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 15),
			(val_max, ":relation", 40),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 15),
			(val_max, ":relation", 40),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded an alliance with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 80),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 80),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
		
		# share wars
		(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
			(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			(neq, ":kingdom_a", ":faction_no"),
			(neq, ":kingdom_b", ":faction_no"),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
			#result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
			(eq, reg0, -2),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
			(ge, reg0, -1),
			(call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", 1),
		(try_end),
		(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
			(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			(neq, ":kingdom_a", ":faction_no"),
			(neq, ":kingdom_b", ":faction_no"),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
			#result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
			(eq, reg0, -2),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
			(ge, reg0, -1),
			(call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", 1),
		(try_end),
	])
	
	#script_dplmc_start_defensive_between_kingdoms, 20 days defensive: 20 days trade aggreement, 20 days non-aggression after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
dplmc_start_defensive_between_kingdoms =	(
	"dplmc_start_defensive_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 10),
		(val_max, ":relation", 30),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 10),
			(val_max, ":relation", 30),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 10),
			(val_max, ":relation", 30),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded a defensive pact with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
			
			
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 60),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 60),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
	])


	#script_dplmc_start_trade_between_kingdoms, 20 days trade aggreement, 20 days non-aggression after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
dplmc_start_trade_between_kingdoms =	(
	"dplmc_start_trade_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 5),
		(val_max, ":relation", 20),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 5),
			(val_max, ":relation", 20),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 5),
			(val_max, ":relation", 20),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded a trade agreement with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
			
			
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
	])
	

	#script_dplmc_start_nonaggression_between_kingdoms, 20 days non-aggression
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
dplmc_start_nonaggression_between_kingdoms =	(
	"dplmc_start_nonaggression_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 3),
		(val_max, ":relation", 10),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 3),
			(val_max, ":relation", 10),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 3),
			(val_max, ":relation", 10),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded a non aggression pact with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_nonaggression_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
			
			
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 20),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
	])


	#script_dplmc_player_center_surrender
	#INPUT: center_no
	#OUTPUT: none
dplmc_player_center_surrender =	(
	"dplmc_player_center_surrender",
		[
		(store_script_param, ":center_no", 1),
		
		#protect player for 24 hours
		(store_current_hours,":protected_until"),
		(val_add, ":protected_until", 48),
		(party_get_slot, ":besieger", ":center_no", slot_center_is_besieged_by),
		(store_faction_of_party, ":besieger_faction",":besieger"),
		(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
		
		(party_set_slot,":besieger",slot_party_ignore_player_until,":protected_until"),
		(party_ignore_player, ":besieger", 48),
		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":besieger_faction"),
			(troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
			(party_is_active, ":led_party"),
			
			(party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
			(party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),
			
			(party_is_active, ":besieger"),
			(store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
			(lt, ":distance_to_marshal", 20),
			
			(party_set_slot,":led_party",slot_party_ignore_player_until,":protected_until"),
			(party_ignore_player, ":led_party", 48),
		(try_end),
		
		(party_set_faction,"$current_town","fac_neutral"), #temporarily erase faction so that it is not the closest town
		(party_get_num_attached_parties, ":num_attached_parties_to_castle",":center_no"),
		(try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
			(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":iap"),
			(party_detach, ":attached_party"),
			(party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
			(eq, ":attached_party_type", spt_kingdom_hero_party),
			(neq, ":attached_party_type", "p_main_party"),
			(store_faction_of_party, ":attached_party_faction", ":attached_party"),
			(call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
			(try_begin),
			(gt, reg0, 0),
			(call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
			(else_try),
			(call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, ":center_no"),
			(try_end),
		(try_end),
		(call_script, "script_party_remove_all_companions", ":center_no"),
		(change_screen_return),
		(party_collect_attachments_to_party, ":center_no", "p_collective_enemy"), #recalculate so that
		(call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
		
		(call_script, "script_give_center_to_faction", "$current_town", ":besieger_faction"),
		(call_script, "script_order_best_besieger_party_to_guard_center", ":center_no", ":besieger_faction"),
		
		#relation and controversy
		(call_script, "script_change_player_relation_with_troop", ":enemy_party_leader", 2),
		(try_begin),
			(gt, "$players_kingdom", 0),
			(neq, "$players_kingdom", "fac_player_supporters_faction"),
			(neq, "$players_kingdom", "fac_player_faction"),
			(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
			(neq, ":faction_leader", "trp_player"),
			(call_script, "script_change_player_relation_with_troop", ":faction_leader", -2),
		(try_end),
		
		(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
		(val_add, ":controversy", 4),
		(val_min, ":controversy", 100),
		(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
	])

	#script_dplmc_send_messenger_to_troop
	#INPUT: target_troop, message, orders_object
	#OUTPUT: none
dplmc_send_messenger_to_troop =	(
	"dplmc_send_messenger_to_troop",
		[
		(store_script_param, ":target_troop", 1),
		(store_script_param, ":message", 2),
		(store_script_param, ":orders_object", 3),
		
		(troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
		
		(try_begin),
			(eq, ":message", spai_accompanying_army),
			(assign, ":orders_object", "p_main_party"),
		(try_end),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_messenger_party"),
		(assign,":spawned_party",reg0),
		(party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
		(store_faction_of_troop, ":player_faction", "trp_player"),
		(party_set_faction, ":spawned_party", ":player_faction"),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_messenger),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
		(party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Send message to {s13}"),
		(try_end),
		])

	#script_dplmc_send_messenger_to_party
	#INPUT: target_party, message, orders_object
	#OUTPUT: none
dplmc_send_messenger_to_party =	(
	"dplmc_send_messenger_to_party",
		[
		(store_script_param, ":target_party", 1),
		(store_script_param, ":message", 2),
		(store_script_param, ":orders_object", 3),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_messenger_party"),
		(assign,":spawned_party",reg0),
		(party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
		(party_set_faction, ":spawned_party", "fac_player_faction"),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_messenger),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
		(party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Send message to {s13}"),
		(try_end),
		])

	#script_dplmc_send_gift
	#INPUT: target_troop, gift
	#OUTPUT: none
dplmc_send_gift =	(
	"dplmc_send_gift",
		[
		(store_script_param, ":target_troop", 1),
		(store_script_param, ":gift", 2),
		
		(try_begin),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
			(troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
		(else_try),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
			(troop_get_slot, ":target_party", ":target_troop", slot_troop_cur_center),
		(try_end),
		
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_item_name, s12, ":gift"),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
		(try_end),
		
		(call_script, "script_dplmc_withdraw_from_treasury", 50),
		(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
		(try_begin),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
			(assign, ":amount", 150),
			(try_for_range, ":inventory_slot", 0, ":capacity"),
			(gt, ":amount", 0),
			(troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
			(eq, ":item", ":gift"),
			(troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
			(try_begin),
				(le, ":tmp_amount", ":amount"),
				(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
				(val_sub, ":amount", ":tmp_amount"),
			(else_try),
				(val_sub, ":tmp_amount", ":amount"),
				(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
				(assign, ":amount", 0),
			(try_end),
			(try_end),
		(else_try),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
			(troop_remove_item, "trp_household_possessions", ":gift"),
		(try_end),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
		(assign,":spawned_party",reg0),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
		(party_set_slot, ":spawned_party",  slot_party_orders_object,  ":target_troop"),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
		(troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
	])
	
	#script_dplmc_send_gift_to_center
	#INPUT: target_party, gift
	#OUTPUT: none
dplmc_send_gift_to_center =	(
	"dplmc_send_gift_to_center",
		[
		(store_script_param, ":target_party", 1),
		(store_script_param, ":gift", 2),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_item_name, s12, ":gift"),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
		(try_end),
		
		(call_script, "script_dplmc_withdraw_from_treasury", 50),
		(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
		(assign, ":amount", 300),
		(try_for_range, ":inventory_slot", 0, ":capacity"),
			(gt, ":amount", 0),
			(troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
			(eq, ":item", ":gift"),
			(troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
			(try_begin),
			(le, ":tmp_amount", ":amount"),
			(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
			(val_sub, ":amount", ":tmp_amount"),
			(else_try),
			(val_sub, ":tmp_amount", ":amount"),
			(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
			(assign, ":amount", 0),
			(try_end),
		(try_end),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
		(assign,":spawned_party",reg0),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
		(party_set_slot, ":spawned_party",  slot_party_orders_object, 0),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
		(troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
		(troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
	])
	
dplmc_pay_into_treasury =	(
	"dplmc_pay_into_treasury",
	  [
		(store_script_param_1, ":amount"),
		(troop_add_gold, "trp_household_possessions", ":amount"),
		(assign, reg0, ":amount"),
		(play_sound, "snd_money_received"),
		(display_message, "@{reg0} denars added to treasury."),
	])