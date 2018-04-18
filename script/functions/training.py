from header import  *

#script_get_random_melee_training_weapon
		# INPUT: none
		# OUTPUT: reg0 = weapon_1, reg1 = weapon_2
get_random_melee_training_weapon = (
	"get_random_melee_training_weapon",
			[
				(assign, ":weapon_1", -1),
				(assign, ":weapon_2", -1),
				(store_random_in_range, ":random_no", 0, 3),
				(try_begin),
					(eq, ":random_no", 0),
					(assign, ":weapon_1", "itm_practice_staff"),
				(else_try),
					(eq, ":random_no", 1),
					(assign, ":weapon_1", "itm_practice_sword"),
					(assign, ":weapon_2", "itm_practice_shield"),
				(else_try),
					(assign, ":weapon_1", "itm_heavy_practice_sword"),
				(try_end),
				(assign, reg0, ":weapon_1"),
				(assign, reg1, ":weapon_2"),
		])
