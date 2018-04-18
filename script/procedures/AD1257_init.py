from header import *

#script_raf_initialize_aristocracy
	# NOTE: sets kings, lords, and ladies age, occupation, reputation
	#		also assigns wifes/hsubands, daughters/sons, widows
	# INPUT: none
	# OUTPUT: none
raf_initialize_aristocracy = ("raf_initialize_aristocracy",
		[
			(assign, ":cur_lady", "trp_kingdom_2_lady_1"),
			
			# King ages
			(try_for_range, ":cur_troop", kings_begin, kings_end),
				(troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
				(store_random_in_range, ":age", 50, 60),
				(troop_set_slot, ":cur_troop", slot_troop_age, ":age"),
			(try_end),
			
			(try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
				(troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
				(store_random_in_range, ":reputation", 20, 26),
				(try_begin),
					(eq, ":reputation", 20),
					(assign, ":reputation", lrep_conventional),
				(try_end),
				(troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":reputation"),
			(try_end),
			
			(try_for_range, ":cur_troop", lords_begin, lords_end),
				(troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
				(store_random_in_range, ":reputation", 0, 8),
				(troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":reputation"),
			(try_end),
			
			(try_for_range, ":cur_troop", pretenders_begin, pretenders_end),
				(troop_set_slot, ":cur_troop", slot_troop_occupation, slto_inactive_pretender),
				(store_random_in_range, ":age", 25, 30),
				(troop_set_slot, ":cur_troop", slot_troop_age, ":age"),
			(try_end),
			
			(try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				
				(call_script, "script_raf_count_kingdom_lords_and_ladies", ":kingdom"),
				(assign, ":lords", reg0),
				(assign, ":ladies", reg1),
				(assign, ":lords_begin", reg3),
				(assign, ":ladies_begin", reg4),
		(gt, ":ladies", 0),
				(store_add, ":lords_end", ":lords_begin", ":lords"),
				#(store_add, ":ladies_end", ":ladies_begin", ":ladies"),
				
				(store_div, ":unmarried_young", ":lords", 5),
				(store_mul, ":unmarried_old", ":unmarried_young", 2),
				(store_mul, ":patriarchs", ":unmarried_young", 2),
				
				(store_add, ":sisters_begin", ":ladies_begin", ":patriarchs"),
				(store_add, ":daughters_begin", ":sisters_begin", ":unmarried_old"),
				
				(store_add, ":patriarchs_end", ":lords_begin", ":patriarchs"),
				(val_sub, ":patriarchs_end", 1),
				
				(store_sub, ":possible_fathers", ":patriarchs", 2),
				
				(store_add, ":unmarried_old_begin", ":patriarchs_end", 1),
				(store_add, ":unmarried_old_end", ":unmarried_old_begin", ":unmarried_old"),
				(val_sub, ":unmarried_old_end", 1),
				
				(store_add, ":sons_begin", ":unmarried_old_end", 1),
				
				(assign, ":index", 0),
				
				(try_begin),
					(neq, ":lords", ":ladies"),
					(str_store_faction_name, s25, ":kingdom"),
					(display_message, "@--DEBUG-- count of lords and ladies for {s25} is not equal"),
				(try_end),
				
				
				# PATRIARCHS
				(assign, ":index", 0),
				(try_for_range, ":cur_lord", ":lords_begin", ":unmarried_old_begin"),
					
					(store_add, ":cur_lady", ":ladies_begin", ":index"),
					
					(store_random_in_range, ":father", 0, ":possible_fathers"), #six possible fathers
					(store_add, ":ancestor_seed", ":lords_end", 10000),
					(val_add, ":father", ":ancestor_seed"),
					(troop_set_slot, ":cur_lord", slot_troop_father, ":father"),
					
					(store_random_in_range, ":age", 45, 64),
					(call_script, "script_init_troop_age", ":cur_lord", ":age"),
					
					(store_random_in_range, ":reputation", 0, 8),
					(troop_set_slot, ":cur_lord", slot_lord_reputation_type, ":reputation"),
					
					# WIFE
					(try_begin),
						(troop_set_slot, ":cur_lord", slot_troop_spouse, ":cur_lady"),
						(troop_set_slot, ":cur_lady", slot_troop_spouse, ":cur_lord"),
						
						(store_random_in_range, ":wife_reputation", 20, 26),
						(try_begin),
							(eq, ":wife_reputation", 20),
							(assign, ":wife_reputation", lrep_conventional),
						(try_end),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":wife_reputation"),
						
						(store_random_in_range, ":age", 35, 54),
						(call_script, "script_init_troop_age", ":cur_lady", ":age"),
						(call_script, "script_add_lady_items", ":cur_lady"),
					(try_end),
					
					# DAUGHTER
					(try_begin),
						(lt, ":index", ":unmarried_young"),
						
						(store_add, ":cur_daughter", ":daughters_begin", ":index"),
						(troop_set_slot, ":cur_daughter", slot_troop_father, ":cur_lord"),
						(store_random_in_range, ":age", 16, 25),
						(call_script, "script_init_troop_age", ":cur_daughter", ":age"),
						(troop_set_slot, ":cur_daughter", slot_troop_mother, ":cur_lady"),
			#tom
						(store_random_in_range, ":lady_reputation", lrep_conventional, 34), #33% chance of father-derived
			(try_begin),
				(le, ":lady_reputation", 25),
				(troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":lady_reputation"),
			(else_try),	
				(eq, ":lady_reputation", 26),
				(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
			(else_try),	
				(eq, ":lady_reputation", 27),
				(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
			(else_try),
				(assign, ":guardian_reputation", ":reputation"),
				(try_begin),
					(this_or_next|eq, ":guardian_reputation", lrep_martial),
						(eq, ":guardian_reputation", 0),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
				(else_try),		
					(eq, ":guardian_reputation", lrep_quarrelsome),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_otherworldly),
				(else_try),		
					(eq, ":guardian_reputation", lrep_selfrighteous),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
				(else_try),		
					(eq, ":guardian_reputation", lrep_cunning),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
				(else_try),		
					(eq, ":guardian_reputation", lrep_goodnatured),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
				(else_try),		
					(eq, ":guardian_reputation", lrep_debauched),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
				(else_try),		
					(eq, ":guardian_reputation", lrep_upstanding),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
				(try_end),
			(try_end),
			#tom
						(call_script, "script_add_lady_items", ":cur_daughter"),
					(try_end),
					
					# SONS
					(try_begin),
						(ge, ":index", ":unmarried_young"),
						
						(assign, ":cur_son", ":sons_begin"),
						(val_add, ":cur_son", ":index"),
						(val_sub, ":cur_son", ":unmarried_young"),
						
						(try_begin),
							(troop_set_slot, ":cur_son", slot_troop_father, ":cur_lord"),
							(troop_set_slot, ":cur_son", slot_troop_mother, ":cur_lady"),
						(try_end),
						(store_random_in_range, ":age", 16, 25),
						(call_script, "script_init_troop_age", ":cur_son", ":age"),
					(try_end),
					
					(val_add, ":index", 1),
				(try_end),
				# END PATRIARCHS
				
				# UNMARRIED OLD
				(assign, ":index", 0),
				(try_for_range, ":cur_lord", ":unmarried_old_begin", ":sons_begin"),
					
					# (store_random_in_range, ":father", 0, ":possible_fathers"), #six possible fathers
					# (store_add, ":ancestor_seed", ":lords_end", 10000),
					# (val_add, ":father", ":ancestor_seed"),
					# (troop_set_slot, ":cur_lord", slot_troop_father, ":father"),
					
					(store_random_in_range, ":age", 25, 36),
					(store_random_in_range, ":reputation", 0, 8),
					(troop_set_slot, ":cur_lord", slot_lord_reputation_type, ":reputation"),
					(call_script, "script_init_troop_age", ":cur_lord", ":age"),
					
					(try_begin),
						(store_add, ":cur_sister", ":sisters_begin", ":index"),
						(store_random_in_range, ":sister_reputation", 20, 26),
						(try_begin),
							(eq, ":sister_reputation", 20),
							(assign, ":sister_reputation", lrep_conventional),
						(try_end),
						(troop_set_slot, ":cur_sister", slot_lord_reputation_type, ":sister_reputation"),
						
						(troop_set_slot, ":cur_sister", slot_troop_guardian, ":cur_lord"),
						
						(call_script, "script_init_troop_age", ":cur_sister", 21),
						(call_script, "script_add_lady_items", ":cur_sister"),
					(try_end),
					(val_add, ":index", 1),
				(try_end),
			(try_end),

	])