from header import *

# script_init_ai_calculation
		# Input: none
		# Output: none
init_ai_calculation = (
	"init_ai_calculation",
			[
				(try_for_range, ":cur_troop", heroes_begin, heroes_end),
					(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
					(troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
					(party_is_active, ":cur_party"),
					(store_troop_faction, ":fac", ":cur_troop"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_strength", ":cur_party", 0), #will update slot_party_cached_strength
				(try_end),
				
				(call_script, "script_party_calculate_strength", "p_main_party", 0), #will update slot_party_cached_strength
				
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":fac", ":cur_center"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_strength", ":cur_center", 0), #will update slot_party_cached_strength
				(try_end),
				
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":fac", ":cur_center"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", ":cur_center"),
				(try_end),
				
				(try_for_range, ":cur_troop", heroes_begin, heroes_end),
					(troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
					(gt, ":cur_troop_party", 0),
					(party_is_active, ":cur_troop_party"),
					(store_troop_faction, ":fac", ":cur_troop"),
					(eq, ":fac", "$g_ai_kingdom"),
					(call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", ":cur_troop_party"),
				(try_end),
				(call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", "p_main_party"),
		])

		
		# script_recalculate_ais
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		#When a lord changes factions
		#When a center changes factions
		#When a center is captured
		#When a marshal is defeated
		#Every 23 hours
recalculate_ais = (
	"recalculate_ais",
			[
				# rafi
				# (assign, ":max_recalculations", 3), #tom was 3
				# (assign, ":recalculations_done", 0),
				
				#(assign, ":recalculate_all", 1), #tom no need?
				
				#(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
				# (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
				# (faction_slot_eq, ":cur_kingdom", slot_faction_recalculate_ai, 0),
				
				# (faction_get_slot, ":last_calculation", ":cur_kingdom", slot_faction_last_ai_calculation),
				# (try_begin),
				# (lt, ":last_calculation", 0),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
				# (try_end),
				
				# (store_current_hours, ":time"),
				# (val_sub, ":time", ":last_calculation"),
				
				# (try_begin),
				# (gt, ":time", 6),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
				# (str_store_faction_name, s21, ":cur_kingdom"),
				# (assign, reg21, ":time"),
				# #(display_message, "@faction {s21} overdue for recalculation {reg21}, adding"),
				# (try_end),
				# (try_end),
				
				# (try_begin),
				# (eq, ":recalculate_all", 255),
				# (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
				# (try_end),
				# (try_end),
				
				(call_script, "script_init_ai_calculation"),
				
				#(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
				(assign, ":faction_no", "$g_ai_kingdom"),
				(try_begin),
					(assign, reg8, ":faction_no"),
					(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
					
					# (val_add, ":recalculations_done", 1),
					# (le, ":recalculations_done", ":max_recalculations"),
					
					(store_current_hours, ":time"),
					(faction_set_slot, ":faction_no", slot_faction_last_ai_calculation, ":time"),
					
					#(str_store_faction_name, s21, ":faction_no"),
					#(display_message, "@AI recalculated for {s21}"),
					#(neg|faction_slot_eq, ":faction_no",  slot_faction_marshall, "trp_player"),
					(call_script, "script_decide_faction_ai", ":faction_no"),
				(try_end),
				
				(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
					(store_troop_faction, ":faction_no", ":troop_no"),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(eq, ":faction_no", "$g_ai_kingdom"),
					(call_script, "script_calculate_troop_ai", ":troop_no"),
				(try_end),
				
				# (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
				# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 0),
				# (try_end),
		])
		
		# script_calculate_troop_ai
		# Input: troop_no
		# Output: none
		#Now called directly from scripts
calculate_troop_ai = (
	"calculate_troop_ai",
			[
				(store_script_param, ":troop_no", 1),
				(try_begin),
					(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
					(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
					(gt, ":party_no", 0),
					(party_is_active, ":party_no"),
					
					(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
					(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
				(try_end),
		])
		