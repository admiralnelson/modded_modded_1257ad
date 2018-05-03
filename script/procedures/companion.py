from header import *
#script_update_companion_candidates_in_taverns
		# WARNING: modified by 1257AD devs
		# INPUT: none
		# OUTPUT: none
update_companion_candidates_in_taverns = (
	"update_companion_candidates_in_taverns",
			[
				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_shuffling_companion_locations"),
				(try_end),
				
				(try_for_range, ":troop_no", companions_begin, companions_end),
					(neg | troop_slot_eq, ":troop_no", slot_troop_traveling, 1), # rafi
					(troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
					(troop_slot_eq, ":troop_no", slot_troop_days_on_mission, 0),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
					
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(try_begin),
						(neg|troop_slot_eq, ":troop_no", slot_troop_home, ":town_no"),
						(neg|troop_slot_eq, ":troop_no", slot_troop_first_encountered, ":town_no"),
						(troop_set_slot, ":troop_no", slot_troop_cur_center, ":town_no"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_troop_name, 4, ":troop_no"),
							(str_store_party_name, 5, ":town_no"),
							(display_message, "@{!}{s4} is in {s5}"),
						(try_end),
					(try_end),
				(try_end),
		])
		
		#script_update_ransom_brokers
		# INPUT: none
		# OUTPUT: none
update_ransom_brokers = (
	"update_ransom_brokers",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_ransom_broker, 0),
				(try_end),
				
				(try_for_range, ":troop_no", ransom_brokers_begin, ransom_brokers_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_ransom_broker, ":troop_no"),
				(try_end),
				
				#(party_set_slot,"p_town_2",slot_center_ransom_broker,"trp_ramun_the_slave_trader"),
		])
		
		#script_update_tavern_travellers
		# INPUT: none
		# OUTPUT: none
update_tavern_travellers = (
	"update_tavern_travellers",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_traveler, 0),
				(try_end),
				
				(try_for_range, ":troop_no", tavern_travelers_begin, tavern_travelers_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_traveler, ":troop_no"),
					(assign, ":end_cond", 15),
					(try_for_range, ":unused", 0, ":end_cond"),
						(store_random_in_range, ":info_faction", kingdoms_begin, kingdoms_end),
						(faction_slot_eq, ":info_faction", slot_faction_state, sfs_active),
						(neq, ":info_faction", "$players_kingdom"),
						(neq, ":info_faction", "fac_player_supporters_faction"),
						(party_set_slot, ":town_no", slot_center_traveler_info_faction, ":info_faction"),
						(assign, ":end_cond", 0),
					(try_end),
				(try_end),
				
				(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "p_town_1_1"),
		])

		
		#script_update_booksellers
		# INPUT: none
		# OUTPUT: none
update_booksellers = (
	"update_booksellers",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_bookseller, 0),
				(try_end),
				
				(try_for_range, ":troop_no", tavern_booksellers_begin, tavern_booksellers_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_bookseller, ":troop_no"),
				(try_end),
				
				
				
		])
		
		#script_update_tavern_minstels
		# INPUT: none
		# OUTPUT: none
update_tavern_minstrels = (
	"update_tavern_minstrels",
			[(try_for_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_minstrel, 0),
				(try_end),
				
				(try_for_range, ":troop_no", tavern_minstrels_begin, tavern_minstrels_end),
					(store_random_in_range, ":town_no", towns_begin, towns_end),
					(party_set_slot, ":town_no", slot_center_tavern_minstrel, ":troop_no"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":troop_no"),
						(str_store_party_name, s5, ":town_no"),
						
						(display_message, "str_s4_is_at_s5"),
					(try_end),
				(try_end),
				
				
		])
		
update_other_taverngoers = (
	"update_other_taverngoers",
			[
				(store_random_in_range, ":fight_promoter_tavern", towns_begin, towns_end),
				(troop_set_slot, "trp_fight_promoter", slot_troop_cur_center, ":fight_promoter_tavern"),
				
				(store_random_in_range, ":belligerent_drunk_tavern", towns_begin, towns_end),
				(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, ":belligerent_drunk_tavern"),
		])
		