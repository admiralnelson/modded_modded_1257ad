from header import *


	# script_set_matching_items
	# Input: arg1 = body_item, arg2 = agent_no, arg3 = troop_no
	# Output: none
set_matching_items = (
	"set_matching_items",
		[
		(store_script_param, ":body_item", 1),
		(store_script_param, ":agent_no", 2),
		(store_script_param, ":troop_no", 3),
		
		#(assign ,reg0, ":body_item"),
		#(assign, reg1, ":troop_no"),
		#(assign, reg2, ":agent_no"),
		
		# (str_store_troop_name, s1, ":troop_no"),
		# (str_store_item_name, s2, ":body_item"),
		#(display_message, "@this is: {s1} item: {s2} - {reg0}, troop: {reg1}, agent: {reg2}", 0xffff0000),
		
		#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
		
		(assign, ":continue", 0),
		
		(try_begin),
			(eq, ":troop_no", "trp_euro_horse_4"),
			(assign, ":continue", 2),
		(else_try),
			(eq, ":troop_no", "trp_nordic_knight"),
			(assign, ":continue", 2),
		(else_try),
			(eq, ":troop_no", "trp_gaelic_knight"),
			(assign, ":continue", 1),
		(else_try),
			(eq, ":troop_no", "trp_welsh_horse_4"),
			(assign, ":continue", 1),  
		(else_try),
			(eq, ":troop_no", "trp_iberian_knight"),
			(assign, ":continue", 2),
		(else_try),
			(eq, ":troop_no", "trp_andalus_horse_4"),
			(assign, ":continue", 1),
		(else_try),
			(eq, ":troop_no", "trp_rus_horse_4"),
			(assign, ":continue", 1),
		(try_end),
		
		(try_begin),
			(neq, ":agent_no", -1),		  
			(eq, ":continue", 1),
			(store_random_in_range, ":random", 0, 100),
			(try_begin),
			(gt, ":random", 65),
			(try_begin),
				(eq, ":troop_no", "trp_rus_horse_4"),
				(store_random_in_range, ":horse", "itm_mon_lamellar_horse_a", "itm_kau_montcada_horse"),
			(else_try),
				(store_random_in_range, ":horse", "itm_warhorse_white", "itm_warhorse_player"),
			(try_end),
			(else_try),
			(store_random_in_range, ":horse", 0, 3),
			(try_begin),
				(eq, ":horse", 0),
				(assign, ":horse", "itm_hunter"),
			(else_try),
				(eq, ":horse", 1),
				(assign, ":horse", "itm_horse_e"),
			(else_try),
				(assign, ":horse", "itm_horse_d"),
			(try_end),
			(try_end),
			(troop_set_inventory_slot, ":troop_no", ek_horse, ":horse"),
		(try_end),
		
		
		(try_begin),
			(eq, ":continue", 2),
			(neq, ":agent_no", -1),
			(try_begin),
			(eq, ":body_item", itm_rnd_surcoat_01),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_01),
			#(troop_set_inventory_slot, ":troop_no", ek_head, itm_rnd_helm_01),
			#(display_message, "@this is: .... {s1} .... item: {s2} - {reg0}, helm_01", 0xff00ff00),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_02),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_02),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_03),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_03),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_04),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_04),
			#(troop_set_inventory_slot, ":troop_no", ek_head, itm_rnd_helm_02),
			#(display_message, "@this is: .... {s1} .... item: {s2} - {reg0}, helm_02", 0xff00ff00),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_05),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_05),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_06),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_06),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_07),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_07),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_08),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_08),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_09),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_09),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_10),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_10),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_11),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_11),
			#(troop_set_inventory_slot, ":troop_no", ek_head, itm_rnd_helm_02),
			#(display_message, "@this is: .... {s1} .... item: {s2} - {reg0}, helm_02", 0xff00ff00),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_12),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_12),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_13),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_13),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_14),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_14),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_15),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_15),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_16),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_16),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_17),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_17),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_18),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_18),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_19),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_19),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_20),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_20),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_21),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_21),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_22),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_22),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_23),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_23),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			# (else_try),
			# (store_random_in_range, ":horse_item", itm_rnd_horse_01, itm_rnd_horse_23 + 1),
			# (troop_set_inventory_slot, ":troop_no", ek_horse, ":horse_item"),
			(try_end),
		(try_end),
		])
	