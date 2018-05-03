from header import *

		# script_party_get_ideal_size @used for NPC parties.
		# party AI size limit
		# WARNING: modified by 1257AD devs
		# Input: arg1 = party_no
		# Output: reg0: ideal size
party_get_ideal_size = (
			"party_get_ideal_size",
			[
				(store_script_param_1, ":party_no"),
				(assign, ":limit", 30),
				
				(try_begin),
					(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
					(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
					(store_faction_of_party, ":faction_id", ":party_no"),
					#(assign, ":limit", 10),
					# rafi
					(assign, ":limit", 30),
					# end rafi
					(store_skill_level, ":skill", "skl_leadership", ":party_leader"),
					(store_attribute_level, ":charisma", ":party_leader", ca_charisma),
					(val_mul, ":skill", 5),
					(val_add, ":limit", ":skill"),
					(val_add, ":limit", ":charisma"),
					
					(troop_get_slot, ":troop_renown", ":party_leader", slot_troop_renown),
					(store_div, ":renown_bonus", ":troop_renown", 25),
					(val_add, ":limit", ":renown_bonus"),
					
					(try_begin),
						(faction_slot_eq, ":faction_id", slot_faction_leader, ":party_leader"),
						(val_add, ":limit", 100),
					(try_end),
					
					(try_begin),
						(faction_slot_eq, ":faction_id", slot_faction_marshall, ":party_leader"),
						(val_add, ":limit", 20),
					(try_end),
					
					(try_for_range, ":cur_center", castles_begin, castles_end),
						(party_slot_eq, ":cur_center", slot_town_lord, ":party_leader"),
						(val_add, ":limit", 20),
					(try_end),
				(try_end),
				
				#tom
				#check if down to the last stronghold
				(assign, ":double", 0),
				(try_for_range, ":other_centers", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":wall_faction", ":other_centers"),
					(eq, ":faction_id", ":wall_faction"),
					(val_add, ":double", 1),
					(ge, ":double", 2),
					(assign, ":other_centers", 0), #break
				(try_end),
				
				(try_begin),
					(eq, ":double", 1),
					#if a king, increase party size
					#(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
					(faction_slot_eq, ":faction_id", slot_faction_leader, ":party_leader"),
					(val_add, ":limit", 150), #limit increase
				(else_try),
					(eq, ":double", 1),
					(val_add, ":limit", 25), #limit increase
				(try_end),
				
				(val_min, ":limit", 350), #maximum size of a party
				# (store_mul, ":ideal_top_size", ":limit", 3),
				# (val_div, ":ideal_top_size", 2),
				#tom
				
				#tom
				# (store_character_level, ":level", "trp_player"), #increase limits a little bit as the game progresses.
				# (store_add, ":level_factor", 80, ":level"),
				# (val_mul, ":limit", ":level_factor"),
				# (val_div, ":limit", 80),

				(assign, reg0, ":limit"),
		])
		
				#script_game_get_party_prisoner_limit:
		# This script is called from the game engine when the prisoner limit is needed for a party.
		# WARNING : modified by 1257AD devs, arg1 used to be arg1 = party_no
		# INPUT: none
		# OUTPUT: reg0 = prisoner_limit
game_get_party_prisoner_limit = (
			"game_get_party_prisoner_limit",
			[
				#      (store_script_param_1, ":party_no"),
				(assign, ":troop_no", "trp_player"),
				
				(assign, ":limit", 0),
				(store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
				(store_mul, ":limit", ":skill", 15),
				(assign, reg0, ":limit"),
				(set_trigger_result, reg0),
		])
		
		#script_game_get_party_prisoner_limit:
		# This script is called from the game engine when the prisoner limit is needed for a party.
		# WARNING : modified by 1257AD devs, arg1 used to be arg1 = party_no
		# INPUT: none
		# OUTPUT: reg0 = prisoner_limit
game_get_party_prisoner_limit = (
			"game_get_party_prisoner_limit",
			[
				#      (store_script_param_1, ":party_no"),
				(assign, ":troop_no", "trp_player"),
				
				(assign, ":limit", 0),
				(store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
				(store_mul, ":limit", ":skill", 15),
				(assign, reg0, ":limit"),
				(set_trigger_result, reg0),
		])

		#script_game_get_party_speed_multiplier
		# This script is called from the game engine when a skill's modifiers are needed
		# INPUT: arg1 = party_no
		# OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
game_get_party_speed_multiplier = (
			"game_get_party_speed_multiplier",
			[
				(store_script_param, ":party_no", 1),
				
				(party_get_current_terrain, ":party_terrain", ":party_no"),
				
				(assign, ":multiplier", 10),
				(try_begin),
					(call_script, "script_cf_is_party_on_water", ":party_no"),
					(assign, ":multiplier", 5),
			(get_global_cloud_amount, ":cloud"),
			(val_div, ":cloud", 10),
			(val_add, ":multiplier", ":cloud"),
				(else_try),
					(eq, ":party_terrain", rt_steppe),
					(assign, ":multiplier", 12),
				(try_end),
				
				(party_get_template_id, ":party_template", ":party_no"),
				(try_begin),
					(eq, ":party_template", "pt_merchant_caravan"),
					(val_add, ":multiplier", 4),
				(else_try),
					(this_or_next | eq, ":party_template", "pt_steppe_bandits"),
					(this_or_next | eq, ":party_template", "pt_desert_bandits"),
					(this_or_next | eq, ":party_template", "pt_taiga_bandits"),
					(this_or_next | eq, ":party_template", "pt_forest_bandits"),
					(this_or_next | eq, ":party_template", "pt_sea_raiders"),
					(this_or_next | eq, ":party_template", "pt_robber_knights"),
					(this_or_next | eq, ":party_template", "pt_taiga_bandits"),
					(this_or_next | eq, ":party_template", "pt_looters"),
					(this_or_next | eq, ":party_template", "pt_village_farmers"),
					(eq, ":party_template", "pt_deserters"),
					(val_sub, ":multiplier", 2),
				(try_end),
				
				(try_begin),
					(party_slot_eq, ":party_no", slot_party_battle_preparation, 1),
					(assign, ":multiplier", 0),
				(try_end),
		
		(try_begin),
			(party_slot_eq, ":party_no", slot_mongol_camp_status, status_stationed),
					(assign, ":multiplier", 0),
				(try_end),
				
				(assign, ":spd", "$g_travel_speed"),
				(val_mul, ":spd", ":multiplier"),
				(val_div, ":spd", 10),
				(set_trigger_result, ":spd"),
		])


		
	#script_party_calculate_strength:
	# INPUT: arg1 = party_id, arg2 = exclude leader
	# OUTPUT: reg0 = strength
party_calculate_strength = (
		"party_calculate_strength",
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
			(try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
				(party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
				(store_character_level, ":stack_strength", ":stack_troop"),
				(val_add, ":stack_strength", 4), #new was 12 (patch 1.125)
				(val_mul, ":stack_strength", ":stack_strength"),
				(val_mul, ":stack_strength", 2), #new (patch 1.125)
				(val_div, ":stack_strength", 100),
				(val_max, ":stack_strength", 1), #new (patch 1.125)
				(try_begin),
					(neg|troop_is_hero, ":stack_troop"),
					(party_stack_get_size, ":stack_size",":party",":i_stack"),
					(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),                    
					(val_sub, ":stack_size", ":num_wounded"),
					(val_mul, ":stack_strength", ":stack_size"),
				(else_try),
					(troop_is_wounded, ":stack_troop"), #hero & wounded
					(assign, ":stack_strength", 0),
				(try_end),
				(val_add, reg0, ":stack_strength"),
			(try_end),
			(party_set_slot, ":party", slot_party_cached_strength, reg0),
	])
		

		#script_party_calculate_loot:
		# INPUT:
		# param1: Party-id
		# OUTPUT: Returns num looted items in reg(0)
party_calculate_loot = (
	"party_calculate_loot",
			[
				(store_script_param_1, ":enemy_party"), #Enemy Party_id
				
				(call_script, "script_calculate_main_party_shares"),
				(assign, ":num_player_party_shares", reg0),
				
				(try_for_range, ":i_loot", 0, num_party_loot_slots),
					(store_add, ":cur_loot_slot", ":i_loot", slot_party_looted_item_1),
					(party_get_slot, ":item_no", "$g_enemy_party", ":cur_loot_slot"),
					(gt, ":item_no", 0),
					(party_set_slot, "$g_enemy_party", ":cur_loot_slot", 0),
					(val_sub, ":cur_loot_slot", slot_party_looted_item_1),
					(val_add, ":cur_loot_slot", slot_party_looted_item_1_modifier),
					(party_get_slot, ":item_modifier", "$g_enemy_party", ":cur_loot_slot"),
					(troop_add_item, "trp_temp_troop", ":item_no", ":item_modifier"),
				(try_end),
				(party_set_slot, "$g_enemy_party", slot_party_next_looted_item_slot, 0),
				
				(assign, ":num_looted_items",0),
				(try_begin),
					(this_or_next|party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_caravan),
					(this_or_next|party_slot_eq, "$g_enemy_party", slot_party_type, spt_bandit_lair),
					(party_slot_eq, "$g_enemy_party", slot_party_type, spt_village_farmer),
					(store_mul, ":plunder_amount", player_loot_share, 30),
					(val_mul, ":plunder_amount", "$g_strength_contribution_of_player"),
					(val_div, ":plunder_amount", 100),
					(val_div, ":plunder_amount", ":num_player_party_shares"),
					(try_begin),
						(party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_caravan),
						(reset_item_probabilities, 100),
						(assign, ":range_min", trade_goods_begin),
						(assign, ":range_max", trade_goods_end),
					(else_try),
						(party_slot_eq, "$g_enemy_party", slot_party_type, spt_bandit_lair),
						(val_div, ":plunder_amount", 2),
						(reset_item_probabilities, 1),
						(assign, ":range_min", food_begin),
						(assign, ":range_max", food_end),
					(else_try),
						(val_div, ":plunder_amount", 5),
						(reset_item_probabilities, 1),
						(assign, ":range_min", food_begin),
						(assign, ":range_max", food_end),
					(try_end),
					(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
					(try_for_range, ":cur_goods", ":range_min", ":range_max"),
						(try_begin),
							(neg|party_slot_eq, "$g_enemy_party", slot_party_type, spt_bandit_lair),
							(store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
							(party_get_slot, ":cur_price", "$g_enemy_party", ":cur_price_slot"),
						(else_try),
							(assign, ":cur_price", maximum_price_factor),
							(val_add, ":cur_price", average_price_factor),
							(val_div, ":cur_price", 3),
						(try_end),
						
						(assign, ":cur_probability", 100),
						(val_mul, ":cur_probability", average_price_factor),
						(val_div, ":cur_probability", ":cur_price"),
						(assign, reg0, ":cur_probability"),
						(set_item_probability_in_merchandise, ":cur_goods", ":cur_probability"),
					(try_end),
					(troop_add_merchandise, "trp_temp_troop", itp_type_goods, ":plunder_amount"),
					(val_add, ":num_looted_items", ":plunder_amount"),
				(try_end),
				
				#Now loot the defeated party
				(store_mul, ":loot_probability", player_loot_share, 3),
				(val_mul, ":loot_probability", "$g_strength_contribution_of_player"),
				(party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
				(val_add, ":player_party_looting", 10),
				(val_mul, ":loot_probability", ":player_party_looting"),
				(val_div, ":loot_probability", 10),
				(val_div, ":loot_probability", ":num_player_party_shares"),
				
				(party_get_num_companion_stacks, ":num_stacks",":enemy_party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":enemy_party",":i_stack"),
					(neg|troop_is_hero, ":stack_troop"),
					(party_stack_get_size, ":stack_size",":enemy_party",":i_stack"),
					(try_for_range, ":unused", 0, ":stack_size"),
						(troop_loot_troop, "trp_temp_troop", ":stack_troop", ":loot_probability"),
					(try_end),
				(try_end),
				
				#(troop_get_inventory_capacity, ":inv_cap", "trp_temp_troop"),
				#(try_for_range, ":i_slot", 0, ":inv_cap"),
				#  (troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
				#  (is_between, ":item_id", horses_begin, horses_end),
				#  (troop_set_inventory_slot, "trp_temp_troop", ":i_slot", -1),
				#(try_end),
				
				(troop_get_inventory_capacity, ":inv_cap", "trp_temp_troop"),
				(try_for_range, ":i_slot", 0, ":inv_cap"),
					(troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
					(ge, ":item_id", 0),
					(val_add, ":num_looted_items", 1),
				(try_end),
				
				(assign, reg0, ":num_looted_items"),
		])
		
		#script_calculate_main_party_shares:
		# INPUT:
		# Returns number of player party shares in reg0
calculate_main_party_shares =	("calculate_main_party_shares",
			[
				(assign, ":num_player_party_shares", player_loot_share),
				# Add shares for player's party
				(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
				(try_for_range, ":i_stack", 1, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
					(try_begin),
						(neg|troop_is_hero, ":stack_troop"),
						(party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
						(val_add, ":num_player_party_shares", ":stack_size"),
					(else_try),
						(val_add, ":num_player_party_shares", hero_loot_share),
					(try_end),
				(try_end),
				
				(assign, reg0, ":num_player_party_shares"),
		])
		
	#script_update_party_creation_random_limits
	# calculate party maximum limit
	# INPUT: none
	# OUTPUT: returns party size limit based on player level
update_party_creation_random_limits	= (
	"update_party_creation_random_limits",
			[
				(store_character_level, ":player_level", "trp_player"),
				(store_mul, ":upper_limit", ":player_level", 3),
				(val_add, ":upper_limit", 25),
				(val_min, ":upper_limit", 100),
				(set_party_creation_random_limits, 0, ":upper_limit"),
				(assign, reg0, ":upper_limit"),
		])

#script_print_casualties_to_s0:
		# INPUT:
		# param1: Party_id, param2: 0 = use new line, 1 = use comma
		
		#OUTPUT:
		# string register 0.
		
print_casualties_to_s0 = (
	"print_casualties_to_s0",
			[(store_script_param, ":party_no", 1),
				(store_script_param, ":use_comma", 2),
				(str_clear, s0),
				(assign, ":total_reported", 0),
				(assign, ":total_wounded", 0),
				(assign, ":total_killed", 0),
				(assign, ":total_routed", 0),
				(party_get_num_companion_stacks, ":num_stacks",":party_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop_id", ":party_no", ":i_stack"),
					(party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
					(party_stack_get_num_wounded, ":num_wounded", ":party_no", ":i_stack"),
					#get number of routed agent numbers
					(try_begin),
						(this_or_next|eq, ":party_no", "p_main_party"),
						(eq, ":party_no", "p_player_casualties"),
						(troop_get_slot, ":num_routed", ":stack_troop_id", slot_troop_player_routed_agents),
						(troop_set_slot, ":stack_troop_id", slot_troop_player_routed_agents, 0),
					(else_try),
						(party_get_attached_to, ":attached_to", ":party_no"),
						(this_or_next|eq, ":party_no", "p_ally_casualties"),
						(ge, ":attached_to", 0),
						(this_or_next|eq, ":party_no", "p_ally_casualties"),
						(eq, ":attached_to", "p_main_party"),
						(troop_get_slot, ":num_routed", ":stack_troop_id", slot_troop_ally_routed_agents),
						(troop_set_slot, ":stack_troop_id", slot_troop_ally_routed_agents, 0),
					(else_try),
						(troop_get_slot, ":num_routed", ":stack_troop_id", slot_troop_enemy_routed_agents),
						(troop_set_slot, ":stack_troop_id", slot_troop_enemy_routed_agents, 0),
					(try_end),
					(store_sub, ":num_killed", ":stack_size", ":num_wounded"),
					(val_sub, ":num_killed", ":num_routed"),
					(val_add, ":total_killed", ":num_killed"),
					(val_add, ":total_wounded", ":num_wounded"),
					(val_add, ":total_routed", ":num_routed"),
					(try_begin),
						(this_or_next|gt, ":num_killed", 0),
						(this_or_next|gt, ":num_wounded", 0),
						(gt, ":num_routed", 0),
						(store_add, reg3, ":num_killed", ":num_wounded"),
						(store_add, reg3, reg3, ":num_routed"),
						(str_store_troop_name_by_count, s1, ":stack_troop_id", reg3),
						(try_begin),
							(troop_is_hero, ":stack_troop_id"),
							(assign, reg3, 0),
						(try_end),
						(try_begin), #there are people who killed, wounded and routed.
							(gt, ":num_killed", 0),
							(gt, ":num_wounded", 0),
							(gt, ":num_routed", 0),
							(assign, reg4, ":num_killed"),
							(assign, reg5, ":num_wounded"),
							(assign, reg6, ":num_routed"),
							(str_store_string, s2, "str_reg4_killed_reg5_wounded_reg6_routed"),
						(else_try), #there are people who killed and routed.
							(gt, ":num_killed", 0),
							(gt, ":num_routed", 0),
							(assign, reg4, ":num_killed"),
							(assign, reg5, ":num_routed"),
							(str_store_string, s2, "str_reg4_killed_reg5_routed"),
						(else_try), #there are people who killed and wounded.
							(gt, ":num_killed", 0),
							(gt, ":num_wounded", 0),
							(assign, reg4, ":num_killed"),
							(assign, reg5, ":num_wounded"),
							(str_store_string, s2, "str_reg4_killed_reg5_wounded"),
						(else_try), #there are people who wounded and routed.
							(gt, ":num_wounded", 0),
							(gt, ":num_routed", 0),
							(assign, reg4, ":num_wounded"),
							(assign, reg5, ":num_routed"),
							(str_store_string, s2, "str_reg4_wounded_reg5_routed"),
						(else_try), #there are people who only killed.
							(gt, ":num_killed", 0),
							(assign, reg1, ":num_killed"),
							(str_store_string, s3, "@killed"),
							(str_store_string, s2, "str_reg1_blank_s3"),
						(else_try), #there are people who only wounded.
							(gt, ":num_wounded", 0),
							(assign, reg1, ":num_wounded"),
							(str_store_string, s3, "@wounded"),
							(str_store_string, s2, "str_reg1_blank_s3"),
						(else_try), #there are people who only routed.
							(assign, reg1, ":num_routed"),
							(str_store_string, s3, "str_routed"),
							(str_store_string, s2, "str_reg1_blank_s3"),
						(try_end),
						(try_begin),
							(eq, ":use_comma", 1),
							(try_begin),
								(eq, ":total_reported", 0),
								(str_store_string, s0, "@{!}{reg3?{reg3}:} {s1} ({s2})"),
							(else_try),
								(str_store_string, s0, "@{!}{s0}, {reg3?{reg3}:} {s1} ({s2})"),
							(try_end),
						(else_try),
							(str_store_string, s0, "@{!}{s0}^{reg3?{reg3}:} {s1} ({s2})"),
						(try_end),
						(val_add, ":total_reported", 1),
					(try_end),
				(try_end),
				(try_begin),
					(this_or_next|gt, ":total_killed", 0),
					(this_or_next|gt, ":total_wounded", 0),
					(gt, ":total_routed", 0),
					(store_add, ":total_agents", ":total_killed", ":total_wounded"),
					(val_add, ":total_agents", ":total_routed"),
					(assign, reg3, ":total_agents"),
					(try_begin),
						(gt, ":total_killed", 0),
						(gt, ":total_wounded", 0),
						(gt, ":total_routed", 0),
						(assign, reg4, ":total_killed"),
						(assign, reg5, ":total_wounded"),
						(assign, reg6, ":total_routed"),
						(str_store_string, s2, "str_reg4_killed_reg5_wounded_reg6_routed"),
					(else_try),
						(gt, ":total_killed", 0),
						(gt, ":total_routed", 0),
						(assign, reg4, ":total_killed"),
						(assign, reg5, ":total_routed"),
						(str_store_string, s2, "str_reg4_killed_reg5_routed"),
					(else_try),
						(gt, ":total_killed", 0),
						(gt, ":total_wounded", 0),
						(assign, reg4, ":total_killed"),
						(assign, reg5, ":total_wounded"),
						(str_store_string, s2, "str_reg4_killed_reg5_wounded"),
					(else_try),
						(gt, ":total_wounded", 0),
						(gt, ":total_routed", 0),
						(assign, reg4, ":total_wounded"),
						(assign, reg5, ":total_routed"),
						(str_store_string, s2, "str_reg4_wounded_reg5_routed"),
					(else_try),
						(gt, ":total_killed", 0),
						(str_store_string, s2, "@killed"),
					(else_try),
						(gt, ":total_wounded", 0),
						(str_store_string, s2, "@wounded"),
					(else_try),
						(str_store_string, s2, "str_routed"),
					(else_try),
					(try_end),
					(str_store_string, s0, "@{s0}^TOTAL: {reg3} ({s2})"),
				(else_try),
					(try_begin),
						(eq, ":use_comma", 1),
						(str_store_string, s0, "@None"),
					(else_try),
						(str_store_string, s0, "@^None"),
					(try_end),
				(try_end),
		])

#script_write_fit_party_members_to_stack_selection
		# INPUT:
		# param1: party_no, exclude_leader
		#OUTPUT:
		# trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
		# trp_stack_selection_ids slots (2..n = stack troops)
write_fit_party_members_to_stack_selection = (
	"write_fit_party_members_to_stack_selection",
			[
				(store_script_param, ":party_no", 1),
				(store_script_param, ":exclude_leader", 2),
				(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
				(assign, ":slot_index", 2),
				(assign, ":total_fit", 0),
				(try_for_range, ":stack_index", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop", ":party_no", ":stack_index"),
					(assign, ":num_fit", 0),
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(try_begin),
							(neg|troop_is_wounded, ":stack_troop"),
							(this_or_next|eq, ":exclude_leader", 0),
							(neq, ":stack_index", 0),
							(assign, ":num_fit",1),
						(try_end),
					(else_try),
						(party_stack_get_size, ":num_fit", ":party_no", ":stack_index"),
						(party_stack_get_num_wounded, ":num_wounded", ":party_no", ":stack_index"),
						(val_sub, ":num_fit", ":num_wounded"),
					(try_end),
					(try_begin),
						(gt, ":num_fit", 0),
						(troop_set_slot, "trp_stack_selection_amounts", ":slot_index", ":num_fit"),
						(troop_set_slot, "trp_stack_selection_ids", ":slot_index", ":stack_troop"),
						(val_add, ":slot_index", 1),
					(try_end),
					(val_add, ":total_fit", ":num_fit"),
				(try_end),
				(val_sub, ":slot_index", 2),
				(troop_set_slot, "trp_stack_selection_amounts", 0, ":slot_index"),
				(troop_set_slot, "trp_stack_selection_amounts", 1, ":total_fit"),
		])
		
		#script_remove_fit_party_member_from_stack_selection
		# INPUT:
		# param1: slot_index
		#OUTPUT:
		# reg0 = troop_no
		# trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
		# trp_stack_selection_ids slots (2..n = stack troops)
remove_fit_party_member_from_stack_selection = (
	"remove_fit_party_member_from_stack_selection",
			[
				(store_script_param, ":slot_index", 1),
				(val_add, ":slot_index", 2),
				(troop_get_slot, ":amount", "trp_stack_selection_amounts", ":slot_index"),
				(troop_get_slot, ":troop_no", "trp_stack_selection_ids", ":slot_index"),
				(val_sub, ":amount", 1),
				(troop_set_slot, "trp_stack_selection_amounts", ":slot_index", ":amount"),
				(troop_get_slot, ":total_amount", "trp_stack_selection_amounts", 1),
				(val_sub, ":total_amount", 1),
				(troop_set_slot, "trp_stack_selection_amounts", 1, ":total_amount"),
				(try_begin),
					(le, ":amount", 0),
					(troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
					(store_add, ":end_cond", ":num_slots", 2),
					(store_add, ":begin_cond", ":slot_index", 1),
					(try_for_range, ":index", ":begin_cond", ":end_cond"),
						(store_sub, ":prev_index", ":index", 1),
						(troop_get_slot, ":value", "trp_stack_selection_amounts", ":index"),
						(troop_set_slot, "trp_stack_selection_amounts", ":prev_index", ":value"),
						(troop_get_slot, ":value", "trp_stack_selection_ids", ":index"),
						(troop_set_slot, "trp_stack_selection_ids", ":prev_index", ":value"),
					(try_end),
					(val_sub, ":num_slots", 1),
					(troop_set_slot, "trp_stack_selection_amounts", 0, ":num_slots"),
				(try_end),
				(assign, reg0, ":troop_no"),
		])
		
		#script_remove_random_fit_party_member_from_stack_selection
		# INPUT:
		# none
		#OUTPUT:
		# reg0 = troop_no
		# trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
		# trp_stack_selection_ids slots (2..n = stack troops)
remove_random_fit_party_member_from_stack_selection = (
	"remove_random_fit_party_member_from_stack_selection",
			[
				(troop_get_slot, ":total_amount", "trp_stack_selection_amounts", 1),
				(store_random_in_range, ":random_troop", 0, ":total_amount"),
				(troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
				(store_add, ":end_cond", ":num_slots", 2),
				(try_for_range, ":index", 2, ":end_cond"),
					(troop_get_slot, ":amount", "trp_stack_selection_amounts", ":index"),
					(val_sub, ":random_troop", ":amount"),
					(lt, ":random_troop", 0),
					(assign, ":end_cond", 0),
					(store_sub, ":slot_index", ":index", 2),
				(try_end),
				(call_script, "script_remove_fit_party_member_from_stack_selection", ":slot_index"),
		])
		
		#script_party_count_fit_for_battle:
		# Returns the number of unwounded companions in a party
		# INPUT:
		# param1: Party-id
		# OUTPUT: reg0 = result
party_count_fit_for_battle = (
	"party_count_fit_for_battle",
			[
				(store_script_param_1, ":party"), #Party_id
				(party_get_num_companion_stacks, ":num_stacks",":party"),
				(assign, reg0, 0),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":party",":i_stack"),
					(assign, ":num_fit",0),
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(try_begin),
							(neg|troop_is_wounded, ":stack_troop"),
							(assign, ":num_fit", 1),
						(try_end),
					(else_try),
						(party_stack_get_size, ":num_fit",":party",":i_stack"),
						(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
						(val_sub, ":num_fit", ":num_wounded"),
					(try_end),
					(val_add, reg0, ":num_fit"),
				(try_end),
		])

		#script_party_count_members_with_full_health
		# Returns the number of unwounded regulars, and heroes other than player with 100% hitpoints in a party
		# INPUT:
		# param1: Party-id
		# OUTPUT: reg0 = result
party_count_members_with_full_health = (
	"party_count_members_with_full_health",
			[
				(store_script_param_1, ":party"), #Party_id
				(party_get_num_companion_stacks, ":num_stacks",":party"),
				(assign, reg0, 0),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":party",":i_stack"),
					(assign, ":num_fit",0),
					(try_begin),
						(troop_is_hero, ":stack_troop"),
						(neq, ":stack_troop", "trp_player"),
						(store_troop_health, ":troop_hp", ":stack_troop"),
						(try_begin),
							(ge, ":troop_hp", 80),
							(assign, ":num_fit",1),
						(try_end),
					(else_try),
						(party_stack_get_size, ":num_fit",":party",":i_stack"),
						(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
						(val_sub, ":num_fit", ":num_wounded"),
						(val_max, ":num_fit", 0),
					(try_end),
					(val_add, reg0, ":num_fit"),
				(try_end),
		])


		#script_get_stack_with_rank:
		# Returns the stack no, containing unwounded regular companions with rank rank.
		# INPUT:
		# param1: Party-id
		# param2: rank
		
get_stack_with_rank = (
	"get_stack_with_rank",
			[
				(store_script_param_1, ":party"), #Party_id
				(store_script_param_2, ":rank"), #Rank
				(party_get_num_companion_stacks, ":num_stacks",":party"),
				(assign, reg(0), -1),
				(assign, ":num_total", 0),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(eq, reg(0), -1), #continue only if we haven't found the result yet.
					(party_stack_get_troop_id,     ":stack_troop",":party",":i_stack"),
					(neg|troop_is_hero, ":stack_troop"),
					(party_stack_get_size,         ":stack_size",":party",":i_stack"),
					(party_stack_get_num_wounded,  ":num_wounded",":party",":i_stack"),
					(val_sub, ":stack_size", ":num_wounded"),
					(val_add, ":num_total", ":stack_size"),
					(try_begin),
						(lt, ":rank", ":num_total"),
						(assign, reg(0), ":i_stack"),
					(try_end),
				(try_end),
		])

#script_get_nonempty_party_in_group:
		# INPUT:
		# param1: Party-id of the root of the group.
		# OUTPUT: reg0: nonempy party-id
		
get_nonempty_party_in_group = (
	"get_nonempty_party_in_group",
			[
				(store_script_param_1, ":party_no"),
				(party_get_num_companion_stacks, ":num_companion_stacks", ":party_no"),
				(try_begin),
					(gt, ":num_companion_stacks", 0),
					(assign, reg0, ":party_no"),
				(else_try),
					(assign, reg0, -1),
					
					(party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
					(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
						(lt, reg0, 0),
						(party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
						(call_script, "script_get_nonempty_party_in_group", ":attached_party"),
					(try_end),
				(try_end),
		])

	#script_party_count_fit_regulars:
	# Returns the number of unwounded regular companions in a party
	# INPUT:
	# param1: Party-id
		
party_count_fit_regulars = (
	"party_count_fit_regulars",
			[
				(store_script_param_1, ":party"), #Party_id
				(party_get_num_companion_stacks, ":num_stacks", ":party"),
				(assign, reg0, 0),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
					(neg|troop_is_hero, ":stack_troop"),
					(party_stack_get_size, ":stack_size",":party",":i_stack"),
					(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
					(val_sub, ":stack_size", ":num_wounded"),
					(val_add, reg0, ":stack_size"),
				(try_end),
		])
		
		# script_cf_get_random_enemy_center_within_range
		# Input: arg1 = party_no, arg2 = range (in kms)
		# Output: reg0 = center_no
cf_get_random_enemy_center_within_range = (
			"cf_get_random_enemy_center_within_range",
			[
				(store_script_param, ":party_no", 1),
				(store_script_param, ":range", 2),
				
				(assign, ":num_centers", 0),
				(store_faction_of_party, ":faction_no", ":party_no"),
				(try_for_range, ":cur_center", centers_begin, centers_end),
					(store_faction_of_party, ":cur_faction", ":cur_center"),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(lt, ":cur_relation", 0),
					(store_distance_to_party_from_party, ":dist", ":party_no", ":cur_center"),
					(le, ":dist", ":range"),
					(val_add, ":num_centers", 1),
				(try_end),
				(gt, ":num_centers", 0),
				(store_random_in_range, ":random_center", 0, ":num_centers"),
				(assign, ":end_cond", centers_end),
				(try_for_range, ":cur_center", centers_begin, ":end_cond"),
					(store_faction_of_party, ":cur_faction", ":cur_center"),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(lt, ":cur_relation", 0),
					(store_distance_to_party_from_party, ":dist", ":party_no", ":cur_center"),
					(le, ":dist", ":range"),
					(val_sub, ":random_center", 1),
					(lt, ":random_center", 0),
					(assign, ":result", ":cur_center"),
					(assign, ":end_cond", 0),#break
				(try_end),
				(assign, reg0, ":result"),
		])


		# script_get_closest_walled_center
		# Input: arg1 = party_no
		# Output: reg0 = center_no (closest)
get_closest_walled_center = (
			"get_closest_walled_center",
			[
				(store_script_param_1, ":party_no"),
				(assign, ":min_distance", 9999999),
				(assign, reg0, -1),
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
					(lt, ":party_distance", ":min_distance"),
					(assign, ":min_distance", ":party_distance"),
					(assign, reg0, ":center_no"),
				(try_end),
		])
		
		# script_get_closest_center
		# Input: arg1 = party_no
		# Output: reg0 = center_no (closest)
get_closest_center = (
			"get_closest_center",
			[
				(store_script_param_1, ":party_no"),
				(assign, ":min_distance", 9999999),
				(assign, reg0, -1),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
					(lt, ":party_distance", ":min_distance"),
					(assign, ":min_distance", ":party_distance"),
					(assign, reg0, ":center_no"),
				(try_end),
		])

		# script_get_closest_center_of_faction
		# Input: arg1 = party_no, arg2 = kingdom_no
		# Output: reg0 = center_no (closest)
get_closest_center_of_faction = (
			"get_closest_center_of_faction",
			[
				(store_script_param_1, ":party_no"),
				(store_script_param_2, ":kingdom_no"),
				(assign, ":min_distance", 99999),
				(assign, ":result", -1),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_faction_of_party, ":faction_no", ":center_no"),
					(eq, ":faction_no", ":kingdom_no"),
					(store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
					(lt, ":party_distance", ":min_distance"),
					(assign, ":min_distance", ":party_distance"),
					(assign, ":result", ":center_no"),
				(try_end),
				(assign, reg0, ":result"),
		])
		
		# script_get_closest_walled_center_of_faction
		# Input: arg1 = party_no, arg2 = kingdom_no
		# Output: reg0 = center_no (closest)
get_closest_walled_center_of_faction = (
			"get_closest_walled_center_of_faction",
			[
				(store_script_param_1, ":party_no"),
				(store_script_param_2, ":kingdom_no"),
				(assign, ":min_distance", 99999),
				(assign, ":result", -1),
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":faction_no", ":center_no"),
					(eq, ":faction_no", ":kingdom_no"),
					(store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
					(lt, ":party_distance", ":min_distance"),
					(assign, ":min_distance", ":party_distance"),
					(assign, ":result", ":center_no"),
				(try_end),
				(assign, reg0, ":result"),
		])
		
		# script_calculate_battle_advantage
		# Output: reg0 = battle advantage
calculate_battle_advantage = (
	"calculate_battle_advantage",
			[
				(call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
				(assign, ":friend_count", reg(0)),
				
				(party_get_skill_level, ":player_party_tactics",  "p_main_party", skl_tactics),
				(party_get_skill_level, ":ally_party_tactics",  "p_collective_friends", skl_tactics),
				(val_max, ":player_party_tactics", ":ally_party_tactics"),
				
				(call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
				(assign, ":enemy_count", reg(0)),
				
				(party_get_skill_level, ":enemy_party_tactics",  "p_collective_enemy", skl_tactics),
				
				(val_add, ":friend_count", 1),
				(val_add, ":enemy_count", 1),
				
				(try_begin),
					(ge, ":friend_count", ":enemy_count"),
					(val_mul, ":friend_count", 100),
					(store_div, ":ratio", ":friend_count", ":enemy_count"),
					(store_sub, ":raw_advantage", ":ratio", 100),
				(else_try),
					(val_mul, ":enemy_count", 100),
					(store_div, ":ratio", ":enemy_count", ":friend_count"),
					(store_sub, ":raw_advantage", 100, ":ratio"),
				(try_end),
				(val_mul, ":raw_advantage", 2),
				
				(val_mul, ":player_party_tactics", 30),
				(val_mul, ":enemy_party_tactics", 30),
				(val_add, ":raw_advantage", ":player_party_tactics"),
				(val_sub, ":raw_advantage", ":enemy_party_tactics"),
				(val_div, ":raw_advantage", 100),
				
				
				(assign, reg0, ":raw_advantage"),
				(display_message, "@Battle Advantage = {reg0}.", 0xFFFFFFFF),
		])
		
		# script_cf_get_random_enemy_center
		# Input: arg1 = party_no
		# Output: reg0 = center_no
cf_get_random_enemy_center	 = (
	"cf_get_random_enemy_center",
			[
				(store_script_param_1, ":party_no"),
				
				(assign, ":result", -1),
				(assign, ":total_enemy_centers", 0),
				(store_faction_of_party, ":party_faction", ":party_no"),
				
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(store_relation, ":party_relation", ":center_faction", ":party_faction"),
					(lt, ":party_relation", 0),
					(val_add, ":total_enemy_centers", 1),
				(try_end),
				
				(gt, ":total_enemy_centers", 0),
				(store_random_in_range, ":random_center", 0, ":total_enemy_centers"),
				(assign, ":total_enemy_centers", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(eq, ":result", -1),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(store_relation, ":party_relation", ":center_faction", ":party_faction"),
					(lt, ":party_relation", 0),
					(val_sub, ":random_center", 1),
					(lt, ":random_center", 0),
					(assign, ":result", ":center_no"),
				(try_end),
				(assign, reg0, ":result"),
		])
		


		# script_get_relation_between_parties
		# Input: arg1 = party_no_1, arg2 = party_no_2
		# Output: reg0 = relation between parties
get_relation_between_parties	 = (
	"get_relation_between_parties",
			[
				(store_script_param_1, ":party_no_1"),
				(store_script_param_2, ":party_no_2"),
				
				(store_faction_of_party, ":party_no_1_faction", ":party_no_1"),
				(store_faction_of_party, ":party_no_2_faction", ":party_no_2"),
				(try_begin),
					(eq, ":party_no_1_faction", ":party_no_2_faction"),
					(assign, reg0, 100),
				(else_try),
					(store_relation, ":relation", ":party_no_1_faction", ":party_no_2_faction"),
					(assign, reg0, ":relation"),
				(try_end),
		])

		# script_calculate_weekly_party_wage
		# no longer behaves like native
		# WARNING: modified by 1257devs
		# Input: arg1 = party_no
		# Output: reg0 = weekly wage
calculate_weekly_party_wage	 = (
	"calculate_weekly_party_wage",
			[
				(store_script_param_1, ":party_no"),
				
				(assign, ":result", 0),
				(party_get_num_companion_stacks, ":num_stacks",":party_no"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
					(party_stack_get_size, ":stack_size",":party_no",":i_stack"),
					#(call_script, "script_npc_get_troop_wage", ":stack_troop", ":party_no"),
					# rafi
					(call_script, "script_game_get_troop_wage", ":stack_troop", ":party_no"),
					(assign, ":cur_wage", reg0),
					(val_mul, ":cur_wage", ":stack_size"),
					(val_add, ":result", ":cur_wage"),
				(try_end),
				(assign, reg0, ":result"),
		])
		
		# script_calculate_player_faction_wage
		# no longer behaves like native
		# WARNING: modified by 1257devs
		# Input: arg1 = party_no
		# Output: reg0 = weekly wage
calculate_player_faction_wage = (
	"calculate_player_faction_wage",
			[(assign, ":nongarrison_wages", 0),
				(assign, ":garrison_wages", 0),
				(try_for_parties, ":party_no"),
					(assign, ":garrison_troop", 0),
					(try_begin),
						(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
						(party_slot_eq, ":party_no", slot_party_type, spt_castle),
						(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
						(assign, ":garrison_troop", 1),
					(try_end),
					(this_or_next|eq, ":party_no", "p_main_party"),
					(eq, ":garrison_troop", 1),
					(party_get_num_companion_stacks, ":num_stacks",":party_no"),
					(try_for_range, ":i_stack", 0, ":num_stacks"),
						(party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
						(party_stack_get_size, ":stack_size",":party_no",":i_stack"),
						(call_script, "script_game_get_troop_wage", ":stack_troop", ":party_no"),
						(assign, ":cur_wage", reg0),
						(val_mul, ":cur_wage", ":stack_size"),
						(try_begin),
							(eq, ":garrison_troop", 1),
							(val_add, ":garrison_wages", ":cur_wage"),
						(else_try),
							(val_add, ":nongarrison_wages", ":cur_wage"),
						(try_end),
					(try_end),
				(try_end),
				(val_div, ":garrison_wages", 2),#tom was 2#Half payment for garrisons
				(store_sub, ":total_payment", 14, "$g_cur_week_half_daily_wage_payments"), #between 0 and 7
				(val_mul, ":nongarrison_wages", ":total_payment"),
				(val_div, ":nongarrison_wages", 14),
				(store_add, reg0, ":nongarrison_wages", ":garrison_wages"),
		])
		

		# script_print_party_members
		# Input: arg1 = party_no
		# Output: s51 = output string. "noone" if the party is empty
print_party_members = ("print_party_members",
			[
				(store_script_param_1, ":party_no"),
				(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
				(assign, reg10, ":num_stacks"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
					(troop_is_hero, ":stack_troop"),
					(try_begin),
						(eq, ":i_stack", 0),
						(str_store_troop_name, s51, ":stack_troop"),
					(try_end),
					(str_store_troop_name, s52, ":stack_troop"),
					(try_begin),
						(eq, ":i_stack", 1),
						(str_store_string, s51, "str_s52_and_s51"),
					(else_try),
						(gt, ":i_stack", 1),
						(str_store_string, s51, "str_s52_comma_s51"),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":num_stacks", 0),
					(str_store_string, s51, "str_noone"),
				(try_end),
		])