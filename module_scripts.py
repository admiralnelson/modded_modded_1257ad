﻿# -*- coding: utf-8 -*-

# library
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *

# include all procedures 

from script.procedures import game as procedure_game #CONTAINS HARCODED STUFFS
from script.procedures import game_init as procedure_game_init #CONTAINS HARCODED STUFFS
from script.procedures import user_interface as procedure_user_interface
from script.procedures import training as procedure_training
from script.procedures import array as procedure_array
from script.procedures import note as procedure_notes
from script.procedures import battle_ui as procedure_battle_ui

from script.procedures import multiplayer as procedure_multiplayer
from script.procedures import multiplayer_init as procedure_multiplayer_init
from script.procedures import quick_battle as procedure_quick_battle

from script.procedures import belfry as procedure_belfry
from script.procedures import wedding as procedure_wedding
from script.procedures import economy as procedure_economy
from script.procedures import troop as procedure_troop #CONTAINS HARCODED STUFFS
from script.procedures import party as procedure_party
from script.procedures import town as procedure_town
from script.procedures import battle as procedure_battle
from script.procedures import scene as procedure_scene
from script.procedures import player as procedure_player
from script.procedures import quest as procedure_quest
from script.procedures import faction as procedure_faction
from script.procedures import siege as procedure_siege
from script.procedures import banner as procedure_banner
from script.procedures import companion as procedure_companion
from script.procedures import music as procedure_music
from script.procedures import item as procedure_item
from script.procedures import tournament as procedure_tournament
from script.procedures import banner as procedure_banner
from script.procedures import note as procedure_note

from script.procedures import campaign as procedure_campaign #CONTAINS HARCODED STUFFS
from script.procedures import campaign_ai as procedure_campaign_ai
from script.procedures import campaign_simulation as procedure_campaign_simulation #CONTAINS HARCODED STUFFS
from script.procedures import ai as procedure_ai
from script.procedures import diplomacy as procedure_diplomacy

from script.procedures import graphicalfx as procedure_graphicalfx
from script.procedures import AD1257_init as procedure_AD1257_init
from script.procedures import AD1257 as procedure_AD1257
from script.procedures import AD1257_manor_scene as procedure_AD1257_manor_scene
from script.procedures import AD1257_siege as procedure_AD1257_siege
from script.procedures import AD1257_ui as procedure_AD1257_ui


# include all functions

from script.functions import game as function_game #CONTAINS HARCODED STUFFS
from script.functions import note as function_note
from script.functions import scene as function_scene
from script.functions import console as function_console 
from script.functions import multiplayer as function_multiplayer 
from script.functions import quick_battle as function_quick_battle
from script.functions import training as function_training
from script.functions import battle as function_battle
from script.functions import battle_ui as function_battle_ui

from script.functions import economy as function_economy #CONTAINS HARCODED STUFFS
from script.functions import party as function_party
from script.functions import item as function_item
from script.functions import troop as function_troop
from script.functions import faction as function_faction
from script.functions import quest as function_quest
from script.functions import town as function_town
from script.functions import player as function_player
from script.functions import campaign as function_campaign
from script.functions import banner as function_banner
from script.functions import music as function_music
from script.functions import tournament as function_tournament
from script.functions import companion as function_companion
from script.functions import player as function_player

from script.functions import AD1257 as function_AD1257
from script.functions import helper as function_helper

# include all conditional functions

from script.conditional_functions import multiplayer as cfunction_multiplayer
from script.conditional_functions import training as cfunction_training
from script.conditional_functions import battle as cfunction_battle
from script.conditional_functions import faction as cfunction_faction
from script.conditional_functions import party as cfunction_party
from script.conditional_functions import player as cfunction_player
from script.conditional_functions import bandit as cfunction_bandit
from script.conditional_functions import troop as cfunction_troop
from script.conditional_functions import banner as cfunction_banner
from script.conditional_functions import town as cfunction_town

## auto-sell
from header_operations import *
from module_items import *
from header_item_modifiers import *
## auto-sell

from header_presentations import *


# KT0 resolve
import string
from process_common import *
from module_troops import *
from module_items import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################
def get_hrd_weight(y):
	a = (y >> ibf_weight_bits) & ibf_armor_mask
	return int(25 * a)

def set_item_score():
	item_score = []
	for i_item in xrange(len(items)):
		## weight
		item_score.append((item_set_slot, i_item, slot_item_weight, get_hrd_weight(items[i_item][6])))

		## difficulty
		item_score.append((item_set_slot, i_item, slot_item_difficulty, get_difficulty(items[i_item][6])))

		## armor type
		if items[i_item][7] == imodbits_cloth:
			item_score.append((item_set_slot, i_item, slot_armor_type, armor_cloth))
		elif items[i_item][7] == imodbits_armor:
			item_score.append((item_set_slot, i_item, slot_armor_type, armor_armor))
		elif items[i_item][7] == imodbits_plate:
			item_score.append((item_set_slot, i_item, slot_armor_type, armor_plate))

		## item_best_modifier
		if items[i_item][7] == imodbits_bow:
			item_score.append((item_set_slot, i_item, slot_item_best_modifier, imod_masterwork))
		elif items[i_item][7] == imodbits_pick:
			item_score.append((item_set_slot, i_item, slot_item_best_modifier, imod_balanced))
		elif items[i_item][7] == imodbits_none:
			item_score.append((item_set_slot, i_item, slot_item_best_modifier, imod_plain))
		else:
			for i in xrange(43):
				if items[i_item][7] >> i == 1:
					item_score.append((item_set_slot, i_item, slot_item_best_modifier, i))

		type = items[i_item][3] & 0x000000ff
		if type == itp_type_two_handed_wpn and items[i_item][3] & itp_two_handed == 0:
			item_score.append((item_set_slot, i_item, slot_item_two_hand_one_hand, 1))

		if items[i_item][3] & itp_cant_use_on_horseback == itp_cant_use_on_horseback:
			item_score.append((item_set_slot, i_item, slot_item_cant_on_horseback, 1))

		if type >= itp_type_head_armor and type <= itp_type_hand_armor:
			item_score.append((item_set_slot, i_item, slot_item_head_armor, get_head_armor(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_body_armor, get_body_armor(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_leg_armor, get_leg_armor(items[i_item][6])))
		elif (type >= itp_type_one_handed_wpn and type <= itp_type_thrown and type != itp_type_shield) or (type >= itp_type_pistol and type <= itp_type_bullets):
			item_score.append((item_set_slot, i_item, slot_item_thrust_damage, get_thrust_damage(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_swing_damage, get_swing_damage(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_speed, get_speed_rating(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_length, get_weapon_length(items[i_item][6])))
		elif type == itp_type_horse:
			item_score.append((item_set_slot, i_item, slot_item_horse_speed, get_missile_speed(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_horse_armor, get_body_armor(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_horse_charge, get_thrust_damage(items[i_item][6])))
		elif type == itp_type_shield:
			item_score.append((item_set_slot, i_item, slot_item_length, get_weapon_length(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_body_armor, get_body_armor(items[i_item][6])))
			item_score.append((item_set_slot, i_item, slot_item_speed, get_speed_rating(items[i_item][6])))

	## item_modifier
	for i_modifier in xrange(len(modifiers)):
		item_score.append((item_set_slot, i_modifier, slot_item_modifier_multiplier, modifiers[i_modifier][1]))
		item_score.append((item_set_slot, i_modifier, slot_item_modifier_quality, modifiers[i_modifier][2]))

	return item_score[:]

def keys_array():
	keys_list = []
	for key_no in xrange(len(keys)):
		keys_list.append((troop_set_slot, "trp_temp_array_a", key_no, keys[key_no]))
		keys_list.append((troop_set_slot, "trp_temp_array_b", key_no, str_key_0+key_no))
	return keys_list[:]

modifiers = [
	(imod_plain, 100, 0),
	(imod_cracked, 50, -1),
	(imod_rusty, 55, -1),
	(imod_bent, 65, -1),
	(imod_chipped, 72, -1),
	(imod_battered, 75, -1),
	(imod_poor, 80, -1),
	(imod_crude, 83, -1),
	(imod_old, 86, -1),
	(imod_cheap, 90, -1),
	(imod_fine, 190, 1),
	(imod_well_made, 250, 1),
	(imod_sharp, 160, 1),
	(imod_balanced, 350, 1),
	(imod_tempered, 670, 1),
	(imod_deadly, 850, 1),
	(imod_exquisite, 1450, 1),
	(imod_masterwork, 1750, 1),
	(imod_heavy, 190, 1),
	(imod_strong, 490, 1),
	(imod_powerful, 320, 1),
	(imod_tattered, 50, -1),
	(imod_ragged, 70, -1),
	(imod_rough, 60, -1),
	(imod_sturdy, 170, 1),
	(imod_thick, 260, 1),
	(imod_hardened, 390, 1),
	(imod_reinforced, 650, 1),
	(imod_superb, 250, 1),
	(imod_lordly, 1150, 1),
	(imod_lame, 40, -1),
	(imod_swaybacked, 60, -1),
	(imod_stubborn, 90, 1),
	(imod_timid, 180, 1),
	(imod_meek, 180, -1),
	(imod_spirited, 650, 1),
	(imod_champion, 1450, 1),
	(imod_fresh, 100, 1),
	(imod_day_old, 100, -1),
	(imod_two_day_old, 90, -1),
	(imod_smelling, 40, -1),
	(imod_rotten, 5, -1),
	(imod_large_bag, 190, 1)
]

keys = [key_0, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_a, key_b, key_c, key_d, key_e, key_f, key_g, key_h, key_i, key_j, key_k, key_l, key_m, key_n, key_o, key_p, key_q, key_r, key_s, key_t, key_u, key_v, key_w, key_x, key_y, key_z, key_numpad_0, key_numpad_1, key_numpad_2, key_numpad_3, key_numpad_4, key_numpad_5, key_numpad_6, key_numpad_7, key_numpad_8, key_numpad_9, key_num_lock, key_numpad_slash, key_numpad_multiply, key_numpad_minus, key_numpad_plus, key_numpad_enter, key_numpad_period, key_insert, key_delete, key_home, key_end, key_page_up, key_page_down, key_up, key_down, key_left, key_right, key_f1, key_f2, key_f3, key_f4, key_f5, key_f6, key_f7, key_f8, key_f9, key_f10, key_f11, key_f12, key_space, key_escape, key_enter, key_tab, key_back_space, key_open_braces, key_close_braces, key_comma, key_period, key_slash, key_back_slash, key_equals, key_minus, key_semicolon, key_apostrophe, key_tilde, key_caps_lock, key_left_shift, key_right_shift, key_left_control, key_right_control, key_left_alt, key_right_alt]
	#### Autoloot improved by rubik end

# procedures and functions are located on procedures_and_functions subdirectory.
# procedures: script that doesn't return a value (doesn't assign value to reg0..regN or s0..SN)
# namespaces
#	game_init : procedures on this namespaces will always be called by the game engine during initialisation (new game/quick battle/multiplayer)
# 	game : procedures on this namespaces will always be called by the game engine at any time (not specific)
#	quick_battle : related to quick_battle feature (UI, functionality, etc)
# 	campaign : campaign system (during overworld map)
#	campaign_simulation : AI algorithms/simulation in overworld map


# function: script that  returns a value
# namespaces
# 	game : function on this namespaces will always be called by the game engine at any time (not specific)
#	quick_battle : related to quick_battle feature (UI, functionality, etc)
#   console : console functionality (get console input)
#	economy : item price calculation 


scripts = [
	
	#script_game_start:
	# This script is called when a new game is started
	# WARNING : HEAVILY Modified by 1257AD devs
	# INPUT: none
	procedure_game_init.game_start,
	
	#script_game_get_use_string
	# This script is called from the game engine for getting using information text
	# WARNING: obscure.
	# INPUT: used_scene_prop_id
	# OUTPUT: s0
	function_game.game_get_use_string,
	
	#script_game_quick_start
	# This script is called from the game engine for initializing the global variables for tutorial, multiplayer and custom battle modes.
	# INPUT:
	# none
	# OUTPUT:
	# none
	procedure_game_init.game_quick_start,
	
	#script_get_army_size_from_slider_value
	# Usage on Quick battle window
	# INPUT: arg1 = slider_value
	# OUTPUT: reg0 = army_size
	function_quick_battle.get_army_size_from_slider_value,
	
	#script_spawn_quick_battle_army
	# Usage on Quick battle window setup
	# INPUT: arg1 = initial_entry_point, arg2 = faction_no, arg3 = infantry_ratio, arg4 = archers_ratio, arg5 = cavalry_ratio, arg6 = divide_archer_entry_points, arg7 = player_team
	# OUTPUT: none
	procedure_quick_battle.spawn_quick_battle_army,

	#script_player_arrived
	# Called in start_phase_3 game_menus.  
	# INPUT: none
	# OUTPUT: none
	procedure_campaign.player_arrived,
	
	#script_game_set_multiplayer_mission_end
	# This script is called from the game engine when a multiplayer map is ended in clients (not in server).
	# INPUT:
	# none
	# OUTPUT:
	# none
	procedure_multiplayer.game_set_multiplayer_mission_end,

	#script_game_enable_cheat_menu
	# This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
	# INPUT:
	# none
	# OUTPUT:
	# none
	procedure_game.game_enable_cheat_menu,
	
	#script_game_get_console_command
	# This script is called from the game engine when a console command is entered from the dedicated server.
	# WARNING: obscure.
	# INPUT: anything
	# OUTPUT: s0 = result text
	function_console.game_get_console_command,
	
	# script_game_event_party_encounter:
	# This script is called from the game engine whenever player party encounters another party or a battle on the world map
	# INPUT: param1: encountered_party, param2: second encountered_party (if this was a battle)
	# OUTPUT: none
	procedure_campaign.game_event_party_encounter,
	
	#script_game_event_simulate_battle:
	# This script is called whenever the game simulates the battle between two parties on the map.
	# INPUT: param1: Defender Party, param2: Attacker Party
	# OUTPUT: none
	procedure_campaign_simulation.game_event_simulate_battle,
	
	#script_game_event_battle_end:
	# This script is called whenever the game ends the battle between two parties on the map.
	# INPUT:
	# param1: Defender Party
	# param2: Attacker Party
	procedure_campaign_simulation.game_event_battle_end,
	
	#script_order_best_besieger_party_to_guard_center:
	# not really documented.
	# INPUT:
	# param1: defeated_center, param2: winner_faction
	# OUTPUT:
	# none
	procedure_campaign_ai.order_best_besieger_party_to_guard_center,
	
	#script_game_get_item_buy_price_factor:
	# This script is called from the game engine for calculating the buying price of any item.
	# INPUT:
	# param1: item_kind_id
	# OUTPUT:
	# trigger_result and reg0 = price_factor
	function_economy.game_get_item_buy_price_factor,
	
	#script_game_get_item_sell_price_factor:
	# This script is called from the game engine for calculating the selling price of any item.
	# INPUT:
	# param1: item_kind_id
	# OUTPUT:
	# trigger_result and reg0 = price_factor
	function_economy.game_get_item_sell_price_factor,
	
	# script_get_trade_penalty
	# Trade penalty if player has bad relation with the town or merchant(?)
	# Input:
	# param1: troop_id,
	# Output: reg0
	function_economy.get_trade_penalty,
	
	#script_game_event_buy_item:
	# This script is called from the game engine when player buys an item.
	# INPUT:
	# param1: item_kind_id
	procedure_economy.game_event_buy_item,
	
	#script_game_event_sell_item:
	# This script is called from the game engine when player sells an item.
	# INPUT:
	# param1: item_kind_id
	procedure_economy.game_event_sell_item,
	
	#script_start_wedding_cutscene
	# starts wedding cutscene
	# INPUT: arg1 = groom_troop, arg2 = bride_troop
	# OUTPUT: none
	procedure_wedding.start_wedding_cutscene,
	
	# script_game_get_troop_wage
	# This script is called from the game engine for calculating troop wages.
	# NOTE: This function is deprecated and not in use anymore.
	# Input:
	# param1: troop_id, param2: party-id
	# Output: reg0: weekly wage
	
	function_troop.orig_game_get_troop_wage,
	
	# script_game_get_total_wage
	# This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
	# Input: none
	# Output: reg0: weekly wage
	function_troop.game_get_total_wage,
	
	# script_game_get_join_cost
	# This script is called from the game engine for calculating troop join cost.
	# Input:
	# param1: troop_id,
	# Output: reg0: weekly wage
	function_troop.game_get_join_cost,
	
	# script_game_get_upgrade_xp
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed exp for upgrade
	function_troop.game_get_upgrade_xp,
	
	# script_game_get_upgrade_cost
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed cost for upgrade
	function_troop.game_get_upgrade_cost,
	
	# script_game_get_prisoner_price
	# This script is called from the game engine for calculating prisoner price
	# Input:
	# param1: troop_id,
	# Output: reg0
	function_troop.game_get_prisoner_price,
	
	
	# script_game_check_prisoner_can_be_sold
	# This script is called from the game engine for checking if a given troop can be sold.
	# Input:
	# param1: troop_id,
	# Output: reg0: 1= can be sold; 0= cannot be sold.
	function_troop.game_check_prisoner_can_be_sold,
	
	# script_game_get_morale_of_troops_from_faction
	# This script is called from the game engine
	# Input:
	# param1: faction_no,
	# Output: reg0: extra morale x 100
	function_troop.game_get_morale_of_troops_from_faction,

	#script_game_event_detect_party:
	# This script is called from the game engine when player party inspects another party.
	# INPUT:
	# param1: Party-id
	procedure_game.game_event_detect_party,
	
	#script_game_event_undetect_party:
	# This script is called from the game engine when player party inspects another party.
	# INPUT:
	# param1: Party-id
	procedure_game.game_event_undetect_party,
	
	#script_game_get_statistics_line:
	# This script is called from the game engine when statistics page is opened.
	# INPUT:
	# param1: line_no
	procedure_game.game_get_statistics_line,
	
	#script_game_get_date_text:
	# This script is called from the game engine when the date needs to be displayed.
	# INPUT: arg1 = number of days passed since the beginning of the game
	# OUTPUT: result string = date
	function_game.game_get_date_text,
	
	#script_game_get_money_text:
	# This script is called from the game engine when an amount of money needs to be displayed.
	# INPUT: arg1 = amount in units
	# OUTPUT: result string s1 = money in text
	function_game.game_get_money_text,
	
	#script_game_get_party_companion_limit:
	# This script is called from the game engine when the companion limit is needed for a party.
	# NOTE: modified by tom "#tom party size here!"
	# INPUT: arg1 = none
	# OUTPUT: reg0 = companion_limit
	function_game.game_get_party_companion_limit,
	
	#script_game_reset_player_party_name:
	# This script is called from the game engine when the player name is changed.
	# INPUT: none
	# OUTPUT: none
	procedure_game.game_reset_player_party_name,
		
	#script_game_get_troop_note
	# This script is called from the game engine when the notes of a troop is needed.
	# INPUT: arg1 = troop_no, arg2 = note_index
	# OUTPUT: s0 = note
	function_note.game_get_troop_note,
	
	#script_game_get_center_note
	# This script is called from the game engine when the notes of a center is needed.
	# INPUT: arg1 = center_no, arg2 = note_index
	# OUTPUT: s0 = note
	function_note.game_get_center_note,
	
	#script_game_get_faction_note
	# This script is called from the game engine when the notes of a faction is needed.
	# INPUT: arg1 = faction_no, arg2 = note_index
	# OUTPUT: s0 = note
	function_note.game_get_faction_note, 
	
	#script_game_get_quest_note
	# This script is called from the game engine when the notes of a quest is needed.
	# INPUT: arg1 = quest_no, arg2 = note_index
	# OUTPUT: s0 = note
	function_note.game_get_quest_note,
	
	#script_game_get_info_page_note
	# This script is called from the game engine when the notes of a info_page is needed.
	# INPUT: arg1 = info_page_no, arg2 = note_index
	# OUTPUT: s0 = note
	function_note.game_get_info_page_note,
	
	
	#script_game_get_scene_name
	# This script is called from the game engine when a name for the scene is needed.
	# INPUT: arg1 = scene_no
	# OUTPUT: s0 = name
	function_scene.game_get_scene_name,
	
	#script_game_get_mission_template_name
	# This script is called from the game engine when a name for the mission template is needed.
	# INPUT: arg1 = mission_template_no
	# OUTPUT: s0 = name
	function_scene.game_get_mission_template_name,
	
	#script_add_kill_death_counts
	# INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
	# OUTPUT: none
 	procedure_multiplayer.add_kill_death_counts, 

	#script_warn_player_about_auto_team_balance
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.warn_player_about_auto_team_balance,
	
	#script_check_team_balance
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.check_team_balance,
	
	#script_check_creating_ladder_dust_effect
	# INPUT: arg1 = instance_id, arg2 = remaining_time
	# OUTPUT: none
	procedure_graphicalfx.check_creating_ladder_dust_effect, 
	
	#script_money_management_after_agent_death
	# INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
	# OUTPUT: none
	procedure_multiplayer.money_management_after_agent_death,
	
	#script_raf_count_kingdom_lords_and_ladies
	# NOTE: count lords and ladies? it purposes? idk. CTRL+F'd, I think this one is deprecated
	# INPUT: kingdom id
	# OUTPUT: reg0 - lord count, reg1 - ladies count, reg3 - lords start, reg4 - ladies start
	function_AD1257.raf_count_kingdom_lords_and_ladies,

	#script_raf_initialize_aristocracy
	# NOTE: sets kings, lords, and ladies age, occupation, reputation
	#		also assigns wifes/hsubands, daughters/sons, widows
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_init.raf_initialize_aristocracy,
	
	#stub procedure
	("initialize_aristocracy",
		[
		]
	), 
		
	#script_initialize_trade_routes
	# NOTE: it's behavior is different from native script. 
	# WARNING : modified by 1257 devs
	# INPUT: none
	# OUTPUT: none		
	procedure_game_init.initialize_trade_routes,
	
	#script_initialize_faction_troop_types
	# NOTE: it's behavior is different from native script. 
	# WARNING : modified by 1257 devs
	# INPUT: none
	# OUTPUT: none	
	procedure_game_init.initialize_faction_troop_types,
	
	#script_initialize_item_info
	# NOTE: it's behavior is different from native script. 
	# WARNING : modified by 1257 devs
	# INPUT: none
	# OUTPUT: none	
	procedure_game_init.initialize_item_info,
	
	#script_initialize_town_arena_info
	# town arena initialisation
	# WARNING : modified by 1257 devs	
	# INPUT: none
	# OUTPUT: none	
	procedure_game_init.initialize_town_arena_info,
	
	#script_initialize_banner_info
	# NOTE: sets banners colour 
	# WARNING : modified by 1257 devs	
	# INPUT: none
	# OUTPUT: none	
	procedure_game_init.initialize_banner_info,
	
	
	#script_initialize_item_info
	# NOTE: it's behavior is different from native script. 
	# WARNING : modified by 1257 devs
	# INPUT: none
	# OUTPUT: none	
	procedure_game_init.initialize_economic_information,
	
	#script_initialize_all_scene_prop_slots
	# NOTE: it's behavior is different from native script. 
	# WARNING : modified by 1257 devs	
	# INPUT: none
	# OUTPUT: none
	procedure_game_init.initialize_all_scene_prop_slots,
	

	#script_initialize_scene_prop_slots
	# INPUT: arg1 = scene_prop_no
	# OUTPUT: none
	procedure_game.initialize_scene_prop_slots,
	
	#script_use_item
	# INPUT: arg1 = agent_id, arg2 = instance_id
	# OUTPUT: none
	procedure_multiplayer.use_item,
	
	#script_determine_team_flags
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.determine_team_flags,
	
	
	#script_calculate_flag_move_time
	# INPUT: arg1 = number_of_total_agents_around_flag, arg2 = dist_between_flag_and_its_pole
	# OUTPUT: reg0 = flag move time
	procedure_multiplayer.calculate_flag_move_time,
	
	#script_move_death_mode_flags_down
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.move_death_mode_flags_down,
	
	#script_move_flag
	# INPUT: arg1 = shown_flag_id, arg2 = move time in seconds, pos0 = target position
	# OUTPUT: none
	procedure_multiplayer.move_flag,
	
	#script_move_headquarters_flags
	# INPUT: arg1 = current_owner, arg2 = number_of_agents_around_flag_team_1, arg3 = number_of_agents_around_flag_team_2
	# OUTPUT: none
	procedure_multiplayer.move_headquarters_flags,
	
	#script_set_num_agents_around_flag
	# INPUT: arg1 = flag_no, arg2 = owner_code
	# OUTPUT: none
	procedure_multiplayer.set_num_agents_around_flag,
	
	#script_change_flag_owner
	# INPUT: arg1 = flag_no, arg2 = owner_code
	# OUTPUT: none
	procedure_multiplayer.change_flag_owner,
	
	#script_move_object_to_nearest_entry_point
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.move_object_to_nearest_entry_point,
	
	
	#script_multiplayer_server_on_agent_spawn_common
	# INPUT: arg1 = agent_no
	# OUTPUT: none
	procedure_multiplayer.multiplayer_server_on_agent_spawn_common ,
	
	#script_multiplayer_server_player_joined_common
	# INPUT: arg1 = player_no
	# OUTPUT: none
	procedure_multiplayer.multiplayer_server_player_joined_common,
	
	#script_multiplayer_server_before_mission_start_common
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.multiplayer_server_before_mission_start_common,
	
	#script_multiplayer_server_on_agent_killed_or_wounded_common
	# INPUT: arg1 = dead_agent_no, arg2 = killer_agent_no
	# OUTPUT: none
	procedure_multiplayer.multiplayer_server_on_agent_killed_or_wounded_common,
	
	#script_multiplayer_close_gate_if_it_is_open
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.multiplayer_close_gate_if_it_is_open,
	
	#script_multiplayer_move_moveable_objects_initial_positions
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.multiplayer_move_moveable_objects_initial_positions ,
	
	#script_move_belfries_to_their_first_entry_point
	# siege engine movemenet in single player
	# WHY THE FUCK DO THEY MIX MP SCRIPTS WITH SP FUCKING TALEWORLDS PIECE OF SHIT
	# INPUT: none
	# OUTPUT: none
	procedure_belfry.move_belfries_to_their_first_entry_point,
	
	#script_team_set_score
	# INPUT: arg1 = team_no, arg2 = score
	# OUTPUT: none
	procedure_multiplayer.team_set_score,
	
	#script_player_set_score
	# INPUT: arg1 = player_no, arg2 = score
	# OUTPUT: none
	procedure_multiplayer.player_set_score,
	
	#script_player_set_kill_count
	# INPUT: arg1 = player_no, arg2 = score
	# OUTPUT: none
	procedure_multiplayer.player_set_kill_count,
	
	#script_player_set_death_count
	# INPUT: arg1 = player_no, arg2 = score
	# OUTPUT: none
	procedure_multiplayer.player_set_death_count,
	
	#script_set_attached_scene_prop
	# INPUT: arg1 = agent_id, arg2 = flag_id
	# OUTPUT: none
	procedure_multiplayer.set_attached_scene_prop,
	
	#script_set_team_flag_situation
	# INPUT: arg1 = team_no, arg2 = score
	# OUTPUT: none
	procedure_multiplayer.set_team_flag_situation,
	
	#script_start_death_mode
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.start_death_mode,
	
	#script_calculate_new_death_waiting_time_at_death_mod
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.calculate_new_death_waiting_time_at_death_mod,
	
	#script_calculate_number_of_targets_destroyed
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer.calculate_number_of_targets_destroyed,
	
	#script_initialize_objects
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer_init.initialize_objects,
	
	#script_initialize_objects_clients
	# INPUT: none
	# OUTPUT: none
	procedure_multiplayer_init.initialize_objects_clients,

	#script_show_multiplayer_message
	# INPUT: arg1 = multiplayer_message_type
	# OUTPUT: none
	procedure_multiplayer.show_multiplayer_message,
	
	#script_get_headquarters_scores
	# INPUT: none
	# OUTPUT: reg0 = team_1_num_flags, reg1 = team_2_num_flags
	procedure_multiplayer.get_headquarters_scores,
	
	#script_draw_this_round
	# INPUT: arg1 = value
	#procedure_multiplayer.draw_this_round,
	##########WARNING For some reason I can't seperate this from main scirpt. It alywas thrown an error durig a compile
	##########WARNING Maybe it's hardcoded?
	("draw_this_round",
	   [
	    (store_script_param, ":value", 1),
	    (try_begin),
	      (eq, ":value", -9), #destroy mod round end
	      (assign, "$g_round_ended", 1),
	      (store_mission_timer_a, "$g_round_finish_time"),
	      #(assign, "$g_multiplayer_message_value_1", -1),
	      #(assign, "$g_multiplayer_message_type", multiplayer_message_type_round_draw),
	      #(start_presentation, "prsnt_multiplayer_message_1"),
	    (else_try),
	      (eq, ":value", -1), #draw
	      (assign, "$g_round_ended", 1),
	      (store_mission_timer_a, "$g_round_finish_time"),
	      (assign, "$g_multiplayer_message_value_1", -1),
	      (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_draw),
	      (start_presentation, "prsnt_multiplayer_message_1"),
	    (else_try), 
	      (eq, ":value", 0), #defender wins
	      #THIS_IS_OUR_LAND achievement
	      (try_begin),
	        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
	        (multiplayer_get_my_player, ":my_player_no"),
	        (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
	        (player_get_agent_id, ":my_player_agent", ":my_player_no"),
	        (ge, ":my_player_agent", 0),
	        (agent_is_alive, ":my_player_agent"),
	        (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
	        (eq, ":my_player_agent_team_no", 0), #defender
	        (unlock_achievement, ACHIEVEMENT_THIS_IS_OUR_LAND),
	      (try_end),
	      #THIS_IS_OUR_LAND achievement end
	      (assign, "$g_round_ended", 1),
	      (store_mission_timer_a, "$g_round_finish_time"),
	        
	      (team_get_faction, ":faction_of_winner_team", 0),
	      (team_get_score, ":team_1_score", 0),
	      (val_add, ":team_1_score", 1),
	      (team_set_score, 0, ":team_1_score"),
	      (assign, "$g_winner_team", 0),
	      (str_store_faction_name, s1, ":faction_of_winner_team"),

	      (assign, "$g_multiplayer_message_value_1", ":value"),
	      (try_begin),
	        (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),    
	        (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
	        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_siege_mode),
	      (else_try),
	        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
	      (try_end),
	      (start_presentation, "prsnt_multiplayer_message_1"),
	    (else_try), 
	      (eq, ":value", 1), #attacker wins
	      (assign, "$g_round_ended", 1),
	      (store_mission_timer_a, "$g_round_finish_time"),
	  
	      (team_get_faction, ":faction_of_winner_team", 1),
	      (team_get_score, ":team_2_score", 1),
	      (val_add, ":team_2_score", 1),
	      (team_set_score, 1, ":team_2_score"),
	      (assign, "$g_winner_team", 1),
	      (str_store_faction_name, s1, ":faction_of_winner_team"),

	      (assign, "$g_multiplayer_message_value_1", ":value"),
	      (try_begin),
	        (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),    
	        (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
	        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_siege_mode),
	      (else_try),
	        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
	      (try_end),
	      (start_presentation, "prsnt_multiplayer_message_1"),
	    (try_end),
	    #LAST_MAN_STANDING achievement
	    (try_begin),
	      (is_between, ":value", 0, 2), #defender or attacker wins
	      (try_begin),
	        (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
	        (multiplayer_get_my_player, ":my_player_no"),
	        (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
	        (player_get_agent_id, ":my_player_agent", ":my_player_no"),
	        (ge, ":my_player_agent", 0),
	        (agent_is_alive, ":my_player_agent"),
	        (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
	        (eq, ":my_player_agent_team_no", ":value"), #winner team
	        (unlock_achievement, ACHIEVEMENT_LAST_MAN_STANDING),
	      (try_end),
	    (try_end),
	    #LAST_MAN_STANDING achievement end
	    ]),   
	###################################
	###################################

	#script_check_achievement_last_man_standing
	#INPUT: arg1 = value
	procedure_multiplayer.check_achievement_last_man_standing,
	
	#script_find_most_suitable_bot_to_control
	# INPUT: arg1 = value
	procedure_multiplayer.find_most_suitable_bot_to_control,

	#script_game_receive_url_response
	#response format should be like this:
	#  [a number or a string]|[another number or a string]|[yet another number or a string] ...
	# here is an example response:
	# 12|Player|100|another string|142|323542|34454|yet another string
	# NOTE: it is disabled by default.
	# INPUT: arg1 = num_integers, arg2 = num_strings
	# reg0, reg1, reg2, ... up to 128 registers contain the integer values
	# s0, s1, s2, ... up to 128 strings contain the string values
	procedure_multiplayer.game_receive_url_response,

	#script_game_get_cheat_mode
	# WARNING: no documentation. perhaps it is used by the game engine
	# INPUT: none
	# OUTPUT: none
	procedure_game.game_get_cheat_mode,

	#script_game_receive_network_message
	# This script is called from the game engine when a new network message is received.
	# INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
	procedure_multiplayer.game_receive_network_message,
		
	# script_cf_multiplayer_evaluate_poll
	# Input: none
	# Output: none (can fail)
	cfunction_multiplayer.cf_multiplayer_evaluate_poll,
		
	# script_multiplayer_accept_duel
	# Input: arg1 = agent_no, arg2 = agent_no_offerer
	# Output: none
	procedure_multiplayer.multiplayer_accept_duel ,
		
	# script_game_get_multiplayer_server_option_for_mission_template
	# Input: arg1 = mission_template_id, arg2 = option_index
	# Output: trigger_result = 1 for option available, 0 for not available
	#         reg0 = option_value
	function_multiplayer.game_get_multiplayer_server_option_for_mission_template,
	
	# script_game_multiplayer_server_option_for_mission_template_to_string
	# Input: arg1 = mission_template_id, arg2 = option_index, arg3 = option_value
	# Output: s0 = option_text
	function_multiplayer.game_multiplayer_server_option_for_mission_template_to_string,
	
	# script_cf_multiplayer_team_is_available
	# Input: arg1 = player_no, arg2 = team_no
	# Output: none, true or false
	cfunction_multiplayer.cf_multiplayer_team_is_available,
	
	# script_find_number_of_agents_constant
	# Input: none
	# Output: reg0 = 100xconstant (100..500)
	function_multiplayer.find_number_of_agents_constant,
	
	# script_game_multiplayer_event_duel_offered
	# Input: arg1 = agent_no
	# Output: none
	procedure_multiplayer.game_multiplayer_event_duel_offered,
	
	# script_game_get_multiplayer_game_type_enum
	# Input: none
	# Output: reg0:first type, reg1:type count
	function_multiplayer.game_get_multiplayer_game_type_enum,
	
	# script_game_multiplayer_get_game_type_mission_template
	# Input: arg1 = game_type
	# Output: mission_template
	function_multiplayer.game_multiplayer_get_game_type_mission_template,
	
	# script_multiplayer_get_mission_template_game_type
	# Input: arg1 = mission_template_no
	# Output: game_type
	function_multiplayer.multiplayer_get_mission_template_game_type,
	
	
	# script_multiplayer_fill_available_factions_combo_button
	# Input: arg1 = overlay_id, arg2 = selected_faction_no, arg3 = opposite_team_selected_faction_no
	# Output: none
	procedure_multiplayer.multiplayer_fill_available_factions_combo_button,
	
	
	# script_multiplayer_get_troop_class
	# Input: arg1 = troop_no
	# Output: reg0: troop_class
	function_multiplayer.multiplayer_get_troop_class,
	
	#script_multiplayer_clear_player_selected_items
	# Input: arg1 = player_no
	# Output: none
	procedure_multiplayer.multiplayer_clear_player_selected_items,
	
	
	#script_multiplayer_init_player_slots
	# Input: arg1 = player_no
	# Output: none
	procedure_multiplayer_init.multiplayer_init_player_slots,
	
	#script_multiplayer_initialize_belfry_wheel_rotations
	# Input: none
	# Output: none
	procedure_multiplayer_init.multiplayer_initialize_belfry_wheel_rotations,
	
	#script_send_open_close_information_of_object
	# Input: arg1 = mission_object_id
	# Output: none
	procedure_multiplayer.send_open_close_information_of_object,
	
	#script_multiplayer_send_initial_information
	# Input: arg1 = player_no
	# Output: none
	procedure_multiplayer.multiplayer_send_initial_information,
	
	#script_multiplayer_remove_headquarters_flags
	# Input: none
	# Output: none
	procedure_multiplayer.multiplayer_remove_headquarters_flags,
	
	#script_multiplayer_remove_destroy_mod_targets
	# Input: none
	# Output: none
	procedure_multiplayer.multiplayer_remove_destroy_mod_targets,
	
	#script_multiplayer_init_mission_variables
	procedure_multiplayer.multiplayer_init_mission_variables,
	
	#script_multiplayer_event_mission_end
	# Input: none
	# Output: none
	procedure_multiplayer.multiplayer_event_mission_end,
	
	
	#script_multiplayer_event_agent_killed_or_wounded
	# Input: arg1 = dead_agent_no, arg2 = killer_agent_no
	# Output: none
	procedure_multiplayer.multiplayer_event_agent_killed_or_wounded,
	
	#script_multiplayer_get_item_value_for_troop
	# Input: arg1 = item_no, arg2 = troop_no
	# Output: reg0: item_value
	function_multiplayer.multiplayer_get_item_value_for_troop,
	
	#script_multiplayer_get_previous_item_for_item_and_troop
	# Input: arg1 = item_no, arg2 = troop_no
	# Output: reg0: previous_item_no (-1 if it is the root item, 0 if the item is invalid)
	function_multiplayer.multiplayer_get_previous_item_for_item_and_troop,
	
	#script_cf_multiplayer_is_item_default_for_troop
	# Input: arg1 = item_no, arg2 = troop_no
	# Output: reg0: total_cost
	cfunction_multiplayer.cf_multiplayer_is_item_default_for_troop,
	
	#script_multiplayer_calculate_cur_selected_items_cost
	# Input: arg1 = player_no
	# Output: reg0: total_cost
	function_multiplayer.multiplayer_calculate_cur_selected_items_cost,
	
	#script_multiplayer_set_item_available_for_troop
	# Input: arg1 = item_no, arg2 = troop_no
	# Output: none
	procedure_multiplayer.multiplayer_set_item_available_for_troop,
	
	#script_multiplayer_send_item_selections
	# Input: none
	# Output: none
	procedure_multiplayer.multiplayer_send_item_selections,
	
	#script_multiplayer_set_default_item_selections_for_troop
	# Input: arg1 = troop_no
	# Output: none
	procedure_multiplayer.multiplayer_set_default_item_selections_for_troop,
	
	#script_multiplayer_display_available_items_for_troop_and_item_classes
	# Input: arg1 = troop_no, arg2 = item_classes_begin, arg3 = item_classes_end, arg4 = pos_x_begin, arg5 = pos_y_begin
	# Output: none
	procedure_multiplayer.multiplayer_display_available_items_for_troop_and_item_classes,
	
	# script_multiplayer_fill_map_game_types
	# Input: game_type
	# Output: num_maps
	function_multiplayer.multiplayer_fill_map_game_types,
	
	
	# script_multiplayer_count_players_bots
	# Input: none
	# Output: none
	procedure_multiplayer.multiplayer_count_players_bots,
	
	# script_multiplayer_find_player_leader_for_bot
	# Input: arg1 = team_no
	# Output: reg0 = player_no
	function_multiplayer.multiplayer_find_player_leader_for_bot,
	
	# script_multiplayer_find_bot_troop_and_group_for_spawn
	# Input: arg1 = team_no
	# Output: reg0 = troop_id, reg1 = group_id
	function_multiplayer.multiplayer_find_bot_troop_and_group_for_spawn,
	
	# script_multiplayer_change_leader_of_bot
	# Input: arg1 = agent_no
	# Output: none
	procedure_multiplayer.multiplayer_change_leader_of_bot,
	
	# script_multiplayer_find_spawn_point
	# Input: arg1 = team_no, arg2 = examine_all_spawn_points, arg3 = is_horseman
	# Output: none
	procedure_multiplayer.multiplayer_find_spawn_point,
	
	# script_multiplayer_find_spawn_point_2
	# Input: arg1 = team_no, arg2 = examine_all_spawn_points, arg3 = is_horseman
	# Output: reg0 = entry_point_no
	function_multiplayer.multiplayer_find_spawn_point_2,
	
	#script_multiplayer_buy_agent_equipment
	# Input: arg1 = player_no
	# Output: none
	procedure_multiplayer.multiplayer_buy_agent_equipment,
		
	###ENOUGH OF MP BULLSHIT!

		# script_party_get_ideal_size @used for NPC parties.
		# party AI size limit
		# WARNING: modified by 1257AD devs
		# Input: arg1 = party_no
		# Output: reg0: ideal size
		function_party.party_get_ideal_size,
		
		
		#script_game_get_party_prisoner_limit:
		# This script is called from the game engine when the prisoner limit is needed for a party.
		# WARNING : modified by 1257AD devs, arg1 used to be arg1 = party_no
		# INPUT: none
		# OUTPUT: reg0 = prisoner_limit
		function_party.game_get_party_prisoner_limit,
		
		#script_game_get_item_extra_text:
		# This script is called from the game engine when an item's properties are displayed.
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = item_no, arg2 = extra_text_id (this can be between 0-7 (7 included)), arg3 = item_modifier
		# OUTPUT: result_string = item extra text, trigger_result = text color (0 for default)
		function_item.game_get_item_extra_text,
		

		###SPECIAL
		#script_game_on_disembark:
		# This script is called from the game engine when the player reaches the shore with a ship.
		# INPUT: pos0 = disembark position
		# OUTPUT: none
		procedure_game.game_on_disembark,
		
		###SPECIAL
		#script_game_context_menu_get_buttons:
		# This script is called from the game engine when the player clicks the right mouse button over a party on the map.
		# INPUT: arg1 = party_no
		# OUTPUT: none, fills the menu buttons
		procedure_user_interface.game_context_menu_get_buttons,
		
		#script_game_event_context_menu_button_clicked:
		# This script is called from the game engine when the player clicks on a button at the right mouse menu.
		# INPUT: arg1 = party_no, arg2 = button_value
		# OUTPUT: none
		procedure_user_interface.game_event_context_menu_button_clicked,
		
		#script_game_get_skill_modifier_for_troop
		# This script is called from the game engine when a skill's modifiers are needed
		# INPUT: arg1 = troop_no, arg2 = skill_no
		# OUTPUT: trigger_result = modifier_value
		function_troop.game_get_skill_modifier_for_troop,
		
		# Note to modders: Uncomment these if you'd like to use the following.
		
		##  #script_game_check_party_sees_party
		##  # This script is called from the game engine when a party is inside the range of another party
		##  # INPUT: arg1 = party_no_seer, arg2 = party_no_seen
		##  # OUTPUT: trigger_result = true or false (1 = true, 0 = false)
		##  ("game_check_party_sees_party",
		##   [
		##     (store_script_param, ":party_no_seer", 1),
		##     (store_script_param, ":party_no_seen", 2),
		##     (set_trigger_result, 1),
		##    ]),

		#script_game_get_party_speed_multiplier
		# This script is called from the game engine when a skill's modifiers are needed
		# INPUT: arg1 = party_no
		# OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
		function_party.game_get_party_speed_multiplier,
		
		
		# script_npc_get_troop_wage
		# This script is called from module system to calculate troop wages for npc parties.
		# Input:
		# param1: troop_id
		# Output: reg0: weekly wage
		
		function_troop.npc_get_troop_wage,
		
		#script_setup_talk_info
		# INPUT: $g_talk_troop, $g_talk_troop_relation
		procedure_troop.setup_talk_info,
		
		#NPC companion changes begin
		#script_setup_talk_info_companions
		procedure_troop.setup_talk_info_companions,
		#NPC companion changes end
		
		#script_update_party_creation_random_limits
		# INPUT: none
		function_party.update_party_creation_random_limits,
		
		#script_set_trade_route_between_centers
		# INPUT:
		# param1: center_no_1
		# param1: center_no_2
		procedure_economy.set_trade_route_between_centers,
		
		# script_average_trade_good_prices
		# Called from start
		# INPUT: none
		# OUTPUT: none
		
		procedure_economy.average_trade_good_prices,
		
		# script_average_trade_good_prices_2
		# Called from start
		# INPUT: none
		# OUTPUT: none
		procedure_economy.average_trade_good_prices_2,
		
		
		
		#script_average_trade_good_productions
		# INPUT: none (called only from game start?)
		#This is currently deprecated, as I was going to try to fine-tune production
		procedure_economy.average_trade_good_productions,
		
		#script_normalize_trade_good_productions
		#Adjusts productions according to the amount of the item produced
		# INPUT: none
		# This currently deprecated, as I was going to try to fine-tune productions
		procedure_economy.normalize_trade_good_productions,
		
		#script_update_trade_good_prices
		# INPUT: none
		procedure_economy.update_trade_good_prices,
		
		#script_update_trade_good_price_for_party
		# INPUT: arg1 = party_no
		#Called once every 72 hours
		procedure_economy.update_trade_good_price_for_party,
		
		#script_center_get_production
		# WARNING: no longer behaves like native, modified by 1257AD devs
		# INPUT: arg1 = town center, arg2 = goods
		# OUTPUT: reg0 = prosperity, reg1 = base_production_modded_by_raw_materials, reg2 = base_production
		function_economy.center_get_production,
		
		# script_center_get_consumption
		# economy stuff I guess
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = town center, arg2 = current good
		# OUTPUT:  reg0 = modified consumption, reg1 = raw material consumption, reg2 = consumer consumption
		function_economy.center_get_consumption,
		
		#script_get_enterprise_name
		# INPUT: arg1 = item_no
		# Output: reg0: production string
		function_economy.get_enterprise_name,
		
		#script_do_merchant_town_trade
		# INPUT: arg1 = party_no (of the merchant), arg2 = center_no
		procedure_economy.do_merchant_town_trade,
		
		#script_party_calculate_regular_strength:
		# INPUT:
		# param1: Party-id
		procedure_party.party_calculate_regular_strength,
		
		
		
		
		#script_party_calculate_strength:
		# INPUT: arg1 = party_id, arg2 = exclude leader
		# OUTPUT: reg0 = strength
	
		function_party.party_calculate_strength,
		
		
		#script_loot_player_items:
		# INPUT: arg1 = enemy_party_no
		# Output: none
		procedure_party.loot_player_items,
		
		
		#script_party_calculate_loot:
		# INPUT:
		# param1: Party-id
		# OUTPUT: Returns num looted items in reg(0)
		function_party.party_calculate_loot,
		
		#script_calculate_main_party_shares:
		# INPUT:
		# Returns number of player party shares in reg0
		function_party.calculate_main_party_shares,
		
		#script_party_give_xp_and_gold:
		# INPUT:
		# param1: destroyed Party-id
		# calculates and gives player paty's share of gold and xp.
		
		procedure_party.party_give_xp_and_gold,
		
		
		#script_setup_troop_meeting:
		# INPUT:
		# param1: troop_id with which meeting will be made.
		# param2: troop_dna (optional)
		
		procedure_troop.setup_troop_meeting,
		
		#script_setup_party_meeting:
		# INPUT:
		# param1: Party-id with which meeting will be made.
		
		procedure_party.setup_party_meeting,
		
		#script_get_meeting_scene:
		# INPUT: none
		# OUTPUT: reg0 contain suitable scene_no
		
		function_scene.get_meeting_scene,

		#script_party_remove_all_companions:
		# INPUT:
		# param1: Party-id from which  companions will be removed.
		# "$g_move_heroes" : controls if heroes will also be removed.
		procedure_party.party_remove_all_companions,
		
		#script_party_remove_all_prisoners:
		# INPUT:
		# param1: Party-id from which  prisoners will be removed.
		# "$g_move_heroes" : controls if heroes will also be removed.
		
		procedure_party.party_remove_all_prisoners,
		
		#script_party_add_party_companions:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
		procedure_party.party_add_party_companions,
		
		#script_party_add_party_prisoners:
		# INPUT:
		# param1: Party-id to add the second party
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
		procedure_party.party_add_party_prisoners,
		
		#script_party_prisoners_add_party_companions:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
		procedure_party.party_prisoners_add_party_companions,
		
		#script_party_prisoners_add_party_prisoners:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
		procedure_party.party_prisoners_add_party_prisoners,
		
		# script_party_add_party:
		# INPUT:
		# param1: Party-id to add the second part
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
		procedure_party.party_add_party,
		
		
		#script_party_copy:
		# INPUT:
		# param1: Party-id to copy the second party
		# param2: Party-id which will be copied to the first one.
		
		procedure_party.party_copy,
		
		
		#script_clear_party_group:
		# INPUT:
		# param1: Party-id of the root of the group.
		# This script will clear the root party and all parties attached to it recursively.
		
		procedure_party.clear_party_group,
		
		
		#script_party_add_wounded_members_as_prisoners:
		# INPUT:
		# param1: Party-id to add the second party
		# param2: Party-id which will be added to the first one.
		# "$g_move_heroes" : controls if heroes will also be added.
		
		procedure_party.party_add_wounded_members_as_prisoners,
		
		
		#script_get_nonempty_party_in_group:
		# INPUT:
		# param1: Party-id of the root of the group.
		# OUTPUT: reg0: nonempy party-id
		
		function_party.get_nonempty_party_in_group,
		
		#script_collect_prisoners_from_empty_parties:
		# INPUT:
		# param1: Party-id of the root of the group.
		# param2: Party to collect prisoners in.
		# make sure collection party is cleared before calling this.
		
		procedure_party.collect_prisoners_from_empty_parties,
		
		#script_change_party_morale:
		# INPUT: party_no, morale_gained
		# OUTPUT: none
		
		procedure_party.change_party_morale,
		
		#script_count_casualties_and_adjust_morale:
		# INPUT: none
		# OUTPUT: none
		
		procedure_party.count_casualties_and_adjust_morale,
		
		#script_print_casualties_to_s0:
		# INPUT:
		# param1: Party_id, param2: 0 = use new line, 1 = use comma
		
		#OUTPUT:
		# string register 0.
		
		function_party.print_casualties_to_s0,
		
		#script_write_fit_party_members_to_stack_selection
		# INPUT:
		# param1: party_no, exclude_leader
		#OUTPUT:
		# trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
		# trp_stack_selection_ids slots (2..n = stack troops)
		function_party.write_fit_party_members_to_stack_selection,
		
		#script_remove_fit_party_member_from_stack_selection
		# INPUT:
		# param1: slot_index
		#OUTPUT:
		# reg0 = troop_no
		# trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
		# trp_stack_selection_ids slots (2..n = stack troops)
		function_party.remove_fit_party_member_from_stack_selection,
		
		#script_remove_random_fit_party_member_from_stack_selection
		# INPUT:
		# none
		#OUTPUT:
		# reg0 = troop_no
		# trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
		# trp_stack_selection_ids slots (2..n = stack troops)
		function_party.remove_random_fit_party_member_from_stack_selection,
		
		
		#script_add_routed_party
		#INPUT: none
		#OUTPUT: none
		procedure_party.add_routed_party, #ozan
		
		
		#script_cf_training_ground_sub_routine_1_for_melee_details
		# INPUT:
		# value
		#OUTPUT:
		# none
		cfunction_training.cf_training_ground_sub_routine_1_for_melee_details,
		
		#script_training_ground_sub_routine_2_for_melee_details
		# INPUT:
		# value
		#OUTPUT:
		# none
		procedure_training.training_ground_sub_routine_2_for_melee_details,
		
		#script_cf_training_ground_sub_routine_for_training_result
		# INPUT:
		# arg1: troop_id, arg2: stack_no, arg3: troop_count, arg4: xp_ratio_to_add
		#OUTPUT:
		# none
		cfunction_training.cf_training_ground_sub_routine_for_training_result,
		
		
		#script_print_troop_owned_centers_in_numbers_to_s0
		# INPUT:
		# param1: troop_no
		#OUTPUT:
		# string register 0.
		function_troop.print_troop_owned_centers_in_numbers_to_s0,
		
		#script_get_random_melee_training_weapon
		# INPUT: none
		# OUTPUT: reg0 = weapon_1, reg1 = weapon_2
		function_training.get_random_melee_training_weapon,
		
		#script_start_training_at_training_ground
		# INPUT:
		# param1: training_weapon_type, param2: training_param
		procedure_training.start_training_at_training_ground,
		
		
		#script_print_party_to_s0:
		# INPUT:
		# param1: Party-id
		
		#OUTPUT:
		# string register 0.
		
		##  ("print_party_to_s0",
		##    [
		##      (store_script_param_1, ":party"), #Party_id
		##      (party_get_num_companion_stacks, ":num_stacks",":party"),
		##      (str_store_string, s50, "str_none"),
		##      (try_for_range, ":i_stack", 0, ":num_stacks"),
		##        (party_stack_get_troop_id,     ":stack_troop",":party",":i_stack"),
		##        (party_stack_get_size,         ":stack_size",":party",":i_stack"),
		##        (str_store_troop_name_by_count, s61, ":stack_troop", ":stack_size"),
		##        (try_begin),
		##          (troop_is_hero, ":stack_troop"),
		##          (str_store_string_reg, s51, s61),
		##        (else_try),
		##          (assign, reg60, ":stack_size"),
		##          (str_store_string, s63, "str_reg60_s61"),
		##        (try_end),
		##        (try_begin),
		##          (eq, ":i_stack", 0),
		##          (str_store_string_reg, s50, s51),
		##        (else_try),
		##          (str_store_string, s50, "str_s50_comma_s51"),
		##        (try_end),
		##      (try_end),
		##      (str_store_string_reg, s0, s50),
		##  ]),
		
		
		
		#script_party_count_fit_regulars:
		# Returns the number of unwounded regular companions in a party
		# INPUT:
		# param1: Party-id
		
		function_party.party_count_fit_regulars,
		
		
		#script_party_count_fit_for_battle:
		# Returns the number of unwounded companions in a party
		# INPUT:
		# param1: Party-id
		# OUTPUT: reg0 = result
		function_party.party_count_fit_for_battle,
		
		
		#script_party_count_members_with_full_health
		# Returns the number of unwounded regulars, and heroes other than player with 100% hitpoints in a party
		# INPUT:
		# param1: Party-id
		# OUTPUT: reg0 = result
		function_party.party_count_members_with_full_health,
		
		
		#script_get_stack_with_rank:
		# Returns the stack no, containing unwounded regular companions with rank rank.
		# INPUT:
		# param1: Party-id
		# param2: rank
		
		function_party.get_stack_with_rank,
		
		#script_inflict_casualties_to_party:
		# INPUT:
		# param1: Party-id
		# param2: number of rounds
		
		#OUTPUT:
		# This script doesn't return a value but populates the parties p_temp_wounded and p_temp_killed with the wounded and killed.
		#Example:
		#  (script_inflict_casualties_to_party, "_p_main_party" ,50),
		#  Simulate 50 rounds of casualties to main_party.
		
		procedure_party.inflict_casualties_to_party,
		
		
		#script_move_members_with_ratio:
		# INPUT:
		# param1: Source Party-id
		# param2: Target Party-id
		# pin_number = ratio of members to move, multiplied by 1000
		
		#OUTPUT:
		# This script doesn't return a value but moves some of the members of source party to target party according to the given ratio.
		procedure_party.move_members_with_ratio,
		
		# script_count_parties_of_faction_and_party_type:
		# counts number of active parties with a template and faction.
		# Input: arg1 = faction_no, arg2 = party_type
		# Output: reg0 = count
		
		function_faction.count_parties_of_faction_and_party_type,
		
		# script_faction_get_number_of_armies
		# Input: arg1 = faction_no
		# Output: reg0 = number_of_armies
		function_faction.faction_get_number_of_armies,
		
		
		# script_faction_recalculate_strength
		# Input: arg1 = faction_no
		# Output: reg0 = strength
		function_faction.faction_recalculate_strength,
		
		#script_cf_select_random_town_with_faction:
		# This script selects a random town in range [towns_begin, towns_end)
		# such that faction of the town is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no
		cfunction_faction.cf_select_random_town_with_faction,
		
		#script_cf_select_random_village_with_faction:
		# This script selects a random village in range [villages_begin, villages_end)
		# such that faction of the village is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching village.
		# reg0 = village_no
		cfunction_faction.cf_select_random_village_with_faction,
		
		
		#script_cf_select_random_walled_center_with_faction:
		# This script selects a random center in range [centers_begin, centers_end)
		# such that faction of the town is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		# arg2 = preferred_center_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no (Can fail)
		cfunction_faction.cf_select_random_walled_center_with_faction,
		
		

	#script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege:
	# INPUT:
	# arg1 = faction_no
	# arg2 = owner_troop_no
	#OUTPUT:
	# This script may return false if there is no matching town.
	# reg0 = center_no (Can fail)
	cfunction_faction.cf_select_random_walled_center_with_faction_and_owner_priority_no_siege,
		
		
		#script_cf_select_random_walled_center_with_faction_and_less_strength_priority:
		# This script selects a random center in range [centers_begin, centers_end)
		# such that faction of the town is equal to given_faction
		# INPUT:
		# arg1 = faction_no
		# arg2 = preferred_center_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no (Can fail)
		cfunction_faction.cf_select_random_walled_center_with_faction_and_less_strength_priority,
		
		
		#script_cf_select_random_town_at_peace_with_faction:
		# This script selects a random town in range [towns_begin, towns_end)
		# such that faction of the town is friendly to given_faction
		# INPUT:
		# arg1 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no
		cfunction_faction.cf_select_random_town_at_peace_with_faction,
		
		#script_cf_select_random_town_at_peace_with_faction_in_trade_route
		# INPUT:
		# arg1 = town_no
		# arg2 = faction_no
		
		#OUTPUT:
		# This script may return false if there is no matching town.
		# reg0 = town_no
		cfunction_faction.cf_select_random_town_at_peace_with_faction_in_trade_route,
		
		
		#script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route
		#the following is a very simple adjustment - it measures the difference in prices between two towns
		#all goods are weighted equally except for luxuries
		#it does not take into account the prices of the goods, nor cargo capacity
		#to do that properly, a merchant would have to virtually fill his baggage, slot by slot, for each town
		#i also found that one needed to introduce demand inelasticity -- prices should vary a lot for grain,  relatively little for iron
		# INPUT: arg1 = town_no, arg2 = faction_no
		# OUTPUT: reg0 = most profitable town
		cfunction_faction.cf_select_most_profitable_town_at_peace_with_faction_in_trade_route,
		
		# script_shuffle_troop_slots:
		# Shuffles a range of slots of a given troop.
		# Used for exploiting a troop as an array.
		# Input: arg1 = troop_no, arg2 = slot_begin, arg3 = slot_end
		procedure_array.shuffle_troop_slots,
		
		
		# script_get_quest  
		# combines old get_random_quest with new get_dynamic_quest
		# Input: arg1 = troop_no (of the troop in conversation), arg2 = min_importance (of the quest)
		# Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
		function_quest.get_quest,

		# script_get_dynamic_quest
		# combines old get_random_quest with new get_dynamic_quest
		# Input: arg1 = troop_no (of the troop in conversation)
		# Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
		#		 reg1 = relevant troop
		#		 reg2 = relevant party
		#		 reg3 = relevant faction
		function_quest.get_dynamic_quest,
		
		# script_get_political_quest- combines old get_random_quest with new get_dynamic_quest
		# Political quests are given by the player's political "coach" -- ie, a spouse or the minister -- to improve standing in the faction
		# Input: arg1 = troop_no (of the troop in conversation)
		# Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
		#		 reg1 = quest_target_troop
		#		 reg2 = quest_object_troop
		function_quest.get_political_quest,
		
		# script_npc_find_quest_for_player_to_s11
		# Input: arg1 = faction_no
		# Output: reg0 = quest_giver_found
		function_quest.npc_find_quest_for_player_to_s11,
		
		
		
		# script_cf_get_random_enemy_center_within_range
		# Input: arg1 = party_no, arg2 = range (in kms)
		# Output: reg0 = center_no
		function_party.cf_get_random_enemy_center_within_range,
		
		# script_cf_faction_get_random_enemy_faction
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (Can fail)
		function_faction.cf_faction_get_random_enemy_faction,
		
		# script_cf_faction_get_random_friendly_faction
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (Can fail)
		function_faction.cf_faction_get_random_friendly_faction,
		
		# script_cf_troop_get_random_enemy_troop_with_occupation
		# Input: arg1 = troop_no,
		# Output: reg0 = enemy_troop_no (Can fail)
		function_troop.cf_troop_get_random_enemy_troop_with_occupation,
		
		
		# script_cf_get_random_lord_in_a_center_with_faction
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
		function_faction.cf_get_random_lord_in_a_center_with_faction,
		
		# script_cf_get_random_lord_except_king_with_faction
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
		function_faction.cf_get_random_lord_except_king_with_faction,
		
		
		# script_cf_get_random_lord_from_another_faction_in_a_center
		# Input: arg1 = faction_no
		# Output: reg0 = troop_no, Can Fail!
		function_faction.cf_get_random_lord_from_another_faction_in_a_center,
		
		# script_get_closest_walled_center
		# Input: arg1 = party_no
		# Output: reg0 = center_no (closest)
		function_party.get_closest_walled_center,
		
		# script_get_closest_center
		# Input: arg1 = party_no
		# Output: reg0 = center_no (closest)
		function_party.get_closest_center,
		
		
		# script_get_closest_center_of_faction
		# Input: arg1 = party_no, arg2 = kingdom_no
		# Output: reg0 = center_no (closest)
		function_party.get_closest_center_of_faction,
		
		# script_get_closest_walled_center_of_faction
		# Input: arg1 = party_no, arg2 = kingdom_no
		# Output: reg0 = center_no (closest)
		function_party.get_closest_walled_center_of_faction,
		
		# script_let_nearby_parties_join_current_battle
		# no longer behaves like native
		# WARNING : modified by 1257AD devs
		# Input: arg1 = besiege_mode, arg2 = dont_add_friends_other_than_accompanying
		# Output: none
		procedure_party.let_nearby_parties_join_current_battle,
		
		# script_party_wound_all_members_aux
		# Input: arg1 = party_no
		procedure_party.party_wound_all_members_aux,
		
		# script_party_wound_all_members
		# Input: arg1 = party_no
		procedure_party.party_wound_all_members,
		
		
		
		# script_calculate_battle_advantage
		# Output: reg0 = battle advantage
		function_party.calculate_battle_advantage,
		
		
		# script_cf_check_enemies_nearby
		# Input: none
		# Output: none, fails when enemies are nearby
		cfunction_battle.cf_check_enemies_nearby,
		
		# script_get_heroes_attached_to_center_aux
		# For internal use only
		procedure_town.get_heroes_attached_to_center_aux,
		
		# script_get_heroes_attached_to_center
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
		procedure_town.get_heroes_attached_to_center,
		
		
		# script_get_heroes_attached_to_center_as_prisoner_aux
		# For internal use only
		procedure_town.get_heroes_attached_to_center_as_prisoner_aux,
		
		
		# script_get_heroes_attached_to_center_as_prisoner
		# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
		# Output: none, adds heroes to the party_no_to_collect_heroes party
		procedure_town.get_heroes_attached_to_center_as_prisoner,
		
		##
		##  # script_cf_get_party_leader
		##  # Input: arg1 = party_no
		##  # Output: reg0 = troop_no of the leader (Can fail)
		##  ("cf_get_party_leader",
		##    [
		##      (store_script_param_1, ":party_no"),
		##
		##      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
		##      (gt, ":num_stacks", 0),
		##      (party_stack_get_troop_id, ":stack_troop", ":party_no", 0),
		##      (troop_is_hero, ":stack_troop"),
		##      (assign, reg0, ":stack_troop"),
		##  ]),
		
		# script_give_center_to_faction
		# added dimplomacy
		# WARNING: modified by 1257dev
		# Input: arg1 = center_no, arg2 = faction
		procedure_town.give_center_to_faction,
		
		# script_give_center_to_faction_aux
		# WARNING modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = faction
		procedure_town.give_center_to_faction_aux,
		
		# script_change_troop_faction
		# Implementation of "lord defected" logic  
		# Input: arg1 = troop_no, arg2 = faction
		procedure_troop.change_troop_faction,
		
		# script_troop_set_title_according_to_faction
		# Input: arg1 = troop_no, arg2 = faction_no
		procedure_troop.troop_set_title_according_to_faction,
		

		# script_give_center_to_lord
		# WARNING: heavily modified by 1257AD devs
		# includes diplomacy!
		# Input: arg1 = center_no, arg2 = lord_troop, arg3 = add_garrison_to_center
		function_troop.give_center_to_lord,
		
		# script_get_number_of_hero_centers
		# Input: arg1 = troop_no
		# Output: reg0 = number of centers that are ruled by the hero
		function_troop.get_number_of_hero_centers,
		
		# script_cf_get_random_enemy_center
		# Input: arg1 = party_no
		# Output: reg0 = center_no
		function_party.cf_get_random_enemy_center,
		
		# script_find_travel_location
		# Input: arg1 = center_no
		# Output: reg0 = new_center_no (to travel within the same faction)
		function_town.find_travel_location,
		
		
		# script_get_relation_between_parties
		# Input: arg1 = party_no_1, arg2 = party_no_2
		# Output: reg0 = relation between parties
		function_party.get_relation_between_parties,

		# script_calculate_weekly_party_wage
		# no longer behaves like native
		# WARNING: modified by 1257devs
		# Input: arg1 = party_no
		# Output: reg0 = weekly wage
		function_party.calculate_weekly_party_wage,
		
		# script_calculate_player_faction_wage
		# no longer behaves like native
		# WARNING: modified by 1257devs
		# Input: arg1 = party_no
		# Output: reg0 = weekly wage
		function_party.calculate_player_faction_wage,
		
		# script_calculate_hero_weekly_net_income_and_add_to_wealth
		# no longer behaves like native
		# WARNING: heavily modified by 1257devs
		# Input: arg1 = troop_no
		# Output: none
		procedure_troop.calculate_hero_weekly_net_income_and_add_to_wealth,
		
		# script_cf_reinforce_party 
		# new tom  should no longer be used for lord parties reinforcement.
		# Can fail.
		# WARNING: heavily modified by 1257devs
		# Input: arg1 = party_no,
		# Output: none
		# Adds reinforcement to party according to its type and faction
		# Called from several places, simple_triggers for centers, script_hire_men_to_kingdom_hero_party for hero parties
		procedure_party.cf_reinforce_party,
		
		# script_hire_men_to_kingdom_hero_party
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = troop_no (hero of the party)
		# Output: none
		procedure_troop.hire_men_to_kingdom_hero_party,
		
		# script_get_percentage_with_randomized_round
		# Input: arg1 = value, arg2 = percentage
		# Output: reg0 result percentage with randomised round
		function_helper.get_percentage_with_randomized_round,
		
		# script_create_cattle_herd
		# Input: arg1 = center_no, arg2 = amount (0 = default)
		# Output: reg0 = party_no
		function_town.create_cattle_herd,
		
		#script_buy_cattle_from_village
		# Input: arg1 = village_no, arg2 = amount, arg3 = single_cost
		# Output: reg0 = party_no
		function_town.buy_cattle_from_village,
		
		#script_kill_cattle_from_herd
		# Input: arg1 = party_no, arg2 = amount
		# Output: none (fills trp_temp_troop's inventory)
		procedure_party.kill_cattle_from_herd,
		
		# script_create_kingdom_hero_party
		# creates player kingdom!
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = troop_no, arg2 = center_no
		# Output: $pout_party = party_no
		procedure_troop.create_kingdom_hero_party,
		
		# script_create_kingdom_party_if_below_limit
		# WARNING: modified by 1257AD devs
		# Input: arg1 = faction_no, arg2 = party_type (variables beginning with spt_)
		# Output: reg0 = party_no
		function_faction.create_kingdom_party_if_below_limit,
		
		
		# script_cf_create_kingdom_party
		# WARNING: modified by 1257AD devs
		# Input: arg1 = faction_no, arg2 = party_type (variables beginning with spt_)
		# Output: reg0 = party_no
		function_faction.cf_create_kingdom_party,
		
		# script_get_troop_attached_party
		# Input: arg1 = troop_no
		# Output: reg0 = party_no (-1 if troop's party is not attached to a party)
		function_troop.get_troop_attached_party,
		
		
		# script_center_get_food_consumption
		# Input: arg1 = center_no
		# Output: reg0: food consumption (1 food item counts as 100 units)
		function_town.center_get_food_consumption,
		
		# script_center_get_food_store_limit
		# WARNING: modified by 1257AD devs
		# Input: arg1 = center_no
		# Output: reg0: food consumption (1 food item counts as 100 units)
		function_town.center_get_food_store_limit,
		
		# script_refresh_village_merchant_inventory
		# Input: arg1 = village_no
		# Output: none
		procedure_town.refresh_village_merchant_inventory,
		
		# script_refresh_village_defenders
		# Input: arg1 = village_no
		# Output: none
		procedure_town.refresh_village_defenders,
		
		# script_village_set_state
		# no longer resemble script in native version
		# 1257AD prosperity system resides here
		# WARNING: heavily modified by 1257AD
		# Input: arg1 = center_no arg2:new_state
		# Output: reg0: food consumption (1 food item counts as 100 units)
		function_town.village_set_state,
		
		##campaign
		# script_process_village_raids
		# called from triggers every two hours
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_campaign.process_village_raids,
		
		## campaign
		# script_process_sieges
		# called from triggers
		# WARNING: heavily modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_campaign.process_sieges,
		
		# script_lift_siege
		# Input: arg1 = center_no, arg2 = display_message
		# Output: none
		# called from triggers
		procedure_campaign.lift_siege,
	
		# script_process_alarms_new
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# this script is called in from a simple triger
		# description: same as an old, but single center thingy, called for a specific thing
		# todo "#maybe do audio sound?"
		# INPUT: center
		# OUTPUT: none
		procedure_AD1257.process_alarms_new,
	
		# script_process_alarms
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# probably this one is deprecated(?)
		# this script is called in from a simple triger
		# Input: none
		# Output: none
		procedure_AD1257.process_alarms,
		
		# script_allow_vassals_to_join_indoor_battle
		# Input: none
		# Output: none
		procedure_campaign.allow_vassals_to_join_indoor_battle,
		
		# script_party_set_ai_state
		# sets party AI state
		# Redone somewhat on Feb 18 to make sure that initative is set properly
		# WARNING: modified by 1257AD devs
		# Input: arg1 = party_no, arg2 = new_ai_state, arg3 = action_object (if necessary)
		# Output: none (Can fail)
		procedure_party.party_set_ai_state,
		
		# script_cf_party_under_player_suggestion
		# idk wtf is this. 
		# INPUT: arg1 = party_no
		# OUTPUT: none. Can fail!

		cfunction_party.cf_party_under_player_suggestion,
		
		# script_troop_does_business_in_center
		# Currently called from process_ai_state, could be called from elsewhere
		# It is used for lord to (1)Court ladies (2)Collect rents (3)Look for volunteers
		# WARNING: heavily modified by 1257AD devs
		# INPUT: arg1 = troop_no, arg2 = center_no
		# OUTPUT: none
		procedure_troop.troop_does_business_in_center,
		
		# script_process_kingdom_parties_ai
		# This is called more frequently than decide_kingdom_parties_ai
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		#called from triggers
		procedure_campaign.process_kingdom_parties_ai,
		
		# script_process_hero_ai
		# This is called more frequently than script_decide_kingdom_party_ais
		# Handles sieges, raids, etc -- does not change the party's basic mission.
		# WARNING: modified by 1257AD devs
		# called from triggers
		# Input: none
		# Output: none
		
		procedure_campaign.process_hero_ai,
		
		# script_begin_assault_on_center
		# called from triggers
		# Input: arg1: faction_no
		# Output: none
		procedure_campaign.begin_assault_on_center,
		
		#DEPRECATED - Using new political issue system instead
		("select_faction_marshall",	[] ),
		
		# script_get_center_faction_relation_including_player
		# called from triggers
		# Input: arg1: center_no, arg2: target_faction_no
		# Output: reg0: relation
		
		function_town.get_center_faction_relation_including_player,
		
		#script_update_report_to_army_quest_note
		# 
		# INPUT: arg1 = faction_no, arg2= faction_strategy, arg3 = old_faction state
		# OUTPUT: none
		procedure_quest.update_report_to_army_quest_note,
		
		
		# script_decide_faction_ai
		# called from triggers
		# WARNING : heavily modified by 1257AD devs
		# note : "abc begins an offensive.  Curret target is xyz" messages are also printed from this procedure
		# Input: arg1: faction_no
		# Output: none
		procedure_campaign.decide_faction_ai,
		
		# script_check_and_finish_active_army_quests_for_faction
		# Input: faction_no
		# Output: none
		procedure_quest.check_and_finish_active_army_quests_for_faction,
		
		# script_troop_get_player_relation
		# Input: arg1 = troop_no
		# Output: reg0 = effective relation (modified by troop reputation, honor, etc.)
		function_troop.troop_get_player_relation,
		
		# script_change_troop_renown
		# Input: arg1 = troop_no, arg2 = relation difference
		# Output: none
		procedure_troop.change_troop_renown,
		
		
		# script_change_player_relation_with_troop
		# Input: arg1 = troop_no, arg2 = relation difference
		# Output: none
		procedure_troop.change_player_relation_with_troop,
		
		# script_change_player_relation_with_center
		# Input: arg1 = party_no, arg2 = relation difference
		# Output: none
		procedure_party.change_player_relation_with_center,
		
		
		# script_change_player_relation_with_faction
		# Input: arg1 = faction_no, arg2 = relation difference
		# Output: none
		procedure_faction.change_player_relation_with_faction,
		
		# script_set_player_relation_with_faction
		# Input: arg1 = faction_no, arg2 = relation
		# Output: none
		procedure_faction.set_player_relation_with_faction,
		
		
		
		# script_change_player_relation_with_faction_ex
		# changes relations with other factions also (according to their relations between each other)
		# Input: arg1 = faction_no, arg2 = relation difference
		# Output: none
		procedure_faction.change_player_relation_with_faction_ex,
		
		# script_cf_get_random_active_faction_except_player_faction_and_faction
		# WARNING : modified by 1257AD devs
		# "rafi: inject religion stuff"
		# Input: arg1 = except_faction_no
		# Output: reg0 = random_faction
		function_faction.cf_get_random_active_faction_except_player_faction_and_faction,
		
		# script_make_kingdom_hostile_to_player
		# Input: arg1 = faction_no, arg2 = relation difference
		# Output: none
		procedure_faction.make_kingdom_hostile_to_player,
		

		# script_change_player_honor
		# prints "you gain/lose honour" if player honour changes
		# Input: arg1 = honor difference
		# Output: none
		procedure_player.change_player_honor,
		
		# script_change_player_party_morale
		# Input: arg1 = morale difference
		# Output: none
		procedure_player.change_player_party_morale,
		

		# script_cf_player_has_item_without_modifier
		# Input: arg1 = item_id, arg2 = modifier
		# Output: none (can_fail)
		cfunction_player.cf_player_has_item_without_modifier,
		
		# script_get_player_party_morale_values
		# Output: reg0 = player_party_morale_target
		function_player.get_player_party_morale_values,
		
		# script_diplomacy_start_war_between_kingdoms
		# sets relations between two kingdoms and their vassals.
		# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
		# Output: none
		procedure_diplomacy.diplomacy_start_war_between_kingdoms,
		#script_diplomacy_party_attacks_neutral
		# called from game_menus (plundering a village, raiding a village),  from dialogs: surprise attacking a neutral lord, any attack on caravan or villagers
		# WARNING: modified by 1257AD devs
		# INPUT: attacker_party, defender_party
		# OUTPUT: none
		procedure_diplomacy.diplomacy_party_attacks_neutral,
		
		# script_party_calculate_and_set_nearby_friend_enemy_follower_strengths
		# WARNING: modified by 1257AD faction
		# Input: party_no
		# Output: none
		procedure_party.party_calculate_and_set_nearby_friend_enemy_follower_strengths,
		
		# script_init_ai_calculation
		# Input: none
		# Output: none
		procedure_ai.init_ai_calculation,
		
		
		# script_recalculate_ais
		# Input: none
		# Output: none
		#When a lord changes factions
		#When a center changes factions
		#When a center is captured
		#When a marshal is defeated
		#Every 23 hours
		procedure_ai.recalculate_ais,
		
		# script_calculate_troop_ai
		# Input: troop_no
		# Output: none
		#Now called directly from scripts
		procedure_ai.calculate_troop_ai,
		
		# script_diplomacy_start_peace_between_kingdoms
		# this procedure includes diplomacy mods
		# WARNING: modified by 1257AD devs
		# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
		# Output: none
		procedure_diplomacy.diplomacy_start_peace_between_kingdoms,
		
		
		# script_event_kingdom_make_peace_with_kingdom
		# Input: arg1 = source_kingdom, arg2 = target_kingdom
		# Output: none
		procedure_diplomacy.event_kingdom_make_peace_with_kingdom,
		
		# script_randomly_start_war_peace
		# Aims to introduce a slightly simpler system in which the AI kings' reasoning could be made more  transparent to the player. 
		# At the start of the game, this may lead to less variation in outcomes, though
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = initializing_war_peace_cond (1 = true, 0 = false)
		# Output: none
		procedure_diplomacy.randomly_start_war_peace_new,
		
		# script_exchange_prisoners_between_factions
		# Input: arg1 = faction_no_1, arg2 = faction_no_2
		procedure_faction.exchange_prisoners_between_factions,
		
		# script_add_notification_menu
		# Input: arg1 = menu_no, arg2 = menu_var_1, arg3 = menu_var_2
		# Output: none
		procedure_user_interface.add_notification_menu,
		
		# script_finish_quest
		# Input: arg1 = quest_no, arg2 = finish_percentage
		# Output: none
		procedure_quest.finish_quest,
		
		
		# script_get_information_about_troops_position
		# Input: arg1 = troop_no, arg2 = time (0 if present tense, 1 if past tense)
		# Output: s1 = String, reg0 = knows-or-not
		function_troop.get_information_about_troops_position,
		
		# script_recruit_troop_as_companion
		# Input: arg1 = troop_no,
		# Output: none
		procedure_troop.recruit_troop_as_companion,
		
		
		# script_setup_random_scene
		# used to generate battle scene! interesting stuffs
		# WARNING : HEAVILY modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = mission_template_no
		# Output: none
		procedure_scene.setup_random_scene,
		
		# script_enter_dungeon
		# Input: arg1 = center_no, arg2 = mission_template_no
		# Output: none
		procedure_scene.enter_dungeon,
		
		# script_enter_court
		# other search term: setup_court
		# includes diplomacy mod
		# WARNING: heavily modified by 1257AD
		# Input: arg1 = center_no
		# Output: none
		procedure_scene.enter_court,
		
		#script_setup_meet_lady
		# sets up a scene to meet player with lady
		# INPUT: lady_no, center_no
		# OUTPUT: none
		procedure_scene.setup_meet_lady,
		
		# script_find_high_ground_around_pos1
		# Input: pos1 should hold center_position_no
		#        arg1: team_no
		#        arg2: search_radius (in meters)
		# Output: pos52 contains highest ground within <search_radius> meters of team leader
		# Destroys position registers: pos10, pos11, pos15
		function_battle.find_high_ground_around_pos1,
		
		# script_select_battle_tactic
		# Input: none
		# Output: none
		procedure_battle.select_battle_tactic,
		
		# script_select_battle_tactic_aux
		# Input: team_no
		# Output: battle_tactic
		function_battle.select_battle_tactic_aux,
		
		# script_battle_tactic_init
		# Input: none
		# Output: none
		procedure_battle.battle_tactic_init,
		
		# script_battle_tactic_init_aux
		# Input: team_no, battle_tactic
		# Output: none
		procedure_battle.orig_battle_tactic_init_aux,
		
		# script_calculate_team_powers
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: ally_power, enemy_power
		function_battle.calculate_team_powers, #ozan
		
		# script_apply_effect_of_other_people_on_courage_scores
		# called during battle, bots logic
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_battle.apply_effect_of_other_people_on_courage_scores, #ozan
		
		# script_apply_death_effect_on_courage_scores
		# called during battle, bots logic
		# WARNING: modified by 1257AD devs
		# Input: dead agent id, killer agent id
		# Output: none
		procedure_battle.apply_death_effect_on_courage_scores, #ozan
		
		# script_decide_run_away_or_not
		# called during battle, bots logic
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_battle.orig_decide_run_away_or_not, #ozan
		
		# script_battle_tactic_apply
		# Input: none
		# Output: none
		procedure_battle.battle_tactic_apply,
		
		# script_battle_tactic_apply_aux
		# Input: team_no, battle_tactic
		# Output: battle_tactic
		function_battle.orig_battle_tactic_apply_aux,
		
		
		# script_team_get_class_percentages
		# Input: arg1: team_no, arg2: try for team's enemies
		# Output: reg0: percentage infantry, reg1: percentage archers, reg2: percentage cavalry
		function_battle.team_get_class_percentages,
		
		# script_get_closest3_distance_of_enemies_at_pos1
		# Input: arg1: team_no, pos1
		# Output: reg0: distance in cms. tom: reg4 - the closest agent id
		function_battle.get_closest3_distance_of_enemies_at_pos1,

		# script_team_get_average_position_of_enemies
		# Input: arg1: team_no,
		# Output: pos0: average position.
		function_battle.team_get_average_position_of_enemies,
		
		
		# script_search_troop_prisoner_of_party
		# Input: arg1 = troop_no
		# Output: reg0 = party_no (-1 if troop is not a prisoner.)
		function_troop.search_troop_prisoner_of_party,
		
		# script_change_debt_to_troop
		# Input: arg1 = troop_no, arg2 = new debt amount
		# Output: none
		procedure_troop.change_debt_to_troop,
		
		
		# script_abort_quest
		# Input: arg1 = quest_no, arg2 = apply relation penalty
		# Output: none
		procedure_quest.abort_quest,
		
		
		# script_cf_is_quest_troop
		# Input: arg1 = troop_no
		# Output: none (can fail)
		cfunction_troop.cf_is_quest_troop,
		
		# script_check_friendly_kills
		# Input: none
		# Output: none (changes the morale of the player's party)
		procedure_battle.check_friendly_kills,
		
		# script_simulate_retreat
		# Input: arg1 = players_side_damage, arg2 = enemy_side_damage, arg3 = continue_battle s5 = title_string
		# Output: none
		procedure_battle.simulate_retreat,

		
		# script_simulate_battle_with_agents_aux
		# For internal use only
		# Input: arg1 = attacker_side (0 = ally, 1 = enemy), arg2 = damage amount
		# Output: none
		procedure_battle.simulate_battle_with_agents_aux,
		
		
		# script_map_get_random_position_around_position_within_range
		# Input: arg1 = minimum_distance in km, arg2 = maximum_distance in km, pos1 = origin position
		# Output: pos2 = result position
		function_campaign.map_get_random_position_around_position_within_range,
		
		
		# script_get_number_of_unclaimed_centers_by_player
		# Input: none
		# Output: reg0 = number of unclaimed centers, reg1 = last unclaimed center_no
		function_campaign.get_number_of_unclaimed_centers_by_player,
		
		# script_cf_troop_check_troop_is_enemy
		# Input: arg1 = troop_no, arg2 = checked_troop_no
		# Output: none (Can fail)
		cfunction_troop.cf_troop_check_troop_is_enemy,
		
		
		# script_troop_get_leaded_center_with_index
		# Input: arg1 = troop_no, arg2 = center index within range between zero and the number of centers that troop owns
		# Output: reg0 = center_no
		function_troop.troop_get_leaded_center_with_index,
		
		# script_cf_troop_get_random_leaded_walled_center_with_less_strength_priority
		# Input: arg1 = troop_no, arg2 = preferred_center_no
		# Output: reg0 = center_no (Can fail)
		function_troop.cf_troop_get_random_leaded_walled_center_with_less_strength_priority,
		
		# script_cf_troop_get_random_leaded_town_or_village_except_center
		# Input: arg1 = troop_no, arg2 = except_center_no
		# Output: reg0 = center_no (Can fail)
		function_troop.cf_troop_get_random_leaded_town_or_village_except_center,
		
		# script_troop_write_owned_centers_to_s2
		# Input: arg1 = troop_no
		# Output: none
		function_troop.troop_write_owned_centers_to_s2,
		
		# script_troop_write_family_relations_to_s1
		# clears s1 string
		# Input: none
		# Output: none
		procedure_troop.troop_write_family_relations_to_s1,
		
		# script_write_family_relation_as_s3s_s2_to_s4
		# Inputs: arg1 = troop_no, arg2 = family_no (valid slot no after slot_troop_family_begin)
		# Outputs: s11 = what troop_1 is to troop_2, reg0 = strength of relationship. Normally, "$g_talk_troop" should be troop_2
		function_troop.troop_get_family_relation_to_troop,
		
		# script_complete_family_relations
		# Inputs: none
		# Outputs: none
		#complete family relations removed
		# script_collect_friendly_parties
		# Fills the party p_collective_friends with the members of parties attached to main_party and ally_party_no
		procedure_troop.collect_friendly_parties,
		
		# script_encounter_calculate_fit
		# Input: arg1 = troop_no
		# Output: none
		procedure_campaign.encounter_calculate_fit,
		
		# script_encounter_init_variables
		# part of freelancer script is in this procedure
		# WARNING : HEAVILY modified by 1257AD devs
		# Input: arg1 = troop_no
		# Output: none
		procedure_campaign.encounter_init_variables,
		
		# script_calculate_renown_value
		# WARNING: slightly modified by 1257AD devs
		# Input: arg1 = troop_no
		# Output: fills $battle_renown_value
		procedure_troop.calculate_renown_value,
		
		# script_get_first_agent_with_troop_id
		# called during battle
		# Input: arg1 = troop_no
		# Output: agent_id
		function_troop.cf_get_first_agent_with_troop_id,
		
		
		# script_cf_team_get_average_position_of_agents_with_type_to_pos1
		# Input: arg1 = team_no, arg2 = class_no (grc_everyone, grc_infantry, grc_cavalry, grc_archers, grc_heroes)
		# Output: none, pos1 = average_position (0,0,0 if there are no matching agents)
		function_battle.cf_team_get_average_position_of_agents_with_type_to_pos1,
		
		# script_cf_turn_windmill_fans
		# Input: arg1 = instance_no (none = 0)
		# Output: none
		procedure_scene.cf_turn_windmill_fans,
		
		# script_print_party_members
		# Input: arg1 = party_no
		# Output: s51 = output string. "noone" if the party is empty
		function_party.print_party_members,
		
		# script_round_value
		# really? the power of talesworlds's ""scripting engine""
		# Input: arg1 = value
		# Output: reg0 = rounded_value
		function_helper.round_value,
		
		# script_change_banners_and_chest
		# Input: none
		# Output: none
		procedure_scene.change_banners_and_chest,
		
		
		# script_remove_siege_objects
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_scene.remove_siege_objects,
	
		#script_remove_manor_objects - tommade
		# interesting stuffs!
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT:none
		# OUTPUT:none
		#description: removes the objects from unique manor scenes which suppose to be not used
		procedure_AD1257_manor_scene.remove_manor_objects,
	
		# script_describe_relation_to_s63
		# Input: arg1 = relation (-100 .. 100)
		# Output: s63
		function_helper.describe_relation_to_s63,
		
		# script_describe_center_relation_to_s3
		# Input: arg1 = relation (-100 .. 100)
		# Output: s3
		function_helper.describe_center_relation_to_s3,
		
		
		# script_center_ambiance_sounds
		# Input: none
		# Output: none
		# to be called every two seconds
		procedure_scene.center_ambiance_sounds,
		
		# script_center_set_walker_to_type
		# Input: arg1 = center_no, arg2 = walker_no, arg3 = walker_type,
		# Output: none
		procedure_scene.center_set_walker_to_type,
		
		
		# script_cf_center_get_free_walker
		# Input: arg1 = center_no
		# Output: reg0 = walker no (can fail)
		function_scene.cf_center_get_free_walker,
		
		# script_center_remove_walker_type_from_walkers
		# Input: arg1 = center_no, arg2 = walker_type,
		# Output: reg0 = 1 if comment found, 0 otherwise; s61 will contain comment string if found
		function_scene.center_remove_walker_type_from_walkers,
		
		
		# script_init_town_walkers
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_scene.init_town_walkers,
		
		
		# script_cf_enter_center_location_bandit_check
		# bandit checks
		# WARNING: modified by 1257AD devs
		# Input: none
		# Output: none
		cfunction_bandit.cf_enter_center_location_bandit_check,
		
		# script_init_town_agent
		# Input: none
		# Output: none
		procedure_scene.init_town_agent,
		
		# script_init_town_walker_agents
		# Input: none
		# Output: none
		procedure_scene.init_town_walker_agents,
		
		# script_agent_get_town_walker_details
		# This script assumes this is one of town walkers.
		# Input: agent_id
		# Output: reg0: town_walker_type, reg1: town_walker_dna
		function_scene.agent_get_town_walker_details,
		
		#script_town_walker_occupation_string_to_s14
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT : agent_no
		# OUTPUT : s14
		function_scene.town_walker_occupation_string_to_s14,
		
		# script_tick_town_walkers
		# Input: none
		# Output: none
		procedure_scene.tick_town_walkers,
		
		
		# script_set_town_walker_destination
		# WARNING: modified by 1257AD devs
		# Input: arg1 = agent_no
		# Output: none
		procedure_scene.set_town_walker_destination,
		
		# script_town_init_doors
		# Input: door_state (-1 = closed, 1 = open, 0 = use $town_nighttime)
		# Output: none (required for siege mission templates)
		procedure_scene.town_init_doors,
		
		# script_siege_init_ai_and_belfry
		# Input: none
		# Output: none (required for siege mission templates)
		procedure_siege.siege_init_ai_and_belfry,

		# script_cf_siege_move_belfry
		# Input: none
		# Output: none (required for siege mission templates)
		procedure_siege.cf_siege_move_belfry,
		
		# script_cf_siege_rotate_belfry_platform
		# Input: none
		# Output: none (required for siege mission templates)
		procedure_siege.cf_siege_rotate_belfry_platform,
		
		# script_cf_siege_assign_men_to_belfry
		# Input: none
		# Output: none (required for siege mission templates)
		procedure_siege.cf_siege_assign_men_to_belfry,
		
		# script_siege_move_archers_to_archer_positions
		# NO longer behaves like native
		# WARNING : modified by 1257AD devs
		# Input: none
		# Output: none
		procedure_siege.siege_move_archers_to_archer_positions,
	
		# script_siege_move_archers_to_archer_positions_new
		# i'm guessing this is AI stuff for archer during battle, idk if it's also gets called from siege. 
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
		procedure_AD1257_siege.siege_move_archers_to_archer_positions_new,
		
		# script_siege_move_infantry_to_infantry_positions_new
		# i'm guessing this is AI stuff for infantry during battle, idk if it's also gets called from siege. 
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
		procedure_AD1257_siege.siege_move_infantry_to_infantry_positions_new,
		
		# script_store_movement_order_name_to_s1
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: arg1 = team_no, arg2 = class_no
		# Output: s1 = order_name
		function_battle_ui.store_movement_order_name_to_s1,
		
		# script_store_riding_order_name_to_s1
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: arg1 = team_no, arg2 = class_no
		# Output: s1 = order_name
		function_battle_ui.store_riding_order_name_to_s1,
		
		# script_store_weapon_usage_order_name_to_s1
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: arg1 = team_no, arg2 = class_no
		# Output: s1 = order_name
		function_battle_ui.store_weapon_usage_order_name_to_s1,
		
		# script_team_give_order_from_order_panel
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: arg1 = leader_agent_no, arg2 = class_no
		# Output: none
		procedure_battle_ui.team_give_order_from_order_panel,
		
		
		# script_update_order_panel
		# some UI stuffs in battle pane during battle, might b interesting
		# WARNING : modified by 1257AD devs
		# Input: arg1 = team_no
		# Output: none
		procedure_battle_ui.update_order_panel,
		
		# script_update_agent_position_on_map
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: arg1 = agent_no, pos2 = map_size_pos
		# Output: none
		procedure_battle_ui.update_agent_position_on_map,
		
		# script_convert_3d_pos_to_map_pos
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: pos1 = 3d_pos, pos2 = map_size_pos
		# Output: pos0 = map_pos
		function_battle_ui.convert_3d_pos_to_map_pos,
		
		# script_update_order_flags_on_map
		# some UI stuffs in battle pane during battle, might b interesting
		# Input: none
		# Output: none
		procedure_battle_ui.update_order_flags_on_map,
		
		# script_update_order_panel_checked_classes
		# some UI stuffs in battle pane during battle, might b interesting 
		# Input: none
		# Output: none
		procedure_battle_ui.update_order_panel_checked_classes,
		
		# script_update_order_panel_statistics_and_map
		# mini map in battle pane
		# Input: none
		# Output: none
		procedure_battle_ui.update_order_panel_statistics_and_map,
		
		# script_set_town_picture
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
		procedure_AD1257_ui.set_town_picture,
		
		
		# script_consume_food
		# Input: arg1: order of the food to be consumed
		# Output: none
		procedure_economy.consume_food,
		
		
		# script_calculate_troop_score_for_center
		# Input: arg1 = troop_no, arg2 = center_no
		# Output: reg0 = score
		function_troop.calculate_troop_score_for_center,
		
		
		# script_assign_lords_to_empty_centers
		# Input: none
		# Output: none
		#Now ONLY called from the start
		procedure_game_init.assign_lords_to_empty_centers,
		
		
		# script_create_village_farmer_party
		# spawns villager party
		# WARNING : modified by 1257AD devs
		# WARNING : IT'S ALSO DISABLED BY TOM!! look simple_triggers at : 2300
		# Input: arg1 = village_no
		# Output: reg0 = party_no
		function_town.create_village_farmer_party,
	 
		#script_do_villager_center_trade - tom mader
		# NOTE: NOT PRESENT IN NATIVE SCRIPTS 1257AD devs
		# USage: to simulate economy systems.
		# INPUT: arg1 = party_no, arg2 = center_no,
		# OUTPUT: reg0 = total_change
		function_economy.do_villager_center_trade,
	 
		#script_do_party_center_trade
		# INPUT: arg1 = party_no, arg2 = center_no, arg3 = percentage_change_in_center
		# OUTPUT: reg0 = total_change
		function_economy.do_party_center_trade,
		
		#script_player_join_faction
		# WARNING : modified by 1257AD devs
		# INPUT: arg1 = faction_no
		# OUTPUT: none
		procedure_player.player_join_faction,
		
		#script_player_leave_faction
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = give_back_fiefs
		# OUTPUT: none
		procedure_player.player_leave_faction,
		
		#script_deactivate_player_faction
		# INPUT: none
		# OUTPUT: none
		procedure_player.deactivate_player_faction,
		
		
		#script_activate_player_faction
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = last_interaction_with_faction
		# OUTPUT: none
		#When a player convinces her husband to rebel
		#When a player proclaims herself queen
		#When a player seizes control of a center
		#When a player recruits a lord through intrigue
		#When a player  modded2x anon: what?
		procedure_player.activate_player_faction,
		
		
		#script_agent_reassign_team
		# there are freelancer scripts resides here
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = agent_no
		# OUTPUT: none
		procedure_battle.agent_reassign_team,
		
		#script_start_quest
		# INPUT: arg1 = quest_no, arg2 = giver_troop_no, s2 = description_text
		# OUTPUT: none
		procedure_quest.start_quest,
		
		#script_conclude_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
		procedure_quest.conclude_quest,
		
		#script_succeed_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
		procedure_quest.succeed_quest,
		
		#script_fail_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
		procedure_quest.fail_quest,
		
		#script_report_quest_troop_positions
		# INPUT: arg1 = quest_no, arg2 = troop_no, arg3 = note_index
		# OUTPUT: none
		procedure_quest.report_quest_troop_positions,
		
		#script_end_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
		procedure_quest.end_quest,
		
		#script_cancel_quest
		# INPUT: arg1 = quest_no
		# OUTPUT: none
		procedure_quest.cancel_quest,
		
		
		#script_get_available_mercenary_troop_and_amount_of_center
		# INPUT: arg1 = center_no
		# OUTPUT: reg0 = mercenary_troop_type, reg1 = amount
		function_town.get_available_mercenary_troop_and_amount_of_center,
		
		#script_update_village_market_towns
		# INPUT: none
		# OUTPUT: none
		procedure_economy.update_village_market_towns,    
		
		#script_update_mercenary_units_of_towns
		# WARNING: heavily modified by 1257AD devs
		# INPUT: none
		# OUTPUT: none
		procedure_town.update_mercenary_units_of_towns,
	
		#script_update_volunteer_troops_in_village
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = center_no
		# OUTPUT: none
		procedure_town.update_volunteer_troops_in_village,
		
		#script_update_npc_volunteer_troops_in_village - tom rewriten
		# no longer behaves like in native!
		# WARNING: heavily modified by 1257AD devs
		# INPUT: arg1 = center_no
		# OUTPUT: none
		procedure_town.update_npc_volunteer_troops_in_village,
		
		#script_update_companion_candidates_in_taverns
		# WARNING: modified by 1257AD devs
		# INPUT: none
		# OUTPUT: none
		procedure_companion.update_companion_candidates_in_taverns,
		
		#script_update_ransom_brokers
		# INPUT: none
		# OUTPUT: none
		procedure_companion.update_ransom_brokers,
		
		#script_update_tavern_travellers
		# INPUT: none
		# OUTPUT: none
		procedure_companion.update_tavern_travellers,
		
		#script_update_villages_infested_by_bandits
		# INPUT: none
		# OUTPUT: none
		procedure_town.update_villages_infested_by_bandits,
		
		#script_update_booksellers
		# INPUT: none
		# OUTPUT: none
		procedure_companion.update_booksellers,
		
		#script_update_tavern_minstels
		# INPUT: none
		# OUTPUT: none
		procedure_companion.update_tavern_minstrels,
		
		#script_update_other_taverngoers
		# INPUT: none
		# OUTPUT: none
		procedure_companion.update_other_taverngoers,
		
		
		#script_update_faction_notes
		# INPUT: faction_no
		# OUTPUT: none
		procedure_notes.update_faction_notes,
		
		#script_update_faction_political_notes
		# INPUT: faction_no
		# OUTPUT: none
		procedure_notes.update_faction_political_notes,
		
		
		
		#script_update_faction_traveler_notes
		# INPUT: faction_no
		# OUTPUT: none
		procedure_notes.update_faction_traveler_notes,
		
		
		#script_update_troop_notes
		# stub procedure
		# INPUT: troop_no
		# OUTPUT: none
		procedure_notes.update_troop_notes,
		
		#script_update_troop_location_notes
		# INPUT: troop_no
		# OUTPUT: none
		procedure_notes.update_troop_location_notes,
		
		#script_update_troop_location_notes_prisoned
		# INPUT: troop_no
		# OUTPUT: none
		procedure_notes.update_troop_location_notes_prisoned,
		
		#script_update_troop_political_notes
		# INPUT: troop_no
		# OUTPUT: none
		procedure_notes.update_troop_political_notes,
		
		#script_update_center_notes

		# INPUT: center_no
		# OUTPUT: none
		procedure_notes.update_center_notes,
		
		
		#script_update_center_recon_notes
		# INPUT: center_no
		# OUTPUT: none
		procedure_notes.update_center_recon_notes,
		
		#script_update_all_notes
		# INPUT: none
		# OUTPUT: none
		procedure_notes.update_all_notes,
		
		#script_agent_troop_get_banner_mesh
		# part of freelancer script resides here
		# WARNING: heavily modified by 1257AD devs
		# INPUT: agent_no, troop_no
		# OUTPUT: banner_mesh
		function_banner.agent_troop_get_banner_mesh,

		#script_shield_item_set_banner
		#script_shield_item_set_banner_old
		# INPUT: agent_no
		# OUTPUT: none
		procedure_banner.shield_item_set_banner_old,
	
		#shield_item_set_banner_old
		# INPUT: agent_no
		# OUTPUT: none
		procedure_banner.shield_item_set_banner,
		
		
		#script_troop_agent_set_banner
		# INPUT: agent_no
		# OUTPUT: none
		procedure_banner.troop_agent_set_banner,
	
	
		#script_agent_troop_get_historical_mesh
		# NOTE: heavily modified by 1257AD devs
		# INPUT: agent_no, troop_no
		# OUTPUT: banner_mesh
		function_banner.agent_troop_get_historical_mesh,
		
		#script_initialize_item_banners
		# NOTE: modified by 1257AD devs 
		# INPUT: none
		# OUTPUT: none
		##initialize certain items default banners - to be used with historical banners
		procedure_game_init.initialize_item_banners,
	
		#script_add_troop_to_cur_tableau
		# INPUT: troop_no
		# OUTPUT: none
		procedure_user_interface.add_troop_to_cur_tableau,
		
		#script_add_troop_to_cur_tableau_for_character
		# INPUT: troop_no
		# OUTPUT: none
		procedure_user_interface.add_troop_to_cur_tableau_for_character,
		
		#script_add_troop_to_cur_tableau_for_inventory
		# INPUT: troop_no
		# OUTPUT: none
		procedure_user_interface.add_troop_to_cur_tableau_for_inventory,
		
		#script_add_troop_to_cur_tableau_for_profile
		# INPUT: troop_no
		# OUTPUT: none
		procedure_user_interface.add_troop_to_cur_tableau_for_profile,
		
		#script_add_troop_to_cur_tableau_for_retirement
		# NOTE: pose in retirement screen
		# INPUT: type
		# OUTPUT: none
		procedure_user_interface.add_troop_to_cur_tableau_for_retirement,
		
		#script_add_troop_to_cur_tableau_for_party
		# INPUT: troop_no
		# OUTPUT: none
		procedure_user_interface.add_troop_to_cur_tableau_for_party,
		
		#script_get_prosperity_text_to_s50
		# INPUT: center_no
		# OUTPUT: returns to s50
		function_economy.get_prosperity_text_to_s50,

		#script_spawn_bandit_lairs - tom made
		# NOTE: NOT PRESENT IN NATIVE SCRIPT! AD1257 devs
		#INPUT: NONE
		#OUTPUT: NONE
		#DESCRIPTION: spawns a bunch of bandit lairs. Bandits lairs latter spawn bandits, excluding the looters.
		procedure_AD1257.spawn_bandit_lairs,

			
		#script_spawn_bandits - tom made
		# NOTE: NOT PRESENT IN NATIVE SCRIPT! AD1257 devs
		# INPUT: none
		# OUTPUT: none
		procedure_AD1257.spawn_bandits2,

	
		#script_spawn_bandits
		# WARNING: heavily modified by 1257AD devs
		# INPUT: none
		# OUTPUT: none
		procedure_campaign.spawn_bandits,

		#script_count_mission_casualties_from_agents
		# WARNING: heavily modified by 1257Ad devs
		# INPUT: none
		# OUTPUT: none
		procedure_battle.count_mission_casualties_from_agents,
		
		#script_get_max_skill_of_player_party
		# INPUT: arg1 = skill_no
		# OUTPUT: reg0 = max_skill, reg1 = skill_owner_troop_no
		function_player.get_max_skill_of_player_party,
		
		#script_upgrade_hero_party
		# INPUT: arg1 = party_id, arg2 = xp_amount
		procedure_party.upgrade_hero_party,
		
		#script_get_improvement_details
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = improvement
		# OUTPUT: reg0 = base_cost
		function_economy.get_improvement_details,
		
		#script_cf_troop_agent_is_alive
		# INPUT: arg1 = troop_id
		cfunction_troop.cf_troop_agent_is_alive,
		
		#script_cf_village_recruit_volunteers_cond
		# INPUT: none
		# OUTPUT: none
		cfunction_town.cf_village_recruit_volunteers_cond,
		
		#script_village_recruit_volunteers_recruit
		# INPUT: none
		# OUTPUT: none
		procedure_town.village_recruit_volunteers_recruit,
		
		#script_get_troop_item_amount
		# INPUT: arg1 = troop_no, arg2 = item_no
		# OUTPUT: reg0 = item_amount
		function_troop.get_troop_item_amount,
		
		#script_get_name_from_dna_to_s50
		# INPUT: arg1 = dna
		# OUTPUT: s50 = name
		function_helper.get_name_from_dna_to_s50,
		
		#script_change_center_prosperity
		# INPUT: arg1 = center_no, arg2 = difference
		# OUTPUT: none
		procedure_town.change_center_prosperity,
		
		#script_get_center_ideal_prosperity
		# INPUT: arg1 = center_no
		# OUTPUT: reg0 = ideal_prosperity
		function_town.get_center_ideal_prosperity,
		
		#script_good_price_affects_good_production
		# INPUT: arg1 = center_no, arg2 input item no, arg3 production, arg4 impact_divisor
		# OUTPUT: reg0 = production
		function_economy.good_price_affects_good_production,
		
		#script_get_poorest_village_of_faction
		# INPUT: arg1 = faction_no
		# OUTPUT: reg0 = village_no
		function_faction.get_poorest_village_of_faction,
		
		#script_troop_add_gold
		# INPUT: arg1 = troop_no, arg2 = amount
		# OUTPUT: none
		procedure_troop.troop_add_gold,
		
		#NPC companion changes begin
		# WARNING: heavily modified by 1257AD
		# INPUT: NONE
		# OUTPUT: NONE
		procedure_game_init.initialize_npcs,
		
		#script_objectionable_action
		# WARNING: modified by 1257AD devs
		# NOTE: it is disabled.
		# NPC objection in player party for certain player action such as looting. modded2x: "I might enable this again lmao"
		# INPUT: action_type, action_string
		# OUTPUT : NONE
		procedure_companion.objectionable_action,
		
		#script_post_battle_personality_clash_check
		# NOTE: NPC companion personality clash
		# it is executed after battle. Quite annoying, frankly.
		# it is disabled. to enable it, post_battle_personality_clash_check := 1
		# INPUT: NONE
		# OUTPUT: NONE
		procedure_companion.post_battle_personality_clash_check,
		
		#script_event_player_defeated_enemy_party
		# INPUT: none
		# OUTPUT: none
		procedure_campaign.event_player_defeated_enemy_party,
		
		#script_event_player_captured_as_prisoner
		# INPUT: none
		# OUTPUT: none
		procedure_campaign.event_player_captured_as_prisoner,

		#script_npc_morale
		#NOTE: NPC morale both returns a string and reg0 as the morale value
		# NPC morale both returns a string and reg0 as the morale value
		# INPUT: troop (npc)
		# OUTPUT: that npc morale with string on s21
		function_companion.npc_morale,
		
		
		
		#script_retire_companion
		#NOTE: not sure what is this thing
		# INPUT npc, length (presumably time?)
		procedure_companion.retire_companion,
		
		#NPC companion changes end
		
		#script_reduce_companion_morale_for_clash
		#script_calculate_ransom_amount_for_troop
		# INPUT: arg1 = troop_no for companion1 arg2 = troop_no for companion2 arg3 = slot_for_clash_state
		# slot_for_clash_state means: 1=give full penalty to companion1; 2=give full penalty to companion2; 3=give penalty equally
		procedure_companion.reduce_companion_morale_for_clash,
		
		#Hunting scripts end
		
		#script_calculate_ransom_amount_for_troop
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = troop_no
		# OUTPUT: reg0 = ransom_amount
		function_troop.calculate_ransom_amount_for_troop,
		
		#script_offer_ransom_amount_to_player_for_prisoners_in_party
		# INPUT: arg1 = party_no
		# OUTPUT: reg0 = result (1 = offered, 0 = not offered)
		function_player.offer_ransom_amount_to_player_for_prisoners_in_party,
		
		# script_event_hero_taken_prisoner_by_player
		# Input: arg1 = troop_no
		# Output: none
		procedure_player.event_hero_taken_prisoner_by_player,
		
		# script_cf_check_hero_can_escape_from_player
		# Input: arg1 = troop_no
		# Output: none (can fail)
		cfunction_troop.cf_check_hero_can_escape_from_player,
		
		# script_cf_party_remove_random_regular_troop
		# Input: arg1 = party_no
		# Output: troop_id that has been removed (can fail)
		function_party.cf_party_remove_random_regular_troop,
		
		# script_place_player_banner_near_inventory
		# Input: none
		# Output: none
		procedure_scene.place_player_banner_near_inventory,
		
		# script_place_player_banner_near_inventory_bms
		# Input: none
		# Output: none
		procedure_scene.place_player_banner_near_inventory_bms,

		# script_stay_captive_for_hours
		# WARNING: modified by 1257AD devs
		# Input: arg1 = num_hours
		# Output: none
		procedure_player.stay_captive_for_hours,
		
		# script_set_parties_around_player_ignore_player
		# Input: arg1 = ignore_range, arg2 = num_hours_to_ignore
		# Output: none
		procedure_player.set_parties_around_player_ignore_player,
		
		# script_randomly_make_prisoner_heroes_escape_from_party
		# Input: arg1 = party_no, arg2 = escape_chance_mul_1000
		# Output: none
		procedure_party.randomly_make_prisoner_heroes_escape_from_party,
		
		
		# script_fill_tournament_participants_troop
		# WARNING: heavily modified by 1257AD devs
		# Input: arg1 = center_no, arg2 = player_at_center
		# Output: none (fills trp_tournament_participants)
		procedure_tournament.fill_tournament_participants_troop,
		
		# script_get_num_tournament_participants
		# Input: none
		# Output: reg0 = num_participants
		function_tournament.get_num_tournament_participants,
		
		# script_get_random_tournament_participant
		# Input: none
		# Output: reg0 = troop_no
		function_tournament.get_random_tournament_participant,
		
		# script_add_tournament_participant
		# Input: arg1 = troop_no
		# Output: none
		procedure_tournament.add_tournament_participant,
		
		# script_get_random_tournament_team_amount_and_size
		# Input: none
		# Output: reg0 = number_of_teams, reg1 = team_size
		function_tournament.get_random_tournament_team_amount_and_size,
		
		# script_get_troop_priority_point_for_tournament
		# Input: arg1 = troop_no
		# Output: reg0 = troop_point
		function_tournament.get_troop_priority_point_for_tournament,
		
		# script_sort_tournament_participant_troops
		# Input: none
		# Output: none (sorts trp_tournament_participants)
		procedure_tournament.sort_tournament_participant_troops,
		
		# script_remove_tournament_participants_randomly
		# Input: arg1 = number_to_be_removed
		# Output: none
		procedure_tournament.remove_tournament_participants_randomly,
		
		# script_end_tournament_fight
		# Input: arg1 = player_team_won (1 or 0)
		# Output: none
		procedure_tournament.end_tournament_fight,
		
		
		# script_get_win_amount_for_tournament_bet
		# Input: none
		# Output: reg0 = win_amount_with_100_denars
		function_tournament.get_win_amount_for_tournament_bet,
		
		# script_tournament_place_bet
		# Input: arg1 = bet_amount
		# Output: none
		procedure_tournament.tournament_place_bet,
		
		# script_calculate_amount_of_cattle_can_be_stolen
		# Input: arg1 = village_no
		# Output: reg0 = max_amount
		function_town.calculate_amount_of_cattle_can_be_stolen,
		
		
		# script_draw_banner_to_region
		# Input: arg1 = troop_no, arg2 = center_pos_x, arg3 = center_pos_y, arg4 = width, arg5 = height, arg6 = stretch_width, arg7 = stretch_height, arg8 = default_scale, arg9 = max_charge_scale, arg10 = drawn_item_type
		# drawn_item_type is 0 for banners, 1 for shields, 2 for heater shield, 3 for armor
		# arguments will be used as fixed point values
		# Output: none
		procedure_banner.draw_banner_to_region,
		
		# script_get_troop_custom_banner_num_positionings
		# Input: arg1 = troop_no
		# Output: reg0 = num_positionings
		function_banner.get_troop_custom_banner_num_positionings,
		
		# script_get_custom_banner_charge_type_position_scale_color
		# Input: arg1 = troop_no, arg2 = positioning_index
		# Output: reg0 = type_1
		#         reg1 = scale_1
		#         reg2 = color_1
		#         reg3 = type_2
		#         reg4 = scale_2
		#         reg5 = color_2
		#         reg6 = type_3
		#         reg7 = scale_3
		#         reg8 = color_3
		#         reg9 = type_4
		#         reg10 = scale_4
		#         reg11 = color_4
		function_banner.get_custom_banner_charge_type_position_scale_color,
		
		# script_get_random_custom_banner
		# Input: arg1 = troop_no
		# Output: none
		procedure_banner.get_random_custom_banner,
		
		# script_get_custom_banner_color_from_index
		# Input: arg1 = color_index
		# Output: reg0 = color
		function_banner.get_custom_banner_color_from_index,
		
		# script_cf_check_color_visibility
		# Input: arg1 = color_1, arg2 = color_2
		# Output: none
		cfunction_banner.cf_check_color_visibility,
		
		# script_get_next_active_kingdom
		# Input: arg1 = faction_no
		# Output: reg0 = faction_no (does not choose player faction)
		function_faction.get_next_active_kingdom,
		
		
		# script_remove_cattles_if_herd_is_close_to_party
		# Input: arg1 = party_no, arg2 = maximum_number_of_cattles_required
		# Output: reg0 = number_of_cattles_removed
		function_player.remove_cattles_if_herd_is_close_to_party,
		
		# script_get_rumor_to_s61
		# Input: rumor_id
		# Output: reg0 = 1 if rumor found, 0 otherwise; s61 will contain rumor string if found
		function_helper.get_rumor_to_s61,

		#script_lord_comment_to_s43
		#INPUT: lord troop
		#OUTPUT: reputation strings in s43, reputation in reg0
		function_helper.lord_comment_to_s43,
		
		#Troop Commentaries begin
		
		# script_add_log_entry
		# WARNING: modified by 1257AD
		# Input: arg1 = entry_type, arg2 = event_actor, arg3 = center_object, arg4 = troop_object, arg5 = faction_object
		# Output: none
		procedure_note.add_log_entry,
		
		
		 # script_get_relevant_comment_for_log_entry
		 # WARNING: heavily modified by 1257AD
		# Input: arg1 = log_entry_no, 
		# Output: reg0 = comment_id; reg1 = relevance
		# Notes: 50 is the default relevance.
		# A comment with relevance less than 30 will always be skipped.
		# A comment with relevance 75 or more will never be skipped.
		# A comment with relevance 50 has about 50% chance to be skipped.
		# If there is more than one comment that is not skipped, the system will randomize their relevance values, and then choose the highest one.
		# Also note that the relevance of events decreases as time passes. After three months, relevance reduces to 50%, after 6 months, 25%, etc...
		function_note.get_relevant_comment_for_log_entry,
							
	# script_get_relevant_comment_to_s42
	# Input: none
	# Output: reg0 = 1 if comment found, 0 otherwise; s61 will contain comment string if found
	function_note.get_relevant_comment_to_s42,
		
	#script_merchant_road_info_to_s42
	# WARNING: heavily modified by 1257AD devs
	#INPUT: town
	#OUTPUT: reg0, ":last_bandit_party_found"
	#		 reg1, ":last_bandit_party_origin"
	#	     reg2, ":last_bandit_party_destination"
	#	     reg3, ":last_bandit_party_hours_ago"
	function_town.merchant_road_info_to_s42,

	#script_get_manhunt_information_to_s15
	# WARNING: heavily modified by 1257AD devs
	# INPUT: quest
	# OUTPUT: information string at s15
	function_quest.get_manhunt_information_to_s15,
	
	
	#Troop Commentaries end
	
	#script_rebellion_arguments
	# INPUT: lord, argument, candidate
	# OUTPUT: argument appeal, argument strength
	function_troop.rebellion_arguments,
	
	
	
	#Rebellion changes end
	
	# script_get_culture_with_party_faction_for_music
	# Input: arg1 = party_no
	# Output: reg0 = culture
	function_music.get_culture_with_party_faction_for_music,
	
	# script_get_culture_with_faction_for_music
	# Input: arg1 = party_no
	# Output: reg0 = culture
	function_music.get_culture_with_faction_for_music,
	
	# script_music_set_situation_with_culture
	# Input: arg1 = music_situation
	# Output: none
	procedure_music.music_set_situation_with_culture,
	
	
	# script_combat_music_set_situation_with_culture
	# Input: none
	# Output: none
	procedure_music.combat_music_set_situation_with_culture,
	
	# script_play_victorious_sound
	# Input: none
	# Output: none
	procedure_music.play_victorious_sound,
	
	# script_set_items_for_tournament
	# WARNING: DISABLED by 1257ad devs
	# Input: arg1 = horse_chance, arg2 = lance_chance (with horse only), arg3 = sword_chance, arg4 = axe_chance, arg5 = bow_chance (without horse only), arg6 = javelin_chance (with horse only), arg7 = mounted_bow_chance (with horse only), arg8 = crossbow_sword_chance, arg9 = armor_item_begin, arg10 = helm_item_begin
	# Output: none (sets mt_arena_melee_fight items)
	# ("set_items_for_tournament",
	# [
	# (store_script_param, ":horse_chance", 1),
	# (store_script_param, ":lance_chance", 2),
	# (store_script_param, ":sword_chance", 3),
	# (store_script_param, ":axe_chance", 4),
	# (store_script_param, ":bow_chance", 5),
	# (store_script_param, ":javelin_chance", 6),
	# (store_script_param, ":mounted_bow_chance", 7),
	# (store_script_param, ":crossbow_sword_chance", 8),
	# (store_script_param, ":armor_item_begin", 9),
	# (store_script_param, ":helm_item_begin", 10),
	# (store_add, ":total_chance", ":sword_chance", ":axe_chance"),
	# (val_add, ":total_chance", ":crossbow_sword_chance"),
	# (try_for_range, ":i_ep", 0, 32),
	# (mission_tpl_entry_clear_override_items, "mt_arena_melee_fight", ":i_ep"),
	# (assign, ":has_horse", 0),
	# (store_div, ":cur_team", ":i_ep", 8),
	# (try_begin),
	# (store_random_in_range, ":random_no", 0, 100),
	# (lt, ":random_no", ":horse_chance"),
	# (assign, ":has_horse", 1),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_horse"),
	# (try_end),
	# (try_begin),
	# (eq, ":has_horse", 1),
	# (store_add, ":cur_total_chance", ":total_chance", ":lance_chance"),
	# (val_add, ":cur_total_chance", ":javelin_chance"),
	# (val_add, ":cur_total_chance", ":mounted_bow_chance"),
	# (else_try),
	# (store_add, ":cur_total_chance", ":total_chance", ":bow_chance"),
	# (try_end),
	# (store_random_in_range, ":random_no", 0, ":cur_total_chance"),
	# (store_add, ":cur_shield_item", "itm_arena_shield_red", ":cur_team"),
	# (try_begin),
	# (val_sub, ":random_no", ":sword_chance"),
	# (lt, ":random_no", 0),
	# (try_begin),
	# (store_random_in_range, ":sub_random_no", 0, 100),
	# (lt, ":sub_random_no", 50),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
	# #            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
	# (else_try),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_heavy_practice_sword"),
	# (try_end),
	# (else_try),
	# (val_sub, ":random_no", ":axe_chance"),
	# (lt, ":random_no", 0),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_axe"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
	# #         (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
	# (else_try),
	# (val_sub, ":random_no", ":crossbow_sword_chance"),
	# (lt, ":random_no", 0),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_crossbow"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bolts"),
	# (else_try),
	# (eq, ":has_horse", 0),
	# (val_sub, ":random_no", ":bow_chance"),
	# (lt, ":random_no", 0),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bow"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_arrows"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_dagger"),
	# (else_try),
	# (eq, ":has_horse", 1),
	# (val_sub, ":random_no", ":lance_chance"),
	# (lt, ":random_no", 0),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_lance"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
	# #          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
	# (else_try),
	# (eq, ":has_horse", 1),
	# (val_sub, ":random_no", ":javelin_chance"),
	# (lt, ":random_no", 0),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_javelin"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
	# #          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
	# (else_try),
	# (eq, ":has_horse", 1),
	# (val_sub, ":random_no", ":mounted_bow_chance"),
	# (lt, ":random_no", 0),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bow"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_arrows"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_dagger"),
	# (try_end),
	# (try_begin),
	# (ge, ":armor_item_begin", 0),
	# (store_add, ":cur_armor_item", ":armor_item_begin", ":cur_team"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_armor_item"),
	# (try_end),
	# (try_begin),
	# (ge, ":helm_item_begin", 0),
	# (store_add, ":cur_helm_item", ":helm_item_begin", ":cur_team"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_helm_item"),
	# (try_end),
	# (try_end),
	# ]),
	
	
	# script_custom_battle_end
	# Input: none
	# Output: none
	procedure_game.custom_battle_end,
	

	# script_remove_troop_from_prison
	# Input: troop_no
	# Output: none
	#Other search terms: release, peace
	
	procedure_troop.remove_troop_from_prison,
	
	# script_debug_variables
	# Input: two variables which will be examined by coder, this script is only for debugging.
	# Output: none
	procedure_game.debug_variables,
	
	#script_troop_describes_troop_to_s15
	#INPUT: troop1, troop2
	#OUTPUT: relation string at s15
	#lord recruitment scripts begin
	function_troop.troop_describes_troop_to_s15,
	#script_troop_describes_quarrel_with_troop_to_s14
	#INPUT: troop1, troop2
	#OUTPUT: string describes the quarrel again lords at s14
	function_troop.troop_describes_quarrel_with_troop_to_s14,
	
	#script_cf_test_lord_incompatibility_to_s17
	#INPUT: source_lord, target_lord
	#OUTPUT: none
	cfunction_troop.cf_test_lord_incompatibility_to_s17,
	
	#script_troop_get_romantic_chemistry_with_troop
	#INPUT: source_lady, target_lord
	#OUTPUT: romantic chemistry level at reg0
	#examples :
		#For a charisma of 18, yields (18 - 0) * 2 = 36, (18 - 3) * 2 = 30, (18 - 12) * 2 = 12, (18 - 27) * 2 = -18, (18 - 48) * 2 = -60
		#For a charisma of 10, yields (10 - 0) * 2 = 20, (10 - 3) * 2 = 14, (10 - 12) * 2 = -4, (10 - 27) * 2 = -34, (10 - 48) * 2 = -76
		#For a charisma of 7, yields  (7 - 0) * 2 = 14,  (7 - 3) * 2 = 8,   (7 - 12) * 2 = -10, (7 - 27) * 2 = -40,  (7 - 48) * 2 = -82
		
		#15 is high attraction, 0 is moderate attraction, -76 is lowest attraction
	function_troop.troop_get_romantic_chemistry_with_troop,
	
	
	#cf_troop_get_romantic_attraction_to_troop
	#INPUT: source_lady, target_lord
	#OUTPUT: weighted_romantic_assessment at reg0
	function_troop.cf_troop_get_romantic_attraction_to_troop,
	
	#script_cf_random_political_event
	# random politics triggers between lords, probably called from triggers
	#INPUT: NONE
	#OUTPUT: NONE
	procedure_campaign_simulation.cf_random_political_event,
	
	#script_evaluate_realm_stability
	#NOTE: this calculates the average number of rivalries per lord, giving a rough indication of how easily a faction may be divided
	#	   fairly expensive in terms of CPU
	#INPUT: realm 
	#OUTPUT: none
	procedure_faction.evaluate_realm_stability,
	
	
	
	#lord recruitment scripts end

	#script_battle_political_consequences
	#called from game_event_simulate_battle
	#Includes a number of consequences that follow on battles, mostly affecting relations between different NPCs
	#This only fires from complete victories
	#INPUT: defeated_party, winner_party
	#OUTPUT: none
	
	procedure_campaign_simulation.battle_political_consequences,
	
	#script_faction_inflict_war_damage_on_faction
	#INPUT: actor faction, target faction, amount
	#OUTPUT: none
	procedure_campaign_simulation.faction_inflict_war_damage_on_faction,
	

	#script_calculate_troop_political_factors_for_liege
	#INPUT: troop, liege
	#OUTPUT: that result whatever on reg0
	function_troop.calculate_troop_political_factors_for_liege,
	
	#script_cf_troop_can_intrigue
	#INPUT: troop, skip_player_party
	#OUTPUT: none
	#This script should be called from dialogs, and also prior to any event which might result in a lord changing sides
	cfunction_troop.cf_troop_can_intrigue,
	
	#script_troop_change_relation_with_troop
	#INPUT: troop1, troop2, amount
	#OUTPUT: none
	procedure_troop.troop_change_relation_with_troop,
	
	#script_troop_change_relation_with_troop
	#INPUT: troop1, troop2
	#OUTPUT: relation amount at reg0
	function_troop.troop_get_relation_with_troop,
	
	
	#script_appoint_faction_marshall
	#INPUT: faction_no, faction_marshall
	#OUTPUT: NONE
	procedure_faction.appoint_faction_marshall,

	#script_center_get_item_consumption
	#STUB SCRIPT
	#it might be easier to monitor whether prices are following an intuitive pattern if we separate production from consumption
	#the current system still works very well, however
	("center_get_item_consumption",
		[
	]),
	
	#script_locate_player_minister
	# call this procedure to display where is player's minister located
	#INPUT: none
	#OUTPUT: none
	procedure_player.locate_player_minister,
	
	("lord_get_home_center",
		[
		(store_script_param, ":troop_no", 1),
		(assign, ":result", -1),
		
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(eq, ":result", -1),
			(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
			(assign, ":result", ":center_no"),
		(try_end),
		
		#NOTE : In old code if a lord has no walled center then home city of this lord is assigning to
		#faction leader's home city. Now I changed this to assign home cities more logical and homogeneous.
		#In new code if a lord has no walled center then his home city becomes his village's border_city.
		#This means his home city becomes owner city of his village. If he has no village then as last change
		#his home city become faction leader's home city.
		(try_begin),
			(eq, ":result", -1),
			(try_for_range, ":center_no", centers_begin, centers_end),
			(eq, ":result", -1),
			(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
			
			(try_begin),
				(neg|is_between, ":center_no", walled_centers_begin, walled_centers_end),
				(party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
				(assign, ":result", ":bound_center"),
			(try_end),
			(try_end),
		(try_end),
		#If lord has no walled center and is player faction, then assign player court
		(try_begin),
			(eq, ":result", -1),
			(store_faction_of_troop, ":faction_no", ":troop_no"),
			(eq, ":faction_no", "fac_player_supporters_faction"),
			(is_between, "$g_player_court", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":player_court_faction", "$g_player_court"),
			(eq, ":player_court_faction", "fac_player_supporters_faction"),
			
			(assign, ":result", "$g_player_court"),
		(try_end),
		
		#If lord has no walled center and any not walled village then assign faction capital
		(try_begin),
			(eq, ":result", -1),
			(store_faction_of_troop, ":faction_no", ":troop_no"),
			(faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
			(neq, ":troop_no", ":faction_leader"),
			(call_script, "script_lord_get_home_center", ":faction_leader"),
			(gt, reg0, -1),
			(assign, ":result", reg0),
		(try_end),
		
		#Any center of the faction
		(try_begin),
			(eq, ":result", -1),
			(store_faction_of_troop, ":faction_no", ":troop_no"),
			
			(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(eq, ":result", -1),
			
			(store_faction_of_party, ":center_faction", ":walled_center"),
			(eq, ":faction_no", ":center_faction"),
			(assign, ":result", ":walled_center"),
			(try_end),
		(try_end),
		
		
		
		(assign, reg0, ":result"),
	]),
	
	
	
	
	("get_kingdom_lady_social_determinants", #Calradian society is rather patriarchal, at least among the upper classes
		[
		(store_script_param, ":kingdom_lady", 1),
		
		(store_faction_of_troop, ":faction_of_lady", ":kingdom_lady"),
		(assign, ":center", -1),
		(assign, ":closest_male_relative", -1),
		(assign, ":best_center_score", 0),
		
		(try_begin),
			(troop_slot_ge, ":kingdom_lady", slot_troop_spouse, 0),
			(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_spouse),
		(else_try),
			(troop_slot_ge, ":kingdom_lady", slot_troop_father, 0),
			(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_father),
		(else_try),
			(troop_slot_ge, ":kingdom_lady", slot_troop_guardian, 0),
			(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_guardian),
		(try_end),
		
		
		(try_begin), #if ongoing social event (maybe add if not besieged)
			(faction_slot_eq, ":faction_of_lady", slot_faction_ai_state, sfai_feast),
			(faction_get_slot, ":feast_center", ":faction_of_lady", slot_faction_ai_object),
			
			(gt, ":closest_male_relative", -1),
			(troop_get_slot, ":closest_male_party", ":closest_male_relative", slot_troop_leaded_party),
			(party_is_active, ":closest_male_party"),
			(party_get_attached_to, ":closest_male_cur_location", ":closest_male_party"),
			
			(eq, ":closest_male_cur_location", ":feast_center"),
			(is_between, ":feast_center", walled_centers_begin, walled_centers_end),
			
			(assign, ":center", ":feast_center"),
			
		(else_try),
			(troop_slot_eq, "trp_player", slot_troop_spouse, ":kingdom_lady"),
			###diplomacy begin
			(try_begin),
			##diplomacy end
			(is_between, "$g_player_court", walled_centers_begin, walled_centers_end),
			##diplomacy begin
			(else_try),
			(troop_get_slot, ":cur_residence", ":kingdom_lady", slot_troop_cur_center),
			(is_between, ":cur_residence", walled_centers_begin, walled_centers_end),
			(party_slot_eq, ":cur_residence", slot_town_lord, "trp_player"),
			(assign, ":center", ":cur_residence"),
			(try_end),
			(is_between, ":center",  walled_centers_begin, walled_centers_end),
			##diplomacy end
		(else_try),
			(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":walled_center_faction", ":walled_center"),
			(this_or_next|eq, ":faction_of_lady", ":walled_center_faction"),
			(neg|is_between, ":faction_of_lady", kingdoms_begin, kingdoms_end), #lady married to a player without a faction
			
			(party_get_slot, ":castle_lord", ":walled_center", slot_town_lord),
			
			(gt, ":castle_lord", -1),
			
			(call_script, "script_troop_get_family_relation_to_troop", ":kingdom_lady", ":castle_lord"),
			
			(try_begin),
				(this_or_next|is_between, ":faction_of_lady", kingdoms_begin, kingdoms_end),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":kingdom_lady"),
				
				(faction_slot_eq, ":faction_of_lady", slot_faction_leader, ":castle_lord"),
				(val_max, reg0, 1),
			(try_end),
			
			(try_begin),
				(eq, "$cheat_mode", 2),
				(str_store_troop_name, s3, ":kingdom_lady"),
				(str_store_troop_name, s4, ":castle_lord"),
				(str_store_party_name, s5, ":walled_center"),
				(display_message, "str_checking_s3_at_s5_with_s11_relationship_with_s4_score_reg0"),
				(str_clear, s11),
			(try_end),
			
			(gt, reg0, ":best_center_score"),
			
			(assign, ":best_center_score", reg0),
			(assign, ":center", ":walled_center"),
			
			
			(try_end),
		(try_end),
		
		(assign, reg0, ":closest_male_relative"),
		(assign, reg1, ":center"),
		
		
	]),
	
	
	#This is probably unnecessarily complicated, but can support a multi-generational mod
	("age_troop_one_year",
		[
		(store_script_param, ":troop_no", 1),
		
		(troop_get_type, ":is_female", ":troop_no"),
		
		(troop_get_slot, ":age", ":troop_no", slot_troop_age),
		(troop_get_slot, ":appearance", ":troop_no", slot_troop_age_appearance),
		
		(val_add, ":age", 1),
		(store_random_in_range, ":addition", 1, 5),
		
		(try_begin),
			(eq, ":is_female", 1),
			#		(val_add, ":addition", 2), #the women's age slider seems to produce less change than the male one - commented out: makes women look too old.
		(try_end),
		
		(val_add, ":appearance", ":addition"),
		(try_begin),
			(gt, ":age", 45),
			(store_attribute_level, ":strength", ":troop_no", ca_strength),
			(store_attribute_level, ":agility", ":troop_no", ca_agility),
			(store_random_in_range, ":random", 0, 50), #2% loss brings it down to about 36% by age 90, but of course can be counteracted by new level gain
			(try_begin),
			(lt, ":random", ":strength"),
			(troop_raise_attribute, ":troop_no", ca_strength, -1),
			(try_end),
			(try_begin),
			(lt, ":random", ":agility"),
			(troop_raise_attribute, ":troop_no", ca_agility, -1),
			(try_end),
		(try_end),
		
		(val_clamp, ":appearance", 1, 100),
		
		(troop_set_slot, ":troop_no", slot_troop_age, ":age"),
		(troop_set_slot, ":troop_no", slot_troop_age_appearance, ":appearance"),
		(troop_set_age, ":troop_no", ":appearance"),
	]),
	
	
	("add_lady_items",
		[
		(store_script_param, ":lady_no", 1),
		#(troop_equip_items, ":lady_no"),
		
		(try_for_range, ":item", "itm_tutorial_spear", "itm_items_end"),
			(troop_remove_item, ":lady_no", ":item"),
		(try_end),
		#(troop_clear_inventory, ":lady_no"),
		
		
		(store_faction_of_troop, ":faction_no", ":lady_no"),
		
		(call_script, "script_raf_aor_faction_to_region", ":faction_no"),
		#(store_random_in_range, ":random", 0, 6),

		(try_begin),
			(eq, reg0, region_mongol),
			(store_random_in_range, ":dress", "itm_khergit_lady_dress", "itm_sarranid_lady_dress"),
			(troop_add_item, ":lady_no", ":dress", 0),
		(else_try),
			(this_or_next | eq, reg0, region_andalusian),
			(this_or_next | eq, reg0, region_north_african),
			(eq, reg0, region_mamluk),
			(store_random_in_range, ":dress", "itm_sarranid_lady_dress", "itm_sarranid_common_dress"),
			(troop_add_item, ":lady_no", ":dress", 0),
		(else_try),
			(store_random_in_range, ":dress", "itm_red_dress", "itm_khergit_lady_dress"),
			(troop_add_item, ":lady_no", ":dress", 0),
		(try_end),
		(troop_add_item, ":lady_no", "itm_blue_hose", 0),
		(troop_equip_items, ":lady_no"),
		
		#(store_random_in_range, ":random", 0, 2),
		
		(try_begin),
			#(eq, ":random", 1),
			(try_begin),
			# (troop_has_item_equipped, ":lady_no", "itm_khergit_lady_dress"),
			# (troop_add_item, ":lady_no", "itm_khergit_lady_hat", 0),
			# (else_try),
			(this_or_next|troop_has_item_equipped, ":lady_no", "itm_red_dress"),
			(this_or_next|troop_has_item_equipped, ":lady_no", "itm_brown_dress"),
			(troop_has_item_equipped, ":lady_no", "itm_green_dress"),
			(store_random_in_range, ":item", "itm_turret_hat_green", "itm_straw_hat"),
			(troop_add_item, ":lady_no", ":item", 0),
			# (else_try),
			# (troop_has_item_equipped, ":lady_no", "itm_khergit_lady_dress_b"),
			# (troop_add_item, ":lady_no", "itm_khergit_lady_hat_b", 0),
			(else_try),
			(troop_has_item_equipped, ":lady_no", "itm_sarranid_lady_dress"),
			(troop_add_item, ":lady_no", "itm_sarranid_head_cloth", 0),
			(else_try),
			(troop_has_item_equipped, ":lady_no", "itm_sarranid_lady_dress_b"),
			(troop_add_item, ":lady_no", "itm_sarranid_head_cloth_b", 0),
			(try_end),
			(troop_equip_items, ":lady_no"),
		(try_end),
		]
	),
	
	("init_troop_age",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":age", 2), #minimum 20
		
		(try_begin),
			(gt, ":age", 20),
			(troop_set_slot, ":troop_no", slot_troop_age, 20),
		(else_try),
			(troop_set_slot, ":troop_no", slot_troop_age, ":age"),
		(try_end),
		
		(store_sub, ":years_to_age", ":age", 20),
		(troop_set_age, ":troop_no", 0),
		
		(try_begin),
			(gt, ":years_to_age", 0),
			(try_for_range, ":unused", 0, ":years_to_age"),
			(call_script, "script_age_troop_one_year", ":troop_no"),
			(try_end),
		(try_end),
		
	]),
	
	
	("assign_troop_love_interests", #Called at the beginning, or whenever a lord is spurned
		[
		(store_script_param, ":cur_troop", 1),
		
		(store_faction_of_troop, ":troop_faction", ":cur_troop"),
		(try_for_range, ":unused", 0, 50),
			(store_random_in_range, ":cur_lady", kingdom_ladies_begin, kingdom_ladies_end),
			(troop_slot_eq, ":cur_lady", slot_troop_spouse, -1),
			(store_faction_of_troop, ":lady_faction", ":cur_lady"),
			(eq, ":troop_faction", ":lady_faction"),
			(call_script, "script_troop_get_family_relation_to_troop", ":cur_troop", ":cur_lady"),
			(eq, reg0, 0),
			
			(call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":cur_lady"),
			(eq, reg0, 0), #do not develop love interest if already spurned or courted
			
			(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, ":cur_lady"),
			(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, ":cur_lady"),
			(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, ":cur_lady"),
			(try_begin),
			(troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, 0),
			(troop_set_slot, ":cur_troop", slot_troop_love_interest_1, ":cur_lady"),
			(else_try),
			(troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, 0),
			(troop_set_slot, ":cur_troop", slot_troop_love_interest_2, ":cur_lady"),
			(else_try),
			(troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, 0),
			(troop_set_slot, ":cur_troop", slot_troop_love_interest_3, ":cur_lady"),
			(try_end),
		(try_end),
		
	]),
	
	("faction_conclude_feast",
		[
		(store_script_param, ":faction_no", 1),
		(store_script_param, ":venue", 2),
		
		(str_store_faction_name, s3, ":faction_no"),
		(str_store_party_name, s4, ":venue"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_s3_feast_concludes_at_s4"),
		(try_end),
		
		(try_begin),
			(eq, ":faction_no", "fac_player_faction"),
			(assign, ":faction_no", "$players_kingdom"),
		(try_end),
		
		(party_set_slot, ":venue", slot_town_has_tournament, 0),
		
		#markspot
		
		(assign, ":nobility_in_faction", 0),
		(assign, ":nobility_in_attendance", 0),
		
		(try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
			(store_faction_of_troop, ":troop_faction", ":troop_no"),
			(eq, ":faction_no", ":troop_faction"),
			
			(val_add, ":nobility_in_faction", 1),
			
			#CHECK -- is the troop there?
			(troop_slot_eq, ":troop_no", slot_troop_cur_center, ":venue"),
			(val_add, ":nobility_in_attendance", 1),
			
			#check for marriages
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
			(troop_get_slot, ":groom", ":troop_no", slot_troop_betrothed),
			(gt, ":groom", 0),
			
			(troop_get_slot, ":groom_party", ":groom", slot_troop_leaded_party),
			(party_is_active, ":groom_party"),
			(party_get_attached_to, ":groom_party_attached", ":groom_party"),
			(eq, ":groom_party_attached", ":venue"),
			
			(store_faction_of_troop, ":lady_faction", ":troop_no"),
			(store_faction_of_troop, ":groom_faction", ":groom"),
			
			(eq, ":groom_faction", ":lady_faction"),
			(eq, ":lady_faction", ":faction_no"),
			(store_current_hours, ":hours_since_betrothal"),
			(troop_get_slot, ":betrothal_time", ":troop_no", slot_troop_betrothal_time),
			(val_sub, ":hours_since_betrothal", ":betrothal_time"),
			(ge, ":hours_since_betrothal", 144), #6 days, should perhaps eventually be 29 days, or 696 yours
			
			(call_script, "script_get_kingdom_lady_social_determinants", ":troop_no"),
			(assign, ":wedding_venue", reg1),
			
			(eq, ":venue", ":wedding_venue"),
			(neq, ":troop_no", "trp_player"),
			(neq, ":groom", "trp_player"),
			
			(call_script, "script_courtship_event_bride_marry_groom", ":troop_no", ":groom", 0), #parameters from dialog
		(try_end),
		
		
		#ssss	(assign, ":placeholder_reminder_to_calculate_effect_for_player_feast", 1),
		
		
		
		(party_get_slot, ":feast_host", ":venue", slot_town_lord),
		(assign, ":quality_of_feast", 0),
		
		(try_begin),
			(check_quest_active, "qst_organize_feast"),
			(quest_slot_eq, "qst_organize_feast", slot_quest_target_center, ":venue"),
			(assign, ":feast_host", "trp_player"),
			
			(assign, ":total_guests", 400),
			
			(call_script, "script_succeed_quest", "qst_organize_feast"),
			(call_script, "script_end_quest", "qst_organize_feast"),
			
			(call_script, "script_internal_politics_rate_feast_to_s9", "trp_household_possessions", ":total_guests", "$players_kingdom", 1),
			(assign, ":quality_of_feast", reg0),
		(else_try),
			(assign, ":quality_of_feast", 60),
		(try_end),
		
		
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":feast_host"),
			(assign, reg4, ":quality_of_feast"),
			(display_message, "@{!}DEBUG - {s4}'s feast has rating of {reg4}"),
		(try_end),
		
		
		(try_begin),
			(ge, ":feast_host", 0),
			(store_div, ":renown_boost", ":quality_of_feast", 3),
			(call_script, "script_change_troop_renown", ":feast_host", ":renown_boost"),
			
			(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
			(party_is_active, ":leaded_party"),
			(party_get_attached_to, ":leaded_party_attached", ":leaded_party"),
			(eq, ":leaded_party_attached", ":venue"),
			
			(assign, ":relation_booster", ":quality_of_feast"),
			(val_div, ":relation_booster", 20),
			
			(try_begin),
				(eq, ":feast_host", "trp_player"),
				(val_sub, ":relation_booster", 1),
				(val_max, ":relation_booster", 0),
			(try_end),
			(call_script, "script_troop_change_relation_with_troop", ":feast_host", ":troop_no", ":relation_booster"),
			(val_add, "$total_feast_changes", ":relation_booster"),
			(try_end),
		(try_end),
		
		
		(assign, reg3, ":nobility_in_attendance"),
		(assign, reg4, ":nobility_in_faction"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_attendance_reg3_nobles_out_of_reg4"),
		(try_end),
	]),
	
	("lady_evaluate_troop_as_suitor",
		[
		(store_script_param, ":lady", 1),
		(store_script_param, ":suitor", 2),
		
		(call_script, "script_troop_get_romantic_chemistry_with_troop", ":lady", ":suitor"),
		(assign, ":romantic_chemistry", reg0),
		
		(try_begin),
			(call_script, "script_cf_test_lord_incompatibility_to_s17", ":lady", ":suitor"),
		(try_end),
		
		(store_sub, ":personality_modifier", 0, reg0),
		(assign, reg2, ":personality_modifier"),
		
		(try_begin),
			(troop_get_slot, ":renown_modifier", ":suitor", slot_troop_renown),
			(val_div, ":renown_modifier", 20),
			(try_begin),
			(this_or_next|troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_conventional),
			(troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_ambitious),
			(val_mul, ":renown_modifier", 2),
			(val_sub, ":renown_modifier", 15),
			(try_end),
		(try_end),
		
		(store_add, ":final_score", ":renown_modifier", ":personality_modifier"),
		(val_add, ":final_score", ":romantic_chemistry"),
		(assign, reg0, ":final_score"),
	]),
	
	("courtship_event_troop_court_lady",
		[
		(store_script_param, ":suitor", 1),
		(store_script_param, ":lady", 2),
		
		
		#(try_begin),
		#(eq, "$cheat_mode", 1),
		#(str_store_troop_name, s4, ":suitor"),
		#(str_store_troop_name, s5, ":lady"),
		#(troop_get_slot, ":lady_location", ":lady", slot_troop_cur_center),
		#(str_store_party_name, s7, ":lady_location"),
		#(display_message, "str_s4_pursues_suit_with_s5_in_s7"),
		#(try_end),
		
		(troop_get_slot, ":previous_suitor", ":lady", slot_lady_last_suitor),
		(troop_set_slot, ":lady", slot_lady_last_suitor, ":suitor"), #can determine quarrels
		
		(try_begin),
			(eq, ":previous_suitor", "trp_player"),
			
			(troop_slot_ge, ":lady", slot_troop_met, 2),
			(call_script, "script_troop_get_relation_with_troop", ":suitor", "trp_player"), #add this to list of quarrels
			(assign, ":suitor_relation_w_player", reg0),
			
			(try_begin),
			(this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_selfrighteous),
			(this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_quarrelsome),
			(troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_debauched),
			(gt, ":suitor_relation_w_player", -20),
			(call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", "trp_player", ":lady", 0),
			(else_try),
			(is_between, ":suitor_relation_w_player", -5, -25),
			(call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", "trp_player", ":lady", 0),
			(try_end),
		(else_try),
			(neq, ":previous_suitor", "trp_player"), #not the player
			
			(neq, ":suitor", ":previous_suitor"),
			(ge, ":previous_suitor", active_npcs_begin),
			
			(call_script, "script_cf_test_lord_incompatibility_to_s17", ":suitor", ":previous_suitor"),
			(call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", ":previous_suitor", ":lady", 0),
			
			(call_script, "script_troop_get_relation_with_troop", ":suitor", ":previous_suitor"), #add this to list of quarrels
			(ge, reg0, 0),
			(call_script, "script_troop_change_relation_with_troop", ":suitor", ":previous_suitor", -20),
			(val_add, "$total_courtship_quarrel_changes", -20),
		(else_try),	 #quarrelsome lords quarrel anyway
			(troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_quarrelsome),
			(neq, ":suitor", ":previous_suitor"),
			(ge, ":previous_suitor", active_npcs_begin),
			
			#		(neq, ":previous_suitor", "trp_player"),
			
			(call_script, "script_troop_get_relation_with_troop", ":suitor", ":previous_suitor"), #add this to list of quarrels
			(lt, reg0, 10),
			(call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", ":previous_suitor", ":lady", 0),
			(ge, reg0, 0),
			(call_script, "script_troop_change_relation_with_troop", ":suitor", ":previous_suitor", -20),
			(val_add, "$total_courtship_quarrel_changes", -20),
			
		(try_end),
		
		
		#	(call_script, "script_troop_get_relation_with_troop", ":lady", ":suitor"),
		#	(assign, ":orig_relation", reg0),
		
		(call_script, "script_lady_evaluate_troop_as_suitor", ":lady", ":suitor"),
		
		(store_random_in_range, ":random", 5, 16),
		(store_div, ":relationship_change", reg0, ":random"),
		
		(call_script, "script_troop_get_relation_with_troop", ":lady", ":suitor"),
		(assign, ":orig_relation", reg0),
		
		(call_script, "script_troop_change_relation_with_troop", ":lady", ":suitor", ":relationship_change"),
		
		(call_script, "script_troop_get_relation_with_troop", ":lady", ":suitor"),
		(assign, ":lady_suitor_relation", reg0),
		
		(try_begin),
			(ge, ":lady_suitor_relation", 10),
			(lt, ":orig_relation", 10),
			(call_script, "script_add_log_entry", logent_lady_favors_suitor, ":lady", 0, ":suitor", 0),
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_note__favor_event_logged"),
			(try_end),
			
		(else_try),
			(this_or_next|lt, ":lady_suitor_relation", -20),
			(ge, ":lady_suitor_relation", 20),
			
			(call_script, "script_get_kingdom_lady_social_determinants", ":lady"),
			(assign, ":guardian", reg0),
			(ge, ":guardian", 0),  #tom - to prevent future errors
			(call_script, "script_troop_get_relation_with_troop", ":suitor", ":guardian"),
			(assign, ":suitor_guardian_relation", reg0),
			#things come to a head, one way or another
			
			(assign, ":highest_competitor_lady_score", -1),
			(assign, ":competitor_preferred_by_lady", -1),
			
			(assign, ":highest_competitor_guardian_score", ":suitor_guardian_relation"),
			(assign, ":competitor_preferred_by_guardian", -1),
			
			#log potential competitors
			(try_for_range, ":possible_competitor", lords_begin, lords_end),
			(neq, ":possible_competitor", ":suitor"),
			
			(this_or_next|troop_slot_eq, ":possible_competitor", slot_troop_love_interest_1, ":lady"),
			(this_or_next|troop_slot_eq, ":possible_competitor", slot_troop_love_interest_2, ":lady"),
			(troop_slot_eq, ":possible_competitor", slot_troop_love_interest_3, ":lady"),
			
			(try_begin),
				(call_script, "script_troop_get_relation_with_troop", ":possible_competitor", ":lady"),
				(gt, reg0, ":highest_competitor_lady_score"),
				(assign, ":competitor_preferred_by_lady", ":possible_competitor"),
				(assign, ":highest_competitor_lady_score", reg0),
			(try_end),
			
			(try_begin),
				(call_script, "script_troop_get_relation_with_troop", ":possible_competitor", ":guardian"),
				(gt, reg0, ":highest_competitor_guardian_score"),
				(assign, ":competitor_preferred_by_guardian", ":possible_competitor"),
				(assign, ":highest_competitor_guardian_score", reg0),
			(try_end),
			(try_end),
			
			#RESULTS
			#Guardian forces lady to be betrothed to suitor now
			(try_begin),
			(lt, ":lady_suitor_relation", -20),
			(this_or_next|troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_selfrighteous),
			(this_or_next|troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_debauched),
			(troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_quarrelsome),
			(eq, ":competitor_preferred_by_guardian", -1),
			
			(this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_selfrighteous),
			(this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_debauched),
			(troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_quarrelsome),
			
			(troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
			(troop_slot_eq, ":lady", slot_troop_betrothed, -1),
			
			(call_script, "script_add_log_entry", logent_lady_betrothed_to_suitor_by_family, ":lady", 0, ":suitor", 0),
			(troop_set_slot, ":suitor", slot_troop_betrothed, ":lady"),
			(troop_set_slot, ":lady", slot_troop_betrothed, ":suitor"),
			(store_current_hours, ":hours"),
			(troop_set_slot, ":lady", slot_troop_betrothal_time, ":hours"),
			(troop_set_slot, ":suitor", slot_troop_betrothal_time, ":hours"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(display_message, "str_result_lady_forced_to_agree_to_engagement"),
			(try_end),
			
			#Lady rejects the suitor
			(else_try),
			(lt, ":lady_suitor_relation", -20),
			
			(call_script, "script_add_log_entry", logent_lady_rejects_suitor, ":lady", 0, ":suitor", 0),
			(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":lady", ":suitor"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(display_message, "str_result_lady_rejects_suitor"),
			(try_end),
			
			#A happy engagement, with parental blessing
			(else_try),
			(gt, ":lady_suitor_relation", 20),
			(gt, ":suitor_guardian_relation", 0),
			(eq, ":competitor_preferred_by_lady", -1),
			
			(troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
			(troop_slot_eq, ":lady", slot_troop_betrothed, -1),
			
			(call_script, "script_add_log_entry", logent_lady_betrothed_to_suitor_by_choice, ":lady", 0, ":suitor", 0),
			(troop_set_slot, ":suitor", slot_troop_betrothed, ":lady"),
			(troop_set_slot, ":lady", slot_troop_betrothed, ":suitor"),
			(store_current_hours, ":hours"),
			(troop_set_slot, ":lady", slot_troop_betrothal_time, ":hours"),
			(troop_set_slot, ":suitor", slot_troop_betrothal_time, ":hours"),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":lady"),
				(str_store_troop_name, s5, ":suitor"),
				(display_message, "str_result_happy_engagement_between_s4_and_s5"),
			(try_end),
			
			#Lady elopes
			(else_try),
			(gt, ":lady_suitor_relation", 20),
			
			(eq, ":competitor_preferred_by_lady", -1),
			(this_or_next|troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_adventurous),
			(troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_ambitious),
			
			(troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
			(troop_slot_eq, ":lady", slot_troop_betrothed, -1),
			
			#lady elopes
			(call_script, "script_courtship_event_bride_marry_groom", ":lady", ":suitor", 1),
			#add elopements to quarrel descriptions
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":lady"),
				(str_store_troop_name, s5, ":suitor"),
				(display_message, "str_result_s4_elopes_with_s5"),
			(try_end),
			
			#Lady reluctantly agrees to marry under pressure from family
			(else_try),
			(troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_conventional),
			(eq, ":competitor_preferred_by_guardian", -1),
			(gt, ":suitor_guardian_relation", 4),
			
			(store_random_in_range, ":random", 0, 5),
			(eq, ":random", 0),
			
			(troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
			(troop_slot_eq, ":lady", slot_troop_betrothed, -1),
			
			(call_script, "script_add_log_entry", logent_lady_betrothed_to_suitor_by_pressure, ":lady", 0, ":suitor", 0),
			(troop_set_slot, ":suitor", slot_troop_betrothed, ":lady"),
			(troop_set_slot, ":lady", slot_troop_betrothed, ":suitor"),
			(store_current_hours, ":hours"),
			(troop_set_slot, ":lady", slot_troop_betrothal_time, ":hours"),
			(troop_set_slot, ":suitor", slot_troop_betrothal_time, ":hours"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":lady"),
				(str_store_troop_name, s5, ":suitor"),
				(display_message, "str_result_s4_reluctantly_agrees_to_engagement_with_s5"),
			(try_end),
			
			#Stalemate -- make patience roll
			(else_try),
			(gt, ":lady_suitor_relation", 20),
			
			(store_random_in_range, reg3, 0, 3),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(display_message, "str_result_stalemate_patience_roll_=_reg3"),
			(try_end),
			
			(eq, reg3, 0),
			(call_script, "script_add_log_entry", logent_lady_rejected_by_suitor, ":lady", 0, ":suitor", 0),
			(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":lady", ":suitor"),
			(try_end),
			
		(try_end),
		
	]),
	
	
	
	("courtship_event_lady_break_relation_with_suitor", #parameters from dialog
		[
		(store_script_param, ":lady", 1),
		(store_script_param, ":suitor", 2),
		
		(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_slot_eq, ":suitor", ":love_interest_slot", ":lady"),
			(troop_set_slot, ":suitor", ":love_interest_slot", 0),
		(try_end),
		(call_script, "script_assign_troop_love_interests", ":suitor"),
		
		(try_begin),
			(troop_slot_eq, ":lady", slot_troop_betrothed, ":suitor"),
			
			
			(troop_set_slot, ":lady", slot_troop_betrothed, -1),
			(troop_set_slot, ":suitor", slot_troop_betrothed, -1),
		(try_end),
		
		
	]),
	
	
	("courtship_event_bride_marry_groom", #parameters from dialog or scripts
		[
		(store_script_param, ":bride", 1),
		(store_script_param, ":groom", 2),
		(store_script_param, ":elopement", 3),
		
		(try_begin),
			(eq, ":bride", "trp_player"),
			(assign, ":venue", "$g_encountered_party"),
		(else_try),
			(troop_get_slot, ":venue", ":bride", slot_troop_cur_center),
		(try_end),
		
		(store_faction_of_troop, ":groom_faction", ":groom"),
		
		
		(try_begin),
			(eq, ":elopement", 0),
			(call_script, "script_add_log_entry", logent_lady_marries_suitor, ":bride", ":venue", ":groom", 0),
		(else_try),
			(call_script, "script_add_log_entry", logent_lady_elopes_with_lord, ":bride", ":venue", ":groom", 0),
		(try_end),
		
		(str_store_troop_name, s3, ":bride"),
		(str_store_troop_name, s4, ":groom"),
		(str_store_party_name, s5, ":venue"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_s3_marries_s4_at_s5"),
		(try_end),
		
		(troop_set_slot, ":bride", slot_troop_spouse, ":groom"),
		(troop_set_slot, ":groom", slot_troop_spouse, ":bride"),
		
		#Break groom's romantic relations
		(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_set_slot, ":groom", ":love_interest_slot", 0),
		(try_end),
		
		#Break bride's romantic relations
		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_slot_eq, ":active_npc", ":love_interest_slot", ":bride"),
			(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":bride", ":active_npc"),
			(try_end),
		(try_end),
		
		
		
		(troop_set_slot, ":bride", slot_troop_betrothed, -1),
		(troop_set_slot, ":groom", slot_troop_betrothed, -1),
		
		
		
		#change relations with family
		(try_for_range, ":family_member", lords_begin, lords_end),
			(call_script, "script_troop_get_family_relation_to_troop", ":bride", ":family_member"),
			(gt, reg0, 0),
			(store_div, ":family_relation_boost", reg0, 3),
			(try_begin),
			(eq, ":elopement", 1),
			(val_mul, ":family_relation_boost", -2),
			(try_end),
			(call_script, "script_troop_change_relation_with_troop", ":groom", ":bride", ":family_relation_boost"),
			(val_add, "$total_courtship_quarrel_changes", ":family_relation_boost"),
		(try_end),
		
		(try_begin),
			(this_or_next|eq, ":groom", "trp_player"),
			(eq, ":bride", "trp_player"),
			(call_script, "script_change_player_right_to_rule", "trp_player", 15),
		(try_end),
		
		
		(try_begin),
			(eq, ":groom", "trp_player"),
			(check_quest_active, "qst_wed_betrothed"),
			(call_script, "script_succeed_quest", "qst_wed_betrothed"),
			(call_script, "script_end_quest", "qst_wed_betrothed"),
		(try_end),
		
		
		(try_begin),
			(check_quest_active, "qst_visit_lady"),
			(quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, ":bride"),
			(call_script, "script_abort_quest", "qst_visit_lady", 0),
		(try_end),
		
		
		(try_begin),
			(eq, ":groom", "trp_player"),
			(check_quest_active, "qst_visit_lady"),
			(call_script, "script_abort_quest", "qst_visit_lady", 0),
		(try_end),
		(try_begin),
			(eq, ":groom", "trp_player"),
			(check_quest_active, "qst_duel_courtship_rival"),
			(call_script, "script_abort_quest", "qst_duel_courtship_rival", 0),
		(try_end),
		
		
		(try_begin),
			(eq, ":bride", "trp_player"),
			(call_script, "script_player_join_faction", ":groom_faction"),
			(assign, "$player_has_homage", 1),
		(else_try),
			(eq, ":groom", "trp_player"),
			(troop_set_faction, ":bride", "$players_kingdom"),
		(else_try),
			(troop_set_faction, ":bride", ":groom_faction"),
		(try_end),
		
		(try_begin),
			(this_or_next|eq, ":groom", "trp_player"),
			(eq, ":bride", "trp_player"),
			(unlock_achievement, ACHIEVEMENT_HAPPILY_EVER_AFTER),
			(try_begin),
			(eq, ":elopement", 1),
			(unlock_achievement, ACHIEVEMENT_HEART_BREAKER),
			(try_end),
		(try_end),
		
		
		
		(try_begin),
			(this_or_next|eq, ":groom", "trp_player"),
			(eq, ":bride", "trp_player"),
			#(eq, ":elopement", 0),
			(call_script, "script_start_wedding_cutscene", ":groom", ":bride"),
		(try_end),
	]),
	
	
	#script_npc_decision_checklist_party_ai
	# DECISION CHECKLISTS (OCT 14)
	# I was thinking of trying to convert as much AI decision-making as possible to the checklist format
	# While outcomes are not as nuanced and varied as a random decision using weighted chances for each outcoms,
	# the checklist has the advantage of being much more transparent, both to developers and to players
	# The checklist can yield a string (standardized to s14) which explains the rationale for the decision
	# When the script yields a yes/no/maybe result, than that is standardized from -3 to +3
	# INPUT: troop_no
	# OUTPUT: none
	("npc_decision_checklist_party_ai",
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
	]),
	
	#script_npc_decision_checklist_troop_follow_or_not
	# INPUT: troop_no
	# OUTPUT: reg0
	(
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
	]),
	
	#script_find_total_prosperity_score
	# INPUT: center_no
	# OUTPUT: reg0 = total_prosperity_score
	(
		"find_total_prosperity_score",
		[
		(store_script_param, ":center_no", 1),
		
		(try_begin), #":total_prosperity_score" changes between 10..100
			(is_between, ":center_no", walled_centers_begin, walled_centers_end),
			
			(party_get_slot, ":center_prosperity", ":center_no", slot_town_prosperity),
			(store_add, ":center_prosperity_add_200_div_10", ":center_prosperity", 200),
			(val_div, ":center_prosperity_add_200_div_10", 10),
			(try_begin),
			(is_between, ":center_no", towns_begin, towns_end),
			(store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 15),
			(else_try),
			(store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 5),
			(try_end),
			(assign, ":total_prosperity_score", ":this_center_score"),
			
			(try_for_range_backwards, ":village_no", villages_begin, villages_end),
			(party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
			
			(party_get_slot, ":village_prosperity", ":village_no", slot_town_prosperity),
			(store_add, ":village_prosperity_add_200_div_10", ":village_prosperity", 200),
			(val_div, ":village_prosperity_add_200_div_10", 10),
			(store_mul, ":this_village_score", ":village_prosperity_add_200_div_10", 5),
			
			(val_add, ":total_prosperity_score", ":this_village_score"),
			(try_end),
		(else_try),
			(party_get_slot, ":center_prosperity", ":center_no", slot_town_prosperity),
			(store_add, ":center_prosperity_add_200_div_10", ":center_prosperity", 200),
			(val_div, ":center_prosperity_add_200_div_10", 10),
			(store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 5),
			(assign, ":total_prosperity_score", ":this_center_score"),
		(try_end),
		(val_div, ":total_prosperity_score", 10),
		
		(assign, reg0, ":total_prosperity_score"),
	]),
	
	#script_calculate_center_assailability_score
	# INPUT: faction_no
	# param1: faction_no
	# param2: all_vassals_included, (becomes 1 if we want to find attackable center if we collected 20% of vassals during gathering army phase)
	# OUTPUT:
	# reg0 = center_to_attack (-1 if none is logical)
	# reg1 = maximum_attack_score
	(
		"calculate_center_assailability_score",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":potential_target", 2),
		(store_script_param, ":all_vassals_included", 3),
		
		(assign, ":target_score", -1),
		
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		
		(store_current_hours, ":hours_since_last_offensive"),
		(faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
		(val_sub, ":hours_since_last_offensive", ":last_offensive_time"),
		
		(store_div, ":last_offensive_time_score", ":hours_since_last_offensive", 12), #30..50
		(val_add, ":last_offensive_time_score", 30),
		(val_min, ":last_offensive_time_score", 100),
		
		(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
		
		(assign, ":marshal_party", -1),
		(assign, ":marshal_strength", 0),
		#(assign, ":strength_of_nearby_friend", 0),
		
		(try_begin),
			(gt, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
			(party_is_active, ":marshal_party"),
			(party_get_slot, ":marshal_strength", ":marshal_party", slot_party_cached_strength),
			#(eq, ":all_vassals_included", 0),
			(party_get_slot, ":strength_of_current_followers", ":marshal_party", slot_party_follower_strength),
			#(party_get_slot, ":strength_of_nearby_friend", ":marshal_party", slot_party_nearby_friend_strength),
		(try_end),
		
		#(try_begin),
		#  (eq, ":all_vassals_included", 0),
		#
		#  (try_begin),
		#    (gt, ":faction_marshal", 0),
		#    (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
		#    (party_is_active, ":marshal_party"),
		#    (party_get_slot, ":strength_of_potential_followers", ":marshal_party", slot_party_follower_strength),
		#  (try_end),
		#(else_try),
		#  (eq, ":all_vassals_included", 1),
		#
		#  (assign, ":strength_of_potential_followers", 0),
		#
		#  (try_for_parties, ":party_no"),
		#    (store_faction_of_party, ":party_faction", ":party_no"),
		#    (eq, ":party_faction", ":faction_no"),
		#    (neq, ":party_no", ":marshal_party"),
		#    (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
		#    (call_script, "script_party_calculate_strength", ":party_no", 0),
		#    (val_add, ":strength_of_potential_followers", reg0),
		#  (try_end),
		#
		#  (val_div, ":strength_of_potential_followers", 2), #Ozan - Think about this, will you divide strength_of_potential_followers to 3 or 2.5 or 2
		#(else_try),
		#  (assign, ":strength_of_potential_followers", 0),
		#(try_end),
		
		(faction_get_slot, ":last_attacked_center", ":faction_no", slot_faction_last_attacked_center),
		(faction_get_slot, ":last_attacked_hours", ":faction_no", slot_faction_last_attacked_hours),
		
		(try_begin),
			(store_current_hours, ":hours"),
			(store_add, ":last_attacked_hours_plus_24", ":last_attacked_hours", 24),
			(gt, ":hours", ":last_attacked_hours_plus_24"),
			(faction_set_slot, ":faction_no", slot_faction_last_attacked_center, 0),
			(assign, ":last_attacked_center", 0),
		(try_end),
		
		(try_begin),
			(this_or_next|eq, ":last_attacked_center", 0),
			(this_or_next|eq, ":last_attacked_center", ":potential_target"),
			(this_or_next|eq, "$g_do_not_skip_other_than_current_ai_object", 1),
			(neg|faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
			
			(party_is_active, ":potential_target"),
			(store_faction_of_party, ":potential_target_faction", ":potential_target"),
			
			(store_relation, ":relation", ":potential_target_faction", ":faction_no"),
			(lt, ":relation", 0),
			
			#attack if and only if we are already besieging that center or anybody do not making besiege.
			(assign, ":faction_of_besieger_party", -1),
			(try_begin),
			(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
			(neg|party_slot_eq, ":potential_target", slot_center_is_besieged_by, -1),
			(party_get_slot, ":besieger_party", ":potential_target", slot_center_is_besieged_by),
			(party_is_active, ":besieger_party"),
			(store_faction_of_party, ":faction_of_besieger_party", ":besieger_party"),
			(try_end),
			
			(this_or_next|eq, ":faction_of_besieger_party", -1),
			(eq, ":faction_of_besieger_party", ":faction_no"),
			
			#attack if and only if this center is not a village or if it is village it should not be raided or looted
			(assign, ":village_is_looted_or_raided_already", 0),
			(try_begin),
			(is_between, ":potential_target", villages_begin, villages_end),
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
			(this_or_next|party_slot_eq, ":potential_target", slot_village_state, svs_looted),
			(eq, ":raiding_by_one_other_faction", 1),
			(assign, ":village_is_looted_or_raided_already", 1),
			(try_end),
			(eq, ":village_is_looted_or_raided_already", 0),
			
			#if ":potential_target" is faction object of some other faction which is enemy to owner of
			#":potential_target" then this target cannot be new target we are looking for.
			(assign, ":this_potantial_target_is_target_of_some_other_faction", 0),
			(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
			(is_between, ":cur_faction", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
			(neq, ":cur_faction", ":faction_no"),
			(faction_get_slot, ":faction_object", ":cur_faction", slot_faction_ai_object),
			(eq, ":faction_object", ":potential_target"),
			(store_relation, ":rel", ":potential_target_faction", ":cur_faction"),
			(lt, ":rel", 0),
			(assign, ":this_potantial_target_is_target_of_some_other_faction", 1),
			(try_end),
			(eq, ":this_potantial_target_is_target_of_some_other_faction", 0),
			
			(try_begin),
			(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
			(party_get_slot, ":potential_target_inside_strength", ":potential_target", slot_party_cached_strength),
			(party_get_slot, ":potential_target_nearby_enemy_strength", ":potential_target", slot_party_nearby_friend_strength),
			(val_div, ":potential_target_nearby_enemy_strength", 2),
			(store_add, ":potential_target_strength", ":potential_target_inside_strength", ":potential_target_nearby_enemy_strength"),
			
			#(try_begin),
			#(eq, ":faction_no", "fac_kingdom_4"),
			#(assign, reg0, ":potential_target_inside_strength"),
			#(assign, reg1, ":potential_target_nearby_enemy_strength"),
			#(assign, reg2, ":marshal_strength"),
			#(assign, reg3, ":strength_of_potential_followers"),
			#(assign, reg4, ":strength_of_nearby_friend"),
			#(assign, reg6, ":marshal_party"),
			#(str_store_party_name, s8, ":potential_target"),
			#(eq, ":all_vassals_included", 0),
			#(display_message, "@DEBUG : {s8}:{reg0}, neare {reg1}, our {reg2}, follow {reg3}, nearf {reg4}"),
			#(try_end),
			
			(val_mul, ":potential_target_strength", 4), #in walled centers defenders have advantage.
			(val_div, ":potential_target_strength", 3),
			
			#(store_add, ":army_strength", ":marshal_strength", ":strength_of_potential_followers"),
			(assign, ":army_strength", ":marshal_strength"),
			(val_add, ":army_strength", ":strength_of_current_followers"),
			(store_mul, ":power_ratio", ":army_strength", 100),
			
			#this ratio ":power_ratio" shows (our total army power) / (their total army power)
			(try_begin),
				(gt, ":potential_target_strength", 0),
				(val_div, ":power_ratio", ":potential_target_strength"),
			(else_try),
				(assign, ":power_ratio", 1000),
			(try_end),
			(else_try),
			(party_get_slot, ":potential_target_nearby_enemy_strength", ":potential_target", slot_party_nearby_friend_strength),
			(assign, ":potential_target_strength", 1000),
			
			#(store_add, ":army_strength", ":marshal_strength", ":strength_of_potential_followers"),
			(assign, ":army_strength", ":marshal_strength"),
			(val_add, ":army_strength", ":strength_of_current_followers"),
			(store_mul, ":power_ratio", ":army_strength", 100),
			
			(try_begin),
				(gt, ":potential_target_strength", 0),
				(val_div, ":power_ratio", ":potential_target_strength"),
			(else_try),
				(assign, ":power_ratio", 1000),
			(try_end),
			(try_end),
			
			(ge, ":power_ratio", 120), #attack if and only if our army is at least 1.2 times powerfull
			(store_sub, ":power_ratio_sub_120", ":power_ratio", 120),
			
			(try_begin),
			(lt, ":power_ratio_sub_120", 100), #changes between 20..120
			(store_add, ":power_ratio_score", ":power_ratio_sub_120", 20),
			(else_try),
			(lt, ":power_ratio_sub_120", 200), #changes between 120..170
			(store_sub, ":power_ratio_score", ":power_ratio_sub_120", 100),
			(val_div, ":power_ratio_score", 2),
			(val_add, ":power_ratio_score", 120),
			(else_try),
			(lt, ":power_ratio_sub_120", 400), #changes between 170..210
			(store_sub, ":power_ratio_score", ":power_ratio_sub_120", 200),
			(val_div, ":power_ratio_score", 5),
			(val_add, ":power_ratio_score", 170),
			(else_try),
			(lt, ":power_ratio_sub_120", 800), #changes between 210..250
			(store_sub, ":power_ratio_score", ":power_ratio_sub_120", 400),
			(val_div, ":power_ratio_score", 10),
			(val_add, ":power_ratio_score", 210),
			(else_try),
			(assign, ":power_ratio_score", 250),
			(try_end),
			
			(assign, ":number_of_walled_centers", 0),
			(assign, ":total_distance", 0),
			(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":walled_center_faction", ":walled_center"),
			(eq, ":walled_center_faction", ":faction_no"),
			
			(store_distance_to_party_from_party, ":dist", ":walled_center", ":potential_target"),
			(val_add, ":total_distance", ":dist"),
			
			(val_add, ":number_of_walled_centers", 1),
			(try_end),
			
			(try_begin),
			(gt, ":number_of_walled_centers", 0),
			(store_div, ":average_distance", ":total_distance", ":number_of_walled_centers"),
			#(assign, reg0, ":average_distance"),
			#(str_store_faction_name, s7, ":faction_no"),
			#(str_store_party_name, s8, ":potential_target"),
			#(display_message, "@average distance for {s7} for {s8} is {reg0}"),
			
			(try_begin),
				(ge, ":marshal_party", 0),
				(party_is_active, ":marshal_party"),
				(store_distance_to_party_from_party, ":marshal_dist_to_potential_target", ":marshal_party", ":potential_target"),
			(else_try),
				(assign, ":marshal_dist_to_potential_target", 100),
			(try_end),
			
			(try_begin),
				#if currently our target is attacking to an enemy center and that center is besieged/raided by one of our parties then
				#divide marshal_distance for other center's to "2" instead of "3" and add some small more distance to avoid easily
				#changing mind during siege because of small score differences.
				
				(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
				(eq, ":current_ai_state", sfai_attacking_center),
				(faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
				
				(ge, ":current_ai_object", 0),
				(neq, ":current_ai_object", ":potential_target"),
				
				(try_begin),
				(ge, ":power_ratio_score", 300), #200 max
				(assign, ":power_ratio_score", 200),
				(else_try),
				(ge, ":power_ratio_score", 100), #100..200
				(val_sub, ":power_ratio_score", 100),
				(val_div, ":power_ratio_score", 2),
				(val_add, ":power_ratio_score", 100),
				(try_end),
				
				(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
				(eq, "$g_do_not_skip_other_than_current_ai_object", 0),
				(assign, ":power_ratio_score", 0), #lets completely forget all other choices if we are already besieging one center.
				(try_end),
				
				(faction_set_slot, ":faction_no", slot_faction_last_attacked_center, ":current_ai_object"),
				(store_current_hours, ":hours"),
				(faction_set_slot, ":faction_no", slot_faction_last_attacked_hours, ":hours"),
				
				(eq, ":all_vassals_included", 0),
				
				(store_div, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target", 2),
				(assign, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target"),
			(else_try),
				(store_div, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target", 3),
			(try_end),
			
			(store_add, ":total_distance", ":average_distance", ":marshal_dist_to_potential_target_div_x"), #in average ":total_distance" is about 150, min : 0, max : 1000
			(else_try),
			(assign, ":total_distance", 100),
			(try_end),
			
			(try_begin),
			#according to cautious troop distance is more important
			
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			
			(try_begin),
				#(lt, ":total_distance", 30), #very close (100p)
				(lt, ":total_distance", 45), #rafi
				(assign, ":distance_score", 100),
			(else_try),
				#(lt, ":total_distance", 80), #close (50p-100p)
				(lt, ":total_distance", 120),#rafo
				#(store_sub, ":distance_score", ":total_distance", 30),
				(store_sub, ":distance_score", ":total_distance", 45), #rafi
				(val_div, ":distance_score", 1),
				(store_sub, ":distance_score", 100, ":distance_score"),
			(else_try),
				#(lt, ":total_distance", 160), #far (10p-50p)
				(lt, ":total_distance", 240), #rafi
				#(store_sub, ":distance_score", ":total_distance", 80),
				(store_sub, ":distance_score", ":total_distance", 120),
				(val_div, ":distance_score", 2),
				(store_sub, ":distance_score", 50, ":distance_score"),
			(else_try),
				(assign, ":distance_score", 10), #very far
			(try_end),
			(else_try),
			#according to agressive troop distance is less important
			
			(try_begin),
				#(lt, ":total_distance", 40), #very close (100p)
				(lt, ":total_distance", 60), #very close (100p)
				(assign, ":distance_score", 100),
			(else_try),
				#(lt, ":total_distance", 140), #close (50p-100p)
				(lt, ":total_distance", 210), #close (50p-100p)
				#(store_sub, ":distance_score", ":total_distance", 40),
				(store_sub, ":distance_score", ":total_distance", 60),
				(val_div, ":distance_score", 2),
				(store_sub, ":distance_score", 100, ":distance_score"),
			(else_try),
				#(lt, ":total_distance", 300), #far (10p-50p)
				(lt, ":total_distance", 450), #far (10p-50p)
				#(store_sub, ":distance_score", ":total_distance", 140),
				(store_sub, ":distance_score", ":total_distance", 210),
				(val_div, ":distance_score", 4),
				(store_sub, ":distance_score", 50, ":distance_score"),
			(else_try),
				(assign, ":distance_score", 10), #very far
			(try_end),
			(try_end),
			
			(store_mul, ":target_score", ":distance_score", ":power_ratio_score"),
			(val_mul, ":target_score", ":last_offensive_time_score"),
			(val_div, ":target_score", 100), #target score is between 0..10000 generally here
			
			(call_script, "script_find_total_prosperity_score", ":potential_target"),
			(assign, ":total_prosperity_score", reg0),
			
			#(try_begin), #new for increase attackability of villages by ai
			#(is_between, ":potential_target", villages_begin, villages_end),
			(val_mul, ":total_prosperity_score", 3),
			(val_div, ":total_prosperity_score", 2),
			#(try_end),
			
			(val_mul, ":target_score", ":total_prosperity_score"),
			
			(try_begin), #if both that center was our (original center) and (ex center) than bonus is 1.2x
			(party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
			(party_slot_eq, ":potential_target", slot_center_original_faction, ":faction_no"),
			(val_mul, ":target_score", 12),
			(val_div, ":target_score", 10),
			(else_try), #if either that center was our (original center) or (ex center) than bonus is 1.1x
			(this_or_next|party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
			(party_slot_eq, ":potential_target", slot_center_original_faction, ":faction_no"),
			(val_mul, ":target_score", 11),
			(val_div, ":target_score", 10),
			(try_end),
			
			(val_div, ":target_score", 1000), #target score is between 0..1000 generally here
			
			(try_begin),
			(eq, ":potential_target_faction", "fac_player_supporters_faction"),
			(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			
			(assign, ":number_of_walled_centers_player_have", 0),
			(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
				(store_faction_of_party, ":center_faction", ":center_no"),
				(eq, ":center_faction", "fac_player_supporters_faction"),
				(val_add, ":number_of_walled_centers_player_have", 1),
			(try_end),
			
			(try_begin),
				(eq, ":reduce_campaign_ai", 2), #easy
				
				(try_begin),
				(le, ":number_of_walled_centers_player_have", 2),
				(assign, ":hardness_score", 0),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 3),
				(assign, ":hardness_score", 20),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 4),
				(assign, ":hardness_score", 40),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 5),
				(eq, ":number_of_walled_centers_player_have", 6),
				(assign, ":hardness_score", 55),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 7),
				(eq, ":number_of_walled_centers_player_have", 8),
				(eq, ":number_of_walled_centers_player_have", 9),
				(assign, ":hardness_score", 70),
				(else_try),
				(assign, ":hardness_score", 85),
				(try_end),
			(else_try),
				(eq, ":reduce_campaign_ai", 1), #medium
				
				(try_begin),
				(le, ":number_of_walled_centers_player_have", 1),
				(assign, ":hardness_score", 25),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 2),
				(assign, ":hardness_score", 45),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 3),
				(assign, ":hardness_score", 60),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 4),
				(eq, ":number_of_walled_centers_player_have", 5),
				(assign, ":hardness_score", 75),
				(else_try),
				(eq, ":number_of_walled_centers_player_have", 6),
				(eq, ":number_of_walled_centers_player_have", 7),
				(eq, ":number_of_walled_centers_player_have", 8),
				(assign, ":hardness_score", 85),
				(else_try),
				(assign, ":hardness_score", 92),
				(try_end),
			(else_try), #hard
				(assign, ":hardness_score", 100),
			(try_end),
			
			(val_mul, ":target_score", ":hardness_score"),
			(val_div, ":target_score", 100),
			(try_end),
			
			#(try_begin),
			#  (eq, ":faction_no", "fac_kingdom_28"),
			#  (ge, ":target_score", -1),
			#  (assign, reg0, ":target_score"),
			#  (assign, reg7, ":total_prosperity_score"),
			#  (assign, reg8, ":power_ratio_score"),
			#  (assign, reg9, ":distance_score"),
			#  (assign, reg10, ":last_offensive_time_score"),
			#  (str_store_party_name, s8, ":potential_target"),
			#  #(eq, ":all_vassals_included", 0),
			#  (assign, reg11, ":all_vassals_included"),
			#(try_end),
		(try_end),
		
		(assign, reg0, ":target_score"),
		(assign, reg1, ":power_ratio"),
		(assign, reg2, ":distance_score"),
		(assign, reg3, ":total_prosperity_score"),
	]),
	
	#script_find_center_to_defend
	# INPUT:
	# param1: faction_no
	# OUTPUT:
	# reg0 = center_to_defend (-1 if none is logical)
	# reg1 = maximum_defend_score
	# reg3 = enemy_strength_near_most_threatened_center
	(
		"find_center_to_defend",
		[
		(store_script_param, ":troop_no", 1),
		
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		
		(faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
		(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
		(assign, ":marshal_party", -1),
		(try_begin),
			(gt, ":faction_marshal", 0),
			(troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
		(try_end),
		
		(assign, ":most_threatened_center", -1),
		(assign, ":maximum_threat_score", 0),
		(try_for_range, ":cur_center", centers_begin, centers_end),
		#(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end), #tom
			(store_faction_of_party, ":center_faction", ":cur_center"),
			(eq, ":center_faction", ":faction_no"),
			
			(party_get_slot, ":exact_enemy_strength", ":cur_center", slot_center_sortie_enemy_strength),
			#Distort this to account for questionable intelligence
			#(call_script, "script_reduce_exact_number_to_estimate", ":exact_enemy_strength"),
			#(assign, ":enemy_strength_nearby", reg0),
			(assign, ":enemy_strength_nearby", ":exact_enemy_strength"),
			
			(assign, ":threat_importance", 0),
			(try_begin),
			(is_between, ":cur_center", walled_centers_begin, walled_centers_end),
			(party_slot_ge, ":cur_center", slot_center_is_besieged_by, 0),
			
			(call_script, "script_find_total_prosperity_score", ":cur_center"),
			(assign, ":total_prosperity_score", reg0),
			
			(party_get_slot, ":cur_center_strength", ":cur_center", slot_party_cached_strength),
			(val_mul, ":cur_center_strength", 4),
			(val_div, ":cur_center_strength", 3), #give 33% bonus to insiders because they are inside a castle
			
			#I removed below line and assigned ":cur_center_nearby_strength" to 0, because if not when defender army comes to help
			#threat become less because of high defence power but not yet enemy cleared.
			#(party_get_slot, ":cur_center_nearby_strength", ":cur_center", slot_party_nearby_friend_strength),
			(assign, ":cur_center_nearby_strength", 0),
			
			(val_add, ":cur_center_strength", ":cur_center_nearby_strength"), #add nearby friends and find ":cur_center_strength"
			
			(store_mul, ":power_ratio", ":enemy_strength_nearby", 100),
			(val_add, ":cur_center_strength", 1),
			(val_max, ":cur_center_strength", 1),
			(val_div, ":power_ratio", ":cur_center_strength"),
			
			(assign, ":player_is_attacking", 0),
			(party_get_slot, ":besieger_party", ":cur_center", slot_center_is_besieged_by),
			(try_begin),
				(party_is_active, ":besieger_party"),
				(try_begin),
				(eq, ":besieger_party", "p_main_party"),
				(assign, ":player_is_attacking", 1),
				#(display_message, "@{!}DEBUG : player is attacking a center (1)"),
				(else_try),
				(store_faction_of_party, ":besieger_faction", ":besieger_party"),
				(eq, ":besieger_faction", "fac_player_faction"),
				(assign, ":player_is_attacking", 1),
				#(display_message, "@{!}DEBUG : player is attacking a center (2)"),
				(else_try),
				(party_get_attached_to, ":player_is_attached_to", "p_main_party"),
				(ge, ":player_is_attached_to", 0),
				(eq, ":player_is_attached_to", ":besieger_party"),
				(assign, ":player_is_attacking", 1),
				#(display_message, "@{!}DEBUG : player is attacking a center (3)"),
				(try_end),
			(try_end),
			
			(try_begin),
				(eq, ":player_is_attacking", 0),
				
				(try_begin),
				(lt, ":power_ratio", 40), #changes between 1..1
				(assign, ":threat_importance", 1),
				(else_try),
				(lt, ":power_ratio", 80), #changes between 1..7
				(store_sub, ":threat_importance", ":power_ratio", 40),
				(val_div, ":threat_importance", 5),
				(val_add, ":threat_importance", 1), #1
				(else_try),
				(lt, ":power_ratio", 120), #changes between 7..17
				(store_sub, ":threat_importance", ":power_ratio", 80),
				(val_div, ":threat_importance", 4),
				(val_add, ":threat_importance", 7), #1 + 6
				(else_try),
				(lt, ":power_ratio", 200),
				(store_sub, ":threat_importance", ":power_ratio", 120),
				(val_div, ":threat_importance", 10),
				(val_add, ":threat_importance", 17), #1 + 6 + 10
				(else_try),
				(assign, ":threat_importance", 25),
				(try_end),
			(else_try),
				(try_begin),
				(lt, ":power_ratio", 200), #changes between 5..25
				(store_div, ":threat_importance", ":power_ratio", 10),
				(val_add, ":threat_importance", 6 ),
				(else_try),
				(assign, ":threat_importance", 26),
				(try_end),
			(try_end),
			(else_try),
			(is_between, ":cur_center", villages_begin, villages_end),
			(party_slot_eq, ":cur_center", slot_village_state, svs_being_raided),
			
			(gt, ":enemy_strength_nearby", 0),
			
			(call_script, "script_find_total_prosperity_score", ":cur_center"),
			(assign, ":power_ratio", 100), #useless
			(assign, ":total_prosperity_score", reg0),
			(assign, ":threat_importance", 10), #if faction village is looted they lose money for shorter time period. So importance is something low (6-8).
			(try_end),
			
			(gt, ":threat_importance", 0),
			
			(try_begin),
			(is_between, ":cur_center", walled_centers_begin, walled_centers_end),
			(assign, ":enemy_strength_nearby_score", 120),
			
			(try_begin),
				(ge, ":marshal_party", 0),
				(party_is_active, ":marshal_party"),
				(store_distance_to_party_from_party, ":marshal_dist_to_cur_center", ":marshal_party", ":cur_center"),
			(else_try),
				(assign, ":marshal_dist_to_cur_center", 100),
			(try_end),
			
			(try_begin),
				#if currently our target is ride to break a siege then
				#divide marshal_distance for other center's to "2" instead of "4" and add some small more distance to avoid easily
				#changing mind during siege because of small score differences.
				
				#(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
				(eq, ":current_ai_state", sfai_attacking_enemies_around_center),
				(faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
				(is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
				(neq, ":current_ai_object", ":cur_center"),
				(val_mul, ":marshal_dist_to_cur_center", 2),
				(val_add, ":marshal_dist_to_cur_center", 20),
			(try_end),
			
			(val_mul, ":marshal_dist_to_cur_center", 2), #standard multipication (1.5x) to adjust distance scoring same with formula at find_center_to_attack
			#(val_div, ":marshal_dist_to_cur_center", 2),
			
			(try_begin),
				(lt, ":marshal_dist_to_cur_center", 10), #very close (100p)
				(assign, ":distance_score", 100),
			(else_try),
				(lt, ":marshal_dist_to_cur_center", 160), #close (50p-100p)
				(store_sub, ":distance_score", ":marshal_dist_to_cur_center", 10),
				(val_div, ":distance_score", 3),
				(store_sub, ":distance_score", 100, ":distance_score"),
			(else_try),
				(lt, ":marshal_dist_to_cur_center", 360), #far (10p-50p)
				(store_sub, ":distance_score", ":marshal_dist_to_cur_center", 250),
				(val_div, ":distance_score", 5),
				(store_sub, ":distance_score", 50, ":distance_score"),
			(else_try),
				(assign, ":distance_score", 10), #very far
			(try_end),
			(else_try),
			(store_add, ":enemy_strength_nearby_score", ":enemy_strength_nearby", 20000),
			(val_div, ":enemy_strength_nearby_score", 200),
			(assign, ":distance_score", 70), #not related to marshal's position, because everybody is going same place (no gathering in most village raids)
			(try_end),
			
			(store_mul, ":threat_score", ":enemy_strength_nearby_score", ":total_prosperity_score"),
			(val_mul, ":threat_score", ":threat_importance"),
			(val_mul, ":threat_score", ":distance_score"),
			(val_div, ":threat_score", 10000),
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(gt, ":threat_score", 0),
			(eq, ":faction_no", "fac_kingdom_6"),
			(assign, reg0, ":threat_score"),
			(str_store_party_name, s32, ":cur_center"),
			(assign, reg1,  ":total_prosperity_score"),
			(assign, reg2, ":enemy_strength_nearby_score"),
			(assign, reg3, ":threat_importance"),
			(assign, reg4, ":distance_score"),
			#(display_message, "@{!}DEBUG : defend of {s32} is {reg0}, prosperity:{reg1}, enemy nearby:{reg2}, threat importance:{reg3}, distance: {reg4}"),
			(try_end),
			
			(gt, ":threat_score", ":maximum_threat_score"),
			
			(assign, ":most_threatened_center", ":cur_center"),
			(assign, ":maximum_threat_score", ":threat_score"),
			(assign, ":enemy_strength_near_most_threatened_center", ":enemy_strength_nearby"),
		(try_end),
		
		(val_mul, ":maximum_threat_score", 3),
		(val_div, ":maximum_threat_score", 2),
		
		(assign, reg0, ":most_threatened_center"),
		(assign, reg1, ":maximum_threat_score"),
		(assign, reg2, ":enemy_strength_near_most_threatened_center"),
	]),
	
	
	#script_npc_decision_checklist_peace_or_war
	(
		"npc_decision_checklist_peace_or_war",
		#this script is used to add a bit more color to diplomacy, particularly with regards to the player
		
		[
		(store_script_param, ":actor_faction", 1),
		(store_script_param, ":target_faction", 2),
		(store_script_param, ":envoy", 3),
		
		(assign, ":actor_strength", 0),
		(assign, ":target_strength", 0),
		(assign, ":actor_centers_held_by_target", 0),
		
		(assign, ":two_factions_share_border", 0),
		(assign, ":third_party_war", 0),
		(assign, ":num_third_party_wars", 0),
		
		(assign, ":active_mutual_enemy", 0), #an active enemy with which the target is at war
		(assign, "$g_concession_demanded", 0),
		
		(faction_get_slot, ":actor_religion", ":actor_faction", slot_faction_religion),
		(faction_get_slot, ":target_religion", ":target_faction", slot_faction_religion),
		
		(store_relation, ":current_faction_relation", ":actor_faction", ":target_faction"),
		
		(call_script, "script_distance_between_factions", ":actor_faction", ":target_faction"),
		(assign, ":war_distance", reg0),
		
		(try_begin),
			(eq, ":target_faction", "fac_player_supporters_faction"),
			(assign, ":modified_honor_and_relation", "$player_honor"), #this can be affected by the emissary's skill
			
			(val_add, ":target_strength", 2), #for player party
		(else_try),
			(assign, ":modified_honor_and_relation", 0), #this can be affected by the emissary's skill
		(try_end),
		
		(faction_get_slot, ":actor_leader", ":actor_faction", slot_faction_leader),
		(faction_get_slot, ":target_leader", ":target_faction", slot_faction_leader),
		
		(call_script, "script_troop_get_relation_with_troop", ":actor_leader", ":target_leader"),
		
		(assign, ":relation_bonus", reg0),
		(val_min, ":relation_bonus", 10),
		(val_add, ":modified_honor_and_relation", ":relation_bonus"),
		
		# rafi
		(try_begin),
			(le, ":war_distance", max_war_distance),
			(assign, ":two_factions_share_border", 1),
			# (else_try),
			# (eq, ":actor_faction", "fac_crusade"),
			# (eq, ":target_faction", "$g_crusade"),
			# (assign, ":two_factions_share_border", 1),
			# (val_sub, ":modified_honor_and_relation", religious_effect_crusade),
			# (else_try),
			# (eq, ":target_faction", "fac_crusade"),
			# (eq, ":actor_faction", "$g_crusade"),
			# (assign, ":two_factions_share_border", 1),
			# (val_sub, ":modified_honor_and_relation", religious_effect_crusade),
		(try_end),
		# rafi
		
		# rafi religious differences
		(assign, ":religious_differences", 0),
		(try_begin),
			(neq, ":actor_religion", ":target_religion"),
			(eq, ":two_factions_share_border", 1),
			(try_begin),
			(eq, ":actor_religion", religion_catholic),
			(eq, ":target_religion", religion_orthodox),
			(assign, ":religious_differences", 2),
			(else_try),
			(eq, ":target_religion", religion_catholic),
			(eq, ":actor_religion", religion_orthodox),
			(assign, ":religious_differences", 2),
			(else_try),
			(assign, ":religious_differences", 1),
			(try_end),
		(try_end),
		
		(try_begin),
			(eq, ":religious_differences", 1),
			(val_sub, ":modified_honor_and_relation", religious_effect_aggressive), # religion effect
		(else_try),
			(eq, ":religious_differences", 2),
			(val_sub, ":modified_honor_and_relation", religious_effect_docile),
		(try_end),
		# rafi
		
		
		
		(str_store_troop_name, s15, ":actor_leader"),
		(str_store_troop_name, s16, ":target_leader"),
		
		
		(assign, ":war_damage_suffered", 0),
		(assign, ":war_damage_inflicted", 0),
		
		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":actor_faction", ":target_faction"),
		(assign, ":war_peace_truce_status", reg0),
		(str_clear, s12),
		(try_begin),
			(eq, ":war_peace_truce_status", -2),
			(str_store_string, s12, "str_s15_is_at_war_with_s16_"),
			
			(store_add, ":war_damage_inflicted_slot", ":target_faction", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":war_damage_inflicted_slot", kingdoms_begin),
			(faction_get_slot, ":war_damage_inflicted", ":actor_faction", ":war_damage_inflicted_slot"),
			
			(store_add, ":war_damage_suffered_slot", ":actor_faction", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":war_damage_suffered_slot", kingdoms_begin),
			(faction_get_slot, ":war_damage_suffered", ":target_faction", ":war_damage_suffered_slot"),
			
			
		(else_try),
			#truce in effect
			(eq, ":war_peace_truce_status", 1),
			(str_store_string, s12, "str_in_the_short_term_s15_has_a_truce_with_s16_as_a_matter_of_general_policy_"),
		(else_try),
			#provocation noted
			(eq, ":war_peace_truce_status", -1),
			(str_store_string, s12, "str_in_the_short_term_s15_was_recently_provoked_by_s16_and_is_under_pressure_to_declare_war_as_a_matter_of_general_policy_"),
		(try_end),
		
		#clear for dialog with lords
		(try_begin),
			(is_between, "$g_talk_troop", active_npcs_begin, active_npcs_end),
			(str_clear, s12),
		(try_end),
		
		(try_begin),
			(gt, ":envoy", -1),
			(store_skill_level, ":persuasion_x_2", "skl_persuasion", ":envoy"),
			(val_mul, ":persuasion_x_2", 2),
			(val_add, ":modified_honor_and_relation", ":persuasion_x_2"),
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg4, ":modified_honor_and_relation"),
			(display_message, "str_envoymodified_diplomacy_score_honor_plus_relation_plus_envoy_persuasion_=_reg4"),
			(try_end),
			
		(try_end),
		
		
		(try_for_range, ":kingdom_to_reset", kingdoms_begin, kingdoms_end),
			(faction_set_slot, ":kingdom_to_reset", slot_faction_temp_slot, 0),
		(try_end),
		
		(try_for_parties, ":party_no"),
			(assign, ":party_value", 0),
			# (try_begin),
				# (is_between, ":party_no", towns_begin, towns_end),
				# (assign, ":party_value", 3),
			# (else_try),
				# (is_between, ":party_no", castles_begin, castles_end),
				# (assign, ":party_value", 2),
			# (else_try),
				# (is_between, ":party_no", villages_begin, villages_end),
				# (assign, ":party_value", 1),
			# (else_try),
				# (party_get_template_id, ":template", ":party_no"),
				# (eq, ":template", "pt_kingdom_hero_party"),
				# (assign, ":party_value", 2),
			# (try_end),
			
			(store_faction_of_party, ":party_current_faction", ":party_no"),
			(party_get_slot, ":party_original_faction", ":party_no", slot_center_original_faction),
			(party_get_slot, ":party_ex_faction", ":party_no", slot_center_ex_faction),
			
			# rafi
			(try_begin),
			(is_between, ":party_current_faction", kingdoms_begin, kingdoms_end),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_town),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
			(this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_mongol_party), #rom
			(party_slot_eq, ":party_no", slot_party_type, spt_patrol),
			(party_get_slot, ":party_value", ":party_no", slot_party_cached_strength),
			(le, ":party_value", 0),
			(store_party_size_wo_prisoners, ":psize", ":party_no"),
			(gt, ":psize", 1),
			(call_script, "script_party_calculate_strength", ":party_no", 1),
			(assign, ":party_value", reg0),
			(try_end),
			# end rafi
			
			#total strengths
			(try_begin),
			(is_between, ":party_current_faction", kingdoms_begin, kingdoms_end),
			(faction_get_slot, ":faction_strength", ":party_current_faction", slot_faction_temp_slot),
			(val_add, ":faction_strength", ":party_value"),
			(faction_set_slot, ":party_current_faction", slot_faction_temp_slot, ":faction_strength"),
			(try_end),
			
			
			(try_begin),
			(eq, ":party_current_faction", ":target_faction"),
			(val_add, ":target_strength", ":party_value"),
			
			(try_begin),
				(this_or_next|eq, ":party_original_faction", ":actor_faction"),
				(eq, ":party_ex_faction", ":actor_faction"),
				(val_add, ":actor_centers_held_by_target", 1),
				(try_begin),
				(is_between, ":party_no", walled_centers_begin, walled_centers_end),
				(assign, "$g_concession_demanded", ":party_no"),
				(str_store_party_name, s18, "$g_concession_demanded"),
				(try_end),
			(try_end),
			
			# Could include two factions share border, but war is unlikely to break out in the first place unless there is a common border
			
			# (try_begin),
			# (is_between, ":party_no", walled_centers_begin, walled_centers_end),
			# (try_for_range, ":other_center", walled_centers_begin, walled_centers_end),
			# (assign, ":two_factions_share_border", 0),
			# (store_faction_of_party, ":other_faction", ":other_center"),
			# (eq, ":other_faction", ":actor_faction"),
			# (store_distance_to_party_from_party, ":distance", ":party_no", ":other_center"),
			# (le, ":distance", 15),
			# (assign, ":two_factions_share_border", 1),
			# (try_end),
			# (try_end),
			(else_try),
			(eq, ":party_current_faction", ":actor_faction"),
			(val_add, ":actor_strength", ":party_value"),
			(try_end),
		(try_end),
		
		#Total Europe strength = 110 x 1 (villages,), 48? x 2 castles, 22 x 3 towns, 88 x 2 lord parties = 272 + 176 = 448
		(assign, ":strongest_kingdom", -1),
		(assign, ":score_to_beat", 60), #Maybe raise once it works
		(try_for_range, ":strongest_kingdom_candidate", kingdoms_begin, kingdoms_end),
			(faction_get_slot, ":candidate_strength", ":strongest_kingdom_candidate", slot_faction_temp_slot),
			(gt, ":candidate_strength", ":score_to_beat"),
			(assign, ":strongest_kingdom", ":strongest_kingdom_candidate"),
			(assign, ":score_to_beat", ":candidate_strength"),
		(try_end),
		
		
		(try_begin),
			(eq, "$cheat_mode", 2),
			(gt, ":strongest_kingdom", 1),
			(str_store_faction_name, s4, ":strongest_kingdom"),
			(assign, reg3, ":score_to_beat"),
			(display_message, "@{!}DEBUG - {s4} strongest kingdom with {reg3} strength"),
		(try_end),
		
		
		(assign, ":strength_ratio", 1),
		(try_begin),
			(gt, ":actor_strength", 0),
			(store_mul, ":strength_ratio", ":target_strength", 100),
			(val_div, ":strength_ratio", ":actor_strength"),
		(try_end),
		
		# rafi
		# (try_begin),
			# (eq, "$cheat_mode", 1),
			# (str_store_faction_name, s51, ":target_faction"),
			# (str_store_faction_name, s52, ":actor_faction"),
			# (assign, reg21, ":strength_ratio"),
			# (assign, reg22, ":target_strength"),
			# (assign, reg23, ":actor_strength"),
			# (assign, reg24, ":war_damage_suffered"),
			# (display_message, "@target: {s51} - {reg22} actor: {s52} - {reg23} strength ratio: {reg21} war damage: {reg24}"),
		# (try_end),
		# rafi
		
		(try_for_range, ":possible_mutual_enemy", kingdoms_begin, kingdoms_end),
			(neq, ":possible_mutual_enemy", ":target_faction"),
			(neq, ":possible_mutual_enemy", ":actor_faction"),
			(faction_slot_eq, ":possible_mutual_enemy", slot_faction_state, sfs_active),
			
			(store_relation, ":relation", ":possible_mutual_enemy", ":actor_faction"),
			(lt, ":relation", 0),
			(assign, ":third_party_war", ":possible_mutual_enemy"),
			(val_add, ":num_third_party_wars", 1),
			
			(store_relation, ":relation", ":possible_mutual_enemy", ":target_faction"),
			(lt, ":relation", 0),
			(assign, ":active_mutual_enemy", ":possible_mutual_enemy"),
		(try_end),
		
		(store_current_hours, ":cur_hours"),
		(faction_get_slot, ":faction_ai_last_decisive_event", ":actor_faction", slot_faction_ai_last_decisive_event),
		(store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
		
		(try_begin),
			(gt, "$supported_pretender", 0),
			(this_or_next|eq, "$supported_pretender", ":actor_leader"),
			(eq, "$supported_pretender", ":target_leader"),
			(this_or_next|eq, ":actor_faction", "$supported_pretender_old_faction"),
			(eq, ":target_faction", "$supported_pretender_old_faction"),
			
			(assign, ":result", -3),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_cannot_negotiate_with_s16_as_to_do_so_would_undermine_reg4herhis_own_claim_to_the_throne_this_civil_war_must_almost_certainly_end_with_the_defeat_of_one_side_or_another"),
			
			# rafi crusades
			# (else_try),
			# (eq, ":target_faction", "$g_crusade"),
			# (eq, ":actor_faction", "fac_crusade"),
			# (assign, ":result", -3),
			# (assign, ":explainer_string", "str_s12s15_is_participating_in_a_crusade_against_s16"),
			# end rafi
		(else_try),
			(gt, ":actor_centers_held_by_target", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Actor centers held by target noted"),
			(try_end),
			
			(lt, ":war_damage_suffered", 200),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}War damage under minimum"),
			(try_end),
			
			(lt, ":strength_ratio", 125),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Strength ratio correct"),
			(try_end),
			
			(eq, ":num_third_party_wars", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Third party wars"),
			(try_end),
			
			(assign, ":result", -2),
			(assign, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
			
			##tom -- papacy, everybody loves em
		(else_try),
			(eq, ":target_faction", "fac_papacy"),
			(eq, ":actor_religion", religion_catholic),
			(assign, ":result", 2),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_prefer_to_remain_friendly_to_s16_due_them_being_the_head_of_cataholic_church"),
			##tom
			# rafi
		(else_try),
			(lt, ":modified_honor_and_relation", 0),
			(gt, ":religious_differences", 0),
			(lt, ":strength_ratio", 125),
			(lt, ":war_damage_suffered", 100),
			(neq, ":war_peace_truce_status", 1),
			(eq, ":num_third_party_wars", 0),
			
			#(assign, ":result", -3),
			(assign, ":result", -1),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_distrusts_s16_due_to_religious_differences"),
			
			# rafi
			
		(else_try),
			(lt, ":modified_honor_and_relation", -20),
			(lt, ":strength_ratio", 125),
			#(lt, ":war_damage_suffered", 400),
			(lt, ":war_damage_suffered", 200),
			(this_or_next|neq, ":war_peace_truce_status", -2),
			(lt, ":hours_since_last_decisive_event", 720),
			
			(eq, ":num_third_party_wars", 0),
			
			(assign, ":result", -3),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
		(else_try),
			(gt, ":actor_centers_held_by_target", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Actor centers held by target noted"),
			(try_end),
			
			#(lt, ":war_damage_suffered", 200),
			(lt, ":war_damage_suffered", 100),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}War damage under minimum"),
			(try_end),
			
			(lt, ":strength_ratio", 125),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Strength ratio correct"),
			(try_end),
			
			(eq, ":num_third_party_wars", 0),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}Third party wars"),
			(try_end),
			
			(assign, ":result", -2),
			(assign, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(lt, ":strength_ratio", 125),
			(le, ":num_third_party_wars", 1),
			(ge, ":war_damage_inflicted", 5),
			(this_or_next|neq, ":war_peace_truce_status", -2),
			(lt, ":hours_since_last_decisive_event", 720),
			
			(store_mul, ":war_damage_suffered_x_2", ":war_damage_suffered", 2),
			(gt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
			
			(assign, ":result", -2),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_feels_that_reg4shehe_is_winning_the_war_against_s16_and_sees_no_reason_not_to_continue"),
		(else_try),
			(le, ":war_peace_truce_status", -1),
			
			(this_or_next|eq, ":war_peace_truce_status", -1), #either a war is just beginning, or there is a provocation
			(le, ":war_damage_inflicted", 1),
			
			(lt, ":strength_ratio", 150),
			(eq, ":num_third_party_wars", 0),
			
			#(faction_slot_ge, ":actor_faction", slot_faction_instability, 60),
			(faction_slot_ge, ":actor_faction", slot_faction_instability, 10), # rafi
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects"),
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(lt, ":war_damage_inflicted", 100),
			(eq, ":num_third_party_wars", 1),
			
			(assign, ":result", -1),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12even_though_reg4shehe_is_fighting_on_two_fronts_s15_is_inclined_to_continue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor"),
			
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(lt, ":war_damage_inflicted", 100),
			(eq, ":num_third_party_wars", 0),
			
			(assign, ":result", -1),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_feels_that_reg4shehe_must_pursue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor"),
		(else_try),
			(this_or_next|faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_attacking_center),
			(this_or_next|faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_raiding_village),
			(faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_attacking_enemy_army),
			(faction_get_slot, ":offensive_object", ":actor_faction", slot_faction_ai_object),
			(party_is_active, ":offensive_object"),
			(store_faction_of_party, ":offensive_object_faction", ":offensive_object"),
			(eq, ":offensive_object_faction", ":target_faction"),
			(str_store_party_name, s17, ":offensive_object"),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_is_currently_on_the_offensive_against_s17_now_held_by_s16_and_reluctant_to_negotiate"),
			
		(else_try),
			(eq, ":two_factions_share_border", 0),
			(assign, ":result", 10),
			(assign, ":explainer_string", "str_s12s15_is_too_far_to_engage_s16"),
			
		(else_try),
			#Attack strongest kingdom, if it is also at war
			(eq, ":strongest_kingdom", ":target_faction"),
			(eq, ":num_third_party_wars", 0),
			
			#Either not at war, or at war for two months
			(this_or_next|ge, ":war_peace_truce_status", -1),
			(lt, ":hours_since_last_decisive_event", 1440),
			
			(eq, ":two_factions_share_border", 1),
			
			(assign, ":at_least_one_other_faction_at_war_with_strongest", 0),
			(try_for_range, ":kingdom_to_check", kingdoms_begin, kingdoms_end),
			(neq, ":kingdom_to_check", ":actor_faction"),
			(neq, ":kingdom_to_check", ":target_faction"),
			(faction_slot_eq, ":kingdom_to_check", slot_faction_state, sfs_active),
			(store_relation, ":relation_of_factions", ":kingdom_to_check", ":target_faction"),
			(lt, ":relation_of_factions", 0),
			(assign, ":at_least_one_other_faction_at_war_with_strongest", 1),
			(try_end),
			(eq, ":at_least_one_other_faction_at_war_with_strongest", 1),
			
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_is_alarmed_by_the_growing_power_of_s16"),
			
			#bid to conquer all Calradia
		(else_try),
			(eq, ":num_third_party_wars", 0),
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- No third party wars for {s15}"),
			(try_end),
			(eq, ":actor_faction", ":strongest_kingdom"),
			#peace with no truce or provocation
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s15} is strongest kingdom"),
			(try_end),
			
			
			(faction_get_slot, ":actor_strength", ":actor_faction", slot_faction_temp_slot),
			(faction_get_slot, ":target_strength", ":target_faction", slot_faction_temp_slot),
			(store_sub, ":strength_difference", ":actor_strength", ":target_strength"),
			(ge, ":strength_difference", 30),
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s15} has 30 point advantage over {s16}"),
			(try_end),
			
			
			(assign, ":nearby_center_found", 0),
			(try_for_range, ":actor_faction_walled_center", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":walled_center_faction_1", ":actor_faction_walled_center"),
			(eq, ":walled_center_faction_1", ":actor_faction"),
			(try_for_range, ":target_faction_walled_center", walled_centers_begin, walled_centers_end),
				(store_faction_of_party, ":walled_center_faction_2", ":target_faction_walled_center"),
				(eq, ":walled_center_faction_2", ":target_faction"),
				(store_distance_to_party_from_party, ":distance", ":target_faction_walled_center", ":actor_faction_walled_center"),
				(lt, ":distance", 25),
				(assign, ":nearby_center_found", 1),
			(try_end),
			(try_end),
			(eq, ":nearby_center_found", 1),
			
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- {s15} has proximity to {s16}"),
			(try_end),
			
			(assign, ":result", -1),
			(assign, ":explainer_string", "str_s12s15_declared_war_to_control_calradia"),
			
		(else_try),
			(lt, ":modified_honor_and_relation", 0),
			(eq, ":religious_differences", 1),
			(lt, ":strength_ratio", 125),
			(eq, ":num_third_party_wars", 0),
			(le, ":war_damage_suffered", 100),
			
			(assign, ":result", 0),
			(assign, ":explainer_string", "str_s12s15_distrusts_s16_due_to_religious_differences"),
			
		(else_try),
			(lt, ":modified_honor_and_relation", -20),
			
			(assign, ":result", 0),
			(assign, ":explainer_string", "str_s12s15_distrusts_s16_and_fears_that_any_deals_struck_between_the_two_realms_will_not_be_kept"),
			
			#wishes to deal
		(else_try),
			(lt, ":current_faction_relation", 0),
			(ge, ":num_third_party_wars", 2),
			(assign, ":result", 3),
			
			(assign, ":explainer_string", "str_s12s15_is_at_war_on_too_many_fronts_and_eager_to_make_peace_with_s16"),
		(else_try),
			(gt, ":active_mutual_enemy", 0),
			(eq, ":actor_centers_held_by_target", 0),
			(this_or_next|ge, ":current_faction_relation", 0),
			#(eq, ":two_factions_share_border", 0),
			#(eq, 1, 1),
			
			(assign, ":result", 3),
			(str_store_faction_name, s17, ":active_mutual_enemy"),
			(troop_get_type, reg4, ":actor_leader"),
			(assign, ":explainer_string", "str_s12s15_seems_to_think_that_s16_and_reg4shehe_have_a_common_enemy_in_the_s17"),
			
		(else_try),
			(eq, ":war_peace_truce_status", -2),
			(ge, ":hours_since_last_decisive_event", 720),
			
			(troop_get_type, reg4, ":actor_leader"),
			
			(assign, ":result", 2),
			(assign, ":explainer_string", "str_s12s15_feels_frustrated_by_reg4herhis_inability_to_strike_a_decisive_blow_against_s16"),
			
			
		(else_try),
			(lt, ":current_faction_relation", 0),
			(gt, ":war_damage_suffered", 100),
			
			(val_mul, ":war_damage_suffered_x_2", 2),
			(lt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
			
			(assign, ":result", 2),
			(assign, ":explainer_string", "str_s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace"),
			
		(else_try),
			(gt, ":third_party_war", 0),
			(ge, ":modified_honor_and_relation", 0),
			(lt, ":current_faction_relation", 0),
			
			(assign, ":result", 1),
			(str_store_faction_name, s17, ":third_party_war"),
			(assign, ":explainer_string", "str_s12s15_would_like_to_firm_up_a_truce_with_s16_to_respond_to_the_threat_from_the_s17"),
		(else_try),
			(gt, ":third_party_war", 0),
			(ge, ":modified_honor_and_relation", 0),
			
			(assign, ":result", 1),
			(str_store_faction_name, s17, ":third_party_war"),
			(assign, ":explainer_string", "str_s12s15_wishes_to_be_at_peace_with_s16_so_as_to_pursue_the_war_against_the_s17"),
		(else_try),
			(gt, ":strength_ratio", 175),
			(eq, ":two_factions_share_border", 1),
			
			(assign, ":result", 1),
			(assign, ":explainer_string", "str_s12s15_seems_to_be_intimidated_by_s16_and_would_like_to_avoid_hostilities"),
		(else_try),
			(lt, ":current_faction_relation", 0),
			
			(assign, ":result", 1),
			(assign, ":explainer_string", "str_s12s15_has_no_particular_reason_to_continue_the_war_with_s16_and_would_probably_make_peace_if_given_the_opportunity"),
		(else_try),
			(assign, ":result", 1),
			(assign, ":explainer_string", "str_s12s15_seems_to_be_willing_to_improve_relations_with_s16"),
		(try_end),
		
		(str_store_string, s14, ":explainer_string"),
		(assign, reg0, ":result"),
		(assign, reg1, ":explainer_string"),
		
	]),
	
	("npc_decision_checklist_male_guardian_assess_suitor", #parameters from dialog
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
		
	]),
	
	("npc_decision_checklist_marry_female_pc", #
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
		
		]
	),
	
	
	#	(
	#	"npc_decision_checklist_king_chooses_lord_for_center",
	#	[
	#	(store_script_param, ":center", 1),
	
	#	(store_faction_of_party, ":faction", ":center"),
	#	(faction_get_slot, ":king", ":faction", slot_faction_leader),
	
	#	(assign, ":total_renown_in_faction"),
	#	(try_for_range, ":lord_iterator", active_npcs_including_player_begin, active_npcs_end),
	#		(assign, ":lord", ":lord_iterator"),
	#		(store_faction_of_troop, ":lord_faction", ":lord"),
	#		(try_begin),
	#			(eq, ":lord_iterator", "trp_kingdom_heroes_including_player_begin"),
	#			(assign, ":lord", "trp_player"),
	#			(assign, ":lord_faction", "$players_kingdom"),
	#		(try_end),
	#		(troop_get_slot, ":renown", ":lord", slot_troop_renown),
	#		(val_add, ":total_renown_in_faction", ":renown"),
	
	#		(troop_set_slot, ":lord", slot_troop_temp_slot, 0),
	#	(try_end),
	
	#	(assign, ":total_property_points_in_faction"),
	#	(try_for_range, ":village", villages_begin, villages_end),
	
	#	(try_end),
	
	
	
	#	(try_begin),
	
	#I needed it for myself
	
	#The one who captured it was suitably deserving
	
	#I had not sufficiently recognized Lord X for his service
	
	#	(try_end),
	
	
	#	]),
	
	
	
	("courtship_poem_reactions", #parameters from dialog
		[
		(store_script_param, ":lady", 1),
		(store_script_param, ":poem", 2),
		
		(troop_get_slot, ":lady_reputation", ":lady", slot_lord_reputation_type),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg4, ":poem"),
			(assign, reg5, ":lady_reputation"),
			(display_message, "str_poem_choice_reg4_lady_rep_reg5"),
		(try_end),
		
		(try_begin), #conventional ++, ambitious -, adventurous -
			(eq, ":poem", courtship_poem_tragic),
			(eq, ":lady_reputation", lrep_conventional),
			(str_store_string, s11, "str_ah__kais_and_layali__such_a_sad_tale_many_a_time_has_it_been_recounted_for_my_family_by_the_wandering_poets_who_come_to_our_home_and_it_has_never_failed_to_bring_tears_to_our_eyes"),
			(assign, ":result", 5),
		(else_try),
			(eq, ":poem", courtship_poem_tragic),
			(eq, ":lady_reputation", lrep_ambitious),
			(str_store_string, s11, "str_kais_and_layali_three_hundred_stanzas_of_pathetic_sniveling_if_you_ask_me_if_kais_wanted_to_escape_heartbreak_he_should_have_learned_to_live_within_his_station_and_not_yearn_for_what_he_cannot_have"),
			(assign, ":result", 0),
		(else_try),
			(eq, ":poem", courtship_poem_tragic),
			(eq, ":lady_reputation", lrep_otherworldly),
			(str_store_string, s11, "str_kais_and_layali_no_one_should_ever_have_written_such_a_sad_poem_if_it_was_the_destiny_of_kais_and_layali_to_be_together_than_their_love_should_have_conquered_all_obstacles"),
			(assign, ":result", 1),
		(else_try),
			(eq, ":poem", courtship_poem_tragic),
			#		moralizing and adventurous
			(str_store_string, s11, "str_ah_kais_and_layali_a_very_old_standby_but_moving_in_its_way"),
			(assign, ":result", 3),
			#Heroic
		(else_try), #adventurous ++, conventional -1, moralizing -1
			(eq, ":poem", courtship_poem_heroic),
			(eq, ":lady_reputation", lrep_adventurous),
			(str_store_string, s11, "str_the_saga_of_helgered_and_kara_such_happy_times_in_which_our_ancestors_lived_women_like_kara_could_venture_out_into_the_world_like_men_win_a_name_for_themselves_and_not_linger_in_their_husbands_shadow"),
			(assign, ":result", 5),
		(else_try), #adventurous ++, conventional -1, moralizing -1
			(eq, ":poem", courtship_poem_heroic),
			(eq, ":lady_reputation", lrep_ambitious),
			(str_store_string, s11, "str_ah_the_saga_of_helgered_and_kara_now_there_was_a_lady_who_knew_what_she_wanted_and_was_not_afraid_to_obtain_it"),
			(assign, ":result", 2),
		(else_try), #adventurous ++, conventional -1, moralizing -1
			(eq, ":poem", courtship_poem_heroic),
			(eq, ":lady_reputation", lrep_otherworldly),
			(str_store_string, s11, "str_the_saga_of_helgered_and_kara_a_terrible_tale__but_it_speaks_of_a_very_great_love_if_she_were_willing_to_make_war_on_her_own_family"),
			(assign, ":result", 2),
		(else_try), #adventurous ++, conventional -1, moralizing -1
			(eq, ":poem", courtship_poem_heroic),
			(eq, ":lady_reputation", lrep_moralist),
			(str_store_string, s11, "str_the_saga_of_helgered_and_kara_as_i_recall_kara_valued_her_own_base_passions_over_duty_to_her_family_that_she_made_war_on_her_own_father_i_have_no_time_for_a_poem_which_praises_such_a_woman"),
			(assign, ":result", 0),
		(else_try), #adventurous ++, conventional -1, moralizing -1
			(eq, ":poem", courtship_poem_heroic),
			(eq, ":lady_reputation", lrep_conventional),
			(str_store_string, s11, "str_the_saga_of_helgered_and_kara_how_could_a_woman_don_armor_and_carry_a_sword_how_could_a_man_love_so_ungentle_a_creature"),
			(assign, ":result", 0),
			#Comic
		(else_try), #ambitious ++, romantic -, moralizing 0
			(eq, ":poem", courtship_poem_comic),
			(eq, ":lady_reputation", lrep_otherworldly),
			(str_store_string, s11, "str_a_conversation_in_the_garden_i_cannot_understand_the_lady_in_that_poem_if_she_loves_the_man_why_does_she_tease_him_so"),
			(assign, ":result", 0),
		(else_try), #ambitious ++, romantic -, moralizing 0
			(eq, ":poem", courtship_poem_comic),
			(eq, ":lady_reputation", lrep_moralist),
			(str_store_string, s11, "str_a_conversation_in_the_garden_let_us_see__it_is_morally_unedifying_it_exalts_deception_it_ends_with_a_maiden_surrendering_to_her_base_passions_and_yet_i_cannot_help_but_find_it_charming_perhaps_because_it_tells_us_that_love_need_not_be_tragic_to_be_memorable"),
			(assign, ":result", 1),
		(else_try), #ambitious ++, romantic -, moralizing 0
			(eq, ":poem", courtship_poem_comic),
			(eq, ":lady_reputation", lrep_ambitious),
			(str_store_string, s11, "str_a_conversation_in_the_garden_now_that_is_a_tale_every_lady_should_know_by_heart_to_learn_the_subtleties_of_the_politics_she_must_practice"),
			(assign, ":result", 5),
		(else_try), #ambitious ++, romantic -, moralizing 0
			(eq, ":poem", courtship_poem_comic),
			#adventurous, conventional
			(str_store_string, s11, "str_a_conversation_in_the_garden_it_is_droll_i_suppose__although_there_is_nothing_there_that_truly_stirs_my_soul"),
			(assign, ":result", 3),
			
			#Allegoric
		(else_try), #moralizing ++, adventurous -, romantic -
			(eq, ":poem", courtship_poem_allegoric),
			(eq, ":lady_reputation", lrep_adventurous),
			(str_store_string, s11, "str_storming_the_fortress_of_love_ah_yes_the_lady_sits_within_doing_nothing_while_the_man_is_the_one_who_strives_and_achieves_i_have_enough_of_that_in_my_daily_life_why_listen_to_poems_about_it"),
			(assign, ":result", 0),
		(else_try), #moralizing ++, adventurous -, romantic -
			(eq, ":poem", courtship_poem_allegoric),
			(this_or_next|eq, ":lady_reputation", lrep_conventional),
			(eq, ":lady_reputation", lrep_moralist),
			(str_store_string, s11, "str_storming_the_fortress_of_love_ah_yes_an_uplifting_tribute_to_the_separate_virtues_of_man_and_woman"),
			(assign, ":result", 3),
		(else_try), #moralizing ++, adventurous -, romantic -
			(eq, ":poem", courtship_poem_allegoric),
			(eq, ":lady_reputation", lrep_otherworldly),
			(str_store_string, s11, "str_storming_the_fortress_of_love_ah_yes_but_although_it_is_a_fine_tale_of_virtues_it_speaks_nothing_of_passion"),
			(assign, ":result", 1),
		(else_try), #moralizing ++, adventurous -, romantic -
			(eq, ":poem", courtship_poem_allegoric),
			(eq, ":lady_reputation", lrep_ambitious),
			(str_store_string, s11, "str_storming_the_fortress_of_love_ah_a_sermon_dressed_up_as_a_love_poem_if_you_ask_me"),
			(assign, ":result", 1),
			
		(else_try), #romantic ++, moralizing 0, ambitious -
			(eq, ":poem", courtship_poem_mystic),
			(eq, ":lady_reputation", lrep_otherworldly),
			(str_store_string, s11, "str_a_hearts_desire_ah_such_a_beautiful_account_of_the_perfect_perfect_love_to_love_like_that_must_be_to_truly_know_rapture"),
			(assign, ":result", 4),
			
		(else_try), #romantic ++, moralizing 0, ambitious -
			(eq, ":poem", courtship_poem_mystic),
			(eq, ":lady_reputation", lrep_ambitious),
			(str_store_string, s11, "str_a_hearts_desire_silly_if_you_ask_me_if_the_poet_desires_a_lady_then_he_should_endeavor_to_win_her__and_not_dress_up_his_desire_with_a_pretense_of_piety"),
			(assign, ":result", 0),
			
		(else_try), #romantic ++, moralizing 0, ambitious -
			(eq, ":poem", courtship_poem_mystic),
			(eq, ":lady_reputation", lrep_moralist),
			(str_store_string, s11, "str_a_hearts_desire_hmm__it_is_an_interesting_exploration_of_earthly_and_divine_love_it_does_speak_of_the_spiritual_quest_which_brings_out_the_best_in_man_but_i_wonder_if_the_poet_has_not_confused_his_yearning_for_higher_things_with_his_baser_passions"),
			(assign, ":result", 2),
			
		(else_try), #romantic ++, moralizing 0, ambitious -
			(eq, ":poem", courtship_poem_mystic),
			(str_store_string, s11, "str_a_hearts_desire_oh_yes__it_is_very_worthy_and_philosophical_but_if_i_am_to_listen_to_a_bard_strum_a_lute_for_three_hours_i_personally_prefer_there_to_be_a_bit_of_a_story"),
			(assign, ":result", 1),
		(try_end),
		
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg4, ":result"),
			(display_message, "str_result_reg4_string_s11"),
		(try_end),
		
		
		(assign, reg0, ":result"),
		
	]),
	
	(
		"diplomacy_faction_get_diplomatic_status_with_faction",
		#result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
		[
		(store_script_param, ":actor_faction", 1),
		(store_script_param, ":target_faction", 2),
		
		(store_add, ":truce_slot", ":target_faction", slot_faction_truce_days_with_factions_begin),
		(store_add, ":provocation_slot", ":target_faction", slot_faction_provocation_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
		(val_sub, ":provocation_slot", kingdoms_begin),
		
		(assign, ":result", 0),
		(assign, ":duration", 0),
		
		(try_begin),
			(store_relation, ":relation", ":actor_faction", ":target_faction"),
			(lt, ":relation", 0),
			(assign, ":result", -2),
		(else_try),
			(faction_slot_ge, ":actor_faction", ":truce_slot", 1),
			(assign, ":result", 1),
			
			(faction_get_slot, ":duration", ":actor_faction", ":truce_slot"),
		(else_try),
			(faction_slot_ge, ":actor_faction", ":provocation_slot", 1),
			(assign, ":result", -1),
			
			(faction_get_slot, ":duration", ":actor_faction", ":provocation_slot"),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":duration"),
	]),
	
	("faction_follows_controversial_policy",
		[
		(store_script_param, ":faction_no", 1),
		(store_script_param, ":policy_type", 2),
		
		(faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
		
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_faction_name, s3, ":faction_no"),
			(display_message, "str_calculating_effect_for_policy_for_s3"),
			
			(val_add, "$number_of_controversial_policy_decisions", 1),
			
		(try_end),
		
		(try_begin),
			(eq, ":policy_type", logent_policy_ruler_attacks_without_provocation),
			(assign, ":hawk_relation_effect", 0),
			(assign, ":honorable_relation_effect", -2),
			(assign, ":honor_change", -1),
			
		(else_try),
			(eq, ":policy_type", logent_policy_ruler_ignores_provocation),
			(assign, ":hawk_relation_effect", -3),
			(assign, ":honorable_relation_effect", 0),
			(assign, ":honor_change", 0),
			
		(else_try),
			(eq, ":policy_type", logent_policy_ruler_declares_war_with_justification),
			(assign, ":hawk_relation_effect", 3),
			(assign, ":honorable_relation_effect", 1),
			(assign, ":honor_change", 0),
			
		(else_try),
			(eq, ":policy_type", logent_policy_ruler_breaks_truce),
			(assign, ":hawk_relation_effect", 0),
			(assign, ":honorable_relation_effect", -3),
			(assign, ":honor_change", -5),
			
		(else_try),
			(eq, ":policy_type", logent_policy_ruler_makes_peace_too_soon),
			(assign, ":hawk_relation_effect", -5),
			(assign, ":honorable_relation_effect", 0),
			(assign, ":honor_change", 0),
			
		(try_end),
		
		(try_begin),
			(eq, ":faction_leader", "trp_player"),
			(call_script, "script_change_player_honor", ":honor_change"),
		(try_end),
		
		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":faction_no"),
			(neq, ":lord", ":faction_leader"),
			(try_begin),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_martial),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_quarrelsome),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
			(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
			(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", ":hawk_relation_effect"),
			(val_add, "$total_policy_dispute_changes", ":hawk_relation_effect"),
			(try_end),
			
			(try_begin),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_martial),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_benefactor), #new for enfiefed commoners
			(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_custodian), #new for enfiefed commoners
			(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_upstanding),
			(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", ":honorable_relation_effect"),
			(val_add, "$total_policy_dispute_changes", ":hawk_relation_effect"),
			
			(try_end),
			
		(try_end),
		
	]),
	
	
	("internal_politics_rate_feast_to_s9",
		[
		(store_script_param, ":householder", 1),
		(store_script_param, ":num_servings", 2),
		#	(store_script_param, ":faction", 3),
		(store_script_param, ":consume_items", 4),
		
		(val_max, ":num_servings", 1),
		
		(try_for_range, ":item", trade_goods_begin, trade_goods_end),
			(item_set_slot, ":item", slot_item_amount_available, 0), #had no "item"
		(try_end),
		
		(troop_get_inventory_capacity, ":capacity", ":householder"),
		(try_for_range, ":inventory_slot", 0, ":capacity"),
			(troop_get_inventory_slot, ":item", ":householder", ":inventory_slot"),
			(is_between, ":item", trade_goods_begin, trade_goods_end),
			(troop_inventory_slot_get_item_amount, ":slot_amount", ":householder", ":inventory_slot"),
			(item_get_slot, ":item_amount", ":item", slot_item_amount_available),
			(val_add, ":item_amount", ":slot_amount"),
			(item_set_slot, ":item", slot_item_amount_available, ":item_amount"),
		(try_end),
		#food
		(assign, ":food_amount", 0),
		(assign, ":food_variety", 0),
		
		(store_div, ":servings_div_by_12", ":num_servings", 12),
		(try_for_range, ":food_item", food_begin, food_end),
			(item_get_slot, ":food_in_slot", ":food_item", slot_item_amount_available),
			(val_add, ":food_amount", ":food_in_slot"),
			
			
			##		(str_store_item_name, s4, ":food_item"),
			##		(assign, reg3, ":food_in_slot"),
			##		(assign, reg5, ":servings_div_by_12"),
			##		(display_message, "str_reg3_units_of_s4_for_reg5_guests_and_retinue"),
			
			
			(ge, ":food_in_slot", ":servings_div_by_12"),
			(val_add, ":food_variety", 1),
		(try_end),
		
		(val_mul, ":food_amount", 100),
		(val_div, ":food_amount", ":num_servings"), #1 to 100 for each
		(val_min, ":food_amount", 100),
		
		(val_mul, ":food_variety", 85), #1 to 100 for each
		(val_div, ":food_variety", 10),
		(val_min, ":food_variety", 100),
		
		#drink
		(assign, ":drink_amount", 0),
		(assign, ":drink_variety", 0),
		(store_div, ":servings_div_by_4", ":num_servings", 4),
		(try_for_range, ":drink_iterator", "itm_wine", "itm_smoked_fish"),
			(assign, ":drink_item", ":drink_iterator"),
			(item_get_slot, ":drink_in_slot", ":drink_item", slot_item_amount_available),
			
			(val_add, ":drink_amount", ":drink_in_slot"),
			
			(ge, ":drink_in_slot", ":servings_div_by_4"),
			(val_add, ":drink_variety", 1),
		(try_end),
		
		(val_mul, ":drink_amount", 200), #amount needed is 50% of the number of guests
		(val_max, ":num_servings", 1),
		
		(val_div, ":drink_amount", ":num_servings"), #1 to 100 for each
		(val_min, ":drink_amount", 100),
		(val_mul, ":drink_variety", 50), #1 to 100 for each
		
		#in the future, it might be worthwhile to add different varieties of spices
		(item_get_slot, ":spice_amount", "itm_spice", slot_item_amount_available),
		(store_mul, ":spice_percentage", ":spice_amount", 100),
		(val_max, ":servings_div_by_12", 1),
		(val_div, ":spice_amount", ":servings_div_by_12"),
		(val_min, ":spice_percentage", 100),
		##	(assign, reg3, ":spice_amount"),
		##	(assign, reg5, ":servings_div_by_12"),
		##	(assign, reg6, ":spice_percentage"),
		##	(display_message, "str_reg3_units_of_spice_of_reg5_to_be_consumed"),
		
		#oil availability. In the future, this may become an "atmospherics" category, including incenses
		(item_get_slot, ":oil_amount", "itm_oil", slot_item_amount_available),
		(store_mul, ":oil_percentage", ":oil_amount", 100),
		(val_max, ":servings_div_by_12", 1),
		(val_div, ":oil_amount", ":servings_div_by_12"),
		(val_min, ":oil_percentage", 100),
		##	(assign, reg3, ":oil_amount"),
		##	(assign, reg5, ":servings_div_by_12"),
		##	(assign, reg6, ":oil_percentage"),
		##	(display_message, "str_reg3_units_of_oil_of_reg5_to_be_consumed"),
		
		(store_div, ":food_amount_string", ":food_amount", 20),
		(val_add, ":food_amount_string", "str_feast_description"),
		(str_store_string, s8, ":food_amount_string"),
		(str_store_string, s9, "str_of_food_which_must_come_before_everything_else_the_amount_is_s8"),
		
		(store_div, ":food_variety_string", ":food_variety", 20),
		(val_add, ":food_variety_string", "str_feast_description"),
		(str_store_string, s8, ":food_variety_string"),
		(str_store_string, s9, "str_s9_and_the_variety_is_s8_"),
		
		(store_div, ":drink_amount_string", ":drink_amount", 20),
		(val_add, ":drink_amount_string", "str_feast_description"),
		(str_store_string, s8, ":drink_amount_string"),
		(str_store_string, s9, "str_s9_of_drink_which_guests_will_expect_in_great_abundance_the_amount_is_s8"),
		
		(store_div, ":drink_variety_string", ":drink_variety", 20),
		(val_add, ":drink_variety_string", "str_feast_description"),
		(str_store_string, s8, ":drink_variety_string"),
		(str_store_string, s9, "str_s9_and_the_variety_is_s8_"),
		
		(store_div, ":spice_string", ":spice_percentage", 20),
		(val_add, ":spice_string", "str_feast_description"),
		(str_store_string, s8, ":spice_string"),
		(str_store_string, s9, "str_s9_of_spice_which_is_essential_to_demonstrate_that_we_spare_no_expense_as_hosts_the_amount_is_s8_"),
		
		(store_div, ":oil_string", ":oil_percentage", 20),
		(val_add, ":oil_string", "str_feast_description"),
		(str_store_string, s8, ":oil_string"),
		(str_store_string, s9, "str_s9_of_oil_which_we_shall_require_to_light_the_lamps_the_amount_is_s8"),
		
		(store_mul, ":food_amount_cap", ":food_amount", 8),
		(store_add, ":total", ":food_amount", ":food_variety"),
		(val_mul, ":total", 2), #x4
		(val_add, ":total", ":drink_variety"),
		(val_add, ":total", ":drink_amount"), #x6
		(val_add, ":total", ":spice_amount"), #x7
		(val_add, ":total", ":oil_amount"), #x8
		(val_min, ":total", ":food_amount_cap"),
		(val_div, ":total", 8),
		(val_clamp, ":total", 1, 101),
		(store_div, ":total_string", ":total", 20),
		(val_add, ":total_string", "str_feast_description"),
		(str_store_string, s8, ":total_string"),
		(str_store_string, s9, "str_s9_overall_our_table_will_be_considered_s8"),
		
		(assign, reg0, ":total"), #zero to 100
		
		
		
		(try_begin),
			(eq, ":consume_items", 1),
			
			(assign, ":num_of_servings_to_serve", ":num_servings"),
			(try_for_range, ":unused", 0, 1999),
			(gt, ":num_of_servings_to_serve", 0),
			
			(try_for_range, ":item", trade_goods_begin, trade_goods_end),
				(item_set_slot, ":item", slot_item_is_checked, 0),
			(try_end),
			
			(troop_get_inventory_capacity, ":inv_size", ":householder"),
			(try_for_range, ":i_slot", 0, ":inv_size"),
				(troop_get_inventory_slot, ":item", ":householder", ":i_slot"),
				(this_or_next|eq, ":item", "itm_spice"),
				(this_or_next|eq, ":item", "itm_oil"),
				(this_or_next|eq, ":item", "itm_wine"),
				(this_or_next|eq, ":item", "itm_ale"),
				(is_between, ":item",  food_begin, food_end),
				(item_slot_eq, ":item", slot_item_is_checked, 0),
				(troop_inventory_slot_get_item_amount, ":cur_amount", ":householder", ":i_slot"),
				(gt, ":cur_amount", 0),
				
				(val_sub, ":cur_amount", 1),
				(troop_inventory_slot_set_item_amount, ":householder", ":i_slot", ":cur_amount"),
				(val_sub, ":num_of_servings_to_serve", 1),
				(item_set_slot, ":item", slot_item_is_checked, 1),
			(try_end),
			(try_end),
		(try_end),
	]),
	
	
	("faction_get_adjective_to_s10",
		[
		(store_script_param, ":faction_no", 1),
		
		(try_begin),
			(eq, ":faction_no", "fac_player_faction"),
			(assign, ":faction_no", "$players_kingdom"),
		(try_end),
		
		
		(try_begin),
			(eq, ":faction_no", "fac_player_supporters_faction"),
			(str_store_string, s10, "str_rebel"),
		(else_try),
			(this_or_next|eq, ":faction_no", "fac_outlaws"),
			(this_or_next|eq, ":faction_no", "fac_mountain_bandits"),
			(this_or_next|eq, ":faction_no", "fac_forest_bandits"),
			(eq, ":faction_no", "fac_deserters"),
			(str_store_string, s10, "str_bandit"),
		(else_try),
			(faction_get_slot, ":adjective_string", ":faction_no", slot_faction_adjective),
			(str_store_string, s10, ":adjective_string"),
		(try_end),
	]),
	
	("setup_tavern_attacker",
		[
		(store_script_param, ":cur_entry", 1),
		
		#tom
		#this is orignal
		(try_begin),
			(neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
			(troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),
			(set_visitor, ":cur_entry", "trp_belligerent_drunk"),
		#(try_end),
		(else_try),#this is not
			(store_random_in_range, ":random", 0, 101),
			(le, ":random", 10),
			(set_visitor, ":cur_entry", "trp_belligerent_drunk"),
		(try_end),
		#tom
		
		(try_begin),
			(troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
			(set_visitor, ":cur_entry", "trp_hired_assassin"),
		(try_end),
	]),
	
	("activate_tavern_attackers",
		[
		(set_party_battle_mode),
		(try_for_agents, ":cur_agent"),
			(agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
			(this_or_next|eq, ":cur_agent_troop", "trp_fugitive"),
			(this_or_next|eq, ":cur_agent_troop", "trp_belligerent_drunk"),
			(eq, ":cur_agent_troop", "trp_hired_assassin"),
			(agent_set_team, ":cur_agent", 1),
			(assign, "$g_main_attacker_agent", ":cur_agent"),
			(agent_ai_set_aggressiveness, ":cur_agent", 199),
		(try_end),
	]),
	
	("deactivate_tavern_attackers",
		[
		(finish_party_battle_mode),
		(try_for_agents, ":cur_agent"),
			(agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
			(this_or_next|eq, ":cur_agent_troop", "trp_fugitive"),
			(this_or_next|eq, ":cur_agent_troop", "trp_belligerent_drunk"),
			(eq, ":cur_agent_troop", "trp_hired_assassin"),
			(agent_set_team, ":cur_agent", 0),
			(agent_ai_set_aggressiveness, ":cur_agent", 0),
		(try_end),
	]),
	
	("activate_town_guard",
		[
		(set_party_battle_mode),
		#(get_player_agent_no, ":player_agent"),
		#(agent_get_team, ":player_team", ":player_agent"),
		
		(try_for_agents, ":cur_agent"),
			(agent_get_troop_id, ":troop_type", ":cur_agent"),
			#(is_between, ":troop_type", "trp_teu_village_recruit", "trp_looter"), #tom
			(is_between, ":troop_type", "trp_finn_village_recruit", "trp_xerina"), #tom
			(agent_set_team, ":cur_agent", 1),
			#(team_give_order, 1, grc_everyone, mordr_charge), - for some reason, this freezes everyone if the player is not yet spawned
			#(try_begin),
			#	(eq, "$g_main_attacker_agent", 0),
			#	(assign, "$g_main_attacker_agent", ":cur_agent"),
			#(try_end),
		(else_try),
			(this_or_next|is_between, ":cur_agent", walkers_begin, walkers_end),
			(is_between, ":cur_agent", armor_merchants_begin, mayors_end),
			
			(agent_clear_scripted_mode, ":cur_agent"),
			(agent_set_team, ":cur_agent", 2),
		(try_end),
	]),
	
	
	#this determines whether or not a lord is thrown into a dungeon by his captor, or is kept out on parole
	#Not currently used (ie, it always fails)
	("cf_prisoner_offered_parole",
		[
		(store_script_param, ":prisoner", 1),
		
		(eq, 1, 0), #disabled, this will always return false
		
		(troop_get_slot, ":captor_party", ":prisoner", slot_troop_prisoner_of_party),
		(party_is_active, ":captor_party"),
		(is_between, ":captor_party", walled_centers_begin, walled_centers_end),
		(party_get_slot, ":captor", ":captor_party", slot_town_lord),
		
		(troop_get_slot, ":prisoner_rep", ":prisoner", slot_lord_reputation_type),
		(troop_get_slot, ":captor_rep", ":captor", slot_lord_reputation_type),
		
		(neq, ":prisoner_rep", lrep_debauched),
		(neq, ":captor_rep", lrep_debauched),
		(neq, ":captor_rep", lrep_quarrelsome),
		
		#Prisoner is a noble, or lord is goodnatured
		(this_or_next|eq, ":captor_rep", lrep_goodnatured),
		(this_or_next|troop_slot_eq, ":prisoner", slot_troop_occupation, slto_kingdom_hero),
		(troop_slot_eq, ":prisoner", slot_troop_occupation, slto_kingdom_lady),
		
		(call_script, "script_troop_get_relation_with_troop", ":captor", ":prisoner"),
		##	(display_message, "str_relation_of_prisoner_with_captor_is_reg0"),
		(ge, reg0, -10),
	]),
	
	("neutral_behavior_in_fight",
		[
		(get_player_agent_no, ":player_agent"),
		(agent_get_position, pos3, ":player_agent"),
		(agent_get_team, ":player_team", ":player_agent"),
		
		(try_begin),
			(gt, "$g_main_attacker_agent", 0),
			(agent_get_team, ":attacker_team_no", "$g_main_attacker_agent"),
			(agent_get_position, pos5, "$g_main_attacker_agent"),
		(else_try),
			(eq, ":attacker_team_no", -1),
			(agent_get_position, pos5, ":player_agent"),
		(try_end),
		
		(set_fixed_point_multiplier, 100),
		
		(try_for_agents, ":agent"),
			(agent_get_team, ":other_team", ":agent"),
			(neq, ":other_team", ":attacker_team_no"),
			(neq, ":other_team", ":player_team"),
			
			(agent_get_troop_id, ":troop_id", ":agent"),
			(neg|is_between, ":troop_id", "trp_teu_village_recruit", "trp_looter"),
			
			(agent_get_position, pos4, ":agent"),
			
			(assign, ":best_position_score", 0),
			(assign, ":best_position", -1),
			
			(try_begin),
			(neg|agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #if agent is running away
			(agent_get_slot, ":target_entry_point_plus_one",  ":agent", slot_agent_is_running_away),
			(store_sub, ":target_entry_point", ":target_entry_point_plus_one", 1),
			(entry_point_get_position, pos6, ":target_entry_point"),
			(get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
			(lt, ":agent_distance_to_target", 100),
			(agent_set_slot, ":agent", slot_agent_is_running_away, 0),
			(try_end),
			
			(agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #if agent is not already running away
			
			(try_begin), #stand in place
			(get_distance_between_positions, ":distance", pos4, pos5),
			(get_distance_between_positions, ":distance_to_player", pos4, pos3),
			
			(val_min, ":distance", ":distance_to_player"),
			
			(this_or_next|gt, ":distance", 700), #7 meters away from main belligerents
			(main_hero_fallen),
			
			(agent_set_scripted_destination, ":agent", pos4),
			(else_try), #get out of the way
			(try_for_range, ":target_entry_point", 0, 64),
				(neg|entry_point_is_auto_generated, ":target_entry_point"),
				(entry_point_get_position, pos6, ":target_entry_point"),
				(get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
				(get_distance_between_positions, ":player_distance_to_target", pos6, pos3),
				(store_sub, ":position_score", ":player_distance_to_target", ":agent_distance_to_target"),
				(ge, ":position_score", 0),
				(try_begin),
				(ge, ":agent_distance_to_target", 2000),
				(store_sub, ":extra_distance", ":agent_distance_to_target", 2000),
				(val_min, ":extra_distance", 1000),
				(val_min, ":agent_distance_to_target", 2000), #if more than 10 meters assume it is 10 meters far while calculating best run away target
				(val_sub, ":agent_distance_to_target", ":extra_distance"),
				(try_end),
				(val_mul, ":position_score", ":agent_distance_to_target"),
				(try_begin),
				(ge, ":position_score", ":best_position_score"),
				(assign, ":best_position_score", ":position_score"),
				(assign, ":best_position", ":target_entry_point"),
				(try_end),
			(try_end),
			
			(try_begin),
				(ge, ":best_position", 0),
				(entry_point_get_position, pos6, ":best_position"),
				(agent_set_speed_limit, ":agent", 10),
				(agent_set_scripted_destination, ":agent", pos6),
				(store_add, ":best_position_plus_one", ":best_position", 1),
				(agent_set_slot, ":agent", slot_agent_is_running_away, ":best_position_plus_one"),
			(try_end),
			(try_end),
		(try_end),
	]),
	
	("party_inflict_attrition", #parameters from dialog
		[
		(store_script_param, ":party", 1),
		(store_script_param, ":attrition_rate", 2),
		#	(store_script_param, ":attrition_type", 3), #1 = desertion, 2 = sickness
		
		(party_clear, "p_temp_casualties"),
		
		(party_get_num_companion_stacks, ":num_stacks", ":party"),
		
		#add to temp casualties
		(try_for_range, ":stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":troop_type", ":party", ":stack"),
			(neg|troop_is_hero, ":troop_type"),
			(party_stack_get_size, ":size", ":party", ":stack"),
			(store_mul, ":casualties_x_100", ":attrition_rate", ":size"),
			(store_div, ":casualties", ":casualties_x_100", 100),
			(party_add_members, "p_temp_casualties", ":troop_type", ":casualties"),
			
			(store_mul, ":subtractor", ":casualties", 100),
			(store_sub, ":chance_of_additional_casualty", ":casualties_x_100", ":subtractor"),
			
			(try_begin),
			(gt, ":chance_of_additional_casualty", 0),
			(store_random_in_range, ":random", 0, 100),
			(lt, ":random", ":chance_of_additional_casualty"),
			(party_add_members, "p_temp_casualties", ":troop_type", ":casualties"),
			(try_end),
			
			#		(try_begin),
			#			(eq, "$cheat_mode", 1),
			#			(str_store_party_name, s7, ":party"),
			#           		...
			#		(try_end),
		(try_end),
		
		#take temp casualties from main party
		(party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
		
		#add to temp casualties
		(try_for_range, ":stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":troop_type", "p_temp_casualties", ":stack"),
			(party_stack_get_size, ":size", "p_temp_casualties", ":stack"),
			(party_remove_members, ":party", ":troop_type", ":size"),
			
			(eq, "$cheat_mode", 1),
			(assign, reg3, ":size"),
			(str_store_troop_name, s4, ":troop_type"),
			(str_store_party_name, s5, ":party"),
			#		(display_message, "str_s5_suffers_attrition_reg3_x_s4"),
			(str_store_string, s65, "str_s5_suffers_attrition_reg3_x_s4"),
			(display_message, "str_s65"),
			#tom
			# (try_begin),
			# (eq, "$debug_message_in_queue", 0),
			# (call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
			# (assign, "$debug_message_in_queue", 1),
			# (try_end),
			#tom
		(try_end),
		(call_script, "script_party_calculate_strength", ":party", 1, 0), # rafi
		
	]),
	
	
	
	
	("add_rumor_string_to_troop_notes", #parameters from dialog
		[
		(store_script_param, ":object_1", 1),
		(store_script_param, ":object_2", 2),
		(store_script_param, ":string", 3),
		
		(str_store_troop_name, s10, "$g_talk_troop"),
		(str_store_string_reg, s11, ":string"),
		
		(store_current_hours, ":hours"),
		(call_script, "script_game_get_date_text", 0, ":hours"),
		
		(str_store_string, s5, "str_s10_said_on_s1_s11__"),
		
		(try_begin),
			(is_between, ":object_1", active_npcs_begin, kingdom_ladies_end),
			(troop_get_slot, ":current_rumor_note", ":object_1", slot_troop_current_rumor),
			(val_add, ":current_rumor_note", 1),
			(try_begin),
			(neg|is_between, ":current_rumor_note", 3, 16),
			(assign, ":current_rumor_note", 3),
			(try_end),
			(troop_set_slot, ":object_1", slot_troop_current_rumor, ":current_rumor_note"),
			
			(add_troop_note_from_sreg, ":object_1", ":current_rumor_note", s5, 0), #troop, note slot, string, show
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s3, ":object_1"),
			(assign, reg4, ":current_rumor_note"),
			(display_message, "str_rumor_note_to_s3s_slot_reg4_s5"),
			(try_end),
		(try_end),
		
		(try_begin),
			(is_between, ":object_2", active_npcs_begin, kingdom_ladies_end),
			(troop_get_slot, ":current_rumor_note", ":object_2", slot_troop_current_rumor),
			(val_add, ":current_rumor_note", 1),
			(try_begin),
			(neg|is_between, ":current_rumor_note", 3, 16),
			(assign, ":current_rumor_note", 3),
			(try_end),
			(troop_set_slot, ":object_2", slot_troop_current_rumor, ":current_rumor_note"),
			
			(add_troop_note_from_sreg, ":object_2", ":current_rumor_note", s5, 0), #troop, note slot, string, show
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s3, ":object_2"),
			(assign, reg4, ":current_rumor_note"),
			(display_message, "str_rumor_note_to_s3s_slot_reg4_s5"),
			(try_end),
		(try_end),
	]),
	
	("character_can_wed_character", #empty now, but might want to add mid-game
		[
	]),
	
	("troop_change_career", #empty now, but might want to add mid-game
		[
	]),
	
	("center_get_goods_availability",
		[
		(store_script_param, ":center_no", 1),
		
		(str_store_party_name, s4, ":center_no"),
		
		(assign, ":hardship_index", 0),
		(try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
			#Must have consumption of at least 4 to be relevant
			#This prevents perishables and raw materials from having a major impact
			(try_begin),
			(is_between, ":center_no", villages_begin, villages_end),
			(item_get_slot, ":consumer_consumption", ":cur_good", slot_item_rural_demand),
			(else_try),
			(item_get_slot, ":consumer_consumption", ":cur_good", slot_item_urban_demand),
			(try_end),
			(gt, ":consumer_consumption", 2),
			
			(store_div, ":max_impact", ":consumer_consumption", 4), #was 4
			
			#High-demand items like grain tend to have much more dramatic price differentiation, so they yield substantially higher results than low-demand items
			
			(store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
			(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
			(party_get_slot, ":price", ":center_no", ":cur_good_price_slot"),
			
			(store_sub, ":price_differential", ":price", 1000),
			(gt, ":price_differential", 200), #was 100
			
			(val_div, ":price_differential", 200),
			(val_min, ":price_differential", ":max_impact"),
			
			(val_add, ":hardship_index", ":price_differential"),
		(try_end),
		
		(assign, reg0, ":hardship_index"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG -- hardship index for {s4} = {reg0}"),
		(try_end),
	]),

	("lord_find_alternative_faction", #Also, make it so that lords will try to keep at least one center unassigned
	[
		(store_script_param, ":troop_no", 1),
		(store_faction_of_troop, ":orig_faction", ":troop_no"),
		
		(assign, ":new_faction", -1),
		(assign, ":score_to_beat", -5),
		
		##tom
		(assign, ":num_centers", 0),
		(try_for_range, ":centers", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":center_faction", ":centers"),
		(eq, ":orig_faction", ":center_faction"),
		(val_add, ":num_centers", 1),
		(try_end),
		(try_begin),
			(eq, ":num_centers", 0),
		(neq, ":orig_faction", "fac_player_supporters_faction"),
		(assign, ":score_to_beat", -100), ##a definite defection
		(try_end),
		##tom

		(try_begin),
			(store_random_in_range, ":advantegous_faction_change_time", 0, 10000), 

			(this_or_next|le, "$g_advantegous_faction", 0),
		(eq, ":advantegous_faction_change_time", 0),
		(store_random_in_range, "$g_advantegous_faction", kingdoms_begin, kingdoms_end), 
		(try_end),

		(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),	  
			(this_or_next|eq, "$g_give_advantage_to_original_faction", 1),
		(neq, ":faction_no", ":orig_faction"),
		 
			(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			(assign, ":number_of_walled_centers", 0),
			(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":center_faction", ":center_no"),
			(eq, ":center_faction", ":faction_no"),

			(try_begin),
				(party_slot_eq, ":center_no", slot_party_type, spt_town),
			(val_add, ":number_of_walled_centers", 2),
			(else_try),
				(val_add, ":number_of_walled_centers", 1),
			(try_end),
		(try_end),

			(assign, ":number_of_lords", 0),
				(try_for_range, ":troop_id", original_kingdom_heroes_begin, active_npcs_end),
					(store_troop_faction, ":faction_of_troop", ":troop_id"),
					(eq, ":faction_of_troop", ":faction_no"),
			(val_add, ":number_of_lords", 1),
				(try_end),
		(val_max, ":number_of_lords", 1),

				(faction_get_slot, ":liege", ":faction_no", slot_faction_leader),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
		(assign, ":relation_with_leader", reg0),

		(store_mul, ":faction_score", ":number_of_walled_centers", 100),
		(val_div, ":faction_score", ":number_of_lords"),
		(val_add, ":faction_score", ":relation_with_leader"),

		(try_begin),
			(eq, ":faction_no", ":orig_faction"),
			(eq, "$g_give_advantage_to_original_faction", 1),
			(val_add, ":faction_score", 100),
		(try_end),

		(try_begin),
			(eq, "$g_advantegous_faction", ":faction_no"),
			(val_add, ":faction_score", 50),
		(try_end),

		(try_begin),
			(eq, ":faction_no", "$players_kingdom"),
			(val_sub, ":faction_score", 100),
			(val_add, "$player_right_to_rule"),
		(try_end),

		(gt, ":faction_score", ":score_to_beat"),

		(assign, ":score_to_beat", ":faction_score"),
				(assign, ":new_faction", ":faction_no"),
		(try_end),
				
		(assign, reg0, ":new_faction"),	
	]),
	
	 #reverted back to 1.134 
	 ("lord_find_alternative_faction_old", #Also, make it so that lords will try to keep at least one center unassigned
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
	]),
	
	("set_up_duel_with_troop", #now the setup is handled through the menu
		[
		(store_script_param, "$g_duel_troop", 1),
		(assign, "$g_start_arena_fight_at_nearest_town", 1),
		(try_begin),
			(eq, "$g_start_arena_fight_at_nearest_town", 1),
		(try_end),
		(unlock_achievement, ACHIEVEMENT_PUGNACIOUS_D),
		(jump_to_menu, "mnu_arena_duel_fight"),
		(finish_mission),
		
	]),
	
	("test_player_for_career_and_marriage_incompatability", #empty now, but might want to add mid-game
		[
		#Married to a lord of one faction, while fighting for another
		#Married to one lord while holding a stipend from the king
	]),
	
	("deduct_casualties_from_garrison", #after a battle in a center, deducts any casualties from "$g_encountered_party"
		[
		##(display_message, "str_totalling_casualties_caused_during_mission"),
		
		(try_for_agents, ":agent"),
			(agent_get_troop_id, ":troop_type", ":agent"),
			(is_between, ":troop_type", regular_troops_begin, regular_troops_end),
			
			(neg|agent_is_alive, ":agent"),
			
			(try_begin), #if troop not present, search for another type which is
			(store_troop_count_companions, ":number", ":troop_type", "$g_encountered_party"),
			(eq, ":number", 0),
			(assign, ":troop_type", 0),
			(try_for_range, ":new_tier", slot_faction_tier_1_troop, slot_faction_tier_5_troop),
				(faction_get_slot, ":troop_type", "$g_encountered_party_faction", ":new_tier"),
				(faction_get_slot, ":new_troop_type", "$g_encountered_party_faction", ":new_tier"),
				(store_troop_count_companions, ":number", ":new_troop_type", "$g_encountered_party"),
				(gt, ":number", 0),
				(assign, ":troop_type", ":new_troop_type"),
			(try_end),
			(try_end),
			
			(gt, ":troop_type", 0),
			
			(party_remove_members, "$g_encountered_party", ":troop_type", 1),
			(str_store_troop_name, s4, ":troop_type"),
			(str_store_party_name, s5, "$g_encountered_party"),
		(try_end),
	]),
	
	("npc_decision_checklist_take_stand_on_issue",
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
		
	]),
	
	
	("npc_decision_checklist_evaluate_faction_strategy",
		[
		#Decides whether the strategy is good or bad -- to be added
	]),
	
	
	("process_player_enterprise",
		#reg0: Profit per cycle
		[
		(store_script_param, ":item_type", 1),
		(store_script_param, ":center", 2),
		
		(item_get_slot, ":price_of_labor", ":item_type", slot_item_overhead_per_run),
		
		(item_get_slot, ":base_price", ":item_type", slot_item_base_price),
		(store_sub, ":cur_good_price_slot", ":item_type", trade_goods_begin),
		(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
		(party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
		(store_mul, ":final_price_for_single_produced_good", ":base_price", ":cur_price_modifier"),
		(val_div, ":final_price_for_single_produced_good", 1000),
		(item_get_slot, ":number_of_outputs_produced", ":item_type", slot_item_output_per_run),
		(store_mul, ":final_price_for_total_produced_goods", ":number_of_outputs_produced", ":final_price_for_single_produced_good"),
		
		(item_get_slot, ":primary_raw_material", ":item_type", slot_item_primary_raw_material),
		(item_get_slot, ":base_price", ":primary_raw_material", slot_item_base_price),
		(store_sub, ":cur_good_price_slot", ":primary_raw_material", trade_goods_begin),
		(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
		(party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
		(store_mul, ":final_price_for_single_input", ":base_price", ":cur_price_modifier"),
		(val_div, ":final_price_for_single_input", 1000),
		(item_get_slot, ":number_of_inputs_required", ":item_type", slot_item_input_number),
		(try_begin),
			(lt, ":number_of_inputs_required", 0),
			(store_div, ":final_price_for_total_inputs", ":final_price_for_single_input", 2),
		(else_try),
			(store_mul, ":final_price_for_total_inputs", ":final_price_for_single_input", ":number_of_inputs_required"),
		(try_end),
		
		(try_begin),
			(item_slot_ge, ":item_type", slot_item_secondary_raw_material, 1),
			(item_get_slot, ":secondary_raw_material", ":item_type", slot_item_secondary_raw_material),
			(item_get_slot, ":base_price", ":secondary_raw_material", slot_item_base_price),
			(store_sub, ":cur_good_price_slot", ":secondary_raw_material", trade_goods_begin),
			(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
			(party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
			
			(try_begin),
			(lt, ":number_of_inputs_required", 0),
			(store_div, ":final_price_for_secondary_input", ":final_price_for_secondary_input", 2),
			(else_try),
			(store_mul, ":final_price_for_secondary_input", ":final_price_for_secondary_input", ":number_of_inputs_required"),
			(try_end),
			
			(store_mul, ":final_price_for_secondary_input", ":base_price", ":cur_price_modifier"),
			(val_div, ":final_price_for_secondary_input", 1000),
		(else_try),
			(assign, ":final_price_for_secondary_input", 0),
		(try_end),
		
		(store_sub, ":profit_per_cycle", ":final_price_for_total_produced_goods", ":final_price_for_total_inputs"),
		(val_sub, ":profit_per_cycle", ":price_of_labor"),
		(val_sub, ":profit_per_cycle", ":final_price_for_secondary_input"),
		
		(assign, reg0, ":profit_per_cycle"),
		(assign, reg1, ":final_price_for_total_produced_goods"),
		(assign, reg2, ":final_price_for_total_inputs"),
		(assign, reg3, ":price_of_labor"),
		(assign, reg4, ":final_price_for_single_produced_good"),
		(assign, reg5, ":final_price_for_single_input"),
		(assign, reg10, ":final_price_for_secondary_input"),
	]),
	
	# script_replace_scene_items_with_spawn_items_before_ms
	# Input: none
	# Output: none
	("replace_scene_items_with_spawn_items_before_ms",
		[
		(try_for_range, ":item_no", all_items_begin, all_items_end),
			(scene_item_get_num_instances, ":num_instances", ":item_no"),
			(item_set_slot, ":item_no", slot_item_num_positions, 0),
			(assign, ":num_positions", 0),
			(try_for_range, ":cur_instance", 0, ":num_instances"),
			(scene_item_get_instance, ":scene_item", ":item_no", ":cur_instance"),
			(prop_instance_get_position, "$g_position_to_use_for_replacing_scene_items", ":scene_item"),
			(store_add, ":cur_slot", slot_item_positions_begin, ":num_positions"),
			(item_set_slot, ":item_no", ":cur_slot", "$g_position_to_use_for_replacing_scene_items"),
			(val_add, ":num_positions", 1),
			(val_add, "$g_position_to_use_for_replacing_scene_items", 1),
			(item_set_slot, ":item_no", slot_item_num_positions, ":num_positions"),
			(try_end),
			(replace_scene_items_with_scene_props, ":item_no", "spr_empty"),
		(try_end),
	]),
	
	# script_replace_scene_items_with_spawn_items_after_ms
	# Input: none
	# Output: none
	("replace_scene_items_with_spawn_items_after_ms",
		[
		(try_for_range, ":item_no", all_items_begin, all_items_end),
			(item_get_slot,  ":num_positions", ":item_no", slot_item_num_positions),
			(try_for_range, ":cur_position", 0, ":num_positions"),
			(store_add, ":cur_slot", slot_item_positions_begin, ":cur_position"),
			(item_get_slot, ":pos_no", ":item_no", ":cur_slot"),
			(set_spawn_position, ":pos_no"),
			(spawn_item, ":item_no", 0),
			(try_end),
		(try_end),
	]),
	
	# script_cf_is_melee_weapon_for_tutorial
	# Input: arg1 = item_no
	# Output: none (can fail)
	("cf_is_melee_weapon_for_tutorial",
		[
		(store_script_param, ":item_no", 1),
		(assign, ":result", 0),
		(try_begin),
			(this_or_next|eq, ":item_no", "itm_quarter_staff"),
			(eq, ":item_no", "itm_practice_sword"),
			(assign, ":result", 1),
		(try_end),
		(eq, ":result", 1),
	]),
	
	# script_iterate_pointer_arrow
	# Input: none
	# Output: none
	("iterate_pointer_arrow",
		[
		(store_mission_timer_a_msec, ":cur_time"),
		(try_begin),
			(assign, ":up_down", ":cur_time"),
			(assign, ":turn_around", ":cur_time"),
			(val_mod, ":up_down", 1080),
			(val_div, ":up_down", 3),
			(scene_prop_get_instance, ":prop_instance", "spr_pointer_arrow", 0),
			(prop_instance_get_position, pos0, ":prop_instance"),
			(position_set_z_to_ground_level, pos0),
			(position_move_z, pos0, "$g_pointer_arrow_height_adder", 1),
			(set_fixed_point_multiplier, 100),
			(val_mul, ":up_down", 100),
			(store_sin, ":up_down_sin", ":up_down"),
			(position_move_z, pos0, ":up_down_sin", 1),
			(position_move_z, pos0, 100, 1),
			(val_mod, ":turn_around", 2880),
			(val_div, ":turn_around", 8),
			(init_position, pos1),
			(position_rotate_z, pos1, ":turn_around"),
			(position_copy_rotation, pos0, pos1),
			(prop_instance_set_position, ":prop_instance", pos0),
		(try_end),
	]),
	
	("find_center_to_attack_alt",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":attack_by_faction", 2),
		(store_script_param, ":all_vassals_included", 3),
		
		(assign, ":result", -1),
		(assign, ":score_to_beat", 0),
		
		(try_for_range, ":center_no", centers_begin, centers_end),
			(call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack",	":troop_no", ":center_no", ":attack_by_faction", ":all_vassals_included"),
			(assign, ":score", reg0),
			
			(gt, ":score", ":score_to_beat"),
			
			(assign, ":result", ":center_no"),
			(assign, ":score_to_beat", ":score"),
		(try_end),
		
		(assign, reg0, ":result"),
		(assign, reg1, ":score_to_beat"),
	]),
	
	("npc_decision_checklist_evaluate_enemy_center_for_attack",
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
	]),
	
	(
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
	]),
	
	(
		"faction_last_reconnoitered_center", #This is called from within decide_faction_ai, or from
		[
		(store_script_param, ":faction_no", 1),
		(store_script_param, ":center_no", 2),
		
		(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
		(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
		(store_current_hours, ":hours_since_last_recon"),
		(party_get_slot, ":last_recon_time", ":center_no", ":faction_recce_slot"),
		
		(try_begin),
			(lt, ":last_recon_time", 1),
			(assign, ":hours_since_last_recon", 1000),
		(else_try),
			(val_sub, ":hours_since_last_recon", ":last_recon_time"),
		(try_end),
		
		(assign, reg0, ":hours_since_last_recon"),
		(assign, reg1, ":last_recon_time"),
	]),
	
	(
		"reduce_exact_number_to_estimate",
		#This is used to simulate limited intelligence
		#It is roughly analogous to the descriptive strings which the player will receive from alarms
		#Information is presumed to be accurate for four days
		#This is obviously cheating for the AI, as the AI will have exact info for four days, and no info at all after that.
		#It would be fairly easy to log the strength at a center when it is scouted, if we want, but I have not done that at this point,
		#The AI also has a hive mind -- ie, each party knows what its allies are thinking. In this, AI factions have an advantage over the player
		#It would be a simple matter to create a set of arrays in which each party's knowledge is individually updated, but that would also take up a lot of data space
		
		[
		(store_script_param, ":exact_number", 1),
		
		(try_begin),
			(lt, ":exact_number", 500),
			(assign, ":estimate", 0),
		(else_try),
			(lt, ":exact_number", 1000),
			(assign, ":estimate", 750),
		(else_try),
			(lt, ":exact_number", 2000),
			(assign, ":estimate", 1500),
		(else_try),
			(lt, ":exact_number", 4000),
			(assign, ":estimate", 3000),
		(else_try),
			(lt, ":exact_number", 8000),
			(assign, ":estimate", 6000),
		(else_try),
			(lt, ":exact_number", 16000),
			(assign, ":estimate", 12000),
		(else_try),
			(assign, ":estimate", 24000),
		(try_end),
		
		(assign, reg0, ":estimate"),
	]),
	
	#script_calculate_castle_prosperities_by_using_its_villages
	(
		"calculate_castle_prosperities_by_using_its_villages", #This is called from within decide_faction_ai, or from
		[
		(try_for_range, ":cur_castle", castles_begin, castles_end),
			(assign, ":total_prosperity", 0),
			(assign, ":total_villages", 0),
			
			(try_for_range, ":cur_village", villages_begin, villages_end),
			(party_get_slot, ":bound_center", ":cur_village", slot_village_bound_center),
			(eq, ":cur_castle", ":bound_center"),
			
			(party_get_slot, ":village_prosperity", ":cur_village", slot_town_prosperity),
			
			(val_add, ":total_prosperity", ":village_prosperity"),
			(val_add, ":total_villages", 1),
			(try_end),
			
			(try_begin),
			(neg|eq, ":total_villages", 0), #tom
			(store_div, ":castle_prosperity", ":total_prosperity", ":total_villages"),
			(else_try),
			(assign, ":castle_prosperity", 50),
			(try_end),
			
			(party_set_slot, ":cur_castle", slot_town_prosperity, ":castle_prosperity"),
		(try_end),
	]),
	
	#script_initialize_tavern_variables
	(
		"initialize_tavern_variables",
		[
		(assign, "$g_main_attacker_agent", 0),
		(assign, "$g_attacker_drawn_weapon", 0),
		(assign, "$g_start_belligerent_drunk_fight", 0),
		(assign, "$g_start_hired_assassin_fight", 0),
		(assign, "$g_belligerent_drunk_leaving", 0),
	]),
	
	#script_prepare_alley_to_fight
	(
		"prepare_alley_to_fight",
		[
		(party_get_slot, ":scene_no", "$current_town", slot_town_alley),
		
		#(store_faction_of_party, ":faction_no", "$current_town"),
		
		(modify_visitors_at_site, ":scene_no"),
		
		(reset_visitors),
		(set_visitor, 0, "trp_player"),
		
		#(try_begin),
		#  (eq, ":faction_no", "fac_kingdom_1"), #swadian
		#  (assign, ":bandit_troop", "trp_steppe_bandit"),
		#(else_try),
		#  (eq, ":faction_no", "fac_kingdom_2"), #vaegir
		#  (assign, ":bandit_troop", "trp_taiga_bandit"),
		#(else_try),
		#  (eq, ":faction_no", "fac_kingdom_3"), #khergit
		#  (assign, ":bandit_troop", "trp_mountain_bandit"),
		#(else_try),
		#  (eq, ":faction_no", "fac_kingdom_4"), #nord
		#  (assign, ":bandit_troop", "trp_sea_raider"),
		#(else_try),
		#  (eq, ":faction_no", "fac_kingdom_5"), #rhodok
		#  (assign, ":bandit_troop", "trp_forest_bandit"),
		#(else_try),
		#  (eq, ":faction_no", "fac_kingdom_6"), #sarradin
		#  (assign, ":bandit_troop", "trp_desert_bandit"),
		#(try_end),
		
		#(set_visitor, 3, ":bandit_troop"),
		(set_visitor, 3, "trp_bandit"),
		
		(assign, "$talked_with_merchant", 0),
		(set_jump_mission, "mt_alley_fight"),
		(jump_to_scene, ":scene_no"),
		(change_screen_mission),
	]),
	
	#script_prepare_town_to_fight
	(
		"prepare_town_to_fight",
		[
		(str_store_party_name_link, s9, "$g_starting_town"),
		(str_store_string, s2, "str_save_town_from_bandits"),
		(call_script, "script_start_quest", "qst_save_town_from_bandits", "$g_talk_troop"),
		
		(assign, "$g_mt_mode", tcm_default),
		(store_faction_of_party, ":town_faction", "$current_town"),
		(faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
		(faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
		(faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),
		
		(party_get_slot, ":town_scene", "$current_town", slot_town_center),
		(modify_visitors_at_site, ":town_scene"),
		(reset_visitors),
		
		#people spawned at #32, #33, #34, #35, #36, #37, #38 and #39 are town walkers.
		(try_begin),
			#(eq, "$town_nighttime", 0),
			(try_for_range, ":walker_no", 0, num_town_walkers),
			(store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
			(party_get_slot, ":walker_troop_id", "$current_town", ":troop_slot"),
			(gt, ":walker_troop_id", 0),
			(store_add, ":entry_no", town_walker_entries_start, ":walker_no"),
			(set_visitor, ":entry_no", ":walker_troop_id"),
			(try_end),
		(try_end),
		
		#guards will be spawned at #25, #26 and #27
		(set_visitors, 25, ":tier_2_troop", 1),
		(set_visitors, 26, ":tier_3_troop", 1),
		(set_visitors, 27, ":tier_4_troop", 1),
		
		(set_visitors, 10, "trp_looter", 1),
		(set_visitors, 11, "trp_bandit", 1),
		(set_visitors, 12, "trp_looter", 1),
		
		(store_faction_of_party, ":starting_town_faction", "$g_starting_town"),
		(try_begin),
			(eq, ":starting_town_faction", "fac_kingdom_1"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_1"),
			#(assign, ":troop_of_bandit", "trp_forest_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_2"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_2"),
			#(assign, ":troop_of_bandit", "trp_mountain_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_3"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_3"),
			#(assign, ":troop_of_bandit", "trp_steppe_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_4"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_4"),
			#(assign, ":troop_of_bandit", "trp_sea_raider"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_5"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_5"),
			#(assign, ":troop_of_bandit", "trp_mountain_bandit"),
		(else_try),
			(this_or_next|eq, ":starting_town_faction", "fac_kingdom_6"),
			(eq, ":starting_town_faction", "fac_kingdom_6"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_6"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_7"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_7"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_8"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_8"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_9"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_9"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_10"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_10"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_11"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_11"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_12"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_12"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_13"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_13"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_14"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_14"),
			#(assign, ":troop_of_bandit", "trp_desert_bandit"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_15"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_15"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_16"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_16"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_17"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_17"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_18"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_18"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_19"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_19"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_20"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_20"),
		(else_try),
			(eq, ":starting_town_faction", "fac_papacy"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_21"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_22"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_22"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_23"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_23"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_24"),
			(eq, ":starting_town_faction", "fac_kingdom_38"),
			(eq, ":starting_town_faction", "fac_kingdom_39"),
			(eq, ":starting_town_faction", "fac_kingdom_40"),
			(eq, ":starting_town_faction", "fac_kingdom_41"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_24"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_25"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_25"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_26"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_26"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_27"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_27"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_28"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_28"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_29"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_29"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_30"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_30"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_31"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_31"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_32"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_32"),
		(else_try),
			(this_or_next|eq, ":starting_town_faction", "fac_kingdom_36"),
			(this_or_next|eq, ":starting_town_faction", "fac_kingdom_34"),
			(this_or_next|eq, ":starting_town_faction", "fac_kingdom_35"),					  
			(eq, ":starting_town_faction", "fac_kingdom_33"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_2"),
		(else_try),
			(eq, ":starting_town_faction", "fac_kingdom_37"),
			(assign, ":troop_of_merchant", "trp_merchant_kingdom_37"),
											
		(try_end),
		(str_store_troop_name, s10, ":troop_of_merchant"),
		
		(set_visitors, 24, "trp_looter", 1),
		(set_visitors, 2, "trp_looter", 2),
		(set_visitors, 4, "trp_looter", 1),
		(set_visitors, 5, "trp_looter", 2),
		(set_visitors, 6, "trp_looter", 1),
		(set_visitors, 7, "trp_looter", 1),
		
		(set_visitors, 3, ":troop_of_merchant", 1),
		
		(set_jump_mission,"mt_town_fight"),
		(jump_to_scene, ":town_scene"),
		(change_screen_mission),
	]),
	
	(
		"change_player_right_to_rule",
		[
		(store_script_param_1, ":right_to_rule_dif"),
		(val_add, "$player_right_to_rule", ":right_to_rule_dif"),
		(val_clamp, "$player_right_to_rule", 0, 100),
		(try_begin),
			(gt, ":right_to_rule_dif", 0),
			(display_message, "@You gain right to rule."),
		(else_try),
			(lt, ":right_to_rule_dif", 0),
			(display_message, "@You lose right to rule."),
		(try_end),
	]),
	
	("indict_lord_for_treason",#originally included in simple_triggers. Needed to be moved here to allow player to indict
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":faction", 2),
		
		(troop_get_type, reg4, ":troop_no"),
		
		(try_for_range, ":center", centers_begin, centers_end), #transfer properties to liege
			(party_slot_eq, ":center", slot_town_lord, ":troop_no"),
			(party_set_slot, ":center", slot_town_lord, stl_unassigned),
		(try_end),
		
		(faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
		(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
		(assign, ":liege_to_lord_relation", reg0),
		(store_sub, ":base_relation_modifier", -150, ":liege_to_lord_relation"),
		(val_div, ":base_relation_modifier", 40),#-1 at -100, -2 at -70, -3 at -30,etc.
		(val_min, ":base_relation_modifier", -1),
		
		#Indictments, cont: Influence relations
		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end), #this effects all lords in all factions
			(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			(eq, ":faction", ":active_npc_faction"),
			
			(call_script, "script_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
			(assign, ":family_relation", reg0),
			
			(assign, ":relation_modifier", ":base_relation_modifier"),
			(try_begin),
			(gt, ":family_relation", 1),
			(store_div, ":family_multiplier", reg0, 3),
			(val_sub, ":relation_modifier", ":family_multiplier"),
			(try_end),
			
			(lt, ":relation_modifier", 0),
			
			(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":active_npc", ":relation_modifier"),
			(val_add, "$total_indictment_changes", ":relation_modifier"),
			(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s17, ":active_npc"),
			(str_store_troop_name, s18, ":faction_leader"),
			
			(assign, reg3, ":relation_modifier"),
			(display_message, "str_trial_influences_s17s_relation_with_s18_by_reg3"),
			(try_end),
		(try_end),
		
		#Indictments, cont: Check for other factions
		(assign, ":new_faction", "fac_outlaws"),
		(try_begin),
			(eq, ":troop_no", "trp_player"),
			(assign, ":new_faction", 0), #kicked out of faction
		(else_try),
			(call_script, "script_lord_find_alternative_faction", ":troop_no"),
			(assign, ":new_faction", reg0),
		(try_end),
		
		#Indictments, cont: Finalize where the lord goes
		(try_begin),
			(is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			
			
			(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":troop_no"),
			(display_message, "@{!}DEBUG - {s4} faction changed in indictment"),
			(try_end),
			
			
			(call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
			(try_begin), #new-begin
			(neq, ":new_faction", "fac_player_supporters_faction"),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
			(troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(try_end), #new-end
			(str_store_faction_name, s10, ":new_faction"),
			(str_store_string, s11, "str_with_the_s10"),
		(else_try),
			(neq, ":troop_no", "trp_player"),
			(call_script, "script_change_troop_faction", ":troop_no", "fac_outlaws"),
			(str_store_string, s11, "str_outside_calradia"),
		(else_try),
			(eq, ":troop_no", "trp_player"),
			(call_script, "script_player_leave_faction", 1),
		(try_end),
		
		#Indictments, cont: Set up string
		(try_begin),
			(eq, ":troop_no", "trp_player"),
			(str_store_string, s9, "str_you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life"),
		(else_try),
			(str_store_troop_name, s4, ":troop_no"),
			(str_store_faction_name, s5, ":faction"),
			(str_store_troop_name, s6, ":faction_leader"),
			
			(troop_get_type, reg4, ":troop_no"),
			(str_store_string, s9, "str_by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11"),
		(try_end),
		(display_message, "@{!}{s9}"),
		
		#Indictments, cont: Remove party
		(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
		(try_begin),
			(party_is_active, ":led_party"),
			(neq, ":led_party", "p_main_party"),
			(remove_party, ":led_party"),
			(troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
		(try_end),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(this_or_next|eq, ":faction", "$players_kingdom"),
			(eq, ":new_faction", "$players_kingdom"),
			(call_script, "script_add_notification_menu", "mnu_notification_treason_indictment", ":troop_no", ":faction"),
		(try_end),
	]),
	
	
	# script_give_center_to_faction_aux
	# Input: arg1 = center_no, arg2 = faction
	("give_center_to_faction_while_maintaining_lord",
		[
		(store_script_param_1, ":center_no"),
		(store_script_param_2, ":faction_no"),
		
		(store_faction_of_party, ":old_faction", ":center_no"),
		(party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
		(party_set_faction, ":center_no", ":faction_no"),
		
		(try_begin),
			(party_slot_eq, ":center_no", slot_party_type, spt_village),
			(party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
			(gt, ":farmer_party", 0),
			(party_is_active, ":farmer_party"),
			(party_set_faction, ":farmer_party", ":faction_no"),
		(try_end),
		
		(call_script, "script_update_faction_notes", ":faction_no"),
		(call_script, "script_update_center_notes", ":center_no"),
		
		(try_for_range, ":other_center", centers_begin, centers_end),
			(party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
			(call_script, "script_give_center_to_faction_while_maintaining_lord", ":other_center", ":faction_no"),
		(try_end),
	]),
	
	# script_check_concilio_calradi_achievement
	("check_concilio_calradi_achievement",
		[
		(try_begin),
			(eq, "$players_kingdom", "fac_player_supporters_faction"),
			(faction_get_slot, ":player_faction_king", "fac_player_supporters_faction", slot_faction_leader),
			(eq, ":player_faction_king", "trp_player"),
			(assign, ":number_of_vassals", 0),
			(try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":cur_faction", ":cur_troop"),
			(eq, ":cur_faction", "fac_player_supporters_faction"),
			(val_add, ":number_of_vassals", 1),
			(try_end),
			(ge, ":number_of_vassals", 3),
			(unlock_achievement, ACHIEVEMENT_CONCILIO_CALRADI),
		(try_end),
	]),
	
	
	#  ("cf_check_quest_active_for_troop",
	#    [
	#      (store_script_param_1, ":quest_no"),
	#      (store_script_param_2, ":troop_no"),
	
	#	  (check_quest_active, ":quest_no"),
	#	  (quest_slot_eq, ":quest_no", slot_quest_giver_troop, ":troop_no"),
	
	# ]),
	
	# matching sets
	
	# script_set_matching_items
	# Input: arg1 = agent_no, arg2 = troop_no
	# Output: none
	("set_matching_items",
		[
		(store_script_param, ":body_item", 1),
		(store_script_param, ":agent_no", 2),
		(store_script_param, ":troop_no", 3),
		
		#(assign ,reg0, ":body_item"),
		#(assign, reg1, ":troop_no"),
		#(assign, reg2, ":agent_no"),
		
		# (str_store_troop_name, s1, ":troop_no"),
		# (str_store_item_name, s2, ":body_item"),
		#(display_message, "@this is: {s1} item: {s2} - {reg0}, troop: {reg1}, agent: {reg2}", 0xffff0000),
		
		#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
		
		(assign, ":continue", 0),
		
		(try_begin),
			(eq, ":troop_no", "trp_euro_horse_4"),
			(assign, ":continue", 2),
		(else_try),
			(eq, ":troop_no", "trp_nordic_knight"),
			(assign, ":continue", 2),
		(else_try),
			(eq, ":troop_no", "trp_gaelic_knight"),
			(assign, ":continue", 1),
		(else_try),
			(eq, ":troop_no", "trp_welsh_horse_4"),
			(assign, ":continue", 1),  
		(else_try),
			(eq, ":troop_no", "trp_iberian_knight"),
			(assign, ":continue", 2),
		(else_try),
			(eq, ":troop_no", "trp_andalus_horse_4"),
			(assign, ":continue", 1),
		(else_try),
			(eq, ":troop_no", "trp_rus_horse_4"),
			(assign, ":continue", 1),
		(try_end),
		
		(try_begin),
			(neq, ":agent_no", -1),		  
			(eq, ":continue", 1),
			(store_random_in_range, ":random", 0, 100),
			(try_begin),
			(gt, ":random", 65),
			(try_begin),
				(eq, ":troop_no", "trp_rus_horse_4"),
				(store_random_in_range, ":horse", "itm_mon_lamellar_horse_a", "itm_kau_montcada_horse"),
			(else_try),
				(store_random_in_range, ":horse", "itm_warhorse_white", "itm_warhorse_player"),
			(try_end),
			(else_try),
			(store_random_in_range, ":horse", 0, 3),
			(try_begin),
				(eq, ":horse", 0),
				(assign, ":horse", "itm_hunter"),
			(else_try),
				(eq, ":horse", 1),
				(assign, ":horse", "itm_horse_e"),
			(else_try),
				(assign, ":horse", "itm_horse_d"),
			(try_end),
			(try_end),
			(troop_set_inventory_slot, ":troop_no", ek_horse, ":horse"),
		(try_end),
		
		
		(try_begin),
			(eq, ":continue", 2),
			(neq, ":agent_no", -1),
			(try_begin),
			(eq, ":body_item", itm_rnd_surcoat_01),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_01),
			#(troop_set_inventory_slot, ":troop_no", ek_head, itm_rnd_helm_01),
			#(display_message, "@this is: .... {s1} .... item: {s2} - {reg0}, helm_01", 0xff00ff00),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_02),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_02),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_03),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_03),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_04),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_04),
			#(troop_set_inventory_slot, ":troop_no", ek_head, itm_rnd_helm_02),
			#(display_message, "@this is: .... {s1} .... item: {s2} - {reg0}, helm_02", 0xff00ff00),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_05),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_05),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_06),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_06),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_07),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_07),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_08),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_08),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_09),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_09),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_10),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_10),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_11),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_11),
			#(troop_set_inventory_slot, ":troop_no", ek_head, itm_rnd_helm_02),
			#(display_message, "@this is: .... {s1} .... item: {s2} - {reg0}, helm_02", 0xff00ff00),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_12),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_12),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_13),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_13),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_14),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_14),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_15),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_15),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_16),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_16),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_17),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_17),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_18),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_18),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_19),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_19),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_20),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_20),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_21),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_21),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_22),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_22),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			(else_try),
			(eq, ":body_item", itm_rnd_surcoat_23),
			(troop_set_inventory_slot, ":troop_no", ek_horse, itm_rnd_horse_23),
			#(troop_set_inventory_slot, ":troop_no", ek_head, -1),
			# (else_try),
			# (store_random_in_range, ":horse_item", itm_rnd_horse_01, itm_rnd_horse_23 + 1),
			# (troop_set_inventory_slot, ":troop_no", ek_horse, ":horse_item"),
			(try_end),
		(try_end),
		]
	),
	
	# script_distance_between_factions
	("distance_between_factions",
		[
		(store_script_param_1, ":attacker_party"),
		(store_script_param_2, ":defender_party"),
		(assign, ":distance", -1),
		
		(try_for_range, ":attacker_centers", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":cur_faction", ":attacker_centers"),
			(eq, ":cur_faction", ":attacker_party"),
			(try_for_range, ":defender_centers", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":cur_faction", ":defender_centers"),
			(eq, ":cur_faction", ":defender_party"),
			
			(store_distance_to_party_from_party,":war_distance",":attacker_centers",":defender_centers"),
			(try_begin),
				(lt, ":distance", 0),
				(assign, ":distance", ":war_distance"),
			(else_try),
				(lt, ":war_distance", ":distance"),
				(assign, ":distance", ":war_distance"),
			(try_end),
			
			(try_end),
		(try_end),
		
		# (try_begin),
		# (le, ":distance", 0),
		# (assign, ":distance", 9999),
		# (try_end),
		#(str_store_faction_name_link, s1, ":attacker_party"),
		#(str_store_faction_name_link, s2, ":defender_party"),
		#(display_message, "@--DEBUG-- war between {s1} and {s2}, distance is: {reg0}"),
		
		(assign, reg0, ":distance"),
	]),
	

	# script_is_party_on_water
	("cf_is_party_on_water",
		[
		(store_script_param_1, ":party_id"),
		(party_get_current_terrain, ":party_terrain", ":party_id"),
		
		(assign, reg0, 0),
		
		(try_begin),
			(this_or_next|eq, ":party_terrain", rt_water),
			(this_or_next|eq, ":party_terrain", rt_river),
			(this_or_next|eq, ":party_terrain", rt_bridge),
			(eq, ":party_terrain", 15),
			(assign, reg0, 1),
		(try_end),
		
		(gt, reg0, 0),
	]),
	
	("raf_replace_troop",
		[
		(store_script_param, ":party_id", 1),
		(store_script_param, ":old_troop", 2),
		(store_script_param, ":new_troop", 3),
		
		(party_get_num_companion_stacks, ":num_stacks",":party_id"),
		(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
			(party_stack_get_troop_id,     ":stack_troop",":party_id",":stack_no"),
			(try_begin),
			(eq, ":stack_troop", ":old_troop"),
			(party_stack_get_size,    ":stack_size",":party_id",":stack_no"),
			(party_remove_members, ":party_id", ":stack_troop", ":stack_size"),
			(party_add_members, ":party_id", ":new_troop", ":stack_size"),
			(try_begin),
				(eq, ":party_id", "p_main_party"),
				(str_store_troop_name, s1, ":stack_troop"),
				(str_store_troop_name, s2, ":new_troop"),
				(assign, reg0, ":stack_size"),
				#(display_message, "@replacing {s1} with {s2}, qty: {reg0}", 0xff0000),
			(try_end),
			(try_end),
		(try_end),
	]),
	
	# deathcam #############################
	# script_dmod_cycle_forwards
	# Output: New $dmod_current_agent
	# Used to cycle forwards through valid agents
	("dmod_cycle_forwards",
		[
		
		(assign, ":agent_moved", 0),
		(assign, ":first_agent", -1),
		(get_player_agent_no, ":player_agent"),
		#(agent_get_team, ":player_team", ":player_agent"),
		
		(try_for_agents, ":agent_no"),
			(ge, ":agent_no", 0),
			(neq, ":agent_moved", 1),
			(neq, ":agent_no", ":player_agent"),
			(agent_is_human, ":agent_no"),
			(agent_is_alive, ":agent_no"),
			#(agent_get_team, ":cur_team", ":agent_no"),
			#(eq, ":cur_team", ":player_team"), #tom
			#                (agent_get_troop_id, ":agent_troop", ":agent_no"),
			(try_begin),
			(lt, ":first_agent", 0),
			(assign, ":first_agent", ":agent_no"),
			(try_end),
			(gt, ":agent_no", "$dmod_current_agent"),
			(assign, "$dmod_current_agent", ":agent_no"),
			(assign, ":agent_moved", 1),
		(try_end),
		
		(try_begin),
			(eq, ":agent_moved", 0),
			(neq, ":first_agent", -1),
			(assign, "$dmod_current_agent", ":first_agent"),
			(assign, ":agent_moved", 1),
		(else_try),
			(eq, ":agent_moved", 0),
			(eq, ":first_agent", -1),
			(display_message, "@No Troops Left."),
		(try_end),
		
		(try_begin),
			(eq, ":agent_moved", 1),
			(str_store_agent_name, 1, "$dmod_current_agent"),
			(display_message, "@Selected Troop: {s1}"),
		(try_end),
		(assign, "$dmod_move_camera", 1),
	]),
	
	# script_dmod_cycle_backwards
	# Output: New $dmod_current_agent
	# Used to cycle backwards through valid agents
	("dmod_cycle_backwards",[
		
		(assign, ":new_agent", -1),
		(assign, ":last_agent", -1),
		(get_player_agent_no, ":player_agent"),
		#(agent_get_team, ":player_team", ":player_agent"),
		
		(try_for_agents, ":agent_no"),
			(gt, ":agent_no", -1),
			(neq, ":agent_no", ":player_agent"),
			(agent_is_human, ":agent_no"),
			(agent_is_alive, ":agent_no"),
			#(agent_get_team, ":cur_team", ":agent_no"),
			#(eq, ":cur_team", ":player_team"), #tom
			#               (agent_get_troop_id, ":agent_troop", ":agent_no"),
			(assign, ":last_agent", ":agent_no"),
			(lt, ":agent_no", "$dmod_current_agent"),
			(assign, ":new_agent", ":agent_no"),
		(try_end),
		
		(try_begin),
			(eq, ":new_agent", -1),
			(neq, ":last_agent", -1),
			(assign, ":new_agent", ":last_agent"),
		(else_try),
			(eq, ":new_agent", -1),
			(eq, ":last_agent", -1),
			(display_message, "@No Troops Left."),
		(try_end),
		
		(try_begin),
			(neq, ":new_agent", -1),
			(assign, "$dmod_current_agent", ":new_agent"),
			(str_store_agent_name, 1, "$dmod_current_agent"),
			(display_message, "@Selected Troop: {s1}"),
		(try_end),
		(assign, "$dmod_move_camera", 1),
	]),
	
	# script_set_real_items_for_tournament
	# Input: arg1 = armor_item_begin, arg2 = helm_item_begin
	# Output: none (sets mt_arena_melee_fight items)
	# ("set_real_items_for_tournament",
	# [
	# (store_script_param_1, ":armor_item_begin"),
	#(store_script_param_2, ":helm_item_begin"),
	# (try_for_range, ":i_ep", 0, 32),
	# (mission_tpl_entry_clear_override_items, "mt_arena_tournament_fight", ":i_ep"),
	# (store_div, ":cur_team", ":i_ep", 8),
	#(store_add, ":cur_shield_item", "itm_arena_shield_red", ":cur_team"),
	# (try_begin),
	# (ge, ":armor_item_begin", 0),
	# (store_add, ":cur_armor_item", ":armor_item_begin", ":cur_team"),
	# (mission_tpl_entry_add_override_item, "mt_arena_tournament_fight", ":i_ep", ":cur_armor_item"),
	# (try_end),
	#(try_begin),
	#(store_add, ":cur_horse_item", "itm_warhorse_red", ":cur_team"),
	#(mission_tpl_entry_add_override_item, "mt_arena_tournament_fight", ":i_ep", ":cur_horse_item"),
	#(try_end),
	# (try_begin),
	# (ge, ":helm_item_begin", 0),
	# (store_add, ":cur_helm_item", ":helm_item_begin", ":cur_team"),
	# (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_helm_item"),
	# (try_end),
	# (try_end),
	# ]),
	
	#script_cf_village_recruit_volunteers_cond
	# INPUT: none
	# OUTPUT: none
	("cf_town_recruit_volunteers_cond",
		[(party_slot_eq, "$current_town", slot_center_is_besieged_by, -1),
		(try_begin),
			(party_slot_eq, "$current_town", slot_party_type, spt_castle),
			(party_get_slot, ":castle_lord", "$current_town", slot_town_lord),
			(try_begin),
			(gt, ":castle_lord", 0),
			(call_script, "script_troop_get_player_relation", ":castle_lord"),
			(assign, ":center_relation", reg0),
			(store_faction_of_party, ":village_faction", "$current_town"),
			(store_relation, ":village_faction_relation", ":village_faction", "fac_player_faction"),
			(else_try),
			(assign, ":center_relation", 0),
			(try_end),
		(else_try),
			(store_faction_of_party, ":village_faction", "$current_town"),
			(party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
			(store_relation, ":village_faction_relation", ":village_faction", "fac_player_faction"),
			#(display_message, "@---DEBUG--- entered town"),
		(try_end),
		(assign, reg0, ":center_relation"),
		#(display_message, "@---DEBUG--- relation: {reg0}"),
		
		(ge, ":center_relation", 0),
		(this_or_next|ge, ":center_relation", 5),
		(this_or_next|eq, ":village_faction", "$players_kingdom"),
		(this_or_next|ge, ":village_faction_relation", 0),
		(this_or_next|eq, ":village_faction", "$supported_pretender_old_faction"),
		(             eq, "$players_kingdom", 0),
		#(display_message, "@---DEBUG--- here"),
		(party_slot_ge, "$current_town", slot_center_volunteer_troop_amount, 0),
		(party_slot_ge, "$current_town", slot_center_volunteer_troop_type, 1),
		(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
		(ge, ":free_capacity", 1),
	]),

	#script_tom_aor_faction_to_region
	##description: for lance recruitment system, select region. whitout player kingdom interferance
	("tom_aor_faction_to_region",
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
		]
	),
	
	("raf_aor_faction_to_region",
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
		]
	),
	
	("raf_aor_region_to_faction",
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
		]
	),
	("raf_create_incidents",
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
		]
	),
	
	#script_spawn_manors - tom made
	# INPUT: none
	# OUTPUT: none
	# DESCRIPTION: Spawns random manor type to villages, castles and towns
	("spawn_manors",
	[  
		(try_for_range, ":center", centers_begin, centers_end),
			(neg|is_between, ":center", castles_begin, castles_end),
			(store_faction_of_party, ":center_faction", ":center"),
		(is_between, ":center_faction", kingdoms_begin, kingdoms_end),
		(store_random_in_range, ":random", 0, 100),
		(lt, ":random", 50),
		(call_script, "script_spawn_manor_party", "pt_manor", ":center"),
		(try_end),
		
		(call_script, "script_update_manor_array"),
	]),
	
	#script_spawn_manor_party - tom made
	#input: party to spawn, center to bind to and spawn around it, bound and rename party(if 0 - not, only for manors).
	#output: reg0 - party id.
	("spawn_manor_party",
	[
		(store_script_param, ":random", 1),
		(store_script_param, ":center", 2),
		
		(set_spawn_radius, 7),
		(store_faction_of_party, ":center_faction", ":center"),
		(spawn_around_party, ":center", ":random"),
		(assign, ":party_id", reg0),
		(try_begin), #this can fail?
			(party_get_position, pos0, ":center"),
			(map_get_land_position_around_position, pos1, pos0, 5),
		(try_end),
		
		(party_get_position, pos0, ":center"),
		(assign, ":upper_bound", 3000),
		(try_for_range, reg1, 0, ":upper_bound"),
			(map_get_land_position_around_position, pos1, pos0, 7),
			(assign, ":bad", 0),
			(try_for_parties, ":parties"),
				(this_or_next|is_between, ":parties", centers_begin, centers_end),
			(eq, ":parties", "pt_manor"),
				(party_get_position, pos2, ":parties"),
			(get_distance_between_positions_in_meters, ":distance", pos2, pos1),
			(try_begin),
				(lt, ":distance", 1),
				(assign, ":bad", 1),
			(try_end),  
			(try_end),
			(try_begin),
				(eq, ":bad", 0),
				(party_set_position,":party_id",pos1),
			(party_get_current_terrain, ":terrain", ":party_id"),
			(try_begin), #bridge/shore - means boo boo
				(eq, ":terrain", rt_bridge),
			(else_try),
				(assign, ":upper_bound", -8),
			(try_end),
			(try_end),	
		(try_end),
		
		##spawn some random buildings in it
		(store_random_in_range, ":random", 1, 5),
		(try_for_range, reg0, 0, ":random"),
			(store_random_in_range, ":random_building", manor_slot_marketplace, manor_slot_walls),
			(party_set_slot, ":party_id", ":random_building", manor_building_operational),
		(try_end),
		
		##add some random stats
		(try_begin),
			(store_random_in_range, ":population", 10, 50),
			(store_random_in_range, ":prosperity", 1, 10),
			(party_set_slot, ":party_id", manor_slot_population, ":population"),
			(party_set_slot, ":party_id", slot_town_prosperity, ":prosperity"),
		(try_end),
		
		#(party_set_position,":party_id",pos1),
		(party_set_faction,":party_id", ":center_faction"),
		(party_set_slot, ":party_id", slot_village_bound_center, ":center"),
		(str_store_party_name, s0, ":center"),
		(str_store_party_name, s1, ":party_id"),
		(str_store_string, s2, "@{s1} of {s0}"),
		(party_set_name, ":party_id", s2),
		(assign, reg0, ":party_id"),
	]
	),
	
	#script_update_manor_array
	#input: none
	#output: none
	#updates the trp_manor_array troop, which is the storage troop for manor id
	("update_manor_array",
	[
			 (assign, ":slot_nr", 1),
		 (try_for_parties, ":party_id"),
			 (party_get_template_id,":party_template",":party_id"),
		 (eq, ":party_template", "pt_manor"),
		 (troop_set_slot,"trp_manor_array",":slot_nr",":party_id"),
		 (val_add, ":slot_nr", 1),		
		 
		 (party_get_slot, ":center", ":party_id", slot_village_bound_center), #get the village of the manor
		 (party_set_slot,":center",village_slot_manor,":party_id"), #save the manor to the village
		 #assign scenes
		 (call_script, "script_manor_set_unique_scene", ":party_id", ":center"),
		 (try_end), #cycle
		 (troop_set_slot,"trp_manor_array",0,":slot_nr"), #zero hold the total amount of parties
	]
	),
	
	
	#script_prepare_manor_troops
	#input:none
	#output:none
	#description: this will set the goods of the manor craftsman
	("prepare_manor_troops",
	[
		(troop_set_slot,"trp_manor_grain", manor_troop_slot_good, itm_grain),
		(troop_set_slot,"trp_manor_livestock", manor_troop_slot_good, itm_wool),
		(troop_set_slot,"trp_manor_fruit", manor_troop_slot_good, itm_apples),
		(troop_set_slot,"trp_manor_fisher", manor_troop_slot_good, itm_smoked_fish),
		(troop_set_slot,"trp_manor_baker", manor_troop_slot_good, itm_bread),
		(troop_set_slot,"trp_manor_winer", manor_troop_slot_good, itm_wine),
		(troop_set_slot,"trp_manor_brewer", manor_troop_slot_good, itm_ale),
		(troop_set_slot,"trp_manor_potter", manor_troop_slot_good, itm_pottery),
		(troop_set_slot,"trp_manor_blacksmith", manor_troop_slot_good, itm_tools),
		(troop_set_slot,"trp_manor_butcher", manor_troop_slot_good, itm_dried_meat),
		(troop_set_slot,"trp_manor_oilmaker", manor_troop_slot_good, itm_oil),
		(troop_set_slot,"trp_manor_linen", manor_troop_slot_good, itm_linen),
		(troop_set_slot,"trp_manor_wool", manor_troop_slot_good, itm_wool_cloth),
		(troop_set_slot,"trp_manor_tanner", manor_troop_slot_good, itm_leatherwork),	
		 
		(troop_set_slot,"trp_manor_trader_silk", manor_troop_slot_good, itm_raw_silk),
		(troop_set_slot,"trp_manor_trader_spice", manor_troop_slot_good, itm_spice),
		(troop_set_slot,"trp_manor_trader_dyes", manor_troop_slot_good, itm_raw_dyes),
		(troop_set_slot,"trp_manor_trader_salt", manor_troop_slot_good, itm_salt),
		 
		(troop_set_slot,"trp_manor_grain", manor_troop_slot_tax, manor_slot_tax_grainfarm),
		(troop_set_slot,"trp_manor_livestock", manor_troop_slot_tax, manor_slot_tax_livestock),
		(troop_set_slot,"trp_manor_fruit", manor_troop_slot_tax, manor_slot_tax_fruitfarm),
		(troop_set_slot,"trp_manor_fisher", manor_troop_slot_tax, manor_slot_tax_fisher),
		(troop_set_slot,"trp_manor_baker", manor_troop_slot_tax, manor_slot_tax_bakery),
		(troop_set_slot,"trp_manor_winer", manor_troop_slot_tax, manor_slot_tax_winery),
		(troop_set_slot,"trp_manor_brewer", manor_troop_slot_tax, manor_slot_tax_brewery),
		(troop_set_slot,"trp_manor_potter", manor_troop_slot_tax, manor_slot_tax_potter),
		(troop_set_slot,"trp_manor_blacksmith", manor_troop_slot_tax, manor_slot_tax_blacksmith),
		(troop_set_slot,"trp_manor_butcher", manor_troop_slot_tax, manor_slot_tax_butcher),
		(troop_set_slot,"trp_manor_oilmaker", manor_troop_slot_tax, manor_slot_tax_oilmaker),
		(troop_set_slot,"trp_manor_linen", manor_troop_slot_tax, manor_slot_tax_linenworkshop),
		(troop_set_slot,"trp_manor_wool", manor_troop_slot_tax, manor_slot_tax_woolworkshop),
		(troop_set_slot,"trp_manor_tanner", manor_troop_slot_tax, manor_slot_tax_tannery),	
	]),
	
	#script_manor_set_unique_scene
	#input:manor_party_id, center
	#output: none
	#description: sets the manor scene based on it's terrain type
	("manor_set_unique_scene",
		[
		(store_script_param, ":manor_party_id", 1),
		(store_script_param, ":center", 2),
		(party_get_slot, ":culture", ":center", slot_center_culture),
		
		(party_get_current_terrain, ":terrain", ":manor_party_id"),
		(try_begin),
			(this_or_next|eq, ":culture", "fac_culture_finnish"),
			(this_or_next|eq, ":culture", "fac_culture_mazovian"),
			(this_or_next|eq, ":culture", "fac_culture_teutonic"),
			(eq, ":culture", "fac_culture_baltic"),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_teutonic"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_snow),
			(eq, ":terrain", rt_snow_forest),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_snow"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_desert),
			(eq, ":terrain", rt_desert_forest),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_desert"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_steppe),
			(eq, ":terrain", rt_steppe_forest),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_steppe"),
		(else_try),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_plains"),
		(try_end),
		]),
	
	
	#script_spawn_mongols
	# INPUT: none
	# OUTPUT: none
	# DESCRIPTION: This script will spawn a camp at each of the monglian faction towns.
	("spawn_mongols",
		[
			(try_for_range, ":town", centers_begin, centers_end),
			# (store_faction_of_party, ":faction", ":town"),
			# (this_or_next|eq, ":town", "fac_kingdom_3"),
			# (eq, ":town", "fac_kingdom_27"),
			(this_or_next|is_between, ":town", "p_town_3_1", "p_town_4_1"),
			(is_between, ":town", "p_town_27_1", "p_town_28_1"),
			(try_begin),
				(is_between, ":town", "p_town_27_1", "p_town_28_1"),
			(assign, ":faction", "fac_kingdom_27"),
			(else_try),
			(assign, ":faction", "fac_kingdom_3"),
			(try_end),
			#(assign, ":town", "p_town_3_1"),
			#(party_get_slot,":camp",":town",slot_mongol_camp),
			#(le, ":camp", 0),
			
			#(store_random_in_range, ":random", 1, 101),
			#(ge, ":random", 50),
			(set_spawn_radius, 5),
			(spawn_around_party,":town","pt_mongolian_camp"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_location),
			(party_set_ai_object, ":party_id", ":town"),
			(party_set_slot, ":party_id", slot_party_ai_object, ":town"),
			(party_set_ai_patrol_radius, ":party_id", 15),
			
			(party_set_slot, ":party_id",slot_mongol_town,":town"),
			(party_set_slot, ":town",slot_mongol_camp,":party_id"),
			(party_set_faction, ":party_id",":faction"),
			(party_set_slot, ":party_id",slot_castle_exterior,"scn_village_mongol"),
			(party_set_slot, ":party_id", slot_feudal_lances, 1),#one lance!
			(party_set_slot, ":party_id", slot_center_culture, "fac_culture_mongol"),
			(party_set_slot, ":party_id",slot_mongol_camp_status, status_stationed),
			(party_set_icon, ":party_id", "icon_camp"),
		(try_end),
		]
	),	  
	

	#script_cf_spawn_crusaders_and_jihadists
	# INPUT: none
	# OUTPUT: none
	("cf_spawn_crusaders_and_jihadists",
		[
		
			(faction_slot_eq, "fac_kingdom_23", slot_faction_state, sfs_active),
		(faction_slot_eq, "fac_kingdom_25", slot_faction_state, sfs_active),
		#jihad
			(assign, ":parties_to_spawn", 2),
		(try_begin),
			(store_num_parties_of_template, ":num_parties", "pt_jihadist_raiders"),
			(lt,":num_parties",":parties_to_spawn"),
				#(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_25"),
				#(assign, ":town_no", reg0),
			#(gt, ":town_no", 0),
				(assign, ":town_no", "p_town_25_5"), #jerusalem
			
			(set_spawn_radius, 5),
			(spawn_around_party,":town_no","pt_jihadist_raiders"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_location),
			(party_set_ai_object, ":party_id", ":town_no"),
			(party_set_slot, ":party_id", slot_party_ai_object, ":town_no"),
			(party_set_ai_patrol_radius, ":party_id", 15),
		 # (party_set_banner_icon, ":party_id", "icon_banner_20"),
		(try_end),
		
		#crusaders
		(assign, ":parties_to_spawn", 4),
		(try_begin),
			(store_num_parties_of_template, ":num_parties", "pt_crusader_raiders"),
			(lt,":num_parties",":parties_to_spawn"),
				#(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_23"),
				#(assign, ":town_no", reg0),
			#(gt, ":town_no", 0),
				(assign, ":town_no", "p_town_23_1"), #acre
			
			(set_spawn_radius, 5),
			(spawn_around_party,":town_no","pt_crusader_raiders"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_location),
			(party_set_ai_object, ":party_id", ":town_no"),
			(party_set_slot, ":party_id", slot_party_ai_object, ":town_no"),
			(party_set_ai_patrol_radius, ":party_id", 15),
			# (party_set_banner_icon, ":party_id", "icon_banner_20"),
		(try_end),
		]
	),
	
	#script_spawn_balts
	# INPUT: none
	# OUTPUT: none
	("spawn_balts",
		[
		#(set_spawn_radius,1),
		
		(assign, ":parties_to_spawn", 3),
		
		(try_begin),
			(store_num_parties_of_template, ":num_parties", "pt_guelphs"),
			(lt,":num_parties",":parties_to_spawn"),
			(faction_slot_eq, "fac_kingdom_40", slot_faction_state, sfs_active),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_town_40_2","pt_guelphs"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_location),
			(party_set_ai_object, ":party_id", "p_town_40_2"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_town_40_2"),
			(party_set_ai_patrol_radius, ":party_id", 10),
			(party_set_banner_icon, ":party_id", "icon_banner_20"),
		(try_end),
		
		(assign, ":parties_to_spawn", 3),
		(try_begin),
			(store_num_parties_of_template, ":num_parties", "pt_ghibellines"),
			(lt,":num_parties",":parties_to_spawn"),
			(faction_slot_eq, "fac_kingdom_41", slot_faction_state, sfs_active),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_town_41_2","pt_ghibellines"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_location),
			(party_set_ai_object, ":party_id", "p_town_41_2"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_town_41_2"),
			(party_set_ai_patrol_radius, ":party_id", 10),
			(party_set_banner_icon, ":party_id", "icon_banner_19"),
		(try_end),
		#tom
		
		(assign, ":parties_to_spawn", 5),
		(try_begin),
			(faction_slot_eq, "fac_kingdom_35", slot_faction_state, sfs_active), #tom
			(store_num_parties_of_template, ":num_parties", "pt_curonians"),
			(lt,":num_parties",":parties_to_spawn"),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_castle_35_1","pt_curonians"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_location),
			(party_set_ai_object, ":party_id", "p_castle_35_1"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_castle_35_1"),
			(party_set_ai_patrol_radius, ":party_id", 15),
		(try_end),
		
		(try_begin),
			(faction_slot_eq, "fac_kingdom_34", slot_faction_state, sfs_active), #tom
			(store_num_parties_of_template, ":num_parties", "pt_prussians"),
			(lt,":num_parties",":parties_to_spawn"),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_castle_34_1","pt_prussians"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
			(party_set_ai_object, ":party_id", "p_castle_34_1"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_castle_34_1"),
			(party_set_ai_patrol_radius, ":party_id", 15),
		(try_end),
		
		(try_begin),
			(faction_slot_eq, "fac_kingdom_36", slot_faction_state, sfs_active), #tom
			(store_num_parties_of_template, ":num_parties", "pt_samogitians"),
			(lt,":num_parties",":parties_to_spawn"),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_castle_36_1","pt_samogitians"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
			(party_set_ai_object, ":party_id", "p_castle_36_1"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_castle_36_1"),
			(party_set_ai_patrol_radius, ":party_id", 15),
		(try_end),
		
		(try_begin),
			(faction_slot_eq, "fac_kingdom_33", slot_faction_state, sfs_active), #tom
			(store_num_parties_of_template, ":num_parties", "pt_yotvingians"),
			(lt,":num_parties",":parties_to_spawn"),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_castle_33_1","pt_yotvingians"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
			(party_set_ai_object, ":party_id", "p_castle_33_1"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_castle_33_1"),
			(party_set_ai_patrol_radius, ":party_id", 15),
		(try_end),
		
		(assign, ":parties_to_spawn", 3),
		(try_begin),
			(faction_slot_eq, "fac_kingdom_37", slot_faction_state, sfs_active), #tom
			(store_num_parties_of_template, ":num_parties", "pt_welsh"),
			(lt,":num_parties",":parties_to_spawn"),
			(set_spawn_radius, 5),
			(spawn_around_party,"p_town_37_1","pt_welsh"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
			(party_set_ai_object, ":party_id", "p_town_37_1"),
			(party_set_slot, ":party_id", slot_party_ai_object, "p_town_37_1"),
			(party_set_ai_patrol_radius, ":party_id", 15),
		(try_end),
		
		(assign, ":parties_to_spawn", 2),
		(try_begin),
			(faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active), #tom
			(store_num_parties_of_template, ":num_parties", "pt_teutonic_raiders"),
			(lt,":num_parties",":parties_to_spawn"),
			(set_spawn_radius, 5),
				(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_1"),
				(assign, ":town_no", reg0),
			(gt, ":town_no", 0),
			(spawn_around_party,":town_no","pt_teutonic_raiders"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
			(party_set_ai_object, ":party_id", ":town_no"),
			(party_set_slot, ":party_id", slot_party_ai_object, ":town_no"),
			(party_set_ai_patrol_radius, ":party_id", 15),  
		(try_end),
		
		##making bandits out of destroyed faction troops
		(try_for_parties, ":party"),
			(party_get_template_id, ":template", ":party"),
			(try_begin),
				(eq, ":template", "pt_guelphs"),
			(neg|faction_slot_eq, "fac_kingdom_40", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_ghibellines"),
			(neg|faction_slot_eq, "fac_kingdom_41", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_curonians"),
			(neg|faction_slot_eq, "fac_kingdom_35", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_prussians"),
			(neg|faction_slot_eq, "fac_kingdom_34", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_samogitians"),
			(neg|faction_slot_eq, "fac_kingdom_36", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_yotvingians"),
			(neg|faction_slot_eq, "fac_kingdom_33", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_welsh"),
			(neg|faction_slot_eq, "fac_kingdom_37", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(else_try),
				(eq, ":template", "pt_teutonic_raiders"),
			(neg|faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active),
			(party_set_faction, ":party", "fac_deserters"),
			(try_end),
		(try_end),
		
	]),
	
	#script_spawn_peasant_rebels
	# INPUT: none
	# OUTPUT: none
	("spawn_peasant_rebels",
		[
			#TOM NEW
		(store_current_day, ":cur_day"),
		#(try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		(store_num_parties_of_template, ":num_parties", "pt_peasant_rebels_euro"), #limit how many rebels can be about
		(store_random_in_range, ":faction", kingdoms_begin, kingdoms_end),
		(try_begin),
			(faction_get_slot, ":last_rebellion", ":faction", slot_faction_peasant_rebellion_last),
			(store_sub, ":ok_to_rebel", ":cur_day", ":last_rebellion"),
			(ge, ":ok_to_rebel", 30),
			(le, ":num_parties", 9), # 6 rebelions!
			
			(assign, ":fac_towns", 0),
			(assign, ":fac_prosperity", 0),
			(assign, ":fac_average_prosperity", 0),
			(assign, ":lowest_prosperity", 100),
			(assign, ":lowest_prosperity_town", -1),
			(try_for_range, ":cur_town", towns_begin, towns_end),
			(store_faction_of_party, ":cur_fac", ":cur_town"),
			(eq, ":cur_fac", ":faction"),
			(val_add, ":fac_towns", 1),
			(party_get_slot, ":prosperity", ":cur_town", slot_town_prosperity),
			(val_add, ":fac_prosperity", ":prosperity"),
			(lt, ":prosperity", ":lowest_prosperity"),
			(assign, ":lowest_prosperity", ":prosperity"),
			(assign, ":lowest_prosperity_town", ":cur_town"),
			(try_end),
			(gt, ":fac_towns", 0),
			(gt, ":lowest_prosperity_town", 0),
			
			(store_div, ":fac_average_prosperity", ":fac_prosperity", ":fac_towns"),
			(le, ":fac_average_prosperity", 25),
			
			
			(set_spawn_radius,3),
			(assign, ":parties_to_spawn", 3),
			(faction_get_slot, ":village", ":faction", slot_faction_tier_1_troop),
			(faction_get_slot, ":town", ":faction", slot_faction_tier_1_town_troop),
			(faction_get_slot, ":castle", ":faction", slot_faction_tier_1_castle_troop),
			(try_for_range, reg1, 0, ":parties_to_spawn"),
				(spawn_around_party,":lowest_prosperity_town", "pt_peasant_rebels_euro"),
			(assign, ":party_id", reg0),
			(party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
			(party_set_ai_object, ":party_id", ":lowest_prosperity_town"),
			(party_set_ai_patrol_radius, ":party_id", 10),
			(str_store_faction_name, s25, ":faction"),
			(party_set_slot, ":party_id", slot_party_ai_object, ":lowest_prosperity_town"),
			(party_add_members, ":party_id", ":castle", 40),
			(party_add_members, ":party_id", ":town", 120),
			(party_add_members, ":party_id", ":village", 240),
			#(party_upgrade_with_xp, ":party_id", 5000, 0),
			(try_end),
			(try_begin),
			(display_message, "@Peasants revolt in areas controlled by the {s25}!", 0xff0000),
			(faction_set_slot, ":faction", slot_faction_peasant_rebellion_last, ":cur_day"),
			(try_end),
		(try_end),		
		#TOM
		##(store_random_in_range, ":faction", fac_kingdom_1, fac_kingdom_28 + 1),
		# (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
			# (assign, ":fac_towns", 0),
			# (assign, ":fac_prosperity", 0),
			
			# (try_for_range, ":cur_town", towns_begin, towns_end),
			# (store_faction_of_party, ":cur_fac", ":cur_town"),
			# (eq, ":cur_fac", ":faction"),
			# (val_add, ":fac_towns", 1),
			# (party_get_slot, ":prosperity", ":cur_town", slot_town_prosperity),
			# (val_add, ":fac_prosperity", ":prosperity"),
			# (try_end),
			
			# (assign, ":fac_average_prosperity", 0),
			# (try_begin),
			# (gt, ":fac_towns", 0),
			# (store_div, ":fac_average_prosperity", ":fac_prosperity", ":fac_towns"),
			# (try_end),
			
			# (set_spawn_radius,1),
			
			# (gt, ":fac_towns", 0),
			
			# (assign, ":parties_to_spawn", 5),
			# (call_script, "script_raf_aor_faction_to_region", ":faction"),
			# (assign, ":region", reg0),
			
			# (try_begin),
			# (eq, ":region", region_nordic),
			# (assign, ":template", "pt_peasant_rebels_nordic"),
			# (else_try),
			# (this_or_next | eq, ":region", region_teutonic),
			# (eq, ":region", region_baltic),
			# (assign, ":template", "pt_peasant_rebels_baltic"),
			# (else_try),
			# (this_or_next | eq, ":region", region_balkan),
			# (this_or_next | eq, ":region", region_byzantine),
			# (eq, ":region", region_eastern),
			# (assign, ":template", "pt_peasant_rebels_eastern"),
			# (else_try),
			# (eq, ":region", region_european),
			# (assign, ":template", "pt_peasant_rebels_euro"),
			# (else_try),  #TOM
			# (eq, ":region", region_scot),
			# (assign, ":template", "pt_peasant_rebels_scot"),
			# (else_try),
			# (eq, ":region", region_latin),
			# (assign, ":template", "pt_peasant_rebels_euro"),
			# (else_try),
			# (this_or_next | eq, ":region", region_anatolian),
			# (eq, ":region", region_mongol),
			# (assign, ":template", "pt_peasant_rebels_mongol"),
			# (else_try),
			# (eq, ":region", region_andalusian),
			# (assign, ":template", "pt_peasant_rebels_andalus"),
			# (else_try),
			# (eq, ":region", region_north_african),
			# (assign, ":template", "pt_peasant_rebels_marinid"),
			# (else_try),
			# (this_or_next | eq, ":region", region_crusaders),
			# (eq, ":region", region_mamluk),
			# (assign, ":template", "pt_peasant_rebels_mamluke"),
			# (try_end),
			
			# (assign, ":spawn_spot", -1),
			# (try_for_range, ":cur_town", towns_begin, towns_end),
			# (store_faction_of_party, ":town_faction", ":cur_town"),
			# (eq, ":town_faction", ":faction"),
			# (assign, ":spawn_spot", ":cur_town"),
			# (try_end),
			
			# (assign, ":message_shown", 0),
			
			# (try_for_range, ":unused", 0, ":parties_to_spawn"),
			# (store_current_day, ":cur_day"),
			# (faction_get_slot, ":last_rebellion", ":faction", slot_faction_peasant_rebellion_last),
			# (store_sub, ":ok_to_rebel", ":cur_day", ":last_rebellion"),
			# (ge, ":ok_to_rebel", 30),
			# (try_begin),
				# (gt, ":fac_average_prosperity", 0),
				# (le, ":fac_average_prosperity", 25),
				# (store_num_parties_of_template, ":num_parties", ":template"),
				# (lt,":num_parties",":parties_to_spawn"),
				# (spawn_around_party,":spawn_spot",":template"),
				# (assign, ":party_id", reg0),
				# (party_set_ai_behavior, ":party_id", ai_bhvr_patrol_party),
				# (party_set_ai_object, ":party_id", ":spawn_spot"),
				# (party_set_ai_patrol_radius, ":party_id", 10),
				# (str_store_faction_name, s25, ":faction"),
				# (party_set_slot, ":party_id", slot_party_ai_object, ":spawn_spot"),
				# (try_begin),
				# (eq, ":message_shown", 0),
				# (display_message, "@Peasants revolt in areas controlled by the {s25}!", 0xff0000),
				# (faction_set_slot, ":faction", slot_faction_peasant_rebellion_last, ":cur_day"),
				# (assign, ":message_shown", 1),
				# (try_end),
			# (try_end),
			# (try_end),
		# (try_end),
		]
	),
	
	##diplomacy begin
	#recruiter kit begin
	("dplmc_send_recruiter",
		[
		(store_script_param, ":number_of_recruits", 1),
		#daedalus begin
		(store_script_param, ":faction_of_recruits", 2),
		(store_script_param, ":recruit_type", 3),
		#daedalus end
		(assign, ":expenses", ":number_of_recruits"),
		#(val_mul, ":expenses", 20),
		(val_mul, ":expenses", reg22),
		#(val_add, ":expenses", 10),
		(val_add, ":expenses", 250),
		(call_script, "script_dplmc_withdraw_from_treasury", ":expenses"),
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_dplmc_recruiter"),
		(assign,":spawned_party",reg0),
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_hold),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_recruiter),
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits, ":number_of_recruits"),
		#daedalus begin
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits_faction, ":faction_of_recruits"),
		#daedalus end
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_origin, "$current_town"),
		(assign, ":faction", "$players_kingdom"),
		(party_set_faction, ":spawned_party", ":faction"),
		(party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_recruitment_type, ":recruit_type"),
	]),
	#recruiter kit end
	
	("dplmc_describe_prosperity_to_s4",
		[
		(store_script_param_1, ":center_no"),
		
		(str_store_party_name, s60,":center_no"),
		(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
		(str_store_string, s4, "str_empty_string"),
		(try_begin),
			(is_between, ":center_no", towns_begin, towns_end),
			(try_begin),
			(eq, ":prosperity", 0),
			(str_store_string, s4, "str_town_prosperity_0"),
			(else_try),
			(is_between, ":prosperity", 1, 11),
			(str_store_string, s4, "str_town_prosperity_10"),
			(else_try),
			(is_between, ":prosperity", 11, 21),
			(str_store_string, s4, "str_town_prosperity_20"),
			(else_try),
			(is_between, ":prosperity", 21, 31),
			(str_store_string, s4, "str_town_prosperity_30"),
			(else_try),
			(is_between, ":prosperity", 31, 41),
			(str_store_string, s4, "str_town_prosperity_40"),
			(else_try),
			(is_between, ":prosperity", 41, 51),
			(str_store_string, s4, "str_town_prosperity_50"),
			(else_try),
			(is_between, ":prosperity", 51, 61),
			(str_store_string, s4, "str_town_prosperity_60"),
			(else_try),
			(is_between, ":prosperity", 61, 71),
			(str_store_string, s4, "str_town_prosperity_70"),
			(else_try),
			(is_between, ":prosperity", 71, 81),
			(str_store_string, s4, "str_town_prosperity_80"),
			(else_try),
			(is_between, ":prosperity", 81, 91),
			(str_store_string, s4, "str_town_prosperity_90"),
			(else_try),
			(is_between, ":prosperity", 91, 101),
			(str_store_string, s4, "str_town_prosperity_100"),
			(try_end),
		(else_try),
			(is_between, ":center_no", villages_begin, villages_end),
			(try_begin),
			(eq, ":prosperity", 0),
			(str_store_string, s4, "str_village_prosperity_0"),
			(else_try),
			(is_between, ":prosperity", 1, 11),
			(str_store_string, s4, "str_village_prosperity_10"),
			(else_try),
			(is_between, ":prosperity", 11, 21),
			(str_store_string, s4, "str_village_prosperity_20"),
			(else_try),
			(is_between, ":prosperity", 21, 31),
			(str_store_string, s4, "str_village_prosperity_30"),
			(else_try),
			(is_between, ":prosperity", 31, 41),
			(str_store_string, s4, "str_village_prosperity_40"),
			(else_try),
			(is_between, ":prosperity", 41, 51),
			(str_store_string, s4, "str_village_prosperity_50"),
			(else_try),
			(is_between, ":prosperity", 51, 61),
			(str_store_string, s4, "str_village_prosperity_60"),
			(else_try),
			(is_between, ":prosperity", 61, 71),
			(str_store_string, s4, "str_village_prosperity_70"),
			(else_try),
			(is_between, ":prosperity", 71, 81),
			(str_store_string, s4, "str_village_prosperity_80"),
			(else_try),
			(is_between, ":prosperity", 81, 91),
			(str_store_string, s4, "str_village_prosperity_90"),
			(else_try),
			(is_between, ":prosperity", 91, 101),
			(str_store_string, s4, "str_village_prosperity_100"),
			(try_end),
		(try_end),
	]),
	
	("dplmc_pay_into_treasury",
		[
		(store_script_param_1, ":amount"),
		(troop_add_gold, "trp_household_possessions", ":amount"),
		(assign, reg0, ":amount"),
		(play_sound, "snd_money_received"),
		(display_message, "@{reg0} denars added to treasury."),
	]),
	
	("dplmc_withdraw_from_treasury",
		[
		(store_script_param_1, ":amount"),
		(troop_remove_gold, "trp_household_possessions", ":amount"),
		(assign, reg0, ":amount"),
		(play_sound, "snd_money_paid"),
		(display_message, "@{reg0} denars removed from treasury."),
	]),
	
	("dplmc_describe_tax_rate_to_s50",
		[
		(store_script_param_1, ":tax_rate"),
		#(val_div, ":tax_rate", 25), #tom
		(store_add, ":str_id","str_dplmc_tax_normal", ":tax_rate"),
		(str_store_string, s50, ":str_id"),
	]),
	
	
	("dplmc_player_troops_leave",
		[
		(store_script_param_1, ":percent"),
		
		(try_begin),#debug
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":percent"),
			(display_message, "@{!}DEBUG : removing player troops: {reg0}%"),
		(try_end),
		
		(assign, ":deserters", 0),
		(try_for_parties, ":party_no"),
			(assign, ":remove_troops", 0),
			(try_begin),
			(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
			(party_slot_eq|party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
			(assign, ":remove_troops", 1),
			(else_try),
			(eq, "p_main_party", ":party_no"),
			(assign, ":remove_troops", 1),
			(try_end),
			
			(eq, ":remove_troops", 1),
			(party_get_num_companion_stacks, ":num_stacks",":party_no"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_size, ":stack_size",":party_no",":i_stack"),
			(val_mul, ":stack_size", ":percent"),
			(val_div, ":stack_size", 100),
			(party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
			(party_remove_members, ":party_no", ":troop_id", ":stack_size"),
			(val_add, ":deserters", ":stack_size"),
			(try_end),
		(try_end),
		(assign, reg0, ":deserters"),
		]
	),
	
	("dplmc_get_item_buy_price_factor",
		[
		(store_script_param_1, ":item_kind_id"),
		(store_script_param_2, ":center_no"),
		(assign, ":price_factor", 100),
		
		(call_script, "script_get_trade_penalty", ":item_kind_id"),
		(assign, ":trade_penalty", reg0),
		
		(try_begin),
			(is_between, ":center_no", centers_begin, centers_end),
			(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
			(store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
			(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
			(party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),
			
			(try_begin),
			(is_between, ":center_no", villages_begin, villages_end),
			(party_get_slot, ":market_town", ":center_no", slot_village_market_town),
			(party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
			(val_max, ":price_factor", ":price_in_market_town"),
			(try_end),
			
			#For villages, the good will be sold no cheaper than in the market town
			#This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers
			
			(val_mul, ":price_factor", 100), #normalize price factor to range 0..100
			(val_div, ":price_factor", average_price_factor),
		(try_end),
		
		(store_add, ":penalty_factor", 100, ":trade_penalty"),
		
		(val_mul, ":price_factor", ":penalty_factor"),
		(val_div, ":price_factor", 100),
		
		(assign, reg0, ":price_factor"),
		(set_trigger_result, reg0),
	]),
	
	("dplmc_party_calculate_strength",
		[
		(store_script_param_1, ":party"), #Party_id
		(store_script_param_2, ":exclude_leader"), #Party_id
		
		(assign, reg0,0),
		(party_get_num_companion_stacks, ":num_stacks", ":party"),
		(assign, ":first_stack", 0),
		(try_begin),
			(neq, ":exclude_leader", 0),
			(assign, ":first_stack", 1),
		(try_end),
		
		(assign, ":sum", 0),
		(try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
			
			(try_begin),
			(neg|troop_is_hero, ":stack_troop"),
			(party_stack_get_size, ":stack_size",":party",":i_stack"),
			(try_end),
			(val_add, ":sum", ":stack_size"),
		(try_end),
		(assign, reg0, ":sum"),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : sum: {reg0}"),
		(try_end),
	]),
	
	#script_dplmc_start_alliance_between_kingdoms, 20 days alliance, 40 days truce after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	("dplmc_start_alliance_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 15),
		(val_max, ":relation", 40),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 15),
			(val_max, ":relation", 40),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 15),
			(val_max, ":relation", 40),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded an alliance with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 80),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 80),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
		
		# share wars
		(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
			(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			(neq, ":kingdom_a", ":faction_no"),
			(neq, ":kingdom_b", ":faction_no"),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
			#result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
			(eq, reg0, -2),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
			(ge, reg0, -1),
			(call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", 1),
		(try_end),
		(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
			(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			(neq, ":kingdom_a", ":faction_no"),
			(neq, ":kingdom_b", ":faction_no"),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
			#result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
			(eq, reg0, -2),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
			(ge, reg0, -1),
			(call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", 1),
		(try_end),
	]),
	
	#script_dplmc_start_defensive_between_kingdoms, 20 days defensive: 20 days trade aggreement, 20 days non-aggression after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	("dplmc_start_defensive_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 10),
		(val_max, ":relation", 30),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 10),
			(val_max, ":relation", 30),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 10),
			(val_max, ":relation", 30),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded a defensive pact with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
			
			
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 60),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 60),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
	]),
	
	#script_dplmc_start_trade_between_kingdoms, 20 days trade aggreement, 20 days non-aggression after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	("dplmc_start_trade_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 5),
		(val_max, ":relation", 20),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 5),
			(val_max, ":relation", 20),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 5),
			(val_max, ":relation", 20),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded a trade agreement with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
			
			
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
	]),
	
	#script_dplmc_start_nonaggression_between_kingdoms, 20 days non-aggression
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	("dplmc_start_nonaggression_between_kingdoms", #sets relations between two kingdoms
		[
		(store_script_param, ":kingdom_a", 1),
		(store_script_param, ":kingdom_b", 2),
		(store_script_param, ":initializing_war_peace_cond", 3),
		
		(store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
		(val_add, ":relation", 3),
		(val_max, ":relation", 10),
		(set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
		(call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
		
		(try_begin),
			(eq, "$players_kingdom", ":kingdom_a"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
			(val_add, ":relation", 3),
			(val_max, ":relation", 10),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
		(else_try),
			(eq, "$players_kingdom", ":kingdom_b"),
			(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
			(val_add, ":relation", 3),
			(val_max, ":relation", 10),
			(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
			#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
		(try_end),
		
		(try_begin),
			(eq, ":initializing_war_peace_cond", 1),
			(str_store_faction_name_link, s1, ":kingdom_a"),
			(str_store_faction_name_link, s2, ":kingdom_b"),
			(display_log_message, "@{s1} and {s2} have concluded a non aggression pact with each other."),
			
			(call_script, "script_add_notification_menu", "mnu_dplmc_notification_nonaggression_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
			
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
			(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
			(assign, "$g_recalculate_ais", 1),
			
			
		(try_end),
		
		(try_begin), #add truce
			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_b", ":truce_slot", 20),
			
			(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
			
			(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
			(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
			
			(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
			(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
			(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
			(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
			(try_end),
			(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
			
		(try_end),
	]),
	
	
	
	# Input: arg1 = faction_no_1, arg2 = faction_no_2
	("dplmc_get_prisoners_value_between_factions",
		[
		(store_script_param, ":faction_no_1", 1),
		(store_script_param, ":faction_no_2", 2),
		
		(assign, ":faction_no_1_value", 0),
		(assign, ":faction_no_2_value", 0),
		
		(try_for_parties, ":party_no"),
			(store_faction_of_party, ":party_faction", ":party_no"),
			(try_begin),
			(eq, ":party_faction", ":faction_no_1"),
			(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
			(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
				(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
				(store_troop_faction, ":cur_faction", ":cur_troop_id"),
				
				(eq, ":cur_faction", ":faction_no_2"),
				(try_begin),
				(troop_is_hero, ":cur_troop_id"),
				(call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
				(val_add, ":faction_no_1_value", reg0),
				
				(try_begin),#debug
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":faction_no_1_value"),
					(display_message, "@{!}DEBUG : faction_no_1_value: {reg0}"),
				(try_end),
				
				(try_end),
			(try_end),
			(else_try),
			(eq, ":party_faction", ":faction_no_2"),
			(party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
			(try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
				(party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
				(store_troop_faction, ":cur_faction", ":cur_troop_id"),
				
				(eq, ":cur_faction", ":faction_no_1"),
				(try_begin),
				(troop_is_hero, ":cur_troop_id"),
				(call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
				(val_add, ":faction_no_2_value", reg0),
				
				(try_begin), #debug
					(eq, "$cheat_mode", 1),
					(assign, reg0, ":faction_no_2_value"),
					(display_message, "@{!}DEBUG : faction_no_2_value: {reg0}"),
				(try_end),
				
				(try_end),
			(try_end),
			(try_end),
		(try_end),
		(store_sub, reg0, ":faction_no_1_value", ":faction_no_2_value"),
	]),
	
	# Input: arg1 = faction_no_1, arg2 = faction_no_2
	("dplmc_get_truce_pay_amount",
		[
		(store_script_param, ":faction_no_1", 1),
		(store_script_param, ":faction_no_2", 2),
		(store_script_param, ":check_peace_war_result", 3),
		
		(assign, ":peace_war_param", 1000),
		(assign, ":concession_param", 3000), #value of a concession
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":check_peace_war_result"), #debug
			(display_message, "@{!}DEBUG : peace_war_result: {reg0}"),#debug
		(try_end),
		
		(val_sub, ":check_peace_war_result", 1),
		(val_mul, ":check_peace_war_result", 4),
		(val_mul, ":check_peace_war_result", ":peace_war_param"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":check_peace_war_result"), #debug
			(display_message, "@{!}DEBUG : peace_war_result after multi: {reg0}"),#debug
		(try_end),
		
		(call_script, "script_dplmc_get_prisoners_value_between_factions", ":faction_no_1", ":faction_no_2"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : prisonser_value: {reg0}"),#debug
		(try_end),
		
		(val_sub, ":check_peace_war_result", reg0),
		(val_max, ":check_peace_war_result", 0),
		(assign, reg0, ":check_peace_war_result"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : peace_war_result after prisoners: {reg0}"),#debug
		(try_end),
		
		(assign, reg1, -1),
		(try_begin),
			(gt, "$g_concession_demanded", 0),
			(assign, ":concession_value", 2),
			(try_begin),
			(is_between, "$g_concession_demanded", towns_begin, towns_end),
			(assign, ":concession_value", 3),
			(else_try),
			(is_between, "$g_concession_demanded", castles_begin, castles_end),
			(assign, ":concession_value", 2),
			(else_try),
			(is_between, "$g_concession_demanded", villages_begin, villages_end),
			(assign, ":concession_value", 1),
			(try_end),
			(val_mul, ":concession_value", ":concession_param"),
			
			(store_sub, reg1, reg0, ":concession_value"), #reg4 = reg3 - concession_value
			(val_max, reg1, 0),
		(try_end),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG : truce_pay_amount0: {reg0}"),
			(display_message, "@{!}DEBUG : truce_pay_amount1: {reg1}"),
		(try_end),
	]),
	
	("dplmc_player_center_surrender",
		[
		(store_script_param, ":center_no", 1),
		
		#protect player for 24 hours
		(store_current_hours,":protected_until"),
		(val_add, ":protected_until", 48),
		(party_get_slot, ":besieger", ":center_no", slot_center_is_besieged_by),
		(store_faction_of_party, ":besieger_faction",":besieger"),
		(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
		
		(party_set_slot,":besieger",slot_party_ignore_player_until,":protected_until"),
		(party_ignore_player, ":besieger", 48),
		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":besieger_faction"),
			(troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
			(party_is_active, ":led_party"),
			
			(party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
			(party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),
			
			(party_is_active, ":besieger"),
			(store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
			(lt, ":distance_to_marshal", 20),
			
			(party_set_slot,":led_party",slot_party_ignore_player_until,":protected_until"),
			(party_ignore_player, ":led_party", 48),
		(try_end),
		
		(party_set_faction,"$current_town","fac_neutral"), #temporarily erase faction so that it is not the closest town
		(party_get_num_attached_parties, ":num_attached_parties_to_castle",":center_no"),
		(try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
			(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":iap"),
			(party_detach, ":attached_party"),
			(party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
			(eq, ":attached_party_type", spt_kingdom_hero_party),
			(neq, ":attached_party_type", "p_main_party"),
			(store_faction_of_party, ":attached_party_faction", ":attached_party"),
			(call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
			(try_begin),
			(gt, reg0, 0),
			(call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
			(else_try),
			(call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, ":center_no"),
			(try_end),
		(try_end),
		(call_script, "script_party_remove_all_companions", ":center_no"),
		(change_screen_return),
		(party_collect_attachments_to_party, ":center_no", "p_collective_enemy"), #recalculate so that
		(call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
		
		(call_script, "script_give_center_to_faction", "$current_town", ":besieger_faction"),
		(call_script, "script_order_best_besieger_party_to_guard_center", ":center_no", ":besieger_faction"),
		
		#relation and controversy
		(call_script, "script_change_player_relation_with_troop", ":enemy_party_leader", 2),
		(try_begin),
			(gt, "$players_kingdom", 0),
			(neq, "$players_kingdom", "fac_player_supporters_faction"),
			(neq, "$players_kingdom", "fac_player_faction"),
			(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
			(neq, ":faction_leader", "trp_player"),
			(call_script, "script_change_player_relation_with_troop", ":faction_leader", -2),
		(try_end),
		
		(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
		(val_add, ":controversy", 4),
		(val_min, ":controversy", 100),
		(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
	]),
	
	
	("dplmc_send_messenger_to_troop",
		[
		(store_script_param, ":target_troop", 1),
		(store_script_param, ":message", 2),
		(store_script_param, ":orders_object", 3),
		
		(troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
		
		(try_begin),
			(eq, ":message", spai_accompanying_army),
			(assign, ":orders_object", "p_main_party"),
		(try_end),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_messenger_party"),
		(assign,":spawned_party",reg0),
		(party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
		(store_faction_of_troop, ":player_faction", "trp_player"),
		(party_set_faction, ":spawned_party", ":player_faction"),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_messenger),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
		(party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Send message to {s13}"),
		(try_end),
		]
	),
	
	("dplmc_send_messenger_to_party",
		[
		(store_script_param, ":target_party", 1),
		(store_script_param, ":message", 2),
		(store_script_param, ":orders_object", 3),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_messenger_party"),
		(assign,":spawned_party",reg0),
		(party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
		(party_set_faction, ":spawned_party", "fac_player_faction"),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_messenger),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
		(party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Send message to {s13}"),
		(try_end),
		]
	),
	
	("dplmc_send_gift",
		[
		(store_script_param, ":target_troop", 1),
		(store_script_param, ":gift", 2),
		
		(try_begin),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
			(troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
		(else_try),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
			(troop_get_slot, ":target_party", ":target_troop", slot_troop_cur_center),
		(try_end),
		
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_item_name, s12, ":gift"),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
		(try_end),
		
		(call_script, "script_dplmc_withdraw_from_treasury", 50),
		(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
		(try_begin),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
			(assign, ":amount", 150),
			(try_for_range, ":inventory_slot", 0, ":capacity"),
			(gt, ":amount", 0),
			(troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
			(eq, ":item", ":gift"),
			(troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
			(try_begin),
				(le, ":tmp_amount", ":amount"),
				(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
				(val_sub, ":amount", ":tmp_amount"),
			(else_try),
				(val_sub, ":tmp_amount", ":amount"),
				(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
				(assign, ":amount", 0),
			(try_end),
			(try_end),
		(else_try),
			(troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
			(troop_remove_item, "trp_household_possessions", ":gift"),
		(try_end),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
		(assign,":spawned_party",reg0),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
		(party_set_slot, ":spawned_party",  slot_party_orders_object,  ":target_troop"),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
		(troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
	]),
	
	("dplmc_send_gift_to_center",
		[
		(store_script_param, ":target_party", 1),
		(store_script_param, ":gift", 2),
		
		(try_begin), #debug
			(eq, "$cheat_mode", 1),
			(str_store_item_name, s12, ":gift"),
			(str_store_party_name, s13, ":target_party"),
			(display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
		(try_end),
		
		(call_script, "script_dplmc_withdraw_from_treasury", 50),
		(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
		(assign, ":amount", 300),
		(try_for_range, ":inventory_slot", 0, ":capacity"),
			(gt, ":amount", 0),
			(troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
			(eq, ":item", ":gift"),
			(troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
			(try_begin),
			(le, ":tmp_amount", ":amount"),
			(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
			(val_sub, ":amount", ":tmp_amount"),
			(else_try),
			(val_sub, ":tmp_amount", ":amount"),
			(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
			(assign, ":amount", 0),
			(try_end),
		(try_end),
		
		(set_spawn_radius, 1),
		(spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
		(assign,":spawned_party",reg0),
		(party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
		(party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
		(party_set_slot, ":spawned_party",  slot_party_orders_object, 0),
		
		(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
		(party_set_ai_object, ":spawned_party", ":target_party"),
		(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
		(party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
		(troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
		(troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
	]),
	
	("dplmc_troop_political_notes_to_s47",
		[
		(store_script_param, ":troop_no", 1),
		(try_begin),
			(str_clear, s47),
			
			(store_faction_of_troop, ":troop_faction", ":troop_no"),
			
			(faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
			
			(str_clear, s40),
			(assign, ":logged_a_rivalry", 0),
			(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_hero"),
			(lt, reg0, -10),
			
			(str_store_troop_name_link, s39, ":kingdom_hero"),
			(try_begin),
				(eq, ":logged_a_rivalry", 0),
				(str_store_string, s40, "str_dplmc_s39_rival"),
				(assign, ":logged_a_rivalry", 1),
			(else_try),
				(str_store_string, s41, "str_s40"),
				(str_store_string, s40, "str_dplmc_s41_s39_rival"),
			(try_end),
			
			(try_end),
			
			(str_clear, s46),
			(str_store_troop_name, s46,":troop_no"),
			(try_begin),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_martial"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_debauched"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_pitiless"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_calculating"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_quarrelsome"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_goodnatured"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_upstanding"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_conventional"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_adventurous),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_adventurous"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_otherworldly),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_romantic"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_moralist"),
			(else_try),
			(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_ambitious),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_ambitious"),
			(else_try),
			(troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
			(str_store_string, s46, "str_dplmc_reputation_cheat_mode_only_reg11"),
			(try_end),
			
			(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
			(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
			(str_store_troop_name, s39, ":love_interest"),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":love_interest"),
			(str_store_string, s45, "str_dplmc_s40_love_interest_s39"),
			(try_begin),
				(troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
				(str_store_string, s45, "str_dplmc_s40_betrothed_s39"),
			(try_end),
			(try_end),
			
			(str_clear, s44),
			(try_begin),
			(neq, ":troop_no", ":faction_leader"),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			
			(assign, ":relation", reg0),
			(store_add, ":normalized_relation", ":relation", 100),
			(val_add, ":normalized_relation", 5),
			(store_div, ":str_offset", ":normalized_relation", 10),
			(val_clamp, ":str_offset", 0, 20),
			(store_add, ":str_id", "str_dplmc_relation_mnus_100_ns",  ":str_offset"),
			(try_begin),
				(eq, ":faction_leader", "trp_player"),
				(str_store_string, s59, "@you"),
			(else_try),
				(str_store_troop_name, s59, ":faction_leader"),
			(try_end),
			(str_store_string, s59, ":str_id"),
			(str_store_string, s44, "@{!}^{s59}"),
			(try_end),
			
			(str_clear, s48),
			
			(try_begin),
			(eq, "$cheat_mode", 1),
			(store_current_hours, ":hours"),
			(gt, ":hours", 0),
			(call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),
			(str_store_string, s48, "str_sense_of_security_military_reg1_court_position_reg3_"),
			(try_end),
			
			(str_store_string, s47, "str_s46s45s44s48"),
			
		(try_end),
	]),
	
	
	## CC
	####################################################################################
	#
	# Autoloot Scripts begin
	# ---------------------------------------------------
	####################################################################################
	
	###################################
	# Can a troop qualify to use this item?
	# Returns 1 = yes, 0 = no.
	("troop_can_use_item",
		[
		(store_script_param, ":troop", 1),
		(store_script_param, ":item", 2),
		(store_script_param, ":item_modifier", 3),
		
		(item_get_type, ":type", ":item"),
		(try_begin),
			(eq, ":type", itp_type_book),
			(item_get_slot, ":difficulty", ":item", slot_item_intelligence_requirement),
		(else_try),
			(item_get_slot, ":difficulty", ":item", slot_item_difficulty),
		(try_end),
		
		(try_begin),
			(eq, ":difficulty", 0), # don't apply imod modifiers if item has no requirement
		(else_try),
			(eq, ":item_modifier", imod_stubborn),
			(val_add, ":difficulty", 1),
		(else_try),
			(eq, ":item_modifier", imod_timid),
			(val_sub, ":difficulty", 1),
		(else_try),
			(eq, ":item_modifier", imod_heavy),
			(neq, ":type", itp_type_horse), #heavy horses don't increase difficulty
			(val_add, ":difficulty", 1),
		(else_try),
			(eq, ":item_modifier", imod_strong),
			(val_add, ":difficulty", 2),
		(else_try),
			(eq, ":item_modifier", imod_masterwork),
			(val_add, ":difficulty", 4),
		(try_end),
		
		(try_begin),
			(eq, ":type", itp_type_horse),
			(store_skill_level, ":skill", skl_riding, ":troop"),
		(else_try),
			(this_or_next|eq, ":type", itp_type_crossbow),
			(this_or_next|eq, ":type", itp_type_one_handed_wpn),
			(this_or_next|eq, ":type", itp_type_two_handed_wpn),
			(this_or_next|eq, ":type", itp_type_polearm),
			(this_or_next|eq, ":type", itp_type_head_armor),
			(this_or_next|eq, ":type", itp_type_body_armor),
			(this_or_next|eq, ":type", itp_type_foot_armor),
			(eq, ":type", itp_type_hand_armor),
			(store_attribute_level, ":skill", ":troop", ca_strength),
		(else_try),
			(eq, ":type", itp_type_shield),
			(store_skill_level, ":skill", skl_shield, ":troop"),
		(else_try),
			(eq, ":type", itp_type_bow),
			(store_skill_level, ":skill", skl_power_draw, ":troop"),
		(else_try),
			(eq, ":type", itp_type_thrown),
			(store_skill_level, ":skill", skl_power_throw, ":troop"),
		(else_try),
			(eq, ":type", itp_type_book),
			(store_attribute_level, ":skill", ":troop", ca_intelligence),
		(try_end),
		
		(try_begin),
			(this_or_next|lt, ":skill", ":difficulty"),
			(this_or_next|is_between, ":item", reference_books_begin, reference_books_end),
			(eq, ":item_modifier", imod_lame),
			(assign, reg0, 0),
		(else_try),
			(troop_slot_eq, ":troop", slot_upgrade_horse, 1),
			(item_slot_eq, ":item", slot_item_cant_on_horseback, 1),
			(assign, reg0, 0),
		(else_try),
			(assign, reg0, 1),
		(try_end),
	]),
	
	#####################################################################
	# gets an item's value
	# Param1: item ID
	# Param2: item modifier
	#####################################################################
	
	################################################################
	##### Custom Commander(CC)
	################################################################
	("get_item_value_with_imod",
		[# returns the sell price based on the item's money value and its imod
		(store_script_param, ":item", 1),
		(store_script_param, ":imod", 2),
		
		(store_item_value, ":score", ":item"),
		(item_get_slot, ":imod_multiplier", ":imod", slot_item_modifier_multiplier),
		(val_mul, ":score", ":imod_multiplier"),
		(assign, reg0, ":score"),
	]),
	
	("get_item_score_with_imod",
		[
		(store_script_param, ":item", 1),
		(store_script_param, ":imod", 2),
		
		(item_get_type, ":type", ":item"),
		(try_begin),
			(eq, ":type", itp_type_book),
			(item_get_slot, ":i_score", ":item", slot_item_intelligence_requirement),
		(else_try),
			(eq, ":type", itp_type_horse),
			(item_get_slot, ":horse_speed", ":item", slot_item_horse_speed),
			(item_get_slot, ":horse_armor", ":item", slot_item_horse_armor),
			(item_get_slot, ":horse_charge", ":item", slot_item_horse_charge),
			
			(try_begin),
			(eq, ":imod", imod_swaybacked),
			(val_add, ":horse_speed", -2),
			(else_try),
			(eq, ":imod", imod_lame),
			(val_add, ":horse_speed", -5),
			(else_try),
			(eq, ":imod", imod_heavy),
			(val_add, ":horse_armor", 3),
			(val_add, ":horse_charge", 4),
			(else_try),
			(eq, ":imod", imod_spirited),
			(val_add, ":horse_speed", 1),
			(val_add, ":horse_armor", 1),
			(val_add, ":horse_charge", 1),
			(else_try),
			(eq, ":imod", imod_champion),
			(val_add, ":horse_speed", 2),
			(val_add, ":horse_armor", 2),
			(val_add, ":horse_charge", 2),
			(try_end),
			
			(store_mul, ":i_score", ":horse_speed", ":horse_armor"),
			(val_mul, ":i_score", ":horse_charge"),
		(else_try),
			(eq, ":type", itp_type_shield),
			(item_get_slot, ":shield_size", ":item", slot_item_length),
			(item_get_slot, ":shield_armor", ":item", slot_item_body_armor),
			(item_get_slot, ":shield_speed", ":item", slot_item_speed),
			
			(try_begin),
			(eq, ":imod", imod_cracked),
			(val_add, ":shield_armor", -4),
			(else_try),
			(eq, ":imod", imod_battered),
			(val_add, ":shield_armor", -2),
			(else_try),
			(eq, ":imod", imod_thick),
			(val_add, ":shield_armor", 2),
			(else_try),
			(eq, ":imod", imod_reinforced),
			(val_add, ":shield_armor", 4),
			(try_end),
			
			(val_add, ":shield_armor", 5),
			(store_mul, ":i_score", ":shield_armor", ":shield_size"),
			(val_mul, ":i_score", ":shield_speed"),
		(else_try),
			(this_or_next|eq, ":type", itp_type_head_armor),
			(this_or_next|eq, ":type", itp_type_body_armor),
			(this_or_next|eq, ":type", itp_type_foot_armor),
			(eq, ":type", itp_type_hand_armor),
			(item_get_slot, ":head_armor", ":item", slot_item_head_armor),
			(item_get_slot, ":body_armor", ":item", slot_item_body_armor),
			(item_get_slot, ":leg_armor", ":item", slot_item_leg_armor),
			(store_add, ":i_score", ":head_armor", ":body_armor"),
			(val_add, ":i_score", ":leg_armor"),
			
			(assign, ":imod_effect_mul", 0),
			(try_begin),
			(gt, ":head_armor", 0),
			(val_add, ":imod_effect_mul", 1),
			(try_end),
			(try_begin),
			(gt, ":body_armor", 0),
			(val_add, ":imod_effect_mul", 1),
			(try_end),
			(try_begin),
			(gt, ":leg_armor", 0),
			(val_add, ":imod_effect_mul", 1),
			(try_end),
			
			(try_begin),
			(eq, ":imod", imod_plain),
			(assign, ":imod_effect", 0),
			(else_try),
			(eq, ":imod", imod_cracked),
			(assign, ":imod_effect", -4),
			(else_try),
			(eq, ":imod", imod_rusty),
			(assign, ":imod_effect", -3),
			(else_try),
			(eq, ":imod", imod_battered),
			(assign, ":imod_effect", -2),
			(else_try),
			(eq, ":imod", imod_crude),
			(assign, ":imod_effect", -1),
			(else_try),
			(eq, ":imod", imod_tattered),
			(assign, ":imod_effect", -3),
			(else_try),
			(eq, ":imod", imod_ragged),
			(assign, ":imod_effect", -2),
			(else_try),
			(eq, ":imod", imod_sturdy),
			(assign, ":imod_effect", 1),
			(else_try),
			(eq, ":imod", imod_thick),
			(assign, ":imod_effect", 2),
			(else_try),
			(eq, ":imod", imod_hardened),
			(assign, ":imod_effect", 3),
			(else_try),
			(eq, ":imod", imod_reinforced),
			(assign, ":imod_effect", 4),
			(else_try),
			(eq, ":imod", imod_lordly),
			(assign, ":imod_effect", 6),
			(try_end),
			
			(val_mul, ":imod_effect", ":imod_effect_mul"),
			(val_add, ":i_score", ":imod_effect"),
		(else_try),
			(this_or_next|eq, ":type", itp_type_one_handed_wpn),
			(this_or_next|eq, ":type", itp_type_two_handed_wpn),
			(this_or_next|eq, ":type", itp_type_bow),
			(this_or_next|eq, ":type", itp_type_crossbow),
			(this_or_next|eq, ":type", itp_type_pistol),
			(this_or_next|eq, ":type", itp_type_musket),
			(eq, ":type", itp_type_polearm),
			(item_get_slot, ":item_speed", ":item", slot_item_speed),
			(item_get_slot, ":item_length", ":item", slot_item_length),
			(item_get_slot, ":swing_damage", ":item", slot_item_swing_damage),
			(item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
			(val_mod, ":swing_damage", 256),
			(val_mod, ":thrust_damage", 256),
			(assign, ":item_damage", ":swing_damage"),
			(val_max, ":item_damage", ":thrust_damage"),
			
			(try_begin),
			(eq, ":imod", imod_cracked),
			(val_add, ":item_damage", -5),
			(else_try),
			(eq, ":imod", imod_rusty),
			(val_add, ":item_damage", -3),
			(else_try),
			(eq, ":imod", imod_bent),
			(val_add, ":item_damage", -3),
			(val_add, ":item_speed", -3),
			(else_try),
			(eq, ":imod", imod_chipped),
			(val_add, ":item_damage", -1),
			(else_try),
			(eq, ":imod", imod_balanced),
			(val_add, ":item_damage", 3),
			(val_add, ":item_speed", 3),
			(else_try),
			(eq, ":imod", imod_tempered),
			(val_add, ":item_damage", 4),
			(else_try),
			(eq, ":imod", imod_masterwork),
			(val_add, ":item_damage", 5),
			(val_add, ":item_speed", 1),
			(else_try),
			(eq, ":imod", imod_heavy),
			(val_add, ":item_damage", 2),
			(val_add, ":item_speed", -2),
			(else_try),
			(eq, ":imod", imod_strong),
			(val_add, ":item_damage", 3),
			(val_add, ":item_speed", -3),
			(try_end),
			
			(try_begin),
			(this_or_next|eq, ":type", itp_type_bow),
			(this_or_next|eq, ":type", itp_type_crossbow),
			(this_or_next|eq, ":type", itp_type_pistol),
			(eq, ":type", itp_type_musket),
			(store_mul, ":i_score", ":item_damage", ":item_speed"),
			(else_try),
			(this_or_next|eq, ":type", itp_type_one_handed_wpn),
			(this_or_next|eq, ":type", itp_type_two_handed_wpn),
			(eq, ":type", itp_type_polearm),
			(store_mul, ":i_score", ":item_damage", ":item_speed"),
			(val_mul, ":i_score", ":item_length"),
			(try_end),
		(else_try),
			(this_or_next|eq, ":type", itp_type_arrows),
			(this_or_next|eq, ":type", itp_type_bolts),
			(this_or_next|eq, ":type", itp_type_bullets),
			(eq, ":type", itp_type_thrown),
			(item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
			(val_mod, ":thrust_damage", 256),
			(assign, ":i_score", ":thrust_damage"),
			(val_add, ":i_score", 3), # +3 to make sure damage > 0
			
			(try_begin),
			(eq, ":imod", imod_plain),
			(val_mul, ":i_score", 2),
			(else_try),
			(eq, ":imod", imod_large_bag),
			(val_mul, ":i_score", 2),
			(val_add, ":i_score", 1),
			(else_try),
			(eq, ":imod", imod_bent),
			(val_sub, ":i_score", 3),
			(val_mul, ":i_score", 2),
			(else_try),
			(eq, ":imod", imod_heavy),
			(val_add, ":i_score", 2),
			(val_mul, ":i_score", 2),
			(else_try),
			(eq, ":imod", imod_balanced),
			(val_add, ":i_score", 3),
			(val_mul, ":i_score", 2),
			(try_end),
		(try_end),
		
		(assign, reg0, ":i_score"),
	]),
	################################################################
	##### Custom Commander(CC)
	################################################################
	
	###################
	# Used in conversations
	
	("print_wpn_upgrades_to_s0",
		[
		(store_script_param_1, ":troop"),
		
		## CC
		(troop_get_slot,":upgrade_wpn_set_sel", ":troop", slot_upgrade_wpn_set_sel),
		(store_mul, ":offset", ":upgrade_wpn_set_sel", offset_of_two_sets_slot),
		(store_add, ":slot_upgrade_wpn_0", slot_upgrade_wpn_0, ":offset"),
		(store_add, ":slot_upgrade_wpn_1", slot_upgrade_wpn_1, ":offset"),
		(store_add, ":slot_upgrade_wpn_2", slot_upgrade_wpn_2, ":offset"),
		(store_add, ":slot_upgrade_wpn_3", slot_upgrade_wpn_3, ":offset"),
		## CC
		
		(str_store_string, s0, "str_empty_string"),
		(troop_get_slot, ":upg", ":troop", ":slot_upgrade_wpn_0"),
		(troop_get_inventory_slot, ":item", ":troop", 0),
		(try_begin),
			(ge, ":item", 0),
			(str_store_item_name, s10, ":item"),
		(else_try),
			(str_store_string, s10, "str_none"),
		(try_end),
		(val_add, ":upg", "str_hero_wpn_slot_none"),
		(str_store_string, s1, ":upg"),
		(str_store_string, s0, "@{s0}^{s1}"),
		(troop_get_slot, ":upg", ":troop", ":slot_upgrade_wpn_1"),
		(troop_get_inventory_slot, ":item", ":troop", 1),
		(try_begin),
			(ge, ":item", 0),
			(str_store_item_name, s10, ":item"),
		(else_try),
			(str_store_string, s10, "str_none"),
		(try_end),
		(val_add, ":upg", "str_hero_wpn_slot_none"),
		(str_store_string, s1, ":upg"),
		(str_store_string, s0, "@{s0}^{s1}"),
		(troop_get_slot, ":upg", ":troop", ":slot_upgrade_wpn_2"),
		(troop_get_inventory_slot, ":item", ":troop", 2),
		(try_begin),
			(ge, ":item", 0),
			(str_store_item_name, s10, ":item"),
		(else_try),
			(str_store_string, s10, "str_none"),
		(try_end),
		(val_add, ":upg", "str_hero_wpn_slot_none"),
		(str_store_string, s1, ":upg"),
		(str_store_string, s0, "@{s0}^{s1}"),
		(troop_get_slot, ":upg", ":troop", ":slot_upgrade_wpn_3"),
		(troop_get_inventory_slot, ":item", ":troop", 3),
		(try_begin),
			(ge, ":item", 0),
			(str_store_item_name, s10, ":item"),
		(else_try),
			(str_store_string, s10, "str_none"),
		(try_end),
		(val_add, ":upg", "str_hero_wpn_slot_none"),
		(str_store_string, s1, ":upg"),
		(str_store_string, s0, "@{s0}^{s1}"),
	]),
	
	################################
	# Copy this troop's upgrade options to everyone
	
	("copy_upgrade_to_all_heroes",
		[
		(store_script_param_1, ":troop"),
		(store_script_param_2, ":type"),
		
		(try_begin),
			(eq, ":type", wpn_setting_1),
			(troop_get_slot,":upg_wpn0", ":troop",slot_upgrade_wpn_0),
			(troop_get_slot,":upg_wpn1", ":troop",slot_upgrade_wpn_1),
			(troop_get_slot,":upg_wpn2", ":troop",slot_upgrade_wpn_2),
			(troop_get_slot,":upg_wpn3", ":troop",slot_upgrade_wpn_3),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_wpn_0,":upg_wpn0"),
			(troop_set_slot,":hero",slot_upgrade_wpn_1,":upg_wpn1"),
			(troop_set_slot,":hero",slot_upgrade_wpn_2,":upg_wpn2"),
			(troop_set_slot,":hero",slot_upgrade_wpn_3,":upg_wpn3"),
			(try_end),
		(else_try),
			(eq, ":type", wpn_setting_2),
			(troop_get_slot,":upg_wpn0", ":troop",slot_upgrade_wpn_0_set_2),
			(troop_get_slot,":upg_wpn1", ":troop",slot_upgrade_wpn_1_set_2),
			(troop_get_slot,":upg_wpn2", ":troop",slot_upgrade_wpn_2_set_2),
			(troop_get_slot,":upg_wpn3", ":troop",slot_upgrade_wpn_3_set_2),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_wpn_0_set_2,":upg_wpn0"),
			(troop_set_slot,":hero",slot_upgrade_wpn_1_set_2,":upg_wpn1"),
			(troop_set_slot,":hero",slot_upgrade_wpn_2_set_2,":upg_wpn2"),
			(troop_set_slot,":hero",slot_upgrade_wpn_3_set_2,":upg_wpn3"),
			(try_end),
		(else_try),
			(eq, ":type", armor_setting),
			(troop_get_slot,":upg_armor", ":troop",slot_upgrade_armor),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_armor,":upg_armor"),
			(try_end),
		(else_try),
			(eq, ":type", horse_setting),
			(troop_get_slot,":upg_horse", ":troop",slot_upgrade_horse),
			(try_for_range, ":hero", companions_begin, companions_end),
			(troop_set_slot,":hero",slot_upgrade_horse,":upg_horse"),
			(try_end),
		(try_end),
	]),
	
	####################################
	# Talk to this troop from the loot menu
	
	#("loot_menu_talk",
	#[
	#(store_script_param, ":troop", 1),
	#(modify_visitors_at_site,"scn_conversation_scene"),
	#(reset_visitors),
	#(set_visitor,0,"trp_player"),
	#(set_visitor,17,":troop"),
	#(set_jump_mission,"mt_conversation_encounter"),
	#(jump_to_scene,"scn_conversation_scene"),
	#(assign, "$g_camp_talk",1),
	#(change_screen_map_conversation, ":troop"),
	#]),
	
	####################################
	# Let each hero loot from the pool
	
	("auto_loot_all",
		[
		# once more to pick up any discards
		(try_for_range, ":unused", 0, 2),
			(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
			(is_between, ":this_hero", companions_begin, companions_end),
			(call_script, "script_auto_loot_troop", ":this_hero", "$pool_troop"),
			# # switch to another set
			# (troop_get_slot, ":wpn_set_sel", ":this_hero", slot_upgrade_wpn_set_sel),
			# (val_add, ":wpn_set_sel", 1),
			# (val_mod, ":wpn_set_sel", 2),
			# (troop_set_slot, ":this_hero", slot_upgrade_wpn_set_sel, ":wpn_set_sel"),
			# (call_script, "script_exchange_equipments_between_two_sets", ":this_hero"),
			# # auto_loot once more
			# (call_script, "script_auto_loot_troop", ":this_hero", "$pool_troop"),
			# # switch back
			# (troop_get_slot, ":wpn_set_sel", ":this_hero", slot_upgrade_wpn_set_sel),
			# (val_add, ":wpn_set_sel", 1),
			# (val_mod, ":wpn_set_sel", 2),
			# (troop_set_slot, ":this_hero", slot_upgrade_wpn_set_sel, ":wpn_set_sel"),
			# (call_script, "script_exchange_equipments_between_two_sets", ":this_hero"),
			(try_end),
		(try_end),
		#Done. Now sort the remainder
		(troop_sort_inventory, "$pool_troop"),
	]),
	
	
	####################################
	# let this troop take its pick from the loot pool
	
	("auto_loot_troop",
		[
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		
		
		(troop_get_slot,":upg_armor", ":troop",slot_upgrade_armor),
		(troop_get_slot,":upg_horses",":troop",slot_upgrade_horse),
		
		## CC
		(troop_get_slot,":upgrade_wpn_set_sel", ":troop", slot_upgrade_wpn_set_sel),
		(store_mul, ":offset", ":upgrade_wpn_set_sel", offset_of_two_sets_slot),
		(store_add, ":slot_upgrade_wpn_0", slot_upgrade_wpn_0, ":offset"),
		(store_add, ":slot_upgrade_wpn_1", slot_upgrade_wpn_1, ":offset"),
		(store_add, ":slot_upgrade_wpn_2", slot_upgrade_wpn_2, ":offset"),
		(store_add, ":slot_upgrade_wpn_3", slot_upgrade_wpn_3, ":offset"),
		## CC
		
		# dump whatever rubbish is in the main inventory
		## CC
		(call_script, "script_transfer_inventory", ":troop", ":pool", 0),
		## CC
		
		# dispose of the troop's equipped items if necessary
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_0", 1),
			(troop_get_inventory_slot, ":item", ":troop", 0),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 0),
			(troop_set_inventory_slot, ":troop", 0, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_1", 1),
			(troop_get_inventory_slot, ":item", ":troop", 1),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 1),
			(troop_set_inventory_slot, ":troop", 1, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_2", 1),
			(troop_get_inventory_slot, ":item", ":troop", 2),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 2),
			(troop_set_inventory_slot, ":troop", 2, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_begin),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_slot_ge, ":troop", ":slot_upgrade_wpn_3", 1),
			(troop_get_inventory_slot, ":item", ":troop", 3),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", 3),
			(troop_set_inventory_slot, ":troop", 3, -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
		(try_end),
		
		(try_for_range, ":i_slot", 4, 9),
			(store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
			(gt, ":pool_inv_cap", 0),
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
			(item_get_type, ":i_type", ":item"),
			(try_begin),
			(this_or_next|eq, ":i_type", itp_type_head_armor),
			(this_or_next|eq, ":i_type", itp_type_body_armor),
			(this_or_next|eq, ":i_type", itp_type_foot_armor),
			(eq, ":i_type", itp_type_hand_armor),
			(neq, ":upg_armor", 0), # we're uprgrading armors
			(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(else_try),
			(eq, ":i_type", itp_type_horse),
			(neq, ":upg_horses", 0), # we're uprgrading horses
			(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
			(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(try_end),
		(try_end),
		
		# clear best matches
		(assign, ":best_helmet_slot", -1),
		(assign, ":best_helmet_val", 0),
		(assign, ":best_body_slot", -1),
		(assign, ":best_body_val", 0),
		(assign, ":best_boots_slot", -1),
		(assign, ":best_boots_val", 0),
		(assign, ":best_gloves_slot", -1),
		(assign, ":best_gloves_val", 0),
		(assign, ":best_horse_slot", -1),
		(assign, ":best_horse_val", 0),
		#(assign, ":best_book_slot", -1),
		#(assign, ":best_book_val", 0),
		
		# Now search through the pool for the best items
		(troop_get_inventory_capacity, ":inv_cap", ":pool"),
		(try_for_range, ":i_slot", 0, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":pool", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":i_slot"),
			(call_script, "script_troop_can_use_item", ":troop", ":item", ":imod"),
			(eq, reg0, 1), # can use
			(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
			(assign, ":score", reg0),
			
			(item_get_type, ":item_type", ":item"),
			
			(try_begin),
			(eq, ":item_type", itp_type_horse), #it's a horse
			(eq, ":upg_horses", 1), # we're uprgrading horses
			(gt, ":score", ":best_horse_val"),
			(assign, ":best_horse_slot", ":i_slot"),
			(assign, ":best_horse_val", ":score"),
			(else_try),
			(try_begin),
				(eq, ":item_type", itp_type_head_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_helmet_val"),
				(assign, ":best_helmet_slot", ":i_slot"),
				(assign, ":best_helmet_val", ":score"),
			(else_try),
				(eq, ":item_type", itp_type_body_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_body_val"),
				(assign, ":best_body_slot", ":i_slot"),
				(assign, ":best_body_val", ":score"),
			(else_try),
				(eq, ":item_type", itp_type_foot_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_boots_val"),
				(assign, ":best_boots_slot", ":i_slot"),
				(assign, ":best_boots_val", ":score"),
			(else_try),
				(eq, ":item_type", itp_type_hand_armor),
				(eq, ":upg_armor", 1), # we're uprgrading armor
				(gt, ":score", ":best_gloves_val"),
				(assign, ":best_gloves_slot", ":i_slot"),
				(assign, ":best_gloves_val", ":score"),
			(try_end),
			(try_end),
		(try_end),
		# Now we know which ones are the best. Give them to the troop.
		(try_begin),
			(assign, ":best_slot", ":best_helmet_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":head_item", ":troop", ek_head),
			(eq, ":head_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_head, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_head, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_body_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":body_item", ":troop", ek_body),
			(eq, ":body_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_body, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_body, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_boots_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":foot_item", ":troop", ek_foot),
			(eq, ":foot_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_foot, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_foot, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_gloves_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":gloves_item", ":troop", ek_gloves),
			(eq, ":gloves_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_gloves, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_gloves, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		(try_begin),
			(assign, ":best_slot", ":best_horse_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":horse_item", ":troop", ek_horse),
			(eq, ":horse_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_horse, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_horse, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),
		
		# (try_begin),
		# (assign, ":best_slot", ":best_book_slot"),
		# (ge, ":best_slot", 0),
		# (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
		# (ge, ":item", 0),
		# (store_free_inventory_capacity, ":troop_inv_cap", ":troop"),
		# (gt, ":troop_inv_cap", 0),
		# (troop_slot_eq, ":troop", slot_troop_current_reading_book, 0),
		# (troop_add_item, ":troop", ":item"),
		# (troop_set_slot, ":troop", slot_troop_current_reading_book, ":item"),
		# (troop_set_inventory_slot, ":pool", ":best_slot", -1),
		# (try_end),
		
		(try_for_range, ":i_slot", 0, 4),
			(store_add, ":trp_slot", ":i_slot", ":slot_upgrade_wpn_0"),
			(troop_get_slot, ":type", ":troop", ":trp_slot"),
			(gt, ":type", 0), #we're upgrading for this slot
			(call_script, "script_scan_for_best_item_of_type", ":pool", ":type", ":troop"), #search for the best
			(assign, ":best_slot", reg0),
			(neq, ":best_slot", -1), #got something
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"), #get it
			(ge, ":item", 0),
			## CC
			(troop_get_inventory_slot, ":wpn_item", ":troop", ":i_slot"),
			(eq, ":wpn_item", -1),
			## CC
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1), #remove from pool
			(troop_set_inventory_slot, ":troop", ":i_slot", ":item"), #add to slot
			(troop_set_inventory_slot_modifier, ":troop", ":i_slot", ":imod"),
		(try_end),
	]),
	
	#######################
	# Search for the most expensive item of a specified type
	
	("scan_for_best_item_of_type",
		[
		(store_script_param, ":troop",1),
		(store_script_param, ":item_type",2),
		(store_script_param, ":troop_using", 3),
		
		(assign, ":best_slot", -1),
		(assign, ":best_value", -1),
		# iterate through the list of items
		(troop_get_inventory_capacity, ":inv_cap", ":troop"),
		(try_for_range, ":i_slot", 0, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
			#### Autoloot improved by rubik begin
			(try_begin),
			(item_slot_eq, ":item", slot_item_two_hand_one_hand, 1),
			(assign, ":this_item_type", itp_type_one_handed_wpn),
			(else_try),
			(item_get_type, ":this_item_type", ":item"),
			(try_end),
			#### Autoloot improved by rubik end
			(eq, ":this_item_type", ":item_type"), # it's one of the kind we're looking for
			(call_script, "script_troop_can_use_item", ":troop_using", ":item", ":imod"),
			(eq, reg0, 1), # can use
			(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
			(gt, reg0, ":best_value"), # best one we've seen yet
			(assign, ":best_slot", ":i_slot"),
			(assign, ":best_value", reg0),
		(try_end),
		
		# return the slot of the best one
		(assign, reg0, ":best_slot"),
	]),
	
	# script_exchange_equipments_between_two_sets
	# Input: none
	# Output: none
	("exchange_equipments_between_two_sets",
		[
		(store_script_param, ":troop_no", 1),
		
		(try_for_range, ":cur_slot", 0, 4),
			(store_sub, ":dest_slot", ":troop_no", companions_begin),
			(val_mul, ":dest_slot", 4),
			(val_add, ":dest_slot", 10),
			(val_add, ":dest_slot", ":cur_slot"),
			
			(str_store_troop_name, s20, ":troop_no"),
			(assign, reg20, ":dest_slot"),
			(display_message, "@{s20} --- dest slot {reg20}"),
			
			(troop_get_inventory_slot, ":dest_item", "trp_merchants_end", ":dest_slot"),
			(troop_get_inventory_slot_modifier, ":dest_imod", "trp_merchants_end", ":dest_slot"),
			(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_slot"),
			(troop_get_inventory_slot_modifier, ":cur_imod", ":troop_no", ":cur_slot"),
			(troop_set_inventory_slot, "trp_merchants_end", ":dest_slot", ":cur_item"),
			(troop_set_inventory_slot_modifier, "trp_merchants_end", ":dest_slot", ":cur_imod"),
			(troop_set_inventory_slot, ":troop_no", ":cur_slot", ":dest_item"),
			(troop_set_inventory_slot_modifier, ":troop_no", ":cur_slot", ":dest_imod"),
		(try_end),
	]),
	
	("transfer_inventory", [
		(store_script_param, ":source", 1),
		(store_script_param, ":dest", 2),
		(store_script_param, ":trans_book", 3),
		
		(store_free_inventory_capacity, ":space", ":dest"),
		(troop_sort_inventory, ":source"),
		
		(troop_get_inventory_capacity, ":inv_cap", ":source"),
		(try_for_range, ":i_slot", 10, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":source", ":i_slot"),
			(troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
			(gt, ":item", -1),
			
			(assign, ":continue", 1),
			(try_begin),
			(eq, ":trans_book", 0),
			(is_between, ":item", reference_books_begin, reference_books_end),
			(assign, ":continue", 0),
			(try_end),
			(eq, ":continue", 1),
			
			(gt, ":space", 0),
			(troop_add_item, ":dest", ":item", ":imod"),
			(val_sub, ":space", 1),
			(try_begin),
			(is_between, ":item", trade_goods_begin, trade_goods_end),
			(troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
			(troop_get_inventory_capacity, ":dest_inv_cap", ":dest"),
			(store_sub, ":dest_slot", ":dest_inv_cap", ":space"),
			(troop_inventory_slot_set_item_amount, ":dest", ":dest_slot", ":amount"),
			(try_end),
			(troop_set_inventory_slot, ":source", ":i_slot", -1),
		(try_end),
	]),
	
	("transfer_special_inventory", [
		(store_script_param, ":source", 1),
		(store_script_param, ":dest", 2),
		
		(store_free_inventory_capacity, ":space", ":dest"),
		(troop_sort_inventory, ":source"),
		
		(troop_get_inventory_capacity, ":inv_cap", ":source"),
		(try_for_range, ":i_slot", 10, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":source", ":i_slot"),
			(troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
			(gt, ":item", -1),
			
			(assign, ":continue", 0),
			(try_begin),
			(call_script, "script_get_item_value_with_imod", ":item", ":imod"),
			(assign, ":item_value", reg0),
			(val_div, ":item_value", 100),
			(ge, ":item_value", "$g_price_threshold_for_picking"),
			(assign, ":continue", 1),
			(else_try),
			(item_get_type, ":item_type", ":item"),
			(this_or_next|eq, ":item_type", itp_type_goods),
			(this_or_next|eq, ":item_type", itp_type_animal),
			(eq, ":item_type", itp_type_book),
			(assign, ":continue", 1),
			(try_end),
			(eq, ":continue", 1),
			
			(gt, ":space", 0),
			(troop_add_item, ":dest", ":item", ":imod"),
			(val_sub, ":space", 1),
			(try_begin),
			(is_between, ":item", trade_goods_begin, trade_goods_end),
			(troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
			(troop_get_inventory_capacity, ":dest_inv_cap", ":dest"),
			(store_sub, ":dest_slot", ":dest_inv_cap", ":space"),
			(troop_inventory_slot_set_item_amount, ":dest", ":dest_slot", ":amount"),
			(try_end),
			(troop_set_inventory_slot, ":source", ":i_slot", -1),
		(try_end),
	]),
	####################################################################################
	#
	# Autoloot Scripts end
	# ---------------------------------------------------
	####################################################################################
	
	("init_item_score", set_item_score()),
	
	("get_inventory_weight_of_whole_party",
		[
		(assign, ":total_weight", 0),
		
		(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
		(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
			(is_between, ":stack_troop", companions_begin, companions_end),
			(troop_get_inventory_capacity, ":inv_cap", ":stack_troop"),
			(try_for_range, ":cur_slot", 10, ":inv_cap"),#inventory slots
			(troop_get_inventory_slot, ":cur_item", ":stack_troop", ":cur_slot"),
			(ge, ":cur_item", 0),
			(item_get_slot, ":cur_item_weight", ":cur_item", slot_item_weight),
			(val_add, ":total_weight", ":cur_item_weight"),
			(try_end),
		(try_end),
		
		(val_div, ":total_weight", 100),
		(assign, reg0, ":total_weight"),
	]),
	
	("sort_food",
		[
		(store_script_param, ":troop_no", 1),
		(assign, ":max_amount", 0),
		
		(troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
		(try_for_range, ":i_slot", 10, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":troop_no", ":i_slot"),
			(troop_get_inventory_slot_modifier, ":imod", ":troop_no", ":i_slot"),
			(gt, ":item", -1),
			(is_between, ":item", food_begin, food_end),
			(try_for_range, ":i_slot_2", ":i_slot", ":inv_cap"),
			(neq, ":i_slot_2", ":i_slot"),
			(troop_get_inventory_slot, ":item_2", ":troop_no", ":i_slot_2"),
			(troop_get_inventory_slot_modifier, ":imod_2", ":troop_no", ":i_slot_2"),
			(gt, ":item_2", -1),
			(eq, ":item_2", ":item"),
			(eq, ":imod_2", ":imod"),
			(troop_inventory_slot_get_item_max_amount, ":max_amount", ":troop_no", ":i_slot"),
			(troop_inventory_slot_get_item_amount, ":item_amount", ":troop_no", ":i_slot"),
			(troop_inventory_slot_get_item_amount, ":item_amount_2", ":troop_no", ":i_slot_2"),
			(store_add, ":total_amount", ":item_amount", ":item_amount_2"),
			(store_sub, ":dest_amount_i_slot_2", ":total_amount", ":max_amount"),
			(try_begin),
				(gt, ":dest_amount_i_slot_2", 0),
				(troop_inventory_slot_set_item_amount, ":troop_no", ":i_slot", ":max_amount"),
				(troop_inventory_slot_set_item_amount, ":troop_no", ":i_slot_2", ":dest_amount_i_slot_2"),
				(assign, ":i_slot_2", 0), # stop
			(else_try),
				(troop_inventory_slot_set_item_amount, ":troop_no", ":i_slot", ":total_amount"),
				(troop_set_inventory_slot, ":troop_no", ":i_slot_2", -1), # delete it
			(try_end),
			(try_end),
		(try_end),
	]),
	
	("auto_sell", [
		(store_script_param_1, ":customer"),
		(store_script_param_2, ":merchant"),
		
		(store_free_inventory_capacity, ":space", ":merchant"),
		(troop_sort_inventory, ":customer"),
		
		(troop_get_inventory_capacity, ":inv_cap", ":customer"),
		(try_for_range_backwards, ":i_slot", 10, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":customer", ":i_slot"),
			(troop_get_inventory_slot_modifier, ":imod", ":customer", ":i_slot"),
			(gt, ":item", -1),
			(item_get_type, ":type", ":item"),
			(item_slot_eq, ":type", slot_item_type_not_for_sell, 0),
			
			(call_script, "script_get_item_value_with_imod", ":item", ":imod"),
			(assign, ":score", reg0),
			(val_div, ":score", 100),
			(call_script, "script_game_get_item_sell_price_factor", ":item"),
			(assign, ":sell_price_factor", reg0),
			(val_mul, ":score", ":sell_price_factor"),
			(val_div, ":score", 100),
			(val_max, ":score",1),
			
			(le, ":score", "$g_auto_sell_price_limit"),
			(store_troop_gold, ":m_gold", ":merchant"),
			(le, ":score", ":m_gold"),
			(gt, ":space", 0),
			
			(troop_add_item, ":merchant", ":item", ":imod"),
			(val_sub, ":space", 1),
			(troop_set_inventory_slot, ":customer", ":i_slot", -1),
			(troop_remove_gold, ":merchant", ":score"),
			(troop_add_gold, ":customer", ":score"),
		(try_end),
	]),
	
	("start_town_conversation",
		[
		(store_script_param, ":troop_slot_no", 1),
		(store_script_param, ":entry_no", 2),
		
		(try_begin),
			(eq, ":troop_slot_no", slot_town_merchant),
			(assign, ":scene_slot_no", slot_town_store),
		(else_try),
			(eq, ":troop_slot_no", slot_town_tavernkeeper),
			(assign, ":scene_slot_no", slot_town_tavern),
		(else_try),
			(assign, ":scene_slot_no", slot_town_center),
			(assign, ":scene_slot_no", slot_town_tavern),
		(try_end),
		
		(party_get_slot, ":conversation_scene", "$current_town", ":scene_slot_no"),
		(modify_visitors_at_site, ":conversation_scene"),
		(reset_visitors),
		(set_visitor, 0, "trp_player"),
		(party_get_slot, ":conversation_troop", "$current_town", ":troop_slot_no"),
		(set_visitor, ":entry_no", ":conversation_troop"),
		(set_jump_mission,"mt_conversation_encounter"),
		(jump_to_scene, ":conversation_scene"),
		(change_screen_map_conversation, ":conversation_troop"),
	]),
	
	("get_book_read_slot",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":item_no", 2),
		
		(store_sub, ":num_companions", companions_end, companions_begin),
		(store_sub, ":item_offset", ":item_no", readable_books_begin),
		(store_sub, ":troop_offset", ":troop_no", companions_begin),
		
		(store_mul, ":slot_no", ":item_offset", ":num_companions"),
		(val_add, ":slot_no", ":troop_offset"),
		(assign, reg0, ":slot_no"),
	]),
	
	("get_troop_max_hp",
		[
		(store_script_param_1, ":troop"),
		
		(store_skill_level, ":skill", skl_ironflesh, ":troop"),
		(store_attribute_level, ":attrib", ":troop", ca_strength),
		(val_mul, ":skill", 2),
		(val_add, ":skill", ":attrib"),
		(val_add, ":skill", 35),
		(assign, reg0, ":skill"),
	]),
	("get_current_item_for_autoloot",
		[
		(store_script_param_1, ":wpn_set"),
		(store_script_param_2, ":slot_no"),
		
		(try_begin),
			(eq, ":wpn_set", 0),
			(assign, ":dest_slot", ":slot_no"),
			(troop_get_inventory_slot, ":item", "$temp", ":dest_slot"),
		(else_try),
			(store_sub, ":dest_slot", "$temp", companions_begin),
			(val_mul, ":dest_slot", 4),
			(val_add, ":dest_slot", 10),
			(val_add, ":dest_slot", ":slot_no"),
			(troop_get_inventory_slot, ":item", "trp_merchants_end", ":dest_slot"),
		(try_end),
		(try_begin),
			(ge, ":item", 0),
			(str_store_item_name, s10, ":item"),
		(else_try),
			(str_store_string, s10, "str_none"),
		(try_end),
	]),
	("prsnt_lines",
		[
		(store_script_param, ":size_x", 1),
		(store_script_param, ":size_y", 2),
		(store_script_param, ":pos_x", 3),
		(store_script_param, ":pos_y", 4),
		
		(create_mesh_overlay, reg1, "mesh_white_plane"),
		(val_mul, ":size_x", 50),
		(val_mul, ":size_y", 50),
		(position_set_x, pos1, ":size_x"),
		(position_set_y, pos1, ":size_y"),
		(overlay_set_size, reg1, pos1),
		(position_set_x, pos1, ":pos_x"),
		(position_set_y, pos1, ":pos_y"),
		(overlay_set_position, reg1, pos1),
		(overlay_set_color, reg1, 0x000000),
	]),
	
	("copy_inventory",
		[
		(store_script_param_1, ":source"),
		(store_script_param_2, ":target"),
		
		(troop_clear_inventory, ":target"),
		(troop_get_inventory_capacity, ":inv_cap", ":source"),
		(try_for_range, ":i_slot", 0, ":inv_cap"),
			(troop_get_inventory_slot, ":item", ":source", ":i_slot"),
			(troop_set_inventory_slot, ":target", ":i_slot", ":item"),
			(troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
			(troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
			(troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
			(gt, ":amount", 0),
			(troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
		(try_end),
	]),
	
	("sell_all_prisoners",
		[
		(assign, ":total_income", 0),
		(party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
		(try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
			(party_prisoner_stack_get_troop_id, ":troop_no", "p_main_party", ":i_stack"),
			(neg|troop_is_hero, ":troop_no"),
			(party_prisoner_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
			(call_script, "script_game_get_prisoner_price", ":troop_no"),
			(assign, ":sell_price", reg0),
			(store_mul, ":stack_total_price", ":sell_price", ":stack_size"),
			(val_add, ":total_income", ":stack_total_price"),
			(party_remove_prisoners, "p_main_party", ":troop_no", ":stack_size"),
		(try_end),
		(troop_add_gold, "trp_player", ":total_income"),
	]),
	

	
	("get_dest_color_from_rgb",
		[
		(store_script_param, ":red", 1),
		(store_script_param, ":green", 2),
		(store_script_param, ":blue", 3),
		
		(assign, ":cur_color", 0xFF000000),
		(val_mul, ":green", 0x100),
		(val_mul, ":red", 0x10000),
		(val_add, ":cur_color", ":blue"),
		(val_add, ":cur_color", ":green"),
		(val_add, ":cur_color", ":red"),
		(assign, reg0, ":cur_color"),
	]),
	
	("convert_rgb_code_to_html_code",
		[
		(store_script_param, ":red", 1),
		(store_script_param, ":green", 2),
		(store_script_param, ":blue", 3),
		
		(str_store_string, s0, "@#"),
			
			(store_div, ":r_1", ":red", 0x10),
			(store_add, ":dest_string", "str_key_0", ":r_1"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_mod, ":r_2", ":red", 0x10),
			(store_add, ":dest_string", "str_key_0", ":r_2"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_div, ":g_1", ":green", 0x10),
			(store_add, ":dest_string", "str_key_0", ":g_1"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_mod, ":g_2", ":green", 0x10),
			(store_add, ":dest_string", "str_key_0", ":g_2"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_div, ":b_1", ":blue", 0x10),
			(store_add, ":dest_string", "str_key_0", ":b_1"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_mod, ":b_2", ":blue", 0x10),
			(store_add, ":dest_string", "str_key_0", ":b_2"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
		]),
									
		("convert_slot_no_to_color",
		[
			(store_script_param, ":cur_color", 1),
			
			(store_mod, ":blue", ":cur_color", 6),
			(val_div, ":cur_color", 6),
			(store_mod, ":green", ":cur_color", 6),
			(val_div, ":cur_color", 6),
			(store_mod, ":red", ":cur_color", 6),
			(val_mul, ":blue", 0x33),
			(val_mul, ":green", 0x33),
			(val_mul, ":red", 0x33),
			(assign, ":dest_color", 0xFF000000),
			(val_mul, ":green", 0x100),
			(val_mul, ":red", 0x10000),
			(val_add, ":dest_color", ":blue"),
			(val_add, ":dest_color", ":green"),
			(val_add, ":dest_color", ":red"),
			(assign, reg0, ":dest_color"),
		]),
		
		
		("raf_send_messenger_to_companion",
		[
			(store_script_param, ":target_party", 1),
			(store_script_param, ":orders_object", 2),
			
			(set_spawn_radius, 1),
			(spawn_around_party, "$current_town", "pt_messenger_party"),
			(assign,":spawned_party",reg0),
			(party_add_members, ":spawned_party", "trp_raf_messenger", 1),
			(try_begin),
			(gt, "$players_kingdom", 0),
			(party_set_faction, ":spawned_party", "$players_kingdom"),
			(party_set_slot, ":spawned_party", slot_center_original_faction, "$players_kingdom"),
			(else_try),
			(party_set_faction, ":spawned_party", "fac_player_faction"),
			(party_set_slot, ":spawned_party", slot_center_original_faction, "fac_player_faction"),
			(try_end),
			
			(party_set_slot, ":spawned_party", slot_party_type, raf_spt_messenger),
			(party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
			
			(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
			(party_set_ai_object, ":spawned_party", ":target_party"),
			(party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
			(party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
			(troop_set_slot, ":orders_object", slot_troop_traveling, 1),
			
		]
		),
		
		("raf_troop_get_religion",
		[
			(store_script_param, ":troop", 1),
			
			(assign, reg0, -1),
			(store_troop_faction, ":faction", ":troop"),
			(try_begin),
			(eq, ":faction", "fac_kingdom_1"),
			(assign, reg0, religion_catholic),
			(else_try),
			(eq, ":faction", "fac_kingdom_2"),
			(assign, reg0, religion_pagan_balt),
			(else_try),
			(eq, ":faction", "fac_kingdom_20"),
			(assign, reg0, religion_muslim),
			(else_try),
			(eq, ":faction", "fac_kingdom_3"),
			(assign, reg0, religion_pagan_mongol),
			(else_try),
			(eq, ":faction", "fac_kingdom_8"),
			(assign, reg0, religion_orthodox),
			(try_end),
		]
		),
		
		("prsnt_upgrade_tree_switch",
		[
			(store_trigger_param_1, ":object"),
			(store_trigger_param_2, ":value"),
			
			(try_begin),
			# (eq, ":object", "$g_presentation_obj_1"),
			# (store_sub, "$temp_2", 9, ":value"),
			# (store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_10"),
			# (start_presentation, ":cur_presentation"),
			# (else_try),
			(eq, ":object", "$g_presentation_obj_5"),
			(presentation_set_duration, 0),
			(try_end),
		]),
		
		("prsnt_upgrade_tree_ready",
		[
			## next presentation
			(assign, "$g_presentation_next_presentation", -1),
			
			# (create_combo_button_overlay, "$g_presentation_obj_1"),
			# (position_set_x, pos1, 500),
			# (position_set_y, pos1, 680),
			# (overlay_set_position, "$g_presentation_obj_1", pos1),
			# # factions
			# (try_for_range_backwards, ":i_upgrade_tree", 0, 10),
			# (store_add, ":faction_no", ":i_upgrade_tree", "fac_kingdom_1"),
			# ## faction name
			# (try_begin),
			# (eq, ":faction_no", "fac_kingdoms_end"),
			# (str_store_string, s0, "@Mercenaries"),
			# (else_try),
			# (eq, ":faction_no", "fac_robber_knights"),
			# (str_store_string, s0, "@Outlaws"),
			# (else_try),
			# (eq, ":faction_no", "fac_khergits"),
			# (str_store_string, s0, "@Personal Guards"),
			# (else_try),
			# (eq, ":faction_no", "fac_manhunters"),
			# (str_store_string, s0, "@Others"),
			# (else_try),
			# (str_store_faction_name, s0, ":faction_no"),
			# (try_end),
			# (overlay_add_item, "$g_presentation_obj_1", s0),
			# (try_end),
			# (store_sub, ":presentation_obj_val", 9, "$temp_2"),
			# (overlay_set_val, "$g_presentation_obj_1", ":presentation_obj_val"),
			
			## back
			(create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
			(position_set_x, pos1, 900),
			(position_set_y, pos1, 25),
			(overlay_set_position, "$g_presentation_obj_5", pos1),
		]),
		
		("prsnt_upgrade_tree_troop_and_name",
		[
			(store_script_param, ":slot_no", 1),
			(store_script_param, ":troop_no", 2),
			(store_script_param, ":pos_x", 3),
			(store_script_param, ":pos_y", 4),
			
			
			(str_store_troop_name, s1, ":troop_no"),
			(create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_vertical_align_center),
			(position_set_x, pos1, 800),
			(position_set_y, pos1, 800),
			(overlay_set_size, reg1, pos1),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			
			(val_sub, ":pos_x", 70),
			(val_add, ":pos_y", 5),
			(store_mul, ":cur_troop", ":troop_no", 2), #with weapons
			(create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
			#(position_set_x, pos1, 600),
			#(position_set_y, pos1, 600),
			(position_set_x, pos1, 450),
			(position_set_y, pos1, 450),
			
			(overlay_set_size, reg1, pos1),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
			(troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
			(troop_set_slot, "trp_temp_array_b", ":slot_no", ":troop_no"),
			
		]),
		
		("prsnt_upgrade_tree_troop_cost",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			
			(call_script, "script_game_get_upgrade_cost", ":troop_no"),
			
			(create_text_overlay, reg1, "@{reg0}", tf_center_justify|tf_vertical_align_center),
			(position_set_x, pos1, 800),
			(position_set_y, pos1, 800),
			(overlay_set_size, reg1, pos1),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg1, pos1),
		]),
		
		("raf_religion_to_s11",
		[
			(store_script_param, ":faction_no", 1),
			(faction_get_slot, ":religion", ":faction_no", slot_faction_religion),
			(try_begin),
			(eq, ":religion", religion_catholic),
			(str_store_string, s11, "str_religion_catholic"),
			(else_try),
			(eq, ":religion", religion_pagan_balt),
			(str_store_string, s11, "str_religion_pagan_balt"),
			(else_try),
			(eq, ":religion", religion_pagan_mongol),
			(str_store_string, s11, "str_religion_pagan_mongol"),
			(else_try),
			(eq, ":religion", religion_muslim),
			(str_store_string, s11, "str_religion_muslim"),
			(else_try),
			(eq, ":religion", religion_orthodox),
			(str_store_string, s11, "str_religion_orthodox"),
			(try_end),
		]
		),

# #Formations Scripts	  
	# script_division_reset_places by motomataru
	# Input: none
	# Output: none
	# Resets globals for placing divisions around player for script_battlegroup_place_around_leader
	("division_reset_places", [
	(assign, "$next_cavalry_place", formation_minimum_spacing_horse_width),	#first spot RIGHT of the player
	(assign, "$next_archer_place", 1000),	#first spot 10m FRONT of the player
	(assign, "$next_infantry_place", -1 * formation_minimum_spacing_horse_width),	#first spot LEFT of the player
	]),
	 
	# script_battlegroup_place_around_leader by motomataru
	# Input: team, division
	# Output: pos61 division position
	("battlegroup_place_around_leader", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(team_get_leader, ":fleader", ":fteam"),
	(try_begin),
		(gt, ":fleader", -1),	#any team members left?
		
		(agent_get_position, pos1, ":fleader"),
		(try_begin),
			(eq, "$autorotate_at_player", 1),
			(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
			(neq, reg0, 0),	#more than 0 enemies still alive?
			(call_script, "script_point_y_toward_position", pos1, pos60),
		(try_end),

		(store_add, ":slot", slot_team_d0_type, ":fdivision"),
		(team_get_slot, ":sd_type", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(team_get_slot, ":fformation", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
# (assign, reg1, ":sd_type"),
# (assign, reg0, ":num_troops"),
# (assign, reg2, ":fteam"),
# (assign, reg3, ":fdivision"),
# (position_get_x, reg4, pos1),
# (position_get_y, reg5, pos1),
# (assign, reg6, ":fformation"),
# (display_message, "@Team {reg2} Division {reg3} type {reg1} numbers {reg0} leader at {reg4},{reg5} formation {reg6}"),
		(try_begin),
			(this_or_next|eq, ":sd_type", sdt_cavalry),
			(eq, ":sd_type", sdt_harcher),
			(position_move_x, pos1, "$next_cavalry_place", 0),
			(try_begin),	#handle Native's way of doing things
				(eq, ":fformation", formation_none),
				(try_begin),
					(ge, ":formation_extra_spacing", 0),
					(store_mul, ":troop_space", ":formation_extra_spacing", 133),
					(val_add, ":troop_space", 150),
				(else_try),	#handle Native multi-ranks
					(assign, ":troop_space", 200),
					(val_mul, ":formation_extra_spacing", -1),
					(val_add, ":formation_extra_spacing", 1),
					(val_div, ":num_troops", ":formation_extra_spacing"),
				(try_end),
				(store_mul, ":formation_width", ":num_troops", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(position_move_x, pos1, reg0, 0),	#cavalry set up RIGHT of leader
# (display_message, "@Cavalry move {reg0}"),
				(copy_position, pos61, pos1),
			(else_try),
				(store_mul, ":troop_space", ":formation_extra_spacing", 50),
				(val_add, ":troop_space", formation_minimum_spacing_horse_width),
				(convert_to_fixed_point, ":num_troops"),
				(store_sqrt, ":formation_width", ":num_troops"),
				(val_mul, ":formation_width", ":troop_space"),
				(convert_from_fixed_point, ":formation_width"),
				(val_sub, ":formation_width", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(position_move_x, pos1, reg0, 0),	#cavalry set up RIGHT of leader
# (display_message, "@Cavalry move {reg0}"),
				(copy_position, pos61, pos1),
				(call_script, "script_form_cavalry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing"),
			(try_end),
			(val_add, "$next_cavalry_place", ":formation_width"),
			(val_add, "$next_cavalry_place", formation_minimum_spacing_horse_width),

		(else_try),
			(eq, ":sd_type", sdt_archer),
			(position_move_y, pos1, "$next_archer_place"),	#archers set up FRONT of leader
			(copy_position, pos61, pos1),
			(try_begin),
				(neq, ":fformation", formation_none),
				(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
				(val_mul, reg0, -1),
				(position_move_x, pos1, reg0, 0),
				(call_script, "script_form_archers", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			(try_end),
			(val_add, "$next_archer_place", 500),	#next archers 5m FRONT of these
			
		(else_try),
			(eq, ":sd_type", sdt_skirmisher),
			(position_move_y, pos1, "$next_archer_place"),	#skirmishers set up FRONT of leader
			(copy_position, pos61, pos1),
			(try_begin),
				(neq, ":fformation", formation_none),
				(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
				(position_move_x, pos1, reg0, 0),
				(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
			(try_end),
			(val_add, "$next_archer_place", 500),	#next archers 5m FRONT of these
			
		(else_try),
			(position_move_x, pos1, "$next_infantry_place", 0),
			(copy_position, pos61, pos1),
			(try_begin),	#handle Native's way of doing things
				(eq, ":fformation", formation_none),
				(try_begin),
					(ge, ":formation_extra_spacing", 0),
					(store_mul, ":troop_space", ":formation_extra_spacing", 75),	#Native minimum spacing not consistent but less than this
					(val_add, ":troop_space", 100),
				(else_try),	#handle Native multi-ranks
					(assign, ":troop_space", 150),
					(val_mul, ":formation_extra_spacing", -1),
					(val_add, ":formation_extra_spacing", 1),
					(val_div, ":num_troops", ":formation_extra_spacing"),
				(try_end),
				(store_mul, ":formation_width", ":num_troops", ":troop_space"),
				(store_div, reg0, ":formation_width", 2),
				(val_mul, reg0, -1),	#infantry set up LEFT of leader
# (display_message, "@Infantry unformed move {reg0}"),
				(position_move_x, pos61, reg0, 0),
			(else_try),
				(call_script, "script_form_infantry", ":fteam", ":fdivision", ":fleader", ":formation_extra_spacing", ":fformation"),
				(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
				(store_mul, ":formation_width", 2, reg0),
				(store_mul, ":troop_space", ":formation_extra_spacing", 50),
				(val_add, ":troop_space", formation_minimum_spacing),
				(val_add, ":formation_width", ":troop_space"),
				(val_mul, reg0, -1),	#infantry set up LEFT of leader
# (display_message, "@Infantry formation move {reg0}"),
				(position_move_x, pos61, reg0, 0),
			(try_end),
			(val_sub, "$next_infantry_place", ":formation_width"),	#next infantry 1m LEFT of these
			(val_sub, "$next_infantry_place", 100),
# (assign, reg0, "$next_infantry_place"),
# (display_message, "@Next infantry {reg0}"),
		(try_end),
		
		(store_add, ":slot", slot_team_d0_move_order, ":fdivision"),
		(team_set_slot, ":fteam", ":slot", mordr_hold),
		(set_show_messages, 0),
		(team_get_movement_order, reg0, ":fteam", ":fdivision"),
		(try_begin),
			(neq, reg0, mordr_hold),
			(team_give_order, ":fteam", ":fdivision", mordr_hold),
		(try_end),
		# (team_set_order_position, ":fteam", ":fdivision", pos61),
		(call_script, "script_set_formation_position", ":fteam", ":fdivision", pos61),
		(set_show_messages, 1),
	(try_end),
	]),
	
	# script_form_cavalry by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing
	# Output: none
	# Form in wedge, (now not) excluding horse archers
	# Creates formation starting at pos1
	("form_cavalry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":x_distance", formation_minimum_spacing_horse_width, ":extra_space"),
	(store_add, ":y_distance", formation_minimum_spacing_horse_length, ":extra_space"),
	(assign, ":max_level", 0),
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
		(agent_get_troop_id, ":troop_id", ":agent"),
		(store_character_level, ":troop_level", ":troop_id"),
		(gt, ":troop_level", ":max_level"),
		(assign, ":max_level", ":troop_level"),
	(end_try),
	(assign, ":column", 1),
	(assign, ":rank_dimension", 1),
	(store_mul, ":neg_y_distance", ":y_distance", -1),
	(store_mul, ":neg_x_distance", ":x_distance", -1),
	(store_div, ":wedge_adj", ":x_distance", 2),
	(store_div, ":neg_wedge_adj", ":neg_x_distance", 2),
	(val_add, ":max_level", 1),
	(assign, ":form_left", 1),
	(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
		(try_for_agents, ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(eq, ":troop_level", ":rank_level"),				
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_x_distance", 0),
			(else_try),
				(position_move_x, pos1, ":x_distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":rank_dimension"),
			(position_move_y, pos1, ":neg_y_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_wedge_adj", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":wedge_adj", 0),
			(try_end),			
			(assign, ":column", 1),
			(val_add, ":rank_dimension", 1),
		(end_try),
	(end_try),
	]),
		 
	# script_form_archers by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing, formation
	# Output: none
	# Form in line, staggered if formation = formation_ranks
	# Creates formation starting at pos1
	("form_archers", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":archers_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops
	(assign, ":total_move_y", 0),	#staggering variable	
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
		(agent_set_scripted_destination, ":agent", pos1, 1),
		(position_move_x, pos1, ":distance", 0),
		(try_begin),
			(eq, ":archers_formation", formation_ranks),
			(val_add, ":total_move_y", 75),
			(try_begin),
				(le, ":total_move_y", 150),
				(position_move_y, pos1, 75, 0),
			(else_try),
				(position_move_y, pos1, -150, 0),
				(assign, ":total_move_y", 0),
			(try_end),
		(try_end),
	(try_end),
	]),
		 
	# script_form_infantry by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing, formation
	# Output: none
	# If input "formation" is formation_default, will select a formation based on faction
	# Creates formation starting at pos1
	("form_infantry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":infantry_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops	
	(store_mul, ":neg_distance", ":distance", -1),
	(store_add, ":slot", slot_team_d0_size, ":fdivision"),
	(team_get_slot, ":num_troops", ":fteam", ":slot"),
	(try_begin),
		(eq, ":infantry_formation", formation_default),
		(call_script, "script_get_default_formation", ":fteam"),
		(assign, ":infantry_formation", reg0),
	(try_end),
	(team_get_weapon_usage_order, ":weapon_order", ":fteam", grc_infantry),
	(assign, ":form_left", 1),
	(assign, ":column", 1),
	(assign, ":rank", 1),

	(try_begin),
		(eq, ":infantry_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, ":square_dimension", ":num_troops"),
		(convert_from_fixed_point, ":square_dimension"),
		(val_add, ":square_dimension", 1),

		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),
				(eq, formation_reequip, 1),
				(eq, ":weapon_order", wordr_use_any_weapon),
				(try_begin),
					(this_or_next|eq, ":rank", 1),
					(this_or_next|ge, ":rank", ":square_dimension"),
					(this_or_next|eq, ":column", 1),
					(ge, ":column", ":square_dimension"),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
				(else_try),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(position_move_x, pos1, ":distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":square_dimension"),
			(position_move_y, pos1, ":neg_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":distance", 0),
			(try_end),			
			(assign, ":column", 1),		
			(val_add, ":rank", 1),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_wedge),
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),

		(assign, ":rank_dimension", 1),
		(store_div, ":wedge_adj", ":distance", 2),
		(store_div, ":neg_wedge_adj", ":neg_distance", 2),
		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(try_begin),
						(this_or_next|eq, ":column", 1),
						(ge, ":column", ":rank_dimension"),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
					(else_try),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				(gt, ":column", ":rank_dimension"),
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_wedge_adj", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":wedge_adj", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank_dimension", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_ranks),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),		
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),


		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(try_begin),
						(eq, ":rank", 1),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
					(else_try),
						(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
					(try_end),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),

				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_shield),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),
		(assign, ":first_second_rank_agent", -1),
		(assign, ":min_len_non_shielded", -1),
		(try_for_range, ":weap_group", 0, 3),
			(store_mul, ":min_len", ":weap_group", Third_Max_Weapon_Length),
			(store_add, ":max_len", ":min_len", Third_Max_Weapon_Length),
			(try_begin),
				(gt, ":min_len_non_shielded", -1),	#looped through agents at least once since rank 2
				(assign, ":min_len_non_shielded", ":min_len"),
			(try_end),
			(try_for_agents, ":agent"),
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fdivision", ":fleader", ":agent"),
				(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
				(try_begin),
					(gt, ":agent_weapon", itm_no_item),
					(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
				(else_try),
					(assign, ":weapon_length", 0),
				(try_end),
				(try_begin),
					(gt, ":rank", 1),
					(try_begin),
						(eq, ":first_second_rank_agent", ":agent"),	#looped through agents at least once since rank 2
						(assign, ":min_len_non_shielded", ":min_len"),
					(else_try),
						(eq, ":first_second_rank_agent", -1),
						(assign, ":first_second_rank_agent", ":agent"),
					(try_end),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(ge, ":weapon_length", ":min_len"),	#avoid reequipping agents that are already in formation
					(eq, ":min_len_non_shielded", -1),	#haven't looped through agents at least once since rank 2
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),	#longest weapon, including two-handed
					(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
					(try_begin),
						(gt, ":agent_weapon", itm_no_item),
						(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
					(else_try),
						(assign, ":weapon_length", 0),
					(try_end),
				(try_end),
				
				(assign, ":form_up", 0),
				(agent_get_wielded_item, ":agent_shield", ":agent", 1),
				(try_begin),
					(gt, ":agent_shield", itm_no_item),
					(item_get_type, reg0, ":agent_shield"),
					(eq, reg0, itp_type_shield),
					(try_begin),
						(is_between, ":weapon_length", ":min_len", ":max_len"),
						(assign, ":form_up", 1),
					(try_end),
				(else_try),
					(gt, ":rank", 1),
					(is_between, ":weapon_length", ":min_len_non_shielded", ":max_len"),
					(assign, ":form_up", 1),
				(try_end),

				(eq, ":form_up", 1),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(eq, formation_reequip, 1),
					(eq, ":weapon_order", wordr_use_any_weapon),
					(eq, ":rank", 1),
					(call_script, "script_equip_best_melee_weapon", ":agent", 1, 0),	#best weapon, force shield
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				
				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(try_end),
		(try_end),
	(try_end),
	]),
		 
	# script_get_default_formation by motomataru
	# Input: team id
	# Output: reg0 default formation
	("get_default_formation", [
	(store_script_param, ":fteam", 1),
	(team_get_slot, ":ffaction", ":fteam", slot_team_faction),
	(try_begin),
			(this_or_next|eq, ":ffaction", fac_player_supporters_faction),
		(eq, ":ffaction", fac_player_faction),
		(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		(neq, "$players_kingdom", fac_player_supporters_faction),
		(assign, ":ffaction", "$players_kingdom"),
	(try_end),
	(faction_get_slot, ":culture", ":ffaction", slot_faction_culture),
	(try_begin), #wall
		(this_or_next|eq, ":culture", "fac_culture_finnish"),
		(this_or_next|eq, ":culture", "fac_culture_mazovian"),
		(this_or_next|eq, ":culture", "fac_culture_welsh"),
		(this_or_next|eq, ":culture", "fac_culture_rus"),
		(this_or_next|eq, ":culture", "fac_culture_nordic"),
		(this_or_next|eq, ":culture", "fac_culture_baltic"),
		(this_or_next|eq, ":culture", "fac_culture_gaelic"),
		(eq, ":culture", "fac_culture_scotish"),
		(assign, reg0, formation_shield),
	(else_try),
		(this_or_next|eq, ":ffaction", "fac_player_supporters_faction"),
		(this_or_next|is_between, ":ffaction", kingdoms_begin, kingdoms_end),
		(is_between, ":culture", fac_culture_finnish, fac_culture_mongol +1),
		(assign, reg0, formation_ranks),
	(try_end),
	
	#assign default formation
	
	#(call_script, "script_raf_aor_faction_to_region", ":ffaction"),
	# (str_store_faction_name, s21, ":ffaction"),
	# (display_message, "@Faction: {s21}"),
	# (try_begin),
		# (eq, reg0, region_baltic),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_nordic),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_eastern),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_balkan),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_mongol),
		# (assign, reg0, formation_none),
	# (else_try),
		# (eq, reg0, region_european),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_latin),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_teutonic),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_crusaders),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_byzantine),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_andalusian),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, reg0, region_north_african),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_anatolian),
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (eq, reg0, region_mamluk),
		# (assign, reg0, formation_ranks),
	# (else_try), #TOM
		# (eq, reg0, region_scot),
		# (assign, reg0, formation_shield),
	# (else_try),
		# (eq, ":ffaction", fac_player_faction),	#independent player
		# (assign, reg0, formation_ranks),
	# (else_try),
		# (assign, reg0, formation_none),	#riffraff don't use formations
	# (try_end),
	]),

	# script_equip_best_melee_weapon by motomataru
	# Input: agent id, flag to force shield, flag to force for length ALONE
	# Output: none
	("equip_best_melee_weapon", [
	(store_script_param, ":agent", 1),
	(store_script_param, ":force_shield", 2),
	(store_script_param, ":force_length", 3),

	#priority items
	(assign, ":shield", itm_no_item),
	(assign, ":weapon", itm_no_item),
	(try_for_range, ":item_slot", ek_item_0, ek_head),
		(agent_get_item_slot, ":item", ":agent", ":item_slot"),
		(gt, ":item", itm_no_item),
		(item_get_type, ":weapon_type", ":item"),
		(try_begin),
			(eq, ":weapon_type", itp_type_shield),
			(assign, ":shield", ":item"),
		(else_try),
			(eq, ":weapon_type", itp_type_thrown),
			# (agent_get_ammo, ":ammo", ":agent", 0),	#assume infantry would have no other kind of ranged weapon
			# (gt, ":ammo", 0),
			(assign, ":weapon", ":item"),	#use thrown weapons first
		(try_end),
	(try_end),

	#select weapon
	(try_begin),
		(eq, ":weapon", itm_no_item),
		(assign, ":cur_score", 0),
		(try_for_range, ":item_slot", ek_item_0, ek_head),
			(agent_get_item_slot, ":item", ":agent", ":item_slot"),
			(gt, ":item", itm_no_item),
			(item_get_type, ":weapon_type", ":item"),
			(neq, ":weapon_type", itp_type_shield),

			(item_get_slot, reg0, ":item", slot_item_needs_two_hands),
			(this_or_next|eq, reg0, 0),
			(this_or_next|eq, ":force_shield", 0),
			(eq, ":shield", itm_no_item),
			
			(try_begin),
				(neq, ":force_length", 0),
				(item_get_slot, ":item_length", ":item", slot_item_length),
				(try_begin),
					(lt, ":cur_score", ":item_length"),
					(assign, ":cur_score", ":item_length"),
					(assign, ":weapon", ":item"),
				(try_end),
			(else_try),
				(assign, ":imod", imodbit_plain),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(try_begin),    #only heroes have item modifications
					(troop_is_hero, ":troop_id"),
					(try_for_range, ":troop_item_slot",  ek_item_0, ek_head),    # heroes have only 4 possible weapons (equipped)
						(troop_get_inventory_slot, reg0, ":troop_id", ":troop_item_slot"),  #Find Item Slot with same item ID as Equipped Weapon
						(eq, reg0, ":item"),
						(troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":troop_item_slot"),
					(try_end),
				(try_end), 

				(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
				(lt, ":cur_score", reg0),
				(assign, ":cur_score", reg0),
				(assign, ":weapon", ":item"),
			(try_end),
		(try_end),
	(try_end),

	#equip selected items if needed
	(agent_get_wielded_item, reg0, ":agent", 0),
	(try_begin),
		(neq, reg0, ":weapon"),
		(try_begin),
			(gt, ":shield", itm_no_item),
			(agent_get_wielded_item, reg0, ":agent", 1),
			(neq, reg0, ":shield"),	#reequipping secondary will UNequip (from experience)
			(agent_set_wielded_item, ":agent", ":shield"),
		(try_end),
		(gt, ":weapon", itm_no_item),
		(agent_set_wielded_item, ":agent", ":weapon"),
	(try_end),
	]),

	# script_formation_current_position by motomataru
	# Input: destination position (not pos0), team, division
	# Output: in destination position
	("formation_current_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fdivision", 3),
	(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
	(team_get_slot, ":first_agent_in_formation", ":fteam", ":slot"),
	(call_script, "script_get_formation_position", pos0, ":fteam", ":fdivision"),
	(try_begin),
		(eq, ":first_agent_in_formation", -1),
		(copy_position, ":fposition", pos0),
	(else_try),
		(agent_get_position, ":fposition", ":first_agent_in_formation"),
		(position_copy_rotation, ":fposition", pos0),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
		(try_begin),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(team_slot_eq, ":fteam", ":slot", sdt_archer),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(team_get_slot, ":fformation", ":fteam", ":slot"),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, ":fposition", reg0, 0),
	(try_end),
	]),

	# script_get_centering_amount by motomataru
	# Input: formation type, number of troops, extra spacing
	#        Use formation type formation_default to use script for archer line
	# Output: reg0 number of centimeters to adjust x-position to center formation
	("get_centering_amount", [
	(store_script_param, ":troop_formation", 1),
	(store_script_param, ":num_troops", 2),
	(store_script_param, ":extra_spacing", 3),
	(store_mul, ":troop_space", ":extra_spacing", 50),
	(val_add, ":troop_space", formation_minimum_spacing),
	(assign, reg0, 0),
	(try_begin),
		(eq, ":troop_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, reg0, ":num_troops"),
		(val_mul, reg0, ":troop_space"),
		(convert_from_fixed_point, reg0),
		(val_sub, reg0, ":troop_space"),
	(else_try),
		(this_or_next|eq, ":troop_formation", formation_ranks),
		(eq, ":troop_formation", formation_shield),
		(store_div, reg0, ":num_troops", 3),
		(try_begin),
			(store_mod, reg1, ":num_troops", 3),
			(eq, reg1, 0),
			(val_sub, reg0, 1),
		(try_end),
		(val_mul, reg0, ":troop_space"),
	(else_try),
		(eq, ":troop_formation", formation_default),	#assume these are archers in a line
		(store_mul, reg0, ":num_troops", ":troop_space"),
	(try_end),
	(val_div, reg0, 2),
	]),

	# script_formation_end
	# Input: team, division
	# Output: none
	("formation_end", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(try_begin),
		(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
		(neg|team_slot_eq, ":fteam", ":slot", formation_none),
		(team_set_slot, ":fteam", ":slot", formation_none),
		(team_get_leader, ":leader", ":fteam"),
		
		(try_for_agents, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_is_human, ":agent"),
			(agent_get_team, ":team", ":agent"),
			(eq, ":team", ":fteam"),
			(neq, ":leader", ":agent"),
			(agent_get_division, ":bgroup", ":agent"),
			(eq, ":bgroup", ":fdivision"),
			(agent_clear_scripted_mode, ":agent"),
		(try_end),
		
		(try_begin),
			(eq, ":fteam", "$fplayer_team_no"),
			(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			#adjust for differences between the two systems of spreading out
			(set_show_messages, 0),
			(try_begin),
				(gt, ":div_spacing", 3),
				(assign, ":div_spacing", 2),	#Native maximum spread out
			(else_try),
				(gt, ":div_spacing", 0),
				(team_give_order, "$fplayer_team_no", ":fdivision", mordr_stand_closer),
				(try_begin),
					(gt, ":div_spacing", 1),
					(assign, ":div_spacing", 1),
				(else_try),
					(assign, ":div_spacing", 0),
				(try_end),
			(try_end),
			(set_show_messages, 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
		(try_end),
	(try_end),
	]),

	# script_formation_move_position by motomataru
	# Input: team, division, formation current position, (1 to advance or -1 to withdraw or 0 to redirect)
	# Output: pos1 (offset for centering)
	("formation_move_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fcurrentpos", 3),
	(store_script_param, ":direction", 4),
	(copy_position, pos1, ":fcurrentpos"),
	(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
	(try_begin),
		(neq, reg0, 0),	#more than 0 enemies still alive?
		(copy_position, pos1, ":fcurrentpos"),	#restore current formation "position"
		(call_script, "script_point_y_toward_position", pos1, pos60),	#record angle from center to enemy
		(assign, ":distance_to_enemy", reg0),
#		(team_get_order_position, pos61, ":fteam", ":fdivision"),
		(call_script, "script_get_formation_position", pos61, ":fteam", ":fdivision"),
		(get_distance_between_positions, ":move_amount", pos1, pos61),	#distance already moving from previous orders
		(val_add, ":move_amount", 1000),
		(try_begin),
			(gt, ":direction", 0),	#moving forward?
			(gt, ":move_amount", ":distance_to_enemy"),
			(assign, ":move_amount", ":distance_to_enemy"),
		(try_end),
		(val_mul, ":move_amount", ":direction"),
		(position_move_y, pos1, ":move_amount", 0),
		(try_begin),
			(lt, ":distance_to_enemy", 1000),	#less than a move away?
			(position_copy_rotation, pos1, pos61),	#avoid rotating formation
		(try_end),
#		(team_set_order_position, ":fteam", ":fdivision", pos1),
		(call_script, "script_set_formation_position", ":fteam", ":fdivision", pos1),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
		(team_get_slot, ":formation_extra_spacing", ":fteam", ":slot"),
		(try_begin),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(neg|team_slot_eq, ":fteam", ":slot", sdt_archer),
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(team_get_slot, ":fformation", ":fteam", ":slot"),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, pos1, reg0, 0),
	(try_end),
	]),

	# script_set_formation_position by motomataru
	# Input: team, troop class, position
	# Kluge around buggy *_order_position functions for teams 0-3
	("set_formation_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fposition", 3),
	
	(position_get_x, ":x", ":fposition"),
	(position_get_y, ":y", ":fposition"),
	(position_get_rotation_around_z, ":zrot", ":fposition"),
	
	(store_add, ":slot", slot_team_d0_formation_x, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":x"),	
	(store_add, ":slot", slot_team_d0_formation_y, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":y"),	
	(store_add, ":slot", slot_team_d0_formation_zrot, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":zrot"),
	
	(team_set_order_position, ":fteam", ":fdivision", ":fposition"),
	]),	

	# script_get_formation_position by motomataru
	# Input: position, team, troop class
	# Output: input position (pos0 used)
	# Kluge around buggy *_order_position functions for teams 0-3
	("get_formation_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fdivision", 3),
	(init_position, ":fposition"),
	(try_begin),
			(is_between, ":fteam", 0, 4),
		(store_add, ":slot", slot_team_d0_formation_x, ":fdivision"),
		(team_get_slot, ":x", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_y, ":fdivision"),
		(team_get_slot, ":y", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_zrot, ":fdivision"),
		(team_get_slot, ":zrot", ":fteam", ":slot"),
		
		(position_set_x, ":fposition", ":x"),
		(position_set_y, ":fposition", ":y"),
		(position_rotate_z, ":fposition", ":zrot"),
	(else_try), #CABA - When would this ever be called?
		(store_add, ":slot", slot_team_d0_first_member, ":fdivision"),
		(team_get_slot, reg0, ":fteam", ":slot"),
		(try_begin),	  # "launder" team_get_order_position shutting down position_move_x
			(gt, reg0, -1),
			(team_get_order_position, ":fposition", ":fteam", ":fdivision"),
			(agent_get_position, pos0, reg0),
			(agent_set_position, reg0, ":fposition"),
			(agent_get_position, ":fposition", reg0),
			(agent_set_position, reg0, pos0),
		(try_end),
	(try_end),
	(position_set_z_to_ground_level, ":fposition"),
	]),	

	# script_cf_battlegroup_valid_formation by Caba'drin
	# Input: team, division, formation
	# Output: reg0: troop count/1 if too few troops/0 if wrong type
	("cf_battlegroup_valid_formation", [
		(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fformation", 3),
	
	(assign, ":valid_type", 0),
	(store_add, ":slot", slot_team_d0_type, ":fdivision"),
	(team_get_slot, ":sd_type", ":fteam", ":slot"),
	(try_begin), #Eventually make this more complex with the sub-divisions
		(this_or_next|eq, ":sd_type", sdt_cavalry),
		(eq, ":sd_type", sdt_harcher),
		(assign, ":size_minimum", formation_min_cavalry_troops),
		(try_begin),
			(eq, ":fformation", formation_wedge),
			(assign, ":valid_type", 1),
		(try_end),
	(else_try),
		(eq, ":sd_type", sdt_archer),
		(assign, ":size_minimum", formation_min_foot_troops),
		(try_begin),
			(this_or_next|eq, ":fformation", formation_ranks),
			(eq, ":fformation", formation_default),
			(assign, ":valid_type", 1),
		(try_end),
	(else_try),
		(assign, ":size_minimum", formation_min_foot_troops),
		(neq, ":fformation", formation_none),
		(assign, ":valid_type", 1), #all types valid
	(try_end),
	
	(try_begin),
			(eq, ":valid_type", 0),
		(assign, ":num_troops", 0),
	(else_try),
		(store_add, ":slot", slot_team_d0_size, ":fdivision"),
			(team_get_slot, ":num_troops", ":fteam", ":slot"),
			(le, ":num_troops", ":size_minimum"),
		(assign, ":num_troops", 1),
	(try_end),
	
	(assign, reg0, ":num_troops"),
	(gt, ":num_troops", 1)
	]),

	# script_cf_valid_formation_member by motomataru #CABA - Modified for Classify_agent phase out
	# Input: team, division, agent number of team leader, test agent
	# Output: failure indicates agent is not member of formation
	("cf_valid_formation_member", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fdivision", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":agent", 4),
	(neq, ":fleader", ":agent"),
	(agent_get_division, ":bgroup", ":agent"),
	(eq, ":bgroup", ":fdivision"),
	#(call_script, "script_classify_agent", ":agent"),
	#(eq, reg0, ":fdivision"),
	(agent_get_team, ":team", ":agent"),
	(eq, ":team", ":fteam"),
	(agent_is_alive, ":agent"),
	(agent_is_human, ":agent"),
	(agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
	]),

# #Player team formations functions
	# script_player_attempt_formation
	# Inputs:	arg1: division
	#			arg2: formation identifier (formation_*)
	# Output: none
	("player_attempt_formation", [
	(store_script_param, ":fdivision", 1),
	(store_script_param, ":fformation", 2),
	(set_fixed_point_multiplier, 100),
	(try_begin),
		(eq, ":fformation", formation_ranks),
		(str_store_string, s1, "@ranks"),
	(else_try),
		(eq, ":fformation", formation_shield),
		(str_store_string, s1, "@shield wall"),
	(else_try),
		(eq, ":fformation", formation_wedge),
		(str_store_string, s1, "@wedge"),
	(else_try),
		(eq, ":fformation", formation_square),
		(str_store_string, s1, "@square"),
	(else_try),
		(str_store_string, s1, "@up"),
	(try_end),
	(str_store_class_name, s2, ":fdivision"),

	(try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", "$fplayer_team_no", ":fdivision", ":fformation"),
		(try_begin),	#new formation?
			(store_add, ":slot", slot_team_d0_formation, ":fdivision"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", ":fformation"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":fformation"),
			(display_message, "@{!}{s2} forming {s1}."),
			(store_add, ":slot", slot_team_d0_formation_space, ":fdivision"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			#bring unformed divisions into sync with formations' minimum
			(set_show_messages, 0),
			(assign, reg0, ":div_spacing"),
			(try_for_range, reg1, reg0, formation_start_spread_out),	#spread out for ease of forming up	
				(team_give_order, "$fplayer_team_no", ":fdivision", mordr_spread_out),
				(val_add, ":div_spacing", 1),
			(try_end),
			(set_show_messages, 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
		(try_end),
		
	(else_try),
		(assign, ":return_val", reg0),
		(call_script, "script_formation_end", "$fplayer_team_no", ":fdivision"),
		(neq, ":fformation", formation_none),
		(try_begin),
			(gt, ":return_val", 0),
			(display_message, "@Not enough troops in {s2} to form {s1}, but holding."),
		(else_try),
			(store_add, ":slot", slot_team_d0_type, ":fdivision"),
			(team_get_slot, reg0, "$fplayer_team_no", ":slot"),
			(call_script, "script_str_store_division_type_name", s3, reg0),
			(display_message, "@{!}{s2} is an {s3} division and cannot form {s1}, so is holding."),
		(try_end),
	(try_end),
	(call_script, "script_battlegroup_place_around_leader", "$fplayer_team_no", ":fdivision"),
	]),

	# script_str_store_division_type_name by motomataru
	# Input:	destination, division type (sdt_*)
	# Output: none
	("str_store_division_type_name", [
	(store_script_param, ":str_reg", 1),
	(store_script_param, ":division_type", 2),
	(try_begin),
		(eq, ":division_type", sdt_infantry),
		(str_store_string, ":str_reg", "@infantry"),
	(else_try),
		(eq, ":division_type", sdt_archer),
		(str_store_string, ":str_reg", "@archer"),
	(else_try),
		(eq, ":division_type", sdt_cavalry),
		(str_store_string, ":str_reg", "@cavalry"),
	(else_try),
		(eq, ":division_type", sdt_polearm),
		(str_store_string, ":str_reg", "@polearm"),
	(else_try),
		(eq, ":division_type", sdt_skirmisher),
		(str_store_string, ":str_reg", "@skirmisher"),
	(else_try),
		(eq, ":division_type", sdt_harcher),
		(str_store_string, ":str_reg", "@mounted archer"),
	(else_try),
		(eq, ":division_type", sdt_support),
		(str_store_string, ":str_reg", "@support"),
	(else_try),
		(eq, ":division_type", sdt_bodyguard),
		(str_store_string, ":str_reg", "@bodyguard"),
	(else_try),
		(str_store_string, ":str_reg", "@undetermined type of"),
	(try_end),
	]),
	
	# script_player_order_formations by motomataru
	# Inputs:	arg1: order to formation (mordr_*)
	# Output: none
	("player_order_formations", [
	(store_script_param, ":forder", 1),
	(set_fixed_point_multiplier, 100),
	
	(try_begin), #On hold, any formations reform in new location		
		(eq, ":forder", mordr_hold),
		(call_script, "script_division_reset_places"),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_size, ":division"),	#apply to all divisions (not just formations)
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation"),
		(try_end),
		
	(else_try),	#Follow is hold	repeated frequently
		(eq, ":forder", mordr_follow),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_size, ":division"),	#apply to all divisions (not just formations)
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),	#update formations
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation"),

			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),
		(try_end),
		
	(else_try),	#charge or retreat ends formation
		(this_or_next|eq, ":forder", mordr_charge),
		(eq, ":forder", mordr_retreat),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(store_add, reg0, ":division", 1),
			(try_begin),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(display_message, "@Division {reg0}: infantry formation disassembled."),
			(else_try),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(display_message, "@Division {reg0}: archer formation disassembled."),
			(else_try),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
				(display_message, "@Division {reg0}: skirmisher formation disassembled."),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(display_message, "@Division {reg0}: cavalry formation disassembled."),
			(else_try),
				(display_message, "@Division {reg0}: formation disassembled."),			
			(try_end),
		(try_end),
		
	(else_try),	#dismount ends formation
		(eq, ":forder", mordr_dismount),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
			(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			(display_message, "@Cavalry formation disassembled."),
				(try_end),
			
	(else_try), 
		(eq, ":forder", mordr_advance),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(try_begin),
				(neq, ":prev_order", mordr_advance),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, 1),

			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
				(try_end),			

	(else_try),
		(eq, ":forder", mordr_fall_back),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_get_slot, ":prev_order", "$fplayer_team_no", ":slot"),	
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(try_begin),
				(neq, ":prev_order", mordr_fall_back),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, -1),			

			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
				(try_end),		

	(else_try),
		(eq, ":forder", mordr_stand_closer),		
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(gt, ":div_spacing", -3),	#Native formations go down to four ranks
			(val_sub, ":div_spacing", 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(try_begin),	#bring unformed divisions into sync with formations' minimum
				(lt, ":div_spacing", 0),
				(set_show_messages, 0),
				(assign, reg0, ":div_spacing"),
				(try_for_range, reg1, reg0, 0),
					(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
					(val_add, ":div_spacing", 1),
				(try_end),
				(set_show_messages, 1),
				(store_add, ":slot", slot_team_d0_formation_space, ":division"),
				(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
				
			(else_try),
				(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),
				(store_add, ":slot", slot_team_d0_type, ":division"),
				(try_begin),
					(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
					(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
				(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
					(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
					(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
				(else_try),
					(store_add, ":slot", slot_team_d0_size, ":division"),
					(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
					(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
				(try_end),
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_spread_out),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(try_begin),
				(this_or_next|neq, ":formation", formation_none),
				(lt, ":div_spacing", 2),	#Native maxes at 2
				(val_add, ":div_spacing", 1),
			(try_end),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			
			(neq, ":formation", formation_none),

			#bring unformed divisions into sync with formations' minimum
			(set_show_messages, 0),
			(assign, reg0, ":div_spacing"),
			(try_for_range, reg1, reg0, 1),
				(team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
				(val_add, ":div_spacing", 1),
			(try_end),
			(set_show_messages, 1),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),

			(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(store_add, ":slot", slot_team_d0_size, ":division"), 
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"), 
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_stand_ground),
		(try_for_range, ":division", 0, 9),
				(class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", ":forder"),	
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division"),
			(copy_position, pos1, pos63),		
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
					(store_add, ":slot", slot_team_d0_size, ":division"),
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
					(val_mul, reg0, -1),
					(position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(else_try),
					(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
			(else_try),
				(store_add, ":slot", slot_team_d0_size, ":division"),
							(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),	
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
					(position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":formation"),
			(try_end),
			(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
		(try_end),			
	(try_end)
	]),

	
# #Utilities used by formations
	# script_point_y_toward_position by motomataru
	# Input: from position, to position
	# Output: reg0 fixed point distance
	("point_y_toward_position", [
	(store_script_param, ":from_position", 1),
	(store_script_param, ":to_position", 2),
	(position_get_x, ":dist_x_to_cosine", ":to_position"),
	(position_get_x, ":from_coord", ":from_position"),
	(val_sub, ":dist_x_to_cosine", ":from_coord"),
	(store_mul, ":sum_square", ":dist_x_to_cosine", ":dist_x_to_cosine"),
	(position_get_y, ":dist_y_to_sine", ":to_position"),
	(position_get_y, ":from_coord", ":from_position"),
	(val_sub, ":dist_y_to_sine", ":from_coord"),
	(store_mul, reg0, ":dist_y_to_sine", ":dist_y_to_sine"),
	(val_add, ":sum_square", reg0),
	(convert_from_fixed_point, ":sum_square"),
	(store_sqrt, ":distance_between", ":sum_square"),
	(convert_to_fixed_point, ":dist_x_to_cosine"),
	(val_div, ":dist_x_to_cosine", ":distance_between"),
	(convert_to_fixed_point, ":dist_y_to_sine"),
	(val_div, ":dist_y_to_sine", ":distance_between"),
	(try_begin),
		(lt, ":dist_x_to_cosine", 0),
		(assign, ":bound_a", 90),
		(assign, ":bound_b", 270),
		(assign, ":theta", 180),
	(else_try),
		(assign, ":bound_a", 90),
		(assign, ":bound_b", -90),
		(assign, ":theta", 0),
	(try_end),
	(assign, ":sine_theta", 0),	#avoid error on compile
	(convert_to_fixed_point, ":theta"),
	(convert_to_fixed_point, ":bound_a"),
	(convert_to_fixed_point, ":bound_b"),
	(try_for_range, reg0, 0, 6),	#precision 90/2exp6 (around 2 degrees)
		(store_sin, ":sine_theta", ":theta"),
		(try_begin),
			(gt, ":sine_theta", ":dist_y_to_sine"),
			(assign, ":bound_a", ":theta"),
		(else_try),
			(lt, ":sine_theta", ":dist_y_to_sine"),
			(assign, ":bound_b", ":theta"),
		(try_end),
		(store_add, ":angle_sum", ":bound_b", ":bound_a"),
		(store_div, ":theta", ":angle_sum", 2),
	(try_end),
	(convert_from_fixed_point, ":theta"),
	(position_get_rotation_around_z, reg0, ":from_position"),
	(val_sub, ":theta", reg0),
	(val_sub, ":theta", 90),	#point y-axis at destination
	(position_rotate_z, ":from_position", ":theta"),
	(assign, reg0, ":distance_between"),
	]),

	# script_store_battlegroup_type by Caba'drin   ##NEEDS EDIT per PMs with moto
	# Input: team, division
	# Output: reg0 and slot_team_dx_type with sdt_* value
	# Automatically called from store_battlegroup_data
	("store_battlegroup_type", [
		(store_script_param_1, ":fteam"),
	(store_script_param_2, ":fdivision"),
	
	#hard-code the traditional three
	(try_begin),
		(eq, ":fdivision", grc_infantry),
		(assign, ":div_type", sdt_infantry),
	(else_try),
		(eq, ":fdivision", grc_archers),
		(assign, ":div_type", sdt_archer),
	(else_try),
		(eq, ":fdivision", grc_cavalry),
		(assign, ":div_type", sdt_cavalry),
		
	#attempt to type the rest
	(else_try),
		(assign, ":count_infantry", 0),
		(assign, ":count_archer", 0),
		(assign, ":count_cavalry", 0),
		(assign, ":count_harcher", 0),
		(assign, ":count_polearms", 0),
		(assign, ":count_skirmish", 0),
		(assign, ":count_support", 0),
		(assign, ":count_bodyguard", 0),	

		(try_for_agents, ":cur_agent"),
			(agent_is_alive, ":cur_agent"),      
			(agent_is_human, ":cur_agent"), 
			(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
			(agent_get_team, ":bgteam", ":cur_agent"),
			(eq, ":bgteam", ":fteam"),
			#(call_script, "script_classify_agent", ":cur_agent"),
			#(assign, ":bgroup", reg0),
			(team_get_leader, ":leader", ":fteam"),
			(neq, ":leader", ":cur_agent"),
			(agent_get_division, ":bgroup", ":cur_agent"),
			(eq, ":bgroup", ":fdivision"),
			(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
			(agent_get_wielded_item, reg0, ":cur_agent", 0),
			
			(try_begin),
				(lt, reg0, 0),
				(assign, ":cur_weapon_type", 0),
			(else_try),
				(item_get_type, ":cur_weapon_type", reg0), 
			(try_end),
			
			(try_begin),
				(neg|troop_is_hero, ":cur_troop"),
				(try_begin), #Cavalry	
					(agent_get_horse, reg0, ":cur_agent"),
					(ge, reg0, 0),
					(try_begin),				
						(gt, ":cur_ammo", 0),
						(val_add, ":count_harcher", 1),
					(else_try),
						(val_add, ":count_cavalry", 1),
					(try_end),
				(else_try), #Archers
					(gt, ":cur_ammo", 0),
					(try_begin),
						(eq, ":cur_weapon_type", itp_type_thrown),
						(val_add, ":count_skirmish", 1),
					(else_try),
						(val_add, ":count_archer", 1),
					(try_end),
				(else_try), #Infantry
					(try_begin),
						(eq, ":cur_weapon_type", itp_type_polearm),
						(val_add, ":count_polearms", 1),
					(else_try),
						(val_add, ":count_infantry", 1),
					(try_end),			    
				(try_end),
			(else_try), #Heroes
				(assign, ":support_skills", 0), #OPEN TO SUGGESTIONS HERE    ?skl_trade, skl_spotting, skl_pathfinding, skl_tracking?
				(store_skill_level, reg0, skl_engineer, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_first_aid, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_surgery, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(store_skill_level, reg0, skl_wound_treatment, ":cur_troop"),
				(val_add, ":support_skills", reg0),
				(try_begin),
					(gt, ":support_skills", 5),
					(val_add, ":count_support", 1),
				(else_try),
					(val_add, ":count_bodyguard", 1),
				(try_end),		
			(try_end), #Regular v Hero		
		(try_end), #Agent Loop	
			
		#Do Comparisons With Counts, set ":div_type"
		(assign, ":slot", slot_team_d0_type),
		(team_set_slot, 7, ":slot", ":count_infantry"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_archer"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_cavalry"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_polearms"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_skirmish"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_harcher"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_support"),
		(val_add, ":slot", 1),
		(team_set_slot, 7, ":slot", ":count_bodyguard"),

		(assign, ":count_to_beat", 0),
		(assign, ":count_total", 0),
		(try_for_range, ":type", sdt_infantry, sdt_infantry + 8), #only 8 sdt_types at the moment
			(store_add, ":slot", slot_team_d0_type, ":type"),
			(team_get_slot, ":count", 7, ":slot"),
			(val_add, ":count_total", ":count"),
			(lt, ":count_to_beat", ":count"),
			(assign, ":count_to_beat", ":count"),
			(assign, ":div_type", ":type"),
		(try_end),
		
		(val_mul, ":count_to_beat", 2),
		(try_begin),
			(lt, ":count_to_beat", ":count_total"), #Less than half of this division
			(assign, ":count_to_beat", 0),
			(assign, ":div_type", -1),
			(try_for_range, ":type", sdt_infantry, sdt_infantry + 3), #check main types for a majority
				(store_add, ":slot", slot_team_d0_type, ":type"),
				(team_get_slot, ":count", 7, ":slot"),
				(val_add, ":slot", 3),	#subtype is three more than main type
				(team_get_slot, reg0, 7, ":slot"),
				(val_add, ":count", reg0),
				(lt, ":count_to_beat", ":count"),
				(assign, ":count_to_beat", ":count"),
				(assign, ":div_type", ":type"),
			(try_end),
		
			(val_mul, ":count_to_beat", 2),
			(lt, ":count_to_beat", ":count_total"), #Less than half of this division
			(assign, ":div_type", sdt_unknown), #Or 0
		(try_end),
	(try_end),	#divisions 3-8
	
	(store_add, ":slot", slot_team_d0_type, ":fdivision"),
	(team_set_slot, ":fteam", ":slot", ":div_type"),
	(assign, reg0, ":div_type"),  
	]),

	# script_store_battlegroup_data by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
	# Input: none
	# Output: sets positions and globals to track data on ALL groups in a battle
	# Globals used: pos1, reg0, reg1, #CABA - NO LONGER USED: positions 24-45
	("store_battlegroup_data", [
	(assign, ":team0_leader", 0),
	(assign, ":team0_x_leader", 0),
	(assign, ":team0_y_leader", 0),
	(assign, ":team0_level_leader", 0),
	(assign, ":team1_leader", 0),
	(assign, ":team1_x_leader", 0),
	(assign, ":team1_y_leader", 0),
	(assign, ":team1_level_leader", 0),
	(assign, ":team2_leader", 0),
	(assign, ":team2_x_leader", 0),
	(assign, ":team2_y_leader", 0),
	(assign, ":team2_level_leader", 0),
	(assign, ":team3_leader", 0),
	(assign, ":team3_x_leader", 0),
	(assign, ":team3_y_leader", 0),
	(assign, ":team3_level_leader", 0),
	
	#Team Slots reset every mission, like agent slots, but just to be sure for when it gets called during the mission
	(try_for_range, ":team", 0, 4),
			(try_for_range, ":slot", reset_team_stats_begin, reset_team_stats_end), #Those within the "RESET GROUP" in formations_constants
				(team_set_slot, ":team", ":slot", 0),
		(try_end),
		(try_for_range, ":bgroup", 0, 9),
			(store_add, ":slot", slot_team_d0_first_member, ":bgroup"),
			(team_set_slot, ":team", ":slot", -1),
		(try_end),
	(try_end),

	(try_for_agents, ":cur_agent"),
		(agent_is_alive, ":cur_agent"),      
		(agent_is_human, ":cur_agent"), 
		(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
		(agent_get_team, ":bgteam", ":cur_agent"),
		#(call_script, "script_classify_agent", ":cur_agent"),
		#(assign, ":bgroup", reg0),
		(agent_get_division, ":bgroup", ":cur_agent"),
		(try_begin),
			(team_get_leader, ":leader", ":bgteam"),
				(eq, ":leader", ":cur_agent"),
			(assign, ":bgroup", -1),
		(try_end),
		(agent_get_troop_id, ":cur_troop", ":cur_agent"),
		(store_character_level, ":cur_level", ":cur_troop"),
		(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
		(assign, ":cur_weapon_type", 0),
		(assign, ":cur_weapon_length", 0),
		(agent_get_wielded_item, reg0, ":cur_agent", 0),
		(try_begin),
			(gt, reg0, itm_no_item),
			(item_get_type, ":cur_weapon_type", reg0),
			(this_or_next|eq, ":cur_weapon_type", itp_type_one_handed_wpn),
			(this_or_next|eq, ":cur_weapon_type", itp_type_two_handed_wpn),
			(this_or_next|eq, ":cur_weapon_type", itp_type_polearm),
			(eq, ":cur_weapon_type", itp_type_thrown),
			(item_get_slot, ":cur_weapon_length", reg0, slot_item_length),
		(try_end),
		(agent_get_position, pos1, ":cur_agent"),
		(position_get_x, ":x_value", pos1),
		(position_get_y, ":y_value", pos1),
		(try_begin),
				(eq, ":bgroup", -1), #Leaders
			(try_begin),
				(eq, ":bgteam", 0),
				(assign, ":team0_leader", 1),
				(assign, ":team0_x_leader", ":x_value"),
				(assign, ":team0_y_leader", ":y_value"),
				(assign, ":team0_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 1),
				(assign, ":team1_leader", 1),
				(assign, ":team1_x_leader", ":x_value"),
				(assign, ":team1_y_leader", ":y_value"),
				(assign, ":team1_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 2),
				(assign, ":team2_leader", 1),
				(assign, ":team2_x_leader", ":x_value"),
				(assign, ":team2_y_leader", ":y_value"),
				(assign, ":team2_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 3),
				(assign, ":team3_leader", 1),
				(assign, ":team3_x_leader", ":x_value"),
				(assign, ":team3_y_leader", ":y_value"),
				(assign, ":team3_level_leader", ":cur_level"),
			(try_end),
		(else_try),
			(try_begin),	#First Agent
				(store_add, ":slot", slot_team_d0_first_member, ":bgroup"),
				(neg|team_slot_ge, ":bgteam", ":slot", 0),
				(team_set_slot, ":bgteam", ":slot", ":cur_agent"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_size, ":bgroup"), #Division Count
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(try_begin),
				(gt, ":cur_ammo", 0),
				(store_add, ":slot", slot_team_d0_percent_ranged, ":bgroup"), #Division Percentage are Archers
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(else_try),
				(store_add, ":slot", slot_team_d0_low_ammo, ":bgroup"), #Division Running out of Ammo Flag
				(team_set_slot, ":bgteam", ":slot", 1),
			(try_end),
			
			(try_begin),
				(eq, ":cur_weapon_type", itp_type_thrown),
				(store_add, ":slot", slot_team_d0_percent_throwers, ":bgroup"), #Division Percentage are Throwers
				(team_get_slot, ":value", ":bgteam", ":slot"),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", ":slot", ":value"),
			(try_end),
			
			(store_add, ":slot", slot_team_d0_level, ":bgroup"), #Division Level
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_level"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_weapon_length, ":bgroup"), #Division Weapon Length
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_weapon_length"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_x, ":bgroup"), #Position X
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":x_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_y, ":bgroup"), #Position Y
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":y_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
		(try_end), #Leader vs Regular
	(try_end), #Agent Loop

	#calculate team sizes, sum positions; within calculate battle group averages
	(try_for_range, ":team", 0, 4),
			(assign, ":team_size", 0),
		(assign, ":team_level", 0),
		(assign, ":team_x", 0),
		(assign, ":team_y", 0),
		
		(assign, ":num_infantry", 0),
		(assign, ":num_archers", 0),
		(assign, ":num_cavalry", 0),
		
			(try_for_range, ":division", 0, 9),
				#sum for team averages
				(store_add, ":slot", slot_team_d0_size, ":division"),
				(team_get_slot, ":division_size", ":team", ":slot"),
			(gt, ":division_size", 0),
			(val_add, ":team_size", ":division_size"),
			
			(store_add, ":slot", slot_team_d0_level, ":division"),
				(team_get_slot, ":division_level", ":team", ":slot"),
			(val_add, ":team_level", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_x, ":division"),
				(team_get_slot, ":division_x", ":team", ":slot"),
			(val_add, ":team_x", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_y, ":division"),
				(team_get_slot, ":division_y", ":team", ":slot"),
			(val_add, ":team_y", ":division_y"),
			
						#calculate battle group averages
			(store_add, ":slot", slot_team_d0_level, ":division"),
			(val_div, ":division_level", ":division_size"),			
			(team_set_slot, ":team", ":slot", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_percent_ranged, ":division"),
			(team_get_slot, ":value", ":team", ":slot"),
			(val_mul, ":value", 100),
			(val_div, ":value", ":division_size"), 
			(team_set_slot, ":team", ":slot", ":value"),	

			(store_add, ":slot", slot_team_d0_percent_throwers, ":division"),
			(team_get_slot, ":value", ":team", ":slot"),
			(val_mul, ":value", 100),
			(val_div, ":value", ":division_size"), 
			(team_set_slot, ":team", ":slot", ":value"),	
		
			(store_add, ":slot", slot_team_d0_weapon_length, ":division"),
				(team_get_slot, ":value", ":team", ":slot"),
			(val_div, ":value", ":division_size"),
			(team_set_slot, ":team", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_x, ":division"),
			(val_div, ":division_x", ":division_size"),
				(team_set_slot, ":team", ":slot", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_y, ":division"),
			(val_div, ":division_y", ":division_size"),
				(team_set_slot, ":team", ":slot", ":division_y"),
			
			#(try_begin),
			#    (lt, ":division", 3), #CABA - This works right now, as only the player has other divisions enabled...NEED TO RECONSIDER LATER
			#    (store_mul, ":team_shift", ":team", 4),
				#    (store_add, ":position_number", Team0_Infantry_Pos, ":team_shift"),
			#    (val_add, ":position_number", ":division"),
			#(else_try),
			#    (store_sub, ":team_shift", ":division", 3),
			#	(store_add, ":position_number", Player_Battle_Group3_Pos, ":team_shift"),
			#(try_end),			    
				#(init_position, ":position_number"), #CABA - REMOVED AUTOMATIC initialization of positions...problem?
			
			#(val_div, ":division_x", ":division_size"),
			#(position_set_x, ":position_number", ":division_x"),
			#(val_div, ":division_y", ":division_size"),
			#(position_set_y, ":position_number", ":division_y"),
			#(position_set_z_to_ground_level, ":position_number"),

			(store_add, ":slot", slot_team_d0_type, ":division"),
			(team_get_slot, reg0, ":team", ":slot"),
			(try_begin),
				(neg|is_between, reg0, 0, 8),	#TODO reset on reinforcements
								(call_script, "script_store_battlegroup_type", ":team", ":division"),
			(try_end),
						(try_begin),
								(this_or_next|eq, reg0, sdt_infantry),
				(eq, reg0, sdt_polearm),
				(val_add, ":num_infantry", ":division_size"),
			(else_try),
					(this_or_next|eq, reg0, sdt_archer),
				(eq, reg0, sdt_skirmisher),
				(val_add, ":num_archers", ":division_size"),
			(else_try),
					(this_or_next|eq, reg0, sdt_cavalry),
				(eq, reg0, sdt_harcher),
				(val_add, ":num_cavalry", ":division_size"),
			(try_end),
		(try_end), #Division Loop
		
		(team_set_slot, ":team", slot_team_num_infantry, ":num_infantry"),
		(team_set_slot, ":team", slot_team_num_archers, ":num_archers"),
		(team_set_slot, ":team", slot_team_num_cavalry, ":num_cavalry"),

		#Team Leader Additions
		(try_begin),
				(eq, ":team", 0),
			(val_add, ":team_size", ":team0_leader"),
			(val_add, ":team_level", ":team0_level_leader"),
			(val_add, ":team_x", ":team0_x_leader"),
			(val_add, ":team_y", ":team0_y_leader"),
		(else_try),
				(eq, ":team", 1),
			(val_add, ":team_size", ":team1_leader"),
			(val_add, ":team_level", ":team1_level_leader"),
			(val_add, ":team_x", ":team1_x_leader"),
			(val_add, ":team_y", ":team1_y_leader"),
		(else_try),
			(eq, ":team", 2),
			(val_add, ":team_size", ":team2_leader"),
			(val_add, ":team_level", ":team2_level_leader"),
			(val_add, ":team_x", ":team2_x_leader"),
			(val_add, ":team_y", ":team2_y_leader"),
		(else_try),
			(eq, ":team", 3),
			(val_add, ":team_size", ":team3_leader"),
			(val_add, ":team_level", ":team3_level_leader"),
			(val_add, ":team_x", ":team3_x_leader"),
			(val_add, ":team_y", ":team3_y_leader"),		
		(try_end),
		
		#calculate team averages 
		(gt, ":team_size", 0),
		(team_set_slot, ":team", slot_team_size, ":team_size"),
		(val_div, ":team_level", ":team_size"),
		(team_set_slot, ":team", slot_team_level, ":team_level"),	
			
		(val_div, ":team_x", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_x, ":team_x"),
		(val_div, ":team_y", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_y, ":team_y"),
		
		#(store_mul, ":team_shift", ":team", 4),
		#(store_add, ":position_number", Team0_Average_Pos, ":team_shift"),
		# (store_add, ":position_number", Team0_Average_Pos, ":team"),
		# (init_position, ":position_number"),		
		# (val_div, ":team_x", ":team_size"),
		# (position_set_x, ":position_number", ":team_x"),
		# (val_div, ":team_y", ":team_size"),
		# (position_set_y, ":position_number", ":team_y"),
		# (position_set_z_to_ground_level, ":position_number"),
	(try_end), #Team Loop
	]),

	# script_team_get_position_of_enemies by motomataru
	# Input: destination position, team, troop class/division
	# Output: destination position: average position if reg0 > 0
	#			reg0: number of enemies
	# Run script_store_battlegroup_data before calling!
	("team_get_position_of_enemies", [
	(store_script_param, ":enemy_position", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":troop_type", 3),
	(assign, ":pos_x", 0),
	(assign, ":pos_y", 0),
	(assign, ":total_size", 0),
	
	(try_for_range, ":other_team", 0, 4),
		(teams_are_enemies, ":other_team", ":team_no"),
		(try_begin),
			(eq, ":troop_type", grc_everyone),
			(team_get_slot, ":team_size", ":other_team", slot_team_size),
			(try_begin),
				(gt, ":team_size", 0),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", grc_everyone),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(else_try),	#MOTO: this doesn't work -- for multiple divisions, should find the CLOSEST of a given type
			(assign, ":team_size", 0),
			(try_for_range, ":enemy_battle_group", 0, 9),
				(eq, ":enemy_battle_group", ":troop_type"),
				(store_add, ":slot", slot_team_d0_size, ":troop_type"),
							(team_get_slot, ":troop_count", ":other_team", ":slot"),
				(gt, ":troop_count", 0),
				(val_add, ":team_size", ":troop_count"),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", ":troop_type"),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(try_end),
		(val_add, ":total_size", ":team_size"),
	(try_end),
	
	(try_begin),
		(eq, ":total_size", 0),
		(init_position, ":enemy_position"),
	(else_try),
		(val_div, ":pos_x", ":total_size"),
		(position_set_x, ":enemy_position", ":pos_x"),
		(val_div, ":pos_y", ":total_size"),
		(position_set_y, ":enemy_position", ":pos_y"),
		(position_set_z_to_ground_level, ":enemy_position"),
	(try_end),

	(assign, reg0, ":total_size"),
	]),

# # M&B Standard AI with changes for formations #CABA - OK; Need expansion when new AI divisions to work with
	# script_formation_battle_tactic_init_aux
	# Input: team_no, battle_tactic
	# Output: none
	("formation_battle_tactic_init_aux",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":battle_tactic", 2),
			(team_get_leader, ":ai_leader", ":team_no"),
			(try_begin),
				(eq, ":battle_tactic", btactic_hold),
				(agent_get_position, pos1, ":ai_leader"),
				(call_script, "script_find_high_ground_around_pos1", ":team_no", 30),
				(copy_position, pos1, pos52),
				(call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
				(copy_position, pos1, pos52),
				(call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
				(team_give_order, ":team_no", grc_everyone, mordr_hold),
				(team_set_order_position, ":team_no", grc_everyone, pos52),
				(team_give_order, ":team_no", grc_archers, mordr_advance),
				(team_give_order, ":team_no", grc_archers, mordr_advance),
			(else_try),
				(eq, ":battle_tactic", btactic_follow_leader),
				(team_get_leader, ":ai_leader", ":team_no"),
				(ge, ":ai_leader", 0),
				(agent_set_speed_limit, ":ai_leader", 8),
				(agent_get_position, pos60, ":ai_leader"),
				(team_give_order, ":team_no", grc_everyone, mordr_hold),
				(team_set_order_position, ":team_no", grc_everyone, pos60),
			(try_end),
# formations additions
		(call_script, "script_division_reset_places"),
		(call_script, "script_get_default_formation", ":team_no"),
		(assign, ":fformation", reg0),
		
		(try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":fformation"),
		(store_add, ":slot", slot_team_d0_formation, grc_infantry),
		(team_set_slot, ":team_no", ":slot", ":fformation"),
		(store_add, ":slot", slot_team_d0_formation_space, grc_infantry),
		(team_set_slot, ":team_no", ":slot", 0),
		(else_try),
		(call_script, "script_formation_end", ":team_no", grc_infantry),
		(try_end),
		(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_infantry),
		
		(try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_archers, formation_default),
		(store_add, ":slot", slot_team_d0_formation, grc_archers),
		(team_set_slot, ":team_no", ":slot", formation_default),
		(store_add, ":slot", slot_team_d0_formation_space, grc_archers),
		(team_set_slot, ":team_no", ":slot", 2),
		(else_try),
		(call_script, "script_formation_end", ":team_no", grc_archers),
		(try_end),
		(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_archers),
		
		(try_begin),
		(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
		(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
		(team_set_slot, ":team_no", ":slot", formation_wedge),
		(store_add, ":slot", slot_team_d0_formation_space, grc_cavalry),
		(team_set_slot, ":team_no", ":slot", 0),
		(else_try),
		(call_script, "script_formation_end", ":team_no", grc_cavalry),
		(try_end),
		(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_cavalry),
		
		(team_give_order, ":team_no", grc_archers, mordr_spread_out),
		(team_give_order, ":team_no", grc_archers, mordr_spread_out),
# end formations additions
	]),
	
	# script_formation_battle_tactic_apply_aux #CABA - OK; Need expansion when new AI divisions to work with
	# Input: team_no, battle_tactic
	# Output: battle_tactic
	("formation_battle_tactic_apply_aux",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":battle_tactic", 2),
			(store_mission_timer_a, ":mission_time"),
			(try_begin),
				(eq, ":battle_tactic", btactic_hold),
				(copy_position, pos1, pos52),
				(call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no", 1),
				(assign, ":avg_dist", reg0),
				(assign, ":min_dist", reg1),
				(try_begin),
					(this_or_next|lt, ":min_dist", 1000),
					(lt, ":avg_dist", 4000),
					(assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
					(team_give_order, ":team_no", grc_everyone, mordr_charge),
				(try_end),
			(else_try),
				(eq, ":battle_tactic", btactic_follow_leader),
				(team_get_leader, ":ai_leader", ":team_no"),
				(try_begin),
					(agent_is_alive, ":ai_leader"),
					(agent_set_speed_limit, ":ai_leader", 9),
					(call_script, "script_team_get_average_position_of_enemies", ":team_no"),
					(copy_position, pos60, pos0),
					(ge, ":ai_leader", 0),
					(agent_get_position, pos61, ":ai_leader"),
					(position_transform_position_to_local, pos62, pos61, pos60), #pos62 = vector to enemy w.r.t leader
					(position_normalize_origin, ":distance_to_enemy", pos62),
					(convert_from_fixed_point, ":distance_to_enemy"),
					(assign, reg17, ":distance_to_enemy"),
					(position_get_x, ":dir_x", pos62),
					(position_get_y, ":dir_y", pos62),
					(val_mul, ":dir_x", 23),
					(val_mul, ":dir_y", 23), #move 23 meters
					(position_set_x, pos62, ":dir_x"),
					(position_set_y, pos62, ":dir_y"),
				
					(position_transform_position_to_parent, pos63, pos61, pos62), #pos63 is 23m away from leader in the direction of the enemy.
					(position_set_z_to_ground_level, pos63),
				
					(team_give_order, ":team_no", grc_everyone, mordr_hold),
					(team_set_order_position, ":team_no", grc_everyone, pos63),
#formations code
			(call_script, "script_point_y_toward_position", pos63, pos60),
			(agent_get_position, pos49, ":ai_leader"),
			(agent_set_position, ":ai_leader", pos63),	#fake out script_battlegroup_place_around_leader
			(call_script, "script_division_reset_places"),
			(call_script, "script_get_default_formation", ":team_no"),
			(assign, ":fformation", reg0),
			
			(try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":fformation"),
			(store_add, ":slot", slot_team_d0_formation, grc_infantry),
			(team_set_slot, ":team_no", ":slot", ":fformation"),
			(store_add, ":slot", slot_team_d0_formation_space, grc_infantry),
			(team_set_slot, ":team_no", ":slot", 0),
			(else_try),
			(call_script, "script_formation_end", ":team_no", grc_infantry),
			(try_end),
			(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_infantry),
			
			(try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_archers, formation_default),
			(store_add, ":slot", slot_team_d0_formation, grc_archers),
			(team_set_slot, ":team_no", ":slot", formation_default),
			(store_add, ":slot", slot_team_d0_formation_space, grc_archers),
			(team_set_slot, ":team_no", ":slot", 2),
			(else_try),
			(call_script, "script_formation_end", ":team_no", grc_archers),
			(try_end),
			(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_archers),
			
			(try_begin),
			(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
			(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
			(team_set_slot, ":team_no", ":slot", formation_wedge),
			(store_add, ":slot", slot_team_d0_formation_space, grc_cavalry),
			(team_set_slot, ":team_no", ":slot", 0),
			(else_try),
			(call_script, "script_formation_end", ":team_no", grc_cavalry),
			(try_end),
			(call_script, "script_battlegroup_place_around_leader", ":team_no", grc_cavalry),
		
			(agent_set_position, ":ai_leader", pos49),
#end formations code
					(agent_get_position, pos1, ":ai_leader"),
					(try_begin),
						(lt, ":distance_to_enemy", 50),
						(ge, ":mission_time", 30),
						(assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
						(team_give_order, ":team_no", grc_everyone, mordr_charge),
						(agent_set_speed_limit, ":ai_leader", 60),
					(try_end),
				(else_try),
					(assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
			(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
			(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
					(team_give_order, ":team_no", grc_everyone, mordr_charge),
				(try_end),
			(try_end),
			
			(try_begin), # charge everyone after a while
				(neq, ":battle_tactic", 0),
				(ge, ":mission_time", 300),
				(assign, ":battle_tactic", 0),
		(call_script, "script_formation_end", ":team_no", grc_infantry),	#formations
		(call_script, "script_formation_end", ":team_no", grc_archers),	#formations
		(call_script, "script_formation_end", ":team_no", grc_cavalry),	#formations
				(team_give_order, ":team_no", grc_everyone, mordr_charge),
				(team_get_leader, ":ai_leader", ":team_no"),
				(agent_set_speed_limit, ":ai_leader", 60),
			(try_end),
			(assign, reg0, ":battle_tactic"),
	]),
	
	# Replacement script for battle_tactic_init_aux to switch between using
	# M&B Standard AI with changes for formations and original based on
	# NOTE: original script "battle_tactic_init_aux" should be renamed to "orig_battle_tactic_init_aux"
	# constant formation_native_ai_use_formation ( 0: original, 1: use formation )
	# script_battle_tactic_init_aux
	# Input: team_no, battle_tactic
	# Output: none
	("battle_tactic_init_aux",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":battle_tactic", 2),
		(try_begin),
		(eq, formation_native_ai_use_formation, 1),
		(call_script, "script_formation_battle_tactic_init_aux", ":team_no", ":battle_tactic"),
		(else_try),
		(call_script, "script_orig_battle_tactic_init_aux", ":team_no", ":battle_tactic"),
		(try_end),
		]),

	# Replacement script for battle_tactic_init_aux to switch between using
	# M&B Standard AI with changes for formations and original based on
	# NOTE: original script "battle_tactic_apply_aux" should be renamed to "orig_battle_tactic_apply_aux"
	# constant formation_native_ai_use_formation ( 0: original, 1: use formation )
	# script_battle_tactic_apply_aux
	# Input: team_no, battle_tactic
	# Output: battle_tactic
	("battle_tactic_apply_aux",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":battle_tactic", 2),
		(try_begin),
		(eq, formation_native_ai_use_formation, 1),
		(call_script, "script_formation_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
		(else_try),
		(call_script, "script_orig_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
		(try_end),
	]),
	
# # AI with Formations Scripts
	# script_calculate_decision_numbers by motomataru
	# Input: AI team, size relative to battle in %
	# Output: reg0 - battle presence plus level bump, reg1 - level bump (team avg level / 3)
	("calculate_decision_numbers", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":battle_presence", 2),
	(try_begin),
		(team_get_slot, reg0, ":team_no", slot_team_level),
		(store_div, reg1, reg0, 3),
		(store_add, reg0, ":battle_presence", reg1),	#decision w.r.t. all enemy teams
	(try_end)
	]),
	
	

	# script_team_field_ranged_tactics by motomataru
	# Input: AI team, size relative to largest team in %, size relative to battle in %
	# Output: none
	("team_field_ranged_tactics", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":rel_army_size", 2),
	(store_script_param, ":battle_presence", 3),
	(assign, ":bgroup", grc_archers), #Pre-Many Divisions
	(assign, ":bg_pos", Archers_Pos), #Pre-Many Divisions

	(store_add, ":slot", slot_team_d0_size, ":bgroup"),
	(try_begin),
		(team_slot_ge, ":team_no", ":slot", 1),
		(call_script, "script_battlegroup_get_position", ":bg_pos", ":team_no", ":bgroup"),
		(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":team_no", grc_everyone),
		(call_script, "script_point_y_toward_position", ":bg_pos", Enemy_Team_Pos),
		(call_script, "script_get_nearest_enemy_battlegroup_location", Nearest_Enemy_Battlegroup_Pos, ":team_no", ":bg_pos"),
		(assign, ":distance_to_enemy", reg0),
			
		(call_script, "script_calculate_decision_numbers", ":team_no", ":battle_presence"),
		(assign, ":decision_index", reg0),
		(assign, ":level_bump", reg1),
		(try_begin),
			(gt, ":decision_index", 86),	#outpower enemies more than 6:1?
			(team_get_movement_order, reg0, ":team_no", ":bgroup"),
			(try_begin),
				(neq, reg0, mordr_charge),
				(team_give_order, ":team_no", ":bgroup", mordr_charge),
			(try_end),

		(else_try),
			(ge, "$battle_phase", BP_Jockey),
			(store_add, ":slot", slot_team_d0_low_ammo, ":bgroup"),
			(team_slot_ge, ":team_no", ":slot", 1),	#running out of ammo?
			(team_get_movement_order, reg0, ":team_no", ":bgroup"),
			(try_begin),
				(neq, reg0, mordr_charge),
				(team_give_order, ":team_no", ":bgroup", mordr_charge),
			(try_end),

		(else_try),
			(gt, "$cur_casualties", 0),
			(eq, "$cur_casualties", "$prev_casualties"),	#no new casualties since last function call?
			(gt, ":decision_index", Advance_More_Point),
			(le, ":distance_to_enemy", AI_long_range),	#closer than reposition?
			(team_give_order, ":team_no", ":bgroup", mordr_advance),

		#hold somewhere
		(else_try),
			(store_add, ":decision_index", ":rel_army_size", ":level_bump"),	#decision w.r.t. largest enemy team
			(assign, ":move_archers", 0),
			(try_begin),
				(eq, "$battle_phase", BP_Setup),
				(assign, ":move_archers", 1),
			(else_try),
				(ge, "$battle_phase", BP_Fight),
				(try_begin),
					(neg|is_between, ":distance_to_enemy", AI_charge_distance, AI_long_range),
					(assign, ":move_archers", 1),
				(else_try),
					(lt, ":decision_index", Hold_Point),	#probably coming from a defensive position (see below)
					(gt, ":distance_to_enemy", AI_firing_distance),
					(assign, ":move_archers", 1),
				(try_end),
			(else_try),
				(ge, ":decision_index", Hold_Point),	#not starting in a defensive position (see below)
				(store_add, ":slot", slot_team_d0_size, grc_infantry), #CABA - EDIT NEEDED????
				(team_get_slot, reg0, ":team_no", ":slot"),
				(try_begin),
					(this_or_next|eq, reg0, 0),
					(gt, ":distance_to_enemy", AI_long_range),
					(assign, ":move_archers", 1),
				(else_try),	#don't outstrip infantry when closing
					(call_script, "script_battlegroup_get_position", Infantry_Pos, ":team_no", grc_infantry), #CABA - POS EDIT
					(get_distance_between_positions, ":infantry_to_enemy", Infantry_Pos, Nearest_Enemy_Battlegroup_Pos),
					(val_sub, ":infantry_to_enemy", ":distance_to_enemy"),
					(le, ":infantry_to_enemy", 1500),
					(assign, ":move_archers", 1),
				(try_end),
			(try_end),
			
			(try_begin),
				(gt, ":move_archers", 0),
				(try_begin), #CABA - POS EDIT?
					(eq, ":team_no", 0),
					(assign, ":team_start_pos", Team0_Starting_Point),
				(else_try),
					(eq, ":team_no", 1),
					(assign, ":team_start_pos", Team1_Starting_Point),
				(else_try),
					(eq, ":team_no", 2),
					(assign, ":team_start_pos", Team2_Starting_Point),
				(else_try),
					(eq, ":team_no", 3),
					(assign, ":team_start_pos", Team3_Starting_Point),
				(try_end),

				(try_begin),
					(lt, ":decision_index", Hold_Point),	#outnumbered?
					(lt, "$battle_phase", BP_Fight),
					(store_div, ":distance_to_move", ":distance_to_enemy", 6),	#middle of rear third of battlefield
					(assign, ":hill_search_radius", ":distance_to_move"),

				(else_try),
					(assign, ":from_start_pos", 0),					
					(try_begin),
						(ge, "$battle_phase", BP_Fight),
						(assign, ":from_start_pos", 1),
					(else_try),
						(gt, "$battle_phase", BP_Setup),
						(call_script, "script_point_y_toward_position", ":team_start_pos", ":bg_pos"),
						(position_get_rotation_around_z, reg0, ":team_start_pos"),
						(position_get_rotation_around_z, reg1, ":bg_pos"),
						(val_sub, reg0, reg1),
						(neg|is_between, reg0, -45, 45),
						(assign, ":from_start_pos", 1),
					(try_end),
					
					(try_begin),
						(gt, ":from_start_pos", 0),
						(copy_position, ":bg_pos", ":team_start_pos"),
						(call_script, "script_point_y_toward_position", ":bg_pos", Enemy_Team_Pos),
						(call_script, "script_get_nearest_enemy_battlegroup_location", Nearest_Enemy_Battlegroup_Pos, ":team_no", ":bg_pos"),
						(assign, ":distance_to_enemy", reg0),
					(try_end),

					(try_begin),
						(eq, "$battle_phase", BP_Setup),
						(assign, ":shot_distance", AI_long_range),
					(else_try),
						(assign, ":shot_distance", AI_firing_distance),
						(store_sub, reg1, AI_firing_distance, AI_charge_distance),
						(val_sub, reg1, 200),	#subtract two meters to prevent automatically provoking melee from forward enemy infantry
						(store_add, ":slot", slot_team_d0_percent_throwers, ":bgroup"),
						(team_get_slot, reg0, ":team_no", ":slot"),
						(val_mul, reg1, reg0),
						(val_div, reg1, 100),
						(val_sub, ":shot_distance", reg1),
					(try_end),

					(store_sub, ":distance_to_move", ":distance_to_enemy", ":shot_distance"),
					(store_div, ":hill_search_radius", ":shot_distance", 3),	#limit so as not to run into enemy
					(try_begin),
						(lt, "$battle_phase", BP_Fight),
						(try_begin),
							(this_or_next|eq, "$battle_phase", BP_Setup),
							(lt, ":battle_presence", Advance_More_Point),	#expect to meet halfway?
							(val_div, ":distance_to_move", 2),
						(try_end),
					(try_end),
				(try_end),

				(position_move_y, ":bg_pos", ":distance_to_move", 0),
				(try_begin),
					(lt, "$battle_phase", BP_Fight),
					(copy_position, pos1, ":bg_pos"),
					(store_div, reg0, ":hill_search_radius", 100),
					(call_script, "script_find_high_ground_around_pos1_corrected", ":bg_pos", reg0),
				(try_end),
			(try_end),

			(team_get_movement_order, reg0, ":team_no", ":bgroup"),
			(try_begin),
				(neq, reg0, mordr_hold),
				(team_give_order, ":team_no", ":bgroup", mordr_hold),
			(try_end),
			(team_set_order_position, ":team_no", ":bgroup", ":bg_pos"),
		(try_end),
	(try_end)
	]),
															
	# script_team_field_melee_tactics by motomataru #EDITED FOR SLOTS BY CABA...many divisions changes necessary
	# Input: AI team, size relative to largest team in %, size relative to battle in %
	# Output: none
	("team_field_melee_tactics", [
	(store_script_param, ":team_no", 1),
#	(store_script_param, ":rel_army_size", 2),
	(store_script_param, ":battle_presence", 3),
	(call_script, "script_calculate_decision_numbers", ":team_no", ":battle_presence"),

	#mop up if outnumber enemies more than 6:1
	(try_begin),
		(gt, reg0, 86),
		(try_for_range, ":division", 0, 9),
				(store_add, ":slot", slot_team_d0_size, ":division"),
			(team_slot_ge, ":team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_type, ":division"),
				(neg|team_slot_eq, ":team_no", ":slot", sdt_archer),
			(neg|team_slot_eq, ":team_no", ":slot", sdt_skirmisher),
			(call_script, "script_formation_end", ":team_no", ":division"),
			(team_get_movement_order, reg0, ":team_no", ":division"),
			(try_begin),
				(neq, reg0, mordr_charge),
				(team_give_order, ":team_no", ":division", mordr_charge),
			(try_end),
		(try_end),

	(else_try),
		#find closest distance of enemy to infantry, cavalry troops
		(assign, ":inf_closest_dist", Far_Away),
		(assign, ":inf_closest_non_cav_dist", Far_Away),
		(assign, ":cav_closest_dist", Far_Away),
		(assign, ":num_enemies_in_melee", 0),
		(assign, ":num_enemies_supporting_melee", 0),
		(assign, ":num_enemy_infantry", 0),
		(assign, ":num_enemy_cavalry", 0),
		(assign, ":num_enemy_others", 0),
		(assign, ":sum_level_enemy_infantry", 0),
		(assign, ":x_enemy", 0),
		(assign, ":y_enemy", 0),
		(try_for_agents, ":enemy_agent"),
			(agent_is_alive, ":enemy_agent"),
			(agent_is_human, ":enemy_agent"),
			(agent_get_team, ":enemy_team_no", ":enemy_agent"),
			(teams_are_enemies, ":enemy_team_no", ":team_no"),
			(agent_slot_eq, ":enemy_agent", slot_agent_is_running_away, 0),
			(agent_get_class, ":enemy_class_no", ":enemy_agent"),
			(try_begin),
				(eq, ":enemy_class_no", grc_infantry),
				(val_add, ":num_enemy_infantry", 1),
				(agent_get_troop_id, ":enemy_troop", ":enemy_agent"),
				(store_character_level, ":enemy_level", ":enemy_troop"),
				(val_add, ":sum_level_enemy_infantry", ":enemy_level"),
			(else_try),
				(eq, ":enemy_class_no", grc_cavalry),
				(val_add, ":num_enemy_cavalry", 1),
			(else_try),
				(val_add, ":num_enemy_others", 1),
			(try_end),
			(agent_get_position, pos0, ":enemy_agent"),
			(position_get_x, ":value", pos0),
			(val_add, ":x_enemy", ":value"),
			(position_get_y, ":value", pos0),
			(val_add, ":y_enemy", ":value"),
			(assign, ":enemy_in_melee", 0),
			(assign, ":enemy_supporting_melee", 0),
			(try_for_agents, ":cur_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":cur_team_no", ":cur_agent"),
				(eq, ":cur_team_no", ":team_no"),
				(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
				(agent_get_class, ":cur_class_no", ":cur_agent"),
				(try_begin),
					(eq, ":cur_class_no", grc_infantry),
					(agent_get_position, pos1, ":cur_agent"),
					(get_distance_between_positions, ":distance_of_enemy", pos0, pos1),
					(try_begin),
						(gt, ":inf_closest_dist", ":distance_of_enemy"),
						(assign, ":inf_closest_dist", ":distance_of_enemy"),
						(copy_position, Nearest_Enemy_Troop_Pos, pos0),
						(assign, ":enemy_nearest_troop_distance", ":distance_of_enemy"),
						(assign, ":enemy_nearest_agent", ":enemy_agent"),
					(try_end),
					(try_begin),
						(neq, ":enemy_class_no", grc_cavalry),
						(gt, ":inf_closest_non_cav_dist", ":distance_of_enemy"),
						(assign, ":inf_closest_non_cav_dist", ":distance_of_enemy"),
						(copy_position, Nearest_Non_Cav_Enemy_Troop_Pos, pos0),
						(assign, ":enemy_nearest_non_cav_troop_distance", ":distance_of_enemy"),
						(assign, ":enemy_nearest_non_cav_agent", ":enemy_agent"),
					(try_end),
					(try_begin),
						(lt, ":distance_of_enemy", 150),
						(assign, ":enemy_in_melee", 1),
					(try_end),
					(try_begin),
						(lt, ":distance_of_enemy", 350),
						(assign, ":enemy_supporting_melee", 1),
					(try_end),
				(else_try),
					(eq, ":cur_class_no", grc_cavalry),
					(agent_get_position, pos1, ":cur_agent"),
					(get_distance_between_positions, ":distance_of_enemy", pos0, pos1),
					(try_begin),
						(gt, ":cav_closest_dist", ":distance_of_enemy"),
						(assign, ":cav_closest_dist", ":distance_of_enemy"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":enemy_in_melee", 1),
				(val_add, ":num_enemies_in_melee", 1),
			(try_end),
			(try_begin),
				(eq, ":enemy_supporting_melee", 1),
				(val_add, ":num_enemies_supporting_melee", 1),
			(try_end),
		(try_end), #IS THERE A WAY TO SIMPLIFY THESE NESTED AGENT LOOPS?
		
		(store_add, ":num_enemies", ":num_enemy_infantry", ":num_enemy_cavalry"),
		(val_add, ":num_enemies", ":num_enemy_others"),
		(gt, ":num_enemies", 0),
		#WHY NOT USING STORED DATA?
		(init_position, Enemy_Team_Pos),
		(val_div, ":x_enemy", ":num_enemies"),
		(position_set_x, Enemy_Team_Pos, ":x_enemy"),
		(val_div, ":y_enemy", ":num_enemies"),
		(position_set_y, Enemy_Team_Pos, ":y_enemy"),
		(position_set_z_to_ground_level, Enemy_Team_Pos),

		(store_add, ":slot", slot_team_d0_size, grc_archers),
		(team_get_slot, ":num_archers", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_archers", 0),
			(assign, ":enemy_from_archers", Far_Away),
			(assign, ":archer_order", mordr_charge),
		(else_try),
			(call_script, "script_battlegroup_get_position", Archers_Pos, ":team_no", grc_archers),
			(call_script, "script_point_y_toward_position", Archers_Pos, Enemy_Team_Pos),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Archers_Pos),
			(assign, ":enemy_from_archers", reg0),
			(team_get_movement_order, ":archer_order", ":team_no", grc_archers),
		(try_end),

		(store_add, ":slot", slot_team_d0_size, grc_infantry),
		(team_get_slot, ":num_infantry", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_infantry", 0),
			(assign, ":enemy_from_infantry", Far_Away),
		(else_try),
			(call_script, "script_battlegroup_get_position", Infantry_Pos, ":team_no", grc_infantry),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Infantry_Pos),
			(assign, ":enemy_from_infantry", reg0),
		(try_end),

		(store_add, ":slot", slot_team_d0_size, grc_cavalry),
		(team_get_slot, ":num_cavalry", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_cavalry", 0),
			(assign, ":enemy_from_cavalry", Far_Away),
		(else_try),
			(call_script, "script_battlegroup_get_position", Cavalry_Pos, ":team_no", grc_cavalry),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Cavalry_Pos),
			(assign, ":enemy_from_cavalry", reg0),
		(try_end),

		(try_begin),
			(lt, "$battle_phase", BP_Fight),
			(this_or_next|le, ":enemy_from_infantry", AI_charge_distance),
			(this_or_next|le, ":enemy_from_cavalry", AI_charge_distance),
			(le, ":enemy_from_archers", AI_charge_distance),
			(assign, "$battle_phase", BP_Fight),
		(else_try),
			(lt, "$battle_phase", BP_Jockey),
			(this_or_next|le, ":inf_closest_dist", AI_long_range),
			(le, ":cav_closest_dist", AI_long_range),
			(assign, "$battle_phase", BP_Jockey),
		(try_end),
		
		(team_get_leader, ":team_leader", ":team_no"),
		
		#infantry AI
		(assign, ":place_leader_by_infantry", 0),
		(try_begin),
			(le, ":num_infantry", 0),
			(assign, ":infantry_order", ":archer_order"),
			
			#deal with mounted heroes that team_give_order() treats as infantry   #CABA...could change their division?
			(team_get_movement_order, reg0, ":team_no", grc_infantry),
			(try_begin),
				(neq, reg0, ":infantry_order"),
				(team_give_order, ":team_no", grc_infantry, ":infantry_order"),
			(try_end),
			(try_begin),
				(gt, ":num_archers", 0),
				(copy_position, pos1, Archers_Pos),
				(position_move_y, pos1, 1000, 0),
				(team_set_order_position, ":team_no", grc_infantry, pos1),
			(else_try),
				(team_set_order_position, ":team_no", grc_infantry, Cavalry_Pos),
			(try_end),
		(else_try),
			(store_mul, ":percent_level_enemy_infantry", ":sum_level_enemy_infantry", 100),
			(val_div, ":percent_level_enemy_infantry", ":num_enemies"),
			(try_begin),
				(teams_are_enemies, ":team_no", "$fplayer_team_no"),
				(assign, ":combined_level", 0),
				(assign, ":combined_team_size", 0),
				(assign, ":combined_num_infantry", ":num_infantry"),
			(else_try),
				(store_add, ":slot", slot_team_d0_level, grc_infantry),
						(team_get_slot, ":combined_level", "$fplayer_team_no", ":slot"),
						(team_get_slot, ":combined_team_size", "$fplayer_team_no", slot_team_size),
				(store_add, ":slot", slot_team_d0_size, grc_infantry),
				(team_get_slot, ":combined_num_infantry", "$fplayer_team_no", ":slot"),
				(val_add, ":combined_num_infantry", ":num_infantry"),
			(try_end),
			(store_mul, ":percent_level_infantry", ":combined_num_infantry", 100),
			(store_add, ":slot", slot_team_d0_level, grc_infantry),
			(team_get_slot, ":level_infantry", ":team_no", ":slot"),
			(val_add, ":combined_level", ":level_infantry"),
			(val_mul, ":percent_level_infantry", ":combined_level"),
			(team_get_slot, reg0, ":team_no", slot_team_size),
			(val_add, ":combined_team_size", reg0),
			(val_div, ":percent_level_infantry", ":combined_team_size"),

			(assign, ":infantry_order", mordr_charge),
			(try_begin),	#enemy far away AND ranged not charging
				(gt, ":enemy_from_archers", AI_charge_distance),
				(gt, ":inf_closest_dist", AI_charge_distance),
				(neq, ":archer_order", mordr_charge),
				(try_begin),	#fighting not started OR not enough infantry
					(this_or_next|le, "$battle_phase", BP_Jockey),
					(lt, ":percent_level_infantry", ":percent_level_enemy_infantry"),
					(assign, ":infantry_order", mordr_hold),
				(try_end),
			(try_end),

			#if low level troops outnumber enemies in melee by 2:1, attempt to whelm
			(try_begin),
				(le, ":level_infantry", 12),
				(gt, ":num_enemies_in_melee", 0),
				(store_mul, reg0, ":num_enemies_supporting_melee", 2),
				(is_between, reg0, 1, ":num_infantry"),
				(get_distance_between_positions, reg0, Infantry_Pos, Nearest_Enemy_Troop_Pos),
				(le, reg0, AI_charge_distance),
				(call_script, "script_formation_end", ":team_no", grc_infantry),
				(team_get_movement_order, reg0, ":team_no", grc_infantry),
				(try_begin),
					(neq, reg0, mordr_charge),
					(team_give_order, ":team_no", grc_infantry, mordr_charge),
				(try_end),
				
			#else attempt to form formation somewhere
			(else_try),
					(team_get_slot, ":infantry_formation", ":team_no", slot_team_default_formation),
				(try_begin),
						(eq, ":infantry_formation", formation_default),
						(call_script, "script_get_default_formation", ":team_no"),
						(assign, ":infantry_formation", reg0),
						(team_set_slot, ":team_no", slot_team_default_formation, ":infantry_formation"),
				(try_end),
				
				(agent_get_division, ":enemy_nearest_troop_battlegroup", ":enemy_nearest_agent"),
				(agent_get_class, ":enemy_nearest_troop_class", ":enemy_nearest_agent"), 
				(agent_get_team, ":enemy_nearest_troop_team", ":enemy_nearest_agent"),
				(team_get_leader, ":enemy_leader", ":enemy_nearest_troop_team"),
				(store_mul, ":percent_enemy_cavalry", ":num_enemy_cavalry", 100),
				(val_div, ":percent_enemy_cavalry", ":num_enemies"),
				(try_begin),
					(neq, ":infantry_formation", formation_none),
					(try_begin),
						(gt, ":percent_enemy_cavalry", 66),
						(assign, ":infantry_formation", formation_square),
					(else_try),
						(neq, ":enemy_nearest_troop_class", grc_cavalry),
						(neq, ":enemy_nearest_troop_class", grc_archers),
						(neq, ":enemy_nearest_agent", ":enemy_leader"),
						(store_add, ":slot", slot_team_d0_size, ":enemy_nearest_troop_battlegroup"),
						(team_get_slot, reg0, ":enemy_nearest_troop_team", ":slot"),
						(gt, reg0, ":num_infantry"),	#got fewer troops?
						(store_add, ":slot", slot_team_d0_level, grc_infantry),
						(team_get_slot, ":average_level", ":team_no", ":slot"),
						(store_add, ":slot", slot_team_d0_level, ":enemy_nearest_troop_battlegroup"),
						(team_get_slot, reg0, ":enemy_nearest_troop_team", ":slot"),
						(gt, ":average_level", reg0),	#got better troops?
						(assign, ":infantry_formation", formation_wedge),
					(try_end),
				(try_end),
				
				#hold near archers?
				(try_begin),
					(eq, ":infantry_order", mordr_hold),
					(gt, ":num_archers", 0),
					(copy_position, pos1, Archers_Pos),
					(position_move_x, pos1, -100, 0),
					(try_begin),
						(this_or_next|eq, ":enemy_nearest_troop_battlegroup", grc_cavalry),
						(gt, ":percent_level_infantry", ":percent_level_enemy_infantry"),
						(position_move_y, pos1, 1000, 0),	#move ahead of archers in anticipation of charges
					(else_try),
						(position_move_y, pos1, -1000, 0),
					(try_end),
					(assign, ":spacing", 1),

				#advance to nearest (preferably unmounted) enemy
				(else_try),
					(assign, ":target_battlegroup", -1),
					(assign, ":target_size", 1),
					(try_begin),
						(eq, ":num_enemies_in_melee", 0),	#not engaged?
						(gt, ":enemy_from_archers", AI_charge_distance),
						(lt, ":percent_enemy_cavalry", 100),
						(assign, ":distance_to_enemy_troop", ":enemy_nearest_non_cav_troop_distance"),
						(copy_position, pos60, Nearest_Non_Cav_Enemy_Troop_Pos),
						(agent_get_team, ":enemy_non_cav_team", ":enemy_nearest_non_cav_agent"),
						(assign, ":target_team", ":enemy_non_cav_team"),
						(team_get_leader, reg0, ":enemy_non_cav_team"),
						(try_begin),
							(eq, ":enemy_nearest_non_cav_agent", reg0),
							(assign, ":distance_to_enemy_group", Far_Away),
						(else_try),
							(agent_get_division, ":target_battlegroup", ":enemy_nearest_non_cav_agent"),
							(call_script, "script_battlegroup_get_position", pos0, ":enemy_non_cav_team", ":target_battlegroup"),
							(get_distance_between_positions, ":distance_to_enemy_group", Infantry_Pos, pos0),
							(store_add, ":slot", slot_team_d0_size, ":target_battlegroup"),
							(team_get_slot, ":target_size", ":enemy_non_cav_team", ":slot"),
						(try_end),
					(else_try),
						(assign, ":distance_to_enemy_troop", ":enemy_nearest_troop_distance"),
						(copy_position, pos60, Nearest_Enemy_Troop_Pos),
						(assign, ":target_team", ":enemy_nearest_troop_team"),
						(try_begin),
							(eq, ":enemy_nearest_agent", ":enemy_leader"),
							(assign, ":distance_to_enemy_group", Far_Away),
						(else_try),
							(assign, ":target_battlegroup", ":enemy_nearest_troop_battlegroup"),
							(call_script, "script_battlegroup_get_position", pos0, ":enemy_nearest_troop_team", ":target_battlegroup"),
							(get_distance_between_positions, ":distance_to_enemy_group", Infantry_Pos, pos0),
							(store_add, ":slot", slot_team_d0_size, ":target_battlegroup"),
							(team_get_slot, ":target_size", ":enemy_nearest_troop_team", ":slot"),
						(try_end),
					(try_end),
					
					(store_sub, reg0, ":distance_to_enemy_group", ":distance_to_enemy_troop"),
					#attack troop if its unit is far off
					(try_begin),
						(gt, reg0, AI_charge_distance),
						(copy_position, pos0, pos60),
						(assign, ":distance_to_move", ":distance_to_enemy_troop"),
						
					#attack unit
					(else_try),
						(assign, ":distance_to_move", ":distance_to_enemy_group"),
						#wedge pushes through to last enemy infantry rank
						(try_begin),
							(eq, ":infantry_formation", formation_wedge),
							(val_sub, ":distance_to_move", formation_minimum_spacing),

						#non-wedge stops before first rank of enemy
						(else_try),
							(store_mul, reg0, formation_minimum_spacing, 1.5),
							(val_sub, ":distance_to_move", reg0),
							
							#back up for enemies in deep formation
							(eq, ":target_battlegroup", grc_infantry),
							(ge, ":target_size", formation_min_foot_troops),
							(try_begin),
								(neq, ":target_team", "$fplayer_team_no"),
								(val_sub, ":distance_to_move", formation_minimum_spacing),
							(else_try),
								(neg|team_slot_eq, "$fplayer_team_no", slot_team_d0_formation, formation_none),
								(val_sub, ":distance_to_move", formation_minimum_spacing),
							(try_end),
						(try_end),
					(try_end),

					#slow for formation appearance on approach
					(try_begin),
						(lt, ":num_infantry", formation_min_foot_troops),
						(assign, ":speed_adjust", 0),
					(else_try),
						(eq, ":infantry_formation", formation_square),
						(assign, reg0, ":num_infantry"),
						(convert_to_fixed_point, reg0),
						(store_sqrt, ":speed_adjust", reg0),
						(val_mul, ":speed_adjust", formation_minimum_spacing),
						(val_div, ":speed_adjust", 2),
						(convert_from_fixed_point, ":speed_adjust"),
					(else_try),
						(eq, ":infantry_formation", formation_wedge),
						(assign, reg0, ":num_infantry"),
						(convert_to_fixed_point, reg0),
						(store_sqrt, ":speed_adjust", reg0),
						(val_mul, ":speed_adjust", formation_minimum_spacing),
						(val_mul, ":speed_adjust", 2),
						(val_div, ":speed_adjust", 3),
						(convert_from_fixed_point, ":speed_adjust"),
					(else_try),
						(assign, ":speed_adjust", formation_minimum_spacing),
					(try_end),
					(try_begin),
						(le, ":distance_to_move", AI_charge_distance),
						(val_add, ":speed_adjust", 600),
					(else_try),
						(le, ":distance_to_move", AI_firing_distance),
						(val_add, ":speed_adjust", 1200),
					(else_try),
						(le, ":distance_to_move", AI_long_range),
						(val_add, ":speed_adjust", 1800),
					(try_end),
					(try_begin),
						(le, ":distance_to_move", AI_long_range),
						(val_min, ":distance_to_move", ":speed_adjust"),
					(try_end),

					#adjust position
					(copy_position, pos1, Infantry_Pos),
					(try_begin),
						(eq, ":num_enemies_in_melee", 0),
						(call_script, "script_point_y_toward_position", pos1, pos0),
						(position_move_y, pos1, ":distance_to_move"),
					(else_try),
						(call_script, "script_get_formation_position", pos2, ":team_no", grc_infantry),
						(position_copy_rotation, pos1, pos2),
						(position_move_y, pos1, -2000),
						(call_script, "script_point_y_toward_position", pos1, pos0),
						(position_move_y, pos1, 2000),
						(position_move_y, pos1, ":distance_to_move"),
					(try_end),
					(assign, ":spacing", 0),
				(try_end),

				(copy_position, pos61, pos1),
				(call_script, "script_get_centering_amount", ":infantry_formation", ":num_infantry", 0),
				(assign, ":centering", reg0),
				(try_begin),
					(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":infantry_formation"),
					(position_move_x, pos1, ":centering"),
					(call_script, "script_form_infantry", ":team_no", grc_infantry, ":team_leader", ":spacing", ":infantry_formation"),		
					(store_add, ":slot", slot_team_d0_formation, grc_infantry),
					(team_set_slot, ":team_no", ":slot", ":infantry_formation"),
					(assign, ":place_leader_by_infantry", 1),
				(else_try),
					(call_script, "script_formation_end", ":team_no", grc_infantry),
					(team_get_movement_order, reg0, ":team_no", grc_infantry),
					(try_begin),
						(neq, reg0, ":infantry_order"),
						(team_give_order, ":team_no", grc_infantry, ":infantry_order"),
					(try_end),
					(eq, ":infantry_order", mordr_hold),
					(assign, ":place_leader_by_infantry", 1),
				(try_end),
				(call_script, "script_set_formation_position", ":team_no", grc_infantry, pos61),
				(position_move_x, pos61, ":centering"),	#for possible leader positioning
			(try_end),
		(try_end),	
		
		#cavalry AI
		(try_begin),
			(gt, ":num_cavalry", 0),

			#get distance to nearest enemy battlegroup(s)
			(store_add, ":slot", slot_team_d0_level, grc_cavalry),
			(team_get_slot, ":average_level", ":team_no", ":slot"),
			(assign, ":nearest_threat_distance", Far_Away),
			(assign, ":nearest_target_distance", Far_Away),
			(assign, ":num_targets", 0),
			(try_for_range, ":enemy_team_no", 0, 4),
				(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
				(teams_are_enemies, ":enemy_team_no", ":team_no"),
				(try_for_range, ":enemy_battle_group", 0, 9),
					(store_add, ":slot", slot_team_d0_size, ":enemy_battle_group"),
					(team_get_slot, ":size_enemy_battle_group", ":enemy_team_no", ":slot"),
					(gt, ":size_enemy_battle_group", 0),
					(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_battle_group"),
					(get_distance_between_positions, ":distance_of_enemy", Cavalry_Pos, pos0),
					(try_begin),	#threat or target?
						(store_add, ":slot", slot_team_d0_weapon_length, ":enemy_battle_group"),
						(team_get_slot, reg0, ":enemy_team_no", ":slot"),
						(assign, ":decision_index", reg0),
						(store_add, ":slot", slot_team_d0_level, ":enemy_battle_group"),
						(team_get_slot, reg0, ":enemy_team_no", ":slot"),
						(val_mul, ":decision_index", reg0),
						(val_mul, ":decision_index", ":size_enemy_battle_group"),
						(val_div, ":decision_index", ":average_level"),
						(val_div, ":decision_index", ":num_cavalry"),
						(try_begin),
							(neq, ":enemy_battle_group", grc_cavalry),
							(val_div, ":decision_index", 2),	#double count cavalry vs. foot soldiers
						(try_end),
						(gt, ":decision_index", 100),
						(try_begin),
							(gt, ":nearest_threat_distance", ":distance_of_enemy"),
							(copy_position, Nearest_Threat_Pos, pos0),
							(assign, ":nearest_threat_distance", ":distance_of_enemy"),
						(try_end),
					(else_try),
						(val_add, ":num_targets", 1),
						(gt, ":nearest_target_distance", ":distance_of_enemy"),
						(copy_position, Nearest_Target_Pos, pos0),
						(assign, ":nearest_target_distance", ":distance_of_enemy"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":nearest_threat_distance", Far_Away),
				(assign, ":nearest_target_guarded", 0),
			(else_try),
				(eq, ":nearest_target_distance", Far_Away),
				(assign, ":nearest_target_guarded", 1),
			(else_try),
				(get_distance_between_positions, reg0, Nearest_Target_Pos, Nearest_Threat_Pos),
				(store_div, reg1, AI_charge_distance, 2),
				(try_begin),	#ignore target too close to threat
					(le, reg0, reg1),
					(assign, ":nearest_target_guarded", 1),
				(else_try),
					(assign, ":nearest_target_guarded", 0),
				(try_end),
			(try_end),

			(assign, ":cavalry_order", mordr_charge), ##CABA HERE
			(try_begin),
				(teams_are_enemies, ":team_no", 0),
				(neg|team_slot_ge, 1, slot_team_reinforcement_stage, AI_Max_Reinforcements),
				(neg|team_slot_eq, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
				(assign, ":cavalry_order", mordr_hold),
			(else_try),
				(teams_are_enemies, ":team_no", 1),
				(neg|team_slot_ge, 0, slot_team_reinforcement_stage, AI_Max_Reinforcements),
				(neg|team_slot_eq, 0, slot_team_reinforcement_stage, "$defender_reinforcement_stage"),
				(assign, ":cavalry_order", mordr_hold),
			(else_try),
				(neq, ":infantry_order", mordr_charge),
				(try_begin),
					(le, "$battle_phase", BP_Jockey),
					(assign, ":cavalry_order", mordr_hold),
				(else_try),
					(eq, ":nearest_target_distance", Far_Away),
					(try_begin),
						(eq, ":num_archers", 0),
						(assign, ":distance_to_archers", 0),
					(else_try),
						(get_distance_between_positions, ":distance_to_archers", Cavalry_Pos, Archers_Pos),
					(try_end),
					(try_begin),
						(this_or_next|gt, ":cav_closest_dist", AI_charge_distance),
						(gt, ":distance_to_archers", AI_charge_distance),
						(assign, ":cavalry_order", mordr_hold),
					(try_end),
				(try_end),
			(try_end),

			(try_begin),
				(eq, ":team_no", 0),
				(assign, ":cav_destination", Team0_Cavalry_Destination),
			(else_try),
				(eq, ":team_no", 1),
				(assign, ":cav_destination", Team1_Cavalry_Destination),
			(else_try),
				(eq, ":team_no", 2),
				(assign, ":cav_destination", Team2_Cavalry_Destination),
			(else_try),
				(eq, ":team_no", 3),
				(assign, ":cav_destination", Team3_Cavalry_Destination),
			(try_end),
			(store_add, ":slot", slot_team_d0_percent_ranged, grc_cavalry),
			(team_get_slot, reg0, ":team_no", ":slot"),
			
			#horse archers don't use wedge
			(try_begin),
				(ge, reg0, 50),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(try_begin),
					(eq, ":num_archers", 0),
					(team_get_movement_order, reg0, ":team_no", grc_cavalry),
					(try_begin),
						(neq, reg0, mordr_charge),
						(team_give_order, ":team_no", grc_cavalry, mordr_charge),
					(try_end),
				(else_try),
					(team_get_movement_order, reg0, ":team_no", grc_cavalry),
					(try_begin),
						(neq, reg0, ":cavalry_order"),
						(team_give_order, ":team_no", grc_cavalry, ":cavalry_order"),
					(try_end),
					(copy_position, ":cav_destination", Archers_Pos),
					(position_move_y, ":cav_destination", -500, 0),
					(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				(try_end),
				
			#close in with no unguarded target farther off, free fight
			(else_try),
				(eq, ":cavalry_order", mordr_charge),
				(le, ":cav_closest_dist", AI_charge_distance),
				(try_begin),
					(eq, ":num_targets", 1),
					(eq, ":nearest_target_guarded", 0),
					(gt, ":nearest_target_distance", ":nearest_threat_distance"),
					(assign, reg0, 0),
				(else_try),
					(ge, ":num_targets", 2),
					(eq, ":nearest_target_guarded", 1),
					(assign, reg0, 0),
				(else_try),
					(assign, reg0, 1),
				(try_end),
				(eq, reg0, 1),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(team_get_movement_order, reg0, ":team_no", grc_cavalry),
				(try_begin),
					(neq, reg0, mordr_charge),
					(team_give_order, ":team_no", grc_cavalry, mordr_charge),
				(try_end),

			#grand charge if target closer than threat AND not guarded
			(else_try),
				(lt, ":nearest_target_distance", ":nearest_threat_distance"),
				(eq, ":nearest_target_guarded", 0),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(team_get_movement_order, reg0, ":team_no", grc_cavalry),
				(try_begin),
					(neq, reg0, mordr_hold),
					(team_give_order, ":team_no", grc_cavalry, mordr_hold),
				(try_end),
				
				#lead archers up to firing point
				(try_begin),
					(gt, ":nearest_target_distance", AI_firing_distance),
					(eq, ":cavalry_order", mordr_hold),
					(try_begin),
						(eq, ":num_archers", 0),
						(copy_position, ":cav_destination", Cavalry_Pos),	#must be reinforcements, so gather at average position
					(else_try),						
						(copy_position, ":cav_destination", Archers_Pos),
						(position_move_y, ":cav_destination", AI_charge_distance, 0),
					(try_end),
					
				#then CHARRRRGE!
				(else_try),
					(copy_position, ":cav_destination", Cavalry_Pos),
					(call_script, "script_point_y_toward_position", ":cav_destination", Nearest_Target_Pos),
					(position_move_y, ":cav_destination", ":nearest_target_distance", 0),
				(try_end),
				(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				
			#make a wedge somewhere
			(else_try),
				(try_begin),
					(eq, ":cavalry_order", mordr_charge),
					(neq, ":nearest_target_distance", Far_Away),
					(copy_position, ":cav_destination", Cavalry_Pos),
					(call_script, "script_point_y_toward_position", ":cav_destination", Nearest_Target_Pos),
					(position_move_y, ":cav_destination", ":nearest_target_distance", 0),
					(position_move_y, ":cav_destination", AI_charge_distance, 0),	#charge on through to the other side
				(else_try),
					(neq, ":cavalry_order", mordr_charge),
					(eq, ":num_archers", 0),
					(copy_position, ":cav_destination", Cavalry_Pos),	#must be reinforcements, so gather at average position
				(else_try),
					(copy_position, ":cav_destination", Archers_Pos),	#hold near archers
					(position_move_x, ":cav_destination", 500, 0),
					(position_move_y, ":cav_destination", -1000, 0),
				(try_end),
				
				#move around threat in the way to destination
				(try_begin),
					(neq, ":nearest_threat_distance", Far_Away),
					(call_script, "script_point_y_toward_position", Cavalry_Pos, Nearest_Threat_Pos),
					(call_script, "script_point_y_toward_position", Nearest_Threat_Pos, ":cav_destination"),
					(position_get_rotation_around_z, reg0, Cavalry_Pos),
					(position_get_rotation_around_z, reg1, Nearest_Threat_Pos),
					(store_sub, ":rotation_diff", reg0, reg1),
					(try_begin),
						(lt, ":rotation_diff", -180),
						(val_add, ":rotation_diff", 360),
					(else_try),
						(gt, ":rotation_diff", 180),
						(val_sub, ":rotation_diff", 360),
					(try_end),
					
					(try_begin),
						(is_between, ":rotation_diff", -135, 136),
						(copy_position, ":cav_destination", Cavalry_Pos),
						(assign, ":distance_to_move", AI_firing_distance),
						(try_begin),	#target is left of threat
							(is_between, ":rotation_diff", -135, 0),
							(val_mul, ":distance_to_move", -1),
						(try_end),
						(position_move_x, ":cav_destination", ":distance_to_move", 0),
						(store_sub, ":distance_to_move", ":nearest_threat_distance", AI_firing_distance),
						(position_move_y, ":cav_destination", ":distance_to_move", 0),
						(call_script, "script_point_y_toward_position", ":cav_destination", Cavalry_Pos),
						(position_rotate_z, ":cav_destination", 180),
					(try_end),
				(try_end),
				(get_scene_boundaries, pos0, pos1),
				(position_get_x, reg0, ":cav_destination"),
				(position_get_x, reg1, pos0),
				(val_max, reg0, reg1),
				(position_get_x, reg1, pos1),
				(val_min, reg0, reg1),
				(position_set_x, ":cav_destination", reg0),
				(position_get_y, reg0, ":cav_destination"),
				(position_get_y, reg1, pos0),
				(val_max, reg0, reg1),
				(position_get_y, reg1, pos1),
				(val_min, reg0, reg1),
				(position_set_y, ":cav_destination", reg0),
				(position_set_z_to_ground_level, ":cav_destination"),
				
				(try_begin),
					(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
					(copy_position, pos1, ":cav_destination"),
					(call_script, "script_form_cavalry", ":team_no", grc_cavalry, ":team_leader", 0),
					(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
					(team_set_slot, ":team_no", ":slot", formation_wedge),
					# (team_give_order, ":team_no", grc_cavalry, mordr_hold),
				(else_try),
					(call_script, "script_formation_end", ":team_no", grc_cavalry),
					(team_get_movement_order, reg0, ":team_no", grc_cavalry),
					(try_begin),
						(neq, reg0, ":cavalry_order"),
						(team_give_order, ":team_no", grc_cavalry, ":cavalry_order"),
					(try_end),
				(try_end),
				(call_script, "script_set_formation_position", ":team_no", grc_cavalry, ":cav_destination"),
			(try_end),
		(try_end),

		#place leader
		(try_begin),
			(ge, ":team_leader", 0),
			(agent_is_alive, ":team_leader"),
			(try_begin),
				(le, ":num_infantry", 0),
				(try_begin),
					(eq, ":archer_order", mordr_charge),
					(agent_clear_scripted_mode, ":team_leader"),
				(else_try),
					(copy_position, pos1, Archers_Pos),
					(position_move_y, pos1, -1000, 0),
					(agent_set_scripted_destination, ":team_leader", pos1, 1),
				(try_end),
			(else_try),
				(neq, ":place_leader_by_infantry", 0),
				(agent_slot_eq, ":team_leader", slot_agent_is_running_away, 0),
				(position_move_x, pos61, 100, 0),
				(agent_set_scripted_destination, ":team_leader", pos61, 1),
			(else_try),
				(agent_clear_scripted_mode, ":team_leader"),
			(try_end),
		(try_end),
	(try_end)
	]),
					
								
	# script_field_tactics by motomataru
	# Input: flag 1 to include ranged
	# Output: none
	("field_tactics", [
	(store_script_param, ":include_ranged", 1),
	
	(assign, ":largest_team_size", 0),
	(assign, ":num_teams", 0),
	(assign, ":battle_size", 0),
	(try_for_range, ":team_no", 0, 4),
			(team_get_slot, ":team_size", ":team_no", slot_team_size),
		(gt, ":team_size", 0),
			(team_get_slot, ":team_cav_size", ":team_no", slot_team_num_cavalry),
		(store_add, ":team_adj_size", ":team_size", ":team_cav_size"),	#double count cavalry to capture effect on battlefield
		(val_add, ":num_teams", 1),		
		(val_add, ":battle_size", ":team_adj_size"),
		
		#tom
		(try_begin),
				(neq, ":team_no", "$fplayer_team_no"),
			(neg|teams_are_enemies, ":team_no", "$fplayer_team_no"),
				(team_get_slot, ":player_team_adj_size", "$fplayer_team_no", slot_team_adj_size),
			(val_add, ":team_adj_size", ":player_team_adj_size"),	#ally team takes player team into account
		(try_end),
		#tom
		(team_set_slot, ":team_no", slot_team_adj_size, ":team_adj_size"),
		
			(lt, ":largest_team_size", ":team_adj_size"),
		(assign, ":largest_team_size", ":team_adj_size"),
	(try_end),

	#apply tactics to every AI team
		(set_show_messages, 0),
	#(try_for_range, ":ai_team", 0, ":num_teams"), #tom
	(try_for_range, ":ai_team", 0, 4),
		(team_get_slot, ":ai_team_size", ":ai_team", slot_team_adj_size),
		(gt, ":ai_team_size", 0),
		
		(assign, ":do_it", 0),
		(try_begin),
			(neq, ":ai_team", "$fplayer_team_no"),
			(assign, ":do_it", 1),
		(else_try),
			(main_hero_fallen),    #have AI take over for mods with post-player battle action
			(eq, "$enable_deahtcam", 1),
			(eq, AI_Replace_Dead_Player, 1),
			(assign, ":do_it", 1),
		(try_end),
		(eq, ":do_it", 1),
		
		(team_get_slot, ":ai_faction", ":ai_team", slot_team_faction),
		(try_begin),
			(this_or_next|eq, AI_for_kingdoms_only, 0),
			(this_or_next|eq, ":ai_faction", fac_deserters),	#deserters have military training
			(is_between, ":ai_faction", fac_kingdom_1, fac_kingdoms_end),
			(val_mul, ":ai_team_size", 100),
			(store_div, ":team_percentage", ":ai_team_size", ":largest_team_size"),
			(store_div, ":team_battle_presence", ":ai_team_size", ":battle_size"),
			(try_begin),
				(eq, ":include_ranged", 1),
				(call_script, "script_team_field_ranged_tactics", ":ai_team", ":team_percentage", ":team_battle_presence"),
			(try_end),
			(call_script, "script_team_field_melee_tactics", ":ai_team", ":team_percentage", ":team_battle_presence"),
		(try_end),
	(try_end),
		(set_show_messages, 1),

	(try_begin),
		(eq, ":include_ranged", 1), 	  
		(assign, "$prev_casualties", "$cur_casualties"),
	(try_end)
	]),

		
		
	# script_find_high_ground_around_pos1_corrected by motomataru
	# Input:	arg1: destination position
	#			arg2: search_radius (in meters)
	#			pos1 should hold center_position_no
	# Output:	destination contains highest ground within a <search_radius> meter square around pos1
	# Also uses position registers: pos0
	("find_high_ground_around_pos1_corrected", [
	(store_script_param, ":destination_pos", 1),
	(store_script_param, ":search_radius", 2),
	(assign, ":fixed_point_multiplier", 1),
	(convert_to_fixed_point, ":fixed_point_multiplier"),
	(set_fixed_point_multiplier, 1),
	
	(position_get_x, ":o_x", pos1),
	(position_get_y, ":o_y", pos1),
	(store_sub, ":min_x", ":o_x", ":search_radius"),
	(store_sub, ":min_y", ":o_y", ":search_radius"),
	(store_add, ":max_x", ":o_x", ":search_radius"),
	(store_add, ":max_y", ":o_y", ":search_radius"),
	
	(get_scene_boundaries, ":destination_pos", pos0),
	(position_get_x, ":scene_min_x", ":destination_pos"),
	(position_get_x, ":scene_max_x", pos0),
	(position_get_y, ":scene_min_y", ":destination_pos"),
	(position_get_y, ":scene_max_y", pos0),
	(val_max, ":min_x", ":scene_min_x"),
	(val_max, ":min_y", ":scene_min_y"),
	(val_min, ":max_x", ":scene_max_x"),
	(val_min, ":max_y", ":scene_max_y"),

	(assign, ":highest_pos_z", -100),
	(copy_position, ":destination_pos", pos1),
	(init_position, pos0),

	(try_for_range, ":i_x", ":min_x", ":max_x"),
		(try_for_range, ":i_y", ":min_y", ":max_y"),
			(position_set_x, pos0, ":i_x"),
			(position_set_y, pos0, ":i_y"),
			(position_set_z_to_ground_level, pos0),
			(position_get_z, ":cur_pos_z", pos0),
			(try_begin),
				(gt, ":cur_pos_z", ":highest_pos_z"),
				(copy_position, ":destination_pos", pos0),
				(assign, ":highest_pos_z", ":cur_pos_z"),
			(try_end),
		(try_end),
	(try_end),
	
	(set_fixed_point_multiplier, ":fixed_point_multiplier"),
	]),
		
		
	# script_cf_count_casualties by motomataru
	# Input: none
	# Output: evalates T/F, reg0 num casualties
	("cf_count_casualties", [
		(assign, ":num_casualties", 0),
	(try_for_agents,":cur_agent"),
			(try_begin),
			(this_or_next|agent_is_wounded, ":cur_agent"),
			(this_or_next|agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 1),
			(neg|agent_is_alive, ":cur_agent"),
			(val_add, ":num_casualties", 1),
		(try_end),
	(try_end),
	(assign, reg0, ":num_casualties"),
	(gt, ":num_casualties", 0)
	]),
	
		
	# script_battlegroup_get_position by motomataru #CABA - EDITED TO USE SLOTS, NOT STORED POS NUMBERS
#MOTO need rotation?
	# Input: destination position, team, battle group (troop class)
	# Output:	battle group position
	#			average team position if "troop class" input NOT set to 0-8
	# NB: Assumes that battle groups beyond 2 are PLAYER team
	# Positions 24-45 reserved (!)  NOW none are reserved...all calculated with slots
	("battlegroup_get_position", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":bgteam", 2),
	(store_script_param, ":bgroup", 3),
	
	(assign, ":x", 0),
	(assign, ":y", 0),
	(init_position, ":bgposition"),
	(try_begin),
		(neg|is_between, ":bgroup", 0, 9),
		(team_slot_ge, ":bgteam", slot_team_size, 1),
		(team_get_slot, ":x", ":bgteam", slot_team_avg_x),
		(team_get_slot, ":y", ":bgteam", slot_team_avg_y),
	(else_try),
		(is_between, ":bgroup", 0, 9),
		(store_add, ":slot", slot_team_d0_size, ":bgroup"),
		(team_slot_ge, ":bgteam", ":slot", 1),
		
		(store_add, ":slot", slot_team_d0_x, ":bgroup"),
		(team_get_slot, ":x", ":bgteam", ":slot"),
		
		(store_add, ":slot", slot_team_d0_y, ":bgroup"),
		(team_get_slot, ":y", ":bgteam", ":slot"),
	(try_end),
	(position_set_x, ":bgposition", ":x"),
	(position_set_y, ":bgposition", ":y"),
	(position_set_z_to_ground_level, ":bgposition"),
	]),	
		
	# script_get_nearest_enemy_battlegroup_location by motomataru
	# Input: destination position, fron team, from position
	# Output:	destination position, reg0 with distance
	# Run script_store_battlegroup_data before calling!
	("get_nearest_enemy_battlegroup_location", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":from_pos", 3),
	(assign, ":distance_to_nearest_enemy_battlegoup", Far_Away),
	(try_for_range, ":enemy_team_no", 0, 4),
		(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
		(teams_are_enemies, ":enemy_team_no", ":team_no"),
		(try_for_range, ":enemy_battle_group", 0, 9),
			(store_add, ":slot", slot_team_d0_size, ":enemy_battle_group"),
			(team_slot_ge, ":enemy_team_no", ":slot", 1),
			(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_battle_group"),
			(get_distance_between_positions, reg0, pos0, ":from_pos"),
			(try_begin),
				(gt, ":distance_to_nearest_enemy_battlegoup", reg0),
				(assign, ":distance_to_nearest_enemy_battlegoup", reg0),
				(copy_position, ":bgposition", pos0),
			(try_end),
		(try_end),
	(try_end),
	(assign, reg0, ":distance_to_nearest_enemy_battlegoup")
	]),
		
# # Line added to clear scripted mode right before each (agent_start_running_away, ":cur_agent")
	# script_decide_run_away_or_not
	# Input: none
	# Output: none
	("decide_run_away_or_not",
		[
			(store_script_param, ":cur_agent", 1),
			(store_script_param, ":mission_time", 2),
			
			(assign, ":force_retreat", 0),
			(agent_get_team, ":agent_team", ":cur_agent"),
			(agent_get_division, ":agent_division", ":cur_agent"),
			(try_begin),
				(lt, ":agent_division", 9), #static classes
				(team_get_movement_order, ":agent_movement_order", ":agent_team", ":agent_division"),
				(eq, ":agent_movement_order", mordr_retreat),
				(assign, ":force_retreat", 1),
			(try_end),

			(agent_get_slot, ":is_cur_agent_running_away", ":cur_agent", slot_agent_is_running_away),
			(try_begin),
				(eq, ":is_cur_agent_running_away", 0),
				(try_begin),
					(eq, ":force_retreat", 1),
					(agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
					(agent_start_running_away, ":cur_agent"),
					(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
				(else_try),
					(ge, ":mission_time", 45), #first 45 seconds anyone does not run away whatever happens.
					(agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
					(store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
					(val_mul, ":agent_hit_points", 4),
					(try_begin),
						(agent_is_ally, ":cur_agent"),
						(val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
					(try_end),
					(val_mul, ":agent_hit_points", 10),
					(store_sub, ":start_running_away_courage_score_limit", 3500, ":agent_hit_points"), 
					(lt, ":agent_courage_score", ":start_running_away_courage_score_limit"), #if (courage score < 3500 - (agent hit points * 40)) and (agent is not running away) then start running away, average hit points : 50, average running away limit = 1500

					(agent_get_troop_id, ":troop_id", ":cur_agent"), #for now do not let heroes to run away from battle
					(neg|troop_is_hero, ":troop_id"),
																
					(agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
					(agent_start_running_away, ":cur_agent"),
					(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
				(try_end),
			(else_try),
				(neq, ":force_retreat", 1),
				(agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
				(store_agent_hit_points, ":agent_hit_points", ":cur_agent"),      
				(val_mul, ":agent_hit_points", 4),
				(try_begin),
					(agent_is_ally, ":cur_agent"),
					(val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
				(try_end),
				(val_mul, ":agent_hit_points", 10),
				(store_sub, ":stop_running_away_courage_score_limit", 3700, ":agent_hit_points"), 
				(ge, ":agent_courage_score", ":stop_running_away_courage_score_limit"), #if (courage score > 3700 - agent hit points) and (agent is running away) then stop running away, average hit points : 50, average running away limit = 1700
				(agent_stop_running_away, ":cur_agent"),
				(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
			(try_end),      
	]), #ozan
		
		("tom_process_player_enterprise",
			[
			(store_script_param, ":enterprise_product", 1),
			(store_script_param, ":enterprise_center", 2),
			(store_script_param, ":future_cost", 3),
			
			(assign, ":enterprise_penalty", ":future_cost"),
			
			(try_for_range, ":center_no", centers_begin, centers_end),
				(party_get_slot, ":item_produced", ":center_no", slot_center_player_enterprise),
				(eq, ":item_produced", ":enterprise_product"),
				(val_add, ":enterprise_penalty", 1),
			(try_end),
			
			#(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
			(try_begin),
				(eq, "$tom_difficulty_enterprise", 0), #hard (1x or 2x reinforcing)
				(assign, ":precent", 25),
			(else_try),
				(eq, "$tom_difficulty_enterprise", 1), #moderate (1x reinforcing)
				(assign, ":precent", 20),
			(else_try),
				(eq, "$tom_difficulty_enterprise", 2), #easy (none or 1x reinforcing)
				(assign, ":precent", 15),
			(try_end),
			
			#reduce the penalty with trade skill
			(store_skill_level, ":cur_trade", "skl_trade", "trp_player"),
			(val_sub, ":precent", ":cur_trade"),
			
			(call_script, "script_process_player_enterprise", ":enterprise_product", ":enterprise_center"),
			(assign, ":penalty_total", 0),
			(assign, ":penalty", reg0),
			(try_for_range, reg1, 0, ":enterprise_penalty"),
				(store_sub, ":penalty", reg0, ":penalty_total"),
				(val_mul, ":penalty", ":precent"),
				(val_div, ":penalty", 100),
				(val_abs, ":penalty"),
				(val_add, ":penalty_total", ":penalty"),
			(try_end),
			
			(val_sub, reg0, ":penalty_total"),
			]
		),
		
		#tom old and unused
		# ("raf_set_ai_recalculation_flags",
		# [
		# (store_script_param, ":faction", 1),
		
		# (try_begin),
		# (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
		# (str_store_faction_name, s21, ":faction"),
		# #(display_message, "@setting {s21} for recalculation"),
		
		# (faction_set_slot, ":faction", slot_faction_recalculate_ai, 1),
		# (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
		# (faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
		# (store_relation, ":rel", ":faction", ":kingdom"),
		# (lt, ":rel", 0),
		# (faction_set_slot, ":kingdom", slot_faction_recalculate_ai, 1),
		# (try_end),
		# (try_end),
		
		
		# (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
		# (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
		
		# (call_script, "script_distance_between_factions", ":faction", ":cur_kingdom"),
		# (le, reg0, max_war_distance - 20),
		# (faction_set_slot, ":cur_kingdom", slot_faction_recalculate_ai, 1),
		# (try_end),
		#   ]
		# ),
		
		# script_process_alarms
		# Input: none
		# Output: none
		#called from triggers
		("raf_process_alarm",
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
			
		]),
		
		("game_get_troop_wage",
			[
			(store_script_param, ":troop_id", 1),
			(store_script_param_2, ":party_id"), #party id
			
			#TOM
			(assign, ":value", 0), #the thing to compare to others
			# (assign, ":value2", 0), #the thing to compare to others
			# (assign, ":meele", 0),
			# (assign, ":range", 0),
			# (assign, ":ammo", 0),
			(assign, ":head", 0),
			(assign, ":body", 0),
			(assign, ":foot", 0),
			# (assign, ":hand", 0),
			# (assign, ":shield", 0),
			(assign, ":mount", 1), #NO NEED?
			(try_begin),
				(neg|troop_is_hero, ":troop_id"),
				(troop_get_inventory_capacity,":cap",":troop_id"),
				(try_for_range, ":inventory", 0, ":cap"), #lets get troop inventory capacity
				(troop_get_inventory_slot,":item",":troop_id",":inventory"), #lets get it's item
				(gt, ":item", 0), #it's not nothing
				(item_get_type, ":item_type", ":item"), #lets get it type
				(try_begin), #meele weapon
					# (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
					# (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
					# (eq, ":item_type", itp_type_polearm),
					# (item_get_slot, ":value", ":item", slot_item_thrust_damage),
					# (item_get_slot, ":value2", ":item", slot_item_swing_damage),
					# (val_add, ":value", ":value2"),
					# (gt, ":value", ":meele"),
					# (assign, ":meele", ":value"),
					# (else_try), #range
					# (this_or_next|eq, ":item_type", itp_type_bow),
					# (this_or_next|eq, ":item_type", itp_type_crossbow),
					# (eq, ":item_type", itp_type_thrown),
					# (item_get_slot, ":value", ":item", slot_item_thrust_damage),
					# (item_get_slot, ":value2", ":item", slot_item_swing_damage),
					# (val_add, ":value", ":value2"),
					# (gt, ":value", ":meele"),
					# (assign, ":meele", ":value"),
					# (else_try), #ammo
					# (this_or_next|eq, ":item_type", itp_type_arrows),
					# (eq, ":item_type", itp_type_bolts),
					# (item_get_slot, ":value", ":item", slot_item_thrust_damage),
					# (item_get_slot, ":value2", ":item", slot_item_swing_damage),
					# (val_add, ":value", ":value2"),
					# (gt, ":value", ":ammo"),
					# (assign, ":ammo", ":value"),
					#(else_try), #shield
					#(eq, ":item_type", itp_type_shield),
					#(item_get_slot, ":value", ":item", slot_item_body_armor), #no idea which
					# (item_get_slot, ":value2", ":item", slot_item_head_armor), #should give the proper value
					#(val_add, ":value", ":value2"),
					#(item_get_slot, ":value2", ":item", slot_item_leg_armor), #so lets check them all
					#(val_add, ":value", ":value2"),
					#(gt, ":value", ":shield"),
					#(assign, ":shield", ":value"),
					#(else_try), #head armor
					(eq, ":item_type", itp_type_head_armor),
					(item_get_slot, ":value", ":item", slot_item_head_armor),
					(gt, ":value", ":head"),
					(assign, ":head", ":value"),
				(else_try), #body armor
					(eq, ":item_type", itp_type_body_armor),
					(item_get_slot, ":value", ":item", slot_item_body_armor),
					(gt, ":value", ":body"),
					(assign, ":body", ":value"),
				(else_try), #foot armor
					(eq, ":item_type", itp_type_foot_armor),
					(item_get_slot, ":value", ":item", slot_item_leg_armor),
					(gt, ":value", ":foot"),
					(assign, ":foot", ":value"),
					# (else_try), #hand armor
					# (eq, ":item_type", itp_type_hand_armor),
					# (item_get_slot, ":value", ":item", slot_item_body_armor), #presume it's this?
					# (gt, ":value", ":hand"),
					# (assign, ":hand", ":value"),
				(else_try),
					(eq, ":item_type", itp_type_horse),
					(assign, ":mount", 2),
				(try_end),
				(try_end),
				#(store_add, ":offense", ":meele", ":range"),
				#(val_add, ":offense", ":ammo"),
				#(store_add, ":defense", ":head", ":body"),
				#(val_add, ":defense", ":shield"),
				#(val_add, ":defense", ":foot"),
				#(val_add, ":defense", ":hand"),
				#(assign, ":offense", 0),
				#(val_mul, ":defense", ":mount"),
				#(store_add, ":wage", ":offense", ":defense"),
				(store_add, ":wage", ":head", ":body"),
				(val_div, ":wage", 4),
				#(val_mul, ":wage", 2),
				
				
				(try_begin),
				(store_character_level,":troop_lvl",":troop_id"),
				(neg|ge, ":troop_lvl", 6),
				#(val_mul, ":wage", 3),
				(val_div, ":wage", 3),
				(val_mul, ":wage", 2),
				(else_try),
				(val_sub, ":wage", 3),
				(try_end),
				
				(try_begin),
				#(else_try),
				(store_character_level,":troop_lvl",":troop_id"),
				(ge, ":troop_lvl", 19),
				(val_add, ":wage", 3),
				(val_mul, ":wage", 2),
				
				(try_begin),
					(ge, ":troop_lvl", 30),
					(val_add, ":wage", 210), #60
				(else_try),
					(ge, ":troop_lvl", 27),
					(val_add, ":wage", 110), #30
				(else_try),
					(ge, ":troop_lvl", 24),
					(val_add, ":wage", 10),
					#(else_try),
					
					#(val_div, ":wage", 2),
				(try_end),
				(try_end),
				(try_begin),
				(eq, ":mount", 2),
				(val_mul, ":wage", 5), #5
				(val_div, ":wage", 4), #4
				(try_end),
			(try_end),
			#(val_max, ":wage", 8),
			#TOM
			
			#TOM - this was original
			# (try_begin),
			# (neg|troop_is_hero, ":troop_id"),
			# (troop_get_slot, ":offense", ":troop_id", kt_slot_troop_o_val),
			# (troop_get_slot, ":defense", ":troop_id", kt_slot_troop_d_val),
			# (store_add, ":wage", ":offense", ":defense"),
			# (try_end),
			#TOM
			
			(try_begin),
				(is_between, ":troop_id", companions_begin, companions_end),
				(store_character_level, ":level", ":troop_id"),
				(store_mul, ":offense", ":level", 3),
				(val_add, ":offense", 50),
				(store_mul, ":defense", ":level", 2),
				(val_add, ":defense", 20),
				(store_add, ":wage", ":offense", ":defense"),
				
				(val_div, ":wage", 2),
				
				(val_max, ":wage", 1),
				(val_sub, ":wage", 31),
				(val_max, ":wage", 1),
				(store_mul, reg0, ":wage", ":wage"),
				
				(assign, ":wage", reg0),
				
				(val_div, ":wage", 200),
				
				(try_begin),
				(lt, ":wage", 80),
				(val_mul, ":wage", 3),
				(try_end),
				
				(val_mul, ":wage", 2),
				(val_div, ":wage", 3),
				
			(try_end),
			
			(party_get_template_id, ":template", ":party_id"),
			#tom
			##this one for lance system - player only
			#troop upkeep whitout a fief is super low
			(try_begin),
				(eq, "$use_feudal_lance", 1),
				(this_or_next|gt, "$g_player_crusading", 0),  
				(eq, "$use_feudal_lance", 1), #intented double check
				(eq, ":template", "p_main_party"),
				(assign, ":reduce", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(assign, ":reduce", 1),
				(assign, ":center_no", -1),
				(try_end),
				(eq, ":reduce", 0),
				(val_mul, ":wage", 2),
				(val_div, ":wage", 3),
				
				(val_max, ":wage", 3),
			(else_try), #in times of peace, as a lord - increase upkeep.
				(eq, "$use_feudal_lance", 1),
				(this_or_next|gt, "$g_player_crusading", 0),  
				(eq, "$use_feudal_lance", 1), #intented double check
				(eq, ":template", "p_main_party"),
				(assign, ":lord", 0),
				(try_for_range, ":center_no", centers_begin, centers_end),
					(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
					(assign, ":lord", 1),
				(store_faction_of_party, ":faction", ":center_no"),
				(assign, ":center_no", -1),
				(try_end),
				(eq, ":lord", 1),
				(call_script, "script_check_if_faction_is_at_war", ":faction"),
				(eq, reg0, 0), #at peace
				(val_mul, ":wage", 3),
				(val_div, ":wage", 2),
			(try_end),
			#tom end
			#tom
			#(game_get_reduce_campaign_ai, ":reduce_campaign_ai"), mod options now
			 
				
			(try_begin), #player only
				(this_or_next|eq, ":party_id", "p_main_party"),
				(eq, ":template", "pt_merc_party"),
				(try_begin),
				(eq, "$tom_difficulty_wages", 0), #hard (1x or 2x reinforcing)
				(val_mul, ":wage", 3),
				(val_div, ":wage", 2),
				(else_try),
				(eq, "$tom_difficulty_wages", 1), #moderate (1x reinforcing)
				(else_try),
				(eq, "$tom_difficulty_wages", 2), #easy (none or 1x reinforcing)
				(val_div, ":wage", 2),
				(try_end),
				(val_max, ":wage", 3),
			(try_end),
			
			
			
			# (val_div, ":wage", 2),
			
			# (val_max, ":wage", 1),
			# (val_sub, ":wage", 31),
			# (val_max, ":wage", 1),
			# (store_mul, reg0, ":wage", ":wage"),
			
			# (assign, ":wage", reg0),
			
			# (val_div, ":wage", 200),
			
			# (try_begin),
			# (lt, ":wage", 80),
			# (val_mul, ":wage", 3),
			# (try_end),
			
			# (val_mul, ":wage", 2),
			# (val_div, ":wage", 3),
			
			(try_begin),
				(neq, ":troop_id", "trp_player"),
				(neq, ":troop_id", "trp_kidnapped_girl"),
				(neg|is_between, ":troop_id", pretenders_begin, pretenders_end),
				(val_max, ":wage", 1),
			(try_end),
			
			(assign, ":troop_leadership", -1),
			(try_begin),
				(ge, ":party_id", 0),
				(try_begin),
				(this_or_next | party_slot_eq, ":party_id", slot_party_type, spt_town),
				(party_slot_eq, ":party_id", slot_party_type, spt_castle),
				(party_get_slot, ":troop_leadership", ":party_id", slot_town_lord),
				(else_try),
				(eq, ":party_id", "p_main_party"),
				(assign, ":troop_leadership", "trp_player"),
				(else_try),
				(party_stack_get_troop_id, ":troop_leadership", ":party_id", 0),
				(try_end),
			(try_end),
			
			(try_begin),
				(ge, ":troop_leadership", 0),
				(store_skill_level, ":leadership_level", "skl_leadership", ":troop_leadership"),
				(store_mul, ":leadership_bonus", 5, ":leadership_level"),
				(store_sub, ":leadership_factor", 100, ":leadership_bonus"),
				(val_mul, ":wage", ":leadership_factor"),  #wage = wage * (100 - 5*leadership)/100
				(val_div, ":wage", 100),
			(try_end),
			
			(assign, reg0, ":wage"),
			(set_trigger_result, reg0),
			]
		),
		
		# script_get_closest_enemy_distance - tom
		# Input: agent to find from
		# Output: reg1: distance in cms, reg4 glosest agent
		("get_closest_enemy_distance",
			[
			(store_script_param, ":input_agent", 1),
			
			(assign, ":min_distance", 100000),
			(assign, ":closest_agent", -1), #tom
			
			(agent_get_position, pos1, ":input_agent"),
			(agent_get_team, ":team_no", ":input_agent"),
			(try_for_agents,":cur_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_active, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(lt, ":cur_dist", ":min_distance"),
				(assign, ":min_distance", ":cur_dist"),
				(assign, ":closest_agent", ":cur_agent"),
			(try_end),
			
			(assign, reg1, ":min_distance"),
			(assign, reg4, ":closest_agent"), #tom
		]),
		
		# script_get_first_closest_enemy_distance - tom
		# Input: agent to find from
		# Output: reg1: distance in cms, reg4 glosest agent
		("get_first_closest_enemy_distance",
			[
			(store_script_param, ":input_agent", 1),
			(store_script_param, ":team_no", 2),
			(store_script_param, ":minimum_distance", 3),
			
			(assign, ":min_distance", 100000),
			(assign, ":closest_agent", -1), #tom
			
			(agent_get_position, pos1, ":input_agent"),
			(try_for_agents,":cur_agent"),
				(gt, ":min_distance", ":minimum_distance"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_active, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(lt, ":cur_dist", ":min_distance"),
				(assign, ":closest_agent", ":cur_agent"),
				(assign, ":min_distance", ":cur_dist"),
			(try_end),
			
			(assign, reg1, ":min_distance"),
			(assign, reg4, ":closest_agent"), #tom
		]),
		
		# script_get_closest_enemy_distance_new - tom
		# Input: agent to find from, team, minimum distance in cms to find
		# Output: reg1: distance in cms, reg4 glosest agent
		("get_closest_enemy_distance_new",
			[
			(store_script_param, ":input_agent", 1),
			(store_script_param, ":team_no", 2),
			(store_script_param, ":minimum_distance", 3),
			
			(assign, ":min_distance", 100000),
			
			(agent_get_position, pos1, ":input_agent"),
			(try_for_agents,":cur_agent"),
				(gt, ":min_distance", ":minimum_distance"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_active, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(lt, ":cur_dist", ":min_distance"),
				(assign, ":min_distance", ":cur_dist"),
			(try_end),
			
			(assign, reg1, ":min_distance"),
		]),
		
		##script_tom_agent_skirmish
		##description: sets the agent to skirmish
		###input: agent, closest_agent id, range to nearest enemy
		###output: none
		("tom_agent_skirmish",
			[
			(store_script_param, ":agent", 1),
			(store_script_param, ":closest_agent", 2),
			(store_script_param, ":nearest_enemy", 3),
			(store_script_param, ":radious", 4), #8500 
			(store_script_param, ":skrimish_start", 5), #9000
			(store_script_param, ":skrimish_angle", 6), #12
			 
				(try_begin),
					(assign, ":r", ":radious"), #50m. 8500
				(gt, ":closest_agent", 0),
			
				(agent_get_position,pos0,":agent"),
				(agent_get_position,pos1,":closest_agent"),
			
				(agent_get_slot, ":direction",":agent", slot_agent_direction),
				(agent_get_slot, ":rotation",":agent", slot_agent_rotation), #slot -random for now
				(try_begin),
					(eq, ":direction", 0),
					(store_random_in_range, ":direction", 1, 3),
					(agent_set_slot, ":agent", slot_agent_direction, ":direction"),
				(try_end),
				(try_begin),
					(le, ":nearest_enemy", ":skrimish_start"), #when the enemy is close enough, rotate
					(val_add, ":rotation", ":skrimish_angle"), #12
						(try_begin),
						(ge, ":rotation", 360),
						(assign, ":rotation", 0),
					(try_end),
				(agent_set_slot, ":agent", slot_agent_rotation, ":rotation"),
				(try_begin),
					(eq, ":direction", 1),
					(val_mul, ":rotation", -1),
					(val_sub, ":r", 1500),
				(try_end),
					
					(position_get_rotation_around_z, reg1,pos1),
					(store_sub, reg0, 360, reg1), 
					(val_add, ":rotation", reg0),
					(position_rotate_z, pos1, ":rotation"), 
					(position_move_x, pos1, ":r", 0),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(agent_set_slot, ":agent", slot_agent_scripted_mode, 1),
				(else_try),
					(agent_clear_scripted_mode, ":agent"),
				(agent_set_slot, ":agent", slot_agent_scripted_mode, 0),
				(try_end),
				#(agent_force_rethink, ":agent"),
			(try_end),
			]		
		),
		
		("raf_set_troop_classes",
			[
			# (troop_set_class, "trp_euro_spearman_1", grc_archers),
			# (troop_set_class, "trp_euro_spearman_2", grc_archers),
			# (troop_set_class, "trp_euro_spearman_3", grc_archers),
			# (troop_set_class, "trp_mercenary_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_teutonic_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_rus_town_3_2", grc_archers),
			# (troop_set_class, "trp_nordic_spearman", grc_archers),
			# (troop_set_class, "trp_nordic_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_balt_spearman", grc_archers),
			# (troop_set_class, "trp_balt_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_templar_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_hospitaller_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_marinid_levy_spearman", grc_archers),
			# (troop_set_class, "trp_mamluke_spearman", grc_archers),
			# (troop_set_class, "trp_iberian_veteran_spearman", grc_archers),
			# (troop_set_class, "trp_andalus_spearman_1", grc_archers),
			# (troop_set_class, "trp_andalus_spearman_2", grc_archers),
			# (troop_set_class, "trp_andalus_spearman_3", grc_archers),
			# (troop_set_class, "trp_gaelic_spearman_1", grc_archers),
			# (troop_set_class, "trp_gaelic_spearman_2", grc_archers),
			# (troop_set_class, "trp_merc_gaelic_spearman", grc_archers),
			# (troop_set_class, "trp_anatolian_christian_spearman_1", grc_archers),
			# (troop_set_class, "trp_anatolian_christian_spearman_2", grc_archers),
			# (troop_set_class, "trp_scottish_forinsec_spearman", grc_archers),
			# (troop_set_class, "trp_scottish_forinsec_spearman", grc_archers),
			#tom
			# (troop_set_class, "trp_euro_spearman_1", grc_spearmen),
			# (troop_set_class, "trp_euro_spearman_2", grc_spearmen),
			# (troop_set_class, "trp_euro_spearman_3", grc_spearmen),
			# (troop_set_class, "trp_mercenary_veteran_spearman", grc_spearmen),
			# (troop_set_class, "trp_teu_town_2_1", grc_spearmen),
			# (troop_set_class, "trp_teu_town_3_1", grc_spearmen),
			# (troop_set_class, "trp_teu_town_4_1", grc_spearmen),
			# (troop_set_class, "trp_rus_town_3_2", grc_spearmen),
			# (troop_set_class, "trp_nordic_spearman", grc_spearmen),
			# (troop_set_class, "trp_nordic_veteran_spearman", grc_spearmen),
			# (troop_set_class, "trp_balt_spearman", grc_spearmen),
			# (troop_set_class, "trp_balt_veteran_spearman", grc_spearmen),
			# (troop_set_class, "trp_marinid_levy_spearman", grc_spearmen),
			# (troop_set_class, "trp_mamluke_spearman_1", grc_spearmen),
			# (troop_set_class, "trp_mamluke_spearman_2", grc_spearmen),
			# (troop_set_class, "trp_mamluke_spearman_3", grc_spearmen),
			# (troop_set_class, "trp_iberian_veteran_spearman", grc_spearmen),
			# (troop_set_class, "trp_andalus_spearman_1", grc_spearmen),
			# (troop_set_class, "trp_andalus_spearman_2", grc_spearmen),
			# (troop_set_class, "trp_andalus_spearman_3", grc_spearmen),
			# (troop_set_class, "trp_gaelic_spearman_1", grc_spearmen),
			# (troop_set_class, "trp_gaelic_spearman_2", grc_spearmen),
			# (troop_set_class, "trp_merc_gaelic_spearman", grc_spearmen),
			# (troop_set_class, "trp_anatolian_christian_spearman_1", grc_spearmen),
			# (troop_set_class, "trp_anatolian_christian_spearman_2", grc_spearmen),
			# (troop_set_class, "trp_scottish_forinsec_spearman", grc_spearmen),
			# (troop_set_class, "trp_scottish_forinsec_spearman", grc_spearmen),
			
			#(str_store_string, s21, "@Spearmen"),
			#(class_set_name, grc_spearmen, s21),
			
			(troop_set_class, "trp_euro_spearman_1", grc_infantry),
			(troop_set_class, "trp_euro_spearman_2", grc_infantry),
			(troop_set_class, "trp_euro_spearman_3", grc_infantry),
			#(troop_set_class, "trp_mercenary_veteran_spearman", grc_infantry),
			(troop_set_class, "trp_teu_town_2_1", grc_infantry),
			(troop_set_class, "trp_teu_town_3_1", grc_infantry),
			(troop_set_class, "trp_teu_town_4_1", grc_infantry),
			(troop_set_class, "trp_rus_town_3_2", grc_infantry),
			(troop_set_class, "trp_nordic_spearman", grc_infantry),
			(troop_set_class, "trp_nordic_veteran_spearman", grc_infantry),
			(troop_set_class, "trp_balt_spearman", grc_infantry),
			(troop_set_class, "trp_balt_veteran_spearman", grc_infantry),
			(troop_set_class, "trp_marinid_levy_spearman", grc_infantry),
			# (troop_set_class, "trp_mamluke_spearman_1", grc_infantry),
			# (troop_set_class, "trp_mamluke_spearman_2", grc_infantry),
			# (troop_set_class, "trp_mamluke_spearman_3", grc_infantry),
			(troop_set_class, "trp_iberian_veteran_spearman", grc_infantry),
			(troop_set_class, "trp_andalus_spearman_1", grc_infantry),
			(troop_set_class, "trp_andalus_spearman_2", grc_infantry),
			(troop_set_class, "trp_andalus_spearman_3", grc_infantry),
			(troop_set_class, "trp_gaelic_spearman_1", grc_infantry),
			(troop_set_class, "trp_gaelic_spearman_2", grc_infantry),
			(troop_set_class, "trp_merc_gaelic_spearman", grc_infantry),
			(troop_set_class, "trp_anatolian_christian_spearman_1", grc_infantry),
			(troop_set_class, "trp_anatolian_christian_spearman_2", grc_infantry),
			(troop_set_class, "trp_scottish_forinsec_spearman", grc_infantry),
			(troop_set_class, "trp_scottish_forinsec_spearman", grc_infantry),
			#tom
			
			(troop_set_class, "trp_tatar_veteran_horse_archer", grc_horse_archers),
			(troop_set_class, "trp_tatar_horse_archer", grc_horse_archers),
			(troop_set_class, "trp_tatar_horseman", grc_horse_archers),
			(troop_set_class, "trp_tatar_skirmisher", grc_horse_archers),
			(troop_set_class, "trp_cuman_veteran_horse_archer", grc_horse_archers),
			(troop_set_class, "trp_cuman_horse_archer", grc_horse_archers),
			(troop_set_class, "trp_cuman_horseman", grc_horse_archers),
			(troop_set_class, "trp_cuman_skirmisher", grc_horse_archers),
			(troop_set_class, "trp_cuman_tribesman", grc_horse_archers),
			(troop_set_class, "trp_rus_horse_1", grc_horse_archers),
			# (troop_set_class, "trp_mamluke_turkoman", grc_horse_archers),
			# (troop_set_class, "trp_mamluke_light_horse_archer", grc_horse_archers),
			# (troop_set_class, "trp_mamluke_medium_horse_archer", grc_horse_archers),
			# (troop_set_class, "trp_mamluke_heavy_horse_archer", grc_horse_archers),
			# (troop_set_class, "trp_mamluke_elite_horse_archer", grc_horse_archers),
			# (troop_set_class, "trp_byz_castle_1", grc_horse_archers),
			(troop_set_class, "trp_byz_castle_2", grc_horse_archers),
			(troop_set_class, "trp_andalus_horse_1", grc_horse_archers),
			(troop_set_class, "trp_andalus_horse_1", grc_horse_archers),
			(troop_set_class, "trp_anatolian_turkoman_1", grc_horse_archers),
			(troop_set_class, "trp_anatolian_turkoman_2", grc_horse_archers),
			# (troop_set_class, "trp_teu_balt_3", grc_horse_archers),
			(troop_set_class, "trp_crusader_turkopole", grc_horse_archers),
			(troop_set_class, "trp_merc_sicily_horse_archer_1", grc_horse_archers),
			(troop_set_class, "trp_merc_sicily_horse_archer_2", grc_horse_archers),
			
			
			(str_store_string, s21, "@Horse Archers"),
			(class_set_name, grc_horse_archers, s21),
			
			
			(troop_set_class, "trp_marinid_village_rabble", grc_infantry),
			(troop_set_class, "trp_marinid_skirmishers", grc_infantry),
			(troop_set_class, "trp_marinid_javelin_infantry", grc_infantry),
			(troop_set_class, "trp_byz_village_2", grc_infantry),
			(troop_set_class, "trp_iberian_village_skirmisher", grc_infantry),
			(troop_set_class, "trp_teu_balt_1", grc_infantry),
			(troop_set_class, "trp_teu_balt_2", grc_infantry),
			(troop_set_class, "trp_balkan_vil_3_1_1", grc_infantry),
			(troop_set_class, "trp_balt_skirmisher", grc_infantry),
			(troop_set_class, "trp_balt_jav", grc_infantry),
			(troop_set_class, "trp_balt_veteran_jav", grc_infantry),
			#(troop_set_class, "trp_balt_jav_sergeant", grc_infantry), Tom
			(troop_set_class, "trp_merc_almogabar", grc_infantry),
			(troop_set_class, "trp_byz_village_3_1", grc_infantry),
			(troop_set_class, "trp_byz_village_4_1", grc_infantry),
			(troop_set_class, "trp_balkan_vil_4_1_1", grc_infantry),
			(troop_set_class, "trp_balkan_vil_4_1_1", grc_infantry),
			
			(troop_set_class, "trp_marinid_mounted_skirmisher_1", grc_cavalry),
			(troop_set_class, "trp_marinid_mounted_skirmisher_2", grc_cavalry),
			(troop_set_class, "trp_marinid_mounted_skirmisher_3", grc_cavalry),
			
			(troop_set_class, "trp_balt_mounted_skirmisher", grc_cavalry),
			(troop_set_class, "trp_balt_light_cavalry", grc_cavalry),
			(troop_set_class, "trp_balt_medium_cavalry", grc_cavalry),
			
			#tom
			(try_for_range, ":troop", lords_begin, lords_end),
				(troop_set_class, ":troop", grc_cavalry),
			(try_end),
			#tom
			]
		),

	#script_party_calculate_regular_strength:
		# INPUT:
		# param1: Party-id
		("party_calculate_regular_strength",
		[
			(store_script_param_1, ":party"), #Party_id
			
			(assign, reg0,0),
			(party_get_num_companion_stacks, ":num_stacks",":party"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
			(neg|troop_is_hero, ":stack_troop"),
			(store_character_level, ":stack_strength", ":stack_troop"),
			(val_add, ":stack_strength", 12),
			(val_mul, ":stack_strength", ":stack_strength"),
			(val_div, ":stack_strength", 100),
			(party_stack_get_size, ":stack_size",":party",":i_stack"),
			(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
			(val_sub, ":stack_size", ":num_wounded"),
			(val_mul, ":stack_strength", ":stack_size"),
			(val_add,reg0, ":stack_strength"),
			(try_end),
		]),
		
		
		
		
		#script_party_calculate_strength:
		# INPUT: arg1 = party_id, arg2 = exclude leader
		# OUTPUT: reg0 = strength
		
		("party_calculate_strength",
		[
			(store_script_param_1, ":party"), #Party_id
			(store_script_param_2, ":exclude_leader"), #Party_id
			
			(assign, reg0,0),
			(party_get_num_companion_stacks, ":num_stacks", ":party"),
			(assign, ":first_stack", 0),
			(try_begin),
			(neq, ":exclude_leader", 0),
			(assign, ":first_stack", 1),
			(try_end),
			(try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
			(store_character_level, ":stack_strength", ":stack_troop"),
			(val_add, ":stack_strength", 4), #new was 12 (patch 1.125)
			(val_mul, ":stack_strength", ":stack_strength"),
			(val_mul, ":stack_strength", 2), #new (patch 1.125)
			(val_div, ":stack_strength", 100),
			(val_max, ":stack_strength", 1), #new (patch 1.125)
			(try_begin),
				(neg|troop_is_hero, ":stack_troop"),
				(party_stack_get_size, ":stack_size",":party",":i_stack"),
				(party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),                    
				(val_sub, ":stack_size", ":num_wounded"),
				(val_mul, ":stack_strength", ":stack_size"),
			(else_try),
				(troop_is_wounded, ":stack_troop"), #hero & wounded
				(assign, ":stack_strength", 0),
			(try_end),
			(val_add, reg0, ":stack_strength"),
			(try_end),
			(party_set_slot, ":party", slot_party_cached_strength, reg0),
		]),
		
		("change_rain_or_snow",
			[
			(party_get_current_terrain, ":terrain_type", "p_main_party"),
			(try_begin),
				(this_or_next|eq, ":terrain_type", rt_snow),
				(eq, ":terrain_type", rt_snow_forest),
				(assign, ":rain_type", 2),
			(else_try),
				(assign, ":rain_type", 1),
			(try_end),
			
			(get_global_cloud_amount, ":rand_rain"),
			(assign, ":its_raining", 0),
			#(store_random_in_range, ":rand_rain", 0, 101),
			(try_begin),
				(neq, ":terrain_type", rt_desert),
				(neq, ":terrain_type", rt_desert_forest),
				#(lt, ":rand_rain", "$g_rand_rain_limit"),
				(gt, ":rand_rain", 67),
				#(store_mul, ":rand_strength", ":rand_rain", "$g_rand_rain_limit"),
				#(val_div, ":rand_strength", 100),
				#(gt, ":rand_strength", 0),
				(store_random_in_range, ":rand_strength", 30, 101),
				(set_rain, ":rain_type", ":rand_strength"),
				(assign, ":its_raining", 1),
				(store_random_in_range, ":fog", 30, 101),
				(set_global_haze_amount, ":fog"),
				# (store_random_in_range, ":fog", 60, 101),
				# (set_global_cloud_amount, 100),
			(try_end),
			
			#tom - blizzzrd perhaps?
			(store_random_in_range, ":sandstorm", 1, 100),
			(try_begin),
				(eq, ":its_raining", 1),
				(eq, ":rain_type", 2), #snow
				(neq|eq, "$tom_sand_storm_chance", 0),
				(lt, ":sandstorm", "$tom_sand_storm_chance"),
				(set_rain, 2, 100),
				(assign, "$tom_sand_storm", 2),
				(set_global_haze_amount, 100),
				#tom - storm perhaps?
			(else_try),
				(eq, ":its_raining", 1),
				(eq, ":rain_type", 1), #rain
				(neq|eq, "$tom_sand_storm_chance", 0),
				(lt, ":sandstorm", "$tom_sand_storm_chance"),
				(set_rain, 1, 100),
				(assign, "$tom_sand_storm", 3),
				(set_global_haze_amount, 100),
				#tom - perhaps sand storm insted?
			(else_try),
				(this_or_next|eq, ":terrain_type", rt_desert),
				(eq, ":terrain_type", rt_desert_forest),
				#(neq|eq, "$tom_sand_storm_chance", 0),
				(lt, ":sandstorm", "$tom_sand_storm_chance"),
				#(set_rain, 0, 0),
				(assign, "$tom_sand_storm", 1),
				(set_global_haze_amount, 0),
			(try_end),
		]),
		
		("vector_length",
			[
			(store_script_param, ":pos", 1),
			
			(set_fixed_point_multiplier, 10),
			(position_get_x, ":x", ":pos"),
			(position_get_y, ":y", ":pos"),
			
			(store_mul, ":xsq", ":x", ":x"),
			(store_mul, ":ysq", ":y", ":y"),
			
			(store_add, ":xysq", ":xsq", ":ysq"),
			(store_pow, reg0, ":xysq", 5),
			
			(val_div, reg0, 10),
			]
		),
		
		("maintain_broken_items",
			[
			(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
			(troop_get_inventory_capacity, ":inv_cap_b", "trp_broken_items"),
			(try_for_range, ":i_slot_b", 0, ":inv_cap_b"),
				(assign, ":dont_remove", 0),
				(troop_get_inventory_slot, ":item_b", "trp_broken_items", ":i_slot_b"),
				(try_for_range, ":i_slot", 0, ":inv_cap"),
				(troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
				(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
				(eq, ":modifier", imod_poor),
				(eq, ":item", ":item_b"),
				(assign, ":dont_remove", 1),
				(try_end),
				(eq, ":dont_remove", 0),
				(troop_remove_item, "trp_broken_items", ":item_b"),
			(try_end),
			]
		),
		
		#tom-script
		#input: team, group, formation_type
		#output: none
		#first formation member sounds the horn. Used mainly for player armies(ai use them diffrently)
		#script_first_formation_member_sound_horn
		("first_formation_member_sound_horn",
		[
			#(store_script_param, ":team", 1),
			#(store_script_param, ":group", 2),
			#(store_script_param, ":formation_type", 3),
			(get_player_agent_no,":player_agent"),
			(agent_get_team, ":team", ":player_agent"),
			(try_for_range, ":cur_group", 0, 9),
			#(try_begin),
			(class_is_listening_order, ":team", ":cur_group"),
			(assign, ":agent_to_play_sound", -1),
			(try_for_agents, ":agent"),
				(neq, ":agent", ":player_agent"),
				(agent_is_alive, ":agent"), 
				(agent_is_human, ":agent"),
				(agent_get_division, ":division", ":agent"),
				(eq, ":division", ":cur_group"),
				(agent_get_team, ":p_team", ":agent"),
				(eq, ":p_team", ":team"),
				(assign, ":agent_to_play_sound" ,":agent"),
			(try_end),
			
			#(call_script, "script_get_first_formation_member", ":team", ":cur_group", 0),
			(try_begin),
				(gt, ":agent_to_play_sound", -1),
				(agent_play_sound, ":agent_to_play_sound", "snd_horn"),
			(try_end),
			(try_end),
		]
		),
		
		#tom-script
		#input: nothing
		#output: nothing
		#script_set_flag_carriers
		("set_flag_carriers",
		[
			(try_for_range, ":team", 0, 4),
				(team_get_slot, ":team_size", ":team", slot_team_size),
			#(try_begin),
			(gt, ":team_size", 0),
			(neq, "$fplayer_team_no", 0),
			(store_div, ":flags", ":team_size", 35),
			(gt, ":flags", 0),
			(assign, ":flags", 1),
			(try_for_agents, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_is_non_player, ":cur_agent"),
				(agent_get_troop_id, ":cur_troop", ":cur_agent"),
				(neg|troop_is_guarantee_ranged, ":cur_troop"),
				(neg|troop_is_guarantee_horse, ":cur_troop"),
				(neg|troop_is_hero,":cur_troop"),
				(agent_get_team, ":cur_team", ":cur_agent"),
				(eq, ":cur_team", 0),
				(gt, ":flags", 0),
				(try_begin),
					(agent_get_party_id, ":party", ":cur_agent"),
				(gt, ":party", 0),
				(store_faction_of_party, ":faction", ":party"),
				(eq, ":faction", "fac_kingdom_23"),
				(party_stack_get_troop_id, ":party_leader", ":party", 0),
				(eq, ":party_leader", "trp_kingdom_23_lord"),
				(assign, ":item", "itm_cross"),
				(else_try),
					(store_random_in_range, ":item", "itm_flag_pole_1", "itm_cross"),
				(try_end),	
				(agent_equip_item, ":cur_agent", ":item"),
				(agent_set_wielded_item, ":cur_agent", ":item"),
				(agent_set_slot, ":cur_agent",slot_agent_banner, 1),
				(val_sub, ":flags", 1),
			(try_end),
			(try_end),
			
			#player team - flag carriers
			(assign, ":group0", 0),
			(assign, ":group1", 0),
			(assign, ":group2", 0),
			(assign, ":group3", 0),
			(assign, ":group4", 0),
			(assign, ":group5", 0),
			(assign, ":group6", 0),
			(assign, ":group7", 0),
			(assign, ":group8", 0),
			#count the amount of agents
			(try_for_agents, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_is_non_player, ":cur_agent"),
			(agent_get_team, ":cur_team", ":cur_agent"),
			(eq, ":cur_team", "$fplayer_team_no"),
			(agent_get_division, ":cur_group", ":cur_agent"),
			(try_begin),
				(eq, ":cur_group", 0),
				(val_add, ":group0", 1),
			(else_try),
				(eq, ":cur_group", 1),
				(val_add, ":group1", 1),
			(else_try),
				(eq, ":cur_group", 2),
				(val_add, ":group2", 1),
			(else_try),
				(eq, ":cur_group", 3),
				(val_add, ":group3", 1),
			(else_try),
				(eq, ":cur_group", 4),
				(val_add, ":group4", 1),
			(else_try),
				(eq, ":cur_group", 5),
				(val_add, ":group5", 1),
			(else_try),
				(eq, ":cur_group", 6),
				(val_add, ":group6", 1),
			(else_try),
				(eq, ":cur_group", 7),
				(val_add, ":group7", 1),
			(else_try),
				(eq, ":cur_group", 8),
				(val_add, ":group8", 1),
			(try_end),
			(try_end),
			
			(try_for_range, reg1, 0, 9),
			(assign, ":head_count", 0),
			(assign, ":group", reg1),
			(try_begin),
				(eq, reg1, 0),
				(val_add, ":head_count", ":group0"),
			(else_try),
				(eq, reg1, 1),
				(val_add, ":head_count", ":group1"),
			(else_try),
				(eq, reg1, 2),
				(val_add, ":head_count", ":group2"),
			(else_try),
				(eq, reg1, 3),
				(val_add, ":head_count", ":group3"),
			(else_try),
				(eq, reg1, 4),
				(val_add, ":head_count", ":group4"),
			(else_try),
				(eq, reg1, 5),
				(val_add, ":head_count", ":group5"),
			(else_try),
				(eq, reg1, 6),
				(val_add, ":head_count", ":group6"),
			(else_try),
				(eq, reg1, 7),
				(val_add, ":head_count", ":group7"),
			(else_try),
				(eq, reg1, 8),
				(val_add, ":head_count", ":group8"),
			(try_end),
			(store_div, ":flags", ":head_count", 20),
			(gt, ":flags", 0),
			(assign, ":flags", 1),
			(try_for_agents, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_is_non_player, ":cur_agent"),
				(agent_get_troop_id, ":cur_troop", ":cur_agent"),
				(neg|is_between, ":cur_troop", active_npcs_begin, active_npcs_end), #not a lord or a companion
				(neg|troop_is_guarantee_ranged, ":cur_troop"),
				(neg|troop_is_guarantee_horse, ":cur_troop"),
				(neg|troop_is_hero,":cur_troop"),
				(agent_get_team, ":cur_team", ":cur_agent"),
				(eq, ":cur_team", "$fplayer_team_no"),
				(agent_get_division, ":cur_group", ":cur_agent"),
				(eq, ":cur_group", ":group"),
				(gt, ":flags", 0),
				# (init_position, pos8),
				(agent_get_position, pos8, ":cur_agent"),
				(set_spawn_position, pos8),
				#(spawn_agent, ":cur_troop"),
				#(display_message, "@spawning"),
				#(assign, ":agent", reg0),
				(assign, ":agent", ":cur_agent"),
				(agent_set_team, ":agent", ":cur_team"),
				#(agent_set_division, ":agent", ":cur_group"),
				(store_random_in_range, ":item", "itm_flag_pole_1", "itm_cross"),
				(agent_equip_item, ":agent", ":item"),
				(agent_equip_item, ":agent", ":item"),
				(agent_equip_item, ":agent", ":item"),
				(agent_set_wielded_item, ":agent", ":item"),
				(agent_set_slot, ":agent",slot_agent_banner, 1),
				(val_sub, ":flags", 1),
			(try_end),
			(try_end),
		]),
		
	##TOM freelancer addon
	## script_freelancer_get_troop
	##input: troop, faction
	##output: reg1 - troop
	("freelancer_get_troop",
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
	]),	  
	
	###script_pass_all_posetions_from_lord_to_lord
	###input: lord_from, lord_to
	###output: none
	##gives all the posetion(except items) to the order lord. Items are remvoed and bread is added
	("pass_all_posetions_from_lord_to_lord",
	[
		 (store_script_param, ":lord_from", 1),
		 (store_script_param, ":lord_to", 2),
		 
		 ##gold
		 (store_troop_gold,":gold", ":lord_from"),
		 (troop_remove_gold,":lord_from",":gold"),
		 (troop_add_gold, ":lord_to", ":gold"),
		 ##items
		 (troop_clear_inventory,":lord_from"),
		 (try_for_range, reg1, all_items_begin,all_items_end),
			 (troop_has_item_equipped,":lord_from",reg1),
		 (troop_remove_item, ":lord_from",reg1),
		 (try_end),
		 (troop_clear_inventory,":lord_from"),
		 ##land
		 # (try_for_range, reg1, centers_begin, centers_end),
			 # (party_get_slot, ":center_lord", reg1, slot_town_lord),
		 # (eq, ":center_lord", ":lord_from"),
		 # (call_script, "script_give_center_to_lord", reg1, ":lord_to", 0),
		 # (try_end),
		 ##bread

	]),
	
	###script_desert_order
	#description: checks if player is in an crusader order and if so does the penalty for deserting
	#input: none
	#output: none
	("desert_order",
	[
		(try_begin),
		(eq, "$crusader_order_joined", 1),
		(display_message, "@Deserting the grandmaster of your order had brought you much dishonor"),
		(call_script, "script_change_player_honor", -50),
		(call_script, "script_change_troop_renown", "trp_player", -50),
		(try_end),
	]),
	#tom freelancer addon
		
#+freelancer start
	 ("freelancer_attach_party",
		[
			#prepare player to be part of lord's party
				(party_attach_to_party, "p_main_party", "$enlisted_party"),
				(set_camera_follow_party, "$enlisted_party"),
				(party_set_flags, "$enlisted_party", pf_always_visible, 1),
				(disable_party, "p_main_party"),

		#initialize service variable
		(assign, "$freelancer_state", 1),		
		]),

	 ("freelancer_detach_party",
		[
			#removes player from commanders party
		(enable_party, "p_main_party"),
				(party_detach, "p_main_party"),
		
		(try_begin),
			(party_is_active, "$enlisted_party"),
			(party_relocate_near_party, "p_main_party", "$enlisted_party", 2),
			(party_set_flags, "$enlisted_party", pf_always_visible, 0),
		(try_end),	
		
			(set_camera_follow_party, "p_main_party"),
		(assign, "$g_player_icon_state", pis_normal),
	]),

# ADDS THE PLAYER TO THE LORD'S PARTY  
		("event_player_enlists",
		[
		(store_script_param, ":tier", 1),
			#initialize service variables
				(troop_get_xp, ":xp", "trp_player"),
		(troop_set_slot, "trp_player", slot_troop_freelancer_start_xp, ":xp"),
				(store_current_day, ":day"), 
				(troop_set_slot, "trp_player", slot_troop_freelancer_start_date, ":day"),		
		(party_get_morale, ":morale", "p_main_party"),
		(party_set_slot, "p_main_party", slot_party_orig_morale, ":morale"),
				#(assign, "$freelancer_state", 1), #moved to script
	
				#needed to stop bug where parties attack the old player party
				(call_script, "script_set_parties_around_player_ignore_player", 2, 4),
				#set lord as your commander
		(assign, "$enlisted_lord", "$g_talk_troop"),
		(troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), 
				#removes troops from player party
				(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
				(try_for_range_backwards, ":cur_stack", 1, ":num_stacks"), #lower bound is 1 to ignore player character
					 (party_stack_get_troop_id, ":cur_troops", "p_main_party", ":cur_stack"),
					 (party_stack_get_size, ":cur_size", "p_main_party", ":cur_stack"),
					 (party_remove_members, "p_main_party", ":cur_troops", ":cur_size"),
				(try_end),
				
		#set faction relations to allow player to join battles
				(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(try_begin),
			(store_relation, ":player_relation", ":commander_faction", "fac_player_supporters_faction"),
			(lt, ":player_relation", 5),
			(call_script, "script_set_player_relation_with_faction", ":commander_faction", 5),
		(try_end),
				(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					 (neq, ":commander_faction", ":cur_faction"),
			 (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
			 (store_relation, ":player_relation", ":cur_faction", "fac_player_supporters_faction"),
			 (ge, ":player_relation", 0),
					 (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
				(try_end),		

		###TOM
				#adds standard issued equipment
		# (try_begin),
			# (neg|faction_slot_eq, ":commander_faction", slot_faction_freelancer_troop, 0),
			# (faction_get_slot, "$player_cur_troop", ":commander_faction", slot_faction_freelancer_troop),
		# (else_try),
			# (faction_get_slot, "$player_cur_troop", ":commander_faction", slot_faction_tier_1_troop),
		# (try_end),	
		(call_script, "script_freelancer_get_troop", "$enlisted_lord", ":commander_faction", ":tier"),		
		(assign, "$player_cur_troop", reg1),
		###TOM
		(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),

		(call_script, "script_freelancer_attach_party"),
		#makes Lords banner the players
		(troop_get_slot, ":banner", "$enlisted_lord", slot_troop_banner_scene_prop),
		(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":banner"),
				(display_message, "@You have been enlisted!"),	

		
				(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, ":commander_faction"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_target_party, "$enlisted_party"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_importance, 5),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_xp_reward, 1000),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_gold_reward, 100),
		(setup_quest_text, "qst_freelancer_enlisted"),
		(str_clear, s2), #description. necessary?
				(call_script, "script_start_quest", "qst_freelancer_enlisted", "$enlisted_lord"),
		(str_store_troop_name, s5, "$player_cur_troop"),
		(str_store_string, s5, "@Current rank: {s5}"),
				(add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),		
		]),

#  RUNS IF THE PLAYER LEAVES THE ARMY

	 ("event_player_discharge",
		[
		#removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", 5),
		(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
						(neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
			(store_relation, ":player_relation", ":cur_faction", "fac_player_supporters_faction"),
			(lt, ":player_relation", 0),
						(call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
				(try_end),
		# removes standard issued equipment
		# (try_for_range, ":cur_inv_slot", ek_item_0, ek_food),
			# (troop_get_inventory_slot, ":soldier_equipment", "$player_cur_troop", ":cur_inv_slot"),
			# (ge, ":soldier_equipment", 0),
			# (troop_remove_item, "trp_player", ":soldier_equipment"),
		# (try_end),
		(call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),		
		(troop_equip_items, "trp_player"),
		

		(troop_set_slot, "trp_player", slot_troop_current_mission, 0),
		(troop_set_slot, "trp_player", slot_troop_days_on_mission, 0),
		(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0),
		(assign, "$freelancer_state", 0),
		(call_script, "script_freelancer_detach_party"),
		(rest_for_hours, 0,0,0),
		(display_message, "@You have left your commander!"), 

				#(call_script, "script_cancel_quest", "qst_freelancer_enlisted"),
		(call_script, "script_finish_quest", "qst_freelancer_enlisted", 100), #percentage--make based on days served?
		]),
	
#  RUNS IF THE PLAYER GOES ON VACATION

		("event_player_vacation",
		[
			(troop_set_slot, "trp_player", slot_troop_current_mission, plyr_mission_vacation), ###move to quests, not missions
		(troop_set_slot, "trp_player", slot_troop_days_on_mission, 14),
	
		#removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
						(neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
						(call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
				(try_end),

		(assign, "$freelancer_state", 2),
		(call_script, "script_freelancer_detach_party"),
		(rest_for_hours, 0,0,0),
		(display_message, "@You have been granted leave!"), 	

		(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, ":commander_faction"),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_target_party, "$enlisted_party"),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_importance, 0),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_xp_reward, 50),
		(quest_set_slot, "qst_freelancer_vacation",	slot_quest_expiration_days, 14),
		(setup_quest_text, "qst_freelancer_vacation"),
		(str_clear, s2), #description. necessary?
				(call_script, "script_start_quest", "qst_freelancer_vacation", "$enlisted_lord"),
		]),

# RUNS WHEN PLAYER RETURNS FROM VACATION

	("event_player_returns_vacation",
		[
				(troop_set_slot, "trp_player", slot_troop_current_mission, 0),
		(troop_set_slot, "trp_player", slot_troop_days_on_mission, 0),
		
		#needed to stop bug where parties attack the old player party
				(call_script, "script_set_parties_around_player_ignore_player", 2, 4),

				#removes troops from player party #Caba--could use party_clear? and then add the player back?
				(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
				(try_for_range_backwards, ":cur_stack", 1, ":num_stacks"), #lower bound is 1 to ignore player character
					 (party_stack_get_troop_id, ":cur_troops", "p_main_party", ":cur_stack"),
					 (party_stack_get_size, ":cur_size", "p_main_party", ":cur_stack"),
					 (party_remove_members, "p_main_party", ":cur_troops", ":cur_size"),
				(try_end),
		
				#To fix any errors of the lord changing parties
		(troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), 
		
		#set faction relations to allow player to join battles
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
					 (neq, ":commander_faction", ":cur_faction"),
			 (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
					 (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
				(try_end),	
		(try_begin),
			(store_relation, ":player_relation", ":commander_faction", "fac_player_supporters_faction"),
			(lt, ":player_relation", 5),
			(call_script, "script_set_player_relation_with_faction", ":commander_faction", 5),
		(try_end),

		(call_script, "script_freelancer_attach_party"),
		(display_message, "@You have rejoined your commander!"), 		
		]),
	
	
	# RUNS IF PLAYER DESERTS OR IS AWOL
	("event_player_deserts",
	 [     
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
	(call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", -10), 
		(call_script, "script_change_player_relation_with_troop", "$enlisted_lord", -10),
		(call_script, "script_change_player_honor", -20),
	
	(troop_set_slot, "trp_player", slot_troop_current_mission, 0),
	(troop_set_slot, "trp_player", slot_troop_days_on_mission, 0),
	(faction_set_slot, ":commander_faction", slot_faction_freelancer_troop, 0),
	(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0),
	(rest_for_hours, 0,0,0),
	(assign, "$freelancer_state", 0),
	#(display_message, "@You have deserted your commander!"), #Taken care of elsewhere
	(call_script, "script_fail_quest", "qst_freelancer_enlisted"),
	
	
	 ]),	
	
	
	# RETURNS PART OF THE ORIGINAL PARTY
		("party_restore", 
		[
				(store_current_day, ":cur_day"),
				#formula for soldier desertion chance
		(troop_get_slot, ":service_day_start", "trp_player", slot_troop_freelancer_start_date),
				(store_sub, ":service_length", ":cur_day", ":service_day_start"), #gets number of days served
		(party_get_slot, ":morale", "p_main_party", slot_party_orig_morale),
				(store_add, ":return_chance", 800, ":morale"), #up to 100
				(val_sub, ":return_chance", ":service_length"), #up to far over 100

				#loop that looks at each troop stack in a party, 
				#then decides if troops of that stack will return, 
				#and randomly assigns a number of troops in that stack to return
				(party_get_num_companion_stacks, ":num_stacks", "p_freelancer_party_backup"),
				(try_for_range, ":cur_stack", 0, ":num_stacks"),
			(assign, ":stack_amount", 0),
			(party_stack_get_troop_id, ":return_troop", "p_freelancer_party_backup", ":cur_stack"),
			(neq, ":return_troop", "trp_player"),
			(try_begin),
				(troop_is_hero, ":return_troop"), #bugfix for companions (simple, they always return)
				(assign, ":stack_amount", 1),
			(else_try),
				#limit may need changed for more accurate probability
				(store_random_in_range, ":return_random", 0, 1000),
				(is_between, ":return_random", 0, ":return_chance"),
				(party_stack_get_size, ":stack_size", "p_freelancer_party_backup", ":cur_stack"),
				#checks what chance there is that all troops in stack will return
				(store_random_in_range, ":return_random", 0, 1000),
				(try_begin),
					(is_between, ":return_random", 0, ":return_chance"),
					(assign, ":stack_amount", ":stack_size"),
				(else_try),
					#else random number of troops return
					(store_random_in_range, ":stack_amount", 0, ":stack_size"),
				(try_end),
			(try_end),
			(ge, ":stack_amount", 1),
			(party_add_members, "p_main_party", ":return_troop", ":stack_amount"),
				(try_end),
		(party_clear, "p_freelancer_party_backup"),
		]),

#  CALCULATES NUMBER OF DESERTING TROOPS

	 ("get_desert_troops", #CABA - check this
		[
				(party_get_morale, ":commander_party_morale", "$enlisted_party"), #does this actually get tracked for non-player parties?
				(store_current_day, ":cur_day"),
				#formula for soldier desertion chance
				#gets number of days served
		(troop_get_slot, ":service_day_start", "trp_player", slot_troop_freelancer_start_date),
				(store_sub, ":service_length", ":cur_day", ":service_day_start"),
				#inverts the commander's party morale
				(store_sub, ":commander_neg_morale", 100, ":commander_party_morale"), #still a positive number... 100-80 = 20
				(store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
				(store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
				#had to multiply these skills to give them a decent effect on desertion chance
				(val_mul, ":cur_leadership", 10), #up to 100
				(val_mul, ":cur_persuasion", 10), #up to 100
				(store_add, ":desert_chance", ":cur_leadership", ":cur_persuasion"), #up to 200
		(val_add, ":desert_chance", ":service_length"), #up to 400 maybe
				(val_add, ":desert_chance", ":commander_neg_morale"), #up to 450, maybe? if party morale is down to 50
				#loop that looks at each troop stack in a party, 
				#then decides if troops of that stack will desert, 
				#and randomly assigns a number of troops in that stack to desert
				(party_get_num_companion_stacks, ":num_stacks", "$enlisted_party"),
				(try_for_range_backwards, ":cur_stack", 1, ":num_stacks"),
						#limit may need changed for more accurate probability
						(store_random_in_range, ":desert_random", 0, 1000),
						(is_between, ":desert_random", 0, ":desert_chance"),
			#switching deserting troops to player party
			(party_stack_get_troop_id, ":desert_troop", "$enlisted_party", ":cur_stack"),
			(party_stack_get_size, ":stack_size", "$enlisted_party", ":cur_stack"),
			(store_random_in_range, ":stack_amount", 0, ":stack_size"),
			(party_remove_members, "$enlisted_party", ":desert_troop", ":stack_amount"),
			(party_add_members, "p_main_party", ":desert_troop", ":stack_amount"),
				(try_end),        		
		]),
	
	("freelancer_keep_field_loot",
	 [
	(get_player_agent_no, ":player"),
	(try_for_range, ":ek_slot", ek_item_0, ek_head),
		(agent_get_item_slot, ":item", ":player", ":ek_slot"), 
		(gt, ":item", 0),
		(neg|troop_has_item_equipped, "trp_player", ":item"),
		(troop_add_item, "trp_player", ":item"),
	(try_end),
	(agent_get_horse, ":horse", ":player"),
	(try_begin),
		(gt, ":horse", 0),
		(agent_get_item_id, ":horse", ":horse"),
		(troop_get_inventory_slot, ":old_horse", "trp_player", ek_horse),
		(neq, ":horse", ":old_horse"),
		(try_begin),
		(gt, ":old_horse", 0),
		(troop_get_inventory_slot_modifier, ":horse_imod", "trp_player", ek_horse),
		(troop_add_item, "trp_player", ":old_horse", ":horse_imod"),
		(try_end),
		(troop_set_inventory_slot, "trp_player", ek_horse, ":horse"),
	(try_end),
	 ]),
		
	 ("cf_freelancer_player_can_upgrade",
	 #Reg0 outputs reason for failure
	 [
	(store_script_param_1, ":source_troop"),
	
	(troop_get_inventory_capacity, ":troop_cap", ":source_troop"),	
	(assign, ":continue", 1),
	
	(assign, ":type_available", 0),
	(assign, ":type_count", 0),
	(assign, ":end", itp_type_arrows),
	(try_for_range, ":type", itp_type_one_handed_wpn, ":end"),
		#Count Items from Source Troop
		(assign, ":end2", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end2"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":item_type", ":item"),
			(eq, ":item_type", ":type"),
			(val_add, ":type_count", 1),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),		
			(assign, ":type_available", 1),
			(assign, ":end2", 0), #break
		(try_end),
		(eq, ":type_available", 1),
		(assign, ":end", itp_type_one_handed_wpn), #break
	(try_end), #Melee loop
	(try_begin),
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 0),
	(try_end),
	(eq, ":continue", 1),
	
	(assign, ":type_available", 0),
	(assign, ":type_count", 0),
	(assign, ":end2", ":troop_cap"),
	(try_for_range, ":inv_slot", 0, ":end2"),
		(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
		(gt, ":item", 0),
		(item_get_type, ":item_type", ":item"),
		(eq, ":item_type", itp_type_body_armor),
		(val_add, ":type_count", 1),
		(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
		(eq, reg0, 1),		
		(assign, ":type_available", 1),
		(assign, ":end2", 0), #break
	(try_end),
	(try_begin),
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 1),
	(try_end),
	(eq, ":continue", 1),
	
	(try_begin),
		(troop_is_guarantee_ranged, ":source_troop"),
		(assign, ":type_available", 0),
		(assign, ":type_count", 0),
		(assign, ":end", itp_type_goods),
		(try_for_range, ":type", itp_type_bow, ":end"),
			#Count Items from Source Troop
			(assign, ":end2", ":troop_cap"),
			(try_for_range, ":inv_slot", 0, ":end2"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
				(gt, ":item", 0),
				(item_get_type, ":item_type", ":item"),
				(eq, ":item_type", ":type"),
				(val_add, ":type_count", 1),
				(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
				(eq, reg0, 1),		
				(assign, ":type_available", 1),
				(assign, ":end2", 0), #break
			(try_end),
			(eq, ":type_available", 1),
			(assign, ":end", itp_type_bow), #break
		(try_end), #Ranged loop
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 2), 
	(try_end),
	(eq, ":continue", 1),
	
	(try_begin),
		(troop_is_guarantee_horse, ":source_troop"),
		(assign, ":type_available", 0),
		(assign, ":type_count", 0),
		(assign, ":end2", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end2"),
			(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":item_type", ":item"),
			(eq, ":item_type", itp_type_horse),
			(val_add, ":type_count", 1),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),		
			(assign, ":type_available", 1),
			(assign, ":end2", 0), #break
		(try_end),
		(eq, ":type_available", 0),
		(gt, ":type_count", 0), #only care if there were items possible to equip
		(assign, ":continue", 0),
		(assign, reg0, 3),
	(try_end),
	(eq, ":continue", 1),	
	 ]),
	 
	 
		("freelancer_equip_troop",
	 [
		(store_script_param_1, ":source_troop"),
	
	(str_clear, s2),
	(set_show_messages, 0),
	
	(assign, ":recording_slot", slot_freelancer_equip_start),	
	(troop_get_inventory_capacity, ":troop_cap", ":source_troop"),
	(assign, ":melee_given", 0),
	(assign, ":needs_ammo", 0),
	(assign, ":open_weapon_slot", 0),
	(try_for_range, ":type", itp_type_horse, itp_type_pistol),
			(neq, ":type", itp_type_goods),
		(neq, ":type", itp_type_arrows),
		(neq, ":type", itp_type_bolts),
		
		#Assign Prob. of Getting Type
		(assign, ":continue", 0),
		(try_begin),
			(troop_is_guarantee_horse, ":source_troop"),
				(eq, ":type", itp_type_horse),
			(assign, ":continue", 1),
		(else_try),
				(troop_is_guarantee_ranged, ":source_troop"),
				(this_or_next|eq, ":type", itp_type_bow),
			(this_or_next|eq, ":type", itp_type_crossbow),
			(eq, ":type", itp_type_thrown),
			(assign, ":continue", 1),
		(else_try),
				(this_or_next|eq, ":type", itp_type_shield), #Shields and all armor pieces are guaranteed
				(ge, ":type", itp_type_head_armor),
			(assign, ":continue", 1),
		(else_try),
				(neq, ":type", itp_type_horse),
				(lt, ":open_weapon_slot", 4),
			(store_random_in_range, ":continue", 0, 3), # 1 chance in three of being 1
		(try_end),
		(eq, ":continue", 1),		
		
		#Clear Temp Array
		(try_for_range, ":inv_slot", 0, 20),
			(troop_set_slot, "trp_temp_array_a", ":inv_slot", 0),
		(try_end),	
		
		#Collect Items from Source Troop
		(assign, ":type_count", 0),
		(try_for_range, ":inv_slot", 0, ":troop_cap"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":item_type", ":item"),
			(eq, ":item_type", ":type"),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),		
			(troop_set_slot, "trp_temp_array_a", ":type_count", ":item"),
			(val_add, ":type_count", 1),
		(try_end),
		(gt, ":type_count", 0),
		
		#Pick Random Item of Type from Troop
		(try_begin),
				(eq, ":type_count", 1),
			(assign, ":index", 0),
		(else_try),
			(store_random_in_range, ":index", 0, ":type_count"),
		(try_end),
		(troop_get_slot, ":item", "trp_temp_array_a", ":index"),
		(gt, ":item", 0),		
		(str_store_item_name, s3, ":item"),
		(str_store_string, s2, "@{s3}, {s2}"),
		
		#Select correct EK slot to force equip
		(try_begin),
				(eq, ":type", itp_type_horse),
			(assign, ":ek_slot", ek_horse),
		(else_try),
				(is_between, ":type", itp_type_head_armor, itp_type_pistol),
			(store_sub, ":shift", ":type", itp_type_head_armor),
			(store_add, ":ek_slot", ek_head, ":shift"),
		(else_try),
			(store_add, ":ek_slot", ek_item_0, ":open_weapon_slot"),
		(try_end),
		
		#Check for item already there, move it if present
		(try_begin),
				(troop_get_inventory_slot, ":old_item", "trp_player", ":ek_slot"),
			(gt, ":old_item", 0),
			(troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ":ek_slot"),
			(troop_add_item, "trp_player", ":old_item", ":old_item_imod"),
		(try_end),
		
		#Add Item
		(troop_set_inventory_slot, "trp_player", ":ek_slot", ":item"),
		(party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
		(val_add, ":recording_slot", 1),
		(try_begin),
				(is_between, ":type", itp_type_one_handed_wpn, itp_type_head_armor), #Uses one of the 4 weapon slots
				(val_add, ":open_weapon_slot", 1),
			(try_begin),
				(is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows),
				(assign, ":melee_given", 1),
						(else_try),
				(eq, ":type", itp_type_bow),
				(assign, ":needs_ammo", itp_type_arrows),
			(else_try),
				(eq, ":type", itp_type_crossbow),
				(assign, ":needs_ammo", itp_type_bolts),
			(try_end),
		(try_end),
	(try_end), #Item Types Loop
	 
		#add ammo for any equipped bow
		(try_begin),
			(neq, ":needs_ammo", 0),		
		#Check for item already in the last slot, move it if present
		(try_begin), 
				(troop_get_inventory_slot, ":old_item", "trp_player", ek_item_3),
			(gt, ":old_item", 0),
			(troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ek_item_3),
			(troop_add_item, "trp_player", ":old_item", ":old_item_imod"), 
		(try_end),
		
		(assign, ":end", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":type", ":item"),
			(eq, ":type", ":needs_ammo"),
			(troop_set_inventory_slot, "trp_player", ek_item_3, ":item"),
			(party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
				(val_add, ":recording_slot", 1),
			(assign, ":open_weapon_slot", 4),
			(str_store_item_name, s3, ":item"),
				(str_store_string, s2, "@{s3}, {s2}"),
			(assign, ":end", 0),
		(try_end),
	(try_end), 
	
	#double check melee was given
	(try_begin),
			(eq, ":melee_given", 0),
		(assign, ":end", ":troop_cap"),
		(try_for_range, ":inv_slot", 0, ":end"),
				(troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
			(gt, ":item", 0),
			(item_get_type, ":type", ":item"),
			(is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows),
			(call_script, freelancer_can_use_item, "trp_player", ":item", 0),
			(eq, reg0, 1),	
			(try_begin),
					(gt, ":open_weapon_slot", 3),
					(assign, ":open_weapon_slot", 2),
			(try_end),
			
			#Check for item already there
			(try_begin),
				(troop_get_inventory_slot, ":old_item", "trp_player", ":open_weapon_slot"),
				(gt, ":old_item", 0),
				(troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ":open_weapon_slot"),
				(troop_add_item, "trp_player", ":old_item", ":old_item_imod"),
			(try_end),
			
			(troop_set_inventory_slot, "trp_player", ":open_weapon_slot", ":item"),		
			(party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
				(val_add, ":recording_slot", 1),
			(str_store_item_name, s3, ":item"),
				(str_store_string, s2, "@{s3}, {s2}"),
				(assign, ":end", 0),
		(try_end),
	(try_end), 
	
		(set_show_messages, 1),
	(try_begin),
		(neg|str_is_empty, s2),
		(val_sub, ":recording_slot", slot_freelancer_equip_start),
		(party_set_slot, "p_freelancer_party_backup", slot_freelancer_equip_start - 1, ":recording_slot"),	#Record Number of Items Added
		
		(str_store_troop_name, s1, ":source_troop"),
		(display_message, "@The equipment of a {s1}: {s2}is assigned to you."),	
	(try_end),
	 ]),
	
	("freelancer_unequip_troop",
	 [
		(store_script_param_1, ":source_troop"),

	(str_clear, s2),	
	(set_show_messages, 0),
	
	(party_get_slot, ":num_items", "p_freelancer_party_backup", slot_freelancer_equip_start - 1), #Num of items previously given
	
		(troop_get_inventory_capacity, ":cap", "trp_player"),		
	(try_for_range, ":i", 0, ":num_items"),
			(store_add, ":slot", slot_freelancer_equip_start, ":i"),
			(party_get_slot, ":given_item", "p_freelancer_party_backup", ":slot"),
		(gt, ":given_item", 0),
		
		(assign, ":end", ":cap"),
		(try_for_range, ":inv_slot", 0, ":end"),
			(troop_get_inventory_slot, ":item", "trp_player", ":inv_slot"),
			(eq, ":item", ":given_item"),			
			(troop_get_inventory_slot_modifier, ":imod", "trp_player", ":inv_slot"),
			(eq, ":imod", 0), #Native troop items never have modifiers
			
			(troop_set_inventory_slot, "trp_player", ":inv_slot", -1),
			(str_store_item_name, s3, ":item"),
			(str_store_string, s2, "@{s3}, {s2}"),
			
			(assign, ":end", 0), #Break
		(try_end), #Player Inventory Loop
	(try_end), #Item Given Slot Loop

	(set_show_messages, 1),
	(try_begin),
		(neg|str_is_empty, s2),
		(party_set_slot, "p_freelancer_party_backup", slot_freelancer_equip_start - 1, 0),	#Reset Number of Items Added
		(str_store_troop_name, s1, ":source_troop"),
		(display_message, "@The equipment of a {s1}: {s2}is taken from you."),
	(try_end),	
	(troop_equip_items, "trp_player"),
	 ]), 
#+freelancer end
		
		# ("tom_force_equip_the_bastards",
		# [
			# (try_for_range, ":troop", lords_begin, lords_end),
			# (troop_get_inventory_capacity, ":troop_cap", ":troop"),
			# (try_for_range, ":inv_slot", ek_head, ek_horse),
				# (troop_get_inventory_slot, ":item", ":troop", ":inv_slot"),
				# (gt, ":item", 0),
				######(item_get_type, ":item_type", ":item"),
				######(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":object"),
				######(troop_set_inventory_slot_modifier, ":troop", ":inv_slot", imod_rusty),#imod_plain),
				######(troop_set_inventory_slot_modifier,<troop_id>,<inventory_slot_no>,<value>),
			# (else_try),
				
				# (str_store_troop_name, s3, ":troop" ),
				# (assign, reg5, ":inv_slot"),
				######(str_store_string_reg, s4, reg5),
				# (display_message, "@fail! {s3} does not have: {reg5}"),
				# (try_begin),
				# (eq, ":inv_slot", ek_body),
				# (troop_add_item,":troop","itm_kau_lit_mail"),
				# (try_end),
				######(troop_equip_items, ":troop"),
			# (try_end),
			# (try_end),
		# ]),
		
# script_refresh_center_inventories
	("refresh_center_inventories",
	[   	
		(set_merchandise_modifier_quality,150),
		(reset_item_probabilities,100),	    

		# Add trade goods to merchant inventories
		(try_for_range,":cur_center",towns_begin, towns_end),
			(party_get_slot,":cur_merchant",":cur_center",slot_town_merchant),
			(reset_item_probabilities,100),
			(assign, ":total_production", 0),
			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
				(call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
		(assign, ":cur_production", reg0),

				(try_for_range, ":cur_village", villages_begin, villages_end),
			(party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
					(call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
			(val_div, reg0, 3),
			(val_add, ":cur_production", reg0),
		(try_end),		

		(val_max, ":cur_production", 1),
		(val_mul, ":cur_production", 4),

		(val_add, ":total_production", ":cur_production"),
			(try_end),

		(party_get_slot, ":town_prosperity", ":cur_center", slot_town_prosperity),
		(assign, ":number_of_items_in_town", 25),

		(try_begin), #1.0x - 2.0x (50 - 100 prosperity)
			(ge, ":town_prosperity", 50),
		(store_sub, ":ratio", ":town_prosperity", 50),
		(val_mul, ":ratio", 2),
		(val_add, ":ratio", 100),
		(val_mul, ":number_of_items_in_town", ":ratio"),
		(val_div, ":number_of_items_in_town", 100),
		(else_try), #0.5x - 1.0x (0 - 50 prosperity)
		(store_sub, ":ratio", ":town_prosperity", 50),
		(val_add, ":ratio", 100),
		(val_mul, ":number_of_items_in_town", ":ratio"),
		(val_div, ":number_of_items_in_town", 100),
		(try_end),

		(val_clamp, ":number_of_items_in_town", 10, 40),	

		(try_begin),
			(is_between, ":cur_center", castles_begin, castles_end),
			(val_div, ":number_of_items_in_town", 2),
			(try_end),

			(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
				(call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
		(assign, ":cur_production", reg0),

				(try_for_range, ":cur_village", villages_begin, villages_end),
			(party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
					(call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
			(val_div, reg0, 3),
			(val_add, ":cur_production", reg0),
		(try_end),		

		(val_max, ":cur_production", 1),
		(val_mul, ":cur_production", 4),

				(val_mul, ":cur_production", ":number_of_items_in_town"),
		(val_mul, ":cur_production", 100),
		(val_div, ":cur_production", ":total_production"),
				(set_item_probability_in_merchandise, ":cur_goods", ":cur_production"),						  
			(try_end),

		(troop_clear_inventory, ":cur_merchant"),
			(troop_add_merchandise, ":cur_merchant", itp_type_goods, ":number_of_items_in_town"),

			(troop_ensure_inventory_space, ":cur_merchant", 20),
			(troop_sort_inventory, ":cur_merchant"),
			(store_troop_gold, ":cur_gold",":cur_merchant"),
			(lt,":cur_gold",1500),
			(store_random_in_range,":new_gold",500,1000),
			(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end), 	
	]), 
		
	# script_refresh_center_armories
	("refresh_center_armories",
	[
		(reset_item_probabilities, 100),
	(set_merchandise_modifier_quality, 150),    
	(try_for_range, ":cur_merchant", armor_merchants_begin, armor_merchants_end),    
		(store_sub, ":cur_town", ":cur_merchant", armor_merchants_begin),
		(val_add, ":cur_town", towns_begin),
		(troop_clear_inventory, ":cur_merchant"),
		(party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
		#tom
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 16),
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 16),
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_foot_armor, 8),
		# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_hand_armor, 4),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 2),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 2),
		(faction_get_slot, ":culture", ":cur_faction", slot_faction_culture),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_body_armor, 16),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_head_armor, 16),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_foot_armor, 8),
		(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_hand_armor, 4),
		#tom
		(troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
		(troop_sort_inventory, ":cur_merchant"),
		(store_troop_gold, reg6, ":cur_merchant"),
		(lt, reg6, 1000),
		(store_random_in_range, ":new_gold", 250, 500),
		(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(end_try),
	]),

	# script_refresh_center_weaponsmiths
	("refresh_center_weaponsmiths",
	[
		(reset_item_probabilities, 100),
		(set_merchandise_modifier_quality, 150),
		(try_for_range, ":cur_merchant", weapon_merchants_begin, weapon_merchants_end),
		(store_sub, ":cur_town", ":cur_merchant", weapon_merchants_begin),
			(val_add, ":cur_town", towns_begin), 
		(troop_clear_inventory, ":cur_merchant"),
			(party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
		#tom
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 6),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 4),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 3),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 5),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_arrows, 2),
			# (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bolts, 2),	  
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 1),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 1),
		(faction_get_slot, ":culture", ":cur_faction", slot_faction_culture),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_one_handed_wpn, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_two_handed_wpn, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_polearm, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_shield, 6),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_bow, 4),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_crossbow, 3),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_thrown, 5),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_arrows, 2),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_bolts, 2),	  
		#tom
			(troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
			(troop_sort_inventory, ":cur_merchant"), 
			(store_troop_gold, reg6, ":cur_merchant"),
			(lt, reg6, 1000),
			(store_random_in_range, ":new_gold", 250, 500),
			(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end),
	]),

	# script_refresh_center_stables
	("refresh_center_stables",
	[
		(reset_item_probabilities, 100),
		(set_merchandise_modifier_quality, 150),
		(try_for_range, ":cur_merchant", horse_merchants_begin, horse_merchants_end),
		(troop_clear_inventory, ":cur_merchant"),
			(store_sub, ":cur_town", ":cur_merchant", horse_merchants_begin),
			(val_add, ":cur_town", towns_begin),
			(party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
		#tom
			#(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 20),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 2),
		(faction_get_slot, ":culture", ":cur_faction", slot_faction_culture),
			(troop_add_merchandise_with_faction, ":cur_merchant", ":culture", itp_type_horse, 20),
		#tom
			(troop_ensure_inventory_space, ":cur_merchant", 65),
			(troop_sort_inventory, ":cur_merchant"),
			(store_troop_gold, ":cur_gold", ":cur_merchant"),
			(lt, ":cur_gold", 600),
			(store_random_in_range, ":new_gold", 250, 500),
			(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end),
	]),
		
	("tom_command_cheer", #tom made
	[
		(get_player_agent_no, ":player"),
		(agent_get_team, ":team", ":player"),
		(try_for_range, ":class", 0, 9),
		(try_begin),
			(class_is_listening_order, ":team", ":class"),
			(try_for_agents, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_is_human, ":agent"),
			(agent_get_class, ":agent_class", ":agent"),
			(eq, ":agent_class", ":class"),
			(agent_get_simple_behavior,":state",":agent"),
			(neq,":state",aisb_melee),
			(agent_play_sound, ":agent", "snd_man_victory"),
			(try_end),
			(assign, ":class", 11),
		(try_end),
	]),
	
	#script_update_manor_infested_by_bandits
	#input: none
	#output: none
	#description: updates the manors with possible crysis. Called from triggers
	 ("update_manor_infested_by_bandits",
	 [
		#0 - none
		#1 - regular bandits
		#2 - mercenery band rampaging
		#3 - two nobles conflicting
		#4 - angry peasents are angry for some reason
		#5 - 
		(troop_get_slot,":manor_amount","trp_manor_array",0),
		(try_for_range, ":slot", 1, ":manor_amount"),
			(troop_get_slot,":manor","trp_manor_array",":slot"),
		(party_clear, ":manor"),
		(party_set_slot, ":manor", slot_village_state, svs_normal),
		(store_random_in_range, ":random", 0, 100),
		(party_clear_particle_systems, ":manor"),
		#manors with walls does not get infested(unique manors that is)
		(try_begin),
			(party_slot_eq, ":manor", manor_slot_walls, manor_building_operational),
			(assign, ":random", 0), #not infested
		(try_end),
		(try_begin), #monastery does not get infested
			(party_get_template_id, ":manor_template", ":manor"),
			(eq, ":manor_template", "pt_monastery"),
			(assign, ":random", 0), #not infested
		(try_end),
		
		#note manor bandits work diffrently from villages. We store id of the crysis, insted of the troop infesting it.
		
		(try_begin),
			(lt, ":random", 80), 
			(party_set_slot,":manor",slot_village_infested_by_bandits, 0),
			(party_clear_particle_systems, ":manor"),
		(else_try),
			(store_random_in_range, ":random", 1, 3),
			(party_set_slot,":manor",slot_village_infested_by_bandits,":random"),
			#(party_add_particle_system, ":manor", "psys_map_village_fire"),
					(party_add_particle_system, ":manor", "psys_map_village_fire_smoke"),
			(try_end),
		(try_end),
	 ]),
	 
	 #script_get_mercenary_troop_for_manor - tom made
	 #input: faction of the manor
	 #output: reg0 - troop id
	 #called to determine the faction mercenary troop, to raid the center. Does not include the special troops, such as the varangian guard
	 ("get_mercenary_troop_for_manor",
	 [
			(store_script_param, ":fac", 1),
			 
		(assign, ":troop_no", "trp_merc_euro_spearman"),
		(try_begin),
			(call_script, "script_cf_select_random_town_with_faction", ":fac"),
			(assign, ":town_no", reg0),
			(gt, ":town_no", 0),
			#(party_get_slot, ":regional_mercs", ":town_no", slot_regional_mercs),
			(assign, ":merc_slot", slot_regional_mercs),
			(try_begin),
				(party_slot_eq, ":town_no", ":merc_slot", generic_euro),
				(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_balt),
				(store_random_in_range, ":troop_no", "trp_merc_balt_spearman", "trp_merc_mamluke_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_maghreb),
				(store_random_in_range, ":troop_no", "trp_merc_maghreb_spearman", "trp_merc_rus_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_rus),
				(store_random_in_range, ":troop_no", "trp_merc_rus_spearman", "trp_merc_latin_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_latin),
				(store_random_in_range, ":troop_no", "trp_merc_latin_spearman", "trp_merc_balkan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_balkan),
				(store_random_in_range, ":troop_no", "trp_merc_balkan_spearman", "trp_merc_scan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_scandinavian),
				(store_random_in_range, ":troop_no", "trp_merc_scan_spearman", "trp_merc_gaelic_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_gaelic),
				(store_random_in_range, ":troop_no", "trp_merc_gaelic_spearman", "trp_genoese_crossbowman"),
			(else_try),
				(party_slot_eq, ":town_no", ":merc_slot", generic_mamluk),
				(store_random_in_range, ":troop_no", "trp_merc_mamluke_spearman", "trp_merc_maghreb_spearman"),
			(try_end),
		(try_end),
		(assign, reg0, ":troop_no"),
	 ]),
	 
	 
		# script_init_manor_agents #init_town_walkers as template
		# Input: manor_id
		# Output: none
		("init_manor_agents",
			[
		(store_script_param, ":manor_id", 1),

			(party_get_slot, ":village", ":manor_id", slot_village_bound_center), 
			(party_get_slot, ":village_lord", ":village", slot_town_lord), 
		
		(store_faction_of_party, ":manor_faction", ":manor_id"),
		(try_begin),
			(eq, ":manor_faction", "fac_player_supporters_faction"),
			(assign, ":manor_faction", "$g_player_culture"),
		(try_end),
		(party_get_slot, ":population", ":manor_id", manor_slot_population),
		(try_begin),
			(le, ":population", 200),
			(assign, ":peasents", 1),
			(assign, ":burgers", 0),
			(assign, ":nobles", 0),
		(else_try),
			(le, ":population", 400),
			(assign, ":peasents", 2),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 1),
				(assign, ":nobles", 0),
			(try_end),
		(else_try),
			(le, ":population", 600),
			(assign, ":peasents", 3),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 2),
				(assign, ":nobles", 0),  
			(try_end),
		(else_try),
			(le, ":population", 800),
			(assign, ":peasents", 4),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 3),
				(assign, ":nobles", 0),
			(try_end),
		(else_try),
			(gt, ":population", 800),
			(assign, ":peasents", 4),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 4),
				(assign, ":nobles", 1),  
			(try_end),
		(try_end),
			# (assign, ":peasents", 4),
		# (assign, ":burgers", 4),
		# (assign, ":nobles", 1),
		(try_begin),
			(eq, ":village_lord", "trp_player"),
				(set_visitor, 10, "trp_manor_seneschal"),
			(set_visitor, 11, "trp_manor_storage"),
			(set_visitor, 12, "trp_manor_marshal"),
		(try_end),
		
				(try_begin), #daytime
					(eq, "$town_nighttime", 0),
			(faction_get_slot,":culture",":manor_faction",slot_faction_culture),
			(faction_get_slot,":walker1",":culture",slot_faction_village_walker_male_troop),
			(faction_get_slot,":walker2",":culture",slot_faction_village_walker_female_troop),
					(try_for_range, ":entry_no", 31, 40), #peasents
				(try_for_range, reg0, 0, ":peasents"),
				#(store_random_in_range, ":random", 0, 6),
				#(store_add, ":troop", ":random", "trp_manor_peasent"),
				(store_random_in_range, ":troop", ":walker1", ":walker2"),
				(set_visitor, ":entry_no", ":troop"),
				# (try_begin),
					# (eq, ":random", 0),
								# (set_visitor, ":entry_no", "trp_manor_peasent", ":peasents"),
				# (else_try),
					# (set_visitor, ":entry_no", "trp_manor_peasent2", ":peasents"),
				# (try_end),
			(try_end), 
					(try_end), 
			(faction_get_slot,":culture",":manor_faction",slot_faction_culture),
			(faction_get_slot,":walker1",":culture",slot_faction_town_walker_male_troop),
			(faction_get_slot,":walker2",":culture",slot_faction_town_walker_female_troop),
			(try_for_range, ":entry_no", 20, 25), #burgers
				(try_for_range, reg0, 0, ":burgers"),
					(store_random_in_range, ":troop", ":walker1", ":walker2"),
				(set_visitor, ":entry_no", ":troop"),
			(try_end),
					(try_end), 
			
			(try_for_range, ":entry_no", 25, 30), #nobles
				(try_for_range, reg0, 0, ":nobles"),
				(store_add, ":troop_upper", "trp_manor_noble2", 1),
					(store_random_in_range, ":troop", "trp_manor_noble", ":troop_upper"),
				#(store_add, ":troop", ":random", "trp_manor_noble"),
				(set_visitor, ":entry_no", ":troop"),
			(try_end),
					(try_end), 
			
			#pedlers and craftsman
			(try_for_range, ":slot", 0, manor_slot_prison - manor_slot_grainfarm),
				(store_add, ":building_slot", ":slot", manor_slot_grainfarm),
			(store_add, ":entry_point", ":slot", 41),
			(store_add, ":troop", ":slot", "trp_manor_grain"),
				(party_slot_eq, "$g_encountered_party", ":building_slot", manor_building_operational),
			(set_visitor, ":entry_point", ":troop"),
			(party_slot_eq, "$g_encountered_party", manor_slot_marketplace, manor_building_operational),
			(store_add, ":entry_point", ":slot", 81),
			(set_visitor, ":entry_point", "trp_manor_seller"),
					(try_end),
			
			#priest
			(faction_get_slot, ":religion", ":manor_faction", slot_faction_religion),
			(try_begin),
				#(eq, ":village_lord", "trp_player"),
				(party_slot_eq, "$g_encountered_party", manor_slot_Monastery, manor_building_operational),
			(store_add, ":troop", ":religion", "trp_priest_catholic"),
				(set_visitor, 71, ":troop"),
			(try_end),
			
			#armor weapon fletcher stables - need to do order
			(try_for_range, ":slot", 0, 4),
				 #(eq, ":village_lord", "trp_player"),
				 (store_add, ":building_slot", ":slot", manor_slot_armorsmith),
			 (store_add, ":troop", ":slot", "trp_manor_armorsmith"),
			 (store_add, ":entry_point", ":slot", 13),
				 (party_slot_eq, "$g_encountered_party", ":building_slot", manor_building_operational),
			 (set_visitor, ":entry_point", ":troop"),
			(try_end),
			
			#traders
			(try_begin),
				(eq, ":village_lord", "trp_player"),
				#(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, -1),
			(party_get_slot, ":troop", "$g_encountered_party", manor_slot_trader),
			(gt, ":troop", 0),
			(set_visitor, 72, ":troop"),
			(try_end),
			
			#bookseler or crusader?
			(try_begin),
				(eq, ":village_lord", "trp_player"),
				#(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, -1),
			(party_slot_eq, "$g_encountered_party", manor_slot_Monastery_upgrade, manor_Monastery_scriptorium),
			(set_visitor, 73, "trp_manor_trader_book"),
			(try_end),
				(try_end),
		
		(try_begin), #night or day
			(try_begin),
				(party_slot_eq, "$g_encountered_party", manor_slot_whorehouse, manor_building_operational),
				(set_visitor, 70, "trp_whore"),
			(try_end),
			
			 #merc dirty code ministrel
			 (try_for_range, ":entry_point", 66, 70),
				(party_slot_eq, "$g_encountered_party", manor_slot_tavern, manor_building_operational),
			 
			 (store_random_in_range, ":random", "trp_tavern_minstrel_1", "trp_kingdom_heroes_including_player_begin"),
			 (set_visitor, ":entry_point", ":random"),
			#(call_script, "script_get_mercenary_troop_for_manor", ":manor_faction"),
			#(set_visitor, ":entry_point", reg0),
					(try_end),
			
			#guard dirty code
			(faction_get_slot, ":troop" ,":manor_faction", slot_faction_tier_2_troop),
			(try_for_range, ":entry_point", 60, 66),
				(party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_operational),
				(set_visitor, ":entry_point", ":troop"),
			(try_end),
			
			#prison
			(try_begin),
				(party_slot_eq, "$g_encountered_party", manor_slot_prison, manor_building_operational),
				(store_random_in_range, ":troop", "trp_ransom_broker_1", "trp_tavern_traveler_1"),
			(set_visitor, 17, ":troop"),
			(try_end),
			
		(try_end),
		]),
	
	# script_manor_refresh_inventories
		# Input: manor_id
		# Output: none
	("manor_refresh_inventories",
	[
		(store_script_param, ":manor_id", 1),
		(party_get_slot, ":village", ":manor_id", slot_village_bound_center), 
		#(store_faction_of_party, ":cur_faction", ":manor_id"),
		(party_get_slot, ":cur_faction", ":village", slot_center_original_faction),
		(reset_item_probabilities, 100),
			(set_merchandise_modifier_quality, 150),
		
		###ARMOR
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_armorsmith,manor_building_operational),
			(troop_clear_inventory, "trp_manor_armorsmith"),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_body_armor, 16),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_head_armor, 16),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_foot_armor, 8),
			(troop_add_merchandise_with_faction, "trp_manor_armorsmith", ":cur_faction", itp_type_hand_armor, 4),
		(troop_ensure_inventory_space, "trp_manor_armorsmith", 30),
				(troop_sort_inventory, "trp_manor_armorsmith"),
		## gold
		(store_troop_gold, reg6, "trp_manor_armorsmith"),
		(troop_remove_gold,"trp_manor_armorsmith",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_armorsmith", ":new_gold"),
		(try_end),
		###ARMOR END
		###WEAPONS
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_weaponsmith,manor_building_operational),
		(troop_clear_inventory, "trp_manor_weaponsmith"),
			(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_one_handed_wpn, 5),
				(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_two_handed_wpn, 5),
				(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_polearm, 5),
				(troop_add_merchandise_with_faction, "trp_manor_weaponsmith", ":cur_faction", itp_type_shield, 6),
				(troop_ensure_inventory_space, "trp_manor_weaponsmith", 30),
				(troop_sort_inventory, "trp_manor_weaponsmith"),
		##gold
		(store_troop_gold, reg6, "trp_manor_weaponsmith"),
		(troop_remove_gold,"trp_manor_weaponsmith",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_weaponsmith", ":new_gold"),
			(try_end),
		###WEAPON END
		###FLETCHER
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_fletcher,manor_building_operational),
		(troop_clear_inventory, "trp_manor_fletcher"),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_bow, 4),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_crossbow, 3),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_thrown, 5),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_arrows, 2),
				(troop_add_merchandise_with_faction, "trp_manor_fletcher", ":cur_faction", itp_type_bolts, 2),
				(troop_ensure_inventory_space, "trp_manor_fletcher", 30),
				(troop_sort_inventory, "trp_manor_fletcher"),
		##gold
		(store_troop_gold, reg6, "trp_manor_fletcher"),
		(troop_remove_gold,"trp_manor_fletcher",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_fletcher", ":new_gold"),
		(try_end),
		###FLETCHER END
		###STABLE
		(try_begin),
			(party_slot_eq,":manor_id",manor_slot_breeder,manor_building_operational),
		(troop_clear_inventory, "trp_manor_breeder"),
		(troop_add_merchandise_with_faction, "trp_manor_breeder", ":cur_faction", itp_type_horse, 20),
		(troop_ensure_inventory_space, "trp_manor_breeder", 30),
				(troop_sort_inventory, "trp_manor_breeder"),
		##gold
		(store_troop_gold, reg6, "trp_manor_breeder"),
		(troop_remove_gold,"trp_manor_breeder",reg6),
		(store_random_in_range, ":new_gold", 250, 500),
				(call_script, "script_troop_add_gold", "trp_manor_breeder", ":new_gold"),
		(try_end),
		###STABLE END
		###OTHER CRAPERS
		(try_for_range, ":cur_merchant", trp_manor_grain, trp_manor_tanner+1),
			(troop_get_slot, ":goods", ":cur_merchant", manor_troop_slot_good),
		(troop_clear_inventory, ":cur_merchant"),
		(store_random_in_range, ":good_amount", 2, 5),
		(troop_add_items,":cur_merchant",":goods",":good_amount"),
		(troop_ensure_inventory_space, ":cur_merchant", 20),
		(troop_sort_inventory, ":cur_merchant"),
		## gold
			(store_troop_gold, reg6, ":cur_merchant"),
		(troop_remove_gold,":cur_merchant",reg6),
		(store_random_in_range, ":new_gold", 150, 300),
				(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
		(try_end),
		###OTHER CRAPERS END
	]),
	
	# script_init_town_walker_agents
		# Input: none
		# Output: none
		("init_manor_walker_agents",
			[(assign, ":num_walkers", 0),
				(try_for_agents, ":cur_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			# (try_begin),
				# (eq, ":cur_troop", "trp_manor_seneschal"),
				# (agent_set_stand_animation, ":cur_agent", "anim_sit_drink"),
			
			# (entry_point_get_position, pos0, 11 ),
			# (agent_set_look_target_position, ":cur_agent", pos0), 
			# (try_end),
			(this_or_next|is_between, ":cur_troop", walkers_begin, walkers_end),
					(this_or_next|is_between, ":cur_troop", "trp_manor_noble", "trp_manor_trader_silk"), #manor walkers
			(is_between, ":cur_troop", "trp_farmer", "trp_kingdom_heroes_including_player_begin"), #manor walkers
			(neg|is_between, ":cur_troop", "trp_ransom_broker_1", "trp_tavern_traveler_1"), #manor walkers
					(val_add, ":num_walkers", 1),
					(agent_get_position, pos1, ":cur_agent"),
			
			(store_random_in_range, ":r", 0, 2),
			(try_begin),
				(eq, ":r", 0),
				(store_random_in_range, ":i_e_p", 20, 72),
			(else_try),
				(store_random_in_range, ":i_e_p", 81, 95),
			(try_end),
			
					#(try_for_range, ":i_e_p", 20, 94),#Entry points
			#  (neg|is_between, ":i_e_p", 73, 81),
						#(entry_point_get_position, pos2, ":i_e_p"),
						#(get_distance_between_positions, ":distance", pos1, pos2),
						#(lt, ":distance", 200),
						(agent_set_slot, ":cur_agent", 0, ":i_e_p"),
				 # (try_end),
					(call_script, "script_set_town_walker_destination", ":cur_agent"),
				(try_end),
		]),
	
	# script_tick_manor_walkers
		# Input: none
		# Output: none
		("tick_manor_walkers",
			[
			(try_for_agents, ":cur_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(this_or_next|is_between, ":cur_troop", walkers_begin, walkers_end),
					(this_or_next|is_between, ":cur_troop", "trp_manor_noble", "trp_manor_trader_silk"), #manor walkers
			(is_between, ":cur_troop", "trp_farmer", "trp_kingdom_heroes_including_player_begin"), #manor walkers
					(agent_get_slot, ":target_entry_point", ":cur_agent", 0),
					(entry_point_get_position, pos1, ":target_entry_point"),
					(try_begin),
						#(lt, ":target_entry_point", 32),
			(this_or_next|is_between, ":target_entry_point", 41, 61), #manor walkers
				(is_between, ":target_entry_point", 80, 95), 
			
						(init_position, pos2),
						(position_set_y, pos2, 250),
						(position_transform_position_to_parent, pos1, pos1, pos2),
					(try_end),
					(agent_get_position, pos2, ":cur_agent"),
					(get_distance_between_positions, ":distance", pos1, pos2),
					(lt, ":distance", 400),
					(assign, ":random_no", 0),
					(try_begin),
						#(lt, ":target_entry_point", 32),
			(this_or_next|is_between, ":target_entry_point", 41, 61), #manor walkers
				(is_between, ":target_entry_point", 80, 95), 
			
						(store_random_in_range, ":random_no", 0, 100),
					(try_end),
					(lt, ":random_no", 20),
					(call_script, "script_set_town_walker_destination", ":cur_agent"),
				(try_end),
		]),
	
	#script_select_mercenary_troop - tom made
		# INPUT: arg1 = center_no
		# OUTPUT: reg1 = troop_no
	("select_mercenary_troop",
	[
			(store_script_param, ":town_no", 1),
		
			(assign, ":troop_no", "trp_merc_euro_spearman"),
			#(party_get_slot, ":regional_mercs", ":town_no", slot_regional_mercs),
			(try_begin),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_euro),
				(store_random_in_range, ":troop_no", "trp_merc_euro_spearman", "trp_merc_balt_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_balt),
				(store_random_in_range, ":troop_no", "trp_merc_balt_spearman", "trp_merc_maghreb_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_maghreb),
				(store_random_in_range, ":troop_no", "trp_merc_maghreb_spearman", "trp_merc_rus_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_rus),
				(store_random_in_range, ":troop_no", "trp_merc_rus_spearman", "trp_merc_latin_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_latin),
				(store_random_in_range, ":troop_no", "trp_merc_latin_spearman", "trp_merc_balkan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_balkan),
				(store_random_in_range, ":troop_no", "trp_merc_balkan_spearman", "trp_merc_scan_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_scandinavian),
				(store_random_in_range, ":troop_no", "trp_merc_scan_spearman", "trp_merc_gaelic_spearman"),
			(else_try),
				(party_slot_eq, ":town_no", slot_regional_mercs, generic_gaelic),
				(store_random_in_range, ":troop_no", "trp_merc_gaelic_spearman", "trp_genoese_crossbowman"),
			(try_end),
		
			(assign, reg0, ":troop_no"),
	]),

	##script_cf_recruit_individual_merc - tom made
	#description: recruits several troops of the center the lord is in
	#input: party_no to recruit to
	#output: none
	#TODO: crusaders, mercs
		("cf_recruit_individual_merc", #tom-made
			[
			(store_script_param, ":party_no", 1),

		(party_get_attached_to, ":no_center", ":party_no"),
		(is_between, ":no_center", walled_centers_begin, walled_centers_end),
		(try_begin),
			(store_random_in_range, ":random", 1, 10), #more for merc hiring
			(call_script, "script_select_mercenary_troop", ":no_center"),
			(assign, ":troop", reg1),
			###(gt, ":troop", "trp_farmer"),
			(gt, ":troop", "trp_player"),
			(party_add_members, ":party_no", ":troop", ":random"),
		(try_end),		
		]
	),
	
	##script_cf_recruit_merc_lance_for_npc - tom made
	#description: selects a owned center of the lord and then recruits lance
	#input: party_no to recruit to.
	#output: none
	#TODO: crusaders, mercs
		("cf_recruit_merc_lance_for_npc", #tom-made
			[
			(store_script_param, ":party_no", 1),

		(store_faction_of_party, ":party_faction", ":party_no"),
		#####(assign, ":party_faction", "fac_kingdom_23"),
		
		#select center to recruit from
		(call_script, "script_cf_select_random_town_with_faction", ":party_faction"),
		(gt, reg0, 0),
		(assign, ":no_center", reg0),
		
		(party_get_slot,":mercs_generic", ":no_center", slot_regional_mercs),
		(party_get_slot,":mercs1", ":no_center", slot_spec_mercs1),
		(party_get_slot,":mercs2", ":no_center", slot_spec_mercs2),
		
		(party_get_slot,":mercs_generic_number", ":no_center", slot_regional_mercs_number_npc),
		(party_get_slot,":mercs1_number", ":no_center", slot_spec_mercs1_number_npc),
		(party_get_slot,":mercs2_number", ":no_center", slot_spec_mercs2_number_npc),
		
		(assign, ":slot_to_recruit_from", -1), #recruit from generic mercs
		(try_begin),
			(gt, ":mercs2", 0), #generic should be guaranteed, special not
			(gt, ":mercs2_number", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(assign, ":slot_to_recruit_from", slot_spec_mercs2),
			(val_sub, ":mercs2_number", 1),
				(party_set_slot, ":no_center", slot_regional_mercs_number_npc, ":mercs2_number"),
		(else_try),
			(gt, ":mercs1", 0), #generic should be guaranteed, special not
			(gt, ":mercs1_number", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(assign, ":slot_to_recruit_from", slot_spec_mercs1),
			(val_sub, ":mercs1_number", 1),
			(party_set_slot, ":no_center", slot_spec_mercs1_number_npc, ":mercs1_number"),
		(else_try),
			(gt, ":mercs_generic", 0), #generic should be guaranteed
			(gt, ":mercs_generic_number", 0), 
			(assign, ":slot_to_recruit_from", slot_regional_mercs),
			(val_sub, ":mercs_generic_number", 1),
			(party_set_slot, ":no_center", slot_spec_mercs2_number_npc, ":mercs_generic_number"),
		(try_end),
		
		(gt, ":slot_to_recruit_from", -1),
		(call_script, "script_fill_company", ":no_center", ":party_no", ":slot_to_recruit_from"),  
		
			##hire some individual mercs - todo
		# (try_begin),
			# (store_random_in_range, ":random", 1, 10), #more for merc hiring
			# (gt, ":random", 0),
			# (call_script, "script_select_mercenary_troop", ":no_center"),
			# (assign, ":troop", reg1),
			# (gt, ":troop", "trp_farmer"),
			# (party_add_members, ":party_no", ":troop", ":random"),
		# (try_end),		
		]
	),
	
	##script_cf_recruit_lance_for_npc - tom made
	#description: selects a owned center of the lord and then recruits lance
	#input: party_no to recruit to.
	#output: none
	#TODO: crusaders, mercs
	("cf_recruit_lance_for_npc", #tom-made
			[
			(store_script_param, ":party_no", 1),

		#(store_faction_of_party, ":party_faction", ":party_no"),
		(party_get_slot, ":party_type",":party_no", slot_party_type),
		
		(assign, ":leader", -1),
				(try_begin),
					(eq, ":party_type", spt_kingdom_hero_party),
					(party_stack_get_troop_id, ":leader", ":party_no"),
				(try_end),
		
		#(neq, ":leader", -1),
		#select center to recruit from
		(assign, ":no_center", -1), #for funny future merc recruitment
		(assign, ":recruit_amount", 2),
		(assign, ":top_range", centers_end),
		(try_for_range, ":center", centers_begin, ":top_range"),
			(this_or_next|neg|party_slot_ge, ":center", slot_center_is_besieged_by, 1),
			(neg|party_slot_eq, ":center", slot_village_state, svs_being_raided),
			(party_get_slot, ":town_lord", ":center", slot_town_lord),
			(eq, ":town_lord", ":leader"),
			(party_get_slot, ":lances_available", ":center", slot_feudal_lances),
			(gt, ":lances_available", 0),
			(call_script, "script_fill_lance", ":center", ":party_no"),
			(val_sub, ":lances_available", 1),
			(party_set_slot, ":center", slot_feudal_lances, ":lances_available"),
			(assign, ":no_center", ":center"),
			(val_sub, ":recruit_amount", 1),
			(eq, ":recruit_amount", 0),
			(assign, ":top_range", -1), #break
		(try_end),
		
		(gt, ":no_center", 0),
		#later - merc company hiring #TODO seperate thing in the future
		# (store_party_size, ":size" ,":party_no"),
		# (try_begin),
			# (eq, ":center", -1),
			# (try_for_range, ":center2", centers_begin, centers_end),
				# (store_faction_of_party, ":center_faction", ":center2"),
			# (eq, ":center_faction", ":party_faction"),
			# (assign, ":center", ":center2"),
			# (assign, ":center2", -1),
			# (try_end),
			# (neq, ":center", -1),
			# (lt, ":size", 50), 
			# (call_script, "script_fill_lance", ":center", ":party_no"),
		# (try_end),
		
			#hire some individual mercs - todo. This is obsolete, selects volunteers instead
		# (try_begin),
			# (store_random_in_range, ":random", 0, 2),
			# (gt, ":random", 0),
			# (call_script, "script_select_mercenary_troop", ":no_center"),
			# (assign, ":troop", reg1),
			# (gt, ":troop", "trp_farmer"),
			# (party_add_members, ":party_no", ":troop", ":random"),
		# (try_end),		
		]
	),
	
	#script_get_random_merc_company_from_center
	#input: center
	#output: reg0 random merc company
	#decription: gets a random mect company from the specified center. Does not consume merc resources. Used for kingdom parties
	("get_random_merc_company_from_center",
	 [
		(store_script_param, ":center", 1),
		
		(party_get_slot,":mercs_generic", ":center", slot_regional_mercs),
		(party_get_slot,":mercs1", ":center", slot_spec_mercs1),
		(party_get_slot,":mercs2", ":center", slot_spec_mercs2),
		
		#(assign, ":template", 0),
		(try_begin),
			(gt, ":mercs2", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs2_party_template),
		(else_try),
			(gt, ":mercs1", 0), #generic should be guaranteed, special not
			(store_random_in_range, ":random", 0, 2),
			(eq, ":random", 0),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs1_party_template),
		(else_try),
			(gt, ":mercs_generic", 0), #generic should be guaranteed
			(party_get_slot, ":company_template", ":center", slot_regional_party_template),
		(try_end),
		
		(assign, reg0, ":company_template"),
	 ]
	),
	
	
	#script_get_orig_culture
	#description: auxilary script to get the culture to recruit troops
	#input: original faction, cur faction, original culture
	#output reg0 - culture to use for troops
	("get_orig_culture",
		[
			(store_script_param, ":orig_faction", 1),
		(store_script_param, ":cur_faction", 2),
		(store_script_param, ":orig_culture", 3),
		
			(try_begin), #balts under teutons
				(this_or_next|eq, ":orig_culture", "fac_culture_baltic"),
			(eq, ":orig_culture", "fac_culture_finnish"),
			(eq, ":cur_faction", "fac_kingdom_1"), #set to teutonic
			(assign, ":orig_culture", "fac_culture_teutonic"),
		(else_try), #latin
			(eq, ":orig_culture", "fac_culture_byzantium"),
			(eq, ":cur_faction", "fac_kingdom_26"),
			(assign, ":orig_culture", "fac_culture_italian"),
		(else_try), # if crusader states conquers arabians
			# (this_or_next|eq, ":orig_faction", "fac_kingdom_25"), ##mamluks
				# (eq, ":orig_faction", "fac_kingdom_28"), ##Hafsid
			(eq, ":cur_faction", "fac_kingdom_23"), #and now they are crusader
			(assign, ":orig_culture", "fac_culture_western"),  #crusader culture
		(else_try),
			(eq, ":orig_faction", "fac_kingdom_23"), #if originaly crusader states
			(neq, ":cur_faction", "fac_kingdom_23"), #but no longer theres
			(assign, ":orig_culture", "fac_culture_mamluke"),  #mamluk culture
		# (else_try), #anatolians - armenians and turks
			# (this_or_next|eq, ":orig_culture", "fac_culture_anatolian"), 
			# (eq, ":orig_culture", "fac_culture_anatolian_christian"), 
			# (eq, ":cur_faction", "fac_kingdom_27"),
			
		(try_end),
		(assign, reg0, ":orig_culture"),
		]
	),
	
	#script_check_agents_for_lances
	#description: checks all the agents on the battlefield and removes the dead ones from the arrays.
	#input: none
	#output: none
	("check_agents_for_lances",
		[
			(get_player_agent_no,":p_agent"),
			(try_for_agents, ":cur_agent"),
			(neg|agent_slot_eq, ":cur_agent", slot_possessed, 1), #not a waste
			(neg|agent_is_alive, ":cur_agent"),
			(neg|agent_is_wounded, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_get_party_id, ":agent_party", ":cur_agent"),
			(eq, ":agent_party", "p_main_party"),
			(neq, ":p_agent", ":cur_agent"),
			(agent_get_slot, ":index", ":cur_agent", slot_index_value),
			(ge, ":index", 0),
			(troop_set_slot, "trp_lances_places",":index",0), #dead - remove
			(troop_set_slot, "trp_lances_troops",":index",0), #dead - remove
		(try_end),
		(call_script, "script_balance_lance_storage"),
		]
	),
	
	#script_balance_lance_storage
	#description: removes the dead troops in the lance storage. Both in reserve and the combatans
	#input: none
	#output:none
	("balance_lance_storage",
		[
		##COMBATANTS
		#copy to backup
		(assign, ":new_amount", 0),
		(try_for_range, ":index", 0, "$lance_troop_serving"),
			(troop_get_slot, ":troop","trp_lances_troops",":index"),
			(troop_get_slot, ":place","trp_lances_places",":index"),
			(gt, ":troop", 0),
			(troop_set_slot, "trp_temp_array_a", ":new_amount", ":troop"), #copy alive troops
			(troop_set_slot, "trp_temp_array_b", ":new_amount", ":place"), #copy alive troop hailings
			(val_add, ":new_amount", 1),
		(try_end),
		
		#copy it back adjused
		(assign, "$lance_troop_serving", ":new_amount"),
		(try_for_range, ":index", 0, "$lance_troop_serving"),
			(troop_get_slot, ":troop","trp_temp_array_a",":index"),
			(troop_get_slot, ":place","trp_temp_array_b",":index"),
			(troop_set_slot, "trp_lances_troops", ":index", ":troop"), #copy alive troops
			(troop_set_slot, "trp_lances_places", ":index", ":place"), #copy alive troop hailings
		(try_end),
	###########
	##RESERVE
			#copy to backup
		(assign, ":new_amount", 0),
		(try_for_range, ":index", 0, "$lance_troop_reserve"),
			(troop_get_slot, ":troop","trp_lances_troops_reserve",":index"),
			(troop_get_slot, ":place","trp_lances_places_reserve",":index"),
			(gt, ":troop", 0),
			(troop_set_slot, "trp_temp_array_a", ":new_amount", ":troop"), #copy alive troops
			(troop_set_slot, "trp_temp_array_b", ":new_amount", ":place"), #copy alive troop hailings
			(val_add, ":new_amount", 1),
		(try_end),
		
		#copy it back adjused
		(assign, "$lance_troop_reserve", ":new_amount"),
		(try_for_range, ":index", 0, "$lance_troop_reserve"),
			(troop_get_slot, ":troop","trp_temp_array_a",":index"),
			(troop_get_slot, ":place","trp_temp_array_b",":index"),
			(troop_set_slot, "trp_lances_troops_reserve", ":index", ":troop"), #copy alive troops
			(troop_set_slot, "trp_lances_places_reserve", ":index", ":place"), #copy alive troop hailings
		(try_end),
		]
	),
	
	
	##script_count_nobles_commoners_for_center
	##description: count nobles and commoners for each center. Increase lances if there are troop uncounted
	##input: none
	##output: none
	("count_nobles_commoners_for_center",
		[
		#clear slots
		(try_for_parties, ":party"),
			(party_set_slot, ":party", slot_number_commoner, 0),
			(party_set_slot, ":party", slot_number_nobles, 0),
			(party_get_slot, ":troop_amount" ,":party", slot_number_troops_pending), #get pending
			(party_set_slot, ":party", slot_number_troops_pending, 0), #reset pending
			(ge, ":troop_amount", 1), #there are uncounted ones
			(val_div, ":troop_amount", 10),
			(party_get_slot, ":lance_amount" ,":party", slot_feudal_lances), #get pending
			(val_add, ":lance_amount", ":troop_amount"),
			(party_set_slot, ":party", slot_feudal_lances, ":lance_amount"),
		(try_end),
		
		(try_for_range, ":index", 0, "$lance_troop_reserve"),
			(troop_get_slot, ":troop","trp_lances_troops_reserve",":index"),
			(troop_get_slot, ":place","trp_lances_places_reserve",":index"),
			
			(assign, ":top_faction", "fac_player_faction"),
			(try_for_range, ":culture", "fac_culture_finnish", ":top_faction"),
				(call_script, "script_troop_find_culture", ":troop", ":culture"),
				(ge, reg0, 0), #found a culture
				(try_begin), #noble tree!
					(eq, reg0, 2),
				(party_get_slot, ":amount",":place", slot_number_nobles),
				(val_add, ":amount", 1),
				(party_set_slot, ":place", slot_number_nobles, ":amount"),
				(else_try), #townsman
				(party_get_slot, ":amount",":place", slot_number_commoner),
				(val_add, ":amount", 1),
				(party_set_slot, ":place", slot_number_commoner, ":amount"),
				(try_end),
			(assign, ":top_faction", -1), #break culture cycle
			(try_end),
		(try_end),
		]
	),
	
	#script_get_noble_troop
	#input: center to earch for
	#output: reg1- the troop, -1 if not found
	("get_noble_troop",
		[
		(store_script_param, ":center", 1),
		
		(assign, reg1, -1),
		(assign, ":higher", "$lance_troop_reserve"),
		(try_for_range, ":index", 0, ":higher"), #spin trough all the reserve
			(troop_slot_eq, "trp_lances_places_reserve", ":index", ":center"), #matching center
			(troop_get_slot,":troop", "trp_lances_troops_reserve", ":index"), #get troop
			#(party_get_slot, ":culture", ":center", slot_center_culture),
			#(call_script, "script_troop_find_culture", ":troop", ":culture"),
			#(eq, reg0, 2), #found a noble!
			(assign, ":top_faction", "fac_player_faction"),
			(try_for_range, ":culture", "fac_culture_finnish", ":top_faction"),
				(call_script, "script_troop_find_culture", ":troop", ":culture"),
			(eq, reg0, 2), #found a noble!
			(assign, ":top_faction", -1),
			(try_end),
			(eq, reg0, 2), #found a noble!
			
			(troop_set_slot, "trp_lances_troops_reserve",":index", 0),
			(troop_set_slot, "trp_lances_places_reserve",":index", 0),
			(assign, reg1, ":troop"),
			(assign, ":higher", -1),
		(try_end),
		]
	),
	
	#script_get_commoner_troop
	#input: center to earch for
	#output: reg1- the troop, -1 if not found
	("get_commoner_troop",
		[
		(store_script_param, ":center", 1),
		
		(assign, reg1, -1),
		(assign, ":higher", "$lance_troop_reserve"),
		(try_for_range, ":index", 0, ":higher"), #spin trough all the reserve
			(troop_slot_eq, "trp_lances_places_reserve", ":index", ":center"), #matching center
			(troop_get_slot,":troop", "trp_lances_troops_reserve", ":index"), #get troop
			# (party_get_slot, ":culture", ":center", slot_center_culture),
			# (call_script, "script_troop_find_culture", ":troop", ":culture"),
			# (is_between, reg0, 0, 2), #found a commoner!
			
			(assign, ":top_faction", "fac_player_faction"),
			(try_for_range, ":culture", "fac_culture_finnish", ":top_faction"),
				(call_script, "script_troop_find_culture", ":troop", ":culture"),
			(is_between, reg0, 0, 2), #found a commoner!
			(assign, ":top_faction", -1),
			(try_end),
			(is_between, reg0, 0, 2), #found a commoner!
			
			(troop_set_slot, "trp_lances_troops_reserve",":index", 0),
			(troop_set_slot, "trp_lances_places_reserve",":index", 0),
			(assign, reg1, ":troop"),
			(assign, ":higher", -1),
		(try_end),
		]
	),
	
	
	#script_add_lance_troop_to_regulars
	#description: adds the current troop to regulars(serving in players party), increases the counter
	#input: troop, center recruited from
	#output: none
	("add_lance_troop_to_regulars",
		[
		(store_script_param, ":troop", 1), 
		(store_script_param, ":center", 2), 
		(troop_set_slot, "trp_lances_places", "$lance_troop_serving", ":center"),
		(troop_set_slot, "trp_lances_troops", "$lance_troop_serving", ":troop"),
		(val_add, "$lance_troop_serving", 1),
		]
	),
	
	#script_search_for_troop
	#description: searches for such a troop in service and returns the it's index in the array
	#input: troop
	#output: reg0- troop index at the array
	("search_for_troop",
		[
		(store_script_param, ":troop", 1),
		
		(assign, reg0, -1),
		(assign, ":higher", "$lance_troop_serving"),
		(try_for_range, ":index", 0, ":higher"), 
			(troop_slot_eq, "trp_lances_troop_in_combat", ":index", 0), #is not flaged yet
			(troop_slot_eq, "trp_lances_troops", ":index", ":troop"), #the troop matches
			(assign, reg0, ":index"),
			(troop_set_slot, "trp_lances_troop_in_combat", ":index", 1),
			(assign, ":higher", -1), #break
		(try_end),
		]
	),
	
	#script_clear_troop_array
	#description: clears the troop array
	#input: troop, begin_index, end_index
	#output: none
	("clear_troop_array",
		[
		(store_script_param, ":troop_array", 1),
		(store_script_param, ":begin_index", 2),
		(store_script_param, ":end_index", 3),
		(try_for_range, ":index", ":begin_index", ":end_index"),
			(troop_set_slot, ":troop_array", ":index", 0),
		(try_end),
		]
	),
	
	#script_fill_lance
	#description: select the troop for recruitment
	#input: spawn_center, party_to_fill
	#output: spawned party_id
	("fill_lance",
			[
			(store_script_param, ":center", 1), #party to recruit from
		(store_script_param, ":spawned_party", 2), #party to fill with troops
		#(store_script_param, ":type", 2),  #
		#(store_script_param, ":fac", 3), 
		 
		#get prosperity, original faction
		(party_get_slot, ":orig_faction", ":center", slot_center_original_faction),

		(party_get_slot, ":orig_culture", ":center", slot_center_culture),
		(party_get_slot, ":prosperity", ":center", slot_town_prosperity),
		(party_get_slot, ":nobles", ":center", slot_center_nobility_law),
		(party_get_slot, ":regulars", ":center", slot_center_commoner_law),
		(party_stack_get_troop_id, ":leader", ":spawned_party"),
		(store_faction_of_party, ":cur_faction", ":center"),
		
		#check for minor cultures - update this for regular system as well
		(call_script, "script_get_orig_culture", ":orig_faction", ":cur_faction", ":orig_culture"),
		(assign, ":orig_culture", reg0),
		
		#based on prosperity design assign the chances 
		# (try_begin), #low
			# (lt, ":prosperity", 25),
			# (assign, ":tier1", 50),
			# (assign, ":tier2", 85),
			# (assign, ":tier3", 95),
			# (assign, ":tier4", 95),
			# #(display_message, "@low"),
		# (else_try), #avg
			# #(ge, ":prosperity", 25),
			# (lt, ":prosperity", 75),
			# (assign, ":tier1", 30),
			# (assign, ":tier2", 80),
			# (assign, ":tier3", 95),
			# (assign, ":tier4", 95),
			# #(display_message, "@avg"),
		# (else_try), #high
		 # # (ge, ":prosperity", 75),
			# (assign, ":tier1", 10),
			# (assign, ":tier2", 75),
			# (assign, ":tier3", 90),
			# (assign, ":tier4", 90),
			# #(display_message, "@high"),
		# (try_end),
		(try_begin), ##lance recruited from town/castle
			(is_between, ":spawned_party", walled_centers_begin, walled_centers_end),
			(party_slot_ge, ":spawned_party", slot_town_lord, 0), #assigned center
			(party_get_slot, ":leader", ":spawned_party", slot_town_lord),
		(try_end),
		
		#troop types
		(faction_get_slot, ":village_troop", ":orig_culture", slot_faction_tier_1_troop),
		(faction_get_slot, ":castle_troop", ":orig_culture", slot_faction_tier_1_castle_troop),
		(faction_get_slot, ":town_troop", ":orig_culture", slot_faction_tier_1_town_troop),
		
		#get regular troop types
		(assign, ":chance_for_village", 50),
		(try_begin), #castle
			#(this_or_next|is_between, ":center", villages_begin, villages_end),
			(is_between, ":center", castles_begin, castles_end),
			(assign, ":chance_for_village", 50),
			#(assign, ":regular_troop", ":village_troop"),
		(else_try), #village
			(is_between, ":center", villages_begin, villages_end),
			(assign, ":chance_for_village", 70),
		(else_try), #town
			(assign, ":chance_for_village", 30),
		(try_end),
		
		(store_random_in_range, ":random", 1, 101),
		(try_begin), #village troop if random < chance_for_village
			(le, ":random", ":chance_for_village"),
			(assign, ":regular_troop", ":village_troop"),
		(else_try), #town lance!
			(assign, ":regular_troop", ":town_troop"),
		(try_end),
		
		#lets fill special troops
		(try_begin), #crusader knights
			(eq, ":leader", "trp_knight_23_6"), # teutonic
			(assign, ":regular_troop", "trp_teu_town_1"),
			(assign, ":castle_troop", "trp_teu_horse_1"),
		(else_try),
			(eq, ":leader", "trp_knight_23_1"), # hospitaller
			(store_random_in_range, ":castle_troop", "trp_hospitaller_half_brother", "trp_saint_lazarus_half_brother"),
		(else_try),	
				(eq, ":leader", "trp_knight_23_2"), # templar
			(assign, ":castle_troop", "trp_templar_half_brother", "trp_hospitaller_half_brother"),
		(else_try),	
				(eq, ":leader", "trp_knight_16_1"), # santiago
			(assign, ":castle_troop", "trp_santiago_half_brother", "trp_calatrava_half_brother"),
		(else_try),	
				(eq, ":leader", "trp_knight_18_9"), # caltrava
			(assign, ":castle_troop", "trp_calatrava_half_brother", "trp_saint_thomas_half_brother"),
		(else_try), #cuman
			(eq, ":leader", "trp_knight_7_15"), 
			#(assign, ":regular_troop", "trp_teu_town_1"),
			(assign, ":town_troop", "trp_cuman_tribesman"),
			(assign, ":castle_troop", "trp_cuman_horseman"),
		(else_try), #monogls recruit mongols as well
			(neg|is_between, ":spawned_party", centers_begin, centers_end),
			(this_or_next|is_between, ":leader", "trp_knight_3_1", "trp_knight_3_20"), #mongol
			(this_or_next|is_between, ":leader", "trp_knight_27_4", "trp_knight_2_1"), #ilkhanate
			(this_or_next|eq, ":leader", "trp_kingdom_3_lord"), #mongol
			(eq, ":leader", "trp_kingdom_27_lord"), #ilkhanate
			(assign, ":regular_troop", "trp_tatar_tribesman"),
			(assign, ":castle_troop", "trp_tatar_horseman"),  
		(try_end),
		
		###initiate amount of troop ratio
		#in the future do a script call?
		# (try_begin), #lords - double to save cpu
			# (is_between, ":leader", active_npcs_begin, active_npcs_end),
			# (assign, ":nobles", 4),
			# (assign, ":regulars", 16),
		# (else_try), #player
			#(assign, ":nobles", 2),
			#(assign, ":regulars", 8),
		# (try_end),
		
		(try_begin), ## error fix
			(neg|is_between, ":nobles", size_small, size_large +1),
			(assign, ":nobles", size_average),
		(try_end),
		(try_begin), ## error fix
			(neg|is_between, ":regulars", size_small, size_large +1),
			(assign, ":regulars", size_average),
		(try_end),
		
		(call_script, "script_get_lance_precentage", ":nobles", ":prosperity"),
		(assign, ":tier1", reg1),
		(assign, ":tier2", reg2),
		(assign, ":tier3", reg3),
		#(assign, ":tier1", reg1),
		
		#lets spin the dice for the troop.
		(try_for_range, reg10, 0, ":nobles"),
			(store_random_in_range, ":random", 1, 101),
			(try_begin),
				(eq, ":spawned_party", "p_main_party"),
			(party_slot_ge, ":center", slot_number_nobles, 1),
			(call_script, "script_get_noble_troop", ":center"),
			(ge, reg1, 0),
			(party_get_slot,":amount", ":center", slot_number_nobles),
			(val_sub, ":amount", 1),
			(party_set_slot,":center", slot_number_nobles, ":amount"),
			#(str_store_troop_name, s0, reg1),
			#(display_message, "@noble: {s0}"),
			(else_try),
				(lt, ":random", ":tier1"),
			#(display_message, "@spawning tier 1"),
			#(party_add_members, ":spawned_party", ":castle_troop", 1),
			(assign, reg1, ":castle_troop"),
			(else_try),
				(lt, ":random", ":tier2"),
			(call_script, "script_choose_random_troop_for_lance", ":castle_troop", 2),
			#(display_message, "@spawning tier 2"),
			(else_try),
				(lt, ":random", ":tier3"),
			#(assign, ":temp_troop", ":castle_troop"),
			(call_script, "script_choose_random_troop_for_lance", ":castle_troop", 3),
			#(display_message, "@spawning tier 3"),
			(else_try),
				#(ge, ":random", ":tier4"),
			(store_random_in_range, ":random2", 0, 100),
				(try_begin),
				(lt, ":random2", 50),
				(call_script, "script_choose_random_troop_for_lance", ":castle_troop", 4),
				#(display_message, "@spawning tier 4"),
			(else_try),
				(call_script, "script_choose_random_troop_for_lance", ":castle_troop", 5),
				#(display_message, "@spawning tier 5"),
			(try_end),
			(try_end),
			# (try_begin),
				# (eq, reg1, "trp_player"),
			# (str_store_party_name,s0,":center"),
				# (display_message, "@ADDING PLAYER noble! {s0}"),
				# (assign, reg1, ":castle_troop"),
			# (try_end),
			(try_begin),
				(eq,":spawned_party", "p_main_party"),
			(call_script, "script_add_lance_troop_to_regulars", reg1, ":center"),
			(try_end),
			(party_add_members, ":spawned_party", reg1, 1),
		(try_end),
		
		(call_script, "script_get_lance_precentage", ":regulars", ":prosperity"),
		(assign, ":tier1", reg1),
		(assign, ":tier2", reg2),
		(assign, ":tier3", reg3),
		
		(val_mul, ":regulars", 4),
		#do these cycles a script call?
		(try_for_range, reg10, 0, ":regulars"),
			(store_random_in_range, ":random", 1, 101),
			(try_begin),
				(eq, ":spawned_party", "p_main_party"),
			(party_slot_ge, ":center", slot_number_commoner, 1),
			(call_script, "script_get_commoner_troop", ":center"),
			(ge, reg1, 0),
			(party_get_slot,":amount", ":center", slot_number_commoner),
			(val_sub, ":amount", 1),
			(party_set_slot,":center", slot_number_commoner, ":amount"),
			(str_store_troop_name, s0, reg1),
			#(display_message, "@commoner: {s0}"),
			(else_try),	
				(lt, ":random", ":tier1"),
			#(party_add_members, ":spawned_party", ":regular_troop", 1),
			(assign, reg1, ":regular_troop"),
			#(display_message, "@spawning tier 1"),
			(else_try),
				(lt, ":random", ":tier2"),
			(call_script, "script_choose_random_troop_for_lance", ":regular_troop", 2),
			#(display_message, "@spawning tier 2"),
			(else_try),
				(lt, ":random", ":tier3"),
			#(assign, ":temp_troop", ":regular_troop"),
			(call_script, "script_choose_random_troop_for_lance", ":regular_troop", 3),
			#(display_message, "@spawning tier 3"),
			(else_try),
				#(ge, ":random", ":tier4"),
			(store_random_in_range, ":random2", 0, 100),
				(try_begin),
				(lt, ":random2", 50),
				(call_script, "script_choose_random_troop_for_lance", ":regular_troop", 4),
				#(display_message, "@spawning tier 4"),
			(else_try),
				(call_script, "script_choose_random_troop_for_lance", ":regular_troop", 5),
				#(display_message, "@spawning tier 5"),
			(try_end),
			(try_end),
			#(try_begin),
				#(eq, reg1, "trp_player"),
				#(display_message, "@ADDING PLAYER regular! {s0}"),
				#(assign, reg1, ":regular_troop"),
			#(try_end),
			(try_begin),
				(eq,":spawned_party", "p_main_party"),
			(call_script, "script_add_lance_troop_to_regulars", reg1, ":center"),
			(try_end),
			(party_add_members, ":spawned_party", reg1, 1),
		(try_end),
		
		(assign, reg0, ":spawned_party"),
		]
	),
	
	##script_choose_random_troop_for_lance - tom made
	##description: gets a random troop for the lance. Either one of the two upgrade troops, 
	##the only one if one is available, or just returns the orignal troop if non upgradable
	##input: original_troop to upgrade from, which tier to return
	##output: returns via reg0
	("choose_random_troop_for_lance",
		[ 
			(store_script_param, ":orig_troop", 1),
			(store_script_param, ":tier", 2),
		(val_sub, ":tier", 1),
		#set a fail-safe
		
		(assign, reg1, ":orig_troop"),
		#get the upgrade paths
		(assign, ":first", -1),
		(assign, ":second", -1),
		(troop_get_upgrade_troop, ":first", ":orig_troop", 0),
		(troop_get_upgrade_troop, ":second", ":orig_troop", 1),
		#choose the troop
		(try_begin),
			(gt, ":first", 0),
			(gt, ":second", 0),
			(store_random_in_range, ":random", 0, 101),
			(try_begin),
				(lt, ":random", 50),
			(assign, reg1, ":first"),
			#(display_message, "@first"),
			(else_try),
				(assign, reg1, ":second"),
			#(display_message, "@second"),
			(try_end),
		(else_try),
			(gt, ":first", 0),
			(assign, reg1, ":first"),
			#(display_message, "@second failed, adds first"),
		(else_try),
			(gt, ":second", 0),
			(assign, reg1, ":second"),
			#(display_message, "@FAILSESAFE: first failed, adds first"),  
		(try_end),
		(try_begin),
			(gt, ":tier", 1),
			(call_script, "script_choose_random_troop_for_lance", reg1, ":tier"),
		(try_end),
		(assign, reg2, ":tier"),
		#(display_message, "@exiting tier:{reg2}"),
		]
	),
	
	##script_feudal_lance_manpower_update - tom made
	##Input: party_id(village/town/castle)
	##output: none
	##description: updates the feudal recruits for the lance system in villages. max lances per village - 10.
	("feudal_lance_manpower_update",
		[
		(store_script_param, ":center_no", 1),
		(store_script_param, ":limit", 2),
		(try_begin),
			(party_get_slot, ":manpower", ":center_no", slot_feudal_lances),
			
			#(party_get_slot, ":limit", ":center_no", slot_lances_cap),
			#set limit for the player
			(try_begin),
				(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
				(party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
				(val_div, ":player_relation", 25),
				(val_add, ":limit", ":player_relation"),
			(try_end),
			(lt, ":manpower", ":limit"),
			#(store_random_in_range, ":random", 1, 4), #1-3
			#(val_add, ":manpower", ":random"),
			(store_faction_of_party,":faction", ":center_no"),
			(try_begin), #when faction at paece - extra lance
				 (faction_slot_eq, ":faction", slot_faction_at_war, 0), #at peace
			 (val_add, ":manpower", 1),
			(try_end),
			(val_add, ":manpower", 1),
			(val_clamp, ":manpower", 1, ":limit"), #limit it to 10-15
			(party_set_slot, ":center_no", slot_feudal_lances, ":manpower"),
		(try_end),
		]
	),

	###script_fill_company - tom made
	###input: center, party, merc_type
	###output: none
	###description: company size - 30 men; 1 seargant, ~10 crossbow
	("fill_company",
		[
		(store_script_param, ":center", 1), #to recruit from
		(store_script_param, ":party", 2), #to add recruits to
		(store_script_param, ":merc_slot", 3), #like, generic, special, ect. SLOT

		(assign, ":company_template", "pt_generic_euro"),
		(try_begin),
			(eq, ":merc_slot", slot_regional_mercs),
			(party_get_slot, ":company_template", ":center", slot_regional_party_template),
		(else_try),
			(eq, ":merc_slot", slot_spec_mercs1),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs1_party_template),
		(else_try),
			(eq, ":merc_slot", slot_spec_mercs2),
			(party_get_slot, ":company_template", ":center", slot_spec_mercs2_party_template),
		(try_end),
		
		(party_add_template, ":party", ":company_template"),
		]
	),
	
	## script_get_lance_size
	## description: returns the size of the lance
		## Input: item_no, agent_no
		## Output: reg0 - tottal size, reg1 - noble size, reg2 - commoner size 
	("get_lance_size",
	[
		(store_script_param, ":center", 1),
		
		(party_get_slot, ":noble", ":center", slot_center_nobility_law),
		(party_get_slot, ":commoner", ":center", slot_center_commoner_law),
		
		(val_mul, ":commoner", 4),
		(try_begin),
			(le, ":commoner", 0),
		(assign, ":commoner", 1),
		(try_end),
		(try_begin),
			(le, ":noble", 0),
		(assign, ":noble", 1),
		(try_end),
		(store_add, reg0, ":commoner", ":noble"),
		(assign, reg1, ":noble"),
		(assign, reg2, ":commoner"),
	]),
	
	## script_get_lance_precentage
	## description: returns the precentage for lance troop tier chance
		## Input: item_no, agent_no
		## Output: reg1 - tier1, reg2 - tier2, reg3 - tier3, reg4 - tier4, reg5 - tier5 
	("get_lance_precentage",
	[
		(store_script_param, ":law", 1),
		(store_script_param, ":prosperity", 2),
		
		#(party_get_slot, ":noble", ":center", slot_center_nobility_law),
		#(party_get_slot, ":commoner", ":center", slot_center_commoner_law),
		#(party_get_slot, ":prosperity", ":center", slot_town_prosperity),
		
		(try_begin), #low
			(le, ":prosperity", 25),
			(assign, ":tier1", 50),
			(assign, ":tier2", 90),
			(assign, ":tier3", 95),
			#(assign, ":tier4", 100),
			#(display_message, "@low"),
		(else_try), #avg
			(le, ":prosperity", 75),
			(assign, ":tier1", 30),
			(assign, ":tier2", 80),
			(assign, ":tier3", 90),
			#(assign, ":tier4", 100),
			#(display_message, "@avg"),
		(else_try), #high
			(assign, ":tier1", 10),
			(assign, ":tier2", 70),
			(assign, ":tier3", 85),
			#(assign, ":tier4", 100),
			#(display_message, "@high"),
		(try_end),
		
		(try_begin),
		(eq, ":law", size_small),
		(val_sub, ":tier1", tier1_dif),
		(val_sub, ":tier2", tier2_dif),
		(val_sub, ":tier3", tier3_dif),
		(else_try),
		(eq, ":law", size_large),
		(val_add, ":tier1", tier1_dif),
		(val_add, ":tier2", tier2_dif),
		(val_add, ":tier3", tier3_dif),
		(try_end),
		
		(assign, reg1, ":tier1"),
		(assign, reg2, ":tier2"),
		(assign, reg3, ":tier3"),
	]),
	
	##script_check_if_faction_is_at_war - tom made
	##Input: faction_id
	##output: reg0 - sets 1 if at war, 0 if not
	##description: Check if at war with any other major faction. 
	("check_if_faction_is_at_war",
		[
		(store_script_param, ":faction", 1),
		
		(assign, reg0, 0),
		(assign, ":end", kingdoms_end),
		(try_for_range, ":faction2", kingdoms_begin, ":end"),
			(neq, ":faction", ":faction2"),
			(store_relation, ":relation", ":faction2", ":faction"),
			(lt, ":relation", 0),
			(assign, reg0, 1),
			(assign, ":end", -5), #break;
		(try_end),
		]
	),
	
	##script_set_sea_icons - tom made
	##Input: none
	##output: none
	##description: Option trigger - moving party icons to default
	("set_sea_icons",
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
		]
	),
	
	##script_get_party_campsite - tom made
	##Input: party
	##output: reg0 - campsite scene
	##description: Sets the scene based on the current party terrain
	("get_party_campsite",
		[
			(store_script_param, ":party", 1),
			(party_get_current_terrain,":terrain",":party"),
		#(assign, ":terrain", rt_plain),
		(assign, reg0, "scn_campside_plain"),
		(try_begin),
			(this_or_next|eq, ":terrain", rt_plain),
			(this_or_next|eq, ":terrain", rt_mountain_forest),
			(eq, ":terrain", rt_forest),
			(assign, reg0, "scn_campside_plain"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_snow),
			(eq, ":terrain", rt_snow_forest),
			(assign, reg0, "scn_campside_snow"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_steppe),
			(eq, ":terrain", rt_steppe_forest),
			(assign, reg0, "scn_campside_steppe"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_desert),
			(eq, ":terrain", rt_desert_forest),
			(assign, reg0, "scn_campside_desert"),
		(try_end),
		]
	),
	
	##script_cf_hire_npc_specialist - tom made
	##Input: companion, companion_culture
	##output: none
	##description: Hires the specialist for the players party
	("cf_hire_npc_specialist",
		[
		(store_script_param, ":troop", 1),
		#(store_script_param, ":culture", 2),
		
		#hero is not in a party
		(party_count_members_of_type, reg1, "p_main_party", ":troop"),
		(eq, reg1, 0),
		
		#if enough space for the 
		(assign, ":continue", 0),
		(party_get_free_companions_capacity, reg1, "p_main_party"),
		(try_begin),
			(eq, reg1, 0),
			(assign, ":continue", 1),
			(display_message, "@Not enough space in the party to hire this specialist!"),
		(try_end),
		(eq, ":continue", 0),
		
		#get the price for npc
		(store_character_level, ":level",":troop"),
		(assign, ":cost", 50),
		(val_mul, ":cost", ":level"),
		(try_begin),
			(troop_slot_ge, ":troop", slot_troop_prisoner_of_party, 0),
			(val_mul, ":cost", 2),
		(try_end),
		
		#enough gold to hire
		(store_troop_gold, ":gold", "trp_player"),
		(try_begin),
			(ge, ":gold", ":cost"),
			(assign, ":continue", 0),
		(else_try),
			(assign, ":continue", 1),
			(display_message, "@Not enough gold!"),
		(try_end),
		(eq, ":continue", 0),
		(troop_remove_gold, "trp_player", ":cost"),

		#this in the future remove?
		#get culture
		(party_get_slot, ":culture", "$current_town", slot_center_culture),
		#(str_store_faction_name,s20, ":culture"),
		#(display_message, "@faction: {s20}"),
		#recruit
		(try_begin),
			#(display_message, "@try to equip"),
			(troop_slot_eq, ":troop", npc_slot_naked, 0),
			#(display_message, "@equiping"),
			(faction_get_slot, ":troop_type", ":culture", slot_faction_tier_1_town_troop),
			#(str_store_troop_name, s20, ":troop_type"),
			#(display_message, "@troop name: {s20}"),
			(call_script, "script_equip_companion", ":troop", ":troop_type"),
			# (troop_equip_items, ":troop"),
			# (troop_clear_inventory, ":troop"),
			#(display_message, "@equiped"),
			(troop_set_slot, ":troop", npc_slot_naked, 1),
			#(display_message, "@exiting"),
		(try_end),
		
		#hire 
		(party_add_members, "p_main_party", ":troop", 1),
		(troop_set_slot, ":troop", slot_troop_occupation, slto_player_companion),
		(troop_set_slot, ":troop", slot_troop_met, 1),
		
		(troop_get_slot, ":prison_center", ":troop", slot_troop_prisoner_of_party),
		(try_begin),
			(ge, ":prison_center", 1),
					(party_remove_prisoners, ":prison_center", ":troop", 1),
		(try_end),  
		(troop_set_slot, ":troop", slot_troop_prisoner_of_party, -1),
		
		
		(display_message, "@Hired!"),
		]
	),
	
	
	##script_equip_companion - tom made
	##Input: companion, troop
	##output: none
	##description: Sets the equipment of the hero character to the specified troop
	("equip_companion",
		[
		(store_script_param, ":companion", 1),
		(store_script_param, ":troop_id", 2),
		
		(assign, ":main_weapon", 0),
		(assign, ":side_weapon", 25),
		(assign, ":shield", 50),
		(assign, ":two_handed", 75),
		(assign, ":javelin", 100),
		(assign, ":bolts", 125),
		(assign, ":arrows", 150),
		(assign, ":bow", 175),
		(assign, ":crossbow", 200),
		(assign, ":head", 225),
		(assign, ":body", 250),
		(assign, ":foot", 275),
		(assign, ":hand", 300),
		(assign, ":horse", 325),
		
		(assign, ":equip_main", 0),
		(assign, ":equip_side", 0),
		(assign, ":equip_shield", 0),
		(assign, ":equip_two_handed", 0),
		(assign, ":equip_javelin", 0),
		(assign, ":equip_bolts", 0),
		(assign, ":equip_arrows", 0),
		(assign, ":equip_bow", 0),
		(assign, ":equip_crossbow", 0),
		(assign, ":equip_head", 0),
		(assign, ":equip_body", 0),
		(assign, ":equip_foot", 0),
		(assign, ":equip_hand", 0),
		(assign, ":equip_horse", 0),
		
		(troop_clear_inventory, ":companion"),
		(troop_get_inventory_capacity, ":capacity", ":troop_id"),
		(try_for_range, ":cur_slot", 0, ":capacity"),
			(troop_get_inventory_slot, ":cur_item", ":troop_id", ":cur_slot"),
			(gt, ":cur_item", 0),
			(item_get_type, ":type", ":cur_item"),
			(try_begin),
			(eq, ":type", itp_type_polearm),
			(val_add, ":main_weapon", 1),
			(troop_set_slot, "trp_items_array", 0, ":main_weapon"),
			(troop_set_slot, "trp_items_array", ":main_weapon", ":cur_item"),
			(assign, ":equip_main", 1),
			(else_try),	
			(eq, ":type", itp_type_one_handed_wpn),
			(val_add, ":side_weapon", 1),
			(troop_set_slot, "trp_items_array", 25, ":side_weapon"),
			(troop_set_slot, "trp_items_array", ":side_weapon", ":cur_item"),	
			(assign, ":equip_side", 1),
			(else_try),	
			(eq, ":type", itp_type_shield),
			(val_add, ":shield", 1),
			(troop_set_slot, "trp_items_array", 50, ":shield"),
			(troop_set_slot, "trp_items_array", ":shield", ":cur_item"),
			(assign, ":equip_shield", 1),	
			(else_try),	
			(eq, ":type", itp_type_two_handed_wpn),
			(val_add, ":two_handed", 1),
			(troop_set_slot, "trp_items_array", 75, ":two_handed"),
			(troop_set_slot, "trp_items_array", ":two_handed", ":cur_item"),
			(assign, ":equip_two_handed", 1),
			(else_try),	
			(eq, ":type", itp_type_thrown),
			(val_add, ":javelin", 1),
			(troop_set_slot, "trp_items_array", 100, ":javelin"),
			(troop_set_slot, "trp_items_array", ":javelin", ":cur_item"),
			(assign, ":equip_javelin", 1),
			(else_try),	
			(eq, ":type", itp_type_bolts),
			(val_add, ":bolts", 1),
			(troop_set_slot, "trp_items_array", 125, ":bolts"),
			(troop_set_slot, "trp_items_array", ":bolts", ":cur_item"),
			(assign, ":equip_bolts", 1),
			(else_try),	
			(eq, ":type", itp_type_arrows),
			(val_add, ":arrows", 1),
			(troop_set_slot, "trp_items_array", 150, ":arrows"),
			(troop_set_slot, "trp_items_array", ":arrows", ":cur_item"),
			(assign, ":equip_arrows", 1),
			(else_try),	
			(eq, ":type", itp_type_bow),
			(val_add, ":bow", 1),
			(troop_set_slot, "trp_items_array", 175, ":bow"),
			(troop_set_slot, "trp_items_array", ":bow", ":cur_item"),
			(assign, ":equip_bow", 1),
			(else_try),	
			(eq, ":type", itp_type_crossbow),
			(val_add, ":crossbow", 1),
			(troop_set_slot, "trp_items_array", 200, ":crossbow"),
			(troop_set_slot, "trp_items_array", ":crossbow", ":cur_item"),
			(assign, ":equip_crossbow", 1),
			(else_try),	
			(eq, ":type", itp_type_head_armor),
			(val_add, ":head", 1),
			(troop_set_slot, "trp_items_array", 225, ":head"),
			(troop_set_slot, "trp_items_array", ":head", ":cur_item"),
			(assign, ":equip_head", 1),
			(else_try),	
			(eq, ":type", itp_type_body_armor),
			(val_add, ":body", 1),
			(troop_set_slot, "trp_items_array", 250, ":body"),
			(troop_set_slot, "trp_items_array", ":body", ":cur_item"),
			(assign, ":equip_body", 1),	
			(else_try),	
			(eq, ":type", itp_type_foot_armor),
			(val_add, ":foot", 1),
			(troop_set_slot, "trp_items_array", 275, ":foot"),
			(troop_set_slot, "trp_items_array", ":foot", ":cur_item"),
			(assign, ":equip_foot", 1),	
			(else_try),	
			(eq, ":type", itp_type_hand_armor),
			(val_add, ":hand", 1),
			(troop_set_slot, "trp_items_array", 300, ":hand"),
			(troop_set_slot, "trp_items_array", ":hand", ":cur_item"),
			(assign, ":equip_hand", 1),	
			(else_try),	
			(eq, ":type", itp_type_horse),
			(val_add, ":horse", 1),
			(troop_set_slot, "trp_items_array", 325, ":horse"),
			(troop_set_slot, "trp_items_array", ":horse", ":cur_item"),
			(assign, ":equip_horse", 1),	
			(try_end),
		(try_end),
		
		(try_begin),
			(eq, ":equip_main", 1),
			(troop_get_slot, ":amount", "trp_items_array", 0),
			(store_random_in_range, ":slot", 1, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_side", 1),
			(troop_get_slot, ":amount", "trp_items_array", 25),
			(store_random_in_range, ":slot", 26, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_shield", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 50),
			(store_random_in_range, ":slot", 51, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_two_handed", 1),	
			(try_begin),
			(eq, ":equip_side", 1),	#if have and side arm
			(store_random_in_range, ":random", 0, 100),
			(lt, ":random", 65), #small chance for getting a sidearm as well
			(else_try),
			(troop_get_slot, ":amount", "trp_items_array", 75),
			(store_random_in_range, ":slot", 76, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
			(try_end),
		(try_end),
		(try_begin),
			(eq, ":equip_javelin", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 100),
			(store_random_in_range, ":slot", 101, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_bolts", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 125),
			(store_random_in_range, ":slot", 126, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_arrows", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 150),
			(store_random_in_range, ":slot", 151, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_bow", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 175),
			(store_random_in_range, ":slot", 176, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_crossbow", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 200),
			(store_random_in_range, ":slot", 201, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_head", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 225),
			(store_random_in_range, ":slot", 256, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_body", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 250),
			(store_random_in_range, ":slot", 251, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_foot", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 275),
			(store_random_in_range, ":slot", 276, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_hand", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 300),
			(store_random_in_range, ":slot", 301, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(eq, ":equip_horse", 1),	
			(troop_get_slot, ":amount", "trp_items_array", 325),
			(store_random_in_range, ":slot", 326, ":amount"),
			(troop_get_slot, ":itm", "trp_items_array", ":slot"),
			(neq, ":itm", "itm_no_item"),
			(troop_add_item,":companion",":itm"),
		(try_end),
		(try_begin),
			(neq, "trp_player", ":companion"),
			(troop_equip_items, ":companion"),
			(troop_clear_inventory, ":companion"),
			(troop_set_auto_equip, ":companion", 0),
		(try_end),
		]
	),
	
	##script_set_troop_culture
	##description: sets the culture for the regular troops.
	("set_troop_culture",
	[
		(try_for_range, ":troop", "trp_mercenaries_end", "trp_looter"),
			(try_begin),
			(is_between, ":troop", finn_culture_start, finn_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_finnish"),
		(else_try),
			(is_between, ":troop", mazovian_culture_start, mazovian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_mazovian"),
		(else_try),
			(is_between, ":troop", serbian_culture_start, serbian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_serbian"),
		(else_try),
			(is_between, ":troop", welsh_culture_start, welsh_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_welsh"),
		(else_try),
			(is_between, ":troop", teutonic_culture_start, teutonic_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_teutonic"),
		(else_try),
			(is_between, ":troop", mongol_culture_start, mongol_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_mongol"),
		(else_try),
			(is_between, ":troop", balkan_culture_start, balkan_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_balkan"),
		(else_try),
			(is_between, ":troop", rus_culture_start, rus_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_rus"),
		(else_try),
			(is_between, ":troop", nordic_culture_start, nordic_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_nordic"),
		(else_try),
			(is_between, ":troop", balt_culture_start, balt_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_baltic"),
		(else_try),
			(is_between, ":troop", marinid_culture_start, marinid_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_marinid"),
		(else_try),
			(is_between, ":troop", bedouin_culture_start, bedouin_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_mamluke"),
		(else_try),
			(is_between, ":troop", byz_culture_start, byz_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_byzantium"),
		(else_try),
			(is_between, ":troop", iberian_culture_start, iberian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_iberian"),
		(else_try),
			(is_between, ":troop", italian_culture_start, italian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_italian"),
		(else_try),
			(is_between, ":troop", andalus_culture_start, andalus_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_andalus"),
		(else_try),
			(is_between, ":troop", gaelic_culture_start, gaelic_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_gaelic"),
		(else_try),
			(is_between, ":troop", anatolian_culture_start, anatolian_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_anatolian"),
		(else_try),
			(is_between, ":troop", scottish_culture_start, scottish_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_scotish"),
		(else_try),
			(is_between, ":troop", euro_culture_start, euro_culture_end),
			(troop_set_slot, ":troop", slot_troop_culture, "fac_culture_western"),		
		(try_end),
		(try_end),
	]
	),
	
	##script_troop_find_culture
	##description
	##input: troop to search for, culture
	##output: reg0 returns -1 if the troop does not belong to the culture, 0 if belongs(village), 1(town), 2(noble)
	("troop_find_culture",
	[
		(store_script_param, ":troop", 1),
		(store_script_param, ":culture", 2),
		
		(faction_get_slot, ":village", ":culture", slot_faction_tier_1_troop),
		(faction_get_slot, ":town", ":culture", slot_faction_tier_1_town_troop),
		(faction_get_slot, ":noble", ":culture", slot_faction_tier_1_castle_troop),
		
		(assign, reg0, -1),
		(assign, reg10, -1),
		# (try_begin),
			# (call_script, "script_troop_tree_search", ":troop", ":village"),	
		# (eq, reg10, ":troop"),
		# (assign, reg0, 0),
		# (else_try),
			# (call_script, "script_troop_tree_search", ":troop", ":town"),	
		# (eq, reg10, ":troop"),
		# (assign, reg0, 1),
		# (else_try),
			# (call_script, "script_troop_tree_search", ":troop", ":noble"),	
		# (eq, reg10, ":troop"),
		# (assign, reg0, 2),
		# (try_end),
		
				(try_begin),
			(call_script, "script_troop_tree_search", ":troop", ":noble"),	
		(eq, reg10, ":troop"),
		(assign, reg0, 2),
		(else_try),
			(call_script, "script_troop_tree_search", ":troop", ":town"),	
		(eq, reg10, ":troop"),
		(assign, reg0, 1),
		(else_try),
			(call_script, "script_troop_tree_search", ":troop", ":village"),	
		(eq, reg10, ":troop"),
		(assign, reg0, 0),
		(try_end),
	]
	),
	
	##script_troop_tree_search
	##description
	##input: target target_troop - the troop to search for, troop - current troop in the tree path
	##output: reg10 returns the assigned troop if found. IF not reg10 is unchanged.
	("troop_tree_search",
	[
		(store_script_param, ":target_troop", 1),
		(store_script_param, ":troop", 2),
		
		(troop_get_upgrade_troop,":path1",":troop",0),
		(troop_get_upgrade_troop,":path2",":troop",1),
		(try_begin),
			(eq, ":troop", ":target_troop"),
		(assign, reg10, ":target_troop"),
		(else_try),
			(gt, ":path1", 0),
			(call_script, "script_troop_tree_search", ":target_troop", ":path1"),	
		(eq, reg10, ":target_troop"),
		(else_try),  
			(gt, ":path2", 0),
		(call_script, "script_troop_tree_search", ":target_troop", ":path2"),	
		(try_end),
	]
	),
	
	
	###tom - tournament scripts
	##script_init_tournament_participents
	##description: set up tournament participents in trp_tournament_participants
	##input: center_no
	##output: none
	("init_tournament_participents",
	[
		(store_script_param, ":center_no", 1),
		(try_begin), #one-on-one
			#(eq, "$tournament_type", 0), 
		
		(troop_set_slot, "trp_tournament_participants", 0, "trp_player"),
		(assign, ":cur_slot", 1), #player not needed?
		#other bastards
		(party_collect_attachments_to_party, ":center_no", "p_temp_party"),
				(party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
				(try_for_range, ":stack_no", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":cur_troop", "p_temp_party", ":stack_no"),
					(troop_is_hero, ":cur_troop"),
					(troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
					(val_add, ":cur_slot", 1),
				(try_end),
		
		#player companions
		(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
			(try_for_range, ":stack_no", 0, ":num_stacks"),
			(eq, "$freelancer_state", 0), #make sure the player is not on vacation
			(eq, "$tournament_type", 0), #team battle- make members
			(party_stack_get_troop_id, ":cur_troop", "p_main_party", ":stack_no"),
			(troop_is_hero, ":cur_troop"),
			(neq, ":cur_troop", "trp_player"),
			(neq, ":cur_troop", "trp_kidnapped_girl"),
			(troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
			(val_add, ":cur_slot", 1),
			(try_end),
		
		#other heroes
				(try_for_range, ":cur_troop", "trp_Xerina", "trp_tutorial_trainer"),
					(store_random_in_range, ":random_no", 0, 100),
					(lt, ":random_no", 80),
					(troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
					(val_add, ":cur_slot", 1),
				(try_end),
		
		#add bastards if not enough
		(assign, ":begin_slot", ":cur_slot"),
				(try_for_range, ":cur_slot", ":begin_slot", 64),
			(party_get_slot, ":orig_culture", ":center_no", slot_center_culture),
			(faction_get_slot, ":castle_troop", ":orig_culture", slot_faction_tier_1_castle_troop),
			(call_script, "script_choose_random_troop_for_lance", ":castle_troop", 4),
			(troop_set_slot, "trp_tournament_participants", ":cur_slot", reg1),
		(try_end),
		

		(try_end),
		(try_begin),
		#(else_try), #team on team
			(eq, "$tournament_type", 1),
		(try_for_range, reg0, 0, 9),
			(troop_get_slot, ":opponent", "trp_tournament_participants", reg0),
			(store_mul, ":op", reg0, 5),
			(store_add, ":top", ":op", 5),
			##add leader
			(troop_set_slot, "trp_temp_array_b", ":op", ":opponent"),
			(val_add, ":op", 1),
			#add companions if player
			(try_begin),
				(eq, ":opponent", "trp_player"),
			(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
			(try_for_range, ":stack_no", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":cur_troop", "p_main_party", ":stack_no"),
				#(troop_is_hero, ":cur_troop"),
				(neq, ":cur_troop", "trp_player"),
				#(neq, ":cur_troop", "trp_kidnapped_girl"),
				(party_stack_get_size, ":stack_size","p_main_party",":stack_no"),
				(try_for_range, reg1, 0, ":stack_size"),
					(lt, ":op", ":top"),
					(troop_set_slot, "trp_temp_array_b", ":op", ":cur_troop"),
				(val_add, ":op", 1),
				(try_end),
			(try_end),
			(else_try),
				##add the rest of them
				(try_for_range, ":slot", ":op", ":top"),
					(party_get_slot, ":orig_culture", ":center_no", slot_center_culture),
				(faction_get_slot, ":castle_troop", ":orig_culture", slot_faction_tier_1_castle_troop),
				(call_script, "script_choose_random_troop_for_lance", ":castle_troop", 4),
					(troop_set_slot, "trp_temp_array_b", ":slot", reg1),
				(try_end),
			(try_end),
		(try_end),
		(try_end),
		#clear temp-array for tracking winners
		(try_for_range, ":slot", 0, 10),
		(troop_set_slot,"trp_temp_array_c", ":slot", 0),
		(try_end),
	]
	),	
	
	# script_end_tournament_fight_new
		# Input: arg1 = player_team_won (1 or 0)
		# Output: none
	("end_tournament_fight_new",
	[
		(store_script_param, ":p_won", 1),
		(troop_get_slot,":p_count","trp_temp_array_c",0), #player victory count
		(troop_get_slot,":o_count","trp_temp_array_c","$current_opponent"), #opponent victory count
		(try_begin), #player won
			(eq, ":p_won", 1),
		(val_add, ":p_count", 1),
		(assign, "$g_tournament_player_team_won", 1), #this does nothign now
		(else_try), #not!
			(val_add, ":o_count", 1),
		(assign, "$g_tournament_player_team_won", 0),
		(try_end),
		(troop_set_slot, "trp_temp_array_c", 0, ":p_count"),
		(troop_set_slot, "trp_temp_array_c", "$current_opponent", ":o_count"),
		(jump_to_menu, "mnu_town_tournament_new"),
	]
	),	
	
	# script_simulate_next_battle
		# Input: arg1 = player opponent
		# Output: none
	("simulate_next_battle",
	[
		(store_script_param, ":p_opponent", 1),

		(try_begin),
			(eq, ":p_opponent", 1), #who player fights
		#3-4
		(call_script, "script_simulate_next_battle_auxiliary",3,4,0),
		#5-6
		(call_script, "script_simulate_next_battle_auxiliary",5,6,0),
		#7-8
		(call_script, "script_simulate_next_battle_auxiliary",7,8,0),
		(else_try),	
			(eq, ":p_opponent", 2), #who player fights
		#2-4
		(call_script, "script_simulate_next_battle_auxiliary",2,4,0),
		#7-5
		(call_script, "script_simulate_next_battle_auxiliary",7,5,0),
		#6-8
		(call_script, "script_simulate_next_battle_auxiliary",6,8,0),
		(else_try),	
			(eq, ":p_opponent", 3), #who player fights
		#2-3
		(call_script, "script_simulate_next_battle_auxiliary",2,3,0),
		#5-8
		(call_script, "script_simulate_next_battle_auxiliary",5,8,0),
		#7-6
		(call_script, "script_simulate_next_battle_auxiliary",7,6,0),
		(else_try),	
			(eq, ":p_opponent", 4), #who player fights
		#2-6
		(call_script, "script_simulate_next_battle_auxiliary",2,6,0),
		#3-7
		(call_script, "script_simulate_next_battle_auxiliary",3,7,0),
		#4-8
		(call_script, "script_simulate_next_battle_auxiliary",4,8,0),
		(else_try),	
			(eq, ":p_opponent", 5), #who player fights
		#2-5
		(call_script, "script_simulate_next_battle_auxiliary",2,5,0),
		#3-8
		(call_script, "script_simulate_next_battle_auxiliary",3,8,0),
		#4-7
		(call_script, "script_simulate_next_battle_auxiliary",4,7,0),
		(else_try),	
			(eq, ":p_opponent", 6), #who player fights
		#2-8
		(call_script, "script_simulate_next_battle_auxiliary",2,8,0),
		#3-5
		(call_script, "script_simulate_next_battle_auxiliary",3,5,0),
		#4-6
		(call_script, "script_simulate_next_battle_auxiliary",4,6,0),
		(else_try),	
			(eq, ":p_opponent", 7), #who player fights
		#2-7
		(call_script, "script_simulate_next_battle_auxiliary",2,7,0),
		#3-6
		(call_script, "script_simulate_next_battle_auxiliary",3,6,0),
		#4-5
		(call_script, "script_simulate_next_battle_auxiliary",4,5,0),
		(try_end),
	]
	),	
	
	# script_simulate_next_battle_auxiliary
		# Input: oponnent1 slot , opponent2 slot, reduce by 1 slot values(1-no, 0-yes)
		# Output: none
	("simulate_next_battle_auxiliary",
	[
		(store_script_param, ":op1", 1),
		(store_script_param, ":op2", 2),
		(store_script_param, ":reduce", 3),
		(try_begin),
			(eq, ":reduce", 0),
		(val_sub, ":op1", 1),
		(val_sub, ":op2", 1),
		(try_end),
		
		(store_random_in_range, ":random", 1, 101),
		#get victory count
		(troop_get_slot,":v1","trp_temp_array_c", ":op1"),
		(troop_get_slot,":v2","trp_temp_array_c", ":op2"),
		(try_begin),#wins first
			(le, ":random", 50),
		(val_add, ":v1", 1),
		(else_try), #wins second
		(val_add, ":v2", 1),
		(try_end),
		#store the new victory count!
		(troop_set_slot, "trp_temp_array_c", ":op1", ":v1"),
		(troop_set_slot, "trp_temp_array_c", ":op2", ":v2"),
	]
	),	
	
	## script_get_and_remove_member
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: party_to_do_so
		## Output: reg1 - troop
	("get_and_remove_member",
	[
		(store_script_param, ":party", 1),
		(assign, reg1, -1),
		(party_get_num_companion_stacks, ":num_stacks",":party"),
		(try_begin),
			(gt, ":num_stacks", 0),
		(party_stack_get_troop_id, ":stack_troop",":party",0),
		(assign, reg1, ":stack_troop"),
		(party_remove_members,":party",":stack_troop",1),
		(try_end),
	]
	),	
	
	## script_set_matching_sexy_boots
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: item_no, agent_no
		## Output: none
	("set_matching_sexy_boots",
	[
		(store_script_param, ":agent", 1),
		(agent_get_item_slot, ":body", ":agent", ek_body),
		(agent_get_item_slot, ":foot", ":agent", ek_foot),
		(agent_get_item_slot, ":head", ":agent", ek_head),
		(agent_get_item_slot, ":hand", ":agent", ek_gloves),
		(try_begin), #african 
			(is_between, ":head", "itm_kufia_berber_black", "itm_legs_african"), #black head
		(try_begin), #need black hands and or legs
			(le, ":foot", 0),
			(agent_equip_item,":agent","itm_legs_african"),
			(assign, ":foot", "itm_legs_african"),
		(try_end),  
		(try_begin),
			(le, ":hand", 0),
			(agent_equip_item,":agent","itm_hands_african"),
			(assign, ":hand", "itm_hands_african"),
		(try_end),
		(else_try),
			(try_begin),
			(eq, ":hand", "itm_hands_african"),
			(agent_unequip_item, ":agent", "itm_hands_african"),
			(assign, ":hand", 0),
			(else_try),
			(eq, ":foot", "itm_legs_african"),
			(agent_unequip_item, ":agent", "itm_legs_african"),
			(assign, ":foot", 0),
		(try_end),  
		(try_end),
		(try_begin),
		 (le, ":foot", 0),
		 (neg|is_between, ":body", "itm_red_dress", "itm_nomad_armor"),
		 (neg|is_between, ":body", "itm_berber_robe_a", itm_saracen_kaftan_d+1),
		 (neg|is_between, ":body", "itm_meghrebi_leather_a", itm_black_guard+1),
			 (agent_equip_item,":agent","itm_bare_legs"),  
		(else_try), #short boots needed
			##check body armor
			#(this_or_next|is_between, ":body", "itm_veteran_surcoat_a", "itm_kau_aragon_knight"),
			(this_or_next|is_between, ":body", "itm_red_dress", "itm_nomad_armor"),
		(this_or_next|is_between, ":body", "itm_berber_robe_a", itm_saracen_kaftan_d+1),
			(this_or_next|is_between, ":body", "itm_meghrebi_leather_a", itm_black_guard+1),
			(this_or_next|is_between, ":body", "itm_kau_castile_a", "itm_teu_brother_surcoat_e"),
			(this_or_next|is_between, ":body", "itm_templar_sarjeant_surcoat", "itm_hirdman_a"),
			(this_or_next|is_between, ":body", "itm_sarranid_cloth_robe", "itm_skirmisher_armor"),
		(this_or_next|eq, ":body", "itm_teu_postulant_a"),
			(this_or_next|eq, ":body", "itm_teu_coat_of_plates"),
			#(this_or_next|is_between, ":body", "itm_veteran_surcoat_a", "itm_kau_aragon_knight"),
			(is_between, ":body", "itm_veteran_surcoat_a", "itm_kau_aragon_knight"),
		(neq, ":body", "itm_kau_aragon_knight"),
		(neq, ":body", "itm_surcoat_lithuania_a"),
		(neq, ":body", "itm_surcoat_lithuania_b"),
		(neq, ":body", "itm_surcoat_novgorod"),
		(neq, ":body", "itm_surcoat_gslask"),
		(neq, ":body", "itm_surcoat_pol_b"),
		(neq, ":body", "itm_teu_hochmeister_surcoat"),
		(neq, ":body", "itm_teu_hbrother_mail"),
		(neq, ":body", "itm_templar_mail_a"),
		(neq, ":body", "itm_templar_gambeson_a"),
		(neq, ":body", "itm_hospitaller_gambeson_a"),
		#(neg|is_between, ":body", "itm_kau_castile_a", "itm_teu_brother_surcoat_e"),
		
		##check foot armor
		(this_or_next|eq, ":foot", "itm_sarranid_boots_a_long"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_b_long"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_d_long"), 
		(this_or_next|eq, ":foot", "itm_byz_lord_boots_long"),
		(this_or_next|eq, ":foot", "itm_cuman_boots"), #for mamluke boots
		(this_or_next|eq, ":foot", "itm_splinted_greaves_long"),
		(this_or_next|eq, ":foot", "itm_mail_boots_long"),
		(this_or_next|eq, ":foot", "itm_legs_with_shoes"),
		(this_or_next|eq, ":foot", "itm_rus_boots_a"),
		(this_or_next|eq, ":foot", "itm_blue_hose"),
		(eq, ":foot", "itm_kau_mail_boots_dark_long"),
		##adjust and equip
		(val_sub, ":foot", 1),
		(agent_equip_item,":agent",":foot"),
		(else_try), #longs boots needed
			#check boots, no body armor is needed. 
			(this_or_next|eq, ":foot", "itm_sarranid_boots_a"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_b"),
			(this_or_next|eq, ":foot", "itm_sarranid_boots_d"), 
			(this_or_next|eq, ":foot", "itm_byz_lord_boots"), 
			(this_or_next|eq, ":foot", "itm_mamluke_boots"), 
			(this_or_next|eq, ":foot", "itm_splinted_greaves"),
		(this_or_next|eq, ":foot", "itm_mail_boots"),
		(this_or_next|eq, ":foot", "itm_berber_shoes"),
		(this_or_next|eq, ":foot", "itm_rus_cav_boots"),
		(this_or_next|eq, ":foot", "itm_priest_2_boots"),
		(eq, ":foot", "itm_kau_mail_boots_dark"),
		#adjust and equip
		(val_add, ":foot", 1),
			(agent_equip_item,":agent",":foot"),  
		(try_end),
	]
	),
	
	## script_set_prsnt_debug
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: center_id
		## Output: reg0 - village mesh, reg1 - castle mesh, reg2 - town mesh
	("set_prsnt_debug",
	[
			(position_set_x, pos1, 50),
		#HORIZONTAL
		(position_set_y, pos1, 50),
		(create_text_overlay, reg0, "@50----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 100),
		(create_text_overlay, reg0, "@100----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 200),
		(create_text_overlay, reg0, "@200----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 300),
		(create_text_overlay, reg0, "@300----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 400),
		(create_text_overlay, reg0, "@400----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 500),
		(create_text_overlay, reg0, "@500----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 600),
		(create_text_overlay, reg0, "@600----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 660),
		(create_text_overlay, reg0, "@660----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_y, pos1, 700),
		(create_text_overlay, reg0, "@700----------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		
		#VERTICAL
		(position_set_y, pos1, 720),
		(position_set_x, pos1, 50),
		(create_text_overlay, reg0, "@050+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 100),
		(create_text_overlay, reg0, "@100+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 150),
		(create_text_overlay, reg0, "@150+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 200),
		(create_text_overlay, reg0, "@200+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 250),
		(create_text_overlay, reg0, "@250+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 300),
		(create_text_overlay, reg0, "@300+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 350),
		(create_text_overlay, reg0, "@350+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 400),
		(create_text_overlay, reg0, "@400+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 450),
		(create_text_overlay, reg0, "@450+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 500),
		(create_text_overlay, reg0, "@500+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 550),
		(create_text_overlay, reg0, "@550+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 600),
		(create_text_overlay, reg0, "@600+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 650),
		(create_text_overlay, reg0, "@650+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 700),
		(create_text_overlay, reg0, "@700+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 750),
		(create_text_overlay, reg0, "@750+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 800),
		(create_text_overlay, reg0, "@800+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 850),
		(create_text_overlay, reg0, "@850+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 900),
		(create_text_overlay, reg0, "@900+", tf_vertical_align_center),
		(overlay_set_position, reg0, pos1),
	]
	),
	
	
	## script_economy_get_buildings
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: none
		## Output: none
	("economy_get_buildings",
	[
		(party_get_slot, ":acres_pasture", "$g_encountered_party", slot_center_acres_pasture),
		
		(party_get_slot, ":head_cattle", "$g_encountered_party", slot_center_head_cattle),
		(party_get_slot, ":head_sheep", "$g_encountered_party", slot_center_head_sheep),
		(party_get_slot, ":head_horses", "$g_encountered_party", slot_center_head_horses),
		(party_get_slot, ":acres_grain", "$g_encountered_party", slot_center_acres_grain),
		(party_get_slot, ":acres_olives", "$g_encountered_party", slot_center_acres_olives),
		(party_get_slot, ":acres_vineyard", "$g_encountered_party", slot_center_acres_vineyard),
		(party_get_slot, ":acres_flax", "$g_encountered_party", slot_center_acres_flax),
		(party_get_slot, ":acres_dates", "$g_encountered_party", slot_center_acres_dates),
		(party_get_slot, ":fishing_fleet", "$g_encountered_party", slot_center_fishing_fleet),
		(party_get_slot, ":salt_pans", "$g_encountered_party", slot_center_salt_pans),
		(party_get_slot, ":apiaries", "$g_encountered_party", slot_center_apiaries),
		(party_get_slot, ":silk_farms", "$g_encountered_party", slot_center_silk_farms),
		(party_get_slot, ":kirmiz_farms", "$g_encountered_party", slot_center_kirmiz_farms),
		(party_get_slot, ":iron_deposits", "$g_encountered_party", slot_center_iron_deposits),
		(party_get_slot, ":fur_traps", "$g_encountered_party", slot_center_fur_traps),
		(party_get_slot, ":household_gardens", "$g_encountered_party", slot_center_household_gardens),
		
		(party_get_slot, ":mills", "$g_encountered_party", slot_center_mills),
		(party_get_slot, ":breweries", "$g_encountered_party", slot_center_breweries),
		(party_get_slot, ":wine_presses", "$g_encountered_party", slot_center_wine_presses),
		(party_get_slot, ":olive_presses", "$g_encountered_party", slot_center_olive_presses),
		(party_get_slot, ":linen_looms", "$g_encountered_party", slot_center_linen_looms),
		(party_get_slot, ":silk_looms", "$g_encountered_party", slot_center_silk_looms),
		(party_get_slot, ":wool_looms", "$g_encountered_party", slot_center_wool_looms),
		(party_get_slot, ":pottery_kilns", "$g_encountered_party", slot_center_pottery_kilns),
		(party_get_slot, ":smithies", "$g_encountered_party", slot_center_smithies),
		(party_get_slot, ":tanneries", "$g_encountered_party", slot_center_tanneries),
		(party_get_slot, ":shipyards", "$g_encountered_party", slot_center_shipyards),
		
		(assign, reg1, ":head_cattle"),
		(assign, reg2, ":head_sheep"),
		(assign, reg3, ":head_horses"),
		(assign, reg4, ":acres_grain"),
		(assign, reg5, ":acres_olives"),
		(assign, reg6, ":acres_vineyard"),
		(assign, reg7, ":acres_flax"),
		(assign, reg8, ":acres_dates"),
		(assign, reg9, ":fishing_fleet"),
		(assign, reg10, ":salt_pans"),
		(assign, reg11, ":apiaries"),
		(assign, reg12, ":silk_farms"),
		(assign, reg13, ":kirmiz_farms"),
		(assign, reg14, ":iron_deposits"),
		(assign, reg15, ":fur_traps"),
		(assign, reg16, ":household_gardens"),
		
		(assign, reg17, ":mills"),
		(assign, reg18, ":breweries"),
		(assign, reg19, ":wine_presses"),
		(assign, reg20, ":olive_presses"),
		(assign, reg21, ":linen_looms"),
		(assign, reg22, ":silk_looms"),
		(assign, reg23, ":wool_looms"),
		(assign, reg24, ":pottery_kilns"),
		(assign, reg25, ":smithies"),
		(assign, reg26, ":tanneries"),
		(assign, reg27, ":shipyards"),
		
		
		(assign, reg0, cost_head_cattle),
		(str_store_string, s1,  "@Cattle farms({reg1})   {reg0}"),
		(assign, reg0, cost_head_sheep),
		(str_store_string, s2,  "@Sheep farms({reg2})    {reg0}"),
		(assign, reg0, cost_head_horses),
		(str_store_string, s3,  "@Horse stables({reg3})  {reg0}"),
		(assign, reg0, cost_acres_grain),
		(str_store_string, s4,  "@Grain farms({reg4})    {reg0}"),
		(assign, reg0, cost_acres_olives),
		(str_store_string, s5,  "@Olive farms({reg5})    {reg0}"),
		(assign, reg0, cost_acres_vineyard),
		(str_store_string, s6,  "@Vineyard farms({reg6}) {reg0}"),
		(assign, reg0, cost_acres_flax),
		(str_store_string, s7,  "@Flax farms({reg7})     {reg0}"),
		(assign, reg0, cost_acres_dates),
		(str_store_string, s8,  "@Date farms({reg8})     {reg0}"),
		(assign, reg0, cost_fishing_fleet),
		(str_store_string, s9,  "@Fishing fleets({reg9}) {reg0}"),
		(assign, reg0, cost_salt_pans),
		(str_store_string, s10, "@Salt pans({reg10})     {reg0}"),
		(assign, reg0, cost_apiaries),
		(str_store_string, s11, "@Apiaries({reg11})      {reg0}"),
		(assign, reg0, cost_silk_farms),
		(str_store_string, s12, "@Silk farms({reg12})    {reg0}"),
		(assign, reg0, cost_kirmiz_farms),
		(str_store_string, s13, "@Kirmz famrs({reg13})   {reg0}"),
		(assign, reg0, cost_iron_deposits),
		(str_store_string, s14, "@Iron deposits({reg14}) {reg0}"),
		(assign, reg0, cost_fur_traps),
		(str_store_string, s15, "@Fur traps({reg15})     {reg0}"),
		(assign, reg0, cost_household_gardens),
		(str_store_string, s16, "@Gabbage farms({reg16}) {reg0}"),
		
		(assign, reg0, cost_mills),
		(str_store_string, s17, "@Mills({reg17})         {reg0}"),
		(assign, reg0, cost_breweries),
		(str_store_string, s18, "@Breweries({reg18})     {reg0}"),
		(assign, reg0, cost_wine_presses),
		(str_store_string, s19, "@Wineries({reg19})      {reg0}"),
		(assign, reg0, cost_olive_presses),
		(str_store_string, s20, "@Olive presses({reg20}) {reg0}"),
		(assign, reg0, cost_linen_looms),
		(str_store_string, s21, "@Linen looms({reg21})   {reg0}"),
		(assign, reg0, cost_silk_looms),
		(str_store_string, s22, "@Silk looms({reg22})    {reg0}"),
		(assign, reg0, cost_wool_looms),
		(str_store_string, s23, "@Wool looms({reg23})    {reg0}"),
		(assign, reg0, cost_pottery_kilns),
		(str_store_string, s24, "@Pottery kilns({reg24}) {reg0}"),
		(assign, reg0, cost_smithies),
		(str_store_string, s25, "@Smithies({reg25})      {reg0}"),
		(assign, reg0, cost_tanneries),
		(str_store_string, s26, "@Tanneries({reg26})     {reg0}"),
		(assign, reg0, cost_shipyards),
		(str_store_string, s27, "@Shipyards({reg27})     {reg0}"),
	]
	),		
	
	
	## script_get_settlement_mesh
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: center_id
		## Output: reg0 - village mesh, reg1 - castle mesh, reg2 - town mesh
	# ("get_settlement_mesh",
	# [
		# (store_script_param, ":center", 1),
		# (party_get_slot, ":culture", ":center", slot_center_culture),
			# (try_begin), #WEST
			# (this_or_next|eq, ":culture", fac_culture_finnish),
			# (this_or_next|eq, ":culture", fac_culture_mazovian),
			# (this_or_next|eq, ":culture", fac_culture_welsh),
			# (this_or_next|eq, ":culture", fac_culture_iberian),
			# (this_or_next|eq, ":culture", fac_culture_nordic),
			# (this_or_next|eq, ":culture", fac_culture_gaelic),
			# (this_or_next|eq, ":culture", fac_culture_anatolian_christian),
			# (this_or_next|eq, ":culture", fac_culture_scotish),
			# (eq, ":culture", fac_culture_western),
			# (assign, reg0, "mesh_pic_cataholic_village"),
			# (assign, reg1, "mesh_pic_cataholic_castle"),
			# (assign, reg2, "mesh_pic_cataholic_town"),
		# (else_try), #BALTIC  
			# (this_or_next|eq, ":culture", fac_culture_baltic),
			# (eq, ":culture", fac_culture_teutonic),
			# (assign, reg0, "mesh_pic_baltic_village"),
			# (assign, reg1, "mesh_pic_baltic_castle"),
			# (assign, reg2, "mesh_pic_baltic_town"),
		# (else_try), #ORTHODOX
			# (this_or_next|eq, ":culture", fac_culture_serbian),
			# (this_or_next|eq, ":culture", fac_culture_balkan),
			# (this_or_next|eq, ":culture", fac_culture_rus),
			# (this_or_next|eq, ":culture", fac_culture_byzantium),
			# (eq, ":culture", fac_culture_mongol),
			# (assign, reg0, "mesh_pic_orthodox_village"),
			# (assign, reg1, "mesh_pic_orthodox_castle"),
			# (assign, reg2, "mesh_pic_orthodox_town"),
		# (else_try), #MUSLIM  
			# (this_or_next|eq, ":culture", fac_culture_marinid),
			# (this_or_next|eq, ":culture", fac_culture_mamluke),
			# (this_or_next|eq, ":culture", fac_culture_andalus),
			# (eq, ":culture", fac_culture_anatolian),
			# (assign, reg0, "mesh_pic_muslim_town"),
			# (assign, reg1, "mesh_pic_muslim_castle"),
			# (assign, reg2, "mesh_pic_muslim_village"),
		# (else_try),
			# (assign, reg0, "mesh_pic_cataholic_village"),
			# (assign, reg1, "mesh_pic_cataholic_castle"),
			# (assign, reg2, "mesh_pic_cataholic_town"),
		# (try_end),
	# ]
	# ),
	
	##check_pope_crown
	("script_check_pope_crown",
	[
		
	]
	),
	
	##script_add_item_to_pool
	("add_item_to_pool",
	[
		(store_script_param, ":item_to_add", 1),
			(store_script_param, ":pool", 2),
		
		#get number of items
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		
		#check if the item is in the pool
		(assign, ":add", 0), 
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),
			(eq, ":item", ":item_to_add"),
			(assign, ":add", 1),
		(try_end),
		(try_begin),
			(eq, ":add", 0),
			#not in the pool, add the item
			(troop_set_slot, ":pool", ":number", ":item_to_add"),
			(troop_set_slot, ":pool", 0, ":number"),
		(try_end),  
	]
	),
	
	
	##script_cf_add_item_to_pool
	("cf_add_item_to_pool",
	[
		(store_script_param, ":item_to_add", 1),
			(store_script_param, ":pool", 2),
		
		#get number of items
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		
		#check if the item is in the pool
		(assign, ":add", 0), 
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),
			(eq, ":item", ":item_to_add"),
			(assign, ":add", 1),
		(try_end),
		(eq, ":add", 0),
		#not in the pool, add the item
		(troop_set_slot, ":pool", ":number", ":item_to_add"),
		(troop_set_slot, ":pool", 0, ":number"),
	]
	),
	
	
	##script_extract_armor_from_tree
	("extract_armor_from_tree",
	[
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		#(store_script_param, ":tier", 3),
		
		(try_begin),
			(gt, ":troop", 0),
			(troop_get_inventory_capacity, ":capacity", ":troop"),
			(try_for_range, ":slot", 0, ":capacity"),
				(troop_get_inventory_slot, ":item", ":troop", ":slot"),
				(gt, ":item", 0),
				(item_get_type, ":type", ":item"),
				(try_begin),
					# (this_or_next|eq, ":type", itp_type_foot_armor),
					# (this_or_next|eq, ":type", itp_type_hand_armor),
					(this_or_next|eq, ":type", itp_type_head_armor),
				(eq, ":type", itp_type_body_armor),
				(call_script, "script_cf_add_item_to_pool", ":item", ":pool"),
				(try_end),
			(try_end),
			(troop_get_upgrade_troop,":upgrade1",":troop", 0),
			(troop_get_upgrade_troop,":upgrade2",":troop", 1),
			(try_begin),
			(gt, ":upgrade1", 0),
			(neq, ":upgrade1", "trp_teu_balt_1"),
			(call_script, "script_extract_armor_from_tree", ":upgrade1", ":pool"),
			(try_end),
			(try_begin),
				(gt, ":upgrade2", 0),
				(neq, ":upgrade2", "trp_teu_balt_1"),
			(call_script, "script_extract_armor_from_tree", ":upgrade2", ":pool"),
			(try_end),
		(try_end),
	]
	),
	
	##script_fill_pools_by_culture
	##description: initialize culture pools
	("fill_pools_by_culture",
	[
		(store_script_param, ":culture", 1),
		(store_script_param, ":pool_commoner", 2),
		(store_script_param, ":pool_noble", 3),
		(faction_get_slot, ":village", ":culture",slot_faction_tier_1_troop),
		(faction_get_slot, ":town", ":culture",slot_faction_tier_1_town_troop),
		(faction_get_slot, ":castle", ":culture",slot_faction_tier_1_castle_troop),
		
		(call_script, "script_extract_armor_from_tree", ":village", ":pool_commoner"),
		(call_script, "script_extract_armor_from_tree", ":town", ":pool_commoner"),
		(call_script, "script_extract_armor_from_tree", ":castle", ":pool_noble"),
	]
	),	
	
	##script_initialize_culture_pools
	##description: initialize culture pools
	("initialize_culture_pools",
	[
		(try_for_range, ":culture", "fac_culture_finnish", "fac_player_faction"),
			(store_sub, ":adjust", ":culture", "fac_culture_finnish"),
		(store_add, ":commoner_pool", "trp_pool_commoner_finnish", ":adjust"),
		(store_add, ":noble_pool", "trp_pool_noble_finnish", ":adjust"),
		(neq, ":culture", "fac_culture_scotish"),
		(call_script, "script_fill_pools_by_culture", ":culture", ":commoner_pool", ":noble_pool"),
		(try_end),
		##extra pools
		(call_script, "script_extract_armor_from_tree", "trp_teu_balt_1", "trp_pool_teutonic_auxiliary"),
		(call_script, "script_extract_armor_from_tree", "trp_scottish_village_recruit", "trp_pool_commoner_scotish"),
		##extra items for magrebs
		(call_script, "script_add_item_to_pool", "itm_new_turban_a", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_new_turban_a", "trp_pool_noble_marinid"),
		(call_script, "script_add_item_to_pool", "itm_new_turban_b", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_new_turban_b", "trp_pool_noble_marinid"),
		(call_script, "script_add_item_to_pool", "itm_megreb_spangen", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_megreb_spangen", "trp_pool_noble_marinid"),
		(call_script, "script_add_item_to_pool", "itm_berber_white_turban", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_berber_white_turban", "trp_pool_noble_marinid"),
		##teutonic knights need more cloths
		(call_script, "script_add_item_to_pool", "itm_teu_monk_surcoat_a", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_teu_gambeson", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_liv_sergeant", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_teu_sergeant", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_teu_hbrother_mail", "trp_pool_noble_teutonic"),
		##merc rebalance
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_spearman", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_guisarmer", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_range", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_horse", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_spearman", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_guisarmer", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_range", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_horse", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_spearman", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_javalin", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_range", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_syrian", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_maghreb_spearman", "trp_pool_commoner_marinid"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_maghreb_range", "trp_pool_commoner_marinid"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_maghreb_horse", "trp_pool_commoner_marinid"),
		#(call_script, "script_extract_armor_from_tree", "trp_merc_almogabar", "trp_pool_commoner_marinid"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_spearman", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_guisarmer", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_range", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_horse", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_spearman", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_guisarmer", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_range", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_horse", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_light", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_spearman", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_guisarmer", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_range", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_horse", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_spearman", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_guisarmer", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_range", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_horse", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_spearman", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_axeman_1", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_spearman_2", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_axeman_2", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_brabantine_spearman", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_brabantine_xbow", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_brabantine_guisarm", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_foot_archer_1", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_foot_archer_2", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_infantry_1", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_infantry_2", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_horse_archer_1", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_horse_archer_2", "trp_pool_sicily_muslims"),
		
		(call_script, "script_extract_armor_from_tree", "trp_cuman_tribesman", "trp_pool_cuman"),
		(call_script, "script_extract_armor_from_tree", "trp_cuman_horseman", "trp_pool_cuman"),
		(call_script, "script_extract_armor_from_tree", "trp_goergian_horse_archer", "trp_pool_georgian"),
		(call_script, "script_extract_armor_from_tree", "trp_kwarezmian_range", "trp_pool_kwarezmian"),
		(call_script, "script_extract_armor_from_tree", "trp_kwarezmian_light_horse", "trp_pool_kwarezmian"),
		(call_script, "script_extract_armor_from_tree", "trp_kwarezmian_medium_horse", "trp_pool_kwarezmian"),
		(call_script, "script_extract_armor_from_tree", "trp_mordovian_foot", "trp_pool_mordovian"),
		(call_script, "script_extract_armor_from_tree", "trp_mordovian_range", "trp_pool_mordovian"),
		(call_script, "script_extract_armor_from_tree", "trp_mordovian_horse", "trp_pool_mordovian"),
		(call_script, "script_extract_armor_from_tree", "trp_kipchak_range", "trp_pool_kipchak"),
		(call_script, "script_extract_armor_from_tree", "trp_kipchak_light_horse", "trp_pool_kipchak"),
		(call_script, "script_extract_armor_from_tree", "trp_kipchak_medium_horse", "trp_pool_kipchak"),

		(display_message, "@Cultural troop pools initalized"),
	]
	),	
	
	
	##script_cf_add_troop_items_armor
	("cf_add_troop_items_armor",
	[
		(store_script_param, ":troop", 1),
			(store_script_param, ":pool", 2),
			(store_script_param, ":armor_from", 3),
			(store_script_param, ":armor_to", 4),
		
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		(assign, ":add", 0), 
		
		(str_store_troop_name, s1, ":troop"),
		(str_store_troop_name, s0, ":pool"),
		(assign, reg0, ":number"), 
		#(display_message, "@pool: {s0} troop: {s1}, pool size: {reg0}"),
		
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),		  
			(item_get_type, ":type", ":item"),
			#(item_get_slot, ":head_armor", ":item", slot_item_head_armor),
			(item_get_slot, ":body_armor", ":item", slot_item_body_armor),
			(assign, ":armor", -1),
			(try_begin),
			# (eq, ":type", itp_type_head_armor),
			# (ge, ":head_armor", ":armor_from"),
			# (le, ":head_armor", ":armor_to"),
			# (assign, ":armor", ":item"),
			# (str_store_item_name, s1, ":item"),
			# (else_try),
			(eq, ":type", itp_type_body_armor),
			(ge, ":body_armor", ":armor_from"),
			(le, ":body_armor", ":armor_to"),
			(assign, ":armor", ":item"),
			(try_end),
			(gt, ":armor", 0),
			(troop_add_item, ":troop", ":armor"),
			(val_add, ":add", 1),
			# (str_store_troop_name, s0, ":troop"),
			# (str_store_item_name, s1, ":armor"),
			# (display_message, "@{s0} adds item {s1}"),
		(try_end),
		(assign, reg0, ":add"),
		(gt, ":add", 0),
	]
	),
	
	##script_cf_add_troop_items_helmet
	("cf_add_troop_items_helmet",
	[
		(store_script_param, ":troop", 1),
			(store_script_param, ":pool", 2),
			(store_script_param, ":armor_from", 3),
			(store_script_param, ":armor_to", 4),
		
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		(assign, ":add", 0), 
		
		(str_store_troop_name, s1, ":troop"),
		(str_store_troop_name, s0, ":pool"),
		(assign, reg0, ":number"), 
		#(display_message, "@pool: {s0} troop: {s1}, pool size: {reg0}"),
		
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),		  
			(item_get_type, ":type", ":item"),
			(item_get_slot, ":head_armor", ":item", slot_item_head_armor),
			#(item_get_slot, ":body_armor", ":item", slot_item_body_armor),
			(assign, ":armor", -1),
			(try_begin),
			(eq, ":type", itp_type_head_armor),
			(ge, ":head_armor", ":armor_from"),
			(le, ":head_armor", ":armor_to"),
			(assign, ":armor", ":item"),
			# (else_try),
			# (eq, ":type", itp_type_body_armor),
			# (ge, ":body_armor", ":armor_from"),
			# (le, ":body_armor", ":armor_to"),
			# (assign, ":armor", ":item"),
			# (str_store_item_name, s1, ":item"),
			(try_end),
			(gt, ":armor", 0),
			(troop_add_item, ":troop", ":armor"),
			(val_add, ":add", 1),
			# (str_store_troop_name, s0, ":troop"),
			# (str_store_item_name, s1, ":armor"),
			# (display_message, "@{s0} adds item {s1}"),
		(try_end),
		(assign, reg0, ":add"),
		(gt, ":add", 0),
	]
	),	
	
	##script_equip_troops_by_tier
	("equip_troops_by_tier",
	[
		(store_script_param, ":troop", 1),
			(store_script_param, ":pool", 2),
			(store_script_param, ":tier", 3),
		
		#addjust tier for range and mounted
		(try_begin),
			(this_or_next|eq, ":troop", "trp_welsh_horse_1"), #welsh are poor
			(troop_is_guarantee_ranged, ":troop"),
			(val_sub, ":tier", 1),
		(else_try),
			(this_or_next|troop_is_guarantee_horse, ":troop"),
			(is_between, ":troop", "trp_balt_noble_recruit", "trp_marinid_village_rabble"), #batl nobility is not mounted
			(neq, ":troop", "trp_tatar_tribesman"),
			(neq, ":troop", "trp_tatar_skirmisher"),
			(neq, ":troop", "trp_tatar_horse_archer"),
			(neq, ":troop", "trp_tatar_veteran_horse_archer"),
			(val_add, ":tier", 1),
		(try_end),		
		#body armor
		(try_begin), # tier_5_body_armor(51)++
			(ge, ":tier", 5),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 51, 200),
			(gt, reg0, 2),
		(else_try), # tier_4_body_armor(41)++
			(ge, ":tier", 4),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 41, 200),
			(gt, reg0, 2),
		(else_try), # tier_2_body_armor(26) - tier_4_body_armor(41)
			(ge, ":tier", 3),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 26, 41),
			(gt, reg0, 2),
		(else_try), # tier_2_body_armor(26) - tier_3_body_armor(33)
			(ge, ":tier", 2),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 26, 33),
			(gt, reg0, 2),
		(else_try),  #tier 1 <tier_2_body_armor(26) 
			#(le, ":tier", 1),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 0, 26),
			(try_end),
		##helmet
		(try_begin), # 70+
			(ge, ":tier", 5),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 70, 200),
			(gt, reg0, 2),
		(else_try), # 60 - 70
			(ge, ":tier", 4),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 60, 70),
			(gt, reg0, 2),
		(else_try), # 40-60
			(ge, ":tier", 3),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 50, 60),
			(gt, reg0, 2),
		(else_try), # <40-50
			(ge, ":tier", 2),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 40, 50),
			(gt, reg0, 2),
		(else_try),  #tier 1 <40
			#(le, ":tier", 1),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 0, 40),
			(try_end),
	]
	),
	
	##script_rebalance_troop_trees
	##description:
	("rebalance_troop_trees",
	[
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		(store_script_param, ":tier", 3),		
		
		(try_begin),
			(gt, ":troop", 0),
			
			##remove current items
			(try_for_range, ":item", "itm_tutorial_spear", "itm_items_end"),
				(item_get_type, ":type", ":item"),
			(this_or_next|eq, ":type", itp_type_head_armor),
			(eq, ":type", itp_type_body_armor),
				(troop_remove_item, ":troop", ":item"),
			(try_end),
			##add new items from pool by tier
			(call_script, "script_equip_troops_by_tier", ":troop", ":pool", ":tier"),
			(troop_equip_items, ":troop"),
			(val_add, ":tier", 1),
			(troop_get_upgrade_troop,":upgrade1",":troop", 0),
			(troop_get_upgrade_troop,":upgrade2",":troop", 1),
			(try_begin),
			(gt, ":upgrade1", 0),
			(neq, ":upgrade1", "trp_teu_balt_1"),
			(call_script, "script_rebalance_troop_trees", ":upgrade1", ":pool", ":tier"),
			(try_end),
			(try_begin),
				(gt, ":upgrade2", 0),
			(neq, ":upgrade2", "trp_teu_balt_1"),
			(call_script, "script_rebalance_troop_trees", ":upgrade2", ":pool", ":tier"),
			(try_end),
		(try_end),
	]
	),
	
	##script_rebalance_troops_by_culture
	##description:
	("rebalance_troops_by_culture",
	[
		(try_for_range, ":culture", "fac_culture_finnish", "fac_player_faction"),
			(store_sub, ":adjust", ":culture", "fac_culture_finnish"),
		(store_add, ":commoner_pool", "trp_pool_commoner_finnish", ":adjust"),
		(store_add, ":noble_pool", "trp_pool_noble_finnish", ":adjust"),
		(neq, ":culture", "fac_culture_scotish"),
			(faction_get_slot, ":village", ":culture",slot_faction_tier_1_troop),
			(faction_get_slot, ":town", ":culture",slot_faction_tier_1_town_troop),
			(faction_get_slot, ":castle", ":culture",slot_faction_tier_1_castle_troop),
		(call_script, "script_rebalance_troop_trees", ":village", ":commoner_pool", 1),
		(call_script, "script_rebalance_troop_trees", ":town", ":commoner_pool", 1),
		(call_script, "script_rebalance_troop_trees", ":castle", ":noble_pool", 1),
		(try_end),
		##extra rebalance
		(call_script, "script_rebalance_troop_trees", "trp_teu_balt_1", "trp_pool_teutonic_auxiliary", 2),
		(call_script, "script_rebalance_troop_trees", "trp_scottish_village_recruit", "trp_pool_commoner_scotish", 1),

		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_spearman", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_guisarmer", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_range", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_horse", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_spearman", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_guisarmer", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_range", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_horse", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_spearman", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_javalin", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_range", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_syrian", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_maghreb_spearman", "trp_pool_commoner_marinid", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_maghreb_range", "trp_pool_commoner_marinid", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_maghreb_horse", "trp_pool_commoner_marinid", 3),
		#(call_script, "script_rebalance_troop_trees", "trp_merc_almogabar", "trp_pool_commoner_marinid", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_spearman", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_guisarmer", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_range", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_horse", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_spearman", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_guisarmer", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_range", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_horse", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_light", "trp_pool_commoner_iberian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_spearman", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_guisarmer", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_range", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_horse", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_spearman", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_guisarmer", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_range", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_horse", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_spearman", "trp_pool_commoner_gaelic", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_axeman_1", "trp_pool_commoner_gaelic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_spearman_2", "trp_pool_commoner_gaelic", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_axeman_2", "trp_pool_commoner_gaelic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_brabantine_spearman", "trp_pool_commoner_western", 4),
		(call_script, "script_rebalance_troop_trees", "trp_merc_brabantine_xbow", "trp_pool_commoner_western", 4),
		(call_script, "script_rebalance_troop_trees", "trp_merc_brabantine_guisarm", "trp_pool_commoner_western", 4),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_foot_archer_1", "trp_pool_sicily_muslims", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_foot_archer_2", "trp_pool_sicily_muslims", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_infantry_1", "trp_pool_sicily_muslims", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_infantry_2", "trp_pool_sicily_muslims", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_horse_archer_1", "trp_pool_sicily_muslims", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_horse_archer_2", "trp_pool_sicily_muslims", 3),
		
		(call_script, "script_rebalance_troop_trees", "trp_cuman_tribesman", "trp_pool_cuman", 1),
		(call_script, "script_rebalance_troop_trees", "trp_cuman_horseman", "trp_pool_cuman", 1),
		(call_script, "script_rebalance_troop_trees", "trp_goergian_horse_archer", "trp_pool_georgian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kwarezmian_range", "trp_pool_kwarezmian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kwarezmian_light_horse", "trp_pool_kwarezmian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kwarezmian_medium_horse", "trp_pool_kwarezmian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_mordovian_foot", "trp_pool_mordovian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_mordovian_range", "trp_pool_mordovian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_mordovian_horse", "trp_pool_mordovian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kipchak_range", "trp_pool_kipchak", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kipchak_light_horse", "trp_pool_kipchak", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kipchak_medium_horse", "trp_pool_kipchak", 3),
		
		(display_message, "@Troop rebalanced"),
	]
	),
	
	]
