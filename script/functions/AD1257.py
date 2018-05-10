from header import *

# count lords and ladies?
# NOTE: it purposes? idk. CTRL+F'd, I think this one is deprecated
# INPUT: kingdom id
# OUTPUT: reg0 - lord count, reg1 - ladies count, reg3 - lords start, reg4 - ladies start
raf_count_kingdom_lords_and_ladies = (
	"raf_count_kingdom_lords_and_ladies",
		[
			(store_script_param, ":kingdom", 1),
			
			(assign, ":lords", 0),
			(assign, ":ladies", 0),
		(assign, reg3, 0),
		(assign, reg4, 0),
			
			(try_for_range, ":cur_troop", lords_begin, lords_end),
				(store_faction_of_troop, ":faction", ":cur_troop"),
				(eq, ":faction", ":kingdom"),
				(try_begin),
					(eq, ":lords", 0),
					(assign, reg3, ":cur_troop"),
				(try_end),
				(val_add, ":lords", 1),
			(try_end),
			(try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
				(store_faction_of_troop, ":faction", ":cur_troop"),
				(eq, ":faction", ":kingdom"),
				(try_begin),
					(eq, ":ladies", 0),
					(assign, reg4, ":cur_troop"),
				(try_end),
				(val_add, ":ladies", 1),
			(try_end),
			
			(assign, reg0, ":lords"),
			(assign, reg1, ":ladies"),
		])

#script_lord_find_alternative_faction_old
	#WARNING: this is totally new procedure (not present in native). 1257AD devs
	#reverted back to 1.134 
	#INPUT: troop_no
	#OUTPUT: new_faction
lord_find_alternative_faction_old = (
	"lord_find_alternative_faction_old", #Also, make it so that lords will try to keep at least one center unassigned
	[
		(store_script_param, ":troop_no", 1),
		(store_faction_of_troop, ":orig_faction", ":troop_no"),
		
		##tom - check if the troops faction have centers - if not it needs force migrate
		(assign, ":force_migration", 0),
		(try_begin),
			(neq, ":orig_faction", "fac_player_supporters_faction"), ##player faction is not affected
		(assign, ":head", walled_centers_end),
		(assign, ":force_migration", 1), ##migrate!
		(try_for_range, ":center", walled_centers_begin, ":head"),
			(store_faction_of_party, ":center_faction", ":center"),
			(eq, ":center_faction", ":orig_faction"),
			(assign, ":force_migration", 0), #do not migrate
			(assign, ":head", -1), ##break
		(try_end),
		(try_end),
		##tom
		
		(assign, ":new_faction", -1),
		(assign, ":score_to_beat", -5),
		##tom
		(try_begin),
			(eq, ":force_migration", 1), 
			(assign, ":score_to_beat", -100),
		(try_end),
		##tom
		
		#Factions with an available center
		(try_for_range, ":center_no", centers_begin, centers_end),
			(this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_unassigned),
			(party_slot_eq, ":center_no", slot_town_lord, stl_rejected_by_player),
			(store_faction_of_party, ":center_faction", ":center_no"),
			(neq, ":center_faction", ":orig_faction"),
			(faction_get_slot, ":liege", ":center_faction", slot_faction_leader),
			(this_or_next|neq, ":liege", "trp_player"),
			(ge, "$player_right_to_rule", 25),	    
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
			(assign, ":liege_relation", reg0),
			(gt, ":liege_relation", ":score_to_beat"),
			(assign, ":new_faction", ":center_faction"),
			(assign, ":score_to_beat", ":liege_relation"),
		(try_end),
		
		#Factions without an available center
		(try_begin),
			(eq, ":new_faction", -1),
			(assign, ":score_to_beat", 0),
			##tom
		(try_begin),
			(eq, ":force_migration", 1), 
			(assign, ":score_to_beat", -100),
		(try_end),
		##tom
			(try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
				(faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
				(faction_get_slot, ":liege", ":kingdom", slot_faction_leader),
				(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
				(assign, ":liege_relation", reg0),		
				(gt, ":liege_relation", ":score_to_beat"),
				
				(assign, ":new_faction", ":kingdom"),
				(assign, ":score_to_beat", ":liege_relation"),		
			(try_end),
		(try_end),
		
		(assign, reg0, ":new_faction"),	
	])
	
	