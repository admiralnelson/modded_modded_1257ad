from header import *


# script_cf_check_color_visibility
# Input: arg1 = color_1, arg2 = color_2
# Output: none
cf_check_color_visibility = (
	"cf_check_color_visibility",
			[
				(store_script_param, ":color_1", 1),
				(store_script_param, ":color_2", 2),
				(store_mod, ":blue_1", ":color_1", 256),
				(store_div, ":green_1", ":color_1", 256),
				(val_mod, ":green_1", 256),
				(store_div, ":red_1", ":color_1", 256 * 256),
				(val_mod, ":red_1", 256),
				(store_mod, ":blue_2", ":color_2", 256),
				(store_div, ":green_2", ":color_2", 256),
				(val_mod, ":green_2", 256),
				(store_div, ":red_2", ":color_2", 256 * 256),
				(val_mod, ":red_2", 256),
				(store_sub, ":red_dif", ":red_1", ":red_2"),
				(val_abs, ":red_dif"),
				(store_sub, ":green_dif", ":green_1", ":green_2"),
				(val_abs, ":green_dif"),
				(store_sub, ":blue_dif", ":blue_1", ":blue_2"),
				(val_abs, ":blue_dif"),
				(assign, ":max_dif", 0),
				(val_max, ":max_dif", ":red_dif"),
				(val_max, ":max_dif", ":green_dif"),
				(val_max, ":max_dif", ":blue_dif"),
				(ge, ":max_dif", 64),
		])