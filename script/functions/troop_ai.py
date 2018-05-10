from header import *

	#script_npc_decision_checklist_troop_follow_or_not
	# WARNING: behaviour is different from native. modified by 1257AD devs
	# INPUT: troop_no
	# OUTPUT: reg0
npc_decision_checklist_troop_follow_or_not = (
	"npc_decision_checklist_troop_follow_or_not", [
		
		(store_script_param, ":troop_no", 1),
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		(faction_get_slot, ":faction_ai_state", ":faction_no", slot_faction_ai_state),
		
		(troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
		(faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
		
		(assign, ":result", 0),
		(try_begin),
			(eq, ":faction_marshall", -1),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__i_am_acting_independently_because_no_marshal_is_appointed"),
			(try_end),
		(else_try),
			(troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
			(neg|party_is_active, ":faction_marshall_party"),
			
			#Not doing an offensive
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__i_am_acting_independently_because_our_marshal_is_currently_indisposed"),
			(try_end),
		(else_try),
			(neq, ":faction_ai_state", sfai_attacking_center),
			(neq, ":faction_ai_state", sfai_raiding_village),
			(neq, ":faction_ai_state", sfai_attacking_enemies_around_center),
			(neq, ":faction_ai_state", sfai_attacking_enemy_army),
			(neq, ":faction_ai_state", sfai_gathering_army),
			
			#Not doing an offensive
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__i_am_acting_independently_because_our_realm_is_currently_not_on_campaign"),
			(try_end),
		(else_try),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_marshall"),
			(assign, ":relation_with_marshall", reg0),
			
			(try_begin),
			(le, ":relation_with_marshall", -10),
			(assign, ":acceptance_level", 10000),
			(else_try),
			(store_mul, ":acceptance_level", ":relation_with_marshall", -1000),
			(try_end),
			
			(val_add, ":acceptance_level", 1500),
			
			# rafi
			(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			(try_begin),
			(neq, ":faction_no", "$players_kingdom"),
			(try_begin),
				(eq, ":reduce_campaign_ai", 0), #hard
				(val_add, ":acceptance_level", -1250),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #moderate
			(else_try),
				(eq, ":reduce_campaign_ai", 2), #easy
				(val_add, ":acceptance_level", 1250),
			(try_end),
			(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, "trp_player"),
			(try_begin),
				(eq, ":reduce_campaign_ai", 0), #hard/player's faction
				(val_add, ":acceptance_level", -1000),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #moderate/player's faction
				(val_add, ":acceptance_level", -1500),
			(else_try),
				(eq, ":reduce_campaign_ai", 2), #easy/player's faction
				(val_add, ":acceptance_level", -2000),
			(try_end),
			(try_end),
			
			(troop_get_slot, ":temp_ai_seed", ":troop_no", slot_troop_temp_decision_seed),
			
			(le, ":temp_ai_seed", ":acceptance_level"),
			
			#Very low opinion of marshall
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__i_am_not_accompanying_the_marshal_because_i_fear_that_he_may_lead_us_into_disaster"),
			(try_end),
			#Make nuanced, depending on personality type
		(else_try),
			(troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_faction_marshall),
			
			(lt, ":relation_with_marshall", 0),
			(ge, ":marshal_controversy", 50),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str_i_am_not_accompanying_the_marshal_because_i_question_his_judgment"),
			(try_end),
		(else_try),
			(troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_faction_marshall),
			(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":faction_marshall"),
			
			(lt, ":relation_with_marshall", 5),
			(ge, ":marshal_controversy", 80),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str_i_am_not_accompanying_the_marshal_because_will_be_reappointment"),
			(try_end),
		(else_try),
			#(lt, ":relation_with_marshall", 45),
			#(eq, ":faction_marshall", "trp_player"), #moved below as only effector. Search "think about this".
			(store_sub, ":relation_with_marshal_difference", 50, ":relation_with_marshall"),
			
			#for 50 relation with marshal ":acceptance_level" will be 0
			#for 20 relation with marshal ":acceptance_level" will be 2100
			#for 10 relation with marshal ":acceptance_level" will be 2800
			#for 0 relation with marshal ":acceptance_level" will be 3500
			#for -10 relation with marshal ":acceptance_level" will be 4200
			#average is about 2500
			(store_mul, ":acceptance_level", ":relation_with_marshal_difference", 70),
			
			(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			(try_begin),
			(neq, ":faction_no", "$players_kingdom"),
			
			(try_begin),
				(eq, ":reduce_campaign_ai", 0), #hard
				(val_add, ":acceptance_level", -1200),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #moderate
			(else_try),
				(eq, ":reduce_campaign_ai", 2), #easy
				(val_add, ":acceptance_level", 1200),
			(try_end),
			(else_try),
			(eq, ":faction_marshall", "trp_player"),
			
			(try_begin),
				(eq, ":reduce_campaign_ai", 0), #hard
				(val_add, ":acceptance_level", -1000),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #moderate
				(val_add, ":acceptance_level", -1500),
			(else_try),
				(eq, ":reduce_campaign_ai", 2), #easy
				(val_add, ":acceptance_level", -2000),
			(try_end),
			(try_end),
			
			(try_begin),
			(eq, ":troop_reputation", lrep_selfrighteous),
			(val_add, ":acceptance_level", 1500),
			(else_try),
			(this_or_next|eq, ":troop_reputation", lrep_martial),
			(this_or_next|eq, ":troop_reputation", lrep_roguish),
			(eq, ":troop_reputation", lrep_quarrelsome),
			(val_add, ":acceptance_level", 1000),
			(else_try),
			(eq, ":troop_reputation", lrep_cunning),
			(val_add, ":acceptance_level", 500),
			(else_try),
			(eq, ":troop_reputation", lrep_upstanding), #neutral
			(else_try),
			(this_or_next|eq, ":troop_reputation", lrep_benefactor), #helper
			(eq, ":troop_reputation", lrep_goodnatured),
			(val_add, ":acceptance_level", -500),
			(else_try),
			(eq, ":troop_reputation", lrep_custodian), #very helper
			(val_add, ":acceptance_level", -1000),
			(try_end),
			
			(try_begin),
			(troop_slot_eq, ":faction_marshall", slot_lord_reputation_type, lrep_quarrelsome),
			(val_add, ":acceptance_level", -750),
			(else_try),
			(this_or_next|troop_slot_eq, ":faction_marshall", slot_lord_reputation_type, lrep_martial),
			(troop_slot_eq, ":faction_marshall", slot_lord_reputation_type, lrep_upstanding),
			(val_add, ":acceptance_level", -250),
			(try_end),
			
			(val_add, ":acceptance_level", 2000), #tom was 2000
			#average become 2500 + 2000 = 4500, (45% of lords will not join campaign because of this reason. (33% for hard, 57% for easy, 30% for marshal player))

			#tom feudal problematic gathering
			(try_begin),
				(ge, "$feudal_inefficency", 1),
				(neq, ":faction_marshall", "trp_player"),
			(store_mul, ":inefficency", 1500, "$feudal_inefficency"),
			(val_add, ":acceptance_level", ":inefficency"),
			(try_end),
			#tom
			
			(troop_get_slot, ":temp_ai_seed", ":troop_no", slot_troop_temp_decision_seed),
			
			# (assign, reg0, ":acceptance_level"),
			# (assign, reg1, ":temp_ai_seed"),
			# (str_store_troop_name, s1, ":troop_no"),
			
			# (display_message, "@{s1} acceptance level: {reg0}, seed:{reg1}."),
			
			(le, ":temp_ai_seed", ":acceptance_level"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str_i_am_not_accompanying_the_marshal_because_i_can_do_greater_deeds"),
			(try_end),
			
			#(try_begin),
			#  (ge, "$cheat_mode", 1),
			#  (assign, reg7, ":acceptance_level"),
			#  (assign, reg8, ":relation_with_marshall"),
			#  (display_message, "@{!}DEBUGS : acceptance level : {reg7}, relation with marshal : {reg8}"),
			#(try_end),
		(else_try),
			(store_current_hours, ":hours_since_last_faction_rest"),
			(faction_get_slot, ":last_rest_time", ":faction_no", slot_faction_ai_last_rest_time),
			(val_sub, ":hours_since_last_faction_rest", ":last_rest_time"),
			
			#nine days on average, marshal will usually end after 10 days
			#ozan changed, 360 hours (15 days) in average, marshal cannot end it during a siege attack/defence anymore.
			(assign, ":troop_campaign_limit", 360),
			(store_mul, ":marshal_relation_modifier", ":relation_with_marshall", 6), #ozan changed 4 to 6.
			(val_add, ":troop_campaign_limit", ":marshal_relation_modifier"),
			
			(try_begin),
			(eq, ":troop_reputation", lrep_upstanding),
			(val_mul, ":troop_campaign_limit", 4),
			(val_div, ":troop_campaign_limit", 3),
			(try_end),
			
			(str_store_troop_name, s16, ":faction_marshall"),
			
			(gt, ":hours_since_last_faction_rest", ":troop_campaign_limit"),
			
			#Too long a campaign
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__s16_has_kept_us_on_campaign_on_far_too_long_and_there_are_other_pressing_matters_to_which_i_must_attend"),
			(try_end),
			#Also make nuanced, depending on personality type
		(else_try),
			(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
			(neg|party_is_active, ":party_no"),
			#This string should not occur, as it will only happen if a lord is contemplating following the player
		(else_try),
			(troop_get_slot, ":marshal_party", ":faction_marshall", slot_troop_leaded_party),
			(assign, ":information_radius", 40),
			(try_begin),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
			(assign, ":information_radius", 50),
			(try_end),
			
			(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			(try_begin),
			(neq, ":faction_no", "fac_player_supporters_faction"),
			(neq, ":faction_no", "$players_kingdom"),
			(try_begin),
				(eq, ":reduce_campaign_ai", 2), #easy
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
				(val_add, ":information_radius", -10),
				(else_try),
				(val_add, ":information_radius", -8),
				(try_end),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #moderate
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
				(val_add, ":information_radius", -5),
				(else_try),
				(val_add, ":information_radius", -4),
				(try_end),
			(try_end),
			(else_try),
			(try_begin),
				(eq, ":reduce_campaign_ai", 2), #easy
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
				(val_add, ":information_radius", 25),
				(else_try),
				(val_add, ":information_radius", 20),
				(try_end),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #moderate
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
				(val_add, ":information_radius", 15),
				(else_try),
				(val_add, ":information_radius", 12),
				(try_end),
			(else_try),
				(eq, ":reduce_campaign_ai", 0), #hard
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
				(val_add, ":information_radius", 5),
				(else_try),
				(val_add, ":information_radius", 4),
				(try_end),
			(try_end),
			(try_end),
			
			(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
			(assign, reg17, 0),
			(try_begin),
			(try_begin),
				(neg|is_between, ":faction_object", villages_begin, villages_end),
				(assign, reg17, 1),
			(try_end),
			(try_begin),
				(neg|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
				(assign, reg17, 1),
			(try_end),
			(eq, reg17, 1),
			
			(store_distance_to_party_from_party, ":distance", ":marshal_party", ":party_no"),
			
			(gt, ":distance", ":information_radius"),
			
			(try_begin),
				(eq, ":troop_no", "$g_talk_troop"),
				(str_store_string, s15, "str__i_am_not_participating_in_the_marshals_campaign_because_i_do_not_know_where_to_find_our_main_army"),
			(try_end),
			(else_try),
			(eq, reg17, 0),
			
			(assign, reg17, 1),
			(try_begin),
				#if we are already accompanying marshal forget below.
				(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
				(party_slot_eq, ":party_no", slot_party_ai_object, ":marshal_party"),
				(assign, reg17, 0),
			(try_end),
			(eq, reg17, 1),
			
			#if faction ai is "attacking enemies around a center" is then do not find and compare distance to marshal, find and compare distance to "attacked village"
			(party_get_slot, ":enemy_strength_nearby", ":faction_object", slot_center_sortie_enemy_strength),
			
			(try_begin), #changes between 70..x (as ":enemy_strength_nearby" increases, ":information_radius" increases too.),
				(ge, ":enemy_strength_nearby", 4000),
				(val_sub, ":enemy_strength_nearby", 4000),
				(store_div, ":information_radius", ":enemy_strength_nearby", 200),
				(val_add, ":information_radius", 70),
			(else_try), #changes between 30..70
				(store_div, ":information_radius", ":enemy_strength_nearby", 100),
				(val_add, ":information_radius", 30),
			(try_end),
			
			(store_distance_to_party_from_party, ":distance", ":faction_object", ":party_no"),
			
			(gt, ":distance", ":information_radius"),
			
			(try_begin),
				(eq, ":troop_no", "$g_talk_troop"),
				(str_store_string, s15, "str__i_am_acting_independently_although_some_enemies_have_been_spotted_within_our_borders_they_havent_come_in_force_and_the_local_troops_should_be_able_to_dispatch_them"),
			(try_end),
			(try_end),
			
			(gt, ":distance", ":information_radius"),
		(else_try),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__the_needs_of_the_realm_must_come_first"),
			(try_end),
			(assign, ":result", 1),
		(try_end),
		
		#tom feudal problematic gathering
		# (try_begin),
			# (ge, "$feudal_inefficency", 1),
			# (eq, ":result", 1),
			# (neq, ":faction_marshall", "trp_player"),
			# (store_random_in_range, ":random", 0, 100),
			# (store_mul, ":top", 20, "$feudal_inefficency"),
			# (lt, ":random", ":top"), #0-19
			# (assign, ":result", 0),
		# (try_end),
		#tom end
		
		(assign, reg0, ":result"),
	])
	
	#script_npc_decision_checklist_male_guardian_assess_suitor
	#called from dialogs
	#WARNING: heavily modified by 1257AD devs
	#INPUT: lord, suitor
	#OUTPUT: reg0 result, reg1 explainer_string
npc_decision_checklist_male_guardian_assess_suitor =(
	"npc_decision_checklist_male_guardian_assess_suitor", #parameters from dialog
		[
		(store_script_param, ":lord", 1),
		(store_script_param, ":suitor", 2),
		
		(troop_get_slot, ":lord_reputation", ":lord", slot_lord_reputation_type),
		(store_faction_of_troop, ":lord_faction", ":lord"),
		
		(try_begin),
			(eq, ":suitor", "trp_player"),
			(assign, ":suitor_faction", "$players_kingdom"),
		(else_try),
			(store_faction_of_troop, ":suitor_faction", ":suitor"),
		(try_end),
		(store_relation, ":faction_relation_with_suitor", ":lord_faction", ":suitor_faction"),
		
		(call_script, "script_troop_get_relation_with_troop", ":lord", ":suitor"),
		(assign, ":lord_suitor_relation", reg0),
		
		(troop_get_slot, ":suitor_renown", ":suitor", slot_troop_renown),
		
		
		(assign, ":competitor_found", -1),
		
		(try_begin),
			(eq, ":suitor", "trp_player"),
			(gt, "$marriage_candidate", 0),
			# rafi no TO marriage
			(neq, ":lord_faction", "fac_kingdom_1"),
			(neq, ":suitor_faction", "fac_kingdom_1"),
			
			(try_for_range, ":competitor", lords_begin, lords_end),
			(store_faction_of_troop, ":competitor_faction", ":competitor"),
			(eq, ":competitor_faction", ":lord_faction"),
			(this_or_next|troop_slot_eq, ":competitor", slot_troop_love_interest_1, "$marriage_candidate"),
			(this_or_next|troop_slot_eq, ":competitor", slot_troop_love_interest_2, "$marriage_candidate"),
			(troop_slot_eq, ":competitor", slot_troop_love_interest_3, "$marriage_candidate"),
			
			(call_script, "script_troop_get_relation_with_troop", ":competitor", ":lord"),
			(gt, reg0, 5),
			
			(troop_slot_ge, ":competitor", slot_troop_renown, ":suitor_renown"),  #higher renown than player
			
			(assign, ":competitor_found", ":competitor"),
			(str_store_troop_name, s14, ":competitor"),
			(str_store_troop_name, s16, "$marriage_candidate"),
			(try_end),
		(try_end),
		
		#renown
		(try_begin),
			# rafi no TO marriage
			(eq, ":lord_faction", "fac_kingdom_1"),
			(eq, ":suitor_faction", "fac_kingdom_1"),
			(assign, ":explainer_string", "@I'm sorry, we take vows of chastity here and are not allowed to marry."),
			(assign, ":result", -3),
		(else_try),
			(lt, ":suitor_renown", 50),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_quarrelsome),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
			(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
			(assign, ":explainer_string", "str_excuse_me_how_can_you_possibly_imagine_yourself_worthy_to_marry_into_our_family"),
			(assign, ":result", -3),
		(else_try),
			(lt, ":suitor_renown", 50),
			(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
			
			(assign, ":explainer_string", "str_em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction_fight_hard_count_your_dinars_and_perhaps_some_day_in_the_future_we_may_speak_of_such_things_my_good_man"),
			(assign, ":result", -1),
		(else_try),
			(lt, ":suitor_renown", 50),
			
			(assign, ":explainer_string", "str_em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction"),
			(assign, ":result", -2),
			
		(else_try),
			(lt, ":suitor_renown", 200),
			(neg|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
			(assign, ":explainer_string", "str_it_is_too_early_for_you_to_be_speaking_of_such_things_you_are_still_making_your_mark_in_the_world"),
			
			(assign, ":result", -1),
			
		(else_try), #wrong faction
			(eq, ":suitor", "trp_player"),
			(neq, ":suitor_faction", "$players_kingdom"),
			(str_store_faction_name, s4, ":lord_faction"),
			(this_or_next|eq, ":lord_reputation", lrep_quarrelsome),
			(eq, ":lord_reputation", lrep_debauched),
			(assign, ":explainer_string", "str_you_dont_serve_the_s4_so_id_say_no_one_day_we_may_be_at_war_and_i_prefer_not_to_have_to_kill_my_inlaws_if_at_all_possible"),
			
			(assign, ":result", -1),
			
		(else_try),
			(eq, ":suitor", "trp_player"),
			(neq, ":suitor_faction", "$players_kingdom"),
			(neq, ":lord_reputation", lrep_goodnatured),
			(neq, ":lord_reputation", lrep_cunning),
			
			(assign, ":explainer_string", "str_as_you_are_not_a_vassal_of_the_s4_i_must_decline_your_request_the_twists_of_fate_may_mean_that_we_will_one_day_cross_swords_and_i_would_hope_not_to_make_a_widow_of_a_lady_whom_i_am_obligated_to_protect"),
			
			(assign, ":result", -1),
		(else_try),
			(eq, ":suitor", "trp_player"),
			(lt, ":faction_relation_with_suitor", 0),
			
			(assign, ":explainer_string", "str_as_you_are_not_a_vassal_of_the_s4_i_must_decline_your_request_the_twists_of_fate_may_mean_that_we_will_one_day_cross_swords_and_i_would_hope_not_to_make_a_widow_of_a_lady_whom_i_am_obligated_to_protect"),
			
			(assign, ":result", -1),
			
		(else_try),
			(eq, ":suitor", "trp_player"),
			(neq, "$player_has_homage", 1),
			(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
			
			(assign, ":explainer_string", "str_as_you_are_not_a_pledged_vassal_of_our_liege_with_the_right_to_hold_land_i_must_refuse_your_request_to_marry_into_our_family"),
			
			(assign, ":result", -1),
		(else_try),
			(gt, ":competitor_found", -1),
			
			(this_or_next|eq, ":lord_reputation", lrep_selfrighteous),
			(this_or_next|eq, ":lord_reputation", lrep_debauched),
			(this_or_next|eq, ":lord_reputation", lrep_martial),
			(eq, ":lord_reputation", lrep_quarrelsome),
			
			(assign, ":explainer_string",	"str_look_here_lad__the_young_s14_has_been_paying_court_to_s16_and_youll_have_to_admit__hes_a_finer_catch_for_her_than_you_so_lets_have_no_more_of_this_talk_shall_we"),
			(assign, ":result", -1),
			
		(else_try),
			(lt, ":lord_suitor_relation", -4),
			
			(assign, ":explainer_string", "str_i_do_not_care_for_you_sir_and_i_consider_it_my_duty_to_protect_the_ladies_of_my_household_from_undesirable_suitors"),
			(assign, ":result", -3),
		(else_try),
			(lt, ":lord_suitor_relation", 5),
			
			(assign, ":explainer_string",	"str_hmm_young_girls_may_easily_be_led_astray_so_out_of_a_sense_of_duty_to_the_ladies_of_my_household_i_think_i_would_like_to_get_to_know_you_a_bit_better_we_may_speak_of_this_at_a_later_date"),
			(assign, ":result", -1),
		(else_try),
			
			(assign, ":explainer_string",	"str_you_may_indeed_make_a_fine_match_for_the_young_mistress"),
			(assign, ":result", 1),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":explainer_string"),
		
	])

	#script_npc_decision_checklist_marry_female_pc
	#INPUT: npc
	#OUTPUT: lord_agrees
npc_decision_checklist_marry_female_pc = (
	"npc_decision_checklist_marry_female_pc", #
		[
		(store_script_param, ":npc", 1),
		
		
		(troop_get_slot, ":npc_reputation_type", ":npc", slot_lord_reputation_type),
		
		(call_script, "script_troop_get_romantic_chemistry_with_troop", ":npc", "trp_player"),
		(assign, ":romantic_chemistry", reg0),
		
		(call_script, "script_troop_get_relation_with_troop", ":npc", "trp_player"),
		(assign, ":relation_with_player", reg0),
		
		(assign, ":competitor", -1),
		(try_for_range, ":competitor_candidate", kingdom_ladies_begin, kingdom_ladies_end),
			(this_or_next|troop_slot_eq, ":npc", slot_troop_love_interest_1, ":competitor_candidate"),
			(this_or_next|troop_slot_eq, ":npc", slot_troop_love_interest_2, ":competitor_candidate"),
			(troop_slot_eq, ":npc", slot_troop_love_interest_3, ":competitor_candidate"),
			(call_script, "script_troop_get_relation_with_troop", ":npc", ":competitor"),
			(assign, ":competitor_relation", reg0),
			
			(gt, ":competitor_relation", ":relation_with_player"),
			(assign, ":competitor", ":competitor_candidate"),
		(try_end),
		
		(assign, ":player_possessions", 0),
		(try_for_range, ":center", centers_begin, centers_end),
			(troop_slot_eq, ":center", slot_town_lord, "trp_player"),
			(val_add, ":player_possessions", 1),
		(try_end),
		
		(assign, ":lord_agrees", 0),
		#reasons for refusal
		(try_begin),
			(troop_slot_ge, "trp_player", slot_troop_betrothed, active_npcs_begin),
			(neg|troop_slot_eq, "trp_player", slot_troop_betrothed, ":npc"),
			
			(str_store_string, s14, "str_my_lady_engaged_to_another"),
		(else_try),
			#bad relationship - minor
			(lt, ":relation_with_player", -3),
			(this_or_next|eq, ":npc_reputation_type", lrep_upstanding),
			(this_or_next|eq, ":npc_reputation_type", lrep_cunning),
			(eq, ":npc_reputation_type", lrep_goodnatured),
			
			(str_store_string, s14, "str_madame__given_our_relations_in_the_past_this_proposal_is_most_surprising_i_do_not_think_that_you_are_the_kind_of_woman_who_can_be_bent_to_a_hushands_will_and_i_would_prefer_not_to_have_our_married_life_be_a_source_of_constant_acrimony"),
			
		(else_try), #really bad relationship
			(lt, ":relation_with_player", -10),
			
			(this_or_next|eq, ":npc_reputation_type", lrep_quarrelsome),
			(this_or_next|eq, ":npc_reputation_type", lrep_debauched),
			(eq, ":npc_reputation_type", lrep_selfrighteous),
			
			(str_store_string, s14, "str_i_would_prefer_to_marry_a_proper_maiden_who_will_obey_her_husband_and_is_not_likely_to_split_his_head_with_a_sword"),
		(else_try),
			(lt, ":romantic_chemistry", 5),
			
			(str_store_string, s14, "str_my_lady_not_sufficient_chemistry"),
			
		(else_try), #would prefer someone more ladylike
			(this_or_next|eq, ":npc_reputation_type", lrep_upstanding),
			(eq, ":npc_reputation_type", lrep_martial),
			
			(str_store_string, s14, "str_my_lady_while_i_admire_your_valor_you_will_forgive_me_if_i_tell_you_that_a_woman_like_you_does_not_uphold_to_my_ideal_of_the_feminine_of_the_delicate_and_of_the_pure"),
		(else_try),
			(eq, ":npc_reputation_type", lrep_quarrelsome),
			(lt, ":romantic_chemistry", 15),
			
			(str_store_string, s14, "str_nah_i_want_a_woman_wholl_keep_quiet_and_do_what_shes_told_i_dont_think_thats_you"),
		(else_try), #no properties
			(this_or_next|eq, ":npc_reputation_type", lrep_selfrighteous),
			(eq, ":npc_reputation_type", lrep_debauched),
			
			(ge, ":romantic_chemistry", 10),
			(eq, ":player_possessions", 0),
			
			(str_store_string, s14, "str_my_lady_you_are_possessed_of_great_charms_but_no_properties_until_you_obtain_some_to_marry_you_would_be_an_act_of_ingratitude_towards_my_ancestors_and_my_lineage"),
			
		(else_try), #you're a nobody - I can do better
			(this_or_next|eq, ":npc_reputation_type", lrep_selfrighteous),
			(eq, ":npc_reputation_type", lrep_debauched),
			
			(eq, ":player_possessions", 0),
			
			(str_store_string, s14, "str_my_lady_you_are_a_woman_of_no_known_family_of_no_possessions__in_short_a_nobody_do_you_think_that_you_are_fit_to_marry_into_may_family"),
		(else_try), #just not that into you
			(lt, ":romantic_chemistry", 5),
			(lt, ":relation_with_player", 20),
			
			(neq, ":npc_reputation_type", lrep_debauched),
			(neq, ":npc_reputation_type", lrep_selfrighteous),
			
			(str_store_string, s14, "str_my_lady__forgive_me__the_quality_of_our_bond_is_not_of_the_sort_which_the_poets_tell_us_is_necessary_to_sustain_a_happy_marriage"),
			
		(else_try), #you're a liability, given your relation with the liege
			(eq, ":npc_reputation_type", lrep_cunning),
			(faction_get_slot, ":leader", slot_faction_leader, "$g_talk_troop_faction"),
			(str_store_troop_name, s4, ":leader"),
			(call_script, "script_troop_get_relation_with_troop", ":leader", "trp_player"),
			(lt, reg0, -10),
			
			(str_store_string, s14, "str_um_i_think_that_if_i_want_to_stay_on_s4s_good_side_id_best_not_marry_you"),
		(else_try),	#part of another faction
			(gt, "$players_kingdom", 0),
			(neq, "$players_kingdom", "$g_talk_troop_faction"),
			(faction_get_slot, ":leader", slot_faction_leader, "$g_talk_troop_faction"),
			(troop_get_type, reg4, ":leader"),
			
			(str_store_string, s14, "str_you_serve_another_realm_i_dont_see_s4_granting_reg4herhis_blessing_to_our_union"),
		(else_try), #there's a competitor
			(gt, ":competitor", -1),
			(str_store_troop_name, s4, ":competitor"),
			
			(str_store_string, s14, "str_madame_my_heart_currently_belongs_to_s4"),
			
		(else_try),
			(lt, ":relation_with_player", 10),
			(assign, ":lord_agrees", 2),
			
			(str_store_string, s14, "str_my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_shall_give_your_proposal_consideration"),
		(else_try),
			(assign, ":lord_agrees", 1),
			
			(str_store_string, s14, "str_my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_would_be_most_honored_were_you_to_become_my_wife"),
		(try_end),
		
		
		(assign, reg0, ":lord_agrees"),
		
		])

		#script_npc_decision_checklist_evaluate_enemy_center_for_attack
	#WARNING: modified by 1257AD devs
	#INPUT: troop_no, potential_target, attack_by_faction, all_vassals_included
	#OUTPUT: result, result_explainer, power_ratio

npc_decision_checklist_evaluate_enemy_center_for_attack = (
	"npc_decision_checklist_evaluate_enemy_center_for_attack",
		[
		#NOTES -- LAST OFFENSIVE TIME SCORE IS NOT USED
		
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":potential_target", 2),
		(store_script_param, ":attack_by_faction", 3),
		(store_script_param, ":all_vassals_included", 4),
		
		(assign, ":result", -1),
		(assign, ":explainer_string", -1),
		#(assign, ":reason_is_obvious", 0),
		(assign, ":power_ratio", 0),
		#(assign, ":hours_since_last_recce", -1),
		
		#(assign, ":value_of_target", 0),
		#(assign, ":difficulty_of_capture", 0),
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		
		(try_begin),
			(eq, ":attack_by_faction", 1),
			(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
			(ge, ":faction_marshal", 0), #STEVE ADDITION TO AVOID MESSAGE SPAM
			(troop_get_slot, ":party_no", ":faction_marshal", slot_troop_leaded_party),
		(else_try),
			(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
		(try_end),
		
		(assign, "$g_use_current_ai_object_as_s8", 0),
		
		#THE FIRST BATCH OF DISQUALIFYING CONDITIONS DO NOT REQUIRE THE ATTACKING PARTY TO HAVE CURRENT INTELLIGENCE ON THE TARGET
		(try_begin),
			(neg|party_is_active, ":party_no"),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_party_not_active"),
			#(assign, ":reason_is_obvious", 1),
		(else_try),
			(store_faction_of_party, ":potential_target_faction", ":potential_target"),
			(store_relation, ":relation", ":potential_target_faction", ":faction_no"),
			(ge, ":relation", 0),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_is_friendly"),
			#(assign, ":reason_is_obvious", 1),
		(else_try),
			(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
			(assign, ":faction_of_besieger_party", -1),
			(try_begin),
			(neg|party_slot_eq, ":potential_target", slot_center_is_besieged_by, -1),
			(party_get_slot, ":besieger_party", ":potential_target", slot_center_is_besieged_by),
			(party_is_active, ":besieger_party"),
			(store_faction_of_party, ":faction_of_besieger_party", ":besieger_party"),
			(try_end),
			
			(neq, ":faction_of_besieger_party", -1),
			(neq, ":faction_of_besieger_party", ":faction_no"),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_is_already_besieged"),
			#(assign, ":reason_is_obvious", 1),
		(else_try),
			(is_between, ":potential_target", villages_begin, villages_end),
			(assign, ":village_is_looted_or_raided_already", 0),
			(try_begin),
			(party_slot_eq, ":potential_target", slot_village_state, svs_being_raided),
			(party_get_slot, ":raider_party", ":potential_target", slot_village_raided_by),
			(party_is_active, ":raider_party"),
			(store_faction_of_party, ":raider_faction", ":raider_party"),
			(neq, ":raider_faction", ":faction_no"),
			(assign, ":raiding_by_one_other_faction", 1),
			(else_try),
			(assign, ":raiding_by_one_other_faction", 0),
			(try_end),
			
			(try_begin),
			(this_or_next|party_slot_eq, ":potential_target", slot_village_state, svs_looted),
			(eq, ":raiding_by_one_other_faction", 1),
			(assign, ":village_is_looted_or_raided_already", 1),
			(try_end),
			
			(eq, ":village_is_looted_or_raided_already", 1),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_is_looted_or_raided_already"),
			#(assign, ":reason_is_obvious", 1),
		(else_try),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			
			(is_between, ":potential_target", villages_begin, villages_end),
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_marshal_does_not_want_to_attack_innocents"),
		(else_try),
			(assign, ":distance_from_our_closest_walled_center", 1000),
			(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":cur_center_faction", ":cur_center"),
			(eq, ":cur_center_faction", ":faction_no"),
			(store_distance_to_party_from_party, ":distance_from_cur_center", ":cur_center", ":potential_target"),
			(lt, ":distance_from_cur_center", ":distance_from_our_closest_walled_center"),
			(assign, ":distance_from_our_closest_walled_center", ":distance_from_cur_center"),
			(try_end),
			
			#(gt, ":distance_from_our_closest_walled_center", 75),
			(gt, ":distance_from_our_closest_walled_center", 325), # rafi 225
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_far_away_our_cautious_marshal_does_not_wish_to_reconnoiter"),
			#RECONNOITERING BEGINS HERE - VALUE WILL BE TEN OR LESS
		(else_try),
			# rafi (gt, ":distance_from_our_closest_walled_center", 90),
			(gt, ":distance_from_our_closest_walled_center", 370), # rafi 270
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_far_away_even_for_our_aggressive_marshal_to_reconnoiter"),
			#(assign, ":reason_is_obvious", 1),
		(else_try),
			(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			
			(assign, ":close_center_found", 0),
			(try_for_range, ":friendly_walled_center", walled_centers_begin, walled_centers_end),
			(eq, ":close_center_found", 0),
			(store_faction_of_party, ":friendly_walled_center_faction", ":friendly_walled_center"),
			(eq, ":friendly_walled_center_faction", ":faction_no"),
			(store_distance_to_party_from_party, ":distance_from_walled_center", ":potential_target", ":friendly_walled_center"),
			# rafi (lt, ":distance_from_walled_center", 60),
			(lt, ":distance_from_walled_center", 180),
			(assign, ":close_center_found", 1),
			(try_end),
			(eq, ":close_center_found", 0),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_is_indefensible"),
			#(else_try),
			#For now it is removed as Armagan's decision, we can add this option in later patchs. I and Armagan accept it has good potential. But this system needs also
			#scouting quests and scouting AI added together. If we only add this then we limit AI very much, it can attack only very few of centers, this damages
			#variability of game and surprise attacks of AI. Player can predict where AI will attack and he can full garnisons of only this center.
			#We can add asking travellers about how good defended center X by paying 100 denars for example to equalize situations of AI and human player.
			#But these needs much work and detailed AI tests so Armagan decided to skip this for now.
			
			#(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
			#(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
			#(party_get_slot, ":last_recce_time", ":potential_target", ":faction_recce_slot"),
			#(store_current_hours, ":hours_since_last_recce"),
			#(val_sub, ":hours_since_last_recce", ":last_recce_time"),
			
			#(this_or_next|eq, ":last_recce_time", 0),
			#(gt, ":hours_since_last_recce", 96), #Information is presumed to be accurate for four days
			
			#(store_sub, ":150_minus_distance_div_by_10", 150, ":distance_from_party"),
			#(val_div, ":150_minus_distance_div_by_10", 10),
			
			#(assign, ":result", ":150_minus_distance_div_by_10"),
			#(assign, ":explainer_string", "str_center_has_not_been_scouted"),
			#DECISIONS BASED ON ENEMY STRENGTH BEGIN HERE
		(else_try),
			(party_get_slot, ":party_strength", ":party_no", slot_party_cached_strength),
			(party_get_slot, ":follower_strength", ":party_no", slot_party_follower_strength),
			(party_get_slot, ":strength_of_nearby_friend", ":party_no", slot_party_nearby_friend_strength),
			
			(store_add, ":total_strength", ":party_strength", ":follower_strength"),
			(val_add, ":total_strength", ":strength_of_nearby_friend"),
			
			#(party_get_slot, ":potential_target_nearby_enemy_exact_strength", ":potential_target", slot_party_nearby_friend_strength),
			#(assign, ":potential_target_nearby_enemy_strength", ":potential_target_nearby_enemy_exact_strength"),
			(try_begin),
			(is_between, ":potential_target", villages_begin, villages_end),
			(assign, ":enemy_strength", 10),
			(else_try),
			(party_get_slot, ":enemy_strength", ":potential_target", slot_party_cached_strength),
			(party_get_slot, ":enemy_strength_nearby", ":potential_target", slot_party_nearby_friend_strength),
			(val_add, ":enemy_strength", ":enemy_strength_nearby"),
			(try_end),
			(val_max, ":enemy_strength", 1),
			
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			
			(store_mul, ":power_ratio", ":total_strength", 100),
			(val_div, ":power_ratio", ":enemy_strength"),
			(lt, ":power_ratio", 150),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_protected_by_enemy_army_aggressive"),
		(else_try),
			(ge, ":enemy_strength", ":total_strength"), #if enemy is powerful
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_protected_by_enemy_army_cautious"),
		(else_try),
			(store_mul, ":power_ratio", ":total_strength", 100),
			(val_div, ":power_ratio", ":enemy_strength"),
			(lt, ":power_ratio", 185),
			
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			
			#equations here
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_cautious_marshal_believes_center_too_difficult_to_capture"),
		(else_try),
			(lt, ":power_ratio", 140), #it was 140
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_even_aggressive_marshal_believes_center_too_difficult_to_capture"),
			#To Steve - I moved below two if statement here from upper places, to enable in answering different different answers even
			#if we are close to an unlooted enemy village. For example now it can say "center X" is too far too while our army is
			#looting a village because of its closeness.
		(else_try),
			#if the party has already started the siege
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
			(faction_get_slot, ":current_object", ":faction_no", slot_faction_ai_object),
			(is_between, ":current_object", villages_begin, villages_end),
			(neq, ":potential_target", ":current_object"),
			(party_slot_eq, ":current_object", slot_village_state, svs_under_siege),
			
			(store_current_hours, ":hours_since_siege_began"),
			(party_get_slot, ":hour_that_siege_began", ":current_object", slot_center_siege_begin_hours),
			(val_sub, ":hours_since_siege_began", ":hour_that_siege_began"),
			(gt, ":hours_since_siege_began", 4),
			
			(call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack", ":troop_no", ":current_object", ":attack_by_faction", 0),
			(gt, reg0, -1),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_we_have_already_committed_too_much_time_to_our_present_siege_to_move_elsewhere"),
		(else_try),
			#If the party is close to an unlooted village
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
			(faction_get_slot, ":current_object", ":faction_no", slot_faction_ai_object),
			(neq, ":potential_target", ":current_object"),
			(is_between, ":current_object", villages_begin, villages_end),
			(store_distance_to_party_from_party, ":distance_to_cur_object", ":party_no", ":current_object"),
			(lt, ":distance_to_cur_object", 10),
			
			(call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack", ":troop_no", ":current_object", ":attack_by_faction", 0),
			(gt, reg0, -1),
			
			(assign, "$g_use_current_ai_object_as_s8", 1),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_center_we_are_already_here_we_should_at_least_loot_the_village"),
			#DECISION TO ATTACK IS HERE
			#(else_try),
			#To Steve - I removed below lines, as here decided. We will use pre-function to evaluate assailability scores for centers rather than below lines to make AI
			#selecting better targets. If you want to make some marshals to select not-best options I can add that option into script_calculate_center_assailability_score,
			#for that we can need seed values for each center and for each lord, so we can add these seed values to create variability, clever marshals have seeds with less
			#standard deviation and less values and less-clever marshals have bigger seeds. Then probability of some lords to disagree marshal increases because their seed
			#values will be different from marshal's. If Steve wants it from me to implement I can add this.
			
			#(try_begin),
			#  (is_between, ":potential_target", villages_begin, villages_end),
			#  (party_get_slot, ":score", ":potential_target", slot_town_prosperity),
			#  (val_add, ":score", 50), #average 100
			#(else_try),
			#  (is_between, ":potential_target", castles_begin, castles_end),
			#  (assign, ":score", ":power_ratio"), #ie, at least 140
			#(else_try),
			#  (party_get_slot, ":score", ":potential_target", slot_town_prosperity),
			#  (val_add, ":score", 75),
			#  (val_mul, ":score", ":power_ratio"),
			#  (val_div, ":score", 100), #ie, at least about 200
			#(try_end),
			#
			#(val_sub, ":score", ":distance_from_party"),
			#(lt, ":score", -1),
			
			#(assign, ":result", -1),
			#(assign, ":explainer_string", "str_center_value_outweighed_by_difficulty_of_capture"),
		(else_try),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(eq, ":faction_no", "fac_kingdom_3"),
			(store_faction_of_party, ":potential_target_faction", ":potential_target"),
			(store_relation, ":relation", ":potential_target_faction", ":faction_no"),
			(lt, ":relation", 0),
			(try_end),
			
			(call_script, "script_calculate_center_assailability_score", ":troop_no", ":potential_target", ":all_vassals_included"),
			(assign, ":score", reg0),
			(assign, ":power_ratio", reg1),
			#(assign, ":distance_score", reg2),
			
			(assign, ":result", ":score"),
			
			(try_begin),
			(le, ":power_ratio", 100),
			(try_begin),
				(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
				(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
				(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
				(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
				(assign, ":explainer_string", "str_center_cautious_marshal_believes_center_too_difficult_to_capture"),
			(else_try),
				(assign, ":explainer_string", "str_center_even_aggressive_marshal_believes_center_too_difficult_to_capture"),
			(try_end),
			(else_try),
			(le, ":power_ratio", 150),
			
			(try_begin),
				(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
				(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
				(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
				(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
				(assign, ":explainer_string", "str_center_protected_by_enemy_army_cautious"),
			(else_try),
				(assign, ":explainer_string", "str_center_protected_by_enemy_army_aggressive"),
			(try_end),
			(else_try),
			(try_begin),
				(le, ":score", "$g_faction_object_score"),
				(assign, ":explainer_string", "str_center_value_outweighed_by_difficulty_of_capture"),
			(else_try),
				#To Steve, does not this sentence needs to explain why we are not attacking that city?
				#This sentence says it justifies, so why we are not attacking?
				(assign, ":explainer_string", "str_center_value_justifies_the_difficulty_of_capture"),
			(try_end),
			(try_end),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":explainer_string"),
		(assign, reg2, ":power_ratio"),
		
		# (try_begin),
		# (neq, reg1, "str_center_is_friendly"),
		# (str_store_faction_name, s30, ":faction_no"),
		# (str_store_string, s31, reg1),
		# (str_store_party_name, s32, ":potential_target"),
		# (str_store_troop_name, s33, ":troop_no"),
		# (display_message, "@{s33} of {s30} vs {s32} - {s31} {reg0} {reg2}"),
		# (try_end),
	])

#script_npc_decision_checklist_faction_ai_alt
	#WARNING: heavily modified by 1257AD devs
	#This is called from within decide_faction_ai, or from (modded2x: from wat?)
	#INPUT troop_no
	#OUTPUT: action, object
npc_decision_checklist_faction_ai_alt =	(
		"npc_decision_checklist_faction_ai_alt", #This is called from within decide_faction_ai, or from
		[
		(store_script_param, ":troop_no", 1),
		
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		
		(str_store_troop_name, s4, ":troop_no"),
		(str_store_faction_name, s33, ":faction_no"),
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s4} produces a faction strategy for {s33}"),
		(try_end),
		
		#INFORMATIONS COLLECTING STEP 0: Here we obtain general information about current faction like how much parties that faction has, which lord is the marshall, current ai state and current ai target object
		#(faction_get_slot, ":faction_strength", ":faction_no", slot_faction_number_of_parties),
		(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
		(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
		(faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
		
		(assign, ":marshal_party", -1),
		(assign, ":marshal_party_strength", 0),
		
		(try_begin),
			(gt, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
			(party_is_active, ":marshal_party"),
			(party_get_slot, ":marshal_party_itself_strength", ":marshal_party", slot_party_cached_strength),
			(party_get_slot, ":marshal_party_follower_strength", ":marshal_party", slot_party_follower_strength),
			(store_add, ":marshal_party_strength", ":marshal_party_itself_strength", ":marshal_party_follower_strength"),
		(try_end),
		
		#INFORMATIONS COLLECTING STEP 1: Here we are learning how much hours past from last offensive situation/feast concluded/current state started
		(store_current_hours, ":hours_since_last_offensive"),
		(faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
		(val_sub, ":hours_since_last_offensive", ":last_offensive_time"),
		
		(store_current_hours, ":hours_since_last_feast_start"),
		(faction_get_slot, ":last_feast_time", ":faction_no", slot_faction_last_feast_start_time),
		(val_sub, ":hours_since_last_feast_start", ":last_feast_time"),
		
		(store_current_hours, ":hours_at_current_state"),
		(faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
		(val_sub, ":hours_at_current_state", ":current_state_started"),
		
		(store_current_hours, ":hours_since_last_faction_rest"),
		(faction_get_slot, ":last_rest_time", ":faction_no", slot_faction_ai_last_rest_time),
		(val_sub, ":hours_since_last_faction_rest", ":last_rest_time"),
		
		(try_begin), #calculating ":last_offensive_time_score", this will be used in #11 and #12
			(ge, ":hours_since_last_offensive", 1080), #more than 45 days (100p)
			(assign, ":last_offensive_time_score", 100),
		(else_try),
			(ge, ":hours_since_last_offensive", 480), #more than 20 days (65p..99p)
			(store_sub, ":last_offensive_time_score", ":hours_since_last_offensive", 480),
			(val_div, ":last_offensive_time_score", 20),
			(val_add, ":last_offensive_time_score", 64),
		(else_try),
			(ge, ":hours_since_last_offensive", 240), #more than 10 days (41p..64p)
			(store_sub, ":last_offensive_time_score", ":hours_since_last_offensive", 240),
			(val_div, ":last_offensive_time_score", 10),
			(val_add, ":last_offensive_time_score", 40),
		(else_try), #less than 10 days (0p..40p)
			(store_div, ":last_offensive_time_score", ":hours_since_last_offensive", 6), #0..40
		(try_end),
		
		#INFORMATION COLLECTING STEP 3: Here we are finding the most threatened center
		(call_script, "script_find_center_to_defend", ":troop_no"),
		(assign, ":most_threatened_center", reg0),
		(assign, ":threat_danger_level", reg1),
		(assign, ":enemy_strength_near_most_threatened_center", reg2), #NOTE! This will be off by as much as 50%
		
		#INFORMATION COLLECTING STEP 4: Here we are finding number of vassals who are already following the marshal, and the assigned vassal ratio of current faction.
		(assign, ":vassals_already_assembled", 0),
		(assign, ":total_vassals", 0),
		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":faction_no"),
			(troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
			(party_is_active, ":led_party"),
			(val_add, ":total_vassals", 1),
			
			(party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
			(party_slot_eq, ":led_party", slot_party_ai_object, ":marshal_party"),
			
			(party_is_active, ":marshal_party"),
			(store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":marshal_party"),
			(lt, ":distance_to_marshal", 15),
			(val_add, ":vassals_already_assembled", 1),
		(try_end),
		(assign, ":ratio_of_vassals_assembled", -1),
		(try_begin),
			(gt, ":total_vassals", 0),
			(store_mul, ":ratio_of_vassals_assembled", ":vassals_already_assembled", 100),
			(val_div, ":ratio_of_vassals_assembled", ":total_vassals"),
		(try_end),
		
		#50% of vassals means that the campaign hour limit is ten days
		(store_mul, ":campaign_hour_limit", ":ratio_of_vassals_assembled", 3),
		#(val_add, ":campaign_hour_limit", 90),
		(val_add, ":campaign_hour_limit", 180), #tom
		
		#To Steve - I understand your concern about some marshals will gather army and some will not be able to find any valueable center to attack after gathering,
		#and these marshals will be questioned by other marshals ext. This is ok but if we search for a target without adding all other vassals what if
		#AI cannot find any target for long time because of its low power ratio if enemy cities are equal defended? Do not forget if we do not count other vassals in
		#faction while making target search we can only add marshal army's power and vassals around him. And if there is any threat in our centers even it is smaller,
		#its threat_danger_level will be more than target_value_level if marshal new started gathering for ofensive. Because we only assume marshal and around vassals
		#will join attack. And in our scenarios currently there are less vassals are around him. So power ratio will be low and any small threat will be enought to stop
		#an offensive. Then when players finds out this they periodically will take under siege to enemy's any center and they will be saved from any kind of newly started
		#offensive they will be faced. So we have to calculate both attack levels and select highest one to compare with threat level. Please do not change this part.
		
		(try_begin),
			(ge, ":faction_marshal", 0),
			(ge, ":marshal_party", 0),
			(party_is_active, ":marshal_party"),
			
			(call_script, "script_party_count_fit_for_battle", ":marshal_party"),
			(assign, ":number_of_fit_soldiers_in_marshal_party", reg0),
			(ge, ":number_of_fit_soldiers_in_marshal_party", 40),
			
			(call_script, "script_find_center_to_attack_alt", ":troop_no", 1, 0),
			(assign, ":center_to_attack_all_vassals_included", reg0),
			(assign, ":target_value_level_all_vassals_included", reg1),
			
			(call_script, "script_find_center_to_attack_alt", ":troop_no", 1, 1),
			(assign, ":center_to_attack_only_marshal_and_followers", reg0),
			(assign, ":target_value_level_only_marshal_and_followers", reg1),
		(else_try),
			(assign, ":target_value_level_all_vassals_included", 0),
			(assign, ":target_value_level_only_marshal_and_followers", 0),
			(assign, ":center_to_attack_all_vassals_included", -1),
			(assign, ":center_to_attack_only_marshal_and_followers", -1),
		(try_end),
		
		(try_begin),
			(ge, ":target_value_level_all_vassals_included", ":center_to_attack_only_marshal_and_followers"),
			(assign, ":center_to_attack", ":center_to_attack_all_vassals_included"),
			(assign, ":target_value_level", ":target_value_level_all_vassals_included"),
		(else_try),
			(assign, ":center_to_attack", ":center_to_attack_only_marshal_and_followers"),
			(assign, ":target_value_level", ":target_value_level_only_marshal_and_followers"),
		(try_end),
		
		(try_begin),
			(eq, ":current_ai_state", sfai_attacking_center),
			(val_mul, ":target_value_level", 3),
			(val_div, ":target_value_level", 2),
		(try_end),
		
		# (try_begin),
			# (eq, "$cheat_mode", 1),
			# (try_begin),
			# (is_between, ":center_to_attack", centers_begin, centers_end),
			# (str_store_party_name, s4, ":center_to_attack"),
			# (display_message, "@{!}Best offensive target {s4} has value level of {reg1}"),
			# (else_try),
			# (display_message, "@{!}No center found to attack"),
			# (try_end),
			
			# (try_begin),
			# (is_between, ":most_threatened_center", centers_begin, centers_end),
			# (str_store_party_name, s4, ":most_threatened_center"),
			# (assign, reg1, ":threat_danger_level"),
			# (display_message, "@{!}Best threat of {s4} has value level of {reg1}"),
			# (else_try),
			# (display_message, "@{!}No center found to defend"),
			# (try_end),
		# (try_end),
		
		# (try_begin),
			# (eq, "$cheat_mode", 1),
			
			# (try_begin),
			# (is_between, ":most_threatened_center", centers_begin, centers_end),
			# (str_store_party_name, s4, ":most_threatened_center"),
			# (assign, reg1, ":threat_danger_level"),
			# (display_message, "@Best threat of {s4} has value level of {reg1}"),
			# (else_try),
			# (display_message, "@No center found to defend"),
			# (try_end),
		# (try_end),
		
		(assign, "$g_target_after_gathering", -1),
		
		(store_current_hours, ":hours"),
		(try_begin),
			(ge, ":target_value_level", ":threat_danger_level"),
			(faction_set_slot, ":faction_no", slot_faction_last_safe_hours, ":hours"),
		(try_end),
		(faction_get_slot, ":last_safe_hours", ":faction_no", slot_faction_last_safe_hours),
		(try_begin),
			(eq, ":last_safe_hours", 0),
			(faction_set_slot, ":faction_no", slot_faction_last_safe_hours, ":hours"),
		(try_end),
		(faction_get_slot, ":last_safe_hours", ":faction_no", slot_faction_last_safe_hours),
		(store_sub, ":hours_since_days_defensive_started", ":hours", ":last_safe_hours"),
		(str_store_faction_name, s7, ":faction_no"),
		
		(assign, ":at_peace_with_everyone", 1),
		(try_for_range, ":faction_at_war", kingdoms_begin, kingdoms_end),
			(store_relation, ":relation", ":faction_no", ":faction_at_war"),
			(lt, ":relation", 0),
			(assign, ":at_peace_with_everyone", 0),
		(try_end),
		
		
		#INFORMATIONS ARE COLLECTED, NOW CHECK ALL POSSIBLE ACTIONS AND DECIDE WHAT TO DO	NEXT
		#Player marshal
		(try_begin), # a special case to end long-running feasts
			(eq, ":troop_no", "trp_player"),
			
			(eq, ":current_ai_state", sfai_feast),
			(ge, ":hours_at_current_state", 72),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			
			#Normally you are not supposed to set permanent values in this state, but this is a special case to end player-called feasts
			(assign, "$player_marshal_ai_state", sfai_default),
			(assign, "$player_marshal_ai_object", -1),
		(else_try), #another special state, to make player-called feasts last for a while when the player is the leader of the faction, but not the marshal
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
			(neq, ":troop_no", "trp_player"),
			
			(eq, ":current_ai_state", sfai_feast),
			(le, ":hours_at_current_state", 48),
			
			(party_slot_eq, ":current_ai_object", slot_town_lord, "trp_player"),
			(store_faction_of_party, ":current_ai_object_faction", ":current_ai_object"),
			(eq, ":current_ai_object_faction", "$players_kingdom"),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":current_ai_object"),
			
			
		(else_try), #this is the main player marshal state
			(eq, ":troop_no", "trp_player"),
			
			(str_clear, s14),
			(assign, ":action", "$player_marshal_ai_state"),
			(assign, ":object", "$player_marshal_ai_object"),
			
			#1-RESTING IF NEEDED
			#If not currently attacking a besieging a center and vassals did not rest for long time, let them rest.
			#If we do not take this part to toppest level, tired vassals already did not accept any order, so that
			#faction cannot do anything already. So first let vassals rest if they need. Thats why it should be toppest.
		(else_try),
			(neq, ":current_ai_state", sfai_default),
			(neq, ":current_ai_state", sfai_feast),
			(party_is_active, ":marshal_party"),
			
			(party_slot_eq, ":marshal_party", slot_party_ai_state, spai_retreating_to_center),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_the_enemy_temporarily_has_the_field"),
			
		(else_try),
			(neq, ":current_ai_state", sfai_feast),
			
			(assign, ":currently_besieging", 0),
			(try_begin),
			(eq, ":current_ai_state", sfai_attacking_center),
			(is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
			(party_get_slot, ":besieger_party", ":current_ai_object", slot_center_is_besieged_by),
			(party_is_active, ":besieger_party"),
			(store_faction_of_party, ":besieger_faction", ":besieger_party"),
			(eq, ":besieger_faction", ":faction_no"),
			(assign, ":currently_besieging", 1),
			(try_end),
			
			(assign, ":currently_defending_center", 0),
			(try_begin),
			(eq, ":current_ai_state", sfai_attacking_enemies_around_center),
			(gt, ":marshal_party", 0),
			(party_is_active, ":marshal_party"),
			
			(assign, ":besieged_center", -1),
			(try_begin),
				(party_slot_eq, ":marshal_party", slot_party_ai_state, spai_holding_center), #if commander is holding a center
				(party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (center they are holding)
				(party_get_battle_opponent, ":besieger_enemy", ":marshal_object"), #get this object's battle opponent
				(ge, ":besieger_enemy", 0),
				(assign, ":besieged_center", ":marshal_object"),
			(else_try),
				(party_slot_eq, ":marshal_party", slot_party_ai_state, spai_engaging_army), #if commander is engaging an army
				(party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (army which they engaded)
				(ge, ":marshal_object", 0), #if commander has an object
				(neg|is_between, ":marshal_object", centers_begin, centers_end), #if this object is not a center, so it is a party
				(party_is_active, ":marshal_object"),
				(party_get_battle_opponent, ":besieged_center", ":marshal_object"), #get this object's battle opponent
			(try_end),
			
			(eq, ":besieged_center", ":current_ai_object"),
			(assign, ":currently_defending_center", 1),
			(try_end),
			
			(eq, ":currently_besieging", 0),
			(eq, ":currently_defending_center", 0),
			(ge, ":hours_since_last_faction_rest", 1240),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_the_vassals_are_tired_we_let_them_rest_for_some_time"),
			
			#2-DEFENSIVE ACTIONS : GATHERING ARMY FOR DEFENDING
		(else_try),
			(party_is_active, ":marshal_party"),
			(eq, ":at_peace_with_everyone", 0),
			
			#(is_between, ":most_threatened_center", centers_begin, centers_end),
			(is_between, ":most_threatened_center", walled_centers_begin, walled_centers_end), #TOM
			(this_or_next|eq, ":current_ai_state", sfai_default),    #MOTO not going to attack anyway 
					(this_or_next|eq, ":current_ai_state", sfai_feast),    #MOTO not going to attack anyway (THIS is the emergency to stop feast)
			(gt, ":threat_danger_level", ":target_value_level"),
			
			(assign, ":continue_gathering", 0),
			(assign, ":start_gathering", 0),
			
			(try_begin),
			(is_between, ":most_threatened_center", villages_begin, villages_end),
			
			(assign, ":continue_gathering", 0),
			(else_try),
			(try_begin),
				(lt, ":hours_since_days_defensive_started", 3),
				(assign, ":multiplier", 150),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 6),
				(assign, ":multiplier", 140),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 9),
				(assign, ":multiplier", 132),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 12),
				(assign, ":multiplier", 124),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 15),
				(assign, ":multiplier", 118),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 18),
				(assign, ":multiplier", 114),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 21),
				(assign, ":multiplier", 110),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 24),
				(assign, ":multiplier", 106),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 27),
				(assign, ":multiplier", 102),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 31),
				(assign, ":multiplier", 98),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 34),
				(assign, ":multiplier", 94),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 37),
				(assign, ":multiplier", 90),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 40),
				(assign, ":multiplier", 86),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 43),
				(assign, ":multiplier", 82),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 46),
				(assign, ":multiplier", 79),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 49),
				(assign, ":multiplier", 76),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 52),
				(assign, ":multiplier", 73),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 56),
				(assign, ":multiplier", 70),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 60),
				(assign, ":multiplier", 68),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 66),
				(assign, ":multiplier", 66),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 72),
				(assign, ":multiplier", 64),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 80),
				(assign, ":multiplier", 62),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 90),
				(assign, ":multiplier", 60),
			(else_try),
				(lt, ":hours_since_days_defensive_started", 100),
				(assign, ":multiplier", 58),
			(else_try),
				(assign, ":multiplier", 56),
			(try_end),
			
			(store_mul, ":enemy_strength_multiplied", ":enemy_strength_near_most_threatened_center", ":multiplier"),
			(val_div, ":enemy_strength_multiplied", 100),
			
			(try_begin),
				(lt, ":marshal_party_strength", ":enemy_strength_multiplied"),
				(assign, ":continue_gathering", 1),
			(try_end),
			(else_try),
			(eq, ":current_ai_state", sfai_attacking_enemies_around_center),
			(neq, ":most_threatened_center", ":current_ai_object"),
			
			(assign, ":marshal_is_already_defending_a_center", 0),
			(try_begin),
				(gt, ":marshal_party", 0),
				(party_is_active, ":marshal_party"),
				
				(assign, ":besieged_center", -1),
				(try_begin),
				(party_slot_eq, ":marshal_party", slot_party_ai_state, spai_holding_center), #if commander is holding a center
				(party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (center they are holding)
				(party_get_battle_opponent, ":besieger_enemy", ":marshal_object"), #get this object's battle opponent
				(ge, ":besieger_enemy", 0),
				(assign, ":besieged_center", ":marshal_object"),
				(else_try),
				(party_slot_eq, ":marshal_party", slot_party_ai_state, spai_engaging_army), #if commander is engaging an army
				(party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (army which they engaded)
				(ge, ":marshal_object", 0), #if commander has an object
				(neg|is_between, ":marshal_object", centers_begin, centers_end), #if this object is not a center, so it is a party
				(party_is_active, ":marshal_object"),
				(party_get_battle_opponent, ":besieged_center", ":marshal_object"), #get this object's battle opponent
				(try_end),
				
				(eq, ":besieged_center", ":current_ai_object"),
				
				(assign, ":marshal_is_already_defending_a_center", 1),
			(try_end),
			
			(eq, ":marshal_is_already_defending_a_center", 0),
			
			(store_mul, ":enemy_strength_multiplied", ":enemy_strength_near_most_threatened_center", 80),
			(val_div, ":enemy_strength_multiplied", 100),
			(lt, ":marshal_party_strength", ":enemy_strength_multiplied"),
			
			(this_or_next|is_between, ":most_threatened_center", walled_centers_begin, walled_centers_end),
			(neq, ":faction_no", "$players_kingdom"),
			
			(assign, ":start_gathering", 1),
			(try_end),
			
			(this_or_next|eq, ":continue_gathering", 1),
			(eq, ":start_gathering", 1),
			
			(assign, ":action", sfai_gathering_army),
			(assign, ":object", -1),
			(str_store_party_name, s21, ":most_threatened_center"),
			(str_store_string, s14, "str_we_should_prepare_to_defend_s21_but_we_should_gather_our_forces_until_we_are_strong_enough_to_engage_them"),
			
			(try_begin),
			(eq, ":faction_no", "$players_kingdom"),
			(assign, "$g_gathering_reason", ":most_threatened_center"),
			(try_end),
			
			#3-DEFENSIVE ACTIONS : RIDE TO BREAK ENEMY SIEGE / DEFEAT ENEMIES NEAR OUR CENTER
		(else_try),
			(party_is_active, ":marshal_party"),
			(is_between, ":most_threatened_center", walled_centers_begin, walled_centers_end),
			(this_or_next|eq, ":current_ai_state", sfai_default),    #MOTO not going to attack anyway 
					(this_or_next|eq, ":current_ai_state", sfai_feast),    #MOTO not going to attack anyway (THIS is the emergency to stop feast)
			(ge, ":threat_danger_level", ":target_value_level"),
			(party_slot_ge, ":most_threatened_center", slot_center_is_besieged_by, 0),
			
			(assign, ":action", sfai_attacking_enemies_around_center),
			(assign, ":object", ":most_threatened_center"),
			
			(str_store_party_name, s21, ":most_threatened_center"),
			(str_store_string, s14, "str_we_should_ride_to_break_the_siege_of_s21"),
			
			#3b - DEFEAT ENEMIES NEAR CENTER - similar to above, but a different string
		(else_try),
			(eq, 0, 1), ##tom village is no longer faction defensive priority.
			(party_is_active, ":marshal_party"),
			(this_or_next|eq, ":current_ai_state", sfai_default),    #MOTO not going to attack anyway 
					(this_or_next|eq, ":current_ai_state", sfai_feast),    #MOTO not going to attack anyway (THIS is the emergency to stop feast)
			(ge, ":threat_danger_level", ":target_value_level"),
			(is_between, ":most_threatened_center", villages_begin, villages_end),
			
			(assign, ":action", sfai_attacking_enemies_around_center),
			(assign, ":object", ":most_threatened_center"),
			(str_store_party_name, s21, ":most_threatened_center"),
			(str_store_string, s14, "str_we_should_ride_to_defeat_the_enemy_gathered_near_s21"),
			
			#4-DEMOBILIZATION
			#Let vassals attend their own business
		(else_try),
			(this_or_next|eq, ":current_ai_state", sfai_gathering_army),
			(this_or_next|eq, ":current_ai_state", sfai_attacking_center),
			(eq, ":current_ai_state", sfai_raiding_village),
			
			(ge, ":hours_since_last_faction_rest", ":campaign_hour_limit"), #Effected by ratio of vassals
			(ge, ":hours_at_current_state", 24),
			
			#Ozan : I am adding some codes here because sometimes armies demobilize during last seconds of an important event like taking a castle, ext.
			(assign, ":there_is_an_important_situation", 0),
			(try_begin), #do not demobilize during taking a castle/town (fighting in the castle)
			(is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
			(party_get_battle_opponent, ":besieger_party", ":current_ai_object"),
			(party_is_active, ":besieger_party"),
			(store_faction_of_party, ":besieger_faction", ":besieger_party"),
			(this_or_next|eq, ":besieger_faction", ":faction_no"),
			(eq, ":besieger_faction", "fac_player_faction"),
			(assign, ":there_is_an_important_situation", 1),
			(else_try), #do not demobilize during besieging a siege (holding around castle)
			(is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
			(party_get_slot, ":besieger_party", ":current_ai_object", slot_center_is_besieged_by),
			(party_is_active, ":besieger_party"),
			(store_faction_of_party, ":besieger_faction", ":besieger_party"),
			(this_or_next|eq, ":besieger_faction", ":faction_no"),
			(eq, ":besieger_faction", "fac_player_faction"),
			(assign, ":there_is_an_important_situation", 1),
			(else_try), #do not demobilize during raiding a village (holding around village)
			(is_between, ":current_ai_object", centers_begin, centers_end),
			(neg|is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
			(party_slot_eq, ":current_ai_object", slot_village_state, svs_being_raided),
			(assign, ":there_is_an_important_situation", 1),
			(try_end),
			
			(eq, ":there_is_an_important_situation", 0),
			#end addition ozan
			
			(assign, reg7, ":hours_since_last_faction_rest"),
			(assign, reg8, ":campaign_hour_limit"),
			
			(str_store_string, s14, "str_this_offensive_needs_to_wind_down_soon_so_the_vassals_can_attend_to_their_own_business"),
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			
			#6-GATHERING BECAUSE OF NO REASON
			#Start to gather the army
		(else_try),
			(party_is_active, ":marshal_party"),
			(eq, ":at_peace_with_everyone", 0),
			
			
			(eq, ":current_ai_state", sfai_default),
			(ge, ":hours_since_last_offensive", 60),
			(lt, ":hours_since_last_faction_rest", 120),
			
			#There should not be a center as a precondition for attack
			#Otherwise, we are unlikely to have a situation in which the army gathers, but does nothing -- which is important to have for role-playing purposes
			
			(assign, ":action", sfai_gathering_army),
			(assign, ":object", -1),
			(str_store_string, s14, "str_it_is_time_to_go_on_the_offensive_and_we_must_first_assemble_the_army"),
			
			(try_begin),
			(eq, ":faction_no", "$players_kingdom"),
			(assign, "$g_gathering_reason", -1),
			(try_end),
			
			#7-OFFENSIVE ACTIONS : CONTINUE GATHERING
		(else_try),
			(party_is_active, ":marshal_party"),
			(eq, ":current_ai_state", sfai_gathering_army),
			(eq, ":at_peace_with_everyone", 0),
			
			(lt, ":hours_at_current_state", 54), #gather army for 54 hours
			
			(lt, ":ratio_of_vassals_assembled", 12),
			
			(str_store_string, s14, "str_we_must_continue_to_gather_the_army_before_we_ride_forth_on_an_offensive_operation"),
			(assign, ":action", sfai_gathering_army),
			(assign, ":object", -1),
			
			#7-OFFENSIVE ACTIONS PART 2 : CONTINUE GATHERING
		(else_try),
			(assign, ":minimum_possible_attackable_target_value_level", 50),
			(eq, ":at_peace_with_everyone", 0),
			
			(try_begin), #agressive marshal
			(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
			(this_or_next|eq, ":reputation", lrep_martial),
			(this_or_next|eq, ":reputation", lrep_quarrelsome),
			(eq, ":reputation", lrep_selfrighteous),
			(val_mul, ":minimum_possible_attackable_target_value_level", 9),
			(val_div, ":minimum_possible_attackable_target_value_level", 10),
			(try_end),
			
			(party_is_active, ":marshal_party"),
			(eq, ":current_ai_state", sfai_gathering_army),
			
			(try_begin),
			(lt, ":hours_at_current_state", 6),
			(assign, ":minimum_needed_target_value_level", 1500),
			(else_try),
			(lt, ":hours_at_current_state", 10),
			(assign, ":minimum_needed_target_value_level", 1000),
			(else_try),
			(lt, ":hours_at_current_state", 14),
			(assign, ":minimum_needed_target_value_level", 720),
			(else_try),
			(lt, ":hours_at_current_state", 18),
			(assign, ":minimum_needed_target_value_level", 480),
			(else_try),
			(lt, ":hours_at_current_state", 22),
			(assign, ":minimum_needed_target_value_level", 360),
			(else_try),
			(lt, ":hours_at_current_state", 26),
			(assign, ":minimum_needed_target_value_level", 240),
			(else_try),
			(lt, ":hours_at_current_state", 30),
			(assign, ":minimum_needed_target_value_level", 180),
			(else_try),
			(lt, ":hours_at_current_state", 34),
			(assign, ":minimum_needed_target_value_level", 120),
			(else_try),
			(lt, ":hours_at_current_state", 38),
			(assign, ":minimum_needed_target_value_level", 100),
			(else_try),
			(lt, ":hours_at_current_state", 42),
			(assign, ":minimum_needed_target_value_level", 80),
			(else_try),
			(lt, ":hours_at_current_state", 46),
			(assign, ":minimum_needed_target_value_level", 65),
			(else_try),
			(lt, ":hours_at_current_state", 50),
			(assign, ":minimum_needed_target_value_level", 55),
			(else_try),
			#(assign, ":minimum_needed_target_value_level", ":minimum_possible_attackable_target_value_level"), #tom
			(assign, ":minimum_needed_target_value_level", 0), #tom - burn the fuckers even if it's not worth it
			#(assign, ":minimum_possible_attackable_target_value_level", 0), #TOM same reason as above
			(try_end),
			
			(try_begin), #agressive marshal
			(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
			(this_or_next|eq, ":reputation", lrep_martial),
			(this_or_next|eq, ":reputation", lrep_quarrelsome),
			(eq, ":reputation", lrep_selfrighteous),
			(val_mul, ":minimum_needed_target_value_level", 9),
			(val_div, ":minimum_needed_target_value_level", 10),
			(try_end),
			
			(le, ":target_value_level", ":minimum_needed_target_value_level"),
			(le, ":hours_at_current_state", 54),
			
			(str_store_string, s14, "str_we_have_assembled_some_vassals"),
			(assign, ":action", sfai_gathering_army),
			(assign, ":object", -1),
			
			#8-ATTACK AN ENEMY CENTER case 1, reconnaissance against walled center
			#(else_try),
			#(party_is_active, ":marshal_party"),
			#(neq, ":current_ai_state", sfai_default),
			#(neq, ":current_ai_state", sfai_feast),
			#(is_between, ":center_to_attack", walled_centers_begin, walled_centers_end),
			
			#(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
			#(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
			#(store_current_hours, ":hours_since_last_recon"),
			#(party_get_slot, ":last_recon_time", ":center_to_attack", ":faction_recce_slot"),
			#(val_sub, ":hours_since_last_recon", ":last_recon_time"),
			#(this_or_next|eq, ":last_recon_time", 0),
			#(gt, ":hours_since_last_recon", 96),
			
			#(assign, ":action", sfai_attacking_center),
			#(assign, ":object", ":center_to_attack"),
			#(str_store_string, s14, "str_we_are_conducting_recce"),
			
			#8-ATTACK AN ENEMY CENTER case 2, reconnaissance against village
			#(else_try),
			#(party_is_active, ":marshal_party"),
			#(neq, ":current_ai_state", sfai_default),
			#(neq, ":current_ai_state", sfai_feast),
			#(is_between, ":center_to_attack", villages_begin, villages_end),
			
			#(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
			#(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
			#(store_current_hours, ":hours_since_last_recon"),
			#(party_get_slot, ":last_recon_time", ":center_to_attack", ":faction_recce_slot"),
			#(val_sub, ":hours_since_last_recon", ":last_recon_time"),
			#(this_or_next|eq, ":last_recon_time", 0),
			#(gt, ":hours_since_last_recon", 96),
			
			
			#(assign, ":action", sfai_raiding_village),
			#(assign, ":object", ":center_to_attack"),
			#(str_store_string, s14, "str_we_are_conducting_recce"),
		(else_try),
			(party_is_active, ":marshal_party"),
			(neq, ":current_ai_state", sfai_default),
			(neq, ":current_ai_state", sfai_feast),
			
			(assign, ":center_to_attack", ":center_to_attack_only_marshal_and_followers"),
			
			(is_between, ":center_to_attack", walled_centers_begin, walled_centers_end),
			
			#(ge, ":target_value_level", ":minimum_possible_attackable_target_value_level"), ##tom
			
			(assign, ":action", sfai_attacking_center),
			(assign, ":object", ":center_to_attack"),
			(str_store_string, s14, "str_we_believe_the_fortress_will_be_worth_the_effort_to_take_it"),
			####TOM AI
		(else_try),
			(party_is_active, ":marshal_party"),
			(neq, ":current_ai_state", sfai_default),
			(neq, ":current_ai_state", sfai_feast),
			
			(assign, ":center_to_attack", ":center_to_attack_only_marshal_and_followers"),
			
			(is_between, ":center_to_attack", villages_begin, villages_end),
			
			(ge, ":target_value_level", ":minimum_possible_attackable_target_value_level"),
			
			(assign, ":action", sfai_raiding_village),
			(assign, ":object", ":center_to_attack"),
			(str_store_string, s14, "str_we_shall_leave_a_fiery_trail_through_the_heart_of_the_enemys_lands_targeting_the_wealthy_settlements_if_we_can"),
			####TOM AI
			#9 -- DISBAND THE ARMY
		(else_try),
			(eq, ":current_ai_state", sfai_gathering_army),
			
			(str_store_string, s14, "str_the_army_will_be_disbanded_because_we_have_been_waiting_too_long_without_a_target"),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			#OFFENSIVE OPERATIONS END
			
			#FEAST-RELATED OPERATIONS BEGIN
			#10-CONCLUDE CURRENT FEAST
		(else_try),
			(eq, ":current_ai_state", sfai_feast),
			(gt, ":hours_at_current_state", 72),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_it_is_time_for_the_feast_to_conclude"),
			
			#11-CONTINE FEAST UNLESS THERE IS AN EMERGENCY
		(else_try),
			(eq, ":current_ai_state", sfai_feast),
			(le, ":hours_at_current_state", 72),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":current_ai_object"),
			(str_store_string, s14, "str_we_should_continue_the_feast_unless_there_is_an_emergency"),
			
			#12-HOLD A FEAST BECAUSE THE PLAYER WANTS TO ORGANIZE ONE
		(else_try),
			(check_quest_active, "qst_organize_feast"),
			(eq, "$players_kingdom", ":faction_no"),
			
			(quest_get_slot, ":target_center", "qst_organize_feast", slot_quest_target_center),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":target_center"),
			(str_store_string, s14, "str_you_had_wished_to_hold_a_feast"),
			
			#13-HOLD A FEAST BECAUSE FEMALE PLAYER SCHEDULED TO GET MARRIED
		(else_try),
			(check_quest_active, "qst_wed_betrothed_female"),
			
			(quest_get_slot, ":groom", "qst_wed_betrothed_female", slot_quest_giver_troop),
			(troop_slot_eq, ":groom", slot_troop_prisoner_of_party, -1),
			
			(store_faction_of_troop, ":groom_faction", ":groom"),
			(eq, ":groom_faction", ":faction_no"),
			
			(faction_get_slot, ":faction_leader", ":groom_faction", slot_faction_leader),
			
			(assign, ":location_feast", -1),
			(try_for_range, ":possible_location", walled_centers_begin, walled_centers_end),
			(eq, ":location_feast", -1),
			(party_slot_eq, ":possible_location", slot_town_lord, ":groom"),
			(party_slot_ge, ":possible_location", slot_center_is_besieged_by, 0),
			(assign, ":location_feast", ":possible_location"),
			(try_end),
			
			(try_for_range, ":possible_location", walled_centers_begin, walled_centers_end),
			(eq, ":location_feast", -1),
			(party_slot_eq, ":possible_location", slot_town_lord, ":faction_leader"),
			(party_slot_ge, ":possible_location", slot_center_is_besieged_by, 0),
			(assign, ":location_feast", ":possible_location"),
			(try_end),
			
			(is_between, ":location_feast", walled_centers_begin, walled_centers_end),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":location_feast"),
			(str_store_string, s14, "str_your_wedding_day_approaches_my_lady"),
			
			#14-HOLD A FEAST BECAUSE A MALE CHARACTER WANTS TO GET MARRIED
		(else_try),
			(check_quest_active, "qst_wed_betrothed"),
			(neg|quest_slot_ge, "qst_wed_betrothed", slot_quest_expiration_days, 362),
			
			(quest_get_slot, ":bride", "qst_wed_betrothed", slot_quest_target_troop),
			(call_script, "script_get_kingdom_lady_social_determinants", ":bride"),
			(assign, ":feast_host", reg0),
			(store_faction_of_troop, ":feast_host_faction", ":feast_host"),
			(eq, ":feast_host_faction", ":faction_no"),
			
			(troop_slot_eq, ":feast_host", slot_troop_prisoner_of_party, -1),
			(assign, ":wedding_venue", reg1),
			
			(is_between, ":wedding_venue", centers_begin, centers_end),
			(party_slot_eq, ":wedding_venue", slot_center_is_besieged_by, -1),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":wedding_venue"),
			(str_store_string, s14, "str_your_wedding_day_approaches"),
			
			#15-HOLD A FEAST BECAUSE AN NPC WANTS TO GET MARRIED
		(else_try),
			(ge, ":hours_since_last_feast_start", 192), #If at least eight days past last feast start time
			
			(assign, ":location_feast", -1),
			
			(try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
			(troop_get_slot, ":groom", ":kingdom_lady", slot_troop_betrothed),
			(gt, ":groom", 0), #not the player
			
			(store_faction_of_troop, ":lady_faction", ":kingdom_lady"),
			(store_faction_of_troop, ":groom_faction", ":groom"),
			
			(try_begin), #The groom checks if he wants to continue or break off relations. This causes actions, rather than just returns a value, so it probably should be moved elsewhere
				(troop_slot_ge, ":groom", slot_troop_prisoner_of_party, 0),
			(else_try),
				(neq, ":groom_faction", ":lady_faction"),
				(neq, ":groom_faction", "fac_player_faction"),
				(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":kingdom_lady", ":groom"),
			(else_try),
				(eq, ":lady_faction", ":faction_no"),
				(store_current_hours, ":hours_since_betrothal"),
				(troop_get_slot, ":betrothal_time", ":kingdom_lady", slot_troop_betrothal_time),
				(val_sub, ":hours_since_betrothal", ":betrothal_time"),
				(ge, ":hours_since_betrothal", 719), #30 days
				
				(call_script, "script_get_kingdom_lady_social_determinants", ":kingdom_lady"),
				(assign, ":wedding_venue", reg1),
				
				(assign, ":location_feast", ":wedding_venue"),
				(assign, ":final_bride", ":kingdom_lady"),
				(assign, ":final_groom", ":groom"),
			(try_end),
			(try_end),
			
			(ge, ":location_feast", centers_begin),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":location_feast"),
			
			(str_store_troop_name, s22, ":final_bride"),
			(str_store_troop_name, s23, ":final_groom"),
			(str_store_string, s14, "str_s22_and_s23_wish_to_marry"),
			
			#16-HOLD A FEAST ANYWAY
		(else_try),
			(eq, ":current_ai_state", sfai_default),
			(gt, ":hours_since_last_feast_start", 240), #If at least 10 days past after last feast. (added by ozan)
			
			(assign, ":location_high_score", 0),
			(assign, ":location_feast", -1),
			
			(try_for_range, ":location", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":location_faction", ":location"),
			(eq, ":location_faction", ":faction_no"),
			
			(try_begin),
				(neg|party_slot_eq, ":location", slot_village_state, svs_under_siege),
				(party_get_slot, ":location_lord", ":location", slot_town_lord),
				(is_between, ":location_lord", active_npcs_begin, active_npcs_end),
				(troop_get_slot, ":location_score", ":location_lord", slot_troop_renown),
				(store_random_in_range, ":random", 0, 1000), #will probably be king or senior lord
				(val_add, ":location_score", ":random"),
				(gt, ":location_score", ":location_high_score"),
				(assign, ":location_high_score", ":location_score"),
				(assign, ":location_feast", ":location"),
			(else_try), #do not start new feasts if any place is under siege or being raided
				(this_or_next|party_slot_eq, ":location", slot_village_state, svs_under_siege),
				(party_slot_eq, ":location", slot_village_state, svs_being_raided),
				(assign, ":location_high_score", 9999),
				(assign, ":location_feast", -1),
			(try_end),
			(try_end),
			
			(is_between, ":location_feast", walled_centers_begin, walled_centers_end),
			(party_get_slot, ":feast_host", ":location_feast", slot_town_lord),
			(troop_slot_eq, ":feast_host", slot_troop_prisoner_of_party, -1),
			
			(assign, ":action", sfai_feast),
			(assign, ":object", ":location_feast"),
			(str_store_string, s14, "str_it_has_been_a_long_time_since_the_lords_of_the_realm_gathered_for_a_feast"),
			
			#17-DO NOTHING
		(else_try),
			(neq, ":current_ai_state", sfai_default),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_the_circumstances_which_led_to_this_decision_no_longer_apply_so_we_should_stop_and_reconsider_shortly"),
			
			#18-DO NOTHING
		(else_try),
			(eq, ":current_ai_state", sfai_default),
			
			(eq, ":at_peace_with_everyone", 1),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_we_are_currently_at_peace"),
		(else_try),
			(eq, ":current_ai_state", sfai_default),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, -1),
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_we_are_waiting_for_selection_of_marshal"),
			
		(else_try),
			(eq, ":current_ai_state", sfai_default),
			
			(assign, ":action", sfai_default),
			(assign, ":object", -1),
			(str_store_string, s14, "str_the_vassals_still_need_time_to_attend_to_their_own_business"),
		(try_end),
		
		(assign, reg0, ":action"),
		(assign, reg1, ":object"),
	])
	
	#script_npc_decision_checklist_take_stand_on_issue
	#Called from dialogs, and from simple_triggers
	#INPUT: troop_no
	#OUTPUT: result, result_explainer
npc_decision_checklist_take_stand_on_issue = (
	"npc_decision_checklist_take_stand_on_issue",
		#Called from dialogs, and from simple_triggers
		
		#This a very inefficient checklist, and if I did it again, I would score for each troop. That way the troop could answer "why not" to an individual lord
		[
		(store_script_param, ":troop_no", 1),
		(store_faction_of_troop, ":troop_faction", ":troop_no"),
		
		(assign, ":result", -1),
		(faction_get_slot, ":faction_issue", ":troop_faction", slot_faction_political_issue),
		
		(assign, ":player_declines_honor", 0),
		(try_begin),
			(is_between, ":faction_issue", centers_begin, centers_end),
			(gt, "$g_dont_give_fief_to_player_days", 1),
			(assign, ":player_declines_honor", 1),
		(else_try),
			(gt, "$g_dont_give_marshalship_to_player_days", 1),
			(assign, ":player_declines_honor", 1),
		(try_end),
		
		
		(assign, ":total_faction_renown", 0),
		(troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
		(try_begin),
			(eq, "$players_kingdom", ":troop_faction"),
			(eq, "$player_has_homage", 1),
			(troop_get_slot, ":total_faction_renown", "trp_player", slot_troop_renown),
		(try_end),
		
		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0), #reset to zero
			
			(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			(eq, ":active_npc_faction", ":troop_faction"),
			(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
			
			(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
			(val_add, ":total_faction_renown", ":renown"),
		(try_end),
		
		
		(assign, ":total_faction_center_value", 0),
		(try_for_range, ":center", centers_begin, centers_end),
			(store_faction_of_party, ":center_faction", ":center"),
			(eq, ":center_faction", ":troop_faction"),
			
			(assign, ":center_value", 1),
			(try_begin),
			(is_between, ":center", towns_begin, towns_end),
			(assign, ":center_value", 2),
			(try_end),
			
			(val_add, ":total_faction_center_value", ":center_value"),
			
			(party_get_slot, ":town_lord", ":center", slot_town_lord),
			(gt, ":town_lord", -1),
			
			(troop_get_slot, ":temp_slot", ":town_lord", slot_troop_temp_slot),
			(val_add, ":temp_slot", ":center_value"),
			(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":temp_slot"),
		(try_end),
		(val_max, ":total_faction_center_value", 1),
		
		(store_div, ":average_renown_per_center_point", ":total_faction_renown", ":total_faction_center_value"),
		
		
		(try_begin),
			(is_between, ":faction_issue", centers_begin, centers_end),
			#NOTE -- The algorithms here might seem a bit repetitive, but are designed that way to create internal cliques among the lords in a faction.
			
			
			
			(try_begin),#If the center is a village, and a lord has no fief, choose him
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
			
			(is_between, ":faction_issue", villages_begin, villages_end),
			(assign, ":favorite_lord_without_center", -1),
			(assign, ":score_to_beat", -1),
			
			
			(try_begin),
				(eq, "$players_kingdom", ":troop_faction"),
				(eq, "$player_has_homage", 1),
				(eq, ":player_declines_honor", 0),
				
				(troop_slot_eq, "trp_player", slot_troop_temp_slot, 0),
				(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
				(assign, ":relation", reg0),
				
				(gt, ":relation", ":score_to_beat"),
				(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 75),
				(assign, ":favorite_lord_without_center", "trp_player"),
				(assign, ":score_to_beat", ":relation"),
			(try_end),
			(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":troop_faction"),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
				
				(troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
				(try_begin),
				(eq, ":active_npc", ":troop_no"),
				(assign, ":relation", 50),
				(else_try),
				(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
				(assign, ":relation", reg0),
				(try_end),
				(neg|troop_slot_ge, ":active_npc", slot_troop_controversy, 75),
				
				(gt, ":relation", ":score_to_beat"),
				(assign, ":favorite_lord_without_center", ":active_npc"),
				(assign, ":score_to_beat", ":relation"),
			(try_end),
			
			(gt, ":favorite_lord_without_center", -1),
			(assign, ":result", ":favorite_lord_without_center"),
			(assign, ":result_explainer", "str_political_explanation_lord_lacks_center"),
			
			(else_try),	#taken by troop
			(is_between, ":faction_issue", walled_centers_begin, walled_centers_end),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			
			(party_get_slot, ":last_taken_by_troop", ":faction_issue", slot_center_last_taken_by_troop),
			(try_begin),
				(try_begin),
				(neq, ":troop_faction", "$players_kingdom"),
				(assign, ":last_taken_by_troop", -1),
				(else_try),
				(eq, "$player_has_homage", 0),
				(assign, ":last_taken_by_troop", -1),
				(else_try),
				(eq, ":faction_issue", "$g_castle_requested_by_player"),
				(assign, ":last_taken_by_troop", "trp_player"),
				(else_try),
				(eq, ":faction_issue", "$g_castle_requested_for_troop"),
				(assign, ":last_taken_by_troop", "trp_player"),
				(else_try), #ie, the fellow who took it is no longer in the faction
				(gt, ":last_taken_by_troop", -1),
				(store_faction_of_troop, ":last_take_by_troop_faction", ":last_taken_by_troop"),
				(neq, ":last_take_by_troop_faction", ":troop_faction"),
				(assign, ":last_taken_by_troop", -1),
				(try_end),
			(try_end),
			(gt, ":last_taken_by_troop", -1),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(gt, ":last_taken_by_troop", -1),
				(str_store_troop_name, s3, ":last_taken_by_troop"),
				(display_message, "@{!}Castle taken by {s3}"),
			(try_end),
			
			
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":last_taken_by_troop"),
			(ge, reg0, 0),
			
			(neg|troop_slot_ge, ":last_taken_by_troop", slot_troop_controversy, 25),
			
			(troop_get_slot, ":renown", ":last_taken_by_troop", slot_troop_renown),
			(troop_get_slot, ":center_points", ":last_taken_by_troop", slot_troop_temp_slot),
			(val_max, ":center_points", 1),
			(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
			(val_mul, ":renown_divided_by_center_points", 6), #was five
			(val_div, ":renown_divided_by_center_points", 4),
			
			(ge, ":renown_divided_by_center_points", ":average_renown_per_center_point"),
			
			
			(assign, ":result", ":last_taken_by_troop"),
			(assign, ":result_explainer", "str_political_explanation_lord_took_center"),
			
			
			#Check self, immediate family
			#This is done instead of a single weighted score to create cliques -- groups of NPCs who support one another
			(else_try),
			(assign, ":most_deserving_close_friend", -1),
			(assign, ":score_to_beat", ":average_renown_per_center_point"),
			(val_div, ":score_to_beat", 3),
			(val_mul, ":score_to_beat", 2),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(assign, reg3, ":score_to_beat"),
				(display_message, "@{!}Two-thirds average_renown = {reg3}"),
			(try_end),
			
			(try_begin),
				(eq, "$players_kingdom", ":troop_faction"),
				(eq, "$player_has_homage", 1),
				(eq, ":player_declines_honor", 0),
				
				(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
				(assign, ":relation", reg0),
				(ge, ":relation", 20),
				(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 50),
				
				(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
				(troop_get_slot, ":center_points", "trp_player", slot_troop_temp_slot),
				(val_max, ":center_points", 1),
				(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
				
				
				(assign, ":most_deserving_close_friend", "trp_player"),
				(assign, ":score_to_beat", ":renown_divided_by_center_points"),
			(try_end),
			(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":troop_faction"),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
				
				(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
				(assign, ":relation", reg0),
				
				(this_or_next|eq, ":active_npc", ":troop_no"),
				(ge, ":relation", 20),
				(neg|troop_slot_ge, ":active_npc", slot_troop_controversy, 50),
				
				(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
				(troop_get_slot, ":center_points", ":active_npc", slot_troop_temp_slot),
				(val_max, ":center_points", 1),
				(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
				
				
				(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s10, ":active_npc"),
				(assign, reg3, ":renown_divided_by_center_points"),
				(display_message, "@{!}DEBUG -- Colleague test: score for {s10} = {reg3}"),
				(try_end),
				
				
				(gt, ":renown_divided_by_center_points", ":score_to_beat"),
				
				(assign, ":most_deserving_close_friend", ":active_npc"),
				(assign, ":score_to_beat", ":renown_divided_by_center_points"),
			(try_end),
			
			(gt, ":most_deserving_close_friend", -1),
			
			
			(assign, ":result", ":most_deserving_close_friend"),
			(assign, ":result_explainer", "str_political_explanation_most_deserving_friend"),
			
			
			
			(else_try),
			#Most deserving in entire faction, minus those with no relation
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
			
			(assign, ":most_deserving_in_faction", -1),
			(assign, ":score_to_beat", 0),
			
			(try_begin),
				(eq, "$players_kingdom", ":troop_faction"),
				(eq, "$player_has_homage", 1),
				(eq, ":player_declines_honor", 0),
				
				(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
				(assign, ":relation", reg0),
				(ge, ":relation", 0),
				(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
				(troop_get_slot, ":center_points", "trp_player", slot_troop_temp_slot),
				(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 25),
				
				(val_max, ":center_points", 1),
				(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
				
				(assign, ":most_deserving_in_faction", "trp_player"),
				(assign, ":score_to_beat", ":renown_divided_by_center_points"),
			(try_end),
			(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":troop_faction"),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
				
				(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
				(assign, ":relation", reg0),
				(this_or_next|eq, ":active_npc", ":troop_no"),
				(ge, ":relation", 0),
				(neg|troop_slot_ge, ":active_npc", slot_troop_controversy, 25),
				
				(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
				(troop_get_slot, ":center_points", ":active_npc", slot_troop_temp_slot),
				(val_max, ":center_points", 1),
				
				(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
				(gt, ":renown_divided_by_center_points", ":score_to_beat"),
				
				(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_string, s10, ":active_npc"),
				(assign, reg3, ":renown_divided_by_center_points"),
				(display_message, "@{!}DEBUG -- Open test: score for {s10} = {reg3}"),
				(try_end),
				
				
				(assign, ":most_deserving_in_faction", ":active_npc"),
				(assign, ":score_to_beat", ":renown_divided_by_center_points"),
			(try_end),
			
			
			(gt, ":most_deserving_in_faction", -1),
			(assign, ":result", ":most_deserving_in_faction"),
			(assign, ":result_explainer", "str_political_explanation_most_deserving_in_faction"),
			
			(else_try),
			(assign, ":result", ":troop_no"),
			(assign, ":result_explainer", "str_political_explanation_self"),
			(try_end),
			
			
		(else_try),
			(eq, ":faction_issue", 1),
			
			(assign, ":relationship_threshhold", 15),
			(try_begin),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(assign, ":relationship_threshhold", 5),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(assign, ":relationship_threshhold", 25),
			(try_end),
			
			#For marshals, score marshals according to renown divided by controversy - first for friends and family, then for everyone
			(assign, ":marshal_candidate", -1),
			(assign, ":score_to_beat", 0),
			(try_begin),
			(eq, "$players_kingdom", ":troop_faction"),
			(eq, "$player_has_homage", 1),
			(eq, "$g_player_is_captive", 0),
			(eq, ":player_declines_honor", 0),
			
			
			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
			(ge, reg0, ":relationship_threshhold"),
			(assign, ":marshal_candidate", "trp_player"),
			(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
			(troop_get_slot, ":controversy_divisor", "trp_player", slot_troop_controversy),
			(val_add, ":controversy_divisor", 50),
			(store_div, ":score_to_beat", ":renown", ":controversy_divisor"),
			(try_end),
			
			(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			(eq, ":active_npc_faction", ":troop_faction"),
			(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
			(troop_slot_eq, ":active_npc", slot_troop_prisoner_of_party, -1),
			
			(neg|faction_slot_eq, ":troop_faction", slot_faction_leader, ":active_npc"),
			
			(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
			(assign, ":relation", reg0),
			(this_or_next|eq, ":active_npc", ":troop_no"),
			(ge, ":relation", ":relationship_threshhold"),
			
			(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
			(troop_get_slot, ":controversy_divisor", ":active_npc", slot_troop_controversy),
			(val_add, ":controversy_divisor", 50),
			(store_div, ":score", ":renown", ":controversy_divisor"),
			
			(gt, ":score", ":score_to_beat"),
			
			(assign, ":marshal_candidate", ":active_npc"),
			(assign, ":score_to_beat", ":score"),
			
			(try_end),
			
			(assign, ":result", ":marshal_candidate"),
			(assign, ":result_explainer", "str_political_explanation_marshal"),
		(try_end),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(gt, ":result", -1),
			(str_store_troop_name, s8, ":troop_no"),
			(str_store_troop_name, s9, ":result"),
			(str_store_string, s10, ":result_explainer"),
			(display_message, "@{!}DEBUG -- {s8} backs {s9}:{s10}"),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":result_explainer"),
		
	])
	

		#script_npc_decision_checklist_party_ai
	# WARNING: this script is heavily modified by 1257AD devs 
	# DECISION CHECKLISTS (OCT 14)
	# I was thinking of trying to convert as much AI decision-making as possible to the checklist format
	# While outcomes are not as nuanced and varied as a random decision using weighted chances for each outcoms,
	# the checklist has the advantage of being much more transparent, both to developers and to players
	# The checklist can yield a string (standardized to s14) which explains the rationale for the decision
	# When the script yields a yes/no/maybe result, than that is standardized from -3 to +3
	# INPUT: troop_no
	# OUTPUT: action, object
npc_decision_checklist_party_ai = (
	"npc_decision_checklist_party_ai",
		[
		#this script can replace decide_kingdom_hero_ai and decide_kingdom_hero_ai_follow_or_not
		#However, it does not contain script_party_set_ai_state
		
		(store_script_param, ":troop_no", 1),
		
		(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
		#(party_get_slot, ":our_strength", ":party_no", slot_party_cached_strength),
		#(store_div, ":min_strength_behind", ":our_strength", 2),
		#(party_get_slot, ":our_follower_strength", ":party_no", slot_party_follower_strength),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, "$g_talk_troop", ":troop_no"),
		(try_end),
		
		(store_troop_faction, ":faction_no", ":troop_no"),
		
		(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s15, "str__i_must_attend_to_this_matter_before_i_worry_about_the_affairs_of_the_realm"),
		(try_end),
		
		#find current center
		(party_get_attached_to, ":cur_center_no", ":party_no"),
		(try_begin),
			(lt, ":cur_center_no", 0),
			(party_get_cur_town, ":cur_center_no", ":party_no"),
		(try_end),
		(assign, ":besieger_party", -1),
		(try_begin),
			(neg|is_between, ":cur_center_no", centers_begin, centers_end),
			(assign, ":cur_center_no", -1),
		(else_try),
			(party_get_slot, ":besieger_party", ":cur_center_no", slot_center_is_besieged_by),
			(try_begin),
			(neg|party_is_active, ":besieger_party"),
			(assign, ":besieger_party", -1),
			(try_end),
		(try_end),
		
		#party_count
		(call_script, "script_party_count_fit_for_battle", ":party_no"),
		(assign, ":party_fit_for_battle", reg0),
		(call_script, "script_party_get_ideal_size", ":party_no"),
		(assign, ":ideal_size", reg0),
		(store_mul, ":party_strength_as_percentage_of_ideal", ":party_fit_for_battle", 100),
		(val_div, ":party_strength_as_percentage_of_ideal", ":ideal_size"),
		(try_begin),
			(faction_slot_eq, ":faction_no", slot_faction_num_towns, 0),
			(faction_slot_eq, ":faction_no", slot_faction_num_castles, 0),
			(assign, ":party_ratio_of_prisoners", 0), #do not let prisoners have an effect on ai calculation
		(else_try),
			(party_get_num_prisoners, ":num_prisoners", ":party_no"),
			(val_max, ":party_fit_for_battle", 1), #avoid division by zero error
			(store_div, ":party_ratio_of_prisoners", ":num_prisoners", ":party_fit_for_battle"),
		(try_end),
		
		(assign, ":faction_is_at_war", 0),
		(try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
			(faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
			(store_relation, ":relation", ":faction_no", ":kingdom"),
			(lt, ":relation", 0),
			(assign, ":faction_is_at_war", 1),
		(try_end),
		
		(assign, ":operation_in_progress", 0),
		(try_begin),
			(this_or_next|party_slot_eq, ":party_no", slot_party_ai_state, spai_raiding_around_center),
			(party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
			
			(party_get_slot, ":target_center", ":party_no", slot_party_ai_object),
			(is_between, ":target_center", centers_begin, centers_end),
			
			(store_faction_of_party, ":target_center_faction", ":target_center"),
			(store_relation, ":relation", ":faction_no", ":target_center_faction"),
			(lt, ":relation", 0),
			
			(store_distance_to_party_from_party, ":distance", ":party_no", ":target_center"),
			(lt, ":distance", 10),
			(this_or_next|party_slot_eq, ":target_center", slot_village_state, svs_under_siege),
			(this_or_next|party_slot_eq, ":target_center", slot_village_state, svs_normal),
			(party_slot_eq, ":target_center", slot_village_state, svs_being_raided),
			
			(assign, ":operation_in_progress", 1),
		(try_end),
		
		(troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
		
		(party_get_slot, ":old_ai_state", ":party_no", slot_party_ai_state),
		(party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
		
		(party_get_slot, ":party_cached_strength", ":party_no", slot_party_cached_strength),
		
		(store_current_hours, ":hours_since_last_rest"),
		(party_get_slot, ":last_rest_time", ":party_no", slot_party_last_in_any_center),
		(val_sub, ":hours_since_last_rest", ":last_rest_time"),
		
		(store_current_hours, ":hours_since_last_home"),
		(party_get_slot, ":last_home_time", ":party_no", slot_party_last_in_home_center),
		(val_sub, ":hours_since_last_home", ":last_home_time"),
		
		(store_current_hours, ":hours_since_last_combat"),
		(party_get_slot, ":last_combat_time", ":party_no", slot_party_last_in_combat),
		(val_sub, ":hours_since_last_combat", ":last_combat_time"),
		
		(store_current_hours, ":hours_since_last_courtship"),
		(party_get_slot, ":last_courtship_time", ":party_no", slot_party_leader_last_courted),
		(val_sub, ":hours_since_last_courtship", ":last_courtship_time"),
		
		(troop_get_slot, ":temp_ai_seed", ":troop_no", slot_troop_temp_decision_seed),
		(store_mod, ":aggressiveness", ":temp_ai_seed", 73), #To derive the
		(try_begin),
			(eq, ":troop_reputation", lrep_martial),
			(val_add, ":aggressiveness", 27),
		(else_try),
			(neq, ":troop_reputation", lrep_debauched),
			(neq, ":troop_reputation", lrep_quarrelsome),
			(val_add, ":aggressiveness", 14),
		(try_end),
		
		(try_begin),
			(gt, ":aggressiveness", ":hours_since_last_combat"),
			(val_add, ":aggressiveness", ":hours_since_last_combat"),
			(val_div, ":aggressiveness", 2),
		(try_end),
		
		(try_begin),
			(eq, "$cheat_mode", 1), #100
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_troop_name, s4, ":troop_no"),
			(assign, reg3, ":hours_since_last_rest"),
			(assign, reg4, ":hours_since_last_courtship"),
			(assign, reg5, ":hours_since_last_combat"),
			(assign, reg6, ":hours_since_last_home"),
			(assign, reg7, ":aggressiveness"),
			#(display_message, "@{!}{s4}: hours since rest {reg3}, courtship {reg4}, combat {reg5}, home {reg6}, aggressiveness {reg7}"),
		(try_end),
		
		##I am inspecting an estate (use slot_center_npc_volunteer_troop_amount)
		
		(str_store_string, s17, "str_the_other_matter_took_precedence"),
		
		(assign, ":do_only_collecting_rents", 0),
		
		#Wait in current city (dangerous to travel with less (<=10) men)
		(try_begin),
			#NOTE : I added also this condition to very top of list. Because if this condition does not exists in top then a bug happens.
			#Bug is about alone wounded lords without any troop near him travels between cities, sometimes it want to return his home city
			#to collect reinforcements, sometimes it want to patrol ext, but his party is so weak even without anyone. So we sometimes see
			#(0/1) parties in map with only one wounded lord inside. Because after wars completely defeated lords spawn again in a walled center
			#in 48 hours periods (by codes in module_simple_trigers). He spawns with only wounded himself. Then he should wait in there for
			#a time to collect new men to his (0/1) party. If a lord is the only one in his party and if he is at any walled center already then he
			#should stay where he is. He should not travel to anywhere because of any reason. If he is the only one and he is wounded and
			#he is not in any walled center this means this situation happens because of one another bug, because any lord cannot be out of
			#walled centers with wounded himself only. So I am adding this condition below.
			
			#SUMMARY : If lord has not got enought troops (<10 || <10%) with himself and he is currently at a walled center he should not leave
			#his current center because of any reason.
			
			(ge, ":cur_center_no", 0),
			(this_or_next|le, ":party_fit_for_battle", 10),
			(le, ":party_strength_as_percentage_of_ideal", 30), #tom was 30
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":cur_center_no"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_need_to_raise_some_men_before_attempting_anything_else"),
			(str_store_string, s16, "str_i_need_to_raise_some_men_before_attempting_anything_else"),
			(try_end),
			#Stand in a siege
		(else_try),
			(gt, ":besieger_party", -1),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":cur_center_no"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_cannot_leave_this_fortress_now_as_it_is_under_siege"),
			(str_store_string, s16, "str_after_all_we_are_under_siege"),
			(try_end),
			
			#Continue retreat to walled center
		(else_try),
			(eq, ":old_ai_state", spai_retreating_to_center),
				(neg|party_is_in_any_town, ":party_no"),
			
				(ge, ":old_ai_object", 0),
				(party_is_active, ":old_ai_object"),
			
				(store_faction_of_party, ":retreat_center_faction", ":old_ai_object"),
				(eq, ":faction_no", ":retreat_center_faction"),
			
				(assign, ":action", spai_retreating_to_center),
				(assign, ":object", ":old_ai_object"),
			
				(try_begin),
				(eq, ":troop_no", "$g_talk_troop"),
				(str_store_string, s14, "str_we_are_not_strong_enough_to_face_the_enemy_out_in_the_open"),
				(str_store_string, s16, "str_i_should_probably_seek_shelter_behind_some_stout_walls"),
				(try_end),
			#Stand by in current center against enemies
		(else_try),
			(is_between, ":cur_center_no", walled_centers_begin, walled_centers_end),
			# (party_get_slot, ":enemy_strength_in_area", ":cur_center_no", slot_center_sortie_enemy_strength), #tom
			(party_get_slot, ":enemy_strength_in_area", ":cur_center_no", slot_center_sortie_enemy_strength),
			(ge, ":enemy_strength_in_area", 50),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":cur_center_no"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_need_to_raise_some_men_before_attempting_anything_else"),
			(str_store_string, s16, "str_i_need_to_raise_some_men_before_attempting_anything_else"),
			(try_end),
			
			#As the marshall, lead faction campaign
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			(str_clear, s15), #Does not say that overrides faction orders
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
			
			(party_set_ai_initiative, ":party_no", 10),
			
			#new ozan added - active gathering
			#this code will allow marshal to travel around cities while gathering army if currently collected are less than 60%.
			#By ratio increases travel distances become less. Travels will be only points around walled centers.
			(party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
			(assign, ":travel_target", ":old_ai_object"),
			
			(call_script, "script_find_center_to_defend", ":troop_no"),
			(assign, ":most_threatened_center", reg0),
			(assign, ":travel_target_new_assigned", 0),
			
			(try_begin),
			(lt, ":old_ai_object", 0),
			
			(store_random_in_range, ":random_value", 0, 8), #to eanble marshal to wait sometime during active gathering
			(this_or_next|eq, "$g_gathering_new_started", 1),
			(eq, ":random_value", 0),
			
			(assign, ":vassals_already_assembled", 0),
			(assign, ":total_vassals", 0),
			(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
				(store_faction_of_troop, ":lord_faction", ":lord"),
				(eq, ":lord_faction", ":faction_no"),
				(troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
				(party_is_active, ":led_party"),
				(val_add, ":total_vassals", 1),
				
				(party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
				(party_slot_eq, ":led_party", slot_party_ai_object, ":party_no"),
				
				(party_is_active, ":party_no"),
				(store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":party_no"),
				(lt, ":distance_to_marshal", 15),
				(val_add, ":vassals_already_assembled", 1),
			(try_end),
			
			(assign, ":ratio_of_vassals_assembled", -1),
			(try_begin),
				(gt, ":total_vassals", 0),
				(store_mul, ":ratio_of_vassals_assembled", ":vassals_already_assembled", 100),
				(val_div, ":ratio_of_vassals_assembled", ":total_vassals"),
			(try_end),
			
			(try_begin),
				#if more than 35% of vassals already collected do not make any more active gathering, just hold and wait last vassals to participate.
				(le, ":ratio_of_vassals_assembled", 35),
				
				(assign, ":best_center_to_travel", ":most_threatened_center"),
				
				(try_begin),
				(eq, "$g_gathering_new_started", 1),
				
				(assign, ":minimum_distance", 100000),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(eq, ":center_faction", ":faction_no"),
					(try_begin),
					(neq, ":center_no", ":most_threatened_center"), #200
					(store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
					(lt, ":dist", ":minimum_distance"),
					(assign, ":minimum_distance", ":dist"),
					(assign, ":best_center_to_travel", ":center_no"),
					(try_end),
				(try_end),
				(else_try),
				#active gathering
				(assign, ":max_travel_distance", 150),
				(try_begin),
					(ge, ":ratio_of_vassals_assembled",15),
					(store_sub, ":max_travel_distance", 35, ":ratio_of_vassals_assembled"),
					(val_add, ":max_travel_distance", 5), #5..25
					(val_mul, ":max_travel_distance", 6), #30..150
				(try_end),
				
				(try_begin),
					(ge, ":most_threatened_center", 0),
					(store_distance_to_party_from_party, reg12, ":party_no", ":most_threatened_center"),
				(else_try),
					(assign, reg12, 0),
				(try_end),
				
				(assign, ":num_centers", 0),
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(eq, ":center_faction", ":faction_no"),
					(try_begin),
					#(ge, ":max_travel_distance", 0),
					(store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
					
					(try_begin),
						(ge, ":most_threatened_center", 0),
						(store_distance_to_party_from_party, reg13, ":center_no", ":most_threatened_center"),
					(else_try),
						(assign, reg13, 0),
					(try_end),
					
					(store_sub, reg11, reg13, reg12),
					
					(this_or_next|ge, reg11, 40),
					(this_or_next|ge, ":dist", ":max_travel_distance"),
					(eq, ":center_no", ":most_threatened_center"),
					(else_try),
					#this center is a candidate so increase num_centers by one.
					(val_add, ":num_centers", 1),
					(try_end),
				(try_end),
				
				(try_begin),
					(ge, ":num_centers", 0),
					(store_random_in_range, ":random_center_no", 0, ":num_centers"),
					(val_add, ":random_center_no", 1),
					(assign, ":num_centers", 0),
					(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(eq, ":center_faction", ":faction_no"),
					(try_begin),
						(neq, ":center_no", ":most_threatened_center"),
						(store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
						(lt, ":dist", ":max_travel_distance"),
						
						(try_begin),
						(ge, ":most_threatened_center", 0),
						(store_distance_to_party_from_party, reg13, ":center_no", ":most_threatened_center"),
						(else_try),
						(assign, reg13, 0),
						(try_end),
						
						(store_sub, reg11, reg13, reg12),
						(lt, reg11, 40),
						
						(val_sub, ":random_center_no", 1),
						(eq, ":random_center_no", 0),
						(assign, ":best_center_to_travel", ":center_no"),
					(try_end),
					(try_end),
				(try_end),
				(try_end),
				
				(assign, ":travel_target", ":best_center_to_travel"),
				(assign, ":travel_target_new_assigned", 1),
			(try_end),
			(else_try),
			#if party has an ai object and they are close to that object while gathering army,
			#forget that ai object so they will select a new ai object next.
			(is_between, ":old_ai_object", centers_begin, centers_end),
			(party_get_position, pos1, ":party_no"),
			(party_get_position, pos2, ":old_ai_object"),
			(get_distance_between_positions, ":dist", pos1, pos2),
			(le, ":dist", 3),
			(assign, ":travel_target", -1),
			(try_end),
			#end ozan
			
			(try_begin),
			(eq, ":travel_target", -1),
			(assign, ":action", spai_undefined),
			(else_try),
			(assign, ":action", spai_visiting_village),
			(try_end),
			
			(assign, ":object", ":travel_target"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(try_begin),
				(eq, ":travel_target", -1),
				(str_store_string, s14, "str_as_the_marshall_i_am_assembling_the_army_of_the_realm"),
			(else_try),
				(try_begin),
				(eq, ":faction_no", "$players_kingdom"),
				(eq, ":travel_target_new_assigned", 1),
				(le, "$number_of_report_to_army_quest_notes", 13),
				(check_quest_active, "qst_report_to_army"),
				(str_store_party_name_link, s10, ":travel_target"),
				
				(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
				
				(str_store_troop_name_link, s11, ":faction_marshal"),
				(store_current_hours, ":hours"),
				(call_script, "script_game_get_date_text", 0, ":hours"),
				
				(str_store_string, s14, "str_as_the_marshall_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals"),
				(str_store_string, s14, "@({s1}) {s11}: {s14}"),
				(add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
				(val_add, "$number_of_report_to_army_quest_notes", 1),
				(try_end),
				
				(assign, reg0, ":travel_target"),
				(str_store_party_name, s10, ":travel_target"),
				(str_store_string, s14, "str_as_the_marshall_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals"),
			(try_end),
			(str_store_string, s16, "str_i_intend_to_assemble_the_army_of_the_realm"),
			(try_end),
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
			(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
			
			(assign, ":action", spai_besieging_center),
			(assign, ":object", ":faction_object"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_as_the_marshall_i_am_leading_the_siege"),
			(str_store_string, s16, "str_i_intend_to_begin_the_siege"),
			(try_end),
			
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
			(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
			
			(assign, ":action", spai_raiding_around_center),
			(assign, ":object", ":faction_object"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_as_the_marshall_i_am_leading_our_raid"),
			(str_store_string, s16, "str_i_intend_to_start_our_raid"),
			(try_end),
			
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
			(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
			(party_is_active, ":faction_object"),
			
			#moved (party_set_ai_initiative, ":party_no", 10), #new to avoid losing time of marshal with attacking unimportant targets while there is a threat in our centers.
			
			(party_get_battle_opponent, ":besieger_party", ":faction_object"),
			
			(try_begin),
			(gt, ":besieger_party", 0),
			(party_is_active, ":besieger_party"),
			
			(assign, ":action", spai_engaging_army),
			(assign, ":object", ":besieger_party"),
			(try_begin),
				(eq, ":troop_no", "$g_talk_troop"),
				(str_store_string, s14, "str_as_the_marshall_i_am_leading_our_forces_to_engage_the_enemy_in_battle"),
				(str_store_string, s16, "str_i_intend_to_lead_our_forces_out_to_engage_the_enemy"),
			(try_end),
			(else_try),
			(assign, ":action", spai_patrolling_around_center),
			(assign, ":object", ":faction_object"),
			(try_begin),
				(eq, ":troop_no", "$g_talk_troop"),
				(str_store_string, s14, "str_as_the_marshall_i_am_leading_our_forces_in_search_of_the_enemy"),
				(str_store_string, s16, "str_i_intend_to_lead_our_forces_out_to_find_the_enemy"),
			(try_end),
			(try_end),
			
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemy_army),
			(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
			(party_is_active, ":faction_object"),
			
			(assign, ":action", spai_engaging_army),
			(assign, ":object", ":faction_object"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_as_the_marshall_i_am_leading_our_forces_to_engage_the_enemy_in_battle"),
			(str_store_string, s16, "str_i_intend_to_lead_our_forces_out_to_engage_the_enemy"),
			(try_end),
			
			#Get reinforcements
		(else_try),
			#(assign, ":lowest_acceptable_strength_percentage", 30),
			(assign, ":lowest_acceptable_strength_percentage", 30), #tom was 30
			
			#if troop has enought gold then increase by 10%
			#(troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
			#(try_begin),
			#  (ge, ":cur_wealth", 2000),
			#  (assign, ":wealth_addition", 10),
			#(else_try),
			#  (store_div, ":wealth_addition", ":cur_wealth", 200),
			#(try_end),
			#(val_add, ":lowest_acceptable_strength_percentage", ":wealth_addition"),
			
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			(gt, ":home_center", -1),
			(party_slot_eq, ":home_center", slot_town_lord, ":troop_no"), #newly added
			
			#if troop is very close to its home center increase by 20%
			(assign, ":distance_addition", 0),
			(party_get_position, pos0, ":home_center"),
			(party_get_position, pos1, ":party_no"),
			(get_distance_between_positions, ":dist", pos0, pos1),
			
			(try_begin),
			(le, ":dist", 9000),
			(store_div, ":distance_addition", ":dist", 600),
			(store_sub, ":distance_addition", 15, ":distance_addition"),
			(else_try),
			(assign, ":distance_addition", 0),
			(try_end),
			(val_add, ":lowest_acceptable_strength_percentage", ":distance_addition"),
			
			#if there is no campaign for faction increase by 35%
			(assign, ":no_campaign_addition", 35),
			(try_begin),
			(this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemy_army),
			(this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
			(this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
			(this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
			(assign, ":no_campaign_addition", 0),
			
			#If marshal is player itself and if there is a campaign then lower lowest_acceptable_strength_percentage by 10 instead of not changing it.
			#Because players become confused when they see very less participation from AI lords to their campaigns.
			(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_marshall, "trp_player"),
				(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
				(try_begin),
				(eq, ":reduce_campaign_ai", 0), #hard
				(assign, ":no_campaign_addition", 0),
				(else_try),
				(eq, ":reduce_campaign_ai", 1), #medium
				(assign, ":no_campaign_addition", -10),
				(else_try),
				(eq, ":reduce_campaign_ai", 2), #easy
				(assign, ":no_campaign_addition", -15),
				(try_end),
			(try_end),
			(try_end),
			(val_add, ":lowest_acceptable_strength_percentage", ":no_campaign_addition"),
			(val_max, ":lowest_acceptable_strength_percentage", 25),
			
			#max : 30%+15%+35% = 80% (happens when there is no campaign and player is near to its home center.)
			(lt, ":party_strength_as_percentage_of_ideal", ":lowest_acceptable_strength_percentage"),
			
			(try_begin),
			(store_div, ":lowest_acceptable_strength_percentage_div_3", ":lowest_acceptable_strength_percentage", 3),
			(ge, ":party_strength_as_percentage_of_ideal", ":lowest_acceptable_strength_percentage_div_3"),
			(troop_get_slot, ":troop_wealth", ":troop_no", slot_troop_wealth),
			(le, ":troop_wealth", 1800),
			(assign, ":do_only_collecting_rents", 1),
			(try_end),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":home_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_dont_have_enough_troops_and_i_need_to_get_some_more"),
			
			(str_store_string, s16, "str_i_am_running_low_on_troops"),
			(try_end),
			
			(eq, ":do_only_collecting_rents", 0),
			
			#follow player orders
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(party_slot_ge, ":party_no", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
			
			(party_get_slot, ":orders_type", ":party_no", slot_party_orders_type),
			(party_get_slot, ":orders_object", ":party_no", slot_party_orders_object),
			(party_get_slot, ":orders_time", ":party_no", slot_party_orders_time),
			
			(ge, ":orders_object", 0),
			
			(store_current_hours, ":hours_since_orders_given"),
			(val_sub, ":hours_since_orders_given", ":orders_time"),
			
			(party_is_active, ":orders_object"),
			(party_get_slot, ":object_state", ":orders_object", slot_village_state),
			(store_faction_of_party, ":object_faction", ":orders_object"),
			(store_relation, ":relation_with_object", ":faction_no", ":object_faction"),
			
			(assign, ":orders_are_appropriate", 1),
			(try_begin),
			(gt, ":hours_since_orders_given", 48),
			(assign, ":orders_are_appropriate", 0),
			(else_try),
			(eq, ":orders_type", spai_raiding_around_center),
			(this_or_next|ge, ":relation_with_object", 0),
			(ge, ":object_state", 2),
			(assign, ":orders_are_appropriate", 0),
			(else_try),
			(eq, ":orders_type", spai_besieging_center),
			(ge, ":relation_with_object", 0),
			(assign, ":orders_are_appropriate", 0),
			(else_try),
			(this_or_next|eq, ":orders_type", spai_holding_center),
			(this_or_next|eq, ":orders_type", spai_retreating_to_center),
			(this_or_next|eq, ":orders_type", spai_accompanying_army),
			(eq, ":orders_type", spai_visiting_village),
			(le, ":relation_with_object", 0),
			(assign, ":orders_are_appropriate", 0),
			(try_end),
			
			(eq, ":orders_are_appropriate", 1),
			
			(assign, ":action", ":orders_type"),
			(assign, ":object", ":orders_object"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_we_are_following_your_direction"),
			(try_end),
			
			#Host of player wedding
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":operation_in_progress", 0),
			(check_quest_active, "qst_wed_betrothed"),
			(quest_slot_eq, "qst_wed_betrothed", slot_quest_giver_troop, ":troop_no"),
			(quest_get_slot, ":bride", "qst_wed_betrothed", slot_quest_target_troop),
			(call_script, "script_get_kingdom_lady_social_determinants", ":bride"),
			(assign, ":wedding_venue", reg1),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":wedding_venue"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_need_to_make_preparations_for_your_wedding"),
			(str_store_string, s16, "str_after_all_i_need_to_make_preparations_for_your_wedding"),
			(try_end),
			
			#Bridegroom at player wedding
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":operation_in_progress", 0),
			(check_quest_active, "qst_wed_betrothed_female"),
			(quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, ":troop_no"),
			
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
			(faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":feast_venue"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_am_heading_to_the_site_of_our_wedding"),
			(str_store_string, s16, "str_after_all_we_are_soon_to_be_wed"),
			(try_end),
			
			#Host of other feast
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":operation_in_progress", 0),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
			(faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
			(party_slot_eq, ":feast_venue", slot_town_lord, ":troop_no"),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":feast_venue"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_am_hosting_a_feast_there"),
			(str_store_string, s16, "str_i_have_a_feast_to_host"),
			(try_end),
			
			#I am the bridegroom at a feast
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":operation_in_progress", 0),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
			(troop_get_slot, ":troop_betrothed", ":troop_no", slot_troop_betrothed),
			(is_between, ":troop_betrothed", kingdom_ladies_begin, kingdom_ladies_end),
			
			(faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":feast_venue"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_am_to_be_the_bridegroom_there"),
			(str_store_string, s16, "str_my_wedding_day_draws_near"),
			(try_end),
			
			#Drop off prisoners
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(gt,  ":party_ratio_of_prisoners", 35),
			(eq, ":operation_in_progress", 0),
			
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			
			(gt, ":home_center", -1),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":home_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_have_too_much_loot_and_too_many_prisoners_and_need_to_secure_them"),
			(str_store_string, s16, "str_i_should_think_of_dropping_off_some_of_my_prisoners"),
			(try_end),
			
			#Reinforce a weak center
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(assign, ":center_to_reinforce", -1),
			(assign, ":center_reinforce_score", 100),
			(eq, ":operation_in_progress", 0),
			
			(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(party_slot_eq, ":walled_center", slot_town_lord, ":troop_no"),
			(party_get_slot, ":center_strength", ":walled_center", slot_party_cached_strength),
			(lt, ":center_strength", ":center_reinforce_score"),
			(assign, ":center_to_reinforce", ":walled_center"),
			(assign, ":center_reinforce_score", ":center_strength"),
			(try_end),
			
			(gt, ":center_to_reinforce", -1),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":center_to_reinforce"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_need_to_reinforce_it_as_it_is_poorly_garrisoned"),
			(str_store_string, s16, "str_there_is_a_hole_in_our_defenses"),
			(try_end),
			
			#Continue screening, if already doing so
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":old_ai_state", spai_screening_army),
			
			(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
			(ge, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
			(party_is_active, ":marshal_party"),
			
			(call_script, "script_npc_decision_checklist_troop_follow_or_not", ":troop_no"),
			(eq, reg0, 1),
			
			(assign, ":action", spai_screening_army),
			(assign, ":object", ":marshal_party"),
			(try_begin),
			(eq, "$g_talk_troop", ":troop_no"),
			(str_store_string, s14, "str_i_am_following_the_marshals_orders"),
			(str_store_string, s16, "str_the_marshal_has_given_me_this_command"),
			(try_end),
			
		(else_try), #special case for sfai_attacking_enemies_around_center for village raids
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
			(is_between, ":faction_object", villages_begin, villages_end),
			
			(call_script, "script_npc_decision_checklist_troop_follow_or_not", ":troop_no"),
			(eq, reg0, 1),
			
			(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
			(party_get_slot, ":raider_party", ":faction_object", slot_village_raided_by),
			(party_is_active, ":raider_party"),
			
			#think about adding one more condition here, what if raider army is so powerfull, again lords will go and engage enemy one by one?
			(party_get_slot, ":enemy_strength_nearby", ":faction_object", slot_center_sortie_enemy_strength),
			(lt, ":enemy_strength_nearby", 4000), #tom was 4000
			#end think
			
			(assign, ":action", spai_engaging_army),
			(assign, ":object", ":raider_party"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_our_realm_needs_my_support_there_is_enemy_raiding_one_of_our_villages_which_is_not_to_far_from_here_i_am_going_there"),
			(str_store_string, s16, "str_the_marshal_has_issued_a_summons"),
			(try_end),
			
			#Follow the marshall's orders - if on the offensive, and the campaign has not lasted too long. Readiness is currently randomly set
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(call_script, "script_npc_decision_checklist_troop_follow_or_not", ":troop_no"),
			(eq, reg0, 1),
			
			(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
			(ge, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
			
			(assign, ":action", spai_accompanying_army),
			(assign, ":object", ":marshal_party"),
			
			(try_begin),
			(eq, "$g_talk_troop", ":troop_no"),
			(str_store_string, s14, "str_i_am_answering_the_marshals_summons"),
			(str_store_string, s16, "str_the_marshal_has_issued_a_summons"),
			(try_end),
			
			#Support a nearby ally who is on the offensive
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":faction_is_at_war", 1),
			
			(assign, ":party_to_support", -1),
			(try_for_range, ":allied_hero", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":allied_hero", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":allied_hero_faction", ":allied_hero"),
			(eq, ":allied_hero_faction", ":faction_no"),
			
			(neq, ":allied_hero", ":troop_no"),
			
			(troop_get_slot, ":allied_hero_party", ":allied_hero", slot_troop_leaded_party),
			(gt, ":allied_hero_party", 1),
			(party_is_active, ":allied_hero_party"),
			
			
			(this_or_next|party_slot_eq, ":allied_hero_party", slot_party_ai_state, spai_raiding_around_center),
			(party_slot_eq, ":allied_hero_party", slot_party_ai_state, spai_besieging_center),
			
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":allied_hero"),
			(gt, reg0, 4),
			
			(troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
			(troop_get_slot, ":ally_renown", ":allied_hero", slot_troop_renown),
			(le, ":troop_renown", ":ally_renown"), #Ally to support must have higher renown
			
			(store_distance_to_party_from_party, ":distance", ":party_no", ":allied_hero_party"),
			
			(lt, ":distance", 5),
			
			(assign, ":party_to_support", ":allied_hero_party"),
			(try_end),
			(gt, ":party_to_support", 0),
			
			(assign, ":action", spai_accompanying_army),
			(assign, ":object", ":party_to_support"),
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(party_stack_get_troop_id, ":leader", ":object", 0),
			(str_store_troop_name, s10, ":leader"),
			
			(call_script, "script_troop_get_family_relation_to_troop", ":leader", "$g_talk_troop"),
			(try_begin),
				(eq, reg0, 0),
				(str_store_string, s11, "str_comradeinarms"),
			(try_end),
			(str_store_string, s14, "str_i_am_supporting_my_s11_s10"),
			(str_store_string, s16, "str_i_believe_that_one_of_my_comrades_is_in_need"),
			(try_end),
			#I have decided to attack a vulnerable fortress
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":faction_is_at_war", 1),
			(eq, ":operation_in_progress", 0),
			
			(assign, ":walled_center_to_attack", -1),
			(assign, ":walled_center_score", 50),
			
			(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":walled_center_faction", ":walled_center"),
			(store_relation, ":relation", ":faction_no", ":walled_center_faction"),
			(lt, ":relation", 0),
			
			(party_get_slot, ":center_cached_strength", ":walled_center", slot_party_cached_strength),
			(val_mul, ":center_cached_strength", 3),
			(val_mul, ":center_cached_strength", 2),
			
			# (assign, reg30, ":party_cached_strength"),
			# (display_message, "@stength party:{reg30}"),
			#(val_add, ":party_cached_strength", 500), #tom
			(lt, ":center_cached_strength", ":party_cached_strength"),
			(lt, ":center_cached_strength", 750), #tom was 750
			#(val_sub, ":party_cached_strength", 500), #tom
			
			(party_slot_eq, ":walled_center", slot_village_state, svs_normal),
			(store_distance_to_party_from_party, ":distance", ":walled_center", ":party_no"),
			(lt, ":distance", ":walled_center_score"),
			
			(assign, ":walled_center_to_attack", ":walled_center"),
			(assign, ":walled_center_score", ":distance"),
			(try_end),
			
			(is_between, ":walled_center_to_attack", centers_begin, centers_end),
			
			(assign, ":action", spai_besieging_center),
			(assign, ":object", ":walled_center_to_attack"),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_faction_name, s20, ":faction_no"),
			(str_store_party_name, s21, ":object"),
			(display_message, "str_s20_decided_to_attack_s21"),
			(try_end),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_a_fortress_is_vulnerable"),
			(str_store_string, s16, "str_i_believe_that_the_enemy_may_be_vulnerable"),
			(try_end),
			
			#I am visiting an estate
		(else_try),
			(assign, ":center_to_visit", -1),
			(assign, ":score_to_beat", 300), #at least 300 gold to pick up
			(troop_get_slot, ":troop_wealth", ":troop_no", slot_troop_wealth), #average troop wealth is 2000
			(val_div, ":troop_wealth", 10), #average troop wealth 10% is is 200
			(val_add, ":score_to_beat", ":troop_wealth"), #average score to beat is 500
			(eq, ":operation_in_progress", 0),
			
			(try_begin),
			(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
			
			(assign, reg17, 0),
			(try_begin),
				(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
				(party_slot_eq, ":party_no", slot_party_ai_object, ":faction_marshal"),
				(assign, reg17, 1),
			(else_try),
				(party_slot_eq, ":party_no", slot_party_following_player, 1),
				(assign, reg17, 1),
			(try_end),
			(eq, reg17, 1),
			
			(try_begin),
				(neq, ":faction_marshal", "trp_player"),
				(neg|party_slot_eq, ":party_no", slot_party_following_player, 1),
				(val_add, ":score_to_beat", 125),
			(else_try),
				(val_add, ":score_to_beat", 250),
			(try_end),
			(try_end),
			
			(try_for_range, ":center_no", centers_begin, centers_end),
			(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
			
			(assign, reg17, 0),
			(try_begin),
				(is_between, ":center_no", villages_begin, villages_end),
				(party_slot_eq, ":center_no", slot_village_state, svs_normal),
				(assign, reg17, 1),
			(else_try),
				(party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
				(assign, reg17, 1),
			(try_end),
			(eq, reg17, 1),
			
			(party_get_slot, ":tariffs_available", ":center_no", slot_center_accumulated_tariffs),
			(party_get_slot, ":rents_available", ":center_no", slot_center_accumulated_rents),
			(store_add, ":money_available", ":rents_available", ":tariffs_available"),
			
			(gt, ":money_available", ":score_to_beat"),
			(assign, ":center_to_visit", ":center_no"),
			(assign, ":score_to_beat", ":money_available"),
			(try_end),
			
			(is_between, ":center_to_visit", centers_begin, centers_end),
			
			(try_begin),
			(is_between, ":center_to_visit", walled_centers_begin, walled_centers_end),
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":center_to_visit"),
			(else_try),
			(assign, ":action", spai_visiting_village),
			(assign, ":object", ":center_to_visit"),
			(try_end),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_need_to_inspect_my_properties_and_collect_my_dues"),
			(str_store_string, s16, "str_it_has_been_too_long_since_i_have_inspected_my_estates"),
			(try_end),
			
			#My men are weary, and I wish to return home
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(this_or_next|gt, ":hours_since_last_rest", 504), #Three weeks
			(lt, ":aggressiveness", 25),
			(gt, ":hours_since_last_rest", 168), #one week if aggressiveness < 25
			(eq, ":operation_in_progress", 0),
			
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			
			(gt, ":home_center", -1),
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":home_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_my_men_are_weary_so_we_are_returning_home"),
			(str_store_string, s16, "str_my_men_are_becoming_weary"),
			(try_end),
			
			#I have a score to settle with the enemy
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(this_or_next|gt, ":hours_since_last_combat", 12),
			(lt, ":hours_since_last_rest", 96),
			(eq, ":operation_in_progress", 0),
			
			(eq, ":faction_is_at_war", 1),
			(this_or_next|eq, ":troop_reputation", lrep_debauched),
			(eq, ":troop_reputation", lrep_quarrelsome),
			
			(assign, ":target_village", -1),
			(assign, ":score_to_beat", 0), #based on relation
			
			(try_for_range, ":possible_target", villages_begin, villages_end),
			(store_faction_of_party, ":village_faction", ":possible_target"),
			(store_relation, ":relation", ":village_faction", ":faction_no"),
			(lt, ":relation", 0),
			
			(neg|party_slot_ge, ":possible_target", slot_village_state, svs_looted),
			(party_get_slot, ":town_lord", ":possible_target", slot_town_lord),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":town_lord"),
			(assign, ":village_score", reg0),
			
			(lt, ":village_score", ":score_to_beat"),
			(assign, ":score_to_beat", ":village_score"),
			(assign, ":target_village", ":possible_target"),
			(try_end),
			
			(is_between, ":target_village", centers_begin, centers_end),
			(assign, ":action", spai_raiding_around_center),
			(assign, ":object", ":target_village"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_have_a_score_to_settle_with_the_lord_there"),
			(str_store_string, s16, "str_i_am_thinking_of_settling_an_old_score"),
			(try_end),
			
			#I need money, so I am raiding where the money is
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":faction_is_at_war", 1),
			(eq, ":operation_in_progress", 0),
			
			(this_or_next|gt, ":hours_since_last_combat", 12),
			(lt, ":hours_since_last_rest", 96),
			(gt, ":aggressiveness", 40),
			
			(this_or_next|eq, ":troop_reputation", lrep_debauched),
			(this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
			(this_or_next|eq, ":troop_reputation", lrep_cunning),
			(eq, ":troop_reputation", lrep_quarrelsome),
			
			(troop_get_slot, ":wealth", ":troop_no", slot_troop_wealth),
			(lt, ":wealth", 500),
			
			(assign, ":score_to_beat", 0),
			(assign, ":target_village", -1),
			
			(try_for_range, ":possible_target", villages_begin, villages_end),
			(store_faction_of_party, ":village_faction", ":possible_target"),
			(store_relation, ":relation", ":village_faction", ":faction_no"),
			(lt, ":relation", 0),
			
			(this_or_next|party_slot_eq, ":possible_target", slot_village_state, svs_normal),
			(party_slot_eq, ":possible_target", slot_village_state, svs_being_raided),
			
			(party_get_slot, reg17, ":possible_target", slot_town_prosperity),
			(store_distance_to_party_from_party, ":distance", ":party_no", ":possible_target"),
			(val_sub, reg17, ":distance"),
			
			(gt, reg17, ":score_to_beat"),
			(assign, ":score_to_beat", reg17),
			(assign, ":target_village", ":possible_target"),
			(try_end),
			
			(gt, ":target_village", -1),
			
			(assign, ":action", spai_raiding_around_center),
			(assign, ":object", ":target_village"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_am_short_of_money_and_i_hear_that_there_is_much_wealth_there"),
			(str_store_string, s16, "str_i_need_to_refill_my_purse_preferably_with_the_enemys_money"),
			(try_end),
			
			#Attacking wealthiest lands
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":faction_is_at_war", 1),
			(eq, ":operation_in_progress", 0),
			(gt, ":aggressiveness", 65),
			
			(assign, ":score_to_beat", 0),
			(assign, ":target_village", -1),
			
			(try_for_range, ":possible_target", villages_begin, villages_end),
			(store_faction_of_party, ":village_faction", ":possible_target"),
			(store_relation, ":relation", ":village_faction", ":faction_no"),
			(lt, ":relation", 0),
			(neg|party_slot_eq, ":possible_target", slot_village_state, svs_looted),
			(party_get_slot, ":village_prosperity", ":possible_target", slot_town_prosperity),
			(val_mul, ":village_prosperity", 2),
			
			(store_distance_to_party_from_party, ":distance", ":party_no", ":possible_target"),
			(val_sub, ":village_prosperity", ":distance"),
			(gt, ":village_prosperity", ":score_to_beat"),
			
			(assign, ":score_to_beat", ":village_prosperity"),
			(assign, ":target_village", ":possible_target"),
			(try_end),
			
			(gt, ":target_village", -1),
			
			(assign, ":action", spai_raiding_around_center),
			(assign, ":object", ":target_village"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_by_striking_at_the_enemys_richest_lands_perhaps_i_can_draw_them_out_to_battle"),
			(str_store_string, s16, "str_i_am_thinking_of_going_on_the_attack"),
			(try_end),
			
			#End the war
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":troop_reputation", lrep_upstanding),
			(eq, ":faction_is_at_war", 1),
			(eq, ":operation_in_progress", 0),
			
			(assign, ":faction_to_attack", -1),
			(try_for_range, ":possible_faction_to_attack", kingdoms_begin, kingdoms_end),
			(store_relation, ":relation", ":faction_no", ":possible_faction_to_attack"),
			(lt, ":relation", 0),
			(faction_slot_eq, ":possible_faction_to_attack", slot_faction_state, sfs_active),
			
			(store_add, ":war_damage_inflicted_slot", ":possible_faction_to_attack", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":war_damage_inflicted_slot", kingdoms_begin),
			(faction_get_slot, ":war_damage_inflicted", ":faction_no", ":war_damage_inflicted_slot"),
			
			(store_add, ":war_damage_suffered_slot", ":faction_no", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":war_damage_suffered_slot", kingdoms_begin),
			(faction_get_slot, ":war_damage_suffered", ":possible_faction_to_attack", ":war_damage_suffered_slot"),
			
			(gt, ":war_damage_inflicted", 80),
			(lt, ":war_damage_inflicted", ":war_damage_suffered"),
			(assign, ":faction_to_attack", ":possible_faction_to_attack"),
			(try_end),
			
			(gt, ":faction_to_attack", -1),
			
			(assign, ":target_village", -1),
			(assign, ":score_to_beat", 50),
			
			(try_for_range, ":possible_target_village", villages_begin, villages_end),
			(store_faction_of_party, ":village_faction", ":possible_target_village"),
			(eq, ":village_faction", ":faction_to_attack"),
			(neg|party_slot_eq, ":possible_target_village", slot_village_state, svs_looted),
			(store_distance_to_party_from_party, ":distance", ":party_no", ":possible_target_village"),
			(lt, ":distance", ":score_to_beat"),
			
			(assign, ":score_to_beat", ":distance"),
			(assign, ":target_village", ":possible_target_village"),
			(try_end),
			
			(gt, ":target_village", -1),
			
			(assign, ":action", spai_raiding_around_center),
			(assign, ":object", ":target_village"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_perhaps_if_i_strike_one_more_blow_we_may_end_this_war_on_our_terms_"),
			(str_store_string, s16, "str_we_may_be_able_to_bring_this_war_to_a_close_with_a_few_more_blows"),
			(try_end),
			
			#I have a feast to attend
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
			(faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
			(party_get_slot, ":feast_host", ":feast_venue", slot_town_lord),
			(eq, ":operation_in_progress", 0),
			
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":feast_host"),
			(assign, ":relation_with_host", reg0),
			
			(ge, ":relation_with_host", 0),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":feast_venue"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_wish_to_attend_the_feast_there"),
			(str_store_string, s16, "str_there_is_a_feast_which_i_wish_to_attend"),
			(try_end),
			#A lady to court
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(neg|troop_slot_eq, "trp_player", slot_troop_betrothed, ":troop_no"),
			(troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
			(neg|is_between, ":troop_no", kings_begin, kings_end),
			(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
			
			
			(gt, ":hours_since_last_courtship", 72),
			(eq, ":operation_in_progress", 0),
			
			(assign, ":center_to_visit", -1),
			(assign, ":score_to_beat", 150),
			
			(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
			(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
			(troop_get_slot, ":love_interest_center", ":love_interest", slot_troop_cur_center),
			(is_between, ":love_interest_center", centers_begin, centers_end),
			(store_faction_of_party, ":love_interest_faction_no", ":love_interest_center"),
			(eq, ":faction_no", ":love_interest_faction_no"),
			#(store_relation, ":relation", ":faction_no", ":love_interest_faction_no"),
			#(ge, ":relation", 0),
			
			(store_distance_to_party_from_party, ":distance", ":party_no", ":love_interest_center"),
			
			(lt, ":distance", ":score_to_beat"),
			(assign, ":center_to_visit", ":love_interest_center"),
			(assign, ":score_to_beat", ":distance"),
			(try_end),
			
			(gt, ":center_to_visit", -1),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":center_to_visit"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_there_is_a_fair_lady_there_whom_i_wish_to_court"),
			(str_store_string, s16, "str_i_have_the_inclination_to_pay_court_to_a_fair_lady"),
			(try_end),
			
			#Patrolling an alarmed center
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(assign, ":target_center", -1),
			(assign, ":score_to_beat", 60),
			(eq, ":operation_in_progress", 0),
			(gt, ":aggressiveness", 40),
			
			(try_for_range, ":center_to_patrol", centers_begin, centers_end), #find closest center that has spotted enemies.
			(store_faction_of_party, ":center_faction", ":center_to_patrol"),
			(eq, ":center_faction", ":faction_no"),
			(party_slot_ge, ":center_to_patrol", slot_center_last_spotted_enemy, 0),
			
			#new - begin
			(party_get_slot, ":sortie_strength", ":center_to_patrol", slot_center_sortie_strength),
			(party_get_slot, ":enemy_strength", ":center_to_patrol", slot_center_sortie_enemy_strength),
			(store_mul, ":enemy_strength_mul_14_div_10", ":enemy_strength", 14),
			(val_div, ":enemy_strength_mul_14_div_10", 10),
			(party_get_slot, ":party_strength", ":party_no", slot_party_cached_strength),
			
			(this_or_next|neg|party_is_in_town, ":party_no", ":center_to_patrol"),
			(gt, ":sortie_strength", ":enemy_strength_mul_14_div_10"),
			
			(ge, ":party_strength", 100),
			#new - end
			
			(party_get_slot, reg17, ":center_to_patrol", slot_town_lord),
			(call_script, "script_troop_get_relation_with_troop", reg17, ":troop_no"),
			
			(this_or_next|eq, ":troop_reputation", lrep_upstanding),
			(gt, reg0, -5),
			
			(store_distance_to_party_from_party, ":distance", ":party_no", ":center_to_patrol"),
			(lt, ":distance", ":score_to_beat"),
			
			(assign, ":target_center", ":center_to_patrol"),
			(assign, ":score_to_beat", ":distance"),
			(try_end),
			
			(is_between, ":target_center", centers_begin, centers_end),
			
			(assign, ":action", spai_patrolling_around_center),
			(assign, ":object", ":target_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_we_have_heard_reports_that_the_enemy_is_in_the_area"),
			(str_store_string, s16, "str_i_have_heard_reports_of_enemy_incursions_into_our_territory"),
			(try_end),
			
			#Time in household
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(gt, ":hours_since_last_home", 168),
			(eq, ":operation_in_progress", 0),
			
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			(gt, ":home_center", -1),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":home_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_need_to_spend_some_time_with_my_household"),
			(str_store_string, s16, "str_it_has_been_a_long_time_since_i_have_been_able_to_spend_time_with_my_household"),
			(try_end),
			
			#Patrolling the borders
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":faction_is_at_war", 1),
			(gt, ":aggressiveness", 65),
			(eq, ":operation_in_progress", 0),
			
			(assign, ":center_to_patrol", -1),
			(assign, ":score_to_beat", 75), #tom was 75
			
			(try_for_range, ":village", villages_begin, villages_end),
			(store_faction_of_party, ":village_faction", ":village"),
			(store_relation, ":relation", ":village_faction", ":faction_no"),
			(lt, ":relation", 0),
			
			(store_distance_to_party_from_party, ":distance", ":village", ":party_no"),
			(lt, ":distance", ":score_to_beat"),
			
			(assign, ":score_to_beat", ":distance"),
			(assign, ":center_to_patrol", ":village"),
			(try_end),
			
			(is_between, ":center_to_patrol", villages_begin, villages_end),
			
			(assign, ":action", spai_patrolling_around_center),
			(assign, ":object", ":center_to_patrol"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_am_watching_the_borders"),
			(str_store_string, s16, "str_i_may_be_needed_to_watch_the_borders"),
			(try_end),
			
			#Visiting a friend - temporarily disabled
		(else_try),
			(eq, 1, 0),
			
			#Patrolling home
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			
			(is_between, ":home_center", centers_begin, centers_end),
			(eq, ":operation_in_progress", 0),
			
			(assign, ":action", spai_patrolling_around_center),
			(assign, ":object", ":home_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_will_guard_the_areas_near_my_home"),
			(str_store_string, s16, "str_i_am_perhaps_needed_most_at_home"),
			(try_end),
			
			#Default end
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":operation_in_progress", 0),
			
			(call_script, "script_lord_get_home_center", ":troop_no"),
			(assign, ":home_center", reg0),
			(is_between, ":home_center", walled_centers_begin, walled_centers_end),
			
			(assign, ":action", spai_holding_center),
			(assign, ":object", ":home_center"),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_cant_think_of_anything_better_to_do"),
			(try_end),
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(eq, ":operation_in_progress", 1),
			
			(party_get_slot, ":action", ":party_no", slot_party_ai_state),
			(party_get_slot, ":object", ":party_no", slot_party_ai_object),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_am_completing_what_i_have_already_begun"),
			(try_end),
		(else_try),
			(eq, ":do_only_collecting_rents", 0),
			(assign, ":action", spai_undefined),
			(assign, ":object", -1),
			
			(try_begin),
			(eq, ":troop_no", "$g_talk_troop"),
			(str_store_string, s14, "str_i_dont_even_have_a_home_to_which_to_return"),
			(try_end),
		(try_end),
		
		(try_begin),
			(eq, "$cheat_mode", 2),
			(str_store_troop_name, s10, ":troop_no"),
			(display_message, "str_debug__s10_decides_s14_faction_ai_s15"),
		(try_end),
		
		(assign, reg0, ":action"),
		(assign, reg1, ":object"),
	])
	