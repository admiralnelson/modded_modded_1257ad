from header import *

# count lords and ladies?
# NOTE: it purposes? idk. CTRL+F'd, I think this one is deprecated
# INPUT: kingdom id
# OUTPUT: reg0 - lord count, reg1 - ladies count, reg3 - lords start, reg4 - ladies start
raf_count_kingdom_lords_and_ladies = (
	"raf_count_kingdom_lords_and_ladies",
		[
			(store_script_param, ":kingdom", 1),
			
			(assign, ":lords", 0),
			(assign, ":ladies", 0),
		(assign, reg3, 0),
		(assign, reg4, 0),
			
			(try_for_range, ":cur_troop", lords_begin, lords_end),
				(store_faction_of_troop, ":faction", ":cur_troop"),
				(eq, ":faction", ":kingdom"),
				(try_begin),
					(eq, ":lords", 0),
					(assign, reg3, ":cur_troop"),
				(try_end),
				(val_add, ":lords", 1),
			(try_end),
			(try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
				(store_faction_of_troop, ":faction", ":cur_troop"),
				(eq, ":faction", ":kingdom"),
				(try_begin),
					(eq, ":ladies", 0),
					(assign, reg4, ":cur_troop"),
				(try_end),
				(val_add, ":ladies", 1),
			(try_end),
			
			(assign, reg0, ":lords"),
			(assign, reg1, ":ladies"),
		])