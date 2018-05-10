from header import *


	#script_dplmc_get_item_buy_price_factor
	#INPUT: item_kind_id, center_no
	#OUTPUT: price_factor
dplmc_get_item_buy_price_factor = (
	"dplmc_get_item_buy_price_factor",
		[
		(store_script_param_1, ":item_kind_id"),
		(store_script_param_2, ":center_no"),
		(assign, ":price_factor", 100),
		
		(call_script, "script_get_trade_penalty", ":item_kind_id"),
		(assign, ":trade_penalty", reg0),
		
		(try_begin),
			(is_between, ":center_no", centers_begin, centers_end),
			(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
			(store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
			(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
			(party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),
			
			(try_begin),
			(is_between, ":center_no", villages_begin, villages_end),
			(party_get_slot, ":market_town", ":center_no", slot_village_market_town),
			(party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
			(val_max, ":price_factor", ":price_in_market_town"),
			(try_end),
			
			#For villages, the good will be sold no cheaper than in the market town
			#This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers
			
			(val_mul, ":price_factor", 100), #normalize price factor to range 0..100
			(val_div, ":price_factor", average_price_factor),
		(try_end),
		
		(store_add, ":penalty_factor", 100, ":trade_penalty"),
		
		(val_mul, ":price_factor", ":penalty_factor"),
		(val_div, ":price_factor", 100),
		
		(assign, reg0, ":price_factor"),
		(set_trigger_result, reg0),
	])


	#script_dplmc_get_prisoners_value_between_factions
	# Input: arg1 = faction_no_1, arg2 = faction_no_2
	# Output: faction_no_1 - faction_no_2
dplmc_get_prisoners_value_between_factions = (
	"dplmc_get_prisoners_value_between_factions",
		[
		(store_script_param, ":faction_no_1", 1),
		(store_script_param, ":faction_no_2", 2),
		
		(assign, ":faction_no_1_value", 0),
		(assign, ":faction_no_2_value", 0),
		
		(try_for_parties, ":party_no"),
			(store_faction_of_party, ":party_faction", ":party_no"),
			(try_begin),
			(eq, ":party_faction", ":faction_no_1"),
			(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
			(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
				(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
				(store_troop_faction, ":cur_faction", ":cur_troop_id"),
				
				(eq, ":cur_faction", ":faction_no_2"),
				(try_begin),
				(troop_is_hero, ":cur_troop_id"),
				(call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
				(val_add, ":faction_no_1_value", reg0),
				
				(try_begin),#debug
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":faction_no_1_value"),
					(display_message, "@{!}DEBUG : faction_no_1_value: {reg0}"),
				(try_end),
				
				(try_end),
			(try_end),
			(else_try),
			(eq, ":party_faction", ":faction_no_2"),
			(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
			(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
				(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
				(store_troop_faction, ":cur_faction", ":cur_troop_id"),
				
				(eq, ":cur_faction", ":faction_no_1"),
				(try_begin),
				(troop_is_hero, ":cur_troop_id"),
				(call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
				(val_add, ":faction_no_2_value", reg0),
				
				(try_begin), #debug
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":faction_no_2_value"),
					(display_message, "@{!}DEBUG : faction_no_2_value: {reg0}"),
				(try_end),
				
				(try_end),
			(try_end),
			(try_end),
		(try_end),
		(store_sub, reg0, ":faction_no_1_value", ":faction_no_2_value"),
	])
	

	#script_dplmc_get_truce_pay_amount
	# Input: arg1 = faction_no_1, arg2 = faction_no_2
	# Output: concession_value
dplmc_get_truce_pay_amount = (
	"dplmc_get_truce_pay_amount",
		[
		(store_script_param, ":faction_no_1", 1),
		(store_script_param, ":faction_no_2", 2),
		(store_script_param, ":check_peace_war_result", 3),
		
		(assign, ":peace_war_param", 1000),
		(assign, ":concession_param", 3000), #value of a concession
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":check_peace_war_result"), #debug
			(display_message, "@{!}DEBUG : peace_war_result: {reg0}"),#debug
		(try_end),
		
		(val_sub, ":check_peace_war_result", 1),
		(val_mul, ":check_peace_war_result", 4),
		(val_mul, ":check_peace_war_result", ":peace_war_param"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":check_peace_war_result"), #debug
			(display_message, "@{!}DEBUG : peace_war_result after multi: {reg0}"),#debug
		(try_end),
		
		(call_script, "script_dplmc_get_prisoners_value_between_factions", ":faction_no_1", ":faction_no_2"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : prisonser_value: {reg0}"),#debug
		(try_end),
		
		(val_sub, ":check_peace_war_result", reg0),
		(val_max, ":check_peace_war_result", 0),
		(assign, reg0, ":check_peace_war_result"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : peace_war_result after prisoners: {reg0}"),#debug
		(try_end),
		
		(assign, reg1, -1),
		(try_begin),
			(gt, "$g_concession_demanded", 0),
			(assign, ":concession_value", 2),
			(try_begin),
			(is_between, "$g_concession_demanded", towns_begin, towns_end),
			(assign, ":concession_value", 3),
			(else_try),
			(is_between, "$g_concession_demanded", castles_begin, castles_end),
			(assign, ":concession_value", 2),
			(else_try),
			(is_between, "$g_concession_demanded", villages_begin, villages_end),
			(assign, ":concession_value", 1),
			(try_end),
			(val_mul, ":concession_value", ":concession_param"),
			
			(store_sub, reg1, reg0, ":concession_value"), #reg4 = reg3 - concession_value
			(val_max, reg1, 0),
		(try_end),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : truce_pay_amount0: {reg0}"),
			(display_message, "@{!}DEBUG : truce_pay_amount1: {reg1}"),
		(try_end),
	])
	
