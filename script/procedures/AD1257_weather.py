from header import *
from header import *

#script_change_rain_or_snow
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: none
		# OUTPUT: none
change_rain_or_snow = (
	"change_rain_or_snow",
			[
			(party_get_current_terrain, ":terrain_type", "p_main_party"),
			(try_begin),
				(this_or_next|eq, ":terrain_type", rt_snow),
				(eq, ":terrain_type", rt_snow_forest),
				(assign, ":rain_type", 2),
			(else_try),
				(assign, ":rain_type", 1),
			(try_end),
			
			(get_global_cloud_amount, ":rand_rain"),
			(assign, ":its_raining", 0),
			#(store_random_in_range, ":rand_rain", 0, 101),
			(try_begin),
				(neq, ":terrain_type", rt_desert),
				(neq, ":terrain_type", rt_desert_forest),
				#(lt, ":rand_rain", "$g_rand_rain_limit"),
				(gt, ":rand_rain", 67),
				#(store_mul, ":rand_strength", ":rand_rain", "$g_rand_rain_limit"),
				#(val_div, ":rand_strength", 100),
				#(gt, ":rand_strength", 0),
				(store_random_in_range, ":rand_strength", 30, 101),
				(set_rain, ":rain_type", ":rand_strength"),
				(assign, ":its_raining", 1),
				(store_random_in_range, ":fog", 30, 101),
				(set_global_haze_amount, ":fog"),
				# (store_random_in_range, ":fog", 60, 101),
				# (set_global_cloud_amount, 100),
			(try_end),
			
			#tom - blizzzrd perhaps?
			(store_random_in_range, ":sandstorm", 1, 100),
			(try_begin),
				(eq, ":its_raining", 1),
				(eq, ":rain_type", 2), #snow
				(neq|eq, "$tom_sand_storm_chance", 0),
				(lt, ":sandstorm", "$tom_sand_storm_chance"),
				(set_rain, 2, 100),
				(assign, "$tom_sand_storm", 2),
				(set_global_haze_amount, 100),
				#tom - storm perhaps?
			(else_try),
				(eq, ":its_raining", 1),
				(eq, ":rain_type", 1), #rain
				(neq|eq, "$tom_sand_storm_chance", 0),
				(lt, ":sandstorm", "$tom_sand_storm_chance"),
				(set_rain, 1, 100),
				(assign, "$tom_sand_storm", 3),
				(set_global_haze_amount, 100),
				#tom - perhaps sand storm insted?
			(else_try),
				(this_or_next|eq, ":terrain_type", rt_desert),
				(eq, ":terrain_type", rt_desert_forest),
				#(neq|eq, "$tom_sand_storm_chance", 0),
				(lt, ":sandstorm", "$tom_sand_storm_chance"),
				#(set_rain, 0, 0),
				(assign, "$tom_sand_storm", 1),
				(set_global_haze_amount, 0),
			(try_end),
		])