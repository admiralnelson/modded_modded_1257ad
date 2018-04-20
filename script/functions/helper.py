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
round_value=(
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
describe_relation_to_s63=(
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
describe_center_relation_to_s3=(
	"describe_center_relation_to_s3",
			[(store_script_param_1, ":relation"),
				(store_add, ":normalized_relation", ":relation", 100),
				(val_add, ":normalized_relation", 5),
				(store_div, ":str_offset", ":normalized_relation", 10),
				(val_clamp, ":str_offset", 0, 20),
				(store_add, ":str_id", "str_center_relation_mnus_100",  ":str_offset"),
				(str_store_string, s3, ":str_id"),
		])
		