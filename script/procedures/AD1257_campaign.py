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

# script_raf_process_alarms
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
		#called from triggers
raf_process_alarm =	(
	"raf_process_alarm",
			[
			(store_script_param, ":center_no", 1),
			
			#(display_message, "@raf_process_alarm"),
			
			(party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
			(party_set_slot, ":center_no", slot_center_sortie_strength, 0),
			(party_set_slot, ":center_no", slot_center_sortie_enemy_strength, 0),
			
			(assign, ":spotting_range", 3),
			(try_begin),
				(is_currently_night),
				(assign, ":spotting_range", 2),
			(try_end),
			
			(try_begin),
				(party_slot_eq, ":center_no", slot_center_has_watch_tower, 1),
				(val_mul, ":spotting_range", 2),
			(else_try),
				(neg|is_between, ":center_no", villages_begin, villages_end),
				(val_add, ":spotting_range", 1),
				(val_mul, ":spotting_range", 2),
			(try_end),
			
			(store_faction_of_party, ":center_faction", ":center_no"),
			
			(try_for_parties, ":party_no"),
				(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
				(eq, ":party_no", "p_main_party"),
				
				(store_faction_of_party, ":party_faction", ":party_no"),
				
				(try_begin),
				(eq, ":party_no", "p_main_party"),
				(assign, ":party_faction", "$players_kingdom"),
				(try_end),
				
				(try_begin),
				(eq, ":party_faction", ":center_faction"),
				
				(store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
				(le, ":distance", ":spotting_range"),
				
				(party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
				(party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
				(val_add, ":sortie_strength", ":cached_strength"),
				(party_set_slot, ":center_no", slot_center_sortie_strength, ":sortie_strength"),
				(else_try),
				(neq, ":party_faction", ":center_faction"),
				
				(store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
				
				(try_begin),
					(lt, ":distance", 10),
					(store_current_hours, ":hours"),
					(store_sub, ":faction_recce_slot", ":party_faction", kingdoms_begin),
					(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
					(party_set_slot, ":center_no", ":faction_recce_slot", ":hours"),
				(try_end),
				
				(store_relation, ":reln", ":center_faction", ":party_faction"),
				(lt, ":reln", 0),
				
				(try_begin),
					(le, ":distance", ":spotting_range"),
					
					(party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
					(party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
					(val_add, ":enemy_strength", ":cached_strength"),
					(party_set_slot, ":center_no", slot_center_sortie_enemy_strength, ":enemy_strength"),
					(party_set_slot, ":center_no", slot_center_last_spotted_enemy, ":party_no"),
				(try_end),
				(try_end),
			(try_end),
			
		])
		
##script_set_sea_icons - tom made
	##Input: none
	##output: none
	##description: Option trigger - moving party icons to default
set_sea_icons=	(
	"set_sea_icons",
	  [
	  (try_for_parties, ":cur_party"),
		  (party_get_template_id, ":cur_template", ":cur_party"),
		  (try_begin),
			(eq, ":cur_template", "pt_kingdom_hero_party"),
			(party_set_icon,":cur_party","icon_flagbearer_a"),
		  (else_try),
		   (eq, ":cur_template", "pt_kingdom_caravan_party"),
		   (party_set_icon,":cur_party","icon_mule"),
		  (else_try),
			(this_or_next | eq, ":cur_template", "pt_desert_bandits"),
			(eq, ":cur_template", "pt_deserters"),
			(party_set_icon,":cur_party","icon_vaegir_knight"),
		  (else_try),
		    (this_or_next|eq, ":cur_template", "pt_merc_party"),
			(this_or_next|eq, ":cur_template", "pt_prisoner_train_party"),
			(this_or_next|eq, ":cur_template", "pt_patrol_party"),
			(this_or_next|eq, ":cur_template", "pt_ghibellines"),
			(this_or_next|eq, ":cur_template", "pt_guelphs"),
			(eq, ":cur_template", "pt_manhunters"),
			(party_set_icon,":cur_party","icon_gray_knight"),      
		  (else_try),
			(eq, ":cur_template", "pt_steppe_bandits"),
			(party_set_icon,":cur_party","icon_khergit"),
		  (else_try),
			(this_or_next|eq, ":cur_template", "pt_peasant_rebels_euro"),
			(eq, ":cur_template", "pt_village_farmers"),
			(party_set_icon,":cur_party","icon_peasant"),    
		  (else_try),
			(eq, ":cur_template", "pt_cattle_herd"),
			(party_set_icon,":cur_party","icon_cattle"),    
		  (else_try),
			(this_or_next | eq, ":cur_template", "pt_manhunters"),
			(this_or_next | eq, ":cur_template", "pt_dplmc_recruiter"),
			(this_or_next | eq, ":cur_template", "pt_crusaders"),
			(eq, ":cur_template", "pt_merchant_caravan"),
			(party_set_icon,":cur_party","icon_gray_knight"),
		  (else_try),
			(this_or_next|party_slot_eq,":cur_party", slot_party_type, spt_patrol),
			(party_slot_eq,":cur_party", slot_party_type, spt_prisoner_train),      
			(party_set_icon,":cur_party","icon_gray_knight"),      
		  (else_try),
			(this_or_next|eq, ":cur_template", "pt_looters"),
			(this_or_next|eq, ":cur_template", "pt_forest_bandits"),
			(this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
			(this_or_next|eq, ":cur_template", "pt_taiga_bandits"),
			(this_or_next|eq, ":cur_template", "pt_curonians"),
			(this_or_next|eq, ":cur_template", "pt_prussians"),
			(this_or_next|eq, ":cur_template", "pt_samogitians"),
			(this_or_next|eq, ":cur_template", "pt_yotvingians"),
			(this_or_next|eq, ":cur_template", "pt_welsh"),
			(this_or_next|eq, ":cur_template", "pt_robber_knights"),
			(this_or_next|eq, ":cur_template", "pt_troublesome_bandits"),
			(this_or_next|eq, ":cur_template", "pt_bandits_awaiting_ransom"),
			(eq, ":cur_template", "pt_sea_raiders"),
			(party_set_icon,":cur_party","icon_axeman"),
		  (try_end),
	  (try_end),
	  ])