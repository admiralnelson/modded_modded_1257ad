from header import *

# script_get_percentage_with_randomized_round
		# Input: arg1 = value, arg2 = percentage
		# Output: reg0 result percentage with randomised round
get_percentage_with_randomized_round =	(
	"get_percentage_with_randomized_round",
			[
				(store_script_param, ":value", 1),
				(store_script_param, ":percentage", 2),
				
				(store_mul, ":result", ":value", ":percentage"),
				(val_div, ":result", 100),
				(store_mul, ":used_amount", ":result", 100),
				(val_div, ":used_amount", ":percentage"),
				(store_sub, ":left_amount", ":value", ":used_amount"),
				(try_begin),
					(gt, ":left_amount", 0),
					(store_mul, ":chance", ":left_amount", ":percentage"),
					(store_random_in_range, ":random_no", 0, 100),
					(lt, ":random_no", ":chance"),
					(val_add, ":result", 1),
				(try_end),
				(assign, reg0, ":result"),
		])


		# script_round_value
		# really? the power of talesworlds's ""scripting engine""
		# Input: arg1 = value
		# Output: reg0 = rounded_value
round_value = (
	"round_value",
			[
				(store_script_param_1, ":value"),
				(try_begin),
					(lt, ":value", 100),
					(neq, ":value", 0),
					(val_add, ":value", 5),
					(val_div, ":value", 10),
					(val_mul, ":value", 10),
					(try_begin),
						(eq, ":value", 0),
						(assign, ":value", 5),
					(try_end),
				(else_try),
					(lt, ":value", 300),
					(val_add, ":value", 25),
					(val_div, ":value", 50),
					(val_mul, ":value", 50),
				(else_try),
					(val_add, ":value", 50),
					(val_div, ":value", 100),
					(val_mul, ":value", 100),
				(try_end),
				(assign, reg0, ":value"),
		])

		# script_describe_relation_to_s63
		# Input: arg1 = relation (-100 .. 100)
		# Output: s63
describe_relation_to_s63 = (
	"describe_relation_to_s63",
			[(store_script_param_1, ":relation"),
				(store_add, ":normalized_relation", ":relation", 100),
				(val_add, ":normalized_relation", 5),
				(store_div, ":str_offset", ":normalized_relation", 10),
				(val_clamp, ":str_offset", 0, 20),
				(store_add, ":str_id", "str_relation_mnus_100",  ":str_offset"),
				(str_store_string, s63, ":str_id"),
		])
		
		# script_describe_center_relation_to_s3
		# Input: arg1 = relation (-100 .. 100)
		# Output: s3
describe_center_relation_to_s3 = (
	"describe_center_relation_to_s3",
			[(store_script_param_1, ":relation"),
				(store_add, ":normalized_relation", ":relation", 100),
				(val_add, ":normalized_relation", 5),
				(store_div, ":str_offset", ":normalized_relation", 10),
				(val_clamp, ":str_offset", 0, 20),
				(store_add, ":str_id", "str_center_relation_mnus_100",  ":str_offset"),
				(str_store_string, s3, ":str_id"),
		])
		

#script_get_name_from_dna_to_s50
		# INPUT: arg1 = dna
		# OUTPUT: s50 = name
get_name_from_dna_to_s50 = ("get_name_from_dna_to_s50",
			[(store_script_param, ":dna", 1),
				(store_sub, ":num_names", names_end, names_begin),
				(store_sub, ":num_surnames", surnames_end, surnames_begin),
				(assign, ":selected_name", ":dna"),
				(val_mod, ":selected_name", ":num_names"),
				(assign, ":selected_surname", ":dna"),
				(val_div, ":selected_surname", ":num_names"),
				(val_mod, ":selected_surname", ":num_surnames"),
				(val_add, ":selected_name", names_begin),
				(val_add, ":selected_surname", surnames_begin),
				(str_store_string, s50, ":selected_name"),
				(str_store_string, s50, ":selected_surname"),
		])


		# script_get_rumor_to_s61
		# Input: rumor_id
		# Output: reg0 = 1 if rumor found, 0 otherwise; s61 will contain rumor string if found
get_rumor_to_s61 = (
	"get_rumor_to_s61",
			[
				(store_script_param, ":base_rumor_id", 1), # the script returns the same rumor for the same rumor id, so that one cannot hear all rumors by
				# speaking to a single person.
				
				(store_current_hours, ":cur_hours"),
				(store_div, ":cur_day", ":cur_hours", 24),
				(assign, ":rumor_found", 0),
				(assign, ":num_tries", 3),
				(try_for_range, ":try_no", 0, ":num_tries"),
					(store_mul, ":rumor_id", ":try_no", 6781),
					(val_add, ":rumor_id", ":base_rumor_id"),
					(store_mod, ":rumor_type", ":rumor_id", 7),
					(val_add, ":rumor_id", ":cur_hours"),
					(try_begin),
						(eq,  ":rumor_type", 0),
						(try_begin),
							(store_sub, ":range", towns_end, towns_begin),
							(store_mod, ":random_center", ":rumor_id", ":range"),
							(val_add, ":random_center", towns_begin),
							(party_slot_ge, ":random_center", slot_town_has_tournament, 1),
							(neq, ":random_center", "$current_town"),
							(str_store_party_name, s62, ":random_center"),
							(str_store_string, s61, "@I heard that there will be a tournament in {s62} soon."),
							(assign, ":rumor_found", 1),
						(try_end),
					(else_try),
						(eq,  ":rumor_type", 1),
						(try_begin),
							(store_sub, ":range", active_npcs_end, original_kingdom_heroes_begin), #was reversed
							(store_mod, ":random_hero", ":rumor_id", ":range"),
							(val_add, ":random_hero", original_kingdom_heroes_begin),
							(is_between, ":random_hero", active_npcs_begin, active_npcs_end),
							(troop_get_slot, ":personality", ":random_hero", slot_lord_reputation_type),
							(gt, ":personality", 0),
							(store_add, ":rumor_string", ":personality", "str_gossip_about_character_default"),
							(str_store_troop_name, s6, ":random_hero"),
							(str_store_string, s61, ":rumor_string"),
							(assign, ":rumor_found", 1),
						(try_end),
					(else_try),
						(eq,  ":rumor_type", 2),
						(try_begin),
							(store_sub, ":range", trade_goods_end, trade_goods_begin),
							(store_add, ":random_trade_good", ":rumor_id", ":cur_day"),
							(store_mod, ":random_trade_good", ":random_trade_good", ":range"),
							(store_add, ":random_trade_good_slot", ":random_trade_good", slot_town_trade_good_prices_begin),
							(val_add, ":random_trade_good", trade_goods_begin),
							(store_mul, ":min_price", average_price_factor, 3),
							(val_div, ":min_price", 4),
							(assign, ":min_price_center", -1),
							(try_for_range, ":sub_try_no", 0, 10),
								(store_sub, ":range", towns_end, towns_begin),
								(store_add, ":center_rumor_id", ":rumor_id", ":sub_try_no"),
								(store_mod, ":random_center", ":center_rumor_id", ":range"),
								(val_add, ":random_center", towns_begin),
								(neq, ":random_center", "$g_encountered_party"),
								(party_get_slot, ":cur_price", ":random_center", ":random_trade_good_slot"),
								(lt, ":cur_price", ":min_price"),
								(assign, ":min_price", ":cur_price"),
								(assign, ":min_price_center", ":random_center"),
							(try_end),
							(ge, ":min_price_center", 0),
							(str_store_item_name, s62, ":random_trade_good"),
							(str_store_party_name, s63, ":min_price_center"),
							(str_store_string, s61, "@I heard that one can buy {s62} very cheap at {s63}."),
							(assign, ":rumor_found", 1),
						(try_end),
					(else_try),
						(eq,  ":rumor_type", 3),
						(try_begin),
							(store_sub, ":range", trade_goods_end, trade_goods_begin),
							(store_add, ":random_trade_good", ":rumor_id", ":cur_day"),
							(store_mod, ":random_trade_good", ":random_trade_good", ":range"),
							(store_add, ":random_trade_good_slot", ":random_trade_good", slot_town_trade_good_prices_begin),
							(val_add, ":random_trade_good", trade_goods_begin),
							(store_mul, ":max_price", average_price_factor, 5),
							(val_div, ":max_price", 4),
							(assign, ":max_price_center", -1),
							(try_for_range, ":sub_try_no", 0, 10),
								(store_sub, ":range", towns_end, towns_begin),
								(store_add, ":center_rumor_id", ":rumor_id", ":sub_try_no"),
								(store_mod, ":random_center", ":center_rumor_id", ":range"),
								(val_add, ":random_center", towns_begin),
								(neq, ":random_center", "$g_encountered_party"),
								(party_get_slot, ":cur_price", ":random_center", ":random_trade_good_slot"),
								(gt, ":cur_price", ":max_price"),
								(assign, ":max_price", ":cur_price"),
								(assign, ":max_price_center", ":random_center"),
							(try_end),
							(ge, ":max_price_center", 0),
							(str_store_item_name, s62, ":random_trade_good"),
							(str_store_party_name, s63, ":max_price_center"),
							(str_store_string, s61, "@I heard that they pay a very high price for {s62} at {s63}."),
							(assign, ":rumor_found", 1),
						(try_end),
					(try_end),
					(try_begin),
						(gt, ":rumor_found", 0),
						(assign, ":num_tries", 0),
					(try_end),
				(try_end),
				(assign, reg0, ":rumor_found"),
		])


		#script_lord_comment_to_s43
		#INPUT: lord troop
		#OUTPUT: reputation strings in s43, reputation in reg0
lord_comment_to_s43 = (
	"lord_comment_to_s43",
			[(store_script_param, ":lord", 1),
				(store_script_param, ":default_string", 2),
				
				(troop_get_slot,":reputation", ":lord", slot_lord_reputation_type),
				
				(try_begin),
					#some default strings will have added comments for the added commons reputation types
					(try_begin),
						(eq, ":reputation", lrep_roguish),
						(assign, ":reputation", lrep_goodnatured),
					(else_try),
						(eq, ":reputation", lrep_custodian),
						(assign, ":reputation", lrep_cunning),
					(else_try),
						(eq, ":reputation", lrep_benefactor),
						(assign, ":reputation", lrep_goodnatured),
					(try_end),
				(try_end),
				
				(store_add, ":result", ":reputation", ":default_string"),
				
				(str_store_string, 43, ":result"),
				(assign, reg0, ":result"),
				
				
		])

#script_reduce_exact_number_to_estimate
	#This is used to simulate limited intelligence
	#It is roughly analogous to the descriptive strings which the player will receive from alarms
	#Information is presumed to be accurate for four days
	#This is obviously cheating for the AI, as the AI will have exact info for four days, and no info at all after that.
	#It would be fairly easy to log the strength at a center when it is scouted, if we want, but I have not done that at this point,
	#The AI also has a hive mind -- ie, each party knows what its allies are thinking. In this, AI factions have an advantage over the player
	#It would be a simple matter to create a set of arrays in which each party's knowledge is individually updated, but that would also take up a lot of data space
	#INPUT: exact_number
	#OUTPUT: estimate
reduce_exact_number_to_estimate =	(
		"reduce_exact_number_to_estimate",	
		[
		(store_script_param, ":exact_number", 1),
		
		(try_begin),
			(lt, ":exact_number", 500),
			(assign, ":estimate", 0),
		(else_try),
			(lt, ":exact_number", 1000),
			(assign, ":estimate", 750),
		(else_try),
			(lt, ":exact_number", 2000),
			(assign, ":estimate", 1500),
		(else_try),
			(lt, ":exact_number", 4000),
			(assign, ":estimate", 3000),
		(else_try),
			(lt, ":exact_number", 8000),
			(assign, ":estimate", 6000),
		(else_try),
			(lt, ":exact_number", 16000),
			(assign, ":estimate", 12000),
		(else_try),
			(assign, ":estimate", 24000),
		(try_end),
		
		(assign, reg0, ":estimate"),
	])