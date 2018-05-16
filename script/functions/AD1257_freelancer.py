from header import *
##TOM freelancer addon
	## script_freelancer_get_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# freelancer script here!
	##input: troop, faction
	##output: reg1 - troop
freelancer_get_troop =	(
	"freelancer_get_troop",
	[
			(store_script_param, ":talk_troop", 1),
			(store_script_param, ":troop_faction", 2),
			(store_script_param, ":tier", 3),
		
		(try_begin),
			(eq,":talk_troop","trp_knight_23_6"),  # teutonic
			(assign, reg1, "trp_teu_town_1"),
			(try_begin),
				(troop_slot_ge, "trp_player", slot_troop_renown, 120),
			(assign, reg1, "trp_teu_horse_1"),
			(try_end),
		(else_try),
			(eq,":talk_troop","trp_knight_23_1"), # hospitaller
			(assign, reg1, "trp_hospitaller_half_brother"),
			(try_begin),
				(troop_slot_ge, "trp_player", slot_troop_renown, 120),
			(assign, reg1, "trp_hospitaller_knight"),
			(try_end),
		(else_try),
			(eq,":talk_troop","trp_knight_23_2"), # templar
			(assign, reg1, "trp_templar_half_brother"),
			(try_begin),
				(troop_slot_ge, "trp_player", slot_troop_renown, 120),
			(assign, reg1, "trp_templar_knight"),
			(try_end),
		(else_try),
			(eq,":talk_troop","trp_knight_16_1"), # santiago
			(assign, reg1, "trp_santiago_half_brother"),
			(try_begin),
				(troop_slot_ge, "trp_player", slot_troop_renown, 120),
			(assign, reg1, "trp_santiago_knight"),
			(try_end),
		(else_try),
			(eq,":talk_troop","trp_knight_18_9"), # caltrava
			(assign, reg1, "trp_calatrava_half_brother"),
			(try_begin),
				(troop_slot_ge, "trp_player", slot_troop_renown, 120),
			(assign, reg1, "trp_calatrava_knight"),
			(try_end),
		#original
		(else_try),
			(try_begin),
			(neg|faction_slot_eq, ":troop_faction", slot_faction_freelancer_troop, 0),
			(faction_get_slot, reg1, ":troop_faction", slot_faction_freelancer_troop),
			(else_try),
			(faction_get_slot, reg1, ":troop_faction", ":tier"),
			(try_end),
			#(else_try),
			#tom - renown modification
			#(try_begin), #knight
			#  (troop_slot_ge, "trp_player", slot_troop_renown, 120),
			#  (faction_get_slot, reg1, ":troop_faction", slot_faction_tier_1_castle_troop),
			#  (display_message, "@KNIGHT"),
			#(else_try), #townsman
			#  (troop_slot_ge, "trp_player", slot_troop_renown, 80),
			#  (faction_get_slot, reg1, ":troop_faction", slot_faction_tier_1_town_troop),
			#  (display_message, "@TOWN"),
			#(else_try), #peasant
			#  (faction_get_slot, reg1, ":troop_faction", slot_faction_tier_1_troop),
			#  (display_message, "@PEASANT"),
			#(try_end),
			#(try_end),
		(try_end),
	])