from header import *


	##script_troop_find_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description
	##input: troop to search for, culture
	##output: reg0 returns -1 if the troop does not belong to the culture, 0 if belongs(village), 1(town), 2(noble)
troop_find_culture = (
	"troop_find_culture",
	[
		(store_script_param, ":troop", 1),
		(store_script_param, ":culture", 2),
		
		(faction_get_slot, ":village", ":culture", slot_faction_tier_1_troop),
		(faction_get_slot, ":town", ":culture", slot_faction_tier_1_town_troop),
		(faction_get_slot, ":noble", ":culture", slot_faction_tier_1_castle_troop),
		
		(assign, reg0, -1),
		(assign, reg10, -1),
		# (try_begin),
			# (call_script, "script_troop_tree_search", ":troop", ":village"),	
		# (eq, reg10, ":troop"),
		# (assign, reg0, 0),
		# (else_try),
			# (call_script, "script_troop_tree_search", ":troop", ":town"),	
		# (eq, reg10, ":troop"),
		# (assign, reg0, 1),
		# (else_try),
			# (call_script, "script_troop_tree_search", ":troop", ":noble"),	
		# (eq, reg10, ":troop"),
		# (assign, reg0, 2),
		# (try_end),
		
				(try_begin),
			(call_script, "script_troop_tree_search", ":troop", ":noble"),	
		(eq, reg10, ":troop"),
		(assign, reg0, 2),
		(else_try),
			(call_script, "script_troop_tree_search", ":troop", ":town"),	
		(eq, reg10, ":troop"),
		(assign, reg0, 1),
		(else_try),
			(call_script, "script_troop_tree_search", ":troop", ":village"),	
		(eq, reg10, ":troop"),
		(assign, reg0, 0),
		(try_end),
	])
	
	##script_troop_tree_search
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description
	## recursively search a troop.
	##input: target target_troop - the troop to search for, troop - current troop in the tree path
	##output: reg10 returns the assigned troop if found. IF not reg10 is unchanged.
troop_tree_search = (
	"troop_tree_search",
	[
		(store_script_param, ":target_troop", 1),
		(store_script_param, ":troop", 2),
		
		(troop_get_upgrade_troop,":path1",":troop",0),
		(troop_get_upgrade_troop,":path2",":troop",1),
		(try_begin),
			(eq, ":troop", ":target_troop"),
		(assign, reg10, ":target_troop"),
		(else_try),
			(gt, ":path1", 0),
			(call_script, "script_troop_tree_search", ":target_troop", ":path1"),	
		(eq, reg10, ":target_troop"),
		(else_try),  
			(gt, ":path2", 0),
		(call_script, "script_troop_tree_search", ":target_troop", ":path2"),	
		(try_end),
	])
	
	
	