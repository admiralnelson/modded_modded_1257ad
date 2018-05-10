from header import *
# script_cf_is_melee_weapon_for_tutorial
	# Input: arg1 = item_no
	# Output: none (can fail)
cf_is_melee_weapon_for_tutorial = (
	"cf_is_melee_weapon_for_tutorial",
		[
		(store_script_param, ":item_no", 1),
		(assign, ":result", 0),
		(try_begin),
			(this_or_next|eq, ":item_no", "itm_quarter_staff"),
			(eq, ":item_no", "itm_practice_sword"),
			(assign, ":result", 1),
		(try_end),
		(eq, ":result", 1),
	])