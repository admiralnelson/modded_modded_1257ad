from header import *


	##script_cf_hire_npc_specialist - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: companion, companion_culture
	##output: none
	##description: Hires the specialist for the players party
cf_hire_npc_specialist = (
	"cf_hire_npc_specialist",
		[
		(store_script_param, ":troop", 1),
		#(store_script_param, ":culture", 2),
		
		#hero is not in a party
		(party_count_members_of_type, reg1, "p_main_party", ":troop"),
		(eq, reg1, 0),
		
		#if enough space for the 
		(assign, ":continue", 0),
		(party_get_free_companions_capacity, reg1, "p_main_party"),
		(try_begin),
			(eq, reg1, 0),
			(assign, ":continue", 1),
			(display_message, "@Not enough space in the party to hire this specialist!"),
		(try_end),
		(eq, ":continue", 0),
		
		#get the price for npc
		(store_character_level, ":level",":troop"),
		(assign, ":cost", 50),
		(val_mul, ":cost", ":level"),
		(try_begin),
			(troop_slot_ge, ":troop", slot_troop_prisoner_of_party, 0),
			(val_mul, ":cost", 2),
		(try_end),
		
		#enough gold to hire
		(store_troop_gold, ":gold", "trp_player"),
		(try_begin),
			(ge, ":gold", ":cost"),
			(assign, ":continue", 0),
		(else_try),
			(assign, ":continue", 1),
			(display_message, "@Not enough gold!"),
		(try_end),
		(eq, ":continue", 0),
		(troop_remove_gold, "trp_player", ":cost"),

		#this in the future remove?
		#get culture
		(party_get_slot, ":culture", "$current_town", slot_center_culture),
		#(str_store_faction_name,s20, ":culture"),
		#(display_message, "@faction: {s20}"),
		#recruit
		(try_begin),
			#(display_message, "@try to equip"),
			(troop_slot_eq, ":troop", npc_slot_naked, 0),
			#(display_message, "@equiping"),
			(faction_get_slot, ":troop_type", ":culture", slot_faction_tier_1_town_troop),
			#(str_store_troop_name, s20, ":troop_type"),
			#(display_message, "@troop name: {s20}"),
			(call_script, "script_equip_companion", ":troop", ":troop_type"),
			# (troop_equip_items, ":troop"),
			# (troop_clear_inventory, ":troop"),
			#(display_message, "@equiped"),
			(troop_set_slot, ":troop", npc_slot_naked, 1),
			#(display_message, "@exiting"),
		(try_end),
		
		#hire 
		(party_add_members, "p_main_party", ":troop", 1),
		(troop_set_slot, ":troop", slot_troop_occupation, slto_player_companion),
		(troop_set_slot, ":troop", slot_troop_met, 1),
		
		(troop_get_slot, ":prison_center", ":troop", slot_troop_prisoner_of_party),
		(try_begin),
			(ge, ":prison_center", 1),
					(party_remove_prisoners, ":prison_center", ":troop", 1),
		(try_end),  
		(troop_set_slot, ":troop", slot_troop_prisoner_of_party, -1),
		
		
		(display_message, "@Hired!"),
		])