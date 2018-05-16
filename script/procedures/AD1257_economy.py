from header import *
#script_tom_process_player_enterprise
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: enterprise_product, enterprise_center, future_cost
		#OUTPUT: none
tom_process_player_enterprise =	(
	"tom_process_player_enterprise",
			[
			(store_script_param, ":enterprise_product", 1),
			(store_script_param, ":enterprise_center", 2),
			(store_script_param, ":future_cost", 3),
			
			(assign, ":enterprise_penalty", ":future_cost"),
			
			(try_for_range, ":center_no", centers_begin, centers_end),
				(party_get_slot, ":item_produced", ":center_no", slot_center_player_enterprise),
				(eq, ":item_produced", ":enterprise_product"),
				(val_add, ":enterprise_penalty", 1),
			(try_end),
			
			#(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			(try_begin),
				(eq, "$tom_difficulty_enterprise", 0), #hard (1x or 2x reinforcing)
				(assign, ":precent", 25),
			(else_try),
				(eq, "$tom_difficulty_enterprise", 1), #moderate (1x reinforcing)
				(assign, ":precent", 20),
			(else_try),
				(eq, "$tom_difficulty_enterprise", 2), #easy (none or 1x reinforcing)
				(assign, ":precent", 15),
			(try_end),
			
			#reduce the penalty with trade skill
			(store_skill_level, ":cur_trade", "skl_trade", "trp_player"),
			(val_sub, ":precent", ":cur_trade"),
			
			(call_script, "script_process_player_enterprise", ":enterprise_product", ":enterprise_center"),
			(assign, ":penalty_total", 0),
			(assign, ":penalty", reg0),
			(try_for_range, reg1, 0, ":enterprise_penalty"),
				(store_sub, ":penalty", reg0, ":penalty_total"),
				(val_mul, ":penalty", ":precent"),
				(val_div, ":penalty", 100),
				(val_abs, ":penalty"),
				(val_add, ":penalty_total", ":penalty"),
			(try_end),
			
			(val_sub, reg0, ":penalty_total"),
			])

			# script_refresh_center_inventories
# WARNING: this is totally new procedure (not present in native). 1257AD devs
# INPUT: source_troop
# OUTPUT: none
refresh_center_inventories = (
	"refresh_center_inventories",
	[   	
		(set_merchandise_modifier_quality,150),
		(reset_item_probabilities,100),	    

		# Add trade goods to merchant inventories
		(try_for_range,":cur_center",towns_begin, towns_end),
			(party_get_slot,":cur_merchant",":cur_center",slot_town_merchant),
			(reset_item_probabilities,100),
			(assign, ":total_production", 0),
			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
				(call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
		(assign, ":cur_production", reg0),

				(try_for_range, ":cur_village", villages_begin, villages_end),
			(party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
					(call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
			(val_div, reg0, 3),
			(val_add, ":cur_production", reg0),
		(try_end),		

		(val_max, ":cur_production", 1),
		(val_mul, ":cur_production", 4),

		(val_add, ":total_production", ":cur_production"),
			(try_end),

		(party_get_slot, ":town_prosperity", ":cur_center", slot_town_prosperity),
		(assign, ":number_of_items_in_town", 25),

		(try_begin), #1.0x - 2.0x (50 - 100 prosperity)
			(ge, ":town_prosperity", 50),
		(store_sub, ":ratio", ":town_prosperity", 50),
		(val_mul, ":ratio", 2),
		(val_add, ":ratio", 100),
		(val_mul, ":number_of_items_in_town", ":ratio"),
		(val_div, ":number_of_items_in_town", 100),
		(else_try), #0.5x - 1.0x (0 - 50 prosperity)
		(store_sub, ":ratio", ":town_prosperity", 50),
		(val_add, ":ratio", 100),
		(val_mul, ":number_of_items_in_town", ":ratio"),
		(val_div, ":number_of_items_in_town", 100),
		(try_end),

		(val_clamp, ":number_of_items_in_town", 10, 40),	

		(try_begin),
			(is_between, ":cur_center", castles_begin, castles_end),
			(val_div, ":number_of_items_in_town", 2),
			(try_end),

			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
				(call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
		(assign, ":cur_production", reg0),

				(try_for_range, ":cur_village", villages_begin, villages_end),
			(party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
					(call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
			(val_div, reg0, 3),
			(val_add, ":cur_production", reg0),
		(try_end),		

		(val_max, ":cur_production", 1),
		(val_mul, ":cur_production", 4),

				(val_mul, ":cur_production", ":number_of_items_in_town"),
		(val_mul, ":cur_production", 100),
		(val_div, ":cur_production", ":total_production"),
				(set_item_probability_in_merchandise, ":cur_goods", ":cur_production"),						  
			(try_end),

		(troop_clear_inventory, ":cur_merchant"),
			(troop_add_merchandise, ":cur_merchant", itp_type_goods, ":number_of_items_in_town"),

			(troop_ensure_inventory_space, ":cur_merchant", 20),
			(troop_sort_inventory, ":cur_merchant"),
			(store_troop_gold, ":cur_gold",":cur_merchant"),
			(lt,":cur_gold",1500),
			(store_random_in_range,":new_gold",500,1000),
			(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end), 	
	]) 

	# script_refresh_center_armories
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
refresh_center_armories = (
	"refresh_center_armories",
	[
		(reset_item_probabilities, 100),
	(set_merchandise_modifier_quality, 150),    
	(try_for_range, ":cur_merchant", armor_merchants_begin, armor_merchants_end),    
		(store_sub, ":cur_town", ":cur_merchant", armor_merchants_begin),
		(val_add, ":cur_town", towns_begin),
		(troop_clear_inventory, ":cur_merchant"),
		(party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
		#tom
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 16),
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 16),
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_foot_armor, 8),
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_hand_armor, 4),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 2),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 2),
		(faction_get_slot, ":culture", ":cur_faction", slot_faction_culture),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_body_armor, 16),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_head_armor, 16),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_foot_armor, 8),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_hand_armor, 4),
		#tom
		(troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
		(troop_sort_inventory, ":cur_merchant"),
		(store_troop_gold, reg6, ":cur_merchant"),
		(lt, reg6, 1000),
		(store_random_in_range, ":new_gold", 250, 500),
		(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(end_try),
	])

	# script_refresh_center_weaponsmiths
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
refresh_center_weaponsmiths = (
	"refresh_center_weaponsmiths",
	[
		(reset_item_probabilities, 100),
		(set_merchandise_modifier_quality, 150),
		(try_for_range, ":cur_merchant", weapon_merchants_begin, weapon_merchants_end),
		(store_sub, ":cur_town", ":cur_merchant", weapon_merchants_begin),
			(val_add, ":cur_town", towns_begin), 
		(troop_clear_inventory, ":cur_merchant"),
			(party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
		#tom
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 6),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 4),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 3),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_arrows, 2),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bolts, 2),	  
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 1),
		(faction_get_slot, ":culture", ":cur_faction", slot_faction_culture),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_one_handed_wpn, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_two_handed_wpn, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_polearm, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_shield, 6),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_bow, 4),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_crossbow, 3),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_thrown, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_arrows, 2),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_bolts, 2),	  
		#tom
			(troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
			(troop_sort_inventory, ":cur_merchant"), 
			(store_troop_gold, reg6, ":cur_merchant"),
			(lt, reg6, 1000),
			(store_random_in_range, ":new_gold", 250, 500),
			(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end),
	])

# script_refresh_center_stables
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
refresh_center_stables = (
	"refresh_center_stables",
	[
		(reset_item_probabilities, 100),
		(set_merchandise_modifier_quality, 150),
		(try_for_range, ":cur_merchant", horse_merchants_begin, horse_merchants_end),
		(troop_clear_inventory, ":cur_merchant"),
			(store_sub, ":cur_town", ":cur_merchant", horse_merchants_begin),
			(val_add, ":cur_town", towns_begin),
			(party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
		#tom
			#(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 20),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 2),
		(faction_get_slot, ":culture", ":cur_faction", slot_faction_culture),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_horse, 20),
		#tom
			(troop_ensure_inventory_space, ":cur_merchant", 65),
			(troop_sort_inventory, ":cur_merchant"),
			(store_troop_gold, ":cur_gold", ":cur_merchant"),
			(lt, ":cur_gold", 600),
			(store_random_in_range, ":new_gold", 250, 500),
			(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end),
	])
	