from header import *

#script_cf_village_recruit_volunteers_cond
		# INPUT: none
		# OUTPUT: none
cf_village_recruit_volunteers_cond = (
	"cf_village_recruit_volunteers_cond",
			[
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_checking_volunteer_availability_script"),
				(try_end),
				
				(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
				(neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
				(neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
				(store_faction_of_party, ":village_faction", "$current_town"),
				(party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
				(store_relation, ":village_faction_relation", ":village_faction", "fac_player_faction"),
				
				(ge, ":center_relation", 0),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_center_relation_at_least_zero"),
				(try_end),
				
				
				
				
				(this_or_next|ge, ":center_relation", 5),
				(this_or_next|eq, ":village_faction", "$players_kingdom"),
				(this_or_next|ge, ":village_faction_relation", 0),
				(this_or_next|eq, ":village_faction", "$supported_pretender_old_faction"),
				(eq, "$players_kingdom", 0),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_relationfaction_conditions_met"),
				(try_end),
				
				
				(party_slot_ge, "$current_town", slot_center_volunteer_troop_amount, 0),
				(party_slot_ge, "$current_town", slot_center_volunteer_troop_type, 1),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_troops_available"),
				(try_end),
				
				
				(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
				(ge, ":free_capacity", 1),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_party_has_capacity"),
				(try_end),
				
				
		])