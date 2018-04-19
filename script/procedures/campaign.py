from header import *

#script_player_arrived
# Called in start_phase_3 game_menus. 
# INPUT: none
# OUTPUT: none
player_arrived = (
	"player_arrived",
		[
			(assign, ":player_faction_culture", "fac_culture_western"),
			(faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, ":player_faction_culture"),
			(faction_set_slot, "fac_player_faction",  slot_faction_culture, ":player_faction_culture"),
	])

# script_game_event_party_encounter:
# This script is called from the game engine whenever player party encounters another party or a battle on the world map
# INPUT: param1: encountered_party, param2: second encountered_party (if this was a battle)
# OUTPUT: none
game_event_party_encounter = (
	"game_event_party_encounter",
		[
			(store_script_param_1, "$g_encountered_party"),
			(store_script_param_2, "$g_encountered_party_2"),# encountered_party2 is set when we come across a battle or siege, otherwise it's a negative value
			#       (store_encountered_party, "$g_encountered_party"),
			#       (store_encountered_party2,"$g_encountered_party_2"), # encountered_party2 is set when we come across a battle or siege, otherwise it's a minus value
			(store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
			(store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
			
			(party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
			(party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),
			#       (try_begin),
			#         (gt, "$g_encountered_party_2", 0),
			#         (store_faction_of_party, "$g_encountered_party_2_faction","$g_encountered_party_2"),
			#         (store_relation, "$g_encountered_party_2_relation", "$g_encountered_party_2_faction", "fac_player_faction"),
			#         (party_get_template_id,"$g_encountered_party_2_template","$g_encountered_party_2"),
			#       (else_try),
			#         (assign, "$g_encountered_party_2_faction",-1),
			#         (assign, "$g_encountered_party_2_relation", 0),
			#         (assign,"$g_encountered_party_2_template", -1),
			#       (try_end),
			
			#NPC companion changes begin
			(call_script, "script_party_count_fit_regulars", "p_main_party"),
			(assign, "$playerparty_prebattle_regulars", reg0),
			
			#        (try_begin),
			#            (assign, "$player_party__regulars", 0),
			#            (call_script, "script_party_count_fit_regulars", "p_main_party"),
			#            (gt, reg0, 0),
			#            (assign, "$player_party_contains_regulars", 1),
			#        (try_end),
			#NPC companion changes end
		##tom rebalance
			(try_begin), 
			(eq, "$culture_pool_initialized", 1),
		(eq, "$culture_pool", 1),
		(call_script, "script_rebalance_troops_by_culture"),
		(try_end),
		##tom rebalance
			
			(assign, "$g_last_rest_center", -1),
			(assign, "$talk_context", 0),
			(assign,"$g_player_surrenders",0),
			(assign,"$g_enemy_surrenders",0),
			(assign, "$g_leave_encounter",0),
			(assign, "$g_engaged_enemy", 0),
			#       (assign,"$waiting_for_arena_fight_result", 0),
			#       (assign,"$arena_bet_amount",0),
			#       (assign,"$g_player_raiding_village",0),
			(try_begin),
				(neg|is_between, "$g_encountered_party", centers_begin, centers_end),
				(rest_for_hours, 0), #stop waiting
				(assign, "$g_infinite_camping", 0),
			(try_end),
			#       (assign, "$g_permitted_to_center",0),
			(assign, "$new_encounter", 1), #check this in the menu.
			(try_begin),
				(lt, "$g_encountered_party_2",0), #Normal encounter. Not battle or siege.
				(try_begin),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(jump_to_menu, "mnu_castle_outside"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					(jump_to_menu, "mnu_castle_outside"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship),
					(jump_to_menu, "mnu_ship_reembark"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
					(jump_to_menu, "mnu_village"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
					(jump_to_menu, "mnu_cattle_herd"),
				(else_try),
					(is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
					(jump_to_menu, "mnu_training_ground"),
				(else_try),
					(party_get_template_id, ":template", "$g_encountered_party"),
					(ge, ":template", "pt_steppe_bandit_lair"),
					(lt, ":template", "pt_bandit_lair_templates_end"),
					(assign, "$loot_screen_shown", 0),
					#		   (call_script, "script_encounter_init_variables"),
					(jump_to_menu, "mnu_bandit_lair"),
				(else_try),
					(eq, "$g_encountered_party", "p_zendar"),
					(jump_to_menu, "mnu_zendar"),
				(else_try),
					(eq, "$g_encountered_party", "p_salt_mine"),
					(jump_to_menu, "mnu_salt_mine"),
				(else_try),
					(eq, "$g_encountered_party", "p_four_ways_inn"),
					(jump_to_menu, "mnu_four_ways_inn"),
				(else_try),
					(eq, "$g_encountered_party", "p_test_scene"),
					(jump_to_menu, "mnu_test_scene"),
				(else_try),
					(eq, "$g_encountered_party", "p_battlefields"),
					(jump_to_menu, "mnu_battlefields"),
				(else_try),
					(eq, "$g_encountered_party", "p_training_ground"),
					(jump_to_menu, "mnu_tutorial"),
				(else_try),
					(eq, "$g_encountered_party", "p_camp_bandits"),
					(jump_to_menu, "mnu_camp"),
		(else_try), #tom - manor
					(eq, "$g_encountered_party_template", "pt_manor"),
			(jump_to_menu, "mnu_manor_center"),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_mongol_camp_status, status_stationed),
			(eq, "$g_encountered_party_template", "pt_mongolian_camp"),
			(jump_to_menu, "mnu_mongol_camp"),
			#tom end	
				(else_try),
					# (try_begin),
					# (lt, "$g_encountered_party_relation", 0),
					# (party_slot_eq, "$g_encountered_party", slot_party_type, spt_kingdom_hero_party),
					# (try_begin),
					# (eq, "$g_battle_preparation_phase", 0),
					# (assign, "$g_battle_preparation_phase", 1),
					# (try_end),
					# (try_end),
					(jump_to_menu, "mnu_simple_encounter"),
				(try_end),
			(else_try), #Battle or siege
				(try_begin),
					(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					(try_begin),
						(eq, "$auto_enter_town", "$g_encountered_party"),
						(jump_to_menu, "mnu_town"),
					(else_try),
						(eq, "$auto_besiege_town", "$g_encountered_party"),
						(jump_to_menu, "mnu_besiegers_camp_with_allies"),
					(else_try),
						(jump_to_menu, "mnu_join_siege_outside"),
					(try_end),
				(else_try),
					(jump_to_menu, "mnu_pre_join"),
				(try_end),
			(try_end),
			(assign,"$auto_enter_town",0),
			(assign,"$auto_besiege_town",0),
	])

		# script_process_village_raids
		# called from triggers every two hours
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		("process_village_raids",
			[
				(try_for_range, ":village_no", villages_begin, villages_end),
					(party_get_slot, ":village_raid_progress", ":village_no", slot_village_raid_progress),
					(try_begin),
						(party_slot_eq, ":village_no", slot_village_state, 0), #village is normal
						(val_sub, ":village_raid_progress", 5),
						(val_max, ":village_raid_progress", 0),
						(party_set_slot, ":village_no", slot_village_raid_progress, ":village_raid_progress"),
						(try_begin),
							(lt, ":village_raid_progress", 50),
							
							# (try_begin),
								# (party_get_icon, ":village_icon", ":village_no"),
								# (neq, ":village_icon", "icon_village_a"),
								# (party_set_icon, ":village_no", "icon_village_a"),
							# (try_end),
							
							(party_slot_ge, ":village_no", slot_village_smoke_added, 1),
							(party_set_slot, ":village_no", slot_village_smoke_added, 0),
							(party_clear_particle_systems, ":village_no"),
						(try_end),
					(else_try),
						(party_slot_eq, ":village_no", slot_village_state, svs_being_raided), #village is being raided
						#End raid unless there is an enemy party nearby
						(assign, ":raid_ended", 1),
						(party_get_slot, ":raider_party", ":village_no", slot_village_raided_by),
						
						(try_begin),
							(ge, ":raider_party", 0),
							(party_is_active, ":raider_party"),
							(this_or_next|neq, ":raider_party", "p_main_party"),
							(eq, "$g_player_is_captive", 0),
							(store_distance_to_party_from_party, ":distance", ":village_no", ":raider_party"),
							(lt, ":distance", raid_distance),
							(assign, ":raid_ended", 0),
						(try_end),
						
						(try_begin),
							(eq, ":raid_ended", 1),
							(call_script, "script_village_set_state", ":village_no", svs_normal), #clear raid flag
							(party_set_slot, ":village_no", slot_village_smoke_added, 0),
							(party_clear_particle_systems, ":village_no"),
						(else_try),
							(assign, ":raid_progress_increase", 11),
							(party_get_slot, ":looter_party", ":village_no", slot_village_raided_by),
							(try_begin),
								(party_get_skill_level, ":looting_skill", ":looter_party", "skl_looting"),
								(val_add, ":raid_progress_increase", ":looting_skill"),
							(try_end),
							(try_begin),
								(party_slot_eq, ":village_no", slot_center_has_watch_tower, 1),
								(val_mul, ":raid_progress_increase", 2),
								(val_div, ":raid_progress_increase", 3),
							(try_end),
							(val_add, ":village_raid_progress", ":raid_progress_increase"),
							(party_set_slot, ":village_no", slot_village_raid_progress, ":village_raid_progress"),
							(try_begin),
								(ge, ":village_raid_progress", 50),
								(party_slot_eq, ":village_no", slot_village_smoke_added, 0),
								(party_add_particle_system, ":village_no", "psys_map_village_fire"),
								(party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
								#(party_set_icon, ":village_no", "icon_village_burnt_a"), #tom
								(party_set_slot, ":village_no", slot_village_smoke_added, 1),
							(try_end),
							(try_begin),
								(gt, ":village_raid_progress", 100),
								(str_store_party_name_link, s1, ":village_no"),
								(party_stack_get_troop_id, ":raid_leader", ":looter_party", 0),
								(ge, ":raid_leader", 0),
								(str_store_party_name, s2, ":looter_party"),
								# rafi
								(store_troop_faction, ":troop_faction", ":raid_leader"),
								(store_relation, ":rel", ":troop_faction", "$players_kingdom"),
								(try_begin),
									(this_or_next | lt, ":rel", 0),
									(eq, ":troop_faction", "$players_kingdom"),
									(display_log_message, "@The village of {s1} has been looted by {s2}."),
								(try_end),
								# end rafi
								
								(try_begin),
									(party_get_slot, ":village_lord", ":village_no", slot_town_lord),
									(is_between, ":village_lord", active_npcs_begin, active_npcs_end),
									(call_script, "script_troop_change_relation_with_troop", ":raid_leader", ":village_lord", -1),
									(val_add, "$total_battle_enemy_changes", -1),
								(try_end),
								
								#give loot gold to raid leader
								(troop_get_slot, ":raid_leader_gold", ":raid_leader", slot_troop_wealth),
								(party_get_slot, ":village_prosperity", ":village_no"),
								(store_mul, ":value_of_loot", ":village_prosperity", 60), #average is 3000
								(val_add, ":raid_leader_gold", ":value_of_loot"),
								(troop_set_slot, ":raid_leader", slot_troop_wealth, ":raid_leader_gold"),
								
								#take loot gold from village lord #new 1.126
								(try_begin),
									(is_between, ":village_lord", active_npcs_begin, active_npcs_end),
									(troop_get_slot, ":village_lord_gold", ":village_lord", slot_troop_wealth),
									(val_sub, ":village_lord_gold", ":value_of_loot"),
									(val_max, ":village_lord_gold", 0),
									(troop_set_slot, ":village_lord", slot_troop_wealth, ":village_lord_gold"),
								(try_end),
								
								(call_script, "script_village_set_state",  ":village_no", svs_looted),
								(party_set_slot, ":village_no", slot_center_accumulated_rents, 0), #new 1.126
								(party_set_slot, ":village_no", slot_center_accumulated_tariffs, 0), #new 1.126
								
								(party_set_slot, ":village_no", slot_village_raid_progress, 0),
								(party_set_slot, ":village_no", slot_village_recover_progress, 0),
								(try_begin),
									(store_faction_of_party, ":village_faction", ":village_no"),
									(this_or_next|party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
									(eq, ":village_faction", "fac_player_supporters_faction"),
									(call_script, "script_add_notification_menu", "mnu_notification_village_raided", ":village_no", ":raid_leader"),
								(try_end),
								(call_script, "script_add_log_entry", logent_village_raided, ":raid_leader",  ":village_no", -1, -1),
								(store_faction_of_party, ":looter_faction", ":looter_party"),
								#(call_script, "script_faction_inflict_war_damage_on_faction", ":looter_faction", ":village_faction", 5),
								(call_script, "script_faction_inflict_war_damage_on_faction", ":looter_faction", ":village_faction", 15), # rafi
							(try_end),
						(try_end),
					(else_try),
						(party_slot_eq, ":village_no", slot_village_state, svs_looted), #village is looted
						(party_get_slot, ":recover_progress", ":village_no", slot_village_recover_progress),
						(val_add, ":recover_progress", 1),
						(party_set_slot, ":village_no", slot_village_recover_progress, ":recover_progress"), #village looted
						(try_begin),
							(ge, ":recover_progress", 10),
							(party_slot_eq, ":village_no", slot_village_smoke_added, 1),
							(party_clear_particle_systems, ":village_no"),
							(party_add_particle_system, ":village_no", "psys_map_village_looted_smoke"),
							(party_set_slot, ":village_no", slot_village_smoke_added, 2),
						(try_end),
						(try_begin),
							(gt, ":recover_progress", 50),
							(party_slot_eq, ":village_no", slot_village_smoke_added, 2),
							(party_clear_particle_systems, ":village_no"),
							(party_set_slot, ":village_no", slot_village_smoke_added, 3),
							#(party_set_icon, ":village_no", "icon_village_deserted_a"),
						(try_end),
						(try_begin),
							(gt, ":recover_progress", 100),
							(call_script, "script_village_set_state",  ":village_no", 0),#village back to normal
							(party_set_slot, ":village_no", slot_village_recover_progress, 0),
							(party_clear_particle_systems, ":village_no"),
							(party_set_slot, ":village_no", slot_village_smoke_added, 0),
							#(party_set_icon, ":village_no", "icon_village_a"),
						(try_end),
					(try_end),
				(try_end),
		]),
		
		## campaign
		# script_process_sieges
		# called from triggers
		# WARNING: heavily modified by 1257AD devs
		# Input: none
		# Output: none
		("process_sieges",
			[
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					#Reducing siege hardness every day by 20
					(party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
					(val_sub, ":siege_hardness", 20),
					(val_max, ":siege_hardness", 0),
					(party_set_slot, ":center_no", slot_center_siege_hardness, ":siege_hardness"),
					
					(party_get_slot, ":town_food_store", ":center_no", slot_party_food_store),
					(call_script, "script_center_get_food_store_limit", ":center_no"),
					(assign, ":food_store_limit", reg0),
					(try_begin),
						(party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
						(ge, ":besieger_party", 0), #town is under siege
						
					#Reduce prosperity of besieged castle/town by -0.33/-4 every day.
					 (try_begin),
						 (try_begin),
							 (is_between, ":center_no", castles_begin, castles_end),
							 (store_random_in_range, ":random_value", 0, 3),
							 (try_begin),
								 (eq, ":random_value", 0),
								 (assign, ":daily_siege_effect_on_prosperity", -1),
							 (else_try),
								 (assign, ":daily_siege_effect_on_prosperity", 0),
							 (try_end),
						 (else_try),
							 (assign, ":daily_siege_effect_on_prosperity", -4),
						 (try_end),
			 
						 (call_script, "script_change_center_prosperity", ":center_no", ":daily_siege_effect_on_prosperity"),
						 (val_add, "$newglob_total_prosperity_from_townloot", ":daily_siege_effect_on_prosperity"),
					 (try_end),
						
						(store_faction_of_party, ":center_faction", ":center_no"),
						# Lift siege unless there is an enemy party nearby
						(assign, ":siege_lifted", 0),
						(try_begin),
							(try_begin),
								(neg|party_is_active, ":besieger_party"),
								(assign, ":siege_lifted", 1),
							(else_try),
								(store_distance_to_party_from_party, ":besieger_distance", ":center_no", ":besieger_party"),
								(gt, ":besieger_distance", 5),
								(assign, ":siege_lifted", 1),
							(else_try),
								##diplomacy begin
								(neg|party_slot_eq, ":center_no", slot_village_infested_by_bandits, "trp_peasant_woman"),
								##diplomacy end
								(store_faction_of_party, ":besieger_faction", ":besieger_party"),
								(store_relation, ":reln", ":besieger_faction", ":center_faction"),
								(ge, ":reln", 0),
								(assign, ":siege_lifted", 1),
							(try_end),
							
							
							(eq, ":siege_lifted", 1),
							#If another lord can take over the siege, it isn't lifted
							(try_for_range, ":enemy_hero", active_npcs_begin, active_npcs_end),
								(troop_slot_eq, ":enemy_hero", slot_troop_occupation, slto_kingdom_hero),
								(troop_get_slot, ":enemy_party", ":enemy_hero", slot_troop_leaded_party),
								(ge, ":enemy_party", 0),
								(party_is_active, ":enemy_party"),
								(store_faction_of_party, ":party_faction", ":enemy_party"),
								(store_relation, ":reln", ":party_faction", ":center_faction"),
								(lt, ":reln", 0),
								(store_distance_to_party_from_party, ":distance", ":center_no", ":enemy_party"),
								(lt, ":distance", 4),
								(assign, ":besieger_party", ":enemy_party"),
								(party_set_slot, ":center_no", slot_center_is_besieged_by, ":enemy_party"),
								(assign, ":siege_lifted", 0),
							(try_end),
						(try_end),
						(try_begin),
							(eq, ":siege_lifted", 1),
							(call_script, "script_lift_siege", ":center_no", 1),
						(else_try),
							(call_script, "script_center_get_food_consumption", ":center_no"),
							(assign, ":food_consumption", reg0),
							(val_sub, ":town_food_store", ":food_consumption"), # reduce food only under siege???
							(try_begin),
								(le, ":town_food_store", 0), #town is starving
								
								# rafi - cause casualties if no food
								# (party_get_num_companion_stacks, ":num_stacks", ":center_no"),
								# (try_for_range, ":stack_no", 0, ":num_stacks"),
									# (party_stack_get_troop_id, ":stack_troop", ":center_no", ":stack_no"),
									# (try_begin),
										# (party_stack_get_size, ":stack_size", ":center_no", ":stack_no"),
										# (gt, ":stack_size", 0),
										# (store_div, ":to_remove", ":stack_size", 10),
										# (party_remove_members, ":center_no", ":stack_troop", ":to_remove"),
										
										# (party_stack_get_size, ":stack_size", ":center_no", ":stack_no"),
										# (gt, ":stack_size", 0),
										# (store_random_in_range, ":random", 1, ":stack_size"),
										# (party_wound_members, ":center_no", ":stack_troop", ":random"),
									# (try_end),
								# (try_end),
								# end rafi
								(store_random_in_range, ":r", 0, 10),
								(gt, ":r", 0),
								(call_script, "script_party_inflict_attrition", ":center_no", ":r"), #tom
								
								# (store_random_in_range, ":r", 0, 100),
								# (lt, ":r", 10),
								# (call_script, "script_party_wound_all_members", ":center_no"), # town falls with 10% chance if starving
							(try_end),
						(try_end),
					(else_try),
						#town is not under siege...
						(val_add, ":town_food_store", 30), #add 30 food (significant for castles only.
					(try_end),
					
					(val_min, ":town_food_store", ":food_store_limit"),
					(val_max, ":town_food_store", 0),
					(party_set_slot, ":center_no", slot_party_food_store, ":town_food_store"),
				(try_end),
		]),

# script_allow_vassals_to_join_indoor_battle
		# Input: none
		# Output: none
		("allow_vassals_to_join_indoor_battle",
			[
				#if our commander attacks an enemy army
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
					(gt, ":party_no", 0),
					(party_is_active, ":party_no"),
					
					(party_get_attached_to, ":party_is_attached_to", ":party_no"),
					(lt, ":party_is_attached_to", 0),
					
					(store_troop_faction, ":faction_no", ":troop_no"),
					
					(try_begin),
						#(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
						(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
						(party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
						(gt, ":commander_party", 0),
						(party_is_active, ":commander_party"),
						
						(assign, ":besieged_center", -1),
						(try_begin),
							(party_slot_eq, ":commander_party", slot_party_ai_state, spai_holding_center), #if commander is holding a center
							(party_get_slot, ":commander_object", ":commander_party", slot_party_ai_object), #get commander's ai object (center they are holding)
							(party_get_battle_opponent, ":besieger_enemy", ":commander_object"), #get this object's battle opponent
							(party_is_active, ":besieger_enemy"),
							(assign, ":besieged_center", ":commander_object"),
							(assign, ":commander_object", ":besieger_enemy"),
						(else_try),
							(party_slot_eq, ":commander_party", slot_party_ai_state, spai_engaging_army), #if commander is engaging an army
							(party_get_slot, ":commander_object", ":commander_party", slot_party_ai_object), #get commander's ai object (army which they engaded)
							(ge, ":commander_object", 0), #if commander has an object
							(neg|is_between, ":commander_object", centers_begin, centers_end), #if this object is not a center, so it is a party
							(party_is_active, ":commander_object"),
							(party_get_battle_opponent, ":besieged_center", ":commander_object"), #get this object's battle opponent
						(else_try),
							(assign, ":besieged_center", -1),
						(try_end),
						
						(is_between, ":besieged_center", walled_centers_begin, walled_centers_end), #if battle opponent of our commander's ai object is a walled center
						
						(party_get_attached_to, ":attached_to_party", ":commander_party"), #if commander is attached to besieged center already.
						(eq, ":attached_to_party", ":besieged_center"),
						
						(store_faction_of_party, ":besieged_center_faction", ":besieged_center"),#get (battle opponent of our commander's ai object)'s faction
						(eq, ":besieged_center_faction", ":faction_no"), #if battle opponent of our commander's ai object is from same faction with current party
						(party_is_active, ":commander_object"),
						#make also follow_or_not check if needed
						
						(call_script, "script_party_set_ai_state", ":party_no", spai_engaging_army, ":commander_object"), #go and help commander
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_party_name, s7, ":party_no"),
							(str_store_party_name, s6, ":commander_object"),
							(display_message, "@{!}DEBUG : {s7} is helping his commander by fighting with {s6}."),
						(try_end),
					(else_try),
						#(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
						
						(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
						(party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
						(gt, ":commander_party", 0),
						(party_is_active, ":commander_party"),
						
						(party_get_battle_opponent, ":besieged_center", ":commander_party"), #get this object's battle opponent
						
						#make also follow_or_not check if needed
						
						(is_between, ":besieged_center", walled_centers_begin, walled_centers_end), #if this object is a center
						(party_get_attached_to, ":attached_to_party", ":party_no"),
						(neq, ":attached_to_party", ":besieged_center"),
						(party_is_active, ":besieged_center"),
						
						(call_script, "script_party_set_ai_state", ":party_no", spai_engaging_army, ":besieged_center"), #go and help commander
						
						#(try_begin),
						#  (eq, "$cheat_mode", 1),
						#  (str_store_party_name, s7, ":party_no"),
						#  (str_store_party_name, s6, ":besieged_center"),
						#  (display_message, "@{!}DEBUG : {s7} is helping his commander by attacking {s6}."),
						#(try_end),
						
						#(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
						#(party_set_ai_object, ":party_no", ":besieged_center"),
						#(party_set_flags, ":party_no", pf_default_behavior, 1), #is these needed?
						#(party_set_slot, ":party_no", slot_party_ai_substate, 1), #is these needed?
					(try_end),
				(try_end),
		]),

# script_process_kingdom_parties_ai
		# This is called more frequently than decide_kingdom_parties_ai
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		#called from triggers
		("process_kingdom_parties_ai",
			[
			#tom
		# (assign, ":max_mod", 2), #tom was 3
		 
		# (assign, ":current_modula", "$g_alarm_modula"),
				# (val_add, "$g_hero_modula", 1),
				# (try_begin),
					# (eq, "$g_alarm_modula", ":max_mod"),
					# (assign, "$g_hero_modula", 0),
				# (try_end),
		#tom
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
			# (store_mod, ":hero_modula", ":troop_no", ":max_mod"), #tom
					# (eq, ":hero_modula", ":current_modula"),				#tom
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
					(gt, ":party_no", 0),
					(call_script, "script_process_hero_ai", ":troop_no"),
				(try_end),
		]),

		# script_process_hero_ai
		# This is called more frequently than script_decide_kingdom_party_ais
		# Handles sieges, raids, etc -- does not change the party's basic mission.
		# WARNING: modified by 1257AD devs
		# called from triggers
		# Input: none
		# Output: none
		
		("process_hero_ai",
			[
				(store_script_param_1, ":troop_no"),
				(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
				(try_begin),
					(party_is_active, ":party_no"),
					(store_faction_of_party, ":faction_no", ":party_no"),
					(party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
					(party_get_slot, ":ai_object", ":party_no", slot_party_ai_object),
					(try_begin),
						(eq, ":ai_state", spai_besieging_center),
						(try_begin),
							(party_slot_eq, ":ai_object", slot_center_is_besieged_by, -1),
							(store_distance_to_party_from_party, ":distance", ":party_no", ":ai_object"),
							(lt, ":distance", 3),
							(try_begin),
								(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
								(party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
								(party_set_slot, ":ai_object", slot_center_is_besieged_by, ":commander_party"),
							(else_try),
								(party_set_slot, ":ai_object", slot_center_is_besieged_by, ":party_no"),
							(try_end),
							(store_current_hours, ":cur_hours"),
							(party_set_slot, ":ai_object", slot_center_siege_begin_hours, ":cur_hours"),
							
							(str_store_party_name_link, s1, ":ai_object"),
							(str_store_troop_name_link, s2, ":troop_no"),
							(str_store_faction_name_link, s3, ":faction_no"),
							# rafi
							(store_faction_of_party, ":ai_object_faction", ":ai_object"),
							#(store_troop_faction, ":troop_faction", ":troop_no"),
							# update AI for target
							(assign, ":saved_glob", "$g_ai_kingdom"),
							(assign, "$g_ai_kingdom", ":ai_object_faction"),
							(call_script, "script_recalculate_ais"),
							(assign, "$g_ai_kingdom", ":saved_glob"),
							# end AI update
							# (store_relation, ":rel", ":troop_faction", "$players_kingdom"),
							# (try_begin),
								# (this_or_next | lt, ":rel", 0),
								# (this_or_next | eq, ":ai_object_faction", "$players_kingdom"),
								# (eq, ":troop_faction", "$players_kingdom"),
								# (str_store_faction_name_link, s3, ":troop_faction"),
								# (display_log_message, "@{s1} has been besieged by {s2} of {s3}."),
							# (try_end),
							# end rafi
							
							(try_begin),
								(store_faction_of_party, ":ai_object_faction", ":ai_object"),
								(this_or_next|party_slot_eq, ":ai_object", slot_town_lord, "trp_player"),
								(eq, ":ai_object_faction", "fac_player_supporters_faction"),
								(call_script, "script_add_notification_menu", "mnu_notification_center_under_siege", ":ai_object", ":troop_no"),
							(try_end),
							(call_script, "script_village_set_state", ":ai_object", svs_under_siege),
							
							(store_faction_of_party, ":ai_object_faction", ":ai_object"),
							# (call_script, "script_raf_set_ai_recalculation_flags", ":faction_no"),
							# (call_script, "script_raf_set_ai_recalculation_flags", ":ai_object_faction"),
							(assign, "$g_recalculate_ais", 1),
						(try_end),
					(else_try),
						(eq, ":ai_state", spai_raiding_around_center),
						(party_slot_eq, ":party_no", slot_party_ai_substate, 0),
						(assign, ":selected_village", 0),
						(try_for_range, ":enemy_village_no", villages_begin, villages_end),
							(eq, ":selected_village", 0),
							(store_faction_of_party, ":enemy_village_faction", ":enemy_village_no"),
							(try_begin),
								(party_slot_eq, ":enemy_village_no", slot_town_lord, "trp_player"),
								(store_relation, ":reln", "fac_player_supporters_faction", ":faction_no"),
							(else_try),
								(store_relation, ":reln", ":enemy_village_faction", ":faction_no"),
							(try_end),
							(lt, ":reln", 0),
							(store_distance_to_party_from_party, ":dist", ":enemy_village_no", ":party_no"),
							(lt, ":dist", 15),
							(party_slot_eq, ":enemy_village_no", slot_village_state, 0), #village is not already raided
							#CHANGE STATE TO RAID THIS VILLAGE
							(assign, ":selected_village", ":enemy_village_no"),
						(try_end),
						(try_begin),
							(eq, ":selected_village", 0),
							(is_between, ":ai_object", villages_begin, villages_end),
							(assign, ":selected_village", ":ai_object"),
						(try_end),
						(try_begin),
							(gt, ":selected_village", 0),
							(call_script, "script_party_set_ai_state", ":party_no", spai_raiding_around_center, ":selected_village"),
							(try_begin),
								(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
								(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
								(faction_set_slot, ":faction_no", slot_faction_ai_object, ":selected_village"),
							(try_end),
							(party_get_position, pos1, ":selected_village"),
							(map_get_random_position_around_position, pos2, pos1, 1),
							(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
							(party_set_ai_target_position, ":party_no", pos2),
							(party_set_ai_object, ":party_no", ":selected_village"),
							(party_set_slot, ":party_no", slot_party_ai_substate, 1),
						(try_end),
					(else_try),
						(eq, ":ai_state", spai_raiding_around_center),#substate is 1
						(try_begin),
							(store_distance_to_party_from_party, ":distance", ":party_no", ":ai_object"),
							(lt, ":distance", 2),
							(try_begin),
								(party_slot_eq, ":ai_object", slot_village_state, 0),
								(call_script, "script_village_set_state", ":ai_object", svs_being_raided),
								(party_set_slot, ":ai_object", slot_village_raided_by, ":party_no"),
								(try_begin),
									(store_faction_of_party, ":village_faction", ":ai_object"),
									(this_or_next|party_slot_eq, ":ai_object", slot_town_lord, "trp_player"),
									(eq, ":village_faction", "fac_player_supporters_faction"),
									(store_distance_to_party_from_party, ":dist", "p_main_party", ":ai_object"),
									(this_or_next|lt, ":dist", 30),
									(party_slot_eq, ":ai_object", slot_center_has_messenger_post, 1),
									(call_script, "script_add_notification_menu", "mnu_notification_village_raid_started", ":ai_object", ":troop_no"),
								(try_end),
							(else_try),
								(party_slot_eq, ":ai_object", slot_village_state, svs_being_raided),
							(else_try),
								#if anything other than being_raided leave
								(party_set_slot, ":party_no", slot_party_ai_substate, 0),
							(try_end),
						(try_end),
					(else_try),
						(eq, ":ai_state", spai_retreating_to_center),
						(try_begin),
							(party_get_battle_opponent, ":enemy_party", ":party_no"),
							(ge, ":enemy_party", 0), #we are in a battle! we may be caught in a loop!
							(call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
							(party_set_flags, ":party_no", pf_default_behavior, 0),
							(party_set_slot, ":party_no", slot_party_commander_party, -1),
						(try_end),
					(else_try),
						(eq, ":ai_state", spai_patrolling_around_center),
						
						(try_begin),
							(party_slot_eq, ":party_no", slot_party_ai_substate, 0),
							(store_distance_to_party_from_party, ":distance", ":party_no", ":ai_object"),
							(lt, ":distance", 6),
							(party_set_slot, ":party_no", slot_party_ai_substate, 1),
							
							(party_set_aggressiveness, ":party_no", 8),
							(party_set_courage, ":party_no", 8),
							(party_set_ai_initiative, ":party_no", 100),
							
							(party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
							(party_set_ai_object, ":party_no", ":ai_object"),
						(try_end),
					(else_try),
						(eq, ":ai_state", spai_holding_center),
					(try_end),
				(try_end),
		]),


		# script_begin_assault_on_center
		# called from triggers
		# Input: arg1: faction_no
		# Output: none
		("begin_assault_on_center",
			[
				(store_script_param, ":center_no", 1),
				
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
					(gt, ":party_no", 0),
					(party_is_active, ":party_no"),
					
					(assign, ":continue", 0),
					(try_begin),
						(party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
						(party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
						(party_slot_eq, ":party_no", slot_party_ai_substate, 0),
						(assign, ":continue", 1),
					(else_try),
						(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
						(party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
						(gt, ":commander_party", 0),
						(party_is_active, ":commander_party"),
						(party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
						(party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
						(call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
						(assign, ":continue", 1),
					(try_end),
					
					(eq, ":continue", 1),
					
					(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
					(party_set_ai_object, ":party_no", ":center_no"),
					(party_set_flags, ":party_no", pf_default_behavior, 1),
					(party_set_slot, ":party_no", slot_party_ai_substate, 1),
				(try_end),
		]),