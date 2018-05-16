from header import *

	#script_check_agents_for_lances
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: checks all the agents on the battlefield and removes the dead ones from the arrays.
	#input: none
	#output: none
check_agents_for_lances = (
	"check_agents_for_lances",
		[
			(get_player_agent_no,":p_agent"),
			(try_for_agents, ":cur_agent"),
			(neg|agent_slot_eq, ":cur_agent", slot_possessed, 1), #not a waste
			(neg|agent_is_alive, ":cur_agent"),
			(neg|agent_is_wounded, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_get_party_id, ":agent_party", ":cur_agent"),
			(eq, ":agent_party", "p_main_party"),
			(neq, ":p_agent", ":cur_agent"),
			(agent_get_slot, ":index", ":cur_agent", slot_index_value),
			(ge, ":index", 0),
			(troop_set_slot, "trp_lances_places",":index",0), #dead - remove
			(troop_set_slot, "trp_lances_troops",":index",0), #dead - remove
		(try_end),
		(call_script, "script_balance_lance_storage"),
		])
	
	#script_balance_lance_storage
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: removes the dead troops in the lance storage. Both in reserve and the combatans
	#input: none
	#output:none
balance_lance_storage = (
	"balance_lance_storage",
		[
		##COMBATANTS
		#copy to backup
		(assign, ":new_amount", 0),
		(try_for_range, ":index", 0, "$lance_troop_serving"),
			(troop_get_slot, ":troop","trp_lances_troops",":index"),
			(troop_get_slot, ":place","trp_lances_places",":index"),
			(gt, ":troop", 0),
			(troop_set_slot, "trp_temp_array_a", ":new_amount", ":troop"), #copy alive troops
			(troop_set_slot, "trp_temp_array_b", ":new_amount", ":place"), #copy alive troop hailings
			(val_add, ":new_amount", 1),
		(try_end),
		
		#copy it back adjused
		(assign, "$lance_troop_serving", ":new_amount"),
		(try_for_range, ":index", 0, "$lance_troop_serving"),
			(troop_get_slot, ":troop","trp_temp_array_a",":index"),
			(troop_get_slot, ":place","trp_temp_array_b",":index"),
			(troop_set_slot, "trp_lances_troops", ":index", ":troop"), #copy alive troops
			(troop_set_slot, "trp_lances_places", ":index", ":place"), #copy alive troop hailings
		(try_end),
	###########
	##RESERVE
			#copy to backup
		(assign, ":new_amount", 0),
		(try_for_range, ":index", 0, "$lance_troop_reserve"),
			(troop_get_slot, ":troop","trp_lances_troops_reserve",":index"),
			(troop_get_slot, ":place","trp_lances_places_reserve",":index"),
			(gt, ":troop", 0),
			(troop_set_slot, "trp_temp_array_a", ":new_amount", ":troop"), #copy alive troops
			(troop_set_slot, "trp_temp_array_b", ":new_amount", ":place"), #copy alive troop hailings
			(val_add, ":new_amount", 1),
		(try_end),
		
		#copy it back adjused
		(assign, "$lance_troop_reserve", ":new_amount"),
		(try_for_range, ":index", 0, "$lance_troop_reserve"),
			(troop_get_slot, ":troop","trp_temp_array_a",":index"),
			(troop_get_slot, ":place","trp_temp_array_b",":index"),
			(troop_set_slot, "trp_lances_troops_reserve", ":index", ":troop"), #copy alive troops
			(troop_set_slot, "trp_lances_places_reserve", ":index", ":place"), #copy alive troop hailings
		(try_end),
		])
	
	
	##script_count_nobles_commoners_for_center
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: count nobles and commoners for each center. Increase lances if there are troop uncounted
	##input: none
	##output: none
count_nobles_commoners_for_center = (
	"count_nobles_commoners_for_center",
		[
		#clear slots
		(try_for_parties, ":party"),
			(party_set_slot, ":party", slot_number_commoner, 0),
			(party_set_slot, ":party", slot_number_nobles, 0),
			(party_get_slot, ":troop_amount" ,":party", slot_number_troops_pending), #get pending
			(party_set_slot, ":party", slot_number_troops_pending, 0), #reset pending
			(ge, ":troop_amount", 1), #there are uncounted ones
			(val_div, ":troop_amount", 10),
			(party_get_slot, ":lance_amount" ,":party", slot_feudal_lances), #get pending
			(val_add, ":lance_amount", ":troop_amount"),
			(party_set_slot, ":party", slot_feudal_lances, ":lance_amount"),
		(try_end),
		
		(try_for_range, ":index", 0, "$lance_troop_reserve"),
			(troop_get_slot, ":troop","trp_lances_troops_reserve",":index"),
			(troop_get_slot, ":place","trp_lances_places_reserve",":index"),
			
			(assign, ":top_faction", "fac_player_faction"),
			(try_for_range, ":culture", "fac_culture_finnish", ":top_faction"),
				(call_script, "script_troop_find_culture", ":troop", ":culture"),
				(ge, reg0, 0), #found a culture
				(try_begin), #noble tree!
					(eq, reg0, 2),
				(party_get_slot, ":amount",":place", slot_number_nobles),
				(val_add, ":amount", 1),
				(party_set_slot, ":place", slot_number_nobles, ":amount"),
				(else_try), #townsman
				(party_get_slot, ":amount",":place", slot_number_commoner),
				(val_add, ":amount", 1),
				(party_set_slot, ":place", slot_number_commoner, ":amount"),
				(try_end),
			(assign, ":top_faction", -1), #break culture cycle
			(try_end),
		(try_end),
		])

	#script_add_lance_troop_to_regulars
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: adds the current troop to regulars(serving in players party), increases the counter
	#input: troop, center recruited from
	#output: none
add_lance_troop_to_regulars = (
	"add_lance_troop_to_regulars",
		[
		(store_script_param, ":troop", 1), 
		(store_script_param, ":center", 2), 
		(troop_set_slot, "trp_lances_places", "$lance_troop_serving", ":center"),
		(troop_set_slot, "trp_lances_troops", "$lance_troop_serving", ":troop"),
		(val_add, "$lance_troop_serving", 1),
		])

	##script_feudal_lance_manpower_update - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: party_id(village/town/castle)
	##output: none
	##description: updates the feudal recruits for the lance system in villages. max lances per village - 10.
feudal_lance_manpower_update = (
	"feudal_lance_manpower_update",
		[
		(store_script_param, ":center_no", 1),
		(store_script_param, ":limit", 2),
		(try_begin),
			(party_get_slot, ":manpower", ":center_no", slot_feudal_lances),
			
			#(party_get_slot, ":limit", ":center_no", slot_lances_cap),
			#set limit for the player
			(try_begin),
				(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
				(party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
				(val_div, ":player_relation", 25),
				(val_add, ":limit", ":player_relation"),
			(try_end),
			(lt, ":manpower", ":limit"),
			#(store_random_in_range, ":random", 1, 4), #1-3
			#(val_add, ":manpower", ":random"),
			(store_faction_of_party,":faction", ":center_no"),
			(try_begin), #when faction at paece - extra lance
				 (faction_slot_eq, ":faction", slot_faction_at_war, 0), #at peace
			 (val_add, ":manpower", 1),
			(try_end),
			(val_add, ":manpower", 1),
			(val_clamp, ":manpower", 1, ":limit"), #limit it to 10-15
			(party_set_slot, ":center_no", slot_feudal_lances, ":manpower"),
		(try_end),
		])

	###script_fill_company - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	###input: center, party, merc_type
	###output: none
	###description: company size - 30 men; 1 seargant, ~10 crossbow
fill_company = (
	"fill_company",
		[
		(store_script_param, ":center", 1), #to recruit from
		(store_script_param, ":party", 2), #to add recruits to
		(store_script_param, ":merc_slot", 3), #like, generic, special, ect. SLOT

		(assign, ":company_template", "pt_generic_euro"),
		(try_begin),
			(eq, ":merc_slot", slot_regional_mercs),
			(party_get_slot, ":company_template", ":center", slot_regional_party_template),
		(else_try),
			(eq, ":merc_slot", slot_spec_mercs1),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs1_party_template),
		(else_try),
			(eq, ":merc_slot", slot_spec_mercs2),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs2_party_template),
		(try_end),
		
		(party_add_template, ":party", ":company_template"),
		])
	