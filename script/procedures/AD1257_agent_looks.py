from header import *

	## script_set_matching_sexy_boots
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: item_no, agent_no
		## Output: none
set_matching_sexy_boots = (
	"set_matching_sexy_boots",
	[
		(store_script_param, ":agent", 1),
		(agent_get_item_slot, ":body", ":agent", ek_body),
		(agent_get_item_slot, ":foot", ":agent", ek_foot),
		(agent_get_item_slot, ":head", ":agent", ek_head),
		(agent_get_item_slot, ":hand", ":agent", ek_gloves),
		(try_begin), #african 
			(is_between, ":head", "itm_kufia_berber_black", "itm_legs_african"), #black head
		(try_begin), #need black hands and or legs
			(le, ":foot", 0),
			(agent_equip_item,":agent","itm_legs_african"),
			(assign, ":foot", "itm_legs_african"),
		(try_end),  
		(try_begin),
			(le, ":hand", 0),
			(agent_equip_item,":agent","itm_hands_african"),
			(assign, ":hand", "itm_hands_african"),
		(try_end),
		(else_try),
			(try_begin),
			(eq, ":hand", "itm_hands_african"),
			(agent_unequip_item, ":agent", "itm_hands_african"),
			(assign, ":hand", 0),
			(else_try),
			(eq, ":foot", "itm_legs_african"),
			(agent_unequip_item, ":agent", "itm_legs_african"),
			(assign, ":foot", 0),
		(try_end),  
		(try_end),
		(try_begin),
		 (le, ":foot", 0),
		 (neg|is_between, ":body", "itm_red_dress", "itm_nomad_armor"),
		 (neg|is_between, ":body", "itm_berber_robe_a", itm_saracen_kaftan_d+1),
		 (neg|is_between, ":body", "itm_meghrebi_leather_a", itm_black_guard+1),
			 (agent_equip_item,":agent","itm_bare_legs"),  
		(else_try), #short boots needed
			##check body armor
			#(this_or_next|is_between, ":body", "itm_veteran_surcoat_a", "itm_kau_aragon_knight"),
			(this_or_next|is_between, ":body", "itm_red_dress", "itm_nomad_armor"),
		(this_or_next|is_between, ":body", "itm_berber_robe_a", itm_saracen_kaftan_d+1),
			(this_or_next|is_between, ":body", "itm_meghrebi_leather_a", itm_black_guard+1),
			(this_or_next|is_between, ":body", "itm_kau_castile_a", "itm_teu_brother_surcoat_e"),
			(this_or_next|is_between, ":body", "itm_templar_sarjeant_surcoat", "itm_hirdman_a"),
			(this_or_next|is_between, ":body", "itm_sarranid_cloth_robe", "itm_skirmisher_armor"),
		(this_or_next|eq, ":body", "itm_teu_postulant_a"),
			(this_or_next|eq, ":body", "itm_teu_coat_of_plates"),
			#(this_or_next|is_between, ":body", "itm_veteran_surcoat_a", "itm_kau_aragon_knight"),
			(is_between, ":body", "itm_veteran_surcoat_a", "itm_kau_aragon_knight"),
		(neq, ":body", "itm_kau_aragon_knight"),
		(neq, ":body", "itm_surcoat_lithuania_a"),
		(neq, ":body", "itm_surcoat_lithuania_b"),
		(neq, ":body", "itm_surcoat_novgorod"),
		(neq, ":body", "itm_surcoat_gslask"),
		(neq, ":body", "itm_surcoat_pol_b"),
		(neq, ":body", "itm_teu_hochmeister_surcoat"),
		(neq, ":body", "itm_teu_hbrother_mail"),
		(neq, ":body", "itm_templar_mail_a"),
		(neq, ":body", "itm_templar_gambeson_a"),
		(neq, ":body", "itm_hospitaller_gambeson_a"),
		#(neg|is_between, ":body", "itm_kau_castile_a", "itm_teu_brother_surcoat_e"),
		
		##check foot armor
		(this_or_next|eq, ":foot", "itm_sarranid_boots_a_long"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_b_long"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_d_long"), 
		(this_or_next|eq, ":foot", "itm_byz_lord_boots_long"),
		(this_or_next|eq, ":foot", "itm_cuman_boots"), #for mamluke boots
		(this_or_next|eq, ":foot", "itm_splinted_greaves_long"),
		(this_or_next|eq, ":foot", "itm_mail_boots_long"),
		(this_or_next|eq, ":foot", "itm_legs_with_shoes"),
		(this_or_next|eq, ":foot", "itm_rus_boots_a"),
		(this_or_next|eq, ":foot", "itm_blue_hose"),
		(eq, ":foot", "itm_kau_mail_boots_dark_long"),
		##adjust and equip
		(val_sub, ":foot", 1),
		(agent_equip_item,":agent",":foot"),
		(else_try), #longs boots needed
			#check boots, no body armor is needed. 
			(this_or_next|eq, ":foot", "itm_sarranid_boots_a"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_b"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_d"), 
			(this_or_next|eq, ":foot", "itm_byz_lord_boots"), 
			(this_or_next|eq, ":foot", "itm_mamluke_boots"), 
			(this_or_next|eq, ":foot", "itm_splinted_greaves"),
		(this_or_next|eq, ":foot", "itm_mail_boots"),
		(this_or_next|eq, ":foot", "itm_berber_shoes"),
		(this_or_next|eq, ":foot", "itm_rus_cav_boots"),
		(this_or_next|eq, ":foot", "itm_priest_2_boots"),
		(eq, ":foot", "itm_kau_mail_boots_dark"),
		#adjust and equip
		(val_add, ":foot", 1),
			(agent_equip_item,":agent",":foot"),  
		(try_end),
	])
