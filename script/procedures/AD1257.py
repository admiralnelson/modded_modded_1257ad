from header import *
	# script_process_alarms_new
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# this script is called in from a simple triger
	# description: same as an old, but single center thingy, called for a specific thing
	# todo "#maybe do audio sound?"
	# INPUT: center
	# OUTPUT: none
process_alarms_new = (
	"process_alarms_new",
			[
			(store_script_param, ":center_no", 1),
			(try_begin),
		#(try_for_range, ":center_no", centers_begin, centers_end),
				#(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					#(store_mod, ":center_modula", ":center_no", ":max_mod"),
					#(eq, ":center_modula", ":current_modula"),
					
					(party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
					(party_set_slot, ":center_no", slot_center_sortie_strength, 0),
					(party_set_slot, ":center_no", slot_center_sortie_enemy_strength, 0),
					
					(assign, ":spotting_range", 3),
					(try_begin),
						(is_currently_night),
						(assign, ":spotting_range", 2),
					(try_end),
					
					(try_begin),
						(party_slot_eq, ":center_no", slot_center_has_watch_tower, 1),
						(val_mul, ":spotting_range", 2),
					(else_try),
						(neg|is_between, ":center_no", villages_begin, villages_end),
						(val_add, ":spotting_range", 1),
						(val_mul, ":spotting_range", 2),
					(try_end),
					
					(store_faction_of_party, ":center_faction", ":center_no"),
					
					(try_for_parties, ":party_no"),
						(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
						(eq, ":party_no", "p_main_party"),
						
						(store_faction_of_party, ":party_faction", ":party_no"),
						
						(try_begin),
							(eq, ":party_no", "p_main_party"),
							(assign, ":party_faction", "$players_kingdom"),
						(try_end),
						
						(try_begin),
							(eq, ":party_faction", ":center_faction"),
							
							(store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
							(le, ":distance", ":spotting_range"),
							
							(party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
							(party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
							(val_add, ":sortie_strength", ":cached_strength"),
							(party_set_slot, ":center_no", slot_center_sortie_strength, ":sortie_strength"),
						(else_try),
							(neq, ":party_faction", ":center_faction"),
							
							(store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
							
							(try_begin),
								(lt, ":distance", 10),
								(store_current_hours, ":hours"),
								(store_sub, ":faction_recce_slot", ":party_faction", kingdoms_begin),
								(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
								(party_set_slot, ":center_no", ":faction_recce_slot", ":hours"),
								
								#(eq, "$cheat_mode", 1),
								#(str_store_faction_name, s4, ":party_faction"),
								#(str_store_party_name, s5, ":center_no"),
								#(display_message, "@{!}DEBUG -- {s4} reconnoiters {s5}"),
							(try_end),
							
							(store_relation, ":reln", ":center_faction", ":party_faction"),
							(lt, ":reln", 0),
							
							(try_begin),
								(le, ":distance", ":spotting_range"),
								
								(party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
								(party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
								(val_add, ":enemy_strength", ":cached_strength"),
								(party_set_slot, ":center_no", slot_center_sortie_enemy_strength, ":enemy_strength"),
								(party_set_slot, ":center_no", slot_center_last_spotted_enemy, ":party_no"),
							(try_end),
							
						(try_end),
					(try_end),
				(try_end),
				
		(try_begin),
			#(eq, 0, 1), #this never happened in game, waste of space. Perhaps remove it?
				#(try_for_range, ":center_no", centers_begin, centers_end),
				#(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					#(store_mod, ":center_modula", ":center_no", ":max_mod"),
					#(eq, ":center_modula", ":current_modula"),
					
					(try_begin), #eligible units sortie out of castle
						(is_between, ":center_no", walled_centers_begin, walled_centers_end),
						(party_slot_ge, ":center_no", slot_center_last_spotted_enemy, 0),
						
						(party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
						(party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
						
						#Below two lines are new added by ozan. While AI want to drive nearby besieging enemy parties by making sortie them, they give up current battle if they are already joining one.
						#Lets assume there is a battle inside the castle, because enemies are inside castle and they are so close to castle they will be also added to slot_center_sortie_enemy_strength
						#But in this scenario, they are not outside the castle, so searching/patrolling enemy outside the castle is useless at this point.
						#So if there is already a battle inside the center, do not sortie and search enemy outside.
						(party_get_battle_opponent, ":center_battle_opponent", ":center_no"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(ge, ":center_battle_opponent", 0),
							(str_store_party_name, s7, ":center_no"),
							(str_store_party_name, s6, ":center_battle_opponent"),
							(display_message, "@{!}DEBUG : There are already enemies ({s6}) inside {s7}."),
						(try_end),
						(lt, ":center_battle_opponent", 0),
						#New added by ozan ended.
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_party_name, s4, ":center_no"),
							(assign, reg3, ":sortie_strength"),
							(assign, reg4, ":enemy_strength"),
							(display_message, "@{!}DEBUG -- Calculating_sortie for {s4} strength of {reg3} vs {reg4} enemies"),
						(try_end),
						
						(store_mul, ":enemy_strength_mul_14_div_10", ":enemy_strength", 14),
						(val_div, ":enemy_strength_mul_14_div_10", 10),
						(gt, ":sortie_strength", ":enemy_strength_mul_14_div_10"),
						
						(assign, ":at_least_one_party_sorties", 0),
						(try_for_parties, ":sortie_party"),
							(party_get_attached_to, ":town", ":sortie_party"),
							(eq, ":town", ":center_no"),
							
							(party_slot_eq, ":sortie_party", slot_party_type, spt_kingdom_hero_party),
							
							(party_get_slot, ":cached_strength", ":sortie_party", slot_party_cached_strength),
							(ge, ":cached_strength", 100),
							
							(party_detach, ":sortie_party"),
							(call_script, "script_party_set_ai_state", ":sortie_party",  spai_patrolling_around_center, ":center_no"),
							
							(try_begin),
								(eq, "$cheat_mode", 1),
								(str_store_party_name, s4, ":sortie_party"),
								(display_message, "str_s4_sorties"),
							(try_end),
							
							(eq, ":at_least_one_party_sorties", 0),
							(assign, ":at_least_one_party_sorties", ":sortie_party"),
						(try_end),
						
						(try_begin),
							(party_is_in_town, "p_main_party", ":center_no"),
							(eq, "$g_player_is_captive", 0),
							(gt, ":at_least_one_party_sorties", 0),
							(call_script, "script_add_notification_menu", "mnu_notification_sortie_possible", ":center_no", ":sortie_party"),
						(try_end),
					(try_end),
					
					(store_faction_of_party, ":center_faction", ":center_no"),
					
					#Send message
					(this_or_next|eq, "$cheat_mode", 1), #this is message
					(this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(eq, ":center_faction", "$players_kingdom"),
					
					(party_get_slot, ":enemy_party", ":center_no", slot_center_last_spotted_enemy),
					(ge, ":enemy_party", 0),
					(store_distance_to_party_from_party, ":dist", "p_main_party", ":center_no"),
					(assign, ":has_messenger", 0),
					(try_begin),
						(this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
						(eq, ":center_faction", "fac_player_supporters_faction"),
						(party_slot_eq, ":center_no", slot_center_has_messenger_post, 1),
						(assign, ":has_messenger", 1),
					(try_end),
					
					(this_or_next|eq, "$cheat_mode", 1),
					(this_or_next|lt, ":dist", 30),
					(eq, ":has_messenger", 1),
					
					(str_store_party_name_link, s1, ":center_no"),
					(party_get_slot, ":exact_enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
					(val_div, ":exact_enemy_strength", 25),
					
					(try_begin),
						(lt, ":exact_enemy_strength", 500),
						(display_message, "@Small bands of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 1000),
						(display_message, "@Enemy patrols spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 2000),
						(display_message, "@Medium-sized group of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 4000),
						(display_message, "@Significant group of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 8000),
						(display_message, "@Army of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 16000),
						(display_message, "@Large army of enemies spotted near {s1}."),
					(else_try),
						(display_message, "@Great host of enemies spotted near {s1}."),
					(try_end),
					#maybe do audio sound?
					
				(try_end),
		])
	
	# script_process_alarms
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# probably this one is deprecated(?)
		# this script is called in from a simple triger
		# Input: none
		# Output: none
process_alarms = (
	"process_alarms",
			[
				# rafi
				(assign, ":max_mod", 60), #tom was 3 
				# end rafi
				
				(assign, ":current_modula", "$g_alarm_modula"),
				(val_add, "$g_alarm_modula", 1),
				(try_begin),
					(ge, "$g_alarm_modula", ":max_mod"), #tom was eq
					(assign, "$g_alarm_modula", 0),
				(try_end),
				
				(try_for_range, ":center_no", centers_begin, centers_end),
				#(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_mod, ":center_modula", ":center_no", ":max_mod"),
					(eq, ":center_modula", ":current_modula"),
					
					(party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
					(party_set_slot, ":center_no", slot_center_sortie_strength, 0),
					(party_set_slot, ":center_no", slot_center_sortie_enemy_strength, 0),
					
					(assign, ":spotting_range", 3),
					(try_begin),
						(is_currently_night),
						(assign, ":spotting_range", 2),
					(try_end),
					
					(try_begin),
						(party_slot_eq, ":center_no", slot_center_has_watch_tower, 1),
						(val_mul, ":spotting_range", 2),
					(else_try),
						(neg|is_between, ":center_no", villages_begin, villages_end),
						(val_add, ":spotting_range", 1),
						(val_mul, ":spotting_range", 2),
					(try_end),
					
					(store_faction_of_party, ":center_faction", ":center_no"),
					
					(try_for_parties, ":party_no"),
						(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
						(eq, ":party_no", "p_main_party"),
						
						(store_faction_of_party, ":party_faction", ":party_no"),
						
						(try_begin),
							(eq, ":party_no", "p_main_party"),
							(assign, ":party_faction", "$players_kingdom"),
						(try_end),
						
						(try_begin),
							(eq, ":party_faction", ":center_faction"),
							
							(store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
							(le, ":distance", ":spotting_range"),
							
							(party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
							(party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
							(val_add, ":sortie_strength", ":cached_strength"),
							(party_set_slot, ":center_no", slot_center_sortie_strength, ":sortie_strength"),
						(else_try),
							(neq, ":party_faction", ":center_faction"),
							
							(store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
							
							(try_begin),
								(lt, ":distance", 10),
								(store_current_hours, ":hours"),
								(store_sub, ":faction_recce_slot", ":party_faction", kingdoms_begin),
								(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
								(party_set_slot, ":center_no", ":faction_recce_slot", ":hours"),
								
								#(eq, "$cheat_mode", 1),
								#(str_store_faction_name, s4, ":party_faction"),
								#(str_store_party_name, s5, ":center_no"),
								#(display_message, "@{!}DEBUG -- {s4} reconnoiters {s5}"),
							(try_end),
							
							(store_relation, ":reln", ":center_faction", ":party_faction"),
							(lt, ":reln", 0),
							
							(try_begin),
								(le, ":distance", ":spotting_range"),
								
								(party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
								(party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
								(val_add, ":enemy_strength", ":cached_strength"),
								(party_set_slot, ":center_no", slot_center_sortie_enemy_strength, ":enemy_strength"),
								(party_set_slot, ":center_no", slot_center_last_spotted_enemy, ":party_no"),
							(try_end),
							
						(try_end),
					(try_end),
				(try_end),
				
				(try_for_range, ":center_no", centers_begin, centers_end),
				#(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_mod, ":center_modula", ":center_no", ":max_mod"),
					(eq, ":center_modula", ":current_modula"),
					
					(try_begin), #eligible units sortie out of castle
						(is_between, ":center_no", walled_centers_begin, walled_centers_end),
						(party_slot_ge, ":center_no", slot_center_last_spotted_enemy, 0),
						
						(party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
						(party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
						
						#Below two lines are new added by ozan. While AI want to drive nearby besieging enemy parties by making sortie them, they give up current battle if they are already joining one.
						#Lets assume there is a battle inside the castle, because enemies are inside castle and they are so close to castle they will be also added to slot_center_sortie_enemy_strength
						#But in this scenario, they are not outside the castle, so searching/patrolling enemy outside the castle is useless at this point.
						#So if there is already a battle inside the center, do not sortie and search enemy outside.
						(party_get_battle_opponent, ":center_battle_opponent", ":center_no"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(ge, ":center_battle_opponent", 0),
							(str_store_party_name, s7, ":center_no"),
							(str_store_party_name, s6, ":center_battle_opponent"),
							(display_message, "@{!}DEBUG : There are already enemies ({s6}) inside {s7}."),
						(try_end),
						(lt, ":center_battle_opponent", 0),
						#New added by ozan ended.
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_party_name, s4, ":center_no"),
							(assign, reg3, ":sortie_strength"),
							(assign, reg4, ":enemy_strength"),
							(display_message, "@{!}DEBUG -- Calculating_sortie for {s4} strength of {reg3} vs {reg4} enemies"),
						(try_end),
						
						(store_mul, ":enemy_strength_mul_14_div_10", ":enemy_strength", 14),
						(val_div, ":enemy_strength_mul_14_div_10", 10),
						(gt, ":sortie_strength", ":enemy_strength_mul_14_div_10"),
						
						(assign, ":at_least_one_party_sorties", 0),
						(try_for_parties, ":sortie_party"),
							(party_get_attached_to, ":town", ":sortie_party"),
							(eq, ":town", ":center_no"),
							
							(party_slot_eq, ":sortie_party", slot_party_type, spt_kingdom_hero_party),
							
							(party_get_slot, ":cached_strength", ":sortie_party", slot_party_cached_strength),
							(ge, ":cached_strength", 100),
							
							(party_detach, ":sortie_party"),
							(call_script, "script_party_set_ai_state", ":sortie_party",  spai_patrolling_around_center, ":center_no"),
							
							(try_begin),
								(eq, "$cheat_mode", 1),
								(str_store_party_name, s4, ":sortie_party"),
								(display_message, "str_s4_sorties"),
							(try_end),
							
							(eq, ":at_least_one_party_sorties", 0),
							(assign, ":at_least_one_party_sorties", ":sortie_party"),
						(try_end),
						
						(try_begin),
							(party_is_in_town, "p_main_party", ":center_no"),
							(eq, "$g_player_is_captive", 0),
							(gt, ":at_least_one_party_sorties", 0),
							(call_script, "script_add_notification_menu", "mnu_notification_sortie_possible", ":center_no", ":sortie_party"),
						(try_end),
					(try_end),
					
					(store_faction_of_party, ":center_faction", ":center_no"),
					
					#Send message
					(this_or_next|eq, "$cheat_mode", 1), #this is message
					(this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(eq, ":center_faction", "$players_kingdom"),
					
					(party_get_slot, ":enemy_party", ":center_no", slot_center_last_spotted_enemy),
					(ge, ":enemy_party", 0),
					(store_distance_to_party_from_party, ":dist", "p_main_party", ":center_no"),
					(assign, ":has_messenger", 0),
					(try_begin),
						(this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
						(eq, ":center_faction", "fac_player_supporters_faction"),
						(party_slot_eq, ":center_no", slot_center_has_messenger_post, 1),
						(assign, ":has_messenger", 1),
					(try_end),
					
					(this_or_next|eq, "$cheat_mode", 1),
					(this_or_next|lt, ":dist", 30),
					(eq, ":has_messenger", 1),
					
					(str_store_party_name_link, s1, ":center_no"),
					(party_get_slot, ":exact_enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
					(val_div, ":exact_enemy_strength", 25),
					
					(try_begin),
						(lt, ":exact_enemy_strength", 500),
						(display_message, "@Small bands of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 1000),
						(display_message, "@Enemy patrols spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 2000),
						(display_message, "@Medium-sized group of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 4000),
						(display_message, "@Significant group of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 8000),
						(display_message, "@Army of enemies spotted near {s1}."),
					(else_try),
						(lt, ":exact_enemy_strength", 16000),
						(display_message, "@Large army of enemies spotted near {s1}."),
					(else_try),
						(display_message, "@Great host of enemies spotted near {s1}."),
					(try_end),
					#maybe do audio sound?
					
				(try_end),
		])

	#script_spawn_bandits - tom made
	# NOTE: NOT PRESENT IN NATIVE SCRIPT! AD1257 devs
	# INPUT: none
	# OUTPUT: none
spawn_bandits2 = (
			"spawn_bandits2",
			[
			(set_spawn_radius, 3),
			(assign, ":num_parties", 0),
		(try_for_range, ":party_template", 0, 7),
			(store_add, ":lair_template", ":party_template", "pt_steppe_bandit_lair"),
			(store_add, ":bandit_template", ":party_template", "pt_steppe_bandits"),
			(store_num_parties_of_template, ":num_lairs", ":lair_template"),
			(store_num_parties_of_template, ":num_parties", ":bandit_template"),
			(store_mul, ":spawn_cap", ":num_lairs", 2),
			(lt, ":num_parties", ":spawn_cap"),
			(val_sub, ":spawn_cap", ":num_parties"),
			(try_for_range, reg2, 0, ":spawn_cap"),
				(store_random_party_of_template, ":random_lair", ":lair_template"),
				(spawn_around_party, ":random_lair", ":bandit_template"),
			(party_set_slot, reg0, slot_party_ai_object, ":random_lair"),
				#####(spawn_around_party, ":random_lair", ":bandit_template"),
			(try_end),
		(try_end),
		
		(assign, ":looter_amount", 40),
		(store_num_parties_of_template, ":num_parties", "pt_looters"),
		#looters
		(try_begin),
			(lt, ":num_parties", ":looter_amount"),
			(val_sub, ":looter_amount", ":num_parties"),
			(try_for_range, reg2, 0, ":looter_amount"),
				(store_random_in_range, ":random_village", villages_begin, villages_end),
			(spawn_around_party, ":random_village", "pt_looters"),
			(try_begin),
							(check_quest_active, "qst_deal_with_looters"),
							(party_set_flags, reg0, pf_quest_party, 1),
						(else_try),
							(party_set_flags, reg0, pf_quest_party, 0),
						(try_end),
			(try_end),
		(try_end),
		])
	
		#script_spawn_bandit_lairs - tom made
	# NOTE: NOT PRESENT IN NATIVE SCRIPT! AD1257 devs
	#INPUT: NONE
	#OUTPUT: NONE
	#DESCRIPTION: spawns a bunch of bandit lairs. Bandits lairs latter spawn bandits, excluding the looters.
spawn_bandit_lairs = (
		"spawn_bandit_lairs",
	[
		#standart
		(party_template_set_slot, "pt_steppe_bandits", slot_party_template_lair_type, "pt_steppe_bandit_lair"), #ukraine and ilkhanae
				(party_template_set_slot, "pt_taiga_bandits", slot_party_template_lair_type, "pt_taiga_bandit_lair"), #rus
				(party_template_set_slot, "pt_mountain_bandits", slot_party_template_lair_type, "pt_mountain_bandit_lair"), #scandinavia, italy, greece, iberia
				(party_template_set_slot, "pt_forest_bandits", slot_party_template_lair_type, "pt_forest_bandit_lair"),  #baltic - lithuania, to, poland, halych
				(party_template_set_slot, "pt_sea_raiders", slot_party_template_lair_type, "pt_sea_raider_lair"), #spawn around boats
				(party_template_set_slot, "pt_desert_bandits", slot_party_template_lair_type, "pt_desert_bandit_lair"), #africa - egpyt, libija, maroco, crus states
				(party_template_set_slot, "pt_robber_knights", slot_party_template_lair_type, "pt_robber_knight_lair"), #europe
		
		#lets get amount of bandit camps
		(set_spawn_radius, 4),
		(assign, ":num_parties", 0),
		(try_for_range, ":party_template", "pt_steppe_bandit_lair", "pt_looter_lair"),
			(store_num_parties_of_template, ":num", ":party_template"),
			(val_add, ":num_parties", ":num"),
		(try_end),
		# (store_num_parties_of_template, ":num", "pt_robber_knights"),
		# (val_add, ":num_parties", ":num"),
		
		# (assign, reg0, ":num_parties"),
		# (display_message, "@num_of_parties: {reg0}"),
		(assign, ":lair_cap", 32),
		(try_begin),
			(lt, ":num_parties", ":lair_cap"),
			(val_sub, ":lair_cap", ":num_parties"),
			(gt, ":lair_cap", 0),
			(try_for_range, reg1, 0, ":lair_cap"),
				(store_random_in_range, ":random", 0, 101),
				(try_begin), #bandit knights
					(le, ":random", 5),
					(store_random_in_range, ":random_center", walled_centers_begin, walled_centers_end),
				(spawn_around_party, ":random_center", "pt_robber_knight_lair"),
				#(display_message, "@spwaning knighrts"),
				(else_try), #other bandits, excluding the looters
					(le, ":random", 75),
				(store_random_in_range, ":random_center", walled_centers_begin, walled_centers_end),
				(assign, ":terrain", 0),
				(party_get_current_terrain, ":terrain", ":random_center"),
				(try_begin),
					(this_or_next|eq, ":terrain", rt_steppe),
					(eq, ":terrain", rt_steppe_forest),
					(assign, ":party_to_spawn", "pt_steppe_bandit_lair"),
					#(display_message, "@spwaning steppe"),
				(else_try),
					(this_or_next|eq, ":terrain", rt_snow),
					(eq, ":terrain", rt_snow_forest),
					(assign, ":party_to_spawn", "pt_taiga_bandit_lair"),
					#(display_message, "@spwaning taiga"),
				(else_try),
					(this_or_next|eq, ":terrain", rt_desert),
					(eq, ":terrain", rt_desert_forest),
					(assign, ":party_to_spawn", "pt_desert_bandit_lair"),
				 # (display_message, "@spwaning desert"),
				(else_try), #plain
					(store_random_in_range, ":random", 0, 101), #this is reused!
					(try_begin),
						(lt, ":random", 50),
					(assign, ":party_to_spawn", "pt_forest_bandit_lair"),
					#(display_message, "@spwaning forest"),
					(else_try),
						(assign, ":party_to_spawn", "pt_mountain_bandit_lair"),
					#(display_message, "@spwaning mountain"),
					(try_end),
				(try_end),
				(spawn_around_party,":random_center", ":party_to_spawn"),
				(else_try), #pirates
					(store_random_in_range, ":random_center", "p_ship_1", "p_looter_spawn_point"),
					(spawn_around_party, ":random_center", "pt_sea_raider_lair"),
					#(display_message, "@spwaning sea"),
				(try_end),
			(try_end), #cycle end
		(try_end),
	])

#script_raf_replace_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: party_id, old_troop, new_troop
	#OUTPUT: NONE
raf_replace_troop =(
	"raf_replace_troop",
		[
		(store_script_param, ":party_id", 1),
		(store_script_param, ":old_troop", 2),
		(store_script_param, ":new_troop", 3),
		
		(party_get_num_companion_stacks, ":num_stacks",":party_id"),
		(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
			(party_stack_get_troop_id,     ":stack_troop",":party_id",":stack_no"),
			(try_begin),
			(eq, ":stack_troop", ":old_troop"),
			(party_stack_get_size,    ":stack_size",":party_id",":stack_no"),
			(party_remove_members, ":party_id", ":stack_troop", ":stack_size"),
			(party_add_members, ":party_id", ":new_troop", ":stack_size"),
			(try_begin),
				(eq, ":party_id", "p_main_party"),
				(str_store_troop_name, s1, ":stack_troop"),
				(str_store_troop_name, s2, ":new_troop"),
				(assign, reg0, ":stack_size"),
				#(display_message, "@replacing {s1} with {s2}, qty: {reg0}", 0xff0000),
			(try_end),
			(try_end),
		(try_end),
	])

#script_raf_send_messenger_to_companion
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: target_party, orders_object
		# OUTPUT: NONE 		
raf_send_messenger_to_companion = (
	"raf_send_messenger_to_companion",
		[
			(store_script_param, ":target_party", 1),
			(store_script_param, ":orders_object", 2),
			
			(set_spawn_radius, 1),
			(spawn_around_party, "$current_town", "pt_messenger_party"),
			(assign,":spawned_party",reg0),
			(party_add_members, ":spawned_party", "trp_raf_messenger", 1),
			(try_begin),
			(gt, "$players_kingdom", 0),
			(party_set_faction, ":spawned_party", "$players_kingdom"),
			(party_set_slot, ":spawned_party", slot_center_original_faction, "$players_kingdom"),
			(else_try),
			(party_set_faction, ":spawned_party", "fac_player_faction"),
			(party_set_slot, ":spawned_party", slot_center_original_faction, "fac_player_faction"),
			(try_end),
			
			(party_set_slot, ":spawned_party", slot_party_type, raf_spt_messenger),
			(party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
			
			(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
			(party_set_ai_object, ":spawned_party", ":target_party"),
			(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
			(party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
			(troop_set_slot, ":orders_object", slot_troop_traveling, 1),
			
		])
		
