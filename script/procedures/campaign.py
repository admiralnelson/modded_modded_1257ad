from header import *

#script_player_arrived
# Called in start_phase_3 game_menus. 
# INPUT: none
# OUTPUT: none
player_arrived = (
	"player_arrived",
		[
			(assign, ":player_faction_culture", "fac_culture_western"),
			(faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, ":player_faction_culture"),
			(faction_set_slot, "fac_player_faction",  slot_faction_culture, ":player_faction_culture"),
	])

# script_game_event_party_encounter:
# This script is called from the game engine whenever player party encounters another party or a battle on the world map
# INPUT: param1: encountered_party, param2: second encountered_party (if this was a battle)
# OUTPUT: none
game_event_party_encounter = (
	"game_event_party_encounter",
		[
			(store_script_param_1, "$g_encountered_party"),
			(store_script_param_2, "$g_encountered_party_2"),# encountered_party2 is set when we come across a battle or siege, otherwise it's a negative value
			#       (store_encountered_party, "$g_encountered_party"),
			#       (store_encountered_party2,"$g_encountered_party_2"), # encountered_party2 is set when we come across a battle or siege, otherwise it's a minus value
			(store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
			(store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
			
			(party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
			(party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),
			#       (try_begin),
			#         (gt, "$g_encountered_party_2", 0),
			#         (store_faction_of_party, "$g_encountered_party_2_faction","$g_encountered_party_2"),
			#         (store_relation, "$g_encountered_party_2_relation", "$g_encountered_party_2_faction", "fac_player_faction"),
			#         (party_get_template_id,"$g_encountered_party_2_template","$g_encountered_party_2"),
			#       (else_try),
			#         (assign, "$g_encountered_party_2_faction",-1),
			#         (assign, "$g_encountered_party_2_relation", 0),
			#         (assign,"$g_encountered_party_2_template", -1),
			#       (try_end),
			
			#NPC companion changes begin
			(call_script, "script_party_count_fit_regulars", "p_main_party"),
			(assign, "$playerparty_prebattle_regulars", reg0),
			
			#        (try_begin),
			#            (assign, "$player_party__regulars", 0),
			#            (call_script, "script_party_count_fit_regulars", "p_main_party"),
			#            (gt, reg0, 0),
			#            (assign, "$player_party_contains_regulars", 1),
			#        (try_end),
			#NPC companion changes end
		##tom rebalance
			(try_begin), 
			(eq, "$culture_pool_initialized", 1),
		(eq, "$culture_pool", 1),
		(call_script, "script_rebalance_troops_by_culture"),
		(try_end),
		##tom rebalance
			
			(assign, "$g_last_rest_center", -1),
			(assign, "$talk_context", 0),
			(assign,"$g_player_surrenders",0),
			(assign,"$g_enemy_surrenders",0),
			(assign, "$g_leave_encounter",0),
			(assign, "$g_engaged_enemy", 0),
			#       (assign,"$waiting_for_arena_fight_result", 0),
			#       (assign,"$arena_bet_amount",0),
			#       (assign,"$g_player_raiding_village",0),
			(try_begin),
				(neg|is_between, "$g_encountered_party", centers_begin, centers_end),
				(rest_for_hours, 0), #stop waiting
				(assign, "$g_infinite_camping", 0),
			(try_end),
			#       (assign, "$g_permitted_to_center",0),
			(assign, "$new_encounter", 1), #check this in the menu.
			(try_begin),
				(lt, "$g_encountered_party_2",0), #Normal encounter. Not battle or siege.
				(try_begin),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(jump_to_menu, "mnu_castle_outside"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					(jump_to_menu, "mnu_castle_outside"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship),
					(jump_to_menu, "mnu_ship_reembark"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
					(jump_to_menu, "mnu_village"),
				(else_try),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
					(jump_to_menu, "mnu_cattle_herd"),
				(else_try),
					(is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
					(jump_to_menu, "mnu_training_ground"),
				(else_try),
					(party_get_template_id, ":template", "$g_encountered_party"),
					(ge, ":template", "pt_steppe_bandit_lair"),
					(lt, ":template", "pt_bandit_lair_templates_end"),
					(assign, "$loot_screen_shown", 0),
					#		   (call_script, "script_encounter_init_variables"),
					(jump_to_menu, "mnu_bandit_lair"),
				(else_try),
					(eq, "$g_encountered_party", "p_zendar"),
					(jump_to_menu, "mnu_zendar"),
				(else_try),
					(eq, "$g_encountered_party", "p_salt_mine"),
					(jump_to_menu, "mnu_salt_mine"),
				(else_try),
					(eq, "$g_encountered_party", "p_four_ways_inn"),
					(jump_to_menu, "mnu_four_ways_inn"),
				(else_try),
					(eq, "$g_encountered_party", "p_test_scene"),
					(jump_to_menu, "mnu_test_scene"),
				(else_try),
					(eq, "$g_encountered_party", "p_battlefields"),
					(jump_to_menu, "mnu_battlefields"),
				(else_try),
					(eq, "$g_encountered_party", "p_training_ground"),
					(jump_to_menu, "mnu_tutorial"),
				(else_try),
					(eq, "$g_encountered_party", "p_camp_bandits"),
					(jump_to_menu, "mnu_camp"),
		(else_try), #tom - manor
					(eq, "$g_encountered_party_template", "pt_manor"),
			(jump_to_menu, "mnu_manor_center"),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_mongol_camp_status, status_stationed),
			(eq, "$g_encountered_party_template", "pt_mongolian_camp"),
			(jump_to_menu, "mnu_mongol_camp"),
			#tom end	
				(else_try),
					# (try_begin),
					# (lt, "$g_encountered_party_relation", 0),
					# (party_slot_eq, "$g_encountered_party", slot_party_type, spt_kingdom_hero_party),
					# (try_begin),
					# (eq, "$g_battle_preparation_phase", 0),
					# (assign, "$g_battle_preparation_phase", 1),
					# (try_end),
					# (try_end),
					(jump_to_menu, "mnu_simple_encounter"),
				(try_end),
			(else_try), #Battle or siege
				(try_begin),
					(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					(try_begin),
						(eq, "$auto_enter_town", "$g_encountered_party"),
						(jump_to_menu, "mnu_town"),
					(else_try),
						(eq, "$auto_besiege_town", "$g_encountered_party"),
						(jump_to_menu, "mnu_besiegers_camp_with_allies"),
					(else_try),
						(jump_to_menu, "mnu_join_siege_outside"),
					(try_end),
				(else_try),
					(jump_to_menu, "mnu_pre_join"),
				(try_end),
			(try_end),
			(assign,"$auto_enter_town",0),
			(assign,"$auto_besiege_town",0),
	])