from header import *

#script_raf_create_incidents
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: none
	#OUTPUT: none
raf_create_incidents = (
	"raf_create_incidents",
		[
		
		(assign, reg0, -1),
		(assign, reg1, -1),
		
		(assign, ":end_cond", 96),
		
		(try_for_range, ":i", 1, ":end_cond"),
			(store_random_in_range, ":acting_village", villages_begin, villages_end),
			(store_random_in_range, ":target_village", villages_begin, villages_end),
			(store_faction_of_party, ":acting_faction", ":acting_village"),
			(store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
			
			(try_begin),
			(neq, ":acting_village", ":target_village"),
			(neq, ":acting_faction", ":target_faction"),
			(store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
			#(call_script, "script_distance_between_factions", ":acting_faction", ":target_faction"),
			(le, ":distance", 25),
			(assign, reg0, ":acting_village"),
			(assign, reg1, ":target_village"),
			# (str_store_party_name, s1, ":acting_village"),
			# (str_store_party_name, s2, ":target_village"),
			# (display_message, "@--DEBUG-- incident between {s1} and {s2}"),
			# (assign, ":i", ":end_cond"),
			(assign, ":end_cond", 0),
			(else_try),
			(val_add, ":i", 1),
			(try_end),
		(try_end),
		])