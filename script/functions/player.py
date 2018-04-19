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
		