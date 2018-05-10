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
		
		# script_cf_get_random_active_faction_except_player_faction_and_faction
		# WARNING : modified by 1257AD devs
		# "rafi: inject religion stuff"
		# Input: arg1 = except_faction_no
		# Output: reg0 = random_faction
cf_get_random_active_faction_except_player_faction_and_faction = (
	"cf_get_random_active_faction_except_player_faction_and_faction",
			[
				(store_script_param_1, ":except_faction_no"),
				(assign, ":num_factions", 0),
				
				# rafi - inject religion stuff
				(faction_get_slot, ":religion", ":except_faction_no", slot_faction_religion),
				# end rafi
				(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(neq, ":faction_no", ":except_faction_no"),
					(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
					(val_add, ":num_factions", 1),
				(try_end),
				(gt, ":num_factions", 0),
				(assign, ":selected_faction", -1),
				(store_random_in_range, ":random_faction", 0, ":num_factions"),
				(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
					(ge, ":random_faction", 0),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(neq, ":faction_no", ":except_faction_no"),
					(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
					(faction_slot_eq, ":faction_no", slot_faction_religion, ":religion"), # rafi
					(val_sub, ":random_faction", 1),
					(lt, ":random_faction", 0),
					(assign, ":selected_faction", ":faction_no"),
				(try_end),
				(assign, reg0, ":selected_faction"),
		])
		

		
		
		#script_get_poorest_village_of_faction
		# INPUT: arg1 = faction_no
		# OUTPUT: reg0 = village_no
get_poorest_village_of_faction = (
	"get_poorest_village_of_faction",
			[(store_script_param, ":faction_no", 1),
				(assign, ":min_prosperity_village", -1),
				(assign, ":min_prosperity", 101),
				(try_for_range, ":village_no", villages_begin, villages_end),
					(store_faction_of_party, ":village_faction", ":village_no"),
					(eq, ":village_faction", ":faction_no"),
					(party_get_slot, ":prosperity", ":village_no", slot_town_prosperity),
					(lt, ":prosperity", ":min_prosperity"),
					(assign, ":min_prosperity", ":prosperity"),
					(assign, ":min_prosperity_village", ":village_no"),
				(try_end),
				(assign, reg0, ":min_prosperity_village"),
		])
		
		# script_get_next_active_kingdom
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (does not choose player faction)
get_next_active_kingdom = (
	"get_next_active_kingdom",
			[
				(store_script_param, ":faction_no", 1),
				(assign, ":end_cond", kingdoms_end),
				(try_for_range, ":unused", kingdoms_begin, ":end_cond"),
					(val_add, ":faction_no", 1),
					(try_begin),
						(ge, ":faction_no", kingdoms_end),
						(assign, ":faction_no", kingdoms_begin),
					(try_end),
					(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
					(neq, ":faction_no", "fac_player_supporters_faction"),
					(assign, ":end_cond", 0),
				(try_end),
				(assign, reg0, ":faction_no"),
		])

#script_faction_conclude_feast
	#INPUT: faction no, venue
	#OUTPUT: nobility_in_attendance, nobility_in_faction
faction_conclude_feast = (
	"faction_conclude_feast",
		[
		(store_script_param, ":faction_no", 1),
		(store_script_param, ":venue", 2),
		
		(str_store_faction_name, s3, ":faction_no"),
		(str_store_party_name, s4, ":venue"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_s3_feast_concludes_at_s4"),
		(try_end),
		
		(try_begin),
			(eq, ":faction_no", "fac_player_faction"),
			(assign, ":faction_no", "$players_kingdom"),
		(try_end),
		
		(party_set_slot, ":venue", slot_town_has_tournament, 0),
		
		#markspot
		
		(assign, ":nobility_in_faction", 0),
		(assign, ":nobility_in_attendance", 0),
		
		(try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
			(store_faction_of_troop, ":troop_faction", ":troop_no"),
			(eq, ":faction_no", ":troop_faction"),
			
			(val_add, ":nobility_in_faction", 1),
			
			#CHECK -- is the troop there?
			(troop_slot_eq, ":troop_no", slot_troop_cur_center, ":venue"),
			(val_add, ":nobility_in_attendance", 1),
			
			#check for marriages
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
			(troop_get_slot, ":groom", ":troop_no", slot_troop_betrothed),
			(gt, ":groom", 0),
			
			(troop_get_slot, ":groom_party", ":groom", slot_troop_leaded_party),
			(party_is_active, ":groom_party"),
			(party_get_attached_to, ":groom_party_attached", ":groom_party"),
			(eq, ":groom_party_attached", ":venue"),
			
			(store_faction_of_troop, ":lady_faction", ":troop_no"),
			(store_faction_of_troop, ":groom_faction", ":groom"),
			
			(eq, ":groom_faction", ":lady_faction"),
			(eq, ":lady_faction", ":faction_no"),
			(store_current_hours, ":hours_since_betrothal"),
			(troop_get_slot, ":betrothal_time", ":troop_no", slot_troop_betrothal_time),
			(val_sub, ":hours_since_betrothal", ":betrothal_time"),
			(ge, ":hours_since_betrothal", 144), #6 days, should perhaps eventually be 29 days, or 696 yours
			
			(call_script, "script_get_kingdom_lady_social_determinants", ":troop_no"),
			(assign, ":wedding_venue", reg1),
			
			(eq, ":venue", ":wedding_venue"),
			(neq, ":troop_no", "trp_player"),
			(neq, ":groom", "trp_player"),
			
			(call_script, "script_courtship_event_bride_marry_groom", ":troop_no", ":groom", 0), #parameters from dialog
		(try_end),
		
		
		#ssss	(assign, ":placeholder_reminder_to_calculate_effect_for_player_feast", 1),
		
		
		
		(party_get_slot, ":feast_host", ":venue", slot_town_lord),
		(assign, ":quality_of_feast", 0),
		
		(try_begin),
			(check_quest_active, "qst_organize_feast"),
			(quest_slot_eq, "qst_organize_feast", slot_quest_target_center, ":venue"),
			(assign, ":feast_host", "trp_player"),
			
			(assign, ":total_guests", 400),
			
			(call_script, "script_succeed_quest", "qst_organize_feast"),
			(call_script, "script_end_quest", "qst_organize_feast"),
			
			(call_script, "script_internal_politics_rate_feast_to_s9", "trp_household_possessions", ":total_guests", "$players_kingdom", 1),
			(assign, ":quality_of_feast", reg0),
		(else_try),
			(assign, ":quality_of_feast", 60),
		(try_end),
		
		
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":feast_host"),
			(assign, reg4, ":quality_of_feast"),
			(display_message, "@{!}DEBUG - {s4}'s feast has rating of {reg4}"),
		(try_end),
		
		
		(try_begin),
			(ge, ":feast_host", 0),
			(store_div, ":renown_boost", ":quality_of_feast", 3),
			(call_script, "script_change_troop_renown", ":feast_host", ":renown_boost"),
			
			(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
			(party_is_active, ":leaded_party"),
			(party_get_attached_to, ":leaded_party_attached", ":leaded_party"),
			(eq, ":leaded_party_attached", ":venue"),
			
			(assign, ":relation_booster", ":quality_of_feast"),
			(val_div, ":relation_booster", 20),
			
			(try_begin),
				(eq, ":feast_host", "trp_player"),
				(val_sub, ":relation_booster", 1),
				(val_max, ":relation_booster", 0),
			(try_end),
			(call_script, "script_troop_change_relation_with_troop", ":feast_host", ":troop_no", ":relation_booster"),
			(val_add, "$total_feast_changes", ":relation_booster"),
			(try_end),
		(try_end),
		
		
		(assign, reg3, ":nobility_in_attendance"),
		(assign, reg4, ":nobility_in_faction"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_attendance_reg3_nobles_out_of_reg4"),
		(try_end),
	])


	#script_calculate_center_assailability_score
	# INPUT: faction_no
	# param1: faction_no
	# param2: all_vassals_included, (becomes 1 if we want to find attackable center if we collected 20% of vassals during gathering army phase)
	# OUTPUT:
	# reg0 = center_to_attack (-1 if none is logical)
	# reg1 = maximum_attack_score
calculate_center_assailability_score = (
	"calculate_center_assailability_score",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":potential_target", 2),
		(store_script_param, ":all_vassals_included", 3),
		
		(assign, ":target_score", -1),
		
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		
		(store_current_hours, ":hours_since_last_offensive"),
		(faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
		(val_sub, ":hours_since_last_offensive", ":last_offensive_time"),
		
		(store_div, ":last_offensive_time_score", ":hours_since_last_offensive", 12), #30..50
		(val_add, ":last_offensive_time_score", 30),
		(val_min, ":last_offensive_time_score", 100),
		
		(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
		
		(assign, ":marshal_party", -1),
		(assign, ":marshal_strength", 0),
		#(assign, ":strength_of_nearby_friend", 0),
		
		(try_begin),
			(gt, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
			(party_is_active, ":marshal_party"),
			(party_get_slot, ":marshal_strength", ":marshal_party", slot_party_cached_strength),
			#(eq, ":all_vassals_included", 0),
			(party_get_slot, ":strength_of_current_followers", ":marshal_party", slot_party_follower_strength),
			#(party_get_slot, ":strength_of_nearby_friend", ":marshal_party", slot_party_nearby_friend_strength),
		(try_end),
		
		#(try_begin),
		#  (eq, ":all_vassals_included", 0),
		#
		#  (try_begin),
		#    (gt, ":faction_marshal", 0),
		#    (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
		#    (party_is_active, ":marshal_party"),
		#    (party_get_slot, ":strength_of_potential_followers", ":marshal_party", slot_party_follower_strength),
		#  (try_end),
		#(else_try),
		#  (eq, ":all_vassals_included", 1),
		#
		#  (assign, ":strength_of_potential_followers", 0),
		#
		#  (try_for_parties, ":party_no"),
		#    (store_faction_of_party, ":party_faction", ":party_no"),
		#    (eq, ":party_faction", ":faction_no"),
		#    (neq, ":party_no", ":marshal_party"),
		#    (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
		#    (call_script, "script_party_calculate_strength", ":party_no", 0),
		#    (val_add, ":strength_of_potential_followers", reg0),
		#  (try_end),
		#
		#  (val_div, ":strength_of_potential_followers", 2), #Ozan - Think about this, will you divide strength_of_potential_followers to 3 or 2.5 or 2
		#(else_try),
		#  (assign, ":strength_of_potential_followers", 0),
		#(try_end),
		
		(faction_get_slot, ":last_attacked_center", ":faction_no", slot_faction_last_attacked_center),
		(faction_get_slot, ":last_attacked_hours", ":faction_no", slot_faction_last_attacked_hours),
		
		(try_begin),
			(store_current_hours, ":hours"),
			(store_add, ":last_attacked_hours_plus_24", ":last_attacked_hours", 24),
			(gt, ":hours", ":last_attacked_hours_plus_24"),
			(faction_set_slot, ":faction_no", slot_faction_last_attacked_center, 0),
			(assign, ":last_attacked_center", 0),
		(try_end),
		
		(try_begin),
			(this_or_next|eq, ":last_attacked_center", 0),
			(this_or_next|eq, ":last_attacked_center", ":potential_target"),
			(this_or_next|eq, "$g_do_not_skip_other_than_current_ai_object", 1),
			(neg|faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			
			(party_is_active, ":potential_target"),
			(store_faction_of_party, ":potential_target_faction", ":potential_target"),
			
			(store_relation, ":relation", ":potential_target_faction", ":faction_no"),
			(lt, ":relation", 0),
			
			#attack if and only if we are already besieging that center or anybody do not making besiege.
			(assign, ":faction_of_besieger_party", -1),
			(try_begin),
			(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
			(neg|party_slot_eq, ":potential_target", slot_center_is_besieged_by, -1),
			(party_get_slot, ":besieger_party", ":potential_target", slot_center_is_besieged_by),
			(party_is_active, ":besieger_party"),
			(store_faction_of_party, ":faction_of_besieger_party", ":besieger_party"),
			(try_end),
			
			(this_or_next|eq, ":faction_of_besieger_party", -1),
			(eq, ":faction_of_besieger_party", ":faction_no"),
			
			#attack if and only if this center is not a village or if it is village it should not be raided or looted
			(assign, ":village_is_looted_or_raided_already", 0),
			(try_begin),
			(is_between, ":potential_target", villages_begin, villages_end),
			(try_begin),
				(party_slot_eq, ":potential_target", slot_village_state, svs_being_raided),
				(party_get_slot, ":raider_party", ":potential_target", slot_village_raided_by),
				(party_is_active, ":raider_party"),
				
				(store_faction_of_party, ":raider_faction", ":raider_party"),
				(neq, ":raider_faction", ":faction_no"),
				(assign, ":raiding_by_one_other_faction", 1),
			(else_try),
				(assign, ":raiding_by_one_other_faction", 0),
			(try_end),
			(this_or_next|party_slot_eq, ":potential_target", slot_village_state, svs_looted),
			(eq, ":raiding_by_one_other_faction", 1),
			(assign, ":village_is_looted_or_raided_already", 1),
			(try_end),
			(eq, ":village_is_looted_or_raided_already", 0),
			
			#if ":potential_target" is faction object of some other faction which is enemy to owner of
			#":potential_target" then this target cannot be new target we are looking for.
			(assign, ":this_potantial_target_is_target_of_some_other_faction", 0),
			(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
			(is_between, ":cur_faction", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
			(neq, ":cur_faction", ":faction_no"),
			(faction_get_slot, ":faction_object", ":cur_faction", slot_faction_ai_object),
			(eq, ":faction_object", ":potential_target"),
			(store_relation, ":rel", ":potential_target_faction", ":cur_faction"),
			(lt, ":rel", 0),
			(assign, ":this_potantial_target_is_target_of_some_other_faction", 1),
			(try_end),
			(eq, ":this_potantial_target_is_target_of_some_other_faction", 0),
			
			(try_begin),
			(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
			(party_get_slot, ":potential_target_inside_strength", ":potential_target", slot_party_cached_strength),
			(party_get_slot, ":potential_target_nearby_enemy_strength", ":potential_target", slot_party_nearby_friend_strength),
			(val_div, ":potential_target_nearby_enemy_strength", 2),
			(store_add, ":potential_target_strength", ":potential_target_inside_strength", ":potential_target_nearby_enemy_strength"),
			
			#(try_begin),
			#(eq, ":faction_no", "fac_kingdom_4"),
			#(assign, reg0, ":potential_target_inside_strength"),
			#(assign, reg1, ":potential_target_nearby_enemy_strength"),
			#(assign, reg2, ":marshal_strength"),
			#(assign, reg3, ":strength_of_potential_followers"),
			#(assign, reg4, ":strength_of_nearby_friend"),
			#(assign, reg6, ":marshal_party"),
			#(str_store_party_name, s8, ":potential_target"),
			#(eq, ":all_vassals_included", 0),
			#(display_message, "@DEBUG : {s8}:{reg0}, neare {reg1}, our {reg2}, follow {reg3}, nearf {reg4}"),
			#(try_end),
			
			(val_mul, ":potential_target_strength", 4), #in walled centers defenders have advantage.
			(val_div, ":potential_target_strength", 3),
			
			#(store_add, ":army_strength", ":marshal_strength", ":strength_of_potential_followers"),
			(assign, ":army_strength", ":marshal_strength"),
			(val_add, ":army_strength", ":strength_of_current_followers"),
			(store_mul, ":power_ratio", ":army_strength", 100),
			
			#this ratio ":power_ratio" shows (our total army power) / (their total army power)
			(try_begin),
				(gt, ":potential_target_strength", 0),
				(val_div, ":power_ratio", ":potential_target_strength"),
			(else_try),
				(assign, ":power_ratio", 1000),
			(try_end),
			(else_try),
			(party_get_slot, ":potential_target_nearby_enemy_strength", ":potential_target", slot_party_nearby_friend_strength),
			(assign, ":potential_target_strength", 1000),
			
			#(store_add, ":army_strength", ":marshal_strength", ":strength_of_potential_followers"),
			(assign, ":army_strength", ":marshal_strength"),
			(val_add, ":army_strength", ":strength_of_current_followers"),
			(store_mul, ":power_ratio", ":army_strength", 100),
			
			(try_begin),
				(gt, ":potential_target_strength", 0),
				(val_div, ":power_ratio", ":potential_target_strength"),
			(else_try),
				(assign, ":power_ratio", 1000),
			(try_end),
			(try_end),
			
			(ge, ":power_ratio", 120), #attack if and only if our army is at least 1.2 times powerfull
			(store_sub, ":power_ratio_sub_120", ":power_ratio", 120),
			
			(try_begin),
			(lt, ":power_ratio_sub_120", 100), #changes between 20..120
			(store_add, ":power_ratio_score", ":power_ratio_sub_120", 20),
			(else_try),
			(lt, ":power_ratio_sub_120", 200), #changes between 120..170
			(store_sub, ":power_ratio_score", ":power_ratio_sub_120", 100),
			(val_div, ":power_ratio_score", 2),
			(val_add, ":power_ratio_score", 120),
			(else_try),
			(lt, ":power_ratio_sub_120", 400), #changes between 170..210
			(store_sub, ":power_ratio_score", ":power_ratio_sub_120", 200),
			(val_div, ":power_ratio_score", 5),
			(val_add, ":power_ratio_score", 170),
			(else_try),
			(lt, ":power_ratio_sub_120", 800), #changes between 210..250
			(store_sub, ":power_ratio_score", ":power_ratio_sub_120", 400),
			(val_div, ":power_ratio_score", 10),
			(val_add, ":power_ratio_score", 210),
			(else_try),
			(assign, ":power_ratio_score", 250),
			(try_end),
			
			(assign, ":number_of_walled_centers", 0),
			(assign, ":total_distance", 0),
			(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":walled_center_faction", ":walled_center"),
			(eq, ":walled_center_faction", ":faction_no"),
			
			(store_distance_to_party_from_party, ":dist", ":walled_center", ":potential_target"),
			(val_add, ":total_distance", ":dist"),
			
			(val_add, ":number_of_walled_centers", 1),
			(try_end),
			
			(try_begin),
			(gt, ":number_of_walled_centers", 0),
			(store_div, ":average_distance", ":total_distance", ":number_of_walled_centers"),
			#(assign, reg0, ":average_distance"),
			#(str_store_faction_name, s7, ":faction_no"),
			#(str_store_party_name, s8, ":potential_target"),
			#(display_message, "@average distance for {s7} for {s8} is {reg0}"),
			
			(try_begin),
				(ge, ":marshal_party", 0),
				(party_is_active, ":marshal_party"),
				(store_distance_to_party_from_party, ":marshal_dist_to_potential_target", ":marshal_party", ":potential_target"),
			(else_try),
				(assign, ":marshal_dist_to_potential_target", 100),
			(try_end),
			
			(try_begin),
				#if currently our target is attacking to an enemy center and that center is besieged/raided by one of our parties then
				#divide marshal_distance for other center's to "2" instead of "3" and add some small more distance to avoid easily
				#changing mind during siege because of small score differences.
				
				(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
				(eq, ":current_ai_state", sfai_attacking_center),
				(faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
				
				(ge, ":current_ai_object", 0),
				(neq, ":current_ai_object", ":potential_target"),
				
				(try_begin),
				(ge, ":power_ratio_score", 300), #200 max
				(assign, ":power_ratio_score", 200),
				(else_try),
				(ge, ":power_ratio_score", 100), #100..200
				(val_sub, ":power_ratio_score", 100),
				(val_div, ":power_ratio_score", 2),
				(val_add, ":power_ratio_score", 100),
				(try_end),
				
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
				(eq, "$g_do_not_skip_other_than_current_ai_object", 0),
				(assign, ":power_ratio_score", 0), #lets completely forget all other choices if we are already besieging one center.
				(try_end),
				
				(faction_set_slot, ":faction_no", slot_faction_last_attacked_center, ":current_ai_object"),
				(store_current_hours, ":hours"),
				(faction_set_slot, ":faction_no", slot_faction_last_attacked_hours, ":hours"),
				
				(eq, ":all_vassals_included", 0),
				
				(store_div, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target", 2),
				(assign, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target"),
			(else_try),
				(store_div, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target", 3),
			(try_end),
			
			(store_add, ":total_distance", ":average_distance", ":marshal_dist_to_potential_target_div_x"), #in average ":total_distance" is about 150, min : 0, max : 1000
			(else_try),
			(assign, ":total_distance", 100),
			(try_end),
			
			(try_begin),
			#according to cautious troop distance is more important
			
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			
			(try_begin),
				#(lt, ":total_distance", 30), #very close (100p)
				(lt, ":total_distance", 45), #rafi
				(assign, ":distance_score", 100),
			(else_try),
				#(lt, ":total_distance", 80), #close (50p-100p)
				(lt, ":total_distance", 120),#rafo
				#(store_sub, ":distance_score", ":total_distance", 30),
				(store_sub, ":distance_score", ":total_distance", 45), #rafi
				(val_div, ":distance_score", 1),
				(store_sub, ":distance_score", 100, ":distance_score"),
			(else_try),
				#(lt, ":total_distance", 160), #far (10p-50p)
				(lt, ":total_distance", 240), #rafi
				#(store_sub, ":distance_score", ":total_distance", 80),
				(store_sub, ":distance_score", ":total_distance", 120),
				(val_div, ":distance_score", 2),
				(store_sub, ":distance_score", 50, ":distance_score"),
			(else_try),
				(assign, ":distance_score", 10), #very far
			(try_end),
			(else_try),
			#according to agressive troop distance is less important
			
			(try_begin),
				#(lt, ":total_distance", 40), #very close (100p)
				(lt, ":total_distance", 60), #very close (100p)
				(assign, ":distance_score", 100),
			(else_try),
				#(lt, ":total_distance", 140), #close (50p-100p)
				(lt, ":total_distance", 210), #close (50p-100p)
				#(store_sub, ":distance_score", ":total_distance", 40),
				(store_sub, ":distance_score", ":total_distance", 60),
				(val_div, ":distance_score", 2),
				(store_sub, ":distance_score", 100, ":distance_score"),
			(else_try),
				#(lt, ":total_distance", 300), #far (10p-50p)
				(lt, ":total_distance", 450), #far (10p-50p)
				#(store_sub, ":distance_score", ":total_distance", 140),
				(store_sub, ":distance_score", ":total_distance", 210),
				(val_div, ":distance_score", 4),
				(store_sub, ":distance_score", 50, ":distance_score"),
			(else_try),
				(assign, ":distance_score", 10), #very far
			(try_end),
			(try_end),
			
			(store_mul, ":target_score", ":distance_score", ":power_ratio_score"),
			(val_mul, ":target_score", ":last_offensive_time_score"),
			(val_div, ":target_score", 100), #target score is between 0..10000 generally here
			
			(call_script, "script_find_total_prosperity_score", ":potential_target"),
			(assign, ":total_prosperity_score", reg0),
			
			#(try_begin), #new for increase attackability of villages by ai
			#(is_between, ":potential_target", villages_begin, villages_end),
			(val_mul, ":total_prosperity_score", 3),
			(val_div, ":total_prosperity_score", 2),
			#(try_end),
			
			(val_mul, ":target_score", ":total_prosperity_score"),
			
			(try_begin), #if both that center was our (original center) and (ex center) than bonus is 1.2x
			(party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
			(party_slot_eq, ":potential_target", slot_center_original_faction, ":faction_no"),
			(val_mul, ":target_score", 12),
			(val_div, ":target_score", 10),
			(else_try), #if either that center was our (original center) or (ex center) than bonus is 1.1x
			(this_or_next|party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
			(party_slot_eq, ":potential_target", slot_center_original_faction, ":faction_no"),
			(val_mul, ":target_score", 11),
			(val_div, ":target_score", 10),
			(try_end),
			
			(val_div, ":target_score", 1000), #target score is between 0..1000 generally here
			
			(try_begin),
			(eq, ":potential_target_faction", "fac_player_supporters_faction"),
			(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			
			(assign, ":number_of_walled_centers_player_have", 0),
			(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
				(store_faction_of_party, ":center_faction", ":center_no"),
				(eq, ":center_faction", "fac_player_supporters_faction"),
				(val_add, ":number_of_walled_centers_player_have", 1),
			(try_end),
			
			(try_begin),
				(eq, ":reduce_campaign_ai", 2), #easy
				
				(try_begin),
				(le, ":number_of_walled_centers_player_have", 2),
				(assign, ":hardness_score", 0),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 3),
				(assign, ":hardness_score", 20),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 4),
				(assign, ":hardness_score", 40),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 5),
				(eq, ":number_of_walled_centers_player_have", 6),
				(assign, ":hardness_score", 55),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 7),
				(eq, ":number_of_walled_centers_player_have", 8),
				(eq, ":number_of_walled_centers_player_have", 9),
				(assign, ":hardness_score", 70),
				(else_try),
				(assign, ":hardness_score", 85),
				(try_end),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #medium
				
				(try_begin),
				(le, ":number_of_walled_centers_player_have", 1),
				(assign, ":hardness_score", 25),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 2),
				(assign, ":hardness_score", 45),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 3),
				(assign, ":hardness_score", 60),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 4),
				(eq, ":number_of_walled_centers_player_have", 5),
				(assign, ":hardness_score", 75),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 6),
				(eq, ":number_of_walled_centers_player_have", 7),
				(eq, ":number_of_walled_centers_player_have", 8),
				(assign, ":hardness_score", 85),
				(else_try),
				(assign, ":hardness_score", 92),
				(try_end),
			(else_try), #hard
				(assign, ":hardness_score", 100),
			(try_end),
			
			(val_mul, ":target_score", ":hardness_score"),
			(val_div, ":target_score", 100),
			(try_end),
			
			#(try_begin),
			#  (eq, ":faction_no", "fac_kingdom_28"),
			#  (ge, ":target_score", -1),
			#  (assign, reg0, ":target_score"),
			#  (assign, reg7, ":total_prosperity_score"),
			#  (assign, reg8, ":power_ratio_score"),
			#  (assign, reg9, ":distance_score"),
			#  (assign, reg10, ":last_offensive_time_score"),
			#  (str_store_party_name, s8, ":potential_target"),
			#  #(eq, ":all_vassals_included", 0),
			#  (assign, reg11, ":all_vassals_included"),
			#(try_end),
		(try_end),
		
		(assign, reg0, ":target_score"),
		(assign, reg1, ":power_ratio"),
		(assign, reg2, ":distance_score"),
		(assign, reg3, ":total_prosperity_score"),
	])
	

	#script_find_center_to_defend
	# INPUT:
	# param1: faction_no
	# OUTPUT:
	# reg0 = center_to_defend (-1 if none is logical)
	# reg1 = maximum_defend_score
	# reg3 = enemy_strength_near_most_threatened_center
find_center_to_defend = (
	"find_center_to_defend",
		[
		(store_script_param, ":troop_no", 1),
		
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		
		(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
		(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
		(assign, ":marshal_party", -1),
		(try_begin),
			(gt, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
		(try_end),
		
		(assign, ":most_threatened_center", -1),
		(assign, ":maximum_threat_score", 0),
		(try_for_range, ":cur_center", centers_begin, centers_end),
		#(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end), #tom
			(store_faction_of_party, ":center_faction", ":cur_center"),
			(eq, ":center_faction", ":faction_no"),
			
			(party_get_slot, ":exact_enemy_strength", ":cur_center", slot_center_sortie_enemy_strength),
			#Distort this to account for questionable intelligence
			#(call_script, "script_reduce_exact_number_to_estimate", ":exact_enemy_strength"),
			#(assign, ":enemy_strength_nearby", reg0),
			(assign, ":enemy_strength_nearby", ":exact_enemy_strength"),
			
			(assign, ":threat_importance", 0),
			(try_begin),
			(is_between, ":cur_center", walled_centers_begin, walled_centers_end),
			(party_slot_ge, ":cur_center", slot_center_is_besieged_by, 0),
			
			(call_script, "script_find_total_prosperity_score", ":cur_center"),
			(assign, ":total_prosperity_score", reg0),
			
			(party_get_slot, ":cur_center_strength", ":cur_center", slot_party_cached_strength),
			(val_mul, ":cur_center_strength", 4),
			(val_div, ":cur_center_strength", 3), #give 33% bonus to insiders because they are inside a castle
			
			#I removed below line and assigned ":cur_center_nearby_strength" to 0, because if not when defender army comes to help
			#threat become less because of high defence power but not yet enemy cleared.
			#(party_get_slot, ":cur_center_nearby_strength", ":cur_center", slot_party_nearby_friend_strength),
			(assign, ":cur_center_nearby_strength", 0),
			
			(val_add, ":cur_center_strength", ":cur_center_nearby_strength"), #add nearby friends and find ":cur_center_strength"
			
			(store_mul, ":power_ratio", ":enemy_strength_nearby", 100),
			(val_add, ":cur_center_strength", 1),
			(val_max, ":cur_center_strength", 1),
			(val_div, ":power_ratio", ":cur_center_strength"),
			
			(assign, ":player_is_attacking", 0),
			(party_get_slot, ":besieger_party", ":cur_center", slot_center_is_besieged_by),
			(try_begin),
				(party_is_active, ":besieger_party"),
				(try_begin),
				(eq, ":besieger_party", "p_main_party"),
				(assign, ":player_is_attacking", 1),
				#(display_message, "@{!}DEBUG : player is attacking a center (1)"),
				(else_try),
				(store_faction_of_party, ":besieger_faction", ":besieger_party"),
				(eq, ":besieger_faction", "fac_player_faction"),
				(assign, ":player_is_attacking", 1),
				#(display_message, "@{!}DEBUG : player is attacking a center (2)"),
				(else_try),
				(party_get_attached_to, ":player_is_attached_to", "p_main_party"),
				(ge, ":player_is_attached_to", 0),
				(eq, ":player_is_attached_to", ":besieger_party"),
				(assign, ":player_is_attacking", 1),
				#(display_message, "@{!}DEBUG : player is attacking a center (3)"),
				(try_end),
			(try_end),
			
			(try_begin),
				(eq, ":player_is_attacking", 0),
				
				(try_begin),
				(lt, ":power_ratio", 40), #changes between 1..1
				(assign, ":threat_importance", 1),
				(else_try),
				(lt, ":power_ratio", 80), #changes between 1..7
				(store_sub, ":threat_importance", ":power_ratio", 40),
				(val_div, ":threat_importance", 5),
				(val_add, ":threat_importance", 1), #1
				(else_try),
				(lt, ":power_ratio", 120), #changes between 7..17
				(store_sub, ":threat_importance", ":power_ratio", 80),
				(val_div, ":threat_importance", 4),
				(val_add, ":threat_importance", 7), #1 + 6
				(else_try),
				(lt, ":power_ratio", 200),
				(store_sub, ":threat_importance", ":power_ratio", 120),
				(val_div, ":threat_importance", 10),
				(val_add, ":threat_importance", 17), #1 + 6 + 10
				(else_try),
				(assign, ":threat_importance", 25),
				(try_end),
			(else_try),
				(try_begin),
				(lt, ":power_ratio", 200), #changes between 5..25
				(store_div, ":threat_importance", ":power_ratio", 10),
				(val_add, ":threat_importance", 6 ),
				(else_try),
				(assign, ":threat_importance", 26),
				(try_end),
			(try_end),
			(else_try),
			(is_between, ":cur_center", villages_begin, villages_end),
			(party_slot_eq, ":cur_center", slot_village_state, svs_being_raided),
			
			(gt, ":enemy_strength_nearby", 0),
			
			(call_script, "script_find_total_prosperity_score", ":cur_center"),
			(assign, ":power_ratio", 100), #useless
			(assign, ":total_prosperity_score", reg0),
			(assign, ":threat_importance", 10), #if faction village is looted they lose money for shorter time period. So importance is something low (6-8).
			(try_end),
			
			(gt, ":threat_importance", 0),
			
			(try_begin),
			(is_between, ":cur_center", walled_centers_begin, walled_centers_end),
			(assign, ":enemy_strength_nearby_score", 120),
			
			(try_begin),
				(ge, ":marshal_party", 0),
				(party_is_active, ":marshal_party"),
				(store_distance_to_party_from_party, ":marshal_dist_to_cur_center", ":marshal_party", ":cur_center"),
			(else_try),
				(assign, ":marshal_dist_to_cur_center", 100),
			(try_end),
			
			(try_begin),
				#if currently our target is ride to break a siege then
				#divide marshal_distance for other center's to "2" instead of "4" and add some small more distance to avoid easily
				#changing mind during siege because of small score differences.
				
				#(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
				(eq, ":current_ai_state", sfai_attacking_enemies_around_center),
				(faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
				(is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
				(neq, ":current_ai_object", ":cur_center"),
				(val_mul, ":marshal_dist_to_cur_center", 2),
				(val_add, ":marshal_dist_to_cur_center", 20),
			(try_end),
			
			(val_mul, ":marshal_dist_to_cur_center", 2), #standard multipication (1.5x) to adjust distance scoring same with formula at find_center_to_attack
			#(val_div, ":marshal_dist_to_cur_center", 2),
			
			(try_begin),
				(lt, ":marshal_dist_to_cur_center", 10), #very close (100p)
				(assign, ":distance_score", 100),
			(else_try),
				(lt, ":marshal_dist_to_cur_center", 160), #close (50p-100p)
				(store_sub, ":distance_score", ":marshal_dist_to_cur_center", 10),
				(val_div, ":distance_score", 3),
				(store_sub, ":distance_score", 100, ":distance_score"),
			(else_try),
				(lt, ":marshal_dist_to_cur_center", 360), #far (10p-50p)
				(store_sub, ":distance_score", ":marshal_dist_to_cur_center", 250),
				(val_div, ":distance_score", 5),
				(store_sub, ":distance_score", 50, ":distance_score"),
			(else_try),
				(assign, ":distance_score", 10), #very far
			(try_end),
			(else_try),
			(store_add, ":enemy_strength_nearby_score", ":enemy_strength_nearby", 20000),
			(val_div, ":enemy_strength_nearby_score", 200),
			(assign, ":distance_score", 70), #not related to marshal's position, because everybody is going same place (no gathering in most village raids)
			(try_end),
			
			(store_mul, ":threat_score", ":enemy_strength_nearby_score", ":total_prosperity_score"),
			(val_mul, ":threat_score", ":threat_importance"),
			(val_mul, ":threat_score", ":distance_score"),
			(val_div, ":threat_score", 10000),
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(gt, ":threat_score", 0),
			(eq, ":faction_no", "fac_kingdom_6"),
			(assign, reg0, ":threat_score"),
			(str_store_party_name, s32, ":cur_center"),
			(assign, reg1,  ":total_prosperity_score"),
			(assign, reg2, ":enemy_strength_nearby_score"),
			(assign, reg3, ":threat_importance"),
			(assign, reg4, ":distance_score"),
			#(display_message, "@{!}DEBUG : defend of {s32} is {reg0}, prosperity:{reg1}, enemy nearby:{reg2}, threat importance:{reg3}, distance: {reg4}"),
			(try_end),
			
			(gt, ":threat_score", ":maximum_threat_score"),
			
			(assign, ":most_threatened_center", ":cur_center"),
			(assign, ":maximum_threat_score", ":threat_score"),
			(assign, ":enemy_strength_near_most_threatened_center", ":enemy_strength_nearby"),
		(try_end),
		
		(val_mul, ":maximum_threat_score", 3),
		(val_div, ":maximum_threat_score", 2),
		
		(assign, reg0, ":most_threatened_center"),
		(assign, reg1, ":maximum_threat_score"),
		(assign, reg2, ":enemy_strength_near_most_threatened_center"),
	])


	#script_diplomacy_faction_get_diplomatic_status_with_faction
	#INPUT: actor_faction, target_faction
	#OUTPUT: result, duration

diplomacy_faction_get_diplomatic_status_with_faction =	(
	"diplomacy_faction_get_diplomatic_status_with_faction",
		#result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
		[
		(store_script_param, ":actor_faction", 1),
		(store_script_param, ":target_faction", 2),
		
		(store_add, ":truce_slot", ":target_faction", slot_faction_truce_days_with_factions_begin),
		(store_add, ":provocation_slot", ":target_faction", slot_faction_provocation_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
		(val_sub, ":provocation_slot", kingdoms_begin),
		
		(assign, ":result", 0),
		(assign, ":duration", 0),
		
		(try_begin),
			(store_relation, ":relation", ":actor_faction", ":target_faction"),
			(lt, ":relation", 0),
			(assign, ":result", -2),
		(else_try),
			(faction_slot_ge, ":actor_faction", ":truce_slot", 1),
			(assign, ":result", 1),
			
			(faction_get_slot, ":duration", ":actor_faction", ":truce_slot"),
		(else_try),
			(faction_slot_ge, ":actor_faction", ":provocation_slot", 1),
			(assign, ":result", -1),
			
			(faction_get_slot, ":duration", ":actor_faction", ":provocation_slot"),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":duration"),
	])

	#script_faction_get_adjective_to_s10
	#INPUT: faction_no
	#OUTPUT: s10 adjective_string
faction_get_adjective_to_s10 = (
	"faction_get_adjective_to_s10",
		[
		(store_script_param, ":faction_no", 1),
		
		(try_begin),
			(eq, ":faction_no", "fac_player_faction"),
			(assign, ":faction_no", "$players_kingdom"),
		(try_end),
		
		
		(try_begin),
			(eq, ":faction_no", "fac_player_supporters_faction"),
			(str_store_string, s10, "str_rebel"),
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_outlaws"),
			(this_or_next|eq, ":faction_no", "fac_mountain_bandits"),
			(this_or_next|eq, ":faction_no", "fac_forest_bandits"),
			(eq, ":faction_no", "fac_deserters"),
			(str_store_string, s10, "str_bandit"),
		(else_try),
			(faction_get_slot, ":adjective_string", ":faction_no", slot_faction_adjective),
			(str_store_string, s10, ":adjective_string"),
		(try_end),
	])

	#script_faction_last_reconnoitered_center
	#This is called from within decide_faction_ai, or from (modded2x: wat?)
	#INPUT: faction_no, center_no
	#OUTPUT: hours_since_last_recon, last_recon_time
faction_last_reconnoitered_center = (
	"faction_last_reconnoitered_center", #This is called from within decide_faction_ai, or from
		[
		(store_script_param, ":faction_no", 1),
		(store_script_param, ":center_no", 2),
		
		(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
		(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
		(store_current_hours, ":hours_since_last_recon"),
		(party_get_slot, ":last_recon_time", ":center_no", ":faction_recce_slot"),
		
		(try_begin),
			(lt, ":last_recon_time", 1),
			(assign, ":hours_since_last_recon", 1000),
		(else_try),
			(val_sub, ":hours_since_last_recon", ":last_recon_time"),
		(try_end),
		
		(assign, reg0, ":hours_since_last_recon"),
		(assign, reg1, ":last_recon_time"),
	])

	#script_find_center_to_attack_alt
	#INPUT: troop_no, attack_by_faction, all_vassals_included
	#OUTPUT: result, score_to_beat
find_center_to_attack_alt =	(
	"find_center_to_attack_alt",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":attack_by_faction", 2),
		(store_script_param, ":all_vassals_included", 3),
		
		(assign, ":result", -1),
		(assign, ":score_to_beat", 0),
		
		(try_for_range, ":center_no", centers_begin, centers_end),
			(call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack",	":troop_no", ":center_no", ":attack_by_faction", ":all_vassals_included"),
			(assign, ":score", reg0),
			
			(gt, ":score", ":score_to_beat"),
			
			(assign, ":result", ":center_no"),
			(assign, ":score_to_beat", ":score"),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":score_to_beat"),
	])
