from header import *
		# script_map_get_random_position_around_position_within_range
		# Input: arg1 = minimum_distance in km, arg2 = maximum_distance in km, pos1 = origin position
		# Output: pos2 = result position
map_get_random_position_around_position_within_range=(
	"map_get_random_position_around_position_within_range",
			[
				(store_script_param_1, ":min_distance"),
				(store_script_param_2, ":max_distance"),
				(val_mul, ":min_distance", 100),
				(assign, ":continue", 1),
				(try_for_range, ":unused", 0, 20),
					(eq, ":continue", 1),
					(map_get_random_position_around_position, pos2, pos1, ":max_distance"),
					(get_distance_between_positions, ":distance", pos2, pos1),
					(ge, ":distance", ":min_distance"),
					(assign, ":continue", 0),
				(try_end),
		])
		
		# script_get_number_of_unclaimed_centers_by_player
		# Input: none
		# Output: reg0 = number of unclaimed centers, reg1 = last unclaimed center_no
get_number_of_unclaimed_centers_by_player=(
	"get_number_of_unclaimed_centers_by_player",
			[
				(assign, ":unclaimed_centers", 0),
				(assign, reg1, -1),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_faction_of_party, ":faction_no", ":center_no"),
					(eq, ":faction_no", "fac_player_supporters_faction"),
					(party_slot_eq, ":center_no", slot_town_claimed_by_player, 0),
					(party_get_num_companion_stacks, ":num_stacks", ":center_no"),
					(ge, ":num_stacks", 1), #castle is garrisoned
					(assign, reg1, ":center_no"),
					(val_add, ":unclaimed_centers", 1),
				(try_end),
				(assign, reg0, ":unclaimed_centers"),
		])