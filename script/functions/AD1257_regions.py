from header import *

	#script_tom_aor_faction_to_region
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: for lance recruitment system, select region. whitout player kingdom interferance
	# INPUT: faction
	# OUTPUT: region
tom_aor_faction_to_region = (
	"tom_aor_faction_to_region",
		[
		(store_script_param, ":faction", 1),
		
		(try_begin),
			(eq, ":faction", "fac_kingdom_1"),
			(assign, reg0, region_teutonic),
			# generic
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_5"),
			(this_or_next | eq, ":faction", "fac_kingdom_6"),
			(this_or_next | eq, ":faction", "fac_kingdom_7"),
			(this_or_next | eq, ":faction", "fac_kingdom_9"),
			(this_or_next | eq, ":faction", "fac_kingdom_37"),
			(this_or_next | eq, ":faction", "fac_kingdom_19"),
			(this_or_next | eq, ":faction", "fac_kingdom_42"),
			(eq, ":faction", "fac_kingdom_10"), #TOM
			#(this_or_next | eq, ":faction", "fac_kingdom_10"), #TOM
			#(eq, ":faction", "fac_kingdom_12"), #TOM
			
			(assign, reg0, region_european),
			#scot
		(else_try), #TOM
			(eq, ":faction", "fac_kingdom_12"), #TOM
			(assign, reg0, region_scot),
			# gaelic
		(else_try),
			(eq, ":faction", "fac_kingdom_13"),
			(assign, reg0, region_gaelic),
			#latin
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_16"),
			(this_or_next | eq, ":faction", "fac_kingdom_17"),
			(this_or_next | eq, ":faction", "fac_kingdom_18"),
			(this_or_next | eq, ":faction", "fac_papacy"),
			(this_or_next | eq, ":faction", "fac_kingdom_26"),
			(this_or_next | eq, ":faction", "fac_kingdom_32"),
			(this_or_next | eq, ":faction", "fac_kingdom_38"),
			(this_or_next | eq, ":faction", "fac_kingdom_39"),
			(this_or_next | eq, ":faction", "fac_kingdom_40"),
			(this_or_next | eq, ":faction", "fac_kingdom_41"),
			# (this_or_next | eq, ":faction", "fac_kingdom_34"),
			(eq, ":faction", "fac_kingdom_24"),
			(assign, reg0, region_latin),
			#(display_message, "@LATIN"),
			# balt
		(else_try),
			(this_or_next|eq, ":faction", "fac_kingdom_33"),
			(this_or_next|eq, ":faction", "fac_kingdom_34"),
			(this_or_next|eq, ":faction", "fac_kingdom_35"),
			(this_or_next|eq, ":faction", "fac_kingdom_36"),
			(eq, ":faction", "fac_kingdom_2"),
			(assign, reg0, region_baltic),
			# anatolian
		(else_try),
			(eq, ":faction", "fac_kingdom_27"),
			(assign, reg0, region_anatolian),
			# mongol
		(else_try),
			(eq, ":faction", "fac_kingdom_3"),
			(assign, reg0, region_mongol),
			# nordic
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_4"),
			(this_or_next | eq, ":faction", "fac_kingdom_11"),
			(eq, ":faction", "fac_kingdom_14"),
			(assign, reg0, region_nordic),
			# balkan
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_29"),
			(eq, ":faction", "fac_kingdom_30"),
			(assign, reg0, region_balkan),
			# eastern
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_15"),
			(eq, ":faction", "fac_kingdom_8"),
			(assign, reg0, region_eastern),
			# andalus
		(else_try),
			(eq, ":faction", "fac_kingdom_20"),
			(assign, reg0, region_andalusian),
		(else_try),
			# north african
			(this_or_next | eq, ":faction", "fac_kingdom_28"),
			(eq, ":faction", "fac_kingdom_31"),
			(assign, reg0, region_north_african),
		(else_try),
			# mamluk
			(eq, ":faction", "fac_kingdom_25"),
			(assign, reg0, region_mamluk),
		(else_try),
			# byzantine
			(eq, ":faction", "fac_kingdom_22"),
			(assign, reg0, region_byzantine),
		(else_try),
			# crusaders
			(eq, ":faction", "fac_kingdom_23"),
			(assign, reg0, region_crusaders),
		(else_try),
			# anatolian
			(eq, ":faction", "fac_kingdom_27"),
			(assign, reg0, region_anatolian),
		(else_try),
			(assign, reg0, region_unknown),
		(try_end),
		])
	
	#script_raf_aor_faction_to_region
	#INPUT: faction
	#OUTPUT: region
raf_aor_faction_to_region = (
	"raf_aor_faction_to_region",
		[
		(store_script_param, ":faction", 1),
		
		(try_begin),
			(eq, ":faction", "fac_kingdom_1"),
			(try_begin),
			(eq, "$players_kingdom", "fac_kingdom_1"),
			(assign, reg0, region_teutonic),
			(else_try),
			(assign, reg0, region_baltic),
			(try_end),
			# (else_try),
			# (eq, ":faction", "fac_kingdom_26"),
			# (try_begin),
			# (eq, "$players_kingdom", "fac_kingdom_26"),
			# (assign, reg0, region_latin),
			# (else_try),
			# (assign, reg0, region_byzantine),
			# (try_end),
			# generic
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_5"),
			(this_or_next | eq, ":faction", "fac_kingdom_6"),
			(this_or_next | eq, ":faction", "fac_kingdom_7"),
			(this_or_next | eq, ":faction", "fac_kingdom_9"),
			(this_or_next | eq, ":faction", "fac_kingdom_37"),
			(this_or_next | eq, ":faction", "fac_kingdom_19"),
			(this_or_next | eq, ":faction", "fac_kingdom_42"),
			(eq, ":faction", "fac_kingdom_10"), #TOM
			#(this_or_next | eq, ":faction", "fac_kingdom_10"), #TOM
			#(eq, ":faction", "fac_kingdom_12"), #TOM
			
			(assign, reg0, region_european),
			#scot
		(else_try), #TOM
			(eq, ":faction", "fac_kingdom_12"), #TOM
			(assign, reg0, region_scot),
			# gaelic
		(else_try),
			(eq, ":faction", "fac_kingdom_13"),
			(assign, reg0, region_gaelic),
			#latin
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_16"),
			(this_or_next | eq, ":faction", "fac_kingdom_17"),
			(this_or_next | eq, ":faction", "fac_kingdom_18"),
			(this_or_next | eq, ":faction", "fac_papacy"),
			(this_or_next | eq, ":faction", "fac_kingdom_26"),
			(this_or_next | eq, ":faction", "fac_kingdom_32"),
			(this_or_next | eq, ":faction", "fac_kingdom_38"),
			(this_or_next | eq, ":faction", "fac_kingdom_39"),
			(this_or_next | eq, ":faction", "fac_kingdom_40"),
			(this_or_next | eq, ":faction", "fac_kingdom_41"),
			# (this_or_next | eq, ":faction", "fac_kingdom_34"),
			(eq, ":faction", "fac_kingdom_24"),
			(assign, reg0, region_latin),
			#(display_message, "@LATIN"),
			# balt
		(else_try),
			(this_or_next|eq, ":faction", "fac_kingdom_33"),
			(this_or_next|eq, ":faction", "fac_kingdom_34"),
			(this_or_next|eq, ":faction", "fac_kingdom_35"),
			(this_or_next|eq, ":faction", "fac_kingdom_36"),
			(eq, ":faction", "fac_kingdom_2"),
			(assign, reg0, region_baltic),
			# anatolian
		(else_try),
			(eq, ":faction", "fac_kingdom_27"),
			(assign, reg0, region_anatolian),
			# mongol
		(else_try),
			(eq, ":faction", "fac_kingdom_3"),
			(assign, reg0, region_mongol),
			# nordic
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_4"),
			(this_or_next | eq, ":faction", "fac_kingdom_11"),
			(eq, ":faction", "fac_kingdom_14"),
			(assign, reg0, region_nordic),
			# balkan
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_29"),
			(eq, ":faction", "fac_kingdom_30"),
			(assign, reg0, region_balkan),
			# eastern
		(else_try),
			(this_or_next | eq, ":faction", "fac_kingdom_15"),
			(eq, ":faction", "fac_kingdom_8"),
			(assign, reg0, region_eastern),
			# andalus
		(else_try),
			(eq, ":faction", "fac_kingdom_20"),
			(assign, reg0, region_andalusian),
		(else_try),
			# north african
			(this_or_next | eq, ":faction", "fac_kingdom_28"),
			(eq, ":faction", "fac_kingdom_31"),
			(assign, reg0, region_north_african),
		(else_try),
			# mamluk
			(eq, ":faction", "fac_kingdom_25"),
			(assign, reg0, region_mamluk),
		(else_try),
			# byzantine
			(eq, ":faction", "fac_kingdom_22"),
			(assign, reg0, region_byzantine),
		(else_try),
			# crusaders
			(eq, ":faction", "fac_kingdom_23"),
			(assign, reg0, region_crusaders),
		(else_try),
			# anatolian
			(eq, ":faction", "fac_kingdom_27"),
			(assign, reg0, region_anatolian),
		(else_try),
			(assign, reg0, region_unknown),
		(try_end),
		])

	#script_raf_aor_region_to_faction
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: region
	#OUTPUT: faction
raf_aor_region_to_faction = (
	"raf_aor_region_to_faction",
		[
		(store_script_param, ":region", 1),
		
		(try_begin),
			(eq, ":region", region_teutonic),
			(assign, reg0, "fac_kingdom_1"),
			# generic
		(else_try),
			(eq, ":region", region_european),
			(assign, reg0, "fac_kingdom_5"),
			# gaelic
		(else_try),
			(eq, ":region", region_gaelic),
			(assign, reg0, "fac_kingdom_13"),
		(else_try),
			(eq, ":region", region_latin),
			(assign, reg0, "fac_kingdom_16"),
		(else_try),
			(eq, ":region", region_anatolian),
			(assign, reg0, "fac_kingdom_27"),
			# balt
		(else_try),
			(eq, ":region", region_baltic),
			(assign, reg0, "fac_kingdom_2"),
			# mongol
		(else_try),
			(eq, ":region", region_mongol),
			(assign, reg0, "fac_kingdom_3"),
			# nordic
		(else_try),
			(eq, ":region", region_nordic),
			(assign, reg0, "fac_kingdom_4"),
			# balkan
		(else_try),
			(eq, ":region", region_balkan),
			(assign, reg0, "fac_kingdom_29"),
			# eastern
		(else_try),
			(eq, ":region", region_eastern),
			(assign, reg0, "fac_kingdom_8"),
		(else_try),
			(eq, ":region", region_andalusian),
			(assign, reg0, "fac_kingdom_20"),
		(else_try),
			(eq, ":region", region_north_african),
			(assign, reg0, "fac_kingdom_28"),
		(else_try),
			(eq, ":region", region_mamluk),
			(assign, reg0, "fac_kingdom_25"),
		(else_try),
			(eq, ":region", region_crusaders),
			(assign, reg0, "fac_kingdom_23"),
		(else_try),
			(eq, ":region", region_byzantine),
			(assign, reg0, "fac_kingdom_22"),
			#TOM
		(else_try),
			(eq, ":region", region_scot),
			(assign, reg0, "fac_kingdom_12"),
		(try_end),
		])