from header import *
##script_cf_recruit_individual_merc - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: recruits several troops of the center the lord is in
	#input: party_no to recruit to
	#output: none
	#TODO: crusaders, mercs
cf_recruit_individual_merc = (
	"cf_recruit_individual_merc", #tom-made
			[
			(store_script_param, ":party_no", 1),

		(party_get_attached_to, ":no_center", ":party_no"),
		(is_between, ":no_center", walled_centers_begin, walled_centers_end),
		(try_begin),
			(store_random_in_range, ":random", 1, 10), #more for merc hiring
			(call_script, "script_select_mercenary_troop", ":no_center"),
			(assign, ":troop", reg1),
			###(gt, ":troop", "trp_farmer"),
			(gt, ":troop", "trp_player"),
			(party_add_members, ":party_no", ":troop", ":random"),
		(try_end),		
		])

		##script_cf_recruit_merc_lance_for_npc - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: selects a owned center of the lord and then recruits lance
	#input: party_no to recruit to.
	#output: none
	#TODO: crusaders, mercs
cf_recruit_merc_lance_for_npc = (
	"cf_recruit_merc_lance_for_npc", #tom-made
			[
			(store_script_param, ":party_no", 1),

		(store_faction_of_party, ":party_faction", ":party_no"),
		#####(assign, ":party_faction", "fac_kingdom_23"),
		
		#select center to recruit from
		(call_script, "script_cf_select_random_town_with_faction", ":party_faction"),
		(gt, reg0, 0),
		(assign, ":no_center", reg0),
		
		(party_get_slot,":mercs_generic", ":no_center", slot_regional_mercs),
		(party_get_slot,":mercs1", ":no_center", slot_spec_mercs1),
		(party_get_slot,":mercs2", ":no_center", slot_spec_mercs2),
		
		(party_get_slot,":mercs_generic_number", ":no_center", slot_regional_mercs_number_npc),
		(party_get_slot,":mercs1_number", ":no_center", slot_spec_mercs1_number_npc),
		(party_get_slot,":mercs2_number", ":no_center", slot_spec_mercs2_number_npc),
		
		(assign, ":slot_to_recruit_from", -1), #recruit from generic mercs
		(try_begin),
			(gt, ":mercs2", 0), #generic should be guaranteed, special not
			(gt, ":mercs2_number", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(assign, ":slot_to_recruit_from", slot_spec_mercs2),
			(val_sub, ":mercs2_number", 1),
				(party_set_slot, ":no_center", slot_regional_mercs_number_npc, ":mercs2_number"),
		(else_try),
			(gt, ":mercs1", 0), #generic should be guaranteed, special not
			(gt, ":mercs1_number", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(assign, ":slot_to_recruit_from", slot_spec_mercs1),
			(val_sub, ":mercs1_number", 1),
			(party_set_slot, ":no_center", slot_spec_mercs1_number_npc, ":mercs1_number"),
		(else_try),
			(gt, ":mercs_generic", 0), #generic should be guaranteed
			(gt, ":mercs_generic_number", 0), 
			(assign, ":slot_to_recruit_from", slot_regional_mercs),
			(val_sub, ":mercs_generic_number", 1),
			(party_set_slot, ":no_center", slot_spec_mercs2_number_npc, ":mercs_generic_number"),
		(try_end),
		
		(gt, ":slot_to_recruit_from", -1),
		(call_script, "script_fill_company", ":no_center", ":party_no", ":slot_to_recruit_from"),  
		
			##hire some individual mercs - todo
		# (try_begin),
			# (store_random_in_range, ":random", 1, 10), #more for merc hiring
			# (gt, ":random", 0),
			# (call_script, "script_select_mercenary_troop", ":no_center"),
			# (assign, ":troop", reg1),
			# (gt, ":troop", "trp_farmer"),
			# (party_add_members, ":party_no", ":troop", ":random"),
		# (try_end),		
		])

##script_cf_recruit_lance_for_npc - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: selects a owned center of the lord and then recruits lance
	#input: party_no to recruit to.
	#output: none
	#TODO: crusaders, mercs
cf_recruit_lance_for_npc =	(
	"cf_recruit_lance_for_npc", #tom-made
			[
			(store_script_param, ":party_no", 1),

		#(store_faction_of_party, ":party_faction", ":party_no"),
		(party_get_slot, ":party_type",":party_no", slot_party_type),
		
		(assign, ":leader", -1),
				(try_begin),
					(eq, ":party_type", spt_kingdom_hero_party),
					(party_stack_get_troop_id, ":leader", ":party_no"),
				(try_end),
		
		#(neq, ":leader", -1),
		#select center to recruit from
		(assign, ":no_center", -1), #for funny future merc recruitment
		(assign, ":recruit_amount", 2),
		(assign, ":top_range", centers_end),
		(try_for_range, ":center", centers_begin, ":top_range"),
			(this_or_next|neg|party_slot_ge, ":center", slot_center_is_besieged_by, 1),
			(neg|party_slot_eq, ":center", slot_village_state, svs_being_raided),
			(party_get_slot, ":town_lord", ":center", slot_town_lord),
			(eq, ":town_lord", ":leader"),
			(party_get_slot, ":lances_available", ":center", slot_feudal_lances),
			(gt, ":lances_available", 0),
			(call_script, "script_fill_lance", ":center", ":party_no"),
			(val_sub, ":lances_available", 1),
			(party_set_slot, ":center", slot_feudal_lances, ":lances_available"),
			(assign, ":no_center", ":center"),
			(val_sub, ":recruit_amount", 1),
			(eq, ":recruit_amount", 0),
			(assign, ":top_range", -1), #break
		(try_end),
		
		(gt, ":no_center", 0),
		#later - merc company hiring #TODO seperate thing in the future
		# (store_party_size, ":size" ,":party_no"),
		# (try_begin),
			# (eq, ":center", -1),
			# (try_for_range, ":center2", centers_begin, centers_end),
				# (store_faction_of_party, ":center_faction", ":center2"),
			# (eq, ":center_faction", ":party_faction"),
			# (assign, ":center", ":center2"),
			# (assign, ":center2", -1),
			# (try_end),
			# (neq, ":center", -1),
			# (lt, ":size", 50), 
			# (call_script, "script_fill_lance", ":center", ":party_no"),
		# (try_end),
		
			#hire some individual mercs - todo. This is obsolete, selects volunteers instead
		# (try_begin),
			# (store_random_in_range, ":random", 0, 2),
			# (gt, ":random", 0),
			# (call_script, "script_select_mercenary_troop", ":no_center"),
			# (assign, ":troop", reg1),
			# (gt, ":troop", "trp_farmer"),
			# (party_add_members, ":party_no", ":troop", ":random"),
		# (try_end),		
		])
