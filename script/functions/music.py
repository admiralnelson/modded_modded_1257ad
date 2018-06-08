from header import *


	# script_get_culture_with_party_faction_for_music
	# Input: arg1 = party_no
	# Output: reg0 = culture
get_culture_with_party_faction_for_music = (
	"get_culture_with_party_faction_for_music",
		[
		(store_script_param, ":party_no", 1),
		(store_faction_of_party, ":faction_no", ":party_no"),
		(try_begin),
			(this_or_next|eq, ":faction_no", "fac_player_faction"),
			(eq, ":faction_no", "fac_player_supporters_faction"),
				(assign, ":faction_no", "$players_kingdom"),
		(try_end),
		(try_begin),
			(is_between, ":party_no", centers_begin, centers_end),
			(this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
			(neg|is_between, ":faction_no", kingdoms_begin, kingdoms_end),
				(party_get_slot, ":faction_no", ":party_no", slot_center_original_faction),
		(try_end),
		
		# rafi music
		(call_script, "script_get_closest_center", "p_main_party"),
		(party_get_slot, ":faction_no", reg0, slot_center_original_faction),
		# rafi music
		(call_script, "script_get_culture_with_faction_for_music", ":faction_no"),
	])


# script_get_culture_with_faction_for_music
	# Input: arg1 = party_no
	# Output: reg0 = culture
get_culture_with_faction_for_music = (
	"get_culture_with_faction_for_music",
		[
		(store_script_param, ":faction_no", 1),
		# Central europe
		(try_begin),
			(this_or_next|eq, ":faction_no", "fac_kingdom_1"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_5"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_7"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_34"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_42"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_4"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_23"),			
			(this_or_next|eq, ":faction_no", "fac_papacy"),
			(eq, ":faction_no", "fac_kingdom_6"),
				(assign, ":result", mtf_culture_central_eu),
				(display_message, "@region music mtf_culture_central_eu", 0XFFFFFF),
				
		# West europe
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_kingdom_26"),
			(eq, ":faction_no", "fac_kingdom_10"),
				(assign, ":result", mtf_culture_west_eu),
				(display_message, "@region music mtf_culture_west_eu", 0XFFFFFF),
		# Britain
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_kingdom_12"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_13"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_37"),
			(eq, ":faction_no", "fac_kingdom_9"),
				(assign, ":result", mtf_culture_britain),
				(display_message, "@region music mtf_culture_britain", 0XFFFFFF),
		# Eastern europe
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_kingdom_2"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_15"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_29"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_30"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_33"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_35"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_36"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_40"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_8"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_3"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_27"),
			(eq, ":faction_no", "fac_kingdom_41"),
				(assign, ":result", mtf_culture_eastern_eu),
				(display_message, "@region music mtf_culture_eastern_eu", 0XFFFFFF),
		# Mediterannia
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_kingdom_16"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_17"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_18"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_19"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_32"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_38"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_39"),
			(eq, ":faction_no", "fac_kingdom_24"),
				(assign, ":result", mtf_culture_mediterrania),
				(display_message, "@region music mtf_culture_mediterrania", 0XFFFFFF),
		# Nordic
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_kingdom_14"),
			(eq, ":faction_no", "fac_kingdom_11"),
				(assign, ":result", mtf_culture_scandinavia),
				(display_message, "@region music mtf_culture_scandinavia", 0XFFFFFF),
		# Byzantines
		(else_try),
			(eq, ":faction_no", "fac_kingdom_22"),
				(assign, ":result", mtf_culture_byzantine),
				(display_message, "@region music mtf_culture_byzantine", 0XFFFFFF),
		# Arabs
		(else_try), 
			(this_or_next|eq, ":faction_no", "fac_kingdom_8"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_3"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_25"),
			(this_or_next|eq, ":faction_no", "fac_kingdom_28"),	
			(this_or_next|eq, ":faction_no", "fac_kingdom_31"),		
			(eq, ":faction_no", "fac_kingdom_20"),
				(assign, ":result", mtf_culture_arabians),
				(display_message, "@region music mtf_culture_arabians", 0XFFFFFF),
		(else_try),
			(assign, ":result", 0), #no culture, including player with no bindings to another kingdom
			#(display_message, "@region music <- NULL"),
		(try_end),
		(assign, reg0, ":result"),
	])
	
	
	# script_get_culture_with_faction_for_music
	# WARNING: disabled by me (modded2x)
	# Input: arg1 = party_no
	# Output: reg0 = culture
get_culture_with_faction_for_music_UNUSED = (
	"get_culture_with_faction_for_music",
		[
		(store_script_param, ":faction_no", 1),
		(try_begin),
			(this_or_next | eq, ":faction_no", "fac_kingdom_5"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_6"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_7"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_9"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_37"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_10"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_12"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_16"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_17"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_18"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_19"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_24"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_38"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_39"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_40"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_41"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_42"),
			# (this_or_next | eq, ":faction_no", "fac_kingdom_34"),
			
			(this_or_next | eq, ":faction_no", "fac_kingdom_32"),
			(eq, ":faction_no", "fac_kingdom_13"),
				(assign, ":result", mtf_culture_generic),
		(else_try),
			(this_or_next | eq, ":faction_no", "fac_kingdom_2"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_3"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_8"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_15"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_22"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_26"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_27"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_29"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_30"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_33"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_34"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_35"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_36"),
			(eq, ":faction_no", "fac_kingdom_8"),
				(assign, ":result", mtf_culture_eastern),
		(else_try),
			(this_or_next | eq, ":faction_no", "fac_kingdom_4"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_11"),
			(eq, ":faction_no", "fac_kingdom_14"),
				(assign, ":result", mtf_culture_nordic),
		(else_try),
			(this_or_next | eq, ":faction_no", "fac_papacy"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_23"),
			(eq, ":faction_no", "fac_kingdom_1"),
				(assign, ":result", mtf_culture_christian),
		(else_try),
			(this_or_next | eq, ":faction_no", "fac_kingdom_20"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_25"),
			(this_or_next | eq, ":faction_no", "fac_kingdom_31"),
			(eq, ":faction_no", "fac_kingdom_28"),
				(assign, ":result", mtf_culture_moorish),
		(else_try),
			(assign, ":result", 0), #no culture, including player with no bindings to another kingdom
		(try_end),
		(assign, reg0, ":result"),
	])
	