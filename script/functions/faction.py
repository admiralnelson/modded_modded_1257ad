from header import *

# script_count_parties_of_faction_and_party_type:
		# counts number of active parties with a template and faction.
		# Input: arg1 = faction_no, arg2 = party_type
		# Output: reg0 = count
		
count_parties_of_faction_and_party_type = (
			"count_parties_of_faction_and_party_type",
			[
				(store_script_param_1, ":faction_no"),
				(store_script_param_2, ":party_type"),
				(assign, reg0, 0),
				(try_for_parties, ":party_no"),
					(party_is_active, ":party_no"),
					(party_get_slot, ":cur_party_type", ":party_no", slot_party_type),
					(store_faction_of_party, ":cur_faction", ":party_no"),
					(eq, ":cur_party_type", ":party_type"),
					(eq, ":cur_faction", ":faction_no"),
					(val_add, reg0, 1),
				(try_end),
		])


# script_faction_get_number_of_armies
		# Input: arg1 = faction_no
		# Output: reg0 = number_of_armies
faction_get_number_of_armies = (
	"faction_get_number_of_armies",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":num_armies", 0),
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(store_troop_faction, ":hero_faction_no", ":troop_no"),
					(eq, ":hero_faction_no", ":faction_no"),
					(troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
					(ge, ":hero_party", 0),
					(party_is_active, ":hero_party"),
					(call_script, "script_party_count_fit_regulars", ":hero_party"),
					(assign, ":party_size", reg0),
					(call_script, "script_party_get_ideal_size", ":hero_party"),
					(assign, ":ideal_size", reg0),
					(val_mul, ":ideal_size", 60),
					(val_div, ":ideal_size", 100),
					(gt, ":party_size", ":ideal_size"),
					(val_add, ":num_armies", 1),
				(try_end),
				(assign, reg0, ":num_armies"),
		])

		# script_faction_recalculate_strength
		# Input: arg1 = faction_no
		# Output: reg0 = strength
faction_recalculate_strength = (
	"faction_recalculate_strength",
			[
				(store_script_param_1, ":faction_no"),
				
				(call_script, "script_faction_get_number_of_armies", ":faction_no"),
				(assign, ":num_armies", reg0),
				(assign, ":num_castles", 0),
				(assign, ":num_towns", 0),
				
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(eq, ":center_faction", ":faction_no"),
					(try_begin),
						(party_slot_eq, ":center_no", slot_party_type, spt_castle),
						(val_add, ":num_castles", 1),
					(else_try),
						(party_slot_eq, ":center_no", slot_party_type, spt_town),
						(val_add, ":num_towns", 1),
					(try_end),
				(try_end),
				
				(faction_set_slot, ":faction_no", slot_faction_num_armies, ":num_armies"),
				(faction_set_slot, ":faction_no", slot_faction_num_castles, ":num_castles"),
				(faction_set_slot, ":faction_no", slot_faction_num_towns, ":num_towns"),
				
		])

# script_cf_faction_get_random_enemy_faction
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (Can fail)
cf_faction_get_random_enemy_faction = (
	"cf_faction_get_random_enemy_faction",
			[
				(store_script_param_1, ":faction_no"),
				
				(assign, ":result", -1),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(le, ":cur_relation", -1),
					(val_add, ":count_factions", 1),
				(try_end),
				(store_random_in_range,":random_faction",0,":count_factions"),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(eq, ":result", -1),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(le, ":cur_relation", -1),
					(val_add, ":count_factions", 1),
					(gt, ":count_factions", ":random_faction"),
					(assign, ":result", ":cur_faction"),
				(try_end),
				
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		])
		
		# script_cf_faction_get_random_friendly_faction
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (Can fail)
cf_faction_get_random_friendly_faction = (
	"cf_faction_get_random_friendly_faction",
			[
				(store_script_param_1, ":faction_no"),
				
				(assign, ":result", -1),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(neq, ":cur_faction", ":faction_no"),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(ge, ":cur_relation", 0),
					(val_add, ":count_factions", 1),
				(try_end),
				(store_random_in_range,":random_faction",0,":count_factions"),
				(assign, ":count_factions", 0),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					(eq, ":result", -1),
					(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					(neq, ":cur_faction", ":faction_no"),
					(store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
					(ge, ":cur_relation", 0),
					(val_add, ":count_factions", 1),
					(gt, ":count_factions", ":random_faction"),
					(assign, ":result", ":cur_faction"),
				(try_end),
				
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		])



		# script_cf_get_random_lord_in_a_center_with_faction
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
cf_get_random_lord_in_a_center_with_faction = (
	"cf_get_random_lord_in_a_center_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
				(try_end),
				(store_random_in_range, ":random_lord", 0, ":count_lords"),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(eq, ":result", -1),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
					(lt, ":random_lord", ":count_lords"),
					(assign, ":result", ":lord_no"),
				(try_end),
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		])
		
		# script_cf_get_random_lord_except_king_with_faction
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
cf_get_random_lord_except_king_with_faction = (
	"cf_get_random_lord_except_king_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(val_add, ":count_lords", 1),
				(try_end),
				(store_random_in_range, ":random_lord", 0, ":count_lords"),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(eq, ":result", -1),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(eq, ":faction_no", ":lord_faction_no"),
					(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(val_add, ":count_lords", 1),
					(lt, ":random_lord", ":count_lords"),
					(assign, ":result", ":lord_no"),
				(try_end),
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		])
		
		
		# script_cf_get_random_lord_from_another_faction_in_a_center
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
cf_get_random_lord_from_another_faction_in_a_center = (
	"cf_get_random_lord_from_another_faction_in_a_center",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(neq, ":lord_faction_no", ":faction_no"),
					(store_relation, ":our_relation", ":lord_faction_no", "fac_player_supporters_faction"),
					(store_relation, ":lord_relation", ":lord_faction_no", ":faction_no"),
					(lt, ":lord_relation", 0),
					(ge, ":our_relation", 0),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
				(try_end),
				(store_random_in_range, ":random_lord", 0, ":count_lords"),
				(assign, ":count_lords", 0),
				(try_for_range, ":lord_no", heroes_begin, heroes_end),
					(eq, ":result", -1),
					(store_troop_faction, ":lord_faction_no", ":lord_no"),
					(neq, ":lord_faction_no", ":faction_no"),
					(store_relation, ":our_relation", ":lord_faction_no", "fac_player_supporters_faction"),
					(store_relation, ":lord_relation", ":lord_faction_no", ":faction_no"),
					(lt, ":lord_relation", 0),
					(ge, ":our_relation", 0),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					#(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
					(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
					(ge, ":lord_party", 0),
					(party_get_attached_to, ":lord_attachment", ":lord_party"),
					(is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
					(val_add, ":count_lords", 1),
					(lt, ":random_lord", ":count_lords"),
					(assign, ":result", ":lord_no"),
				(try_end),
				(neq, ":result", -1),
				(assign, reg0, ":result"),
		])


		# script_create_kingdom_party_if_below_limit
		# WARNING: modified by 1257AD devs
		# Input: arg1 = faction_no, arg2 = party_type (variables beginning with spt_)
		# Output: reg0 = party_no
create_kingdom_party_if_below_limit	= (
	"create_kingdom_party_if_below_limit",
			[
				(store_script_param_1, ":faction_no"),
				(store_script_param_2, ":party_type"),
				
				(call_script, "script_count_parties_of_faction_and_party_type", ":faction_no", ":party_type"),
				(assign, ":party_count", reg0),
				
				(assign, ":party_count_limit", 0),
				(faction_get_slot, ":num_towns", ":faction_no", slot_faction_num_towns),
				
				(try_begin),
					##        (eq, ":party_type", spt_forager),
					##        (assign, ":party_count_limit", 1),
					##      (else_try),
					##        (eq, ":party_type", spt_scout),
					##        (assign, ":party_count_limit", 1),
					##     (else_try),
					(eq, ":party_type", spt_patrol),
						(try_begin),
							(eq, ":faction_no", "fac_papacy"),
							(assign, ":party_count_limit", 6),
						(else_try),
							(eq, ":num_towns", 0),
								(assign, ":party_count_limit", 0),
						(else_try),
							(eq, ":num_towns", 1),
								(assign, ":party_count_limit", 1),
						(else_try),
							(ge, ":num_towns", 2),
						#(store_mul, ":patrols", ":num_towns", 1),
						#(val_div, ":patrols", 2), #tom
						#(assign, ":party_count_limit", ":patrols"),
								(assign, ":party_count_limit", 0), #tom was 2 only the factions who are about to get destroyed have them
						(try_end),
				 
					# (else_try),
					# (eq, ":party_type", spt_messenger),
					# (try_begin),
					# (eq, ":num_towns", 0),
					# (assign, ":party_count_limit", 0),
					# (else_try),
					# (assign, ":party_count_limit", 1),
					# (try_end),
				(else_try),
					(eq, ":party_type", spt_kingdom_caravan),
					(try_begin),
						(eq, ":num_towns", 0),
							(assign, ":party_count_limit", 0),
					(else_try),
						(eq, ":num_towns", 1),
							(assign, ":party_count_limit", 1),
					(else_try),
						#(eq, ":num_towns", 2),
						(store_mul, ":limit", ":num_towns", 1), #tom was 2
						(assign, ":party_count_limit", ":limit"),
					(try_end),
				(else_try),
					(eq, ":party_type", spt_prisoner_train),
						(try_begin),
							(eq, ":num_towns", 0),
								(assign, ":party_count_limit", 0),
						(else_try),
							(eq, ":num_towns", 1),
								(assign, ":party_count_limit", 1),
						(else_try),
							(store_mul, ":limit", ":num_towns", 2),
							(assign, ":party_count_limit", ":limit"),
						(try_end),
				(try_end),
				(assign, reg0, -1),
				(try_begin),
					(lt, ":party_count", ":party_count_limit"),
						(call_script,"script_cf_create_kingdom_party", ":faction_no", ":party_type"),
				(try_end),
		])
		

		# script_cf_create_kingdom_party
		# WARNING: modified by 1257AD devs
		# Input: arg1 = faction_no, arg2 = party_type (variables beginning with spt_)
		# Output: reg0 = party_no
cf_create_kingdom_party	= (
	"cf_create_kingdom_party",
			[
				(store_script_param_1, ":faction_no"),
				(store_script_param_2, ":party_type"),
				
				(str_store_faction_name, s7, ":faction_no"),
				(assign, ":party_name_str", "str_no_string"),
				
				(faction_get_slot, ":reinforcements_a", ":faction_no", slot_faction_reinforcements_a),
				(faction_get_slot, ":reinforcements_b", ":faction_no", slot_faction_reinforcements_b),
				##      (faction_get_slot, ":reinforcements_c", ":faction_no", slot_faction_reinforcements_c),
				
				(try_begin),
					##        (eq, ":party_type", spt_forager),
					##        (assign, ":party_template", "pt_forager_party"),
					#        (assign, ":party_name_str", "str_s7_foragers"),
					##      (else_try),
					##        (eq, ":party_type", spt_scout),
					##        (assign, ":party_template", "pt_scout_party"),
					#        (assign, ":party_name_str", "str_s7_scouts"),
					##      (else_try),
					(eq, ":party_type", spt_patrol),
						(assign, ":party_template", "pt_patrol_party"),
					#(assign, ":party_name_str", "str_s7_patrol"),
				(else_try),
					(eq, ":party_type", spt_kingdom_caravan),
						(assign, ":party_template", "pt_kingdom_caravan_party"),
					#        (assign, ":party_name_str", "str_s7_caravan"),
					# (else_try),
					# (eq, ":party_type", spt_messenger),
					# (assign, ":party_template", "pt_messenger_party"),
					#        (assign, ":party_name_str", "str_s7_messenger"),
					##      (else_try),
					##        (eq, ":party_type", spt_raider),
					##        (assign, ":party_template", "pt_raider_party"),
					##        (assign, ":party_name_str", "str_s7_raiders"),
				(else_try),
					(eq, ":party_type", spt_prisoner_train),
						(assign, ":party_template", "pt_prisoner_train_party"),
					#(assign, ":party_name_str", "str_s7_prisoner_train"),
				(try_end),
				
				(assign, ":result", -1),
				(try_begin),
					(try_begin),
						(eq, ":party_type", spt_kingdom_caravan),
							(call_script,"script_cf_select_random_town_with_faction", ":faction_no", -1),
								(set_spawn_radius, 0),
					(else_try), #not used at the moment
						(call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
							(set_spawn_radius, 1),
					(try_end),
					(assign, ":spawn_center", reg0),
					(is_between, ":spawn_center", centers_begin, centers_end),
						(spawn_around_party,":spawn_center",":party_template"),
						(assign, ":result", reg0),
						(party_set_faction, ":result", ":faction_no"),
						(try_begin),
						# rafi - add these
							(this_or_next | eq, ":party_type", spt_patrol),
							(this_or_next | eq, ":party_type", spt_prisoner_train),
						# end
							(eq, ":party_type", spt_kingdom_caravan),
								(party_set_slot, ":result", slot_party_home_center, ":spawn_center"),
								(party_set_slot, ":result", slot_party_last_traded_center, ":spawn_center"),
						(try_end),
						(party_set_slot, ":result", slot_party_type, ":party_type"),
						(party_set_slot, ":result", slot_party_ai_state, spai_undefined),
						(try_begin),
							(neq, ":party_name_str", "str_no_string"),
								(party_set_name, ":result", ":party_name_str"),
						(try_end),
					
						(try_begin),
						##          (eq, ":party_type", spt_forager),
						##          (party_add_template, ":result", ":reinforcements_a"),
						##        (else_try),
						##          (eq, ":party_type", spt_scout),
						##          (party_add_template, ":result", ":reinforcements_c"),
						##        (else_try),
						(eq, ":party_type", spt_patrol),
						(try_begin),
							(eq, ":faction_no", "fac_player_supporters_faction"),
								(party_get_slot, ":reinforcement_faction", ":spawn_center", slot_center_original_faction),
								(faction_get_slot, ":reinforcements_a", ":reinforcement_faction", slot_faction_reinforcements_a),
								(faction_get_slot, ":reinforcements_b", ":reinforcement_faction", slot_faction_reinforcements_b),
						(try_end),
						(party_add_template, ":result", ":reinforcements_a"),
						(party_add_template, ":result", ":reinforcements_a"),
						(party_add_template, ":result", ":reinforcements_a"),
						(party_add_template, ":result", ":reinforcements_b"),
			#tom
						(party_add_template, ":result", ":reinforcements_a"),
						(party_add_template, ":result", ":reinforcements_b"),
						(party_add_template, ":result", ":reinforcements_a"),
						(party_add_template, ":result", ":reinforcements_b"),
			#tom
						(party_set_slot, ":result", slot_party_ai_object, ":spawn_center"),
					(else_try),
						(eq, ":party_type", spt_kingdom_caravan),
						(try_begin),
							(eq, ":faction_no", "fac_player_supporters_faction"),
								(party_get_slot, ":reinforcement_faction", ":spawn_center", slot_center_original_faction),
								(faction_get_slot, ":reinforcements_b", ":reinforcement_faction", slot_faction_reinforcements_b),
						(try_end),
			#tom
						(call_script, "script_get_random_merc_company_from_center", ":spawn_center"),
						(assign, ":reinforcements", reg0),
						(party_add_template, ":result", ":reinforcements"),
						(party_add_template, ":result", ":reinforcements"),
						# (party_add_template, ":result", ":reinforcements_b"),
						# (party_add_template, ":result", ":reinforcements_b"),
						# (party_add_template, ":result", ":reinforcements_a"),
						# (party_add_template, ":result", ":reinforcements_a"),
			#tom
						(party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
						(party_set_ai_object,":result",":spawn_center"),
						(party_set_flags, ":result", pf_default_behavior, 1),
						(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
						(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
							(store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
							(party_set_slot, ":result", ":cur_goods_price_slot", average_price_factor),
						(try_end),
						# (else_try),
						# (eq, ":party_type", spt_messenger),
						# (faction_get_slot, ":messenger_troop", ":faction_no", slot_faction_messenger_troop),
						# (party_add_leader, ":result", ":messenger_troop"),
						# (party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
						# (party_set_ai_object,":result",":spawn_center"),
						# (party_set_flags, ":result", pf_default_behavior, 0),
						##        (else_try),
						##          (eq, ":party_type", spt_raider),
						##          (party_add_template, ":result", ":reinforcements_c"),
						##          (party_add_template, ":result", ":reinforcements_b"),
						##          (party_add_template, ":result", "pt_raider_captives"),
					(else_try),
						(eq, ":party_type", spt_prisoner_train),
							(party_add_template, ":result", ":reinforcements_b"),
							(party_add_template, ":result", ":reinforcements_a"),
							(party_add_template, ":result", ":reinforcements_a"),
							(try_begin),
								(call_script,"script_cf_faction_get_random_enemy_faction",":faction_no"),
									(store_random_in_range,":r",0,3),
									(try_begin),
										(lt, ":r", 1),
											(faction_get_slot, ":captive_reinforcements", reg0, slot_faction_reinforcements_b),
									(else_try),
										(faction_get_slot, ":captive_reinforcements", reg0, slot_faction_reinforcements_a),
									(try_end),
									(party_add_template, ":result", ":captive_reinforcements",1),
							(else_try),
									(party_add_template, ":result", "pt_default_prisoners"),
							(try_end),
						(party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
						(party_set_ai_object,":result",":spawn_center"),
						(party_set_flags, ":result", pf_default_behavior, 1),
					(try_end),
				(try_end),
				(ge, ":result", 0),
					(assign, reg0, ":result"),
		])
		