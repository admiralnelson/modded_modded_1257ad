from header import *

#script_copy_upgrade_to_all_heroes
	# Copy this troop's upgrade options to everyone
	# INPUT	: troop, type
	# OUTPUT : none
copy_upgrade_to_all_heroes = (
	"copy_upgrade_to_all_heroes",
		[
		(store_script_param_1, ":troop"),
		(store_script_param_2, ":type"),
		
		(try_begin),
			(eq, ":type", wpn_setting_1),
			(troop_get_slot,":upg_wpn0", ":troop",slot_upgrade_wpn_0),
			(troop_get_slot,":upg_wpn1", ":troop",slot_upgrade_wpn_1),
			(troop_get_slot,":upg_wpn2", ":troop",slot_upgrade_wpn_2),
			(troop_get_slot,":upg_wpn3", ":troop",slot_upgrade_wpn_3),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_wpn_0,":upg_wpn0"),
			(troop_set_slot,":hero",slot_upgrade_wpn_1,":upg_wpn1"),
			(troop_set_slot,":hero",slot_upgrade_wpn_2,":upg_wpn2"),
			(troop_set_slot,":hero",slot_upgrade_wpn_3,":upg_wpn3"),
			(try_end),
		(else_try),
			(eq, ":type", wpn_setting_2),
			(troop_get_slot,":upg_wpn0", ":troop",slot_upgrade_wpn_0_set_2),
			(troop_get_slot,":upg_wpn1", ":troop",slot_upgrade_wpn_1_set_2),
			(troop_get_slot,":upg_wpn2", ":troop",slot_upgrade_wpn_2_set_2),
			(troop_get_slot,":upg_wpn3", ":troop",slot_upgrade_wpn_3_set_2),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_wpn_0_set_2,":upg_wpn0"),
			(troop_set_slot,":hero",slot_upgrade_wpn_1_set_2,":upg_wpn1"),
			(troop_set_slot,":hero",slot_upgrade_wpn_2_set_2,":upg_wpn2"),
			(troop_set_slot,":hero",slot_upgrade_wpn_3_set_2,":upg_wpn3"),
			(try_end),
		(else_try),
			(eq, ":type", armor_setting),
			(troop_get_slot,":upg_armor", ":troop",slot_upgrade_armor),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_armor,":upg_armor"),
			(try_end),
		(else_try),
			(eq, ":type", horse_setting),
			(troop_get_slot,":upg_horse", ":troop",slot_upgrade_horse),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_horse,":upg_horse"),
			(try_end),
		(try_end),
	])

	#script_auto_loot_all
	# Let each hero loot from the pool
	# WARNING: some part of this script are disabled.
	# INPUT	: none
	# OUTPUT : none
auto_loot_all = (
	"auto_loot_all",
		[
		# once more to pick up any discards
		(try_for_range, ":unused", 0, 2),
			(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
			(is_between, ":this_hero", companions_begin, companions_end),
			(call_script, "script_auto_loot_troop", ":this_hero", "$pool_troop"),
			# # switch to another set
			# (troop_get_slot, ":wpn_set_sel", ":this_hero", slot_upgrade_wpn_set_sel),
			# (val_add, ":wpn_set_sel", 1),
			# (val_mod, ":wpn_set_sel", 2),
			# (troop_set_slot, ":this_hero", slot_upgrade_wpn_set_sel, ":wpn_set_sel"),
			# (call_script, "script_exchange_equipments_between_two_sets", ":this_hero"),
			# # auto_loot once more
			# (call_script, "script_auto_loot_troop", ":this_hero", "$pool_troop"),
			# # switch back
			# (troop_get_slot, ":wpn_set_sel", ":this_hero", slot_upgrade_wpn_set_sel),
			# (val_add, ":wpn_set_sel", 1),
			# (val_mod, ":wpn_set_sel", 2),
			# (troop_set_slot, ":this_hero", slot_upgrade_wpn_set_sel, ":wpn_set_sel"),
			# (call_script, "script_exchange_equipments_between_two_sets", ":this_hero"),
			(try_end),
		(try_end),
		#Done. Now sort the remainder
		(troop_sort_inventory, "$pool_troop"),
	])


	#script_auto_loot_troop
	# let this troop take its pick from the loot pool
	# WARNING: some part of this script are disabled.	
	# TAGS: Custom Commander(CC)
	# INPUT	: troop, pool
	# OUTPUT : NONE
auto_loot_troop = (
	"auto_loot_troop",
		[
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		
		
		(troop_get_slot,":upg_armor", ":troop",slot_upgrade_armor),
		(troop_get_slot,":upg_horses",":troop",slot_upgrade_horse),
		
		## CC
		(troop_get_slot,":upgrade_wpn_set_sel", ":troop", slot_upgrade_wpn_set_sel),
		(store_mul, ":offset", ":upgrade_wpn_set_sel", offset_of_two_sets_slot),
		(store_add, ":slot_upgrade_wpn_0", slot_upgrade_wpn_0, ":offset"),
		(store_add, ":slot_upgrade_wpn_1", slot_upgrade_wpn_1, ":offset"),
		(store_add, ":slot_upgrade_wpn_2", slot_upgrade_wpn_2, ":offset"),
		(store_add, ":slot_upgrade_wpn_3", slot_upgrade_wpn_3, ":offset"),
		## CC
		
		# dump whatever rubbish is in the main inventory
		## CC
		(call_script, "script_transfer_inventory", ":troop", ":pool", 0),
		## CC
		
		# dispose of the troop's equipped items if necessary
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_0", 1),
			(troop_get_inventory_slot, ":item", ":troop", 0),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 0),
			(troop_set_inventory_slot, ":troop", 0, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_1", 1),
			(troop_get_inventory_slot, ":item", ":troop", 1),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 1),
			(troop_set_inventory_slot, ":troop", 1, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_2", 1),
			(troop_get_inventory_slot, ":item", ":troop", 2),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 2),
			(troop_set_inventory_slot, ":troop", 2, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_3", 1),
			(troop_get_inventory_slot, ":item", ":troop", 3),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 3),
			(troop_set_inventory_slot, ":troop", 3, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_for_range, ":i_slot", 4, 9),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
			(item_get_type, ":i_type", ":item"),
			(try_begin),
			(this_or_next|eq, ":i_type", itp_type_head_armor),
			(this_or_next|eq, ":i_type", itp_type_body_armor),
			(this_or_next|eq, ":i_type", itp_type_foot_armor),
			(eq, ":i_type", itp_type_hand_armor),
			(neq, ":upg_armor", 0), # we're uprgrading armors
			(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(else_try),
			(eq, ":i_type", itp_type_horse),
			(neq, ":upg_horses", 0), # we're uprgrading horses
			(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(try_end),
		(try_end),
		
		# clear best matches
		(assign, ":best_helmet_slot", -1),
		(assign, ":best_helmet_val", 0),
		(assign, ":best_body_slot", -1),
		(assign, ":best_body_val", 0),
		(assign, ":best_boots_slot", -1),
		(assign, ":best_boots_val", 0),
		(assign, ":best_gloves_slot", -1),
		(assign, ":best_gloves_val", 0),
		(assign, ":best_horse_slot", -1),
		(assign, ":best_horse_val", 0),
		#(assign, ":best_book_slot", -1),
		#(assign, ":best_book_val", 0),
		
		# Now search through the pool for the best items
		(troop_get_inventory_capacity, ":inv_cap", ":pool"),
		(try_for_range, ":i_slot", 0, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":pool", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":i_slot"),
			(call_script, "script_troop_can_use_item", ":troop", ":item", ":imod"),
			(eq, reg0, 1), # can use
			(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
			(assign, ":score", reg0),
			
			(item_get_type, ":item_type", ":item"),
			
			(try_begin),
			(eq, ":item_type", itp_type_horse), #it's a horse
			(eq, ":upg_horses", 1), # we're uprgrading horses
			(gt, ":score", ":best_horse_val"),
			(assign, ":best_horse_slot", ":i_slot"),
			(assign, ":best_horse_val", ":score"),
			(else_try),
			(try_begin),
				(eq, ":item_type", itp_type_head_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_helmet_val"),
				(assign, ":best_helmet_slot", ":i_slot"),
				(assign, ":best_helmet_val", ":score"),
			(else_try),
				(eq, ":item_type", itp_type_body_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_body_val"),
				(assign, ":best_body_slot", ":i_slot"),
				(assign, ":best_body_val", ":score"),
			(else_try),
				(eq, ":item_type", itp_type_foot_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_boots_val"),
				(assign, ":best_boots_slot", ":i_slot"),
				(assign, ":best_boots_val", ":score"),
			(else_try),
				(eq, ":item_type", itp_type_hand_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_gloves_val"),
				(assign, ":best_gloves_slot", ":i_slot"),
				(assign, ":best_gloves_val", ":score"),
			(try_end),
			(try_end),
		(try_end),
		# Now we know which ones are the best. Give them to the troop.
		(try_begin),
			(assign, ":best_slot", ":best_helmet_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":head_item", ":troop", ek_head),
			(eq, ":head_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_head, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_head, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_body_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":body_item", ":troop", ek_body),
			(eq, ":body_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_body, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_body, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_boots_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":foot_item", ":troop", ek_foot),
			(eq, ":foot_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_foot, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_foot, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_gloves_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":gloves_item", ":troop", ek_gloves),
			(eq, ":gloves_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_gloves, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_gloves, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_horse_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":horse_item", ":troop", ek_horse),
			(eq, ":horse_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_horse, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_horse, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		# (try_begin),
		# (assign, ":best_slot", ":best_book_slot"),
		# (ge, ":best_slot", 0),
		# (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
		# (ge, ":item", 0),
		# (store_free_inventory_capacity, ":troop_inv_cap", ":troop"),
		# (gt, ":troop_inv_cap", 0),
		# (troop_slot_eq, ":troop", slot_troop_current_reading_book, 0),
		# (troop_add_item, ":troop", ":item"),
		# (troop_set_slot, ":troop", slot_troop_current_reading_book, ":item"),
		# (troop_set_inventory_slot, ":pool", ":best_slot", -1),
		# (try_end),
		
		(try_for_range, ":i_slot", 0, 4),
			(store_add, ":trp_slot", ":i_slot", ":slot_upgrade_wpn_0"),
			(troop_get_slot, ":type", ":troop", ":trp_slot"),
			(gt, ":type", 0), #we're upgrading for this slot
			(call_script, "script_scan_for_best_item_of_type", ":pool", ":type", ":troop"), #search for the best
			(assign, ":best_slot", reg0),
			(neq, ":best_slot", -1), #got something
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"), #get it
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":wpn_item", ":troop", ":i_slot"),
			(eq, ":wpn_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1), #remove from pool
			(troop_set_inventory_slot, ":troop", ":i_slot", ":item"), #add to slot
			(troop_set_inventory_slot_modifier, ":troop", ":i_slot", ":imod"),
		(try_end),
	])
	
	# script_exchange_equipments_between_two_sets
	# Input: none
	# Output: none
exchange_equipments_between_two_sets = (
	"exchange_equipments_between_two_sets",
		[
		(store_script_param, ":troop_no", 1),
		
		(try_for_range, ":cur_slot", 0, 4),
			(store_sub, ":dest_slot", ":troop_no", companions_begin),
			(val_mul, ":dest_slot", 4),
			(val_add, ":dest_slot", 10),
			(val_add, ":dest_slot", ":cur_slot"),
			
			(str_store_troop_name, s20, ":troop_no"),
			(assign, reg20, ":dest_slot"),
			(display_message, "@{s20} --- dest slot {reg20}"),
			
			(troop_get_inventory_slot, ":dest_item", "trp_merchants_end", ":dest_slot"),
			(troop_get_inventory_slot_modifier, ":dest_imod", "trp_merchants_end", ":dest_slot"),
			(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_slot"),
			(troop_get_inventory_slot_modifier, ":cur_imod", ":troop_no", ":cur_slot"),
			(troop_set_inventory_slot, "trp_merchants_end", ":dest_slot", ":cur_item"),
			(troop_set_inventory_slot_modifier, "trp_merchants_end", ":dest_slot", ":cur_imod"),
			(troop_set_inventory_slot, ":troop_no", ":cur_slot", ":dest_item"),
			(troop_set_inventory_slot_modifier, ":troop_no", ":cur_slot", ":dest_imod"),
		(try_end),
	])
	
	# script_transfer_inventory
	# INPUT	: source, dest, trans_book
	# OUTPUT : none
transfer_inventory = (
	"transfer_inventory", [
		(store_script_param, ":source", 1),
		(store_script_param, ":dest", 2),
		(store_script_param, ":trans_book", 3),
		
		(store_free_inventory_capacity, ":space", ":dest"),
		(troop_sort_inventory, ":source"),
		
		(troop_get_inventory_capacity, ":inv_cap", ":source"),
		(try_for_range, ":i_slot", 10, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":source", ":i_slot"),
			(troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
			(gt, ":item", -1),
			
			(assign, ":continue", 1),
			(try_begin),
			(eq, ":trans_book", 0),
			(is_between, ":item", reference_books_begin, reference_books_end),
			(assign, ":continue", 0),
			(try_end),
			(eq, ":continue", 1),
			
			(gt, ":space", 0),
			(troop_add_item, ":dest", ":item", ":imod"),
			(val_sub, ":space", 1),
			(try_begin),
			(is_between, ":item", trade_goods_begin, trade_goods_end),
			(troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
			(troop_get_inventory_capacity, ":dest_inv_cap", ":dest"),
			(store_sub, ":dest_slot", ":dest_inv_cap", ":space"),
			(troop_inventory_slot_set_item_amount, ":dest", ":dest_slot", ":amount"),
			(try_end),
			(troop_set_inventory_slot, ":source", ":i_slot", -1),
		(try_end),
	])
	
	# script_transfer_special_inventory
	# INPUT	: source, dest
	# OUTPUT : none
transfer_special_inventory = (
	"transfer_special_inventory", [
		(store_script_param, ":source", 1),
		(store_script_param, ":dest", 2),
		
		(store_free_inventory_capacity, ":space", ":dest"),
		(troop_sort_inventory, ":source"),
		
		(troop_get_inventory_capacity, ":inv_cap", ":source"),
		(try_for_range, ":i_slot", 10, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":source", ":i_slot"),
			(troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
			(gt, ":item", -1),
			
			(assign, ":continue", 0),
			(try_begin),
			(call_script, "script_get_item_value_with_imod", ":item", ":imod"),
			(assign, ":item_value", reg0),
			(val_div, ":item_value", 100),
			(ge, ":item_value", "$g_price_threshold_for_picking"),
			(assign, ":continue", 1),
			(else_try),
			(item_get_type, ":item_type", ":item"),
			(this_or_next|eq, ":item_type", itp_type_goods),
			(this_or_next|eq, ":item_type", itp_type_animal),
			(eq, ":item_type", itp_type_book),
			(assign, ":continue", 1),
			(try_end),
			(eq, ":continue", 1),
			
			(gt, ":space", 0),
			(troop_add_item, ":dest", ":item", ":imod"),
			(val_sub, ":space", 1),
			(try_begin),
			(is_between, ":item", trade_goods_begin, trade_goods_end),
			(troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
			(troop_get_inventory_capacity, ":dest_inv_cap", ":dest"),
			(store_sub, ":dest_slot", ":dest_inv_cap", ":space"),
			(troop_inventory_slot_set_item_amount, ":dest", ":dest_slot", ":amount"),
			(try_end),
			(troop_set_inventory_slot, ":source", ":i_slot", -1),
		(try_end),
	])