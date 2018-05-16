from header import *


	#script_select_mercenary_troop - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: arg1 = center_no
		# OUTPUT: reg1 = troop_no
select_mercenary_troop = (
	"select_mercenary_troop",
	[
			(store_script_param, ":town_no", 1),
		
			(assign, ":troop_no", "trp_merc_euro_spearman"),
			#(party_get_slot, ":regional_mercs", ":town_no", slot_regional_mercs),
			(try_begin),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_euro),
				(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_balt),
				(store_random_in_range, ":troop_no", "trp_merc_balt_spearman", "trp_merc_maghreb_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_maghreb),
				(store_random_in_range, ":troop_no", "trp_merc_maghreb_spearman", "trp_merc_rus_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_rus),
				(store_random_in_range, ":troop_no", "trp_merc_rus_spearman", "trp_merc_latin_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_latin),
				(store_random_in_range, ":troop_no", "trp_merc_latin_spearman", "trp_merc_balkan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_balkan),
				(store_random_in_range, ":troop_no", "trp_merc_balkan_spearman", "trp_merc_scan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_scandinavian),
				(store_random_in_range, ":troop_no", "trp_merc_scan_spearman", "trp_merc_gaelic_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_gaelic),
				(store_random_in_range, ":troop_no", "trp_merc_gaelic_spearman", "trp_genoese_crossbowman"),
			(try_end),
		
			(assign, reg0, ":troop_no"),
	])

		#script_get_random_merc_company_from_center
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: center
	#output: reg0 random merc company
	#decription: gets a random mect company from the specified center. Does not consume merc resources. Used for kingdom parties
get_random_merc_company_from_center = (
	"get_random_merc_company_from_center",
	 [
		(store_script_param, ":center", 1),
		
		(party_get_slot,":mercs_generic", ":center", slot_regional_mercs),
		(party_get_slot,":mercs1", ":center", slot_spec_mercs1),
		(party_get_slot,":mercs2", ":center", slot_spec_mercs2),
		
		#(assign, ":template", 0),
		(try_begin),
			(gt, ":mercs2", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs2_party_template),
		(else_try),
			(gt, ":mercs1", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs1_party_template),
		(else_try),
			(gt, ":mercs_generic", 0), #generic should be guaranteed
			(party_get_slot, ":company_template", ":center", slot_regional_party_template),
		(try_end),
		
		(assign, reg0, ":company_template"),
	 ])


	