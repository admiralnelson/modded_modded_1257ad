from header import -

#script_cf_select_random_town_with_faction:
		# This script selects a random town in range [towns_begin, towns_end)
		# such that faction of the town is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no
		("cf_select_random_town_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				# First count num matching spawn points
				(assign, ":no_towns", 0),
				(try_for_range,":cur_town", towns_begin, towns_end),
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(eq, ":cur_faction", ":faction_no"),
					(val_add, ":no_towns", 1),
				(try_end),
				(gt, ":no_towns", 0), #Fail if there are no towns
				(store_random_in_range, ":random_town", 0, ":no_towns"),
				(assign, ":no_towns", 0),
				(try_for_range,":cur_town", towns_begin, towns_end),
					(eq, ":result", -1),
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(eq, ":cur_faction", ":faction_no"),
					(val_add, ":no_towns", 1),
					(gt, ":no_towns", ":random_town"),
					(assign, ":result", ":cur_town"),
				(try_end),
				(assign, reg0, ":result"),
		]),
		
		#script_cf_select_random_village_with_faction:
		# This script selects a random village in range [villages_begin, villages_end)
		# such that faction of the village is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching village.
		# reg0 = village_no
		("cf_select_random_village_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				# First count num matching spawn points
				(assign, ":no_villages", 0),
				(try_for_range,":cur_village", villages_begin, villages_end),
					(store_faction_of_party, ":cur_faction", ":cur_village"),
					(eq, ":cur_faction", ":faction_no"),
					(val_add, ":no_villages", 1),
				(try_end),
				(gt, ":no_villages", 0), #Fail if there are no villages
				(store_random_in_range, ":random_village", 0, ":no_villages"),
				(assign, ":no_villages", 0),
				(try_for_range,":cur_village", villages_begin, villages_end),
					(eq, ":result", -1),
					(store_faction_of_party, ":cur_faction", ":cur_village"),
					(eq, ":cur_faction", ":faction_no"),
					(val_add, ":no_villages", 1),
					(gt, ":no_villages", ":random_village"),
					(assign, ":result", ":cur_village"),
				(try_end),
				(assign, reg0, ":result"),
		]),

		#script_cf_select_random_walled_center_with_faction:
		# This script selects a random center in range [centers_begin, centers_end)
		# such that faction of the town is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		# arg2 = preferred_center_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no (Can fail)
		("cf_select_random_walled_center_with_faction",
			[
				(store_script_param, ":faction_no", 1),
				(store_script_param, ":preferred_center_no", 2),
				(assign, ":result", -1),
				# First count num matching spawn points
				(assign, ":no_centers", 0),
				(try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":cur_faction", ":cur_center"),
					(eq, ":cur_faction", ":faction_no"),
					(val_add, ":no_centers", 1),
					(eq, ":cur_center", ":preferred_center_no"),
					(val_add, ":no_centers", 99),
				(try_end),
				(gt, ":no_centers", 0), #Fail if there are no centers
				(store_random_in_range, ":random_center", 0, ":no_centers"),
				(try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
					(eq, ":result", -1),
					(store_faction_of_party, ":cur_faction", ":cur_center"),
					(eq, ":cur_faction", ":faction_no"),
					(val_sub, ":random_center", 1),
					(try_begin),
						(eq, ":cur_center", ":preferred_center_no"),
						(val_sub, ":random_center", 99),
					(try_end),
					(lt, ":random_center", 0),
					(assign, ":result", ":cur_center"),
				(try_end),
				(assign, reg0, ":result"),
		]),
		
		
	#script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege:
	# INPUT:
	# arg1 = faction_no
	# arg2 = owner_troop_no
	#OUTPUT:
	# This script may return false if there is no matching town.
	# reg0 = center_no (Can fail)
	("cf_select_random_walled_center_with_faction_and_owner_priority_no_siege",
		[
			(store_script_param, ":faction_no", 1),
			(store_script_param, ":troop_no", 2),
			(assign, ":result", -1),
			(assign, ":no_centers", 0),
			
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			
			(try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
				(store_faction_of_party, ":cur_faction", ":cur_center"),
				(eq, ":cur_faction", ":faction_no"),
				(party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
				(val_add, ":no_centers", 1),
				
				#(party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
				(eq, ":home_center", ":cur_center"), #I changed it with above line, now if lord is owner of any village its bound walled center is counted as 1000. Better this way. ozan-18.01.09
				
				(val_add, ":no_centers", 1000),
			(try_end),

		#if no center is available count all centers not besieged do not care its faction.
		(try_begin),
				(le, ":no_centers", 0), 

		(assign, "$g_there_is_no_avaliable_centers", 1),

				(try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
				(party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
					(val_add, ":no_centers", 1),                                   
				(try_end),
		(else_try),
			(assign, "$g_there_is_no_avaliable_centers", 0),
		(try_end),

			(faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
		(this_or_next|eq, "$g_there_is_no_avaliable_centers", 0),
			(neq, ":troop_no", ":faction_leader"), #faction leaders cannot spawn if they have no centers.

			(store_random_in_range, ":random_center", 0, ":no_centers"),
			(try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
				(eq, ":result", -1),
				(store_faction_of_party, ":cur_faction", ":cur_center"),
		(this_or_next|eq, "$g_there_is_no_avaliable_centers", 1),
				(eq, ":cur_faction", ":faction_no"),
				(party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
				(val_sub, ":random_center", 1),
				(try_begin),
					#(party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
					(eq, ":home_center", ":cur_center"), #I changed it with above line, now if lord is owner of any village its bound walled center is counted as 1000. Better this way. ozan-18.01.09
			(eq, "$g_there_is_no_avaliable_centers", 0),

					(val_sub, ":random_center", 1000),
				(try_end),
				(lt, ":random_center", 0),
				(assign, ":result", ":cur_center"),
			(try_end),
			(assign, reg0, ":result"),
	]),

	#script_cf_select_random_walled_center_with_faction_and_less_strength_priority:
		# This script selects a random center in range [centers_begin, centers_end)
		# such that faction of the town is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		# arg2 = preferred_center_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no (Can fail)
		("cf_select_random_walled_center_with_faction_and_less_strength_priority",
			[
				(store_script_param, ":faction_no", 1),
				(store_script_param, ":preferred_center_no", 2),
				(assign, ":result", -1),
				# First count num matching spawn points
				(assign, ":no_centers", 0),
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":cur_faction", ":cur_center"),
					(eq, ":cur_faction", ":faction_no"),
					(party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
					(val_add, ":no_centers", 1),
					(try_begin),
						(eq, ":cur_center", ":preferred_center_no"),
						(val_add, ":no_centers", 99),
					(try_end),
					##        (call_script, "script_party_calculate_regular_strength", ":cur_center"),
					##        (assign, ":strength", reg0),
					##        (lt, ":strength", 80),
					##        (store_sub, ":strength", 100, ":strength"),
					##        (val_div, ":strength", 20),
					##        (val_add, ":no_centers", ":strength"),
				(try_end),
				(gt, ":no_centers", 0), #Fail if there are no centers
				(store_random_in_range, ":random_center", 0, ":no_centers"),
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(eq, ":result", -1),
					(store_faction_of_party, ":cur_faction", ":cur_center"),
					(eq, ":cur_faction", ":faction_no"),
					(party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
					(val_sub, ":random_center", 1),
					(try_begin),
						(eq, ":cur_center", ":preferred_center_no"),
						(val_sub, ":random_center", 99),
					(try_end),
					##        (try_begin),
					##          (call_script, "script_party_calculate_regular_strength", ":cur_center"),
					##          (assign, ":strength", reg0),
					##          (lt, ":strength", 80),
					##          (store_sub, ":strength", 100, ":strength"),
					##          (val_div, ":strength", 20),
					##          (val_sub, ":random_center", ":strength"),
					##        (try_end),
					(lt, ":random_center", 0),
					(assign, ":result", ":cur_center"),
				(try_end),
				(assign, reg0, ":result"),
		]),

		#script_cf_select_random_town_at_peace_with_faction:
		# This script selects a random town in range [towns_begin, towns_end)
		# such that faction of the town is friendly to given_faction
		# INPUT:
		# arg1 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no
		("cf_select_random_town_at_peace_with_faction",
			[
				(store_script_param_1, ":faction_no"),
				(assign, ":result", -1),
				# First count num matching towns
				(assign, ":no_towns", 0),
				(try_for_range,":cur_town", towns_begin, towns_end),
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(store_relation,":reln", ":cur_faction", ":faction_no"),
					(ge, ":reln", 0),
					(val_add, ":no_towns", 1),
				(try_end),
				(gt, ":no_towns", 0), #Fail if there are no towns
				(store_random_in_range, ":random_town", 0, ":no_towns"),
				(assign, ":no_towns", 0),
				(try_for_range,":cur_town", towns_begin, towns_end),
					(eq, ":result", -1),
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(store_relation,":reln", ":cur_faction", ":faction_no"),
					(ge, ":reln", 0),
					(val_add, ":no_towns", 1),
					(gt, ":no_towns", ":random_town"),
					(assign, ":result", ":cur_town"),
				(try_end),
				(assign, reg0, ":result"),
		]),


		#script_cf_select_random_town_at_peace_with_faction_in_trade_route
		# INPUT:
		# arg1 = town_no
		# arg2 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no
		("cf_select_random_town_at_peace_with_faction_in_trade_route",
			[
				(store_script_param, ":town_no", 1),
				(store_script_param, ":faction_no", 2),
				(assign, ":result", -1),
				(assign, ":no_towns", 0),
				(try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
					(party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
					(gt, ":cur_town", 0),
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(store_relation, ":reln", ":cur_faction", ":faction_no"),
					(ge, ":reln", 0),
					(val_add, ":no_towns", 1),
				(try_end),
				(gt, ":no_towns", 0), #Fail if there are no towns
				(store_random_in_range, ":random_town", 0, ":no_towns"),
				(try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
					(eq, ":result", -1),
					(party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
					(gt, ":cur_town", 0),
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(store_relation, ":reln", ":cur_faction", ":faction_no"),
					(ge, ":reln", 0),
					(val_sub, ":random_town", 1),
					(lt, ":random_town", 0),
					(assign, ":result", ":cur_town"),
				(try_end),
				(assign, reg0, ":result"),
		]),

		#the following is a very simple adjustment - it measures the difference in prices between two towns
		#all goods are weighted equally except for luxuries
		#it does not take into account the prices of the goods, nor cargo capacity
		#to do that properly, a merchant would have to virtually fill his baggage, slot by slot, for each town
		#i also found that one needed to introduce demand inelasticity -- prices should vary a lot for grain,  relatively little for iron
		
		("cf_select_most_profitable_town_at_peace_with_faction_in_trade_route",
			[
				(store_script_param, ":town_no", 1),
				(store_script_param, ":faction_no", 2),
				
				(assign, ":result", -1),
				(assign, ":best_town_score", 0),
				(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
				
				(try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
					(party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
					(gt, ":cur_town", 0),
					
					(store_faction_of_party, ":cur_faction", ":cur_town"),
					(store_relation, ":reln", ":cur_faction", ":faction_no"),
					(ge, ":reln", 0),
					
					(assign, ":cur_town_score", 0),
					(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
						(neq, ":cur_goods", "itm_butter"), #Don't count perishables
						(neq, ":cur_goods", "itm_cattle_meat"),
						(neq, ":cur_goods", "itm_chicken"),
						(neq, ":cur_goods", "itm_pork"),
						
						(store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
						(party_get_slot, ":origin_price", ":town_no", ":cur_goods_price_slot"),
						(party_get_slot, ":destination_price", ":cur_town", ":cur_goods_price_slot"),
						
						(gt, ":destination_price", ":origin_price"),
						(store_sub, ":price_dif", ":destination_price", ":origin_price"),
						
						(try_begin), #weight luxury goods double
							(this_or_next|eq, ":cur_goods", "itm_spice"),
							(eq, ":cur_goods", "itm_velvet"),
							(val_mul, ":price_dif", 2),
						(try_end),
						(val_add, ":cur_town_score", ":price_dif"),
					(try_end),
					
					##		(try_begin),
					##			(eq, "$cheat_mode", 1),
					##			(str_store_party_name, s10, ":town_no"),
					##			(str_store_party_name, s11, ":cur_town"),
					##			(assign, reg3, ":cur_town_score"),
					##			(display_message, "str_caravan_in_s10_considers_s11_total_price_dif_=_reg3"),
					##		(try_end),
					
					(gt, ":cur_town_score", ":best_town_score"),
					(assign, ":best_town_score", ":cur_town_score"),
					(assign, ":result", ":cur_town"),
					
				(try_end),
				
				(gt, ":result", -1), #Fail if there are no towns
				
				(assign, reg0, ":result"),
				
				#	  (store_current_hours, ":hour"),
				#	  (party_set_slot, ":result", slot_town_caravan_last_visit, ":hour"),
				
				##	  (try_begin),
				##		(eq, "$cheat_mode", 1),
				##	    (assign, reg3, ":best_town_score"),
				##	    (str_store_party_name, s3, ":town_no"),
				##	    (str_store_party_name, s4, ":result"),
				##	    (display_message, "str_test__caravan_in_s3_selects_for_s4_trade_score_reg3"),
				##	  (try_end),
				
		]),