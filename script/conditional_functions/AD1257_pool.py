from header import *

##script_cf_add_troop_items_armor
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: troop, pool, armor_from, armor_to
	# OUTPUT: nothing (can fail)
cf_add_troop_items_armor = (
	"cf_add_troop_items_armor",
	[
		(store_script_param, ":troop", 1),
			(store_script_param, ":pool", 2),
			(store_script_param, ":armor_from", 3),
			(store_script_param, ":armor_to", 4),
		
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		(assign, ":add", 0), 
		
		(str_store_troop_name, s1, ":troop"),
		(str_store_troop_name, s0, ":pool"),
		(assign, reg0, ":number"), 
		#(display_message, "@pool: {s0} troop: {s1}, pool size: {reg0}"),
		
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),		  
			(item_get_type, ":type", ":item"),
			#(item_get_slot, ":head_armor", ":item", slot_item_head_armor),
			(item_get_slot, ":body_armor", ":item", slot_item_body_armor),
			(assign, ":armor", -1),
			(try_begin),
			# (eq, ":type", itp_type_head_armor),
			# (ge, ":head_armor", ":armor_from"),
			# (le, ":head_armor", ":armor_to"),
			# (assign, ":armor", ":item"),
			# (str_store_item_name, s1, ":item"),
			# (else_try),
			(eq, ":type", itp_type_body_armor),
			(ge, ":body_armor", ":armor_from"),
			(le, ":body_armor", ":armor_to"),
			(assign, ":armor", ":item"),
			(try_end),
			(gt, ":armor", 0),
			(troop_add_item, ":troop", ":armor"),
			(val_add, ":add", 1),
			# (str_store_troop_name, s0, ":troop"),
			# (str_store_item_name, s1, ":armor"),
			# (display_message, "@{s0} adds item {s1}"),
		(try_end),
		(assign, reg0, ":add"),
		(gt, ":add", 0),
	])

	##script_cf_add_troop_items_helmet
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: troop, pool, armor_from, armor_to
	# OUTPUT: nothing (can fail)
cf_add_troop_items_helmet = (
	"cf_add_troop_items_helmet",
	[
		(store_script_param, ":troop", 1),
			(store_script_param, ":pool", 2),
			(store_script_param, ":armor_from", 3),
			(store_script_param, ":armor_to", 4),
		
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		(assign, ":add", 0), 
		
		(str_store_troop_name, s1, ":troop"),
		(str_store_troop_name, s0, ":pool"),
		(assign, reg0, ":number"), 
		#(display_message, "@pool: {s0} troop: {s1}, pool size: {reg0}"),
		
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),		  
			(item_get_type, ":type", ":item"),
			(item_get_slot, ":head_armor", ":item", slot_item_head_armor),
			#(item_get_slot, ":body_armor", ":item", slot_item_body_armor),
			(assign, ":armor", -1),
			(try_begin),
			(eq, ":type", itp_type_head_armor),
			(ge, ":head_armor", ":armor_from"),
			(le, ":head_armor", ":armor_to"),
			(assign, ":armor", ":item"),
			# (else_try),
			# (eq, ":type", itp_type_body_armor),
			# (ge, ":body_armor", ":armor_from"),
			# (le, ":body_armor", ":armor_to"),
			# (assign, ":armor", ":item"),
			# (str_store_item_name, s1, ":item"),
			(try_end),
			(gt, ":armor", 0),
			(troop_add_item, ":troop", ":armor"),
			(val_add, ":add", 1),
			# (str_store_troop_name, s0, ":troop"),
			# (str_store_item_name, s1, ":armor"),
			# (display_message, "@{s0} adds item {s1}"),
		(try_end),
		(assign, reg0, ":add"),
		(gt, ":add", 0),
	])	
	