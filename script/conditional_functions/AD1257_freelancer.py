from header import *

#script_cf_freelancer_player_can_upgrade
	 #Reg0 outputs reason for failure
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: source_troop
	# OUTPUT: none
cf_freelancer_player_can_upgrade = (
	"cf_freelancer_player_can_upgrade",
	 #Reg0 outputs reason for failure
	 [
	(store_script_param_1, ":source_troop"),
	
	(troop_get_inventory_capacity, ":troop_cap", ":source_troop"),	
	(assign, ":continue", 1),
	
	(assign, ":type_available", 0),
	(assign, ":type_count", 0),
	(assign, ":end", itp_type_arrows),
	(try_for_range, ":type", itp_type_one_handed_wpn, ":end"),
		#Count Items from Source Troop
		(assign, ":end2", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end2"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":item_type", ":item"),
			(eq, ":item_type", ":type"),
			(val_add, ":type_count", 1),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),		
			(assign, ":type_available", 1),
			(assign, ":end2", 0), #break
		(try_end),
		(eq, ":type_available", 1),
		(assign, ":end", itp_type_one_handed_wpn), #break
	(try_end), #Melee loop
	(try_begin),
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 0),
	(try_end),
	(eq, ":continue", 1),
	
	(assign, ":type_available", 0),
	(assign, ":type_count", 0),
	(assign, ":end2", ":troop_cap"),
	(try_for_range, ":inv_slot", 0, ":end2"),
		(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
		(gt, ":item", 0),
		(item_get_type, ":item_type", ":item"),
		(eq, ":item_type", itp_type_body_armor),
		(val_add, ":type_count", 1),
		(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
		(eq, reg0, 1),		
		(assign, ":type_available", 1),
		(assign, ":end2", 0), #break
	(try_end),
	(try_begin),
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 1),
	(try_end),
	(eq, ":continue", 1),
	
	(try_begin),
		(troop_is_guarantee_ranged, ":source_troop"),
		(assign, ":type_available", 0),
		(assign, ":type_count", 0),
		(assign, ":end", itp_type_goods),
		(try_for_range, ":type", itp_type_bow, ":end"),
			#Count Items from Source Troop
			(assign, ":end2", ":troop_cap"),
			(try_for_range, ":inv_slot", 0, ":end2"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
				(gt, ":item", 0),
				(item_get_type, ":item_type", ":item"),
				(eq, ":item_type", ":type"),
				(val_add, ":type_count", 1),
				(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
				(eq, reg0, 1),		
				(assign, ":type_available", 1),
				(assign, ":end2", 0), #break
			(try_end),
			(eq, ":type_available", 1),
			(assign, ":end", itp_type_bow), #break
		(try_end), #Ranged loop
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 2), 
	(try_end),
	(eq, ":continue", 1),
	
	(try_begin),
		(troop_is_guarantee_horse, ":source_troop"),
		(assign, ":type_available", 0),
		(assign, ":type_count", 0),
		(assign, ":end2", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end2"),
			(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":item_type", ":item"),
			(eq, ":item_type", itp_type_horse),
			(val_add, ":type_count", 1),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),		
			(assign, ":type_available", 1),
			(assign, ":end2", 0), #break
		(try_end),
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 3),
	(try_end),
	(eq, ":continue", 1),	
	 ])