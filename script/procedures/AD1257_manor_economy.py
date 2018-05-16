from header import *
# script_manor_refresh_inventories
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: manor_id
		# Output: none
manor_refresh_inventories = (
	"manor_refresh_inventories",
	[
		(store_script_param, ":manor_id", 1),
		(party_get_slot, ":village", ":manor_id", slot_village_bound_center), 
		#(store_faction_of_party, ":cur_faction", ":manor_id"),
		(party_get_slot, ":cur_faction", ":village", slot_center_original_faction),
		(reset_item_probabilities, 100),
			(set_merchandise_modifier_quality, 150),
		
		###ARMOR
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_armorsmith,manor_building_operational),
			(troop_clear_inventory, "trp_manor_armorsmith"),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_body_armor, 16),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_head_armor, 16),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_foot_armor, 8),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_hand_armor, 4),
		(troop_ensure_inventory_space, "trp_manor_armorsmith", 30),
				(troop_sort_inventory, "trp_manor_armorsmith"),
		## gold
		(store_troop_gold, reg6, "trp_manor_armorsmith"),
		(troop_remove_gold,"trp_manor_armorsmith",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_armorsmith", ":new_gold"),
		(try_end),
		###ARMOR END
		###WEAPONS
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_weaponsmith,manor_building_operational),
		(troop_clear_inventory, "trp_manor_weaponsmith"),
			(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_one_handed_wpn, 5),
				(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_two_handed_wpn, 5),
				(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_polearm, 5),
				(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_shield, 6),
				(troop_ensure_inventory_space, "trp_manor_weaponsmith", 30),
				(troop_sort_inventory, "trp_manor_weaponsmith"),
		##gold
		(store_troop_gold, reg6, "trp_manor_weaponsmith"),
		(troop_remove_gold,"trp_manor_weaponsmith",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_weaponsmith", ":new_gold"),
			(try_end),
		###WEAPON END
		###FLETCHER
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_fletcher,manor_building_operational),
		(troop_clear_inventory, "trp_manor_fletcher"),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_bow, 4),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_crossbow, 3),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_thrown, 5),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_arrows, 2),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_bolts, 2),
				(troop_ensure_inventory_space, "trp_manor_fletcher", 30),
				(troop_sort_inventory, "trp_manor_fletcher"),
		##gold
		(store_troop_gold, reg6, "trp_manor_fletcher"),
		(troop_remove_gold,"trp_manor_fletcher",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_fletcher", ":new_gold"),
		(try_end),
		###FLETCHER END
		###STABLE
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_breeder,manor_building_operational),
		(troop_clear_inventory, "trp_manor_breeder"),
		(troop_add_merchandise_with_faction, "trp_manor_breeder", ":cur_faction", itp_type_horse, 20),
		(troop_ensure_inventory_space, "trp_manor_breeder", 30),
				(troop_sort_inventory, "trp_manor_breeder"),
		##gold
		(store_troop_gold, reg6, "trp_manor_breeder"),
		(troop_remove_gold,"trp_manor_breeder",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_breeder", ":new_gold"),
		(try_end),
		###STABLE END
		###OTHER CRAPERS
		(try_for_range, ":cur_merchant", trp_manor_grain, trp_manor_tanner+1),
			(troop_get_slot, ":goods", ":cur_merchant", manor_troop_slot_good),
		(troop_clear_inventory, ":cur_merchant"),
		(store_random_in_range, ":good_amount", 2, 5),
		(troop_add_items,":cur_merchant",":goods",":good_amount"),
		(troop_ensure_inventory_space, ":cur_merchant", 20),
		(troop_sort_inventory, ":cur_merchant"),
		## gold
			(store_troop_gold, reg6, ":cur_merchant"),
		(troop_remove_gold,":cur_merchant",reg6),
		(store_random_in_range, ":new_gold", 150, 300),
				(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end),
		###OTHER CRAPERS END
	])	