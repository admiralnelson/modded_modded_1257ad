from header import *
		##script_set_troop_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: sets the culture for the regular troops.
set_troop_culture =	(
	"set_troop_culture",
	[
		(try_for_range, ":troop", "trp_mercenaries_end", "trp_looter"),
			(try_begin),
			(is_between, ":troop", finn_culture_start, finn_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_finnish"),
		(else_try),
			(is_between, ":troop", mazovian_culture_start, mazovian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_mazovian"),
		(else_try),
			(is_between, ":troop", serbian_culture_start, serbian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_serbian"),
		(else_try),
			(is_between, ":troop", welsh_culture_start, welsh_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_welsh"),
		(else_try),
			(is_between, ":troop", teutonic_culture_start, teutonic_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_teutonic"),
		(else_try),
			(is_between, ":troop", mongol_culture_start, mongol_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_mongol"),
		(else_try),
			(is_between, ":troop", balkan_culture_start, balkan_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_balkan"),
		(else_try),
			(is_between, ":troop", rus_culture_start, rus_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_rus"),
		(else_try),
			(is_between, ":troop", nordic_culture_start, nordic_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_nordic"),
		(else_try),
			(is_between, ":troop", balt_culture_start, balt_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_baltic"),
		(else_try),
			(is_between, ":troop", marinid_culture_start, marinid_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_marinid"),
		(else_try),
			(is_between, ":troop", bedouin_culture_start, bedouin_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_mamluke"),
		(else_try),
			(is_between, ":troop", byz_culture_start, byz_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_byzantium"),
		(else_try),
			(is_between, ":troop", iberian_culture_start, iberian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_iberian"),
		(else_try),
			(is_between, ":troop", italian_culture_start, italian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_italian"),
		(else_try),
			(is_between, ":troop", andalus_culture_start, andalus_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_andalus"),
		(else_try),
			(is_between, ":troop", gaelic_culture_start, gaelic_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_gaelic"),
		(else_try),
			(is_between, ":troop", anatolian_culture_start, anatolian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_anatolian"),
		(else_try),
			(is_between, ":troop", scottish_culture_start, scottish_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_scotish"),
		(else_try),
			(is_between, ":troop", euro_culture_start, euro_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_western"),		
		(try_end),
		(try_end),
	])