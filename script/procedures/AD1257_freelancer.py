from header import *

###script_pass_all_posetions_from_lord_to_lord
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	###input: lord_from, lord_to
	###output: none
	##gives all the posetion(except items) to the order lord. Items are remvoed and bread is added
pass_all_posetions_from_lord_to_lord = (
	"pass_all_posetions_from_lord_to_lord",
	[
		 (store_script_param, ":lord_from", 1),
		 (store_script_param, ":lord_to", 2),
		 
		 ##gold
		 (store_troop_gold,":gold", ":lord_from"),
		 (troop_remove_gold,":lord_from",":gold"),
		 (troop_add_gold, ":lord_to", ":gold"),
		 ##items
		 (troop_clear_inventory,":lord_from"),
		 (try_for_range, reg1, all_items_begin,all_items_end),
			 (troop_has_item_equipped,":lord_from",reg1),
		 (troop_remove_item, ":lord_from",reg1),
		 (try_end),
		 (troop_clear_inventory,":lord_from"),
		 ##land
		 # (try_for_range, reg1, centers_begin, centers_end),
			 # (party_get_slot, ":center_lord", reg1, slot_town_lord),
		 # (eq, ":center_lord", ":lord_from"),
		 # (call_script, "script_give_center_to_lord", reg1, ":lord_to", 0),
		 # (try_end),
		 ##bread

	])

	###script_desert_order
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: checks if player is in an crusader order and if so does the penalty for deserting
	#input: none
	#output: none
desert_order = (
	"desert_order",
	[
		(try_begin),
		(eq, "$crusader_order_joined", 1),
		(display_message, "@Deserting the grandmaster of your order had brought you much dishonor"),
		(call_script, "script_change_player_honor", -50),
		(call_script, "script_change_troop_renown", "trp_player", -50),
		(try_end),
	])

	#script_freelancer_attach_party
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none	
	#+freelancer start
freelancer_attach_party	 = (
	"freelancer_attach_party",
		[
			#prepare player to be part of lord's party
				(party_attach_to_party, "p_main_party", "$enlisted_party"),
				(set_camera_follow_party, "$enlisted_party"),
				(party_set_flags, "$enlisted_party", pf_always_visible, 1),
				(disable_party, "p_main_party"),

		#initialize service variable
		(assign, "$freelancer_state", 1),		
		])

#script_freelancer_detach_party
	 # WARNING: this is totally new procedure (not present in native). 1257AD devs
	 # INPUT: none
	 # OUTPUT: none	
freelancer_detach_party	 = (
	"freelancer_detach_party",
		[
			#removes player from commanders party
		(enable_party, "p_main_party"),
				(party_detach, "p_main_party"),
		
		(try_begin),
			(party_is_active, "$enlisted_party"),
			(party_relocate_near_party, "p_main_party", "$enlisted_party", 2),
			(party_set_flags, "$enlisted_party", pf_always_visible, 0),
		(try_end),	
		
			(set_camera_follow_party, "p_main_party"),
		(assign, "$g_player_icon_state", pis_normal),
	])

	 # script_event_player_enlists
	# ADDS THE PLAYER TO THE LORD'S PARTY  
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: tier
	# OUTPUT: none
event_player_enlists	 = (
	"event_player_enlists",
		[
		(store_script_param, ":tier", 1),
			#initialize service variables
				(troop_get_xp, ":xp", "trp_player"),
		(troop_set_slot, "trp_player", slot_troop_freelancer_start_xp, ":xp"),
				(store_current_day, ":day"), 
				(troop_set_slot, "trp_player", slot_troop_freelancer_start_date, ":day"),		
		(party_get_morale, ":morale", "p_main_party"),
		(party_set_slot, "p_main_party", slot_party_orig_morale, ":morale"),
				#(assign, "$freelancer_state", 1), #moved to script
	
				#needed to stop bug where parties attack the old player party
				(call_script, "script_set_parties_around_player_ignore_player", 2, 4),
				#set lord as your commander
		(assign, "$enlisted_lord", "$g_talk_troop"),
		(troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), 
				#removes troops from player party
				(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
				(try_for_range_backwards, ":cur_stack", 1, ":num_stacks"), #lower bound is 1 to ignore player character
					 (party_stack_get_troop_id, ":cur_troops", "p_main_party", ":cur_stack"),
					 (party_stack_get_size, ":cur_size", "p_main_party", ":cur_stack"),
					 (party_remove_members, "p_main_party", ":cur_troops", ":cur_size"),
				(try_end),
				
		#set faction relations to allow player to join battles
				(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(try_begin),
			(store_relation, ":player_relation", ":commander_faction", "fac_player_supporters_faction"),
			(lt, ":player_relation", 5),
			(call_script, "script_set_player_relation_with_faction", ":commander_faction", 5),
		(try_end),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					 (neq, ":commander_faction", ":cur_faction"),
			 (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
			 (store_relation, ":player_relation", ":cur_faction", "fac_player_supporters_faction"),
			 (ge, ":player_relation", 0),
					 (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
				(try_end),		

		###TOM
				#adds standard issued equipment
		# (try_begin),
			# (neg|faction_slot_eq, ":commander_faction", slot_faction_freelancer_troop, 0),
			# (faction_get_slot, "$player_cur_troop", ":commander_faction", slot_faction_freelancer_troop),
		# (else_try),
			# (faction_get_slot, "$player_cur_troop", ":commander_faction", slot_faction_tier_1_troop),
		# (try_end),	
		(call_script, "script_freelancer_get_troop", "$enlisted_lord", ":commander_faction", ":tier"),		
		(assign, "$player_cur_troop", reg1),
		###TOM
		(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),

		(call_script, "script_freelancer_attach_party"),
		#makes Lords banner the players
		(troop_get_slot, ":banner", "$enlisted_lord", slot_troop_banner_scene_prop),
		(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":banner"),
				(display_message, "@You have been enlisted!"),	

		
				(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, ":commander_faction"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_target_party, "$enlisted_party"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_importance, 5),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_xp_reward, 1000),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_gold_reward, 100),
		(setup_quest_text, "qst_freelancer_enlisted"),
		(str_clear, s2), #description. necessary?
				(call_script, "script_start_quest", "qst_freelancer_enlisted", "$enlisted_lord"),
		(str_store_troop_name, s5, "$player_cur_troop"),
		(str_store_string, s5, "@Current rank: {s5}"),
				(add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),		
		])

    #script_event_player_discharge
	#  RUNS IF THE PLAYER LEAVES THE ARMY
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
event_player_discharge	 = (
	"event_player_discharge",
		[
		#removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", 5),
		(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
						(neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
			(store_relation, ":player_relation", ":cur_faction", "fac_player_supporters_faction"),
			(lt, ":player_relation", 0),
						(call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
				(try_end),
		# removes standard issued equipment
		# (try_for_range, ":cur_inv_slot", ek_item_0, ek_food),
			# (troop_get_inventory_slot, ":soldier_equipment", "$player_cur_troop", ":cur_inv_slot"),
			# (ge, ":soldier_equipment", 0),
			# (troop_remove_item, "trp_player", ":soldier_equipment"),
		# (try_end),
		(call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),		
		(troop_equip_items, "trp_player"),
		

		(troop_set_slot, "trp_player", slot_troop_current_mission, 0),
		(troop_set_slot, "trp_player", slot_troop_days_on_mission, 0),
		(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0),
		(assign, "$freelancer_state", 0),
		(call_script, "script_freelancer_detach_party"),
		(rest_for_hours, 0,0,0),
		(display_message, "@You have left your commander!"), 

				#(call_script, "script_cancel_quest", "qst_freelancer_enlisted"),
		(call_script, "script_finish_quest", "qst_freelancer_enlisted", 100), #percentage--make based on days served?
		])
	
	#script_event_player_vacation
		#  RUNS IF THE PLAYER GOES ON VACATION
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: none
		# OUTPUT: none
event_player_vacation	 = (
	"event_player_vacation",
		[
			(troop_set_slot, "trp_player", slot_troop_current_mission, plyr_mission_vacation), ###move to quests, not missions
		(troop_set_slot, "trp_player", slot_troop_days_on_mission, 14),
	
		#removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
						(neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
						(call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
				(try_end),

		(assign, "$freelancer_state", 2),
		(call_script, "script_freelancer_detach_party"),
		(rest_for_hours, 0,0,0),
		(display_message, "@You have been granted leave!"), 	

		(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, ":commander_faction"),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_target_party, "$enlisted_party"),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_importance, 0),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_xp_reward, 50),
		(quest_set_slot, "qst_freelancer_vacation",	slot_quest_expiration_days, 14),
		(setup_quest_text, "qst_freelancer_vacation"),
		(str_clear, s2), #description. necessary?
				(call_script, "script_start_quest", "qst_freelancer_vacation", "$enlisted_lord"),
		])

		#script_event_player_returns_vacation
	# RUNS WHEN PLAYER RETURNS FROM VACATION
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
event_player_returns_vacation = (
	"event_player_returns_vacation",
		[
				(troop_set_slot, "trp_player", slot_troop_current_mission, 0),
		(troop_set_slot, "trp_player", slot_troop_days_on_mission, 0),
		
		#needed to stop bug where parties attack the old player party
				(call_script, "script_set_parties_around_player_ignore_player", 2, 4),

				#removes troops from player party #Caba--could use party_clear? and then add the player back?
				(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
				(try_for_range_backwards, ":cur_stack", 1, ":num_stacks"), #lower bound is 1 to ignore player character
					 (party_stack_get_troop_id, ":cur_troops", "p_main_party", ":cur_stack"),
					 (party_stack_get_size, ":cur_size", "p_main_party", ":cur_stack"),
					 (party_remove_members, "p_main_party", ":cur_troops", ":cur_size"),
				(try_end),
		
				#To fix any errors of the lord changing parties
		(troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), 
		
		#set faction relations to allow player to join battles
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					 (neq, ":commander_faction", ":cur_faction"),
			 (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					 (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
				(try_end),	
		(try_begin),
			(store_relation, ":player_relation", ":commander_faction", "fac_player_supporters_faction"),
			(lt, ":player_relation", 5),
			(call_script, "script_set_player_relation_with_faction", ":commander_faction", 5),
		(try_end),

		(call_script, "script_freelancer_attach_party"),
		(display_message, "@You have rejoined your commander!"), 		
		])
	
	#script_event_player_deserts
	# RUNS IF PLAYER DESERTS OR IS AWOL
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
event_player_deserts = (
	"event_player_deserts",
	 [     
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
	(call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", -10), 
		(call_script, "script_change_player_relation_with_troop", "$enlisted_lord", -10),
		(call_script, "script_change_player_honor", -20),
	
	(troop_set_slot, "trp_player", slot_troop_current_mission, 0),
	(troop_set_slot, "trp_player", slot_troop_days_on_mission, 0),
	(faction_set_slot, ":commander_faction", slot_faction_freelancer_troop, 0),
	(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0),
	(rest_for_hours, 0,0,0),
	(assign, "$freelancer_state", 0),
	#(display_message, "@You have deserted your commander!"), #Taken care of elsewhere
	(call_script, "script_fail_quest", "qst_freelancer_enlisted"),
	
	
	 ])	

	#script_party_restore
		# RETURNS PART OF THE ORIGINAL PARTY
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: none
		# OUTPUT: none
party_restore	 = (
	"party_restore", 
		[
				(store_current_day, ":cur_day"),
				#formula for soldier desertion chance
		(troop_get_slot, ":service_day_start", "trp_player", slot_troop_freelancer_start_date),
				(store_sub, ":service_length", ":cur_day", ":service_day_start"), #gets number of days served
		(party_get_slot, ":morale", "p_main_party", slot_party_orig_morale),
				(store_add, ":return_chance", 800, ":morale"), #up to 100
				(val_sub, ":return_chance", ":service_length"), #up to far over 100

				#loop that looks at each troop stack in a party, 
				#then decides if troops of that stack will return, 
				#and randomly assigns a number of troops in that stack to return
				(party_get_num_companion_stacks, ":num_stacks", "p_freelancer_party_backup"),
				(try_for_range, ":cur_stack", 0, ":num_stacks"),
			(assign, ":stack_amount", 0),
			(party_stack_get_troop_id, ":return_troop", "p_freelancer_party_backup", ":cur_stack"),
			(neq, ":return_troop", "trp_player"),
			(try_begin),
				(troop_is_hero, ":return_troop"), #bugfix for companions (simple, they always return)
				(assign, ":stack_amount", 1),
			(else_try),
				#limit may need changed for more accurate probability
				(store_random_in_range, ":return_random", 0, 1000),
				(is_between, ":return_random", 0, ":return_chance"),
				(party_stack_get_size, ":stack_size", "p_freelancer_party_backup", ":cur_stack"),
				#checks what chance there is that all troops in stack will return
				(store_random_in_range, ":return_random", 0, 1000),
				(try_begin),
					(is_between, ":return_random", 0, ":return_chance"),
					(assign, ":stack_amount", ":stack_size"),
				(else_try),
					#else random number of troops return
					(store_random_in_range, ":stack_amount", 0, ":stack_size"),
				(try_end),
			(try_end),
			(ge, ":stack_amount", 1),
			(party_add_members, "p_main_party", ":return_troop", ":stack_amount"),
				(try_end),
		(party_clear, "p_freelancer_party_backup"),
		])

#script_get_desert_troops
	#  CALCULATES NUMBER OF DESERTING TROOPS
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
get_desert_troops	 = (
	"get_desert_troops", #CABA - check this
		[
				(party_get_morale, ":commander_party_morale", "$enlisted_party"), #does this actually get tracked for non-player parties?
				(store_current_day, ":cur_day"),
				#formula for soldier desertion chance
				#gets number of days served
		(troop_get_slot, ":service_day_start", "trp_player", slot_troop_freelancer_start_date),
				(store_sub, ":service_length", ":cur_day", ":service_day_start"),
				#inverts the commander's party morale
				(store_sub, ":commander_neg_morale", 100, ":commander_party_morale"), #still a positive number... 100-80 = 20
				(store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
				(store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
				#had to multiply these skills to give them a decent effect on desertion chance
				(val_mul, ":cur_leadership", 10), #up to 100
				(val_mul, ":cur_persuasion", 10), #up to 100
				(store_add, ":desert_chance", ":cur_leadership", ":cur_persuasion"), #up to 200
		(val_add, ":desert_chance", ":service_length"), #up to 400 maybe
				(val_add, ":desert_chance", ":commander_neg_morale"), #up to 450, maybe? if party morale is down to 50
				#loop that looks at each troop stack in a party, 
				#then decides if troops of that stack will desert, 
				#and randomly assigns a number of troops in that stack to desert
				(party_get_num_companion_stacks, ":num_stacks", "$enlisted_party"),
				(try_for_range_backwards, ":cur_stack", 1, ":num_stacks"),
						#limit may need changed for more accurate probability
						(store_random_in_range, ":desert_random", 0, 1000),
						(is_between, ":desert_random", 0, ":desert_chance"),
			#switching deserting troops to player party
			(party_stack_get_troop_id, ":desert_troop", "$enlisted_party", ":cur_stack"),
			(party_stack_get_size, ":stack_size", "$enlisted_party", ":cur_stack"),
			(store_random_in_range, ":stack_amount", 0, ":stack_size"),
			(party_remove_members, "$enlisted_party", ":desert_troop", ":stack_amount"),
			(party_add_members, "p_main_party", ":desert_troop", ":stack_amount"),
				(try_end),        		
		])

	 #script_freelancer_keep_field_loot
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
freelancer_keep_field_loot = (
	"freelancer_keep_field_loot",
	 [
	(get_player_agent_no, ":player"),
	(try_for_range, ":ek_slot", ek_item_0, ek_head),
		(agent_get_item_slot, ":item", ":player", ":ek_slot"), 
		(gt, ":item", 0),
		(neg|troop_has_item_equipped, "trp_player", ":item"),
		(troop_add_item, "trp_player", ":item"),
	(try_end),
	(agent_get_horse, ":horse", ":player"),
	(try_begin),
		(gt, ":horse", 0),
		(agent_get_item_id, ":horse", ":horse"),
		(troop_get_inventory_slot, ":old_horse", "trp_player", ek_horse),
		(neq, ":horse", ":old_horse"),
		(try_begin),
		(gt, ":old_horse", 0),
		(troop_get_inventory_slot_modifier, ":horse_imod", "trp_player", ek_horse),
		(troop_add_item, "trp_player", ":old_horse", ":horse_imod"),
		(try_end),
		(troop_set_inventory_slot, "trp_player", ek_horse, ":horse"),
	(try_end),
	 ])

	 #script_freelancer_equip_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs 
	# INPUT: source_troop
	# OUTPUT: none
freelancer_equip_troop = (
	"freelancer_equip_troop",
	 [
		(store_script_param_1, ":source_troop"),
	
	(str_clear, s2),
	(set_show_messages, 0),
	
	(assign, ":recording_slot", slot_freelancer_equip_start),	
	(troop_get_inventory_capacity, ":troop_cap", ":source_troop"),
	(assign, ":melee_given", 0),
	(assign, ":needs_ammo", 0),
	(assign, ":open_weapon_slot", 0),
	(try_for_range, ":type", itp_type_horse, itp_type_pistol),
			(neq, ":type", itp_type_goods),
		(neq, ":type", itp_type_arrows),
		(neq, ":type", itp_type_bolts),
		
		#Assign Prob. of Getting Type
		(assign, ":continue", 0),
		(try_begin),
			(troop_is_guarantee_horse, ":source_troop"),
				(eq, ":type", itp_type_horse),
			(assign, ":continue", 1),
		(else_try),
				(troop_is_guarantee_ranged, ":source_troop"),
				(this_or_next|eq, ":type", itp_type_bow),
			(this_or_next|eq, ":type", itp_type_crossbow),
			(eq, ":type", itp_type_thrown),
			(assign, ":continue", 1),
		(else_try),
				(this_or_next|eq, ":type", itp_type_shield), #Shields and all armor pieces are guaranteed
				(ge, ":type", itp_type_head_armor),
			(assign, ":continue", 1),
		(else_try),
				(neq, ":type", itp_type_horse),
				(lt, ":open_weapon_slot", 4),
			(store_random_in_range, ":continue", 0, 3), # 1 chance in three of being 1
		(try_end),
		(eq, ":continue", 1),		
		
		#Clear Temp Array
		(try_for_range, ":inv_slot", 0, 20),
			(troop_set_slot, "trp_temp_array_a", ":inv_slot", 0),
		(try_end),	
		
		#Collect Items from Source Troop
		(assign, ":type_count", 0),
		(try_for_range, ":inv_slot", 0, ":troop_cap"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":item_type", ":item"),
			(eq, ":item_type", ":type"),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),		
			(troop_set_slot, "trp_temp_array_a", ":type_count", ":item"),
			(val_add, ":type_count", 1),
		(try_end),
		(gt, ":type_count", 0),
		
		#Pick Random Item of Type from Troop
		(try_begin),
				(eq, ":type_count", 1),
			(assign, ":index", 0),
		(else_try),
			(store_random_in_range, ":index", 0, ":type_count"),
		(try_end),
		(troop_get_slot, ":item", "trp_temp_array_a", ":index"),
		(gt, ":item", 0),		
		(str_store_item_name, s3, ":item"),
		(str_store_string, s2, "@{s3}, {s2}"),
		
		#Select correct EK slot to force equip
		(try_begin),
				(eq, ":type", itp_type_horse),
			(assign, ":ek_slot", ek_horse),
		(else_try),
				(is_between, ":type", itp_type_head_armor, itp_type_pistol),
			(store_sub, ":shift", ":type", itp_type_head_armor),
			(store_add, ":ek_slot", ek_head, ":shift"),
		(else_try),
			(store_add, ":ek_slot", ek_item_0, ":open_weapon_slot"),
		(try_end),
		
		#Check for item already there, move it if present
		(try_begin),
				(troop_get_inventory_slot, ":old_item", "trp_player", ":ek_slot"),
			(gt, ":old_item", 0),
			(troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ":ek_slot"),
			(troop_add_item, "trp_player", ":old_item", ":old_item_imod"),
		(try_end),
		
		#Add Item
		(troop_set_inventory_slot, "trp_player", ":ek_slot", ":item"),
		(party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
		(val_add, ":recording_slot", 1),
		(try_begin),
				(is_between, ":type", itp_type_one_handed_wpn, itp_type_head_armor), #Uses one of the 4 weapon slots
				(val_add, ":open_weapon_slot", 1),
			(try_begin),
				(is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows),
				(assign, ":melee_given", 1),
						(else_try),
				(eq, ":type", itp_type_bow),
				(assign, ":needs_ammo", itp_type_arrows),
			(else_try),
				(eq, ":type", itp_type_crossbow),
				(assign, ":needs_ammo", itp_type_bolts),
			(try_end),
		(try_end),
	(try_end), #Item Types Loop
	 
		#add ammo for any equipped bow
		(try_begin),
			(neq, ":needs_ammo", 0),		
		#Check for item already in the last slot, move it if present
		(try_begin), 
				(troop_get_inventory_slot, ":old_item", "trp_player", ek_item_3),
			(gt, ":old_item", 0),
			(troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ek_item_3),
			(troop_add_item, "trp_player", ":old_item", ":old_item_imod"), 
		(try_end),
		
		(assign, ":end", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":type", ":item"),
			(eq, ":type", ":needs_ammo"),
			(troop_set_inventory_slot, "trp_player", ek_item_3, ":item"),
			(party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
				(val_add, ":recording_slot", 1),
			(assign, ":open_weapon_slot", 4),
			(str_store_item_name, s3, ":item"),
				(str_store_string, s2, "@{s3}, {s2}"),
			(assign, ":end", 0),
		(try_end),
	(try_end), 
	
	#double check melee was given
	(try_begin),
			(eq, ":melee_given", 0),
		(assign, ":end", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":type", ":item"),
			(is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),	
			(try_begin),
					(gt, ":open_weapon_slot", 3),
					(assign, ":open_weapon_slot", 2),
			(try_end),
			
			#Check for item already there
			(try_begin),
				(troop_get_inventory_slot, ":old_item", "trp_player", ":open_weapon_slot"),
				(gt, ":old_item", 0),
				(troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ":open_weapon_slot"),
				(troop_add_item, "trp_player", ":old_item", ":old_item_imod"),
			(try_end),
			
			(troop_set_inventory_slot, "trp_player", ":open_weapon_slot", ":item"),		
			(party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
				(val_add, ":recording_slot", 1),
			(str_store_item_name, s3, ":item"),
				(str_store_string, s2, "@{s3}, {s2}"),
				(assign, ":end", 0),
		(try_end),
	(try_end), 
	
		(set_show_messages, 1),
	(try_begin),
		(neg|str_is_empty, s2),
		(val_sub, ":recording_slot", slot_freelancer_equip_start),
		(party_set_slot, "p_freelancer_party_backup", slot_freelancer_equip_start - 1, ":recording_slot"),	#Record Number of Items Added
		
		(str_store_troop_name, s1, ":source_troop"),
		(display_message, "@The equipment of a {s1}: {s2}is assigned to you."),	
	(try_end),
	 ])

#script_freelancer_unequip_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs 
	# INPUT: source_troop
	# OUTPUT: none
freelancer_unequip_troop = (
	"freelancer_unequip_troop",
	 [
		(store_script_param_1, ":source_troop"),

	(str_clear, s2),	
	(set_show_messages, 0),
	
	(party_get_slot, ":num_items", "p_freelancer_party_backup", slot_freelancer_equip_start - 1), #Num of items previously given
	
		(troop_get_inventory_capacity, ":cap", "trp_player"),		
	(try_for_range, ":i", 0, ":num_items"),
			(store_add, ":slot", slot_freelancer_equip_start, ":i"),
			(party_get_slot, ":given_item", "p_freelancer_party_backup", ":slot"),
		(gt, ":given_item", 0),
		
		(assign, ":end", ":cap"),
		(try_for_range, ":inv_slot", 0, ":end"),
			(troop_get_inventory_slot, ":item", "trp_player", ":inv_slot"),
			(eq, ":item", ":given_item"),			
			(troop_get_inventory_slot_modifier, ":imod", "trp_player", ":inv_slot"),
			(eq, ":imod", 0), #Native troop items never have modifiers
			
			(troop_set_inventory_slot, "trp_player", ":inv_slot", -1),
			(str_store_item_name, s3, ":item"),
			(str_store_string, s2, "@{s3}, {s2}"),
			
			(assign, ":end", 0), #Break
		(try_end), #Player Inventory Loop
	(try_end), #Item Given Slot Loop

	(set_show_messages, 1),
	(try_begin),
		(neg|str_is_empty, s2),
		(party_set_slot, "p_freelancer_party_backup", slot_freelancer_equip_start - 1, 0),	#Reset Number of Items Added
		(str_store_troop_name, s1, ":source_troop"),
		(display_message, "@The equipment of a {s1}: {s2}is taken from you."),
	(try_end),	
	(troop_equip_items, "trp_player"),
	 ]) 

