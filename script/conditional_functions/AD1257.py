from header import *


	# script_is_party_on_water
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: party_id
	# OUTPUT: none. boolean
cf_is_party_on_water = (
	"cf_is_party_on_water",
		[
		(store_script_param_1, ":party_id"),
		(party_get_current_terrain, ":party_terrain", ":party_id"),
		
		(assign, reg0, 0),
		
		(try_begin),
			(this_or_next|eq, ":party_terrain", rt_water),
			(this_or_next|eq, ":party_terrain", rt_river),
			(this_or_next|eq, ":party_terrain", rt_bridge),
			(eq, ":party_terrain", 15),
			(assign, reg0, 1),
		(try_end),
		
		(gt, reg0, 0),
	])