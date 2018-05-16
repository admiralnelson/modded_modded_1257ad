from header import *
##script_get_party_campsite - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: party
	##output: reg0 - campsite scene
	##description: Sets the scene based on the current party terrain
get_party_campsite = (
	"get_party_campsite",
		[
			(store_script_param, ":party", 1),
			(party_get_current_terrain,":terrain",":party"),
		#(assign, ":terrain", rt_plain),
		(assign, reg0, "scn_campside_plain"),
		(try_begin),
			(this_or_next|eq, ":terrain", rt_plain),
			(this_or_next|eq, ":terrain", rt_mountain_forest),
			(eq, ":terrain", rt_forest),
			(assign, reg0, "scn_campside_plain"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_snow),
			(eq, ":terrain", rt_snow_forest),
			(assign, reg0, "scn_campside_snow"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_steppe),
			(eq, ":terrain", rt_steppe_forest),
			(assign, reg0, "scn_campside_steppe"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_desert),
			(eq, ":terrain", rt_desert_forest),
			(assign, reg0, "scn_campside_desert"),
		(try_end),
		])