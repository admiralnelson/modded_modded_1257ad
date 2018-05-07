from header import *
		# script_cf_player_has_item_without_modifier
		# Input: arg1 = item_id, arg2 = modifier
		# Output: none (can_fail)
cf_player_has_item_without_modifier	= (
	"cf_player_has_item_without_modifier",
			[
				(store_script_param, ":item_id", 1),
				(store_script_param, ":modifier", 2),
				(player_has_item, ":item_id"),
				#checking if any of the meat is not rotten
				(assign, ":has_without_modifier", 0),
				(troop_get_inventory_capacity, ":inv_size", "trp_player"),
				(try_for_range, ":i_slot", 0, ":inv_size"),
					(troop_get_inventory_slot, ":cur_item", "trp_player", ":i_slot"),
					(eq, ":cur_item", ":item_id"),
					(troop_get_inventory_slot_modifier, ":cur_modifier", "trp_player", ":i_slot"),
					(neq, ":cur_modifier", ":modifier"),
					(assign, ":has_without_modifier", 1),
					(assign, ":inv_size", 0), #break
				(try_end),
				(eq, ":has_without_modifier", 1),
		])
		
		# script_get_player_party_morale_values
		# Output: reg0 = player_party_morale_target
get_player_party_morale_values	= (
	"get_player_party_morale_values",
			[
				(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
				(assign, ":num_men", 0),
				(try_for_range, ":i_stack", 1, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(val_add, ":num_men", 1), #it was 3 in "Mount&Blade", now it is 1 in Warband
					(else_try),
						(party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
						(val_add, ":num_men", ":stack_size"),
					(try_end),
				(try_end),
				(assign, "$g_player_party_morale_modifier_party_size", ":num_men"),
				
				(store_skill_level, ":player_leadership", "skl_leadership", "trp_player"),
				
				(try_begin),
					(eq, "$players_kingdom", "fac_player_supporters_faction"),
					(faction_get_slot, ":cur_faction_king", "$players_kingdom", slot_faction_leader),
					(eq, ":cur_faction_king", "trp_player"),
					(store_mul, "$g_player_party_morale_modifier_leadership", ":player_leadership", 18), #tom was 15
				(else_try),
					(store_mul, "$g_player_party_morale_modifier_leadership", ":player_leadership", 15), #tom was 12
				(try_end),
				
				(assign, ":new_morale", "$g_player_party_morale_modifier_leadership"),
				(val_sub, ":new_morale", "$g_player_party_morale_modifier_party_size"),
				
				(val_add, ":new_morale", 50),
				
				(assign, "$g_player_party_morale_modifier_food", 0),
				(try_for_range, ":cur_edible", food_begin, food_end),
					(call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
					(item_get_slot, ":food_bonus", ":cur_edible", slot_item_food_bonus),
					
					(val_mul, ":food_bonus", 3),
					(val_div, ":food_bonus", 2),
					
					(val_add, "$g_player_party_morale_modifier_food", ":food_bonus"),
				(try_end),
				(val_add, ":new_morale", "$g_player_party_morale_modifier_food"),
				
				(try_begin),
					(eq, "$g_player_party_morale_modifier_food", 0),
					(assign, "$g_player_party_morale_modifier_no_food", 30),
					(val_sub, ":new_morale", "$g_player_party_morale_modifier_no_food"),
				(else_try),
					(assign, "$g_player_party_morale_modifier_no_food", 0),
				(try_end),
				
				(assign, "$g_player_party_morale_modifier_debt", 0),
				(try_begin),
					(gt, "$g_player_debt_to_party_members", 0),
					(call_script, "script_calculate_player_faction_wage"),
					(assign, ":total_wages", reg0),
					(store_mul, "$g_player_party_morale_modifier_debt", "$g_player_debt_to_party_members", 10),
					(val_max, ":total_wages", 1),
					(val_div, "$g_player_party_morale_modifier_debt", ":total_wages"),
					(val_clamp, "$g_player_party_morale_modifier_debt", 1, 31),
					(val_sub, ":new_morale", "$g_player_party_morale_modifier_debt"),
				(try_end),
								
				(val_clamp, ":new_morale", 0, 100),
				(assign, reg0, ":new_morale"),
		])
		
#script_get_max_skill_of_player_party
# INPUT: arg1 = skill_no
# OUTPUT: reg0 = max_skill, reg1 = skill_owner_troop_no
get_max_skill_of_player_party = (
	"get_max_skill_of_player_party",
			[(store_script_param, ":skill_no", 1),
				(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
				(store_skill_level, ":max_skill", ":skill_no", "trp_player"),
				(assign, ":skill_owner", "trp_player"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(neg|troop_is_wounded, ":stack_troop"),
					(store_skill_level, ":cur_skill", ":skill_no", ":stack_troop"),
					(gt, ":cur_skill", ":max_skill"),
					(assign, ":max_skill", ":cur_skill"),
					(assign, ":skill_owner", ":stack_troop"),
				(try_end),
				(party_get_skill_level, reg0, "p_main_party", ":skill_no"),
				##     (assign, reg0, ":max_skill"),
				(assign, reg1, ":skill_owner"),
		])
		

		#script_offer_ransom_amount_to_player_for_prisoners_in_party
		# INPUT: arg1 = party_no
		# OUTPUT: reg0 = result (1 = offered, 0 = not offered)
offer_ransom_amount_to_player_for_prisoners_in_party = (
	"offer_ransom_amount_to_player_for_prisoners_in_party",
			[(store_script_param, ":party_no", 1),
				(assign, ":result", 0),
				(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(eq, ":result", 0),
					(party_prisoner_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(this_or_next|troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
					(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_lady),
					(store_troop_faction, ":stack_troop_faction", ":stack_troop"),
					(store_random_in_range, ":random_no", 0, 100),
					(try_begin),
						(faction_slot_eq, ":stack_troop_faction", slot_faction_state, sfs_active),
						(le, ":random_no", 5),
						(neq, "$g_ransom_offer_rejected", 1),
						(assign, ":num_stacks", 0), #break
						(assign, ":result", 1),
						(assign, "$g_ransom_offer_troop", ":stack_troop"),
						(assign, "$g_ransom_offer_party", ":party_no"),
						(jump_to_menu, "mnu_enemy_offer_ransom_for_prisoner"),
					(try_end),
				(try_end),
				(assign, reg0, ":result"),
		])
		
		
		# script_remove_cattles_if_herd_is_close_to_party
		# Input: arg1 = party_no, arg2 = maximum_number_of_cattles_required
		# Output: reg0 = number_of_cattles_removed
remove_cattles_if_herd_is_close_to_party = (
	"remove_cattles_if_herd_is_close_to_party",
			[
				(store_script_param, ":party_no", 1),
				(store_script_param, ":max_req", 2),
				(assign, ":cur_req", ":max_req"),
				(try_for_parties, ":cur_party"),
					(gt, ":cur_req", 0),
					(party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
					(store_distance_to_party_from_party, ":dist", ":cur_party", ":party_no"),
					(lt, ":dist", 3),
					
					#Do not use the quest herd for "move cattle herd"
					(assign, ":subcontinue", 1),
					(try_begin),
						(check_quest_active, "qst_move_cattle_herd"),
						(quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
						(assign, ":subcontinue", 0),
					(try_end),
					(eq, ":subcontinue", 1),
					#Do not use the quest herd for "move cattle herd" ends
					
					(party_count_companions_of_type, ":num_cattle", ":cur_party", "trp_cattle"),
					(try_begin),
						(le, ":num_cattle", ":cur_req"),
						(assign, ":num_added", ":num_cattle"),
						(remove_party, ":cur_party"),
					(else_try),
						(assign, ":num_added", ":cur_req"),
						(party_remove_members, ":cur_party", "trp_cattle", ":cur_req"),
					(try_end),
					(val_sub, ":cur_req", ":num_added"),
					
					
					(try_begin),
						(party_slot_eq, ":party_no", slot_party_type, spt_village),
						(party_get_slot, ":village_cattle_amount", ":party_no", slot_village_number_of_cattle),
						(val_add, ":village_cattle_amount", ":num_added"),
						(party_set_slot, ":party_no", slot_village_number_of_cattle, ":village_cattle_amount"),
					(try_end),
					
					(assign, reg3, ":num_added"),
					(str_store_party_name_link, s1, ":party_no"),
					(display_message, "@You brought {reg3} heads of cattle to {s1}."),
					(try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, ":village_cattle_amount"),
						(display_message, "@{!}Village now has {reg4}"),
					(try_end),
				(try_end),
				(store_sub, reg0, ":max_req", ":cur_req"),
		])
		