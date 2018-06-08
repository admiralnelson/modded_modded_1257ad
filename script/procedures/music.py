from header import *


	# script_music_set_situation_with_culture
	# Input: arg1 = music_situation
	# Output: none
music_set_situation_with_culture = (
	"music_set_situation_with_culture",
		[
		(store_script_param, ":situation", 1),
		(assign, ":culture", 0), #no culture
		# Hostile area scenario
		(try_begin),
			(eq, ":situation", mtf_hostile_teritory),
				(try_begin),
					(this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_orthodox),
					(faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_catholic),
				    	(val_or, ":culture", mtf_hostile_teritory_christian),
				(else_try),
				    (val_or, ":culture", mtf_hostile_teritory_nonchristian),
				(try_end),
				(val_or, ":culture", reg0),
				(assign, reg32, ":culture"),
				(call_script, "script_modded2x_Int2Bin", reg32),
				(display_message, "@Hostile teritory scenario, flag is {s1}"),
		(else_try),
		# bandit ambush in town scenario
			(this_or_next|eq, ":situation", mtf_sit_ambushed),
			(eq, ":situation", mtf_sit_fight),
				(call_script, "script_get_culture_with_party_faction_for_music", "$g_encountered_party"),
				(val_or, ":culture", reg0),
				(call_script, "script_get_culture_with_party_faction_for_music", "p_main_party"),
				(val_or, ":culture", reg0),
				(call_script, "script_get_closest_center", "p_main_party"),
				(call_script, "script_get_culture_with_party_faction_for_music", reg0),
				(val_or, ":culture", reg0),
				(assign, reg32, ":culture"),
				(call_script, "script_modded2x_Int2Bin", reg32),
				(display_message, "@Bandit ambush scenario, flag is {s1}"),
		(else_try),
		# encounter unfriendly party in overworld map
			(eq, ":situation", mtf_sit_encounter_hostile),
	    		    (try_begin),
					    (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_orthodox),
					    (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_pagan_mongol),
					    (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_pagan_balt),
					    (faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_catholic),
					    	(val_or, ":culture", mtf_encounter_christian),
					(else_try),
					    (val_or, ":culture", mtf_encounter_nonchristian),
					(try_end),
					(assign, reg32, ":culture"),
					(call_script, "script_modded2x_Int2Bin", reg32),
					(display_message, "@encounter hostile party scenario, flag is {s1}"),
		(else_try),
		# battle theme
			(this_or_next|eq, ":situation", mtf_sit_siege),
			(eq, ":situation", mtf_sit_fight),
				(try_begin),
				    (faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_muslim),
				    	(val_or, ":culture", mtf_battle_nonchristian),
				(else_try),
				    (val_or, ":culture", mtf_battle_christian),
				(try_end),
				(assign, reg32, ":culture"),
				(call_script, "script_modded2x_Int2Bin", reg32),
				(display_message, "@battle, flag is {s1}"),
		(else_try),
		# travel
			(eq, ":situation", mtf_sit_travel),
				(call_script, "script_get_culture_with_party_faction_for_music", "p_main_party"),
				(val_or, ":culture", reg0),
				(call_script, "script_get_closest_center", "p_main_party"),
				(call_script, "script_get_culture_with_party_faction_for_music", reg0),
				(val_or, ":culture", reg0),
				(assign, reg32, ":culture"),
				(call_script, "script_modded2x_Int2Bin", reg32),
				(display_message, "@comfy travel, flag is {s1}"),
		(else_try),
		# win
			(eq, ":situation", mtf_sit_victorious),
				(call_script, "script_get_culture_with_party_faction_for_music", "p_main_party"),
				(val_or, ":culture", reg0),
				(assign, reg32, ":culture"),
				(call_script, "script_modded2x_Int2Bin", reg32),
				(display_message, "@win scenario, flag is {s1}"),
		(else_try),
		# ?		
			(eq, ":situation", mtf_sit_killed),
				(call_script, "script_get_culture_with_party_faction_for_music", "$g_encountered_party"),
				(val_or, ":culture", reg0),
		(try_end),
		(try_begin),
			# night theme variation in town
			(this_or_next|eq, ":situation", mtf_sit_town),
			(eq, ":situation", mtf_sit_day),
				(try_begin),
					(is_currently_night),
						#(assign, ":situation", mtf_sit_night),
				(try_end),
		(try_end),
		(music_set_situation, ":situation"),
		(music_set_culture, ":culture"),
		(display_message, "@music is set"),
	])
	
	
	# script_combat_music_set_situation_with_culture
	# Input: none
	# Output: none
combat_music_set_situation_with_culture = (
	"combat_music_set_situation_with_culture",
		[
		(assign, ":situation", mtf_sit_fight),
		(assign, ":num_allies", 0),
		(assign, ":num_enemies", 0),
		(try_for_agents, ":agent_no"),
			(agent_is_alive, ":agent_no"),
			(agent_is_human, ":agent_no"),
			(agent_get_troop_id, ":agent_troop_id", ":agent_no"),
			(store_character_level, ":troop_level", ":agent_troop_id"),
			(val_add,  ":troop_level", 10),
			(val_mul, ":troop_level", ":troop_level"),
			(try_begin),
			(agent_is_ally, ":agent_no"),
			(val_add, ":num_allies", ":troop_level"),
			(else_try),
			(val_add, ":num_enemies", ":troop_level"),
			(try_end),
		(try_end),
		(val_mul, ":num_allies", 4), #play ambushed music if we are 2 times outnumbered.
		(val_div, ":num_allies", 3),
		(try_begin),
			(lt, ":num_allies", ":num_enemies"),
			(assign, ":situation", mtf_sit_ambushed),
		(try_end),
		(call_script, "script_music_set_situation_with_culture", ":situation"),
		(assign,reg32, ":situation"),
		(call_script, "script_modded2x_Int2Bin", reg32),
		(display_message, "@combat music, flag {s1}"),
	])
	
	# script_play_victorious_sound
	# Input: none
	# Output: none
play_victorious_sound = (
	"play_victorious_sound",
		[
		(call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
		#(play_cue_track, "track_victorious_neutral_1"),
		(try_begin),
			(this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_orthodox),
			(faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_catholic),
				(play_track, "track_VictoryChristian", 1),	
		(else_try),
			(faction_slot_eq, "$players_kingdom", slot_faction_religion, religion_muslim ),
				(play_track, "track_VictoryMuslim", 1),	
		(else_try),
				(play_track, "track_VictoryOthers", 1),	
		(try_end),
		
	])
	