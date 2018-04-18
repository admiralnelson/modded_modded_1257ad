from header import *

#script_get_army_size_from_slider_value
# INPUT: arg1 = slider_value
# OUTPUT: reg0 = army_size
get_army_size_from_slider_value = (
	"get_army_size_from_slider_value",
		[
			(store_script_param, ":slider_value", 1),
			(assign, ":army_size", ":slider_value"),
			(try_begin),
				(gt, ":slider_value", 25),
				(store_sub, ":adder_value", ":slider_value", 25),
				(val_add, ":army_size", ":adder_value"),
				(try_begin),
					(gt, ":slider_value", 50),
					(store_sub, ":adder_value", ":slider_value", 50),
					(val_mul, ":adder_value", 3),
					(val_add, ":army_size", ":adder_value"),
				(try_end),
			(try_end),
			(assign, reg0, ":army_size"),
	])