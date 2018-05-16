from header import *

	 #script_get_mercenary_troop_for_manor - tom made
	 # WARNING: this is totally new procedure (not present in native). 1257AD devs
	 #input: faction of the manor
	 #output: reg0 - troop id
	 #called to determine the faction mercenary troop, to raid the center. Does not include the special troops, such as the varangian guard
get_mercenary_troop_for_manor =	 (
	"get_mercenary_troop_for_manor",
	 [
			(store_script_param, ":fac", 1),
			 
		(assign, ":troop_no", "trp_merc_euro_spearman"),
		(try_begin),
			(call_script, "script_cf_select_random_town_with_faction", ":fac"),
			(assign, ":town_no", reg0),
			(gt, ":town_no", 0),
			#(party_get_slot, ":regional_mercs", ":town_no", slot_regional_mercs),
			(assign, ":merc_slot", slot_regional_mercs),
			(try_begin),
				(party_slot_eq, ":town_no", ":merc_slot", generic_euro),
				(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_balt),
				(store_random_in_range, ":troop_no", "trp_merc_balt_spearman", "trp_merc_mamluke_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_maghreb),
				(store_random_in_range, ":troop_no", "trp_merc_maghreb_spearman", "trp_merc_rus_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_rus),
				(store_random_in_range, ":troop_no", "trp_merc_rus_spearman", "trp_merc_latin_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_latin),
				(store_random_in_range, ":troop_no", "trp_merc_latin_spearman", "trp_merc_balkan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_balkan),
				(store_random_in_range, ":troop_no", "trp_merc_balkan_spearman", "trp_merc_scan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_scandinavian),
				(store_random_in_range, ":troop_no", "trp_merc_scan_spearman", "trp_merc_gaelic_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_gaelic),
				(store_random_in_range, ":troop_no", "trp_merc_gaelic_spearman", "trp_genoese_crossbowman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_mamluk),
				(store_random_in_range, ":troop_no", "trp_merc_mamluke_spearman", "trp_merc_maghreb_spearman"),
			(try_end),
		(try_end),
		(assign, reg0, ":troop_no"),
	 ])