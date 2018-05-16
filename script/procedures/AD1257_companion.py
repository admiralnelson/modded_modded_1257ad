from header import *

##script_equip_companion - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: companion, troop
	##output: none
	##description: Sets the equipment of the hero character to the specified troop
equip_companion =	(
	"equip_companion",
		[
		(store_script_param, ":companion", 1),
		(store_script_param, ":troop_id", 2),
		
		(assign, ":main_weapon", 0),
		(assign, ":side_weapon", 25),
		(assign, ":shield", 50),
		(assign, ":two_handed", 75),
		(assign, ":javelin", 100),
		(assign, ":bolts", 125),
		(assign, ":arrows", 150),
		(assign, ":bow", 175),
		(assign, ":crossbow", 200),
		(assign, ":head", 225),
		(assign, ":body", 250),
		(assign, ":foot", 275),
		(assign, ":hand", 300),
		(assign, ":horse", 325),
		
		(assign, ":equip_main", 0),
		(assign, ":equip_side", 0),
		(assign, ":equip_shield", 0),
		(assign, ":equip_two_handed", 0),
		(assign, ":equip_javelin", 0),
		(assign, ":equip_bolts", 0),
		(assign, ":equip_arrows", 0),
		(assign, ":equip_bow", 0),
		(assign, ":equip_crossbow", 0),
		(assign, ":equip_head", 0),
		(assign, ":equip_body", 0),
		(assign, ":equip_foot", 0),
		(assign, ":equip_hand", 0),
		(assign, ":equip_horse", 0),
		
		(troop_clear_inventory, ":companion"),
		(troop_get_inventory_capacity, ":capacity", ":troop_id"),
		(try_for_range, ":cur_slot", 0, ":capacity"),
			(troop_get_inventory_slot, ":cur_item", ":troop_id", ":cur_slot"),
			(gt, ":cur_item", 0),
			(item_get_type, ":type", ":cur_item"),
			(try_begin),
			(eq, ":type", itp_type_polearm),
			(val_add, ":main_weapon", 1),
			(troop_set_slot, "trp_items_array", 0, ":main_weapon"),
			(troop_set_slot, "trp_items_array", ":main_weapon", ":cur_item"),
			(assign, ":equip_main", 1),
			(else_try),	
			(eq, ":type", itp_type_one_handed_wpn),
			(val_add, ":side_weapon", 1),
			(troop_set_slot, "trp_items_array", 25, ":side_weapon"),
			(troop_set_slot, "trp_items_array", ":side_weapon", ":cur_item"),	
			(assign, ":equip_side", 1),
			(else_try),	
			(eq, ":type", itp_type_shield),
			(val_add, ":shield", 1),
			(troop_set_slot, "trp_items_array", 50, ":shield"),
			(troop_set_slot, "trp_items_array", ":shield", ":cur_item"),
			(assign, ":equip_shield", 1),	
			(else_try),	
			(eq, ":type", itp_type_two_handed_wpn),
			(val_add, ":two_handed", 1),
			(troop_set_slot, "trp_items_array", 75, ":two_handed"),
			(troop_set_slot, "trp_items_array", ":two_handed", ":cur_item"),
			(assign, ":equip_two_handed", 1),
			(else_try),	
			(eq, ":type", itp_type_thrown),
			(val_add, ":javelin", 1),
			(troop_set_slot, "trp_items_array", 100, ":javelin"),
			(troop_set_slot, "trp_items_array", ":javelin", ":cur_item"),
			(assign, ":equip_javelin", 1),
			(else_try),	
			(eq, ":type", itp_type_bolts),
			(val_add, ":bolts", 1),
			(troop_set_slot, "trp_items_array", 125, ":bolts"),
			(troop_set_slot, "trp_items_array", ":bolts", ":cur_item"),
			(assign, ":equip_bolts", 1),
			(else_try),	
			(eq, ":type", itp_type_arrows),
			(val_add, ":arrows", 1),
			(troop_set_slot, "trp_items_array", 150, ":arrows"),
			(troop_set_slot, "trp_items_array", ":arrows", ":cur_item"),
			(assign, ":equip_arrows", 1),
			(else_try),	
			(eq, ":type", itp_type_bow),
			(val_add, ":bow", 1),
			(troop_set_slot, "trp_items_array", 175, ":bow"),
			(troop_set_slot, "trp_items_array", ":bow", ":cur_item"),
			(assign, ":equip_bow", 1),
			(else_try),	
			(eq, ":type", itp_type_crossbow),
			(val_add, ":crossbow", 1),
			(troop_set_slot, "trp_items_array", 200, ":crossbow"),
			(troop_set_slot, "trp_items_array", ":crossbow", ":cur_item"),
			(assign, ":equip_crossbow", 1),
			(else_try),	
			(eq, ":type", itp_type_head_armor),
			(val_add, ":head", 1),
			(troop_set_slot, "trp_items_array", 225, ":head"),
			(troop_set_slot, "trp_items_array", ":head", ":cur_item"),
			(assign, ":equip_head", 1),
			(else_try),	
			(eq, ":type", itp_type_body_armor),
			(val_add, ":body", 1),
			(troop_set_slot, "trp_items_array", 250, ":body"),
			(troop_set_slot, "trp_items_array", ":body", ":cur_item"),
			(assign, ":equip_body", 1),	
			(else_try),	
			(eq, ":type", itp_type_foot_armor),
			(val_add, ":foot", 1),
			(troop_set_slot, "trp_items_array", 275, ":foot"),
			(troop_set_slot, "trp_items_array", ":foot", ":cur_item"),
			(assign, ":equip_foot", 1),	
			(else_try),	
			(eq, ":type", itp_type_hand_armor),
			(val_add, ":hand", 1),
			(troop_set_slot, "trp_items_array", 300, ":hand"),
			(troop_set_slot, "trp_items_array", ":hand", ":cur_item"),
			(assign, ":equip_hand", 1),	
			(else_try),	
			(eq, ":type", itp_type_horse),
			(val_add, ":horse", 1),
			(troop_set_slot, "trp_items_array", 325, ":horse"),
			(troop_set_slot, "trp_items_array", ":horse", ":cur_item"),
			(assign, ":equip_horse", 1),	
			(try_end),
		(try_end),
		
		(try_begin),
			(eq, ":equip_main", 1),
			(troop_get_slot, ":amount", "trp_items_array", 0),
			(store_random_in_range, ":slot", 1, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_side", 1),
			(troop_get_slot, ":amount", "trp_items_array", 25),
			(store_random_in_range, ":slot", 26, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_shield", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 50),
			(store_random_in_range, ":slot", 51, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_two_handed", 1),	
			(try_begin),
			(eq, ":equip_side", 1),	#if have and side arm
			(store_random_in_range, ":random", 0, 100),
			(lt, ":random", 65), #small chance for getting a sidearm as well
			(else_try),
			(troop_get_slot, ":amount", "trp_items_array", 75),
			(store_random_in_range, ":slot", 76, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
			(try_end),
		(try_end),
		(try_begin),
			(eq, ":equip_javelin", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 100),
			(store_random_in_range, ":slot", 101, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_bolts", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 125),
			(store_random_in_range, ":slot", 126, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_arrows", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 150),
			(store_random_in_range, ":slot", 151, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_bow", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 175),
			(store_random_in_range, ":slot", 176, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_crossbow", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 200),
			(store_random_in_range, ":slot", 201, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_head", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 225),
			(store_random_in_range, ":slot", 256, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_body", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 250),
			(store_random_in_range, ":slot", 251, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_foot", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 275),
			(store_random_in_range, ":slot", 276, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_hand", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 300),
			(store_random_in_range, ":slot", 301, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_horse", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 325),
			(store_random_in_range, ":slot", 326, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(neq, "trp_player", ":companion"),
			(troop_equip_items, ":companion"),
			(troop_clear_inventory, ":companion"),
			(troop_set_auto_equip, ":companion", 0),
		(try_end),
		])