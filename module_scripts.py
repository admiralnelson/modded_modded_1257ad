# -*- coding: utf-8 -*-

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
from script.procedures import AD1257_party as procedure_AD1257_party
from script.procedures import AD1257_manor_system as procedure_AD1257_manor_system
from script.procedures import AD1257_campaign as procedure_AD1257_campaign
from script.procedures import AD1257_camera_scene as procedure_AD1257_camera_scene
from script.procedures import AD1257_utils as procedure_AD1257_utils
from script.procedures import AD1257_ItemMod_init as procedure_AD1257_itemmod_init
from script.procedures import AD1257_agent_looks as procedure_AD1257_agent_looks
from script.procedures import AD1257_battle as procedure_AD1257_battle
from script.procedures import AD1257_battle_ai as procedure_AD1257_battle_ai
from script.procedures import AD1257_pool as procedure_AD1257_pool
from script.procedures import AD1257_debug as procedure_AD1257_debug
from script.procedures import AD1257_tournament as procedure_AD1257_tournament
from script.procedures import AD1257_troop as procedure_AD1257_troop
from script.procedures import AD1257_companion as procedure_AD1257_companion
from script.procedures import AD1257_lance_system as procedure_AD1257_lance_system
from script.procedures import AD1257_manor_economy as procedure_AD1257_manor_economy
from script.procedures import AD1257_misc as procedure_AD1257_misc
from script.procedures import AD1257_freelancer as procedure_AD1257_freelancer
from script.procedures import AD1257_additional_formation as procedure_AD1257_additional_formation
from script.procedures import AD1257_item as procedure_AD1257_item
from script.procedures import AD1257_weather as procedure_AD1257_weather
from script.procedures import AD1257_economy as procedure_AD1257_economy

from script.procedures import Mod_AutoLoot as procedure_mod_autoloot
from script.procedures import Mod_Diplomacy as procedure_mod_diplomacy
from script.procedures import Mod_Formation as procedure_mod_formation
from script.procedures import Mod_Formation_ai as procedure_mod_formation_ai
from script.procedures import Mod_Formation_utils as procedure_mod_formation_util

from script.procedures import Modded2x as procedure_modded2x
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
from script.functions import faction_ai as function_faction_ai 
from script.functions import troop_ai as fuunction_troop_ai

from script.functions import AD1257 as function_AD1257
from script.functions import AD1257_regions as function_AD1257_regions
from script.functions import AD1257_utils as function_AD1257_utils
from script.functions import AD1257_economy as function_AD1257_economy
from script.functions import AD1257_party as function_AD1257_party
from script.functions import AD1257_troop as function_AD1257_troop
from script.functions import AD1257_campsite as function_AD1257_campsite
from script.functions import AD1257_mercenary as function_AD1257_mercenary
from script.functions import AD1257_manor_system as function_AD1257_manor_system
from script.functions import AD1257_freelancer as function_AD1257_freelancer
from script.functions import AD1257_battle_ai as function_AD1257_battle_ai
from script.functions import AD1257_lance_sys as function_AD1257_lance_system
from script.functions import helper as function_helper

from script.functions import Mod_Diplomacy_economy as function_mod_diplomacy_economy
from script.functions import Mod_Diplomacy as function_mod_diplomacy
from script.functions import Mod_Formation as function_mod_formation
from script.functions import Mod_Formation_utils as function_mod_formation_util
from script.functions import Mod_Formation_ai as function_mod_formation_ai
from script.functions import Mod_AutoLoot as function_mod_autoloot
from script.functions import Modded2x as function_modded2x


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
from script.conditional_functions import tutorial as cfunction_tutorial

from script.conditional_functions import AD1257 as cfunction_AD1257
from script.conditional_functions import Mod_Formation as cfunction_mod_formation
from script.conditional_functions import AD1257_pool as cfunction_AD1257_pool
from script.conditional_functions import AD1257_companion as cfunction_AD1257_companion
from script.conditional_functions import AD1257_mercenary as cfunction_AD1257_mercenary
from script.conditional_functions import AD1257_freelancer as cfunction_AD1257_freelancer

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

keys = [key_0, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_a, key_b, key_c, key_d, key_e, key_f, key_g, key_h, key_i, key_j, key_k, key_l, key_m, key_n, key_o, key_p, key_q, key_r, key_s, key_t, key_u, key_v, key_w, key_x, key_y, key_z, key_numpad_0, key_numpad_1, key_numpad_2, key_numpad_3, key_numpad_4, key_numpad_5, key_numpad_6, key_numpad_7, key_numpad_8, key_numpad_9, key_num_lock, key_numpad_slash, key_numpad_multiply, key_numpad_minus, key_numpad_plus, key_numpad_enter, key_numpad_period, key_insert, key_delete, key_home, key_end, key_page_up, key_page_down, key_up, key_down, key_left, key_right, key_f1, key_f2, key_f3, key_f4, key_f5, key_f6, key_f7, key_f8, key_f9, key_f10, key_f11, key_f12, key_space, key_escape, key_enter, key_tab, key_back_space, key_open_braces, key_close_braces, key_comma, key_period, key_slash, key_back_slash, key_equals, key_minus, key_semicolon, key_apostrophe, key_tilde, key_caps_lock, key_left_shift, key_right_shift, key_left_control, key_right_control, key_left_alt, key_right_alt]
	#### Autoloot improved by rubik end

# procedures and functions are located on script subdirectory.
# procedures: script that doesn't return a value (doesn't assign value to reg0..regN or s0..SN)
# namespaces
#	procedure_game_init : procedures on this namespaces will always be called by the game engine during initialisation (new game/quick battle/multiplayer)
# 	procedure_game : procedures on this namespaces will always be called by the game engine at any time (not specific)
#	procedure_quick_battle : related to quick_battle feature (UI, functionality, etc)
# 	procedure_campaign : campaign system (during overworld map)
#	procedure_campaign_simulation : AI algorithms/simulation in overworld map


# function: script that  returns a value
# namespaces
# 	function_game : function on this namespaces will always be called by the game engine at any time (not specific)
#	function_quick_battle : related to quick_battle feature (UI, functionality, etc)
#   function_console : console functionality (get console input)
#	function_economy : item price calculation 


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
	# WARNING: HEAVILY modified by 1257AD devs
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
		]), 
		
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
	
	#script_lord_get_home_center
	# INPUT: troop no (lord)
	# OUTPUT center
	function_troop.lord_get_home_center,
	
	#script_get_kingdom_lady_social_determinants
	# WARNING: modified by 1257AD devs contain diplomacy script/stuffs.
	# CONTAINS: dimplomacy script
	#Calradian society is rather patriarchal, at least among the upper classes
	#INPUT: lady
	#OUTPUT: closest male relative, town center
	function_troop.get_kingdom_lady_social_determinants,
	
	#script_age_troop_one_year
	#NOTE: note to self modded2x: update lords, kings, and lady age in notes
	#This is probably unnecessarily complicated, but can support a multi-generational mod
	# INPUT: troop no
	# OUTPUT: NONE
	procedure_troop.age_troop_one_year,
	
	
	#script_add_lady_items
	#INPUT: lady no
	#OUTPUT: NONE
	procedure_troop.add_lady_items,
	
	#script_init_troop_age
	#INPUT: troop no, age
	#OUTPUT: none
	procedure_troop.init_troop_age,
	
	#script_assign_troop_love_interests
	#Called at the beginning, or whenever a lord is spurned
	#INPUT: troop no
	#OUTPUT: none
	procedure_troop.assign_troop_love_interests,
	

	#script_faction_conclude_feast
	#INPUT: faction no, venue
	#OUTPUT: nobility_in_attendance, nobility_in_faction
	function_faction.faction_conclude_feast,
	
	#script_lady_evaluate_troop_as_suitor
	#INPUT: lady, suitor
	#OUTPUT: final_score
	function_troop.lady_evaluate_troop_as_suitor,
	
	#script_courtship_event_troop_court_lady
	#INPUT: suitor, lady
	#OUTPUT: none
	procedure_troop.courtship_event_troop_court_lady,
	
	
	#script_courtship_event_lady_break_relation_with_suitor
	#INPUT: lady, suitor
	#OUTPUT: none
	procedure_troop.courtship_event_lady_break_relation_with_suitor,
	
	#script_courtship_event_bride_marry_groom
	#INPUT: bride, groom, elopement
	#OUTPUT: none
	procedure_troop.courtship_event_bride_marry_groom,
	
	
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
	fuunction_troop_ai.npc_decision_checklist_party_ai,
	
	#script_npc_decision_checklist_troop_follow_or_not
	# WARNING: behaviour is different from native. modified by 1257AD devs
	# INPUT: troop_no
	# OUTPUT: reg0
	fuunction_troop_ai.npc_decision_checklist_troop_follow_or_not,
	

	#script_find_total_prosperity_score
	# INPUT: center_no
	# OUTPUT: reg0 = total_prosperity_score
	function_town.find_total_prosperity_score,
	
	#script_calculate_center_assailability_score
	# INPUT: faction_no
	# param1: faction_no
	# param2: all_vassals_included, (becomes 1 if we want to find attackable center if we collected 20% of vassals during gathering army phase)
	# OUTPUT:
	# reg0 = center_to_attack (-1 if none is logical)
	# reg1 = maximum_attack_score
	function_faction.calculate_center_assailability_score,
	
	#script_find_center_to_defend
	# INPUT:
	# param1: faction_no
	# OUTPUT:
	# reg0 = center_to_defend (-1 if none is logical)
	# reg1 = maximum_defend_score
	# reg3 = enemy_strength_near_most_threatened_center
	function_faction.find_center_to_defend,
	
	
	#script_npc_decision_checklist_peace_or_war
	# WARNING: heavily modified by 1257AD devs
	#INPUT: actor_faction, target_faction, envoy
	#OUTPUT: s14 explainer_string, reg0 result, reg1 explainer_string
	function_faction_ai.npc_decision_checklist_peace_or_war,
	
	#script_npc_decision_checklist_male_guardian_assess_suitor
	#called from dialogs
	#WARNING: heavily modified by 1257AD devs
	#INPUT: lord, suitor
	#OUTPUT: reg0 result, reg1 explainer_string
	fuunction_troop_ai.npc_decision_checklist_male_guardian_assess_suitor,
	
	#script_npc_decision_checklist_marry_female_pc
	#INPUT: npc
	#OUTPUT: lord_agrees
	fuunction_troop_ai.npc_decision_checklist_marry_female_pc,
	
	
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
	
	
	#script_courtship_poem_reactions
	#Called from dialogs
	#INPUT: lady, poem
	#OUTPUT: result
	function_troop.courtship_poem_reactions,
	
	#script_diplomacy_faction_get_diplomatic_status_with_faction
	#INPUT: actor_faction, target_faction
	#OUTPUT: result, duration

	function_faction.diplomacy_faction_get_diplomatic_status_with_faction,
	
	#script_faction_follows_controversial_policy
	#INPUT: faction_no, policy_type
	#OUTPUT: none
	procedure_faction.faction_follows_controversial_policy,
	
	#script_internal_politics_rate_feast_to_s9
	#INPUT: householder, num_servings, consume_items
	#OUTPUT: none
	procedure_campaign.internal_politics_rate_feast_to_s9,
	
	#script_faction_get_adjective_to_s10
	#INPUT: faction_no
	#OUTPUT: s10 adjective_string
	function_faction.faction_get_adjective_to_s10,
	
	#script_setup_tavern_attacker
	# WARNING: modified by 1257AD devs
	#INPUT: entry point in the area
	#OUTPUT: none
	procedure_scene.setup_tavern_attacker,
	
	#script_activate_tavern_attackers
	#INPUT: none
	#OUTPUT: none
	procedure_scene.activate_tavern_attackers,
	

	#script_activate_tavern_attackers
	#INPUT: none
	#OUTPUT: none
	procedure_scene.deactivate_tavern_attackers,
	
	#script_activate_town_guard
	#INPUT: none
	#OUTPUT: none
	procedure_scene.activate_town_guard,
	
	#script_cf_prisoner_offered_parole
	#this determines whether or not a lord is thrown into a dungeon by his captor, or is kept out on parole
	#Not currently used (ie, it always fails)
	#INPUT: prisoner
	#OUTPUT: none
	cfunction_troop.cf_prisoner_offered_parole,
	
	#script_neutral_behavior_in_fight
	#WARNING: modified by 1257AD devs
	#INPUT: none
	#OUTPUT: none
	function_battle.neutral_behavior_in_fight,
	
	#script_party_inflict_attrition
	#WARNING: modified by 1257AD devs
	#INPUT: party, attrition_rate
	#OUTPUT: none
	procedure_party.party_inflict_attrition,
	
	
	
	#script_add_rumor_string_to_troop_notes
	# called from dialog
	#INPUT: object_1, object_2, string
	#OUTPUT: NONE 
	procedure_note.add_rumor_string_to_troop_notes,
	
	("character_can_wed_character", #empty now, but might want to add mid-game
		[
	]),
	
	("troop_change_career", #empty now, but might want to add mid-game
		[
	]),
	
	#script_center_get_goods_availability
	#INPUT: center_no
	#OUTPUT: hardship_index
	function_economy.center_get_goods_availability,

	#script_lord_find_alternative_faction
	#WARNING: modified by 1257AD devs
	#Also, make it so that lords will try to keep at least one center unassigned
	#INPUT: troop no
	#OUTPUT: new_faction
	function_troop.lord_find_alternative_faction,
	
	#script_lord_find_alternative_faction_old
	#WARNING: this is totally new procedure (not present in native). 1257AD devs
	#reverted back to 1.134 
	#INPUT: troop_no
	#OUTPUT: new_faction
	 function_AD1257.lord_find_alternative_faction_old,
	
	#script_set_up_duel_with_troop
	#INPUT: duel_troop
	#OUTPUT: none
	procedure_scene.set_up_duel_with_troop,
	
	("test_player_for_career_and_marriage_incompatability", #empty now, but might want to add mid-game
		[
		#Married to a lord of one faction, while fighting for another
		#Married to one lord while holding a stipend from the king
	]),
	
	#script_deduct_casualties_from_garrison
	#INPUT: none
	#OUTPUT: none
	procedure_campaign.deduct_casualties_from_garrison,
	
	#script_npc_decision_checklist_take_stand_on_issue
	#Called from dialogs, and from simple_triggers
	#INPUT: troop_no
	#OUTPUT: result, result_explainer
	fuunction_troop_ai.npc_decision_checklist_take_stand_on_issue,
	
	
	("npc_decision_checklist_evaluate_faction_strategy",
		[
		#Decides whether the strategy is good or bad -- to be added
	]),
	
	#script_process_player_enterprise
	#INPUT: item_type, center
	#OUTPUT:
	#	reg0 profit_per_cycle"
	#	reg1 final_price_for_total_produced_goods"
	#	reg2 final_price_for_total_inputs"
	#	reg3 price_of_labor"
	#	reg4 final_price_for_single_produced_good"
	#	reg5 final_price_for_single_input"
	#	reg10 final_price_for_secondary_input"
	function_economy.process_player_enterprise,
	
	# script_replace_scene_items_with_spawn_items_before_ms
	# Input: none
	# Output: none
	procedure_scene.replace_scene_items_with_spawn_items_before_ms,
	
	# script_replace_scene_items_with_spawn_items_after_ms
	# Input: none
	# Output: none
	procedure_scene.replace_scene_items_with_spawn_items_after_ms,
	
	# script_cf_is_melee_weapon_for_tutorial
	# Input: arg1 = item_no
	# Output: none (can fail)
	cfunction_tutorial.cf_is_melee_weapon_for_tutorial,
	
	# script_iterate_pointer_arrow
	# procedure to rotate that pointer arrow when you hold F1
	# Input: none
	# Output: none
	procedure_scene.iterate_pointer_arrow,
	
	#script_find_center_to_attack_alt
	#INPUT: troop_no, attack_by_faction, all_vassals_included
	#OUTPUT: result, score_to_beat
	function_faction.find_center_to_attack_alt,
	
	#script_npc_decision_checklist_evaluate_enemy_center_for_attack
	#WARNING: modified by 1257AD devs
	#INPUT: troop_no, potential_target, attack_by_faction, all_vassals_included
	#OUTPUT: result, result_explainer, power_ratio

	fuunction_troop_ai.npc_decision_checklist_evaluate_enemy_center_for_attack,
	
	#script_npc_decision_checklist_faction_ai_alt
	#WARNING: heavily modified by 1257AD devs
	#This is called from within decide_faction_ai, or from (modded2x: from wat?)
	#INPUT troop_no
	#OUTPUT: action, object
	fuunction_troop_ai.npc_decision_checklist_faction_ai_alt,

	#script_faction_last_reconnoitered_center
	#This is called from within decide_faction_ai, or from (modded2x: wat?)
	#INPUT: faction_no, center_no
	#OUTPUT: hours_since_last_recon, last_recon_time
	function_faction.faction_last_reconnoitered_center,
	
	#script_reduce_exact_number_to_estimate
	#This is used to simulate limited intelligence
	#It is roughly analogous to the descriptive strings which the player will receive from alarms
	#Information is presumed to be accurate for four days
	#This is obviously cheating for the AI, as the AI will have exact info for four days, and no info at all after that.
	#It would be fairly easy to log the strength at a center when it is scouted, if we want, but I have not done that at this point,
	#The AI also has a hive mind -- ie, each party knows what its allies are thinking. In this, AI factions have an advantage over the player
	#It would be a simple matter to create a set of arrays in which each party's knowledge is individually updated, but that would also take up a lot of data space
	#INPUT: exact_number
	#OUTPUT: estimate
	function_helper.reduce_exact_number_to_estimate,
	
	#script_calculate_castle_prosperities_by_using_its_villages
	#WARNING: modified by 1257AD devs
	#This is called from within decide_faction_ai, or from (modded2x: again, wat? thing like this is so cryptic and hard to understand)
	#INPUT: none
	#OUTPUT: none
	procedure_economy.calculate_castle_prosperities_by_using_its_villages,
	
	#script_initialize_tavern_variables
	#INPUT: none
	#OUTPUT: none
	procedure_scene.initialize_tavern_variables,
	
	#script_prepare_alley_to_fight
	#INPUT: none
	#OUTPUT: none
	procedure_scene.prepare_alley_to_fight,
	
	#script_prepare_town_to_fight
	#INPUT: none
	#OUTPUT: none
	procedure_scene.prepare_town_to_fight,
	
	#script_change_player_right_to_rule
	#INPUT: right_to_rule_dif
	#OUTPUT: none
	procedure_player.change_player_right_to_rule,

	#script_indict_lord_for_treason
	#originally included in simple_triggers. Needed to be moved here to allow player to indict
	#INPUT: troop_no, faction
	#OUTPUT: none
	procedure_faction.indict_lord_for_treason,
	
	
	# script_give_center_to_faction_while_maintaining_lord
	# Input: arg1 = center_no, arg2 = faction
	# Output: none
	procedure_faction.give_center_to_faction_while_maintaining_lord,
	

	# script_check_concilio_calradi_achievement
	procedure_game.check_concilio_calradi_achievement,
	
	
	#  ("cf_check_quest_active_for_troop",
	#    [
	#      (store_script_param_1, ":quest_no"),
	#      (store_script_param_2, ":troop_no"),
	
	#	  (check_quest_active, ":quest_no"),
	#	  (quest_slot_eq, ":quest_no", slot_quest_giver_troop, ":troop_no"),
	
	# ]),
	
	# matching sets
	
	# script_set_matching_items
	# Input: arg1 = body_item, arg2 = agent_no, arg3 = troop_no
	# Output: none
	procedure_item.set_matching_items,
	
	# script_distance_between_factions
	# INPUT: attacker_party, defender_party
	# OUTPUT: distance
	function_party.distance_between_factions,
	

	# script_is_party_on_water
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: party_id
	# OUTPUT: none. boolean
	cfunction_AD1257.cf_is_party_on_water,
	
	#script_raf_replace_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: party_id, old_troop, new_troop
	#OUTPUT: NONE
	procedure_AD1257.raf_replace_troop,
	
	# deathcam #############################
	# script_dmod_cycle_forwards
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# Output: New $dmod_current_agent
	# Used to cycle forwards through valid agents
	procedure_AD1257_camera_scene.dmod_cycle_forwards,
	
	# script_dmod_cycle_backwards
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# Output: New $dmod_current_agent
	# Used to cycle backwards through valid agents
	procedure_AD1257_camera_scene.dmod_cycle_backwards,
	
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
	cfunction_town.cf_town_recruit_volunteers_cond,

	#script_tom_aor_faction_to_region
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: for lance recruitment system, select region. whitout player kingdom interferance
	# INPUT: faction
	# OUTPUT: region
	function_AD1257_regions.tom_aor_faction_to_region,
	
	#script_raf_aor_faction_to_region
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: faction
	#OUTPUT: region
	function_AD1257_regions.raf_aor_faction_to_region,
	
	#script_raf_aor_region_to_faction
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: region
	#OUTPUT: faction
	function_AD1257_regions.raf_aor_region_to_faction,

	#script_raf_create_incidents
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#INPUT: none
	#OUTPUT: none
	procedure_AD1257_campaign.raf_create_incidents,
	
	#script_spawn_manors - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	# DESCRIPTION: Spawns random manor type to villages, castles and towns
	procedure_AD1257_manor_system.spawn_manors,
	
	#script_spawn_manor_party - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: party to spawn, center to bind to and spawn around it, bound and rename party(if 0 - not, only for manors).
	#output: reg0 - party id.
	procedure_AD1257_manor_system.spawn_manor_party,
	
	#script_update_manor_array
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: none
	#output: none
	#updates the trp_manor_array troop, which is the storage troop for manor id
	procedure_AD1257_manor_system.update_manor_array,
	
	
	#script_prepare_manor_troops
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input:none
	#output:none
	#description: this will set the goods of the manor craftsman
	procedure_AD1257_manor_system.prepare_manor_troops,
	
	#script_manor_set_unique_scene
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# NOTE: modded2x: might be cool to alter the terrain algorithms
	#input:manor_party_id, center
	#output: none
	#description: sets the manor scene based on it's terrain type
	procedure_AD1257_manor_scene.manor_set_unique_scene,
	
	
	#script_spawn_mongols
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	# DESCRIPTION: This script will spawn a camp at each of the monglian faction towns.
	procedure_AD1257_party.spawn_mongols,	  
	

	#script_cf_spawn_crusaders_and_jihadists
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_party.cf_spawn_crusaders_and_jihadists,
	
	#script_spawn_balts
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_party.spawn_balts,
	
	#script_spawn_peasant_rebels
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_party.spawn_peasant_rebels,

	##diplomacy begin
	#recruiter kit begin
	#script_dplmc_send_recruiter
	#INPUT: number_of_recruits, faction_of_recruits,recruit_type
	#OUTPUT: none
	procedure_mod_diplomacy.dplmc_send_recruiter,
	#recruiter kit end

	#script_dplmc_send_recruiter
	#INPUT: number_of_recruits, faction_of_recruits,recruit_type
	#OUTPUT: s4 prosperity string
	function_mod_diplomacy.dplmc_describe_prosperity_to_s4,
	
	#script_dplmc_pay_into_treasury
	#INPUT: amount
	#OUTPUT:none
	procedure_mod_diplomacy.dplmc_pay_into_treasury,

	#script_dplmc_withdraw_from_treasury
	#INPUT: amount
	#OUTPUT:none
	procedure_mod_diplomacy.dplmc_withdraw_from_treasury,
	
	#script_dplmc_describe_tax_rate_to_s50
	# WARNING: modified by 1257AD devs
	#INPUT: tax_rate
	#OUTPUT: s50 str_id
	function_mod_diplomacy.dplmc_describe_tax_rate_to_s50,
	
	#script_dplmc_player_troops_leave
	#INPUT: percent
	#OUTPUT: deserters
	function_mod_diplomacy.dplmc_player_troops_leave,
	
	#script_dplmc_get_item_buy_price_factor
	#INPUT: item_kind_id, center_no
	#OUTPUT: price_factor
	function_mod_diplomacy_economy.dplmc_get_item_buy_price_factor,
	
	#script_dplmc_party_calculate_strength
	#INPUT: party, party_leader_exclusion
	#OUTPUT: sum
	function_mod_diplomacy.dplmc_party_calculate_strength,
	
	#script_dplmc_start_alliance_between_kingdoms, 20 days alliance, 40 days truce after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	procedure_mod_diplomacy.dplmc_start_alliance_between_kingdoms,
	
	#script_dplmc_start_defensive_between_kingdoms, 20 days defensive: 20 days trade aggreement, 20 days non-aggression after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	procedure_mod_diplomacy.dplmc_start_defensive_between_kingdoms,
	
	#script_dplmc_start_trade_between_kingdoms, 20 days trade aggreement, 20 days non-aggression after that
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	procedure_mod_diplomacy.dplmc_start_trade_between_kingdoms,
	
	#script_dplmc_start_nonaggression_between_kingdoms, 20 days non-aggression
	# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
	# Output: none
	procedure_mod_diplomacy.dplmc_start_nonaggression_between_kingdoms,
	
	
	#script_dplmc_get_prisoners_value_between_factions
	# Input: arg1 = faction_no_1, arg2 = faction_no_2
	# Output: faction_no_1 - faction_no_2
	function_mod_diplomacy_economy.dplmc_get_prisoners_value_between_factions,
	
	#script_dplmc_get_truce_pay_amount
	# Input: arg1 = faction_no_1, arg2 = faction_no_2
	# Output: concession_value
	function_mod_diplomacy_economy.dplmc_get_truce_pay_amount,
	
	#script_dplmc_player_center_surrender
	#INPUT: center_no
	#OUTPUT: none
	procedure_mod_diplomacy.dplmc_player_center_surrender,
	
	#script_dplmc_send_messenger_to_troop
	#INPUT: target_troop, message, orders_object
	#OUTPUT: none
	procedure_mod_diplomacy.dplmc_send_messenger_to_troop,

	#script_dplmc_send_messenger_to_party
	#INPUT: target_party, message, orders_object
	#OUTPUT: none
	procedure_mod_diplomacy.dplmc_send_messenger_to_party,
	
	#script_dplmc_send_gift
	#INPUT: target_troop, gift
	#OUTPUT: none
	procedure_mod_diplomacy.dplmc_send_gift,
	
	#script_dplmc_send_gift_to_center
	#INPUT: target_party, gift
	#OUTPUT: none
	procedure_mod_diplomacy.dplmc_send_gift_to_center,
	
	#script_dplmc_troop_political_notes_to_s47
	#INPUT: troop_no
	#OUTPUT: s47
	function_mod_diplomacy.dplmc_troop_political_notes_to_s47,
	
	
	## CC
	####################################################################################
	#
	# Autoloot Scripts begin
	# ---------------------------------------------------
	####################################################################################
	
	# script_troop_can_use_item
	# TAGS: Custom Commander(CC)
	# Can a troop qualify to use this item?
	# INPUT: troop, item, item modifiers	
	# Returns 1 = yes, 0 = no.
	function_mod_autoloot.troop_can_use_item,

	################################################################
	##### Custom Commander(CC)
	################################################################

	#script_get_item_value_with_imod
	# TAGS: Custom Commander(CC)
	#INPUT: item ID, item modifier
	#OUTPUT: item value
	function_mod_autoloot.get_item_value_with_imod,
	
	#script_get_item_score_with_imod
	#INPUT: item ID, item modifier
	#OUTPUT	: item with imod score	
	function_mod_autoloot.get_item_score_with_imod,
	################################################################
	##### Custom Commander(CC)
	################################################################
	

	#script_print_wpn_upgrades_to_s0
	# TAGS: Custom Commander(CC)
	# Used in conversations
	# INPUT: troop
	# OUTPUT: s0
	function_mod_autoloot.print_wpn_upgrades_to_s0,
		
	#script_copy_upgrade_to_all_heroes
	# Copy this troop's upgrade options to everyone
	# INPUT	: troop, type
	# OUTPUT : none
	procedure_mod_autoloot.copy_upgrade_to_all_heroes,
	
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

	#script_auto_loot_all
	# Let each hero loot from the pool
	# WARNING: some part of this script are disabled.
	# INPUT	: none
	# OUTPUT : none
	procedure_mod_autoloot.auto_loot_all,
	
	
	#script_auto_loot_troop
	# let this troop take its pick from the loot pool
	# WARNING: some part of this script are disabled.	
	# TAGS: Custom Commander(CC)
	# INPUT	: troop, pool
	# OUTPUT : NONE
	procedure_mod_autoloot.auto_loot_troop,
	
	#script_scan_for_best_item_of_type
	# Search for the most expensive item of a specified type
	# INPUT	: troop, item_type, troop_using
	# OUTPUT : best_slot	
	function_mod_autoloot.scan_for_best_item_of_type,
	
	# script_exchange_equipments_between_two_sets
	# Input: none
	# Output: none
	procedure_mod_autoloot.exchange_equipments_between_two_sets,
	
	# script_transfer_inventory
	# INPUT	: source, dest, trans_book
	# OUTPUT : none
	procedure_mod_autoloot.transfer_inventory,
	
	# script_transfer_special_inventory
	# INPUT	: source, dest
	# OUTPUT : none
	procedure_mod_autoloot.transfer_special_inventory,
	####################################################################################
	# 
	# Autoloot Scripts end
	# ---------------------------------------------------
	####################################################################################
	
	# script_init_item_score
	# INPUT	: none
	# OUTPUT : none
	procedure_AD1257_itemmod_init.init_item_score,
	
	# script_get_inventory_weight_of_whole_party
	# INPUT	: none
	# OUTPUT : none
	procedure_AD1257_utils.get_inventory_weight_of_whole_party,
	
	# script_sort_food
	# INPUT	: troop_no
	# OUTPUT : none
	procedure_AD1257_utils.sort_food,
	
	# script_auto_sell
	# INPUT	: customer, merchant
	# OUTPUT : none
	procedure_AD1257_utils.auto_sell,
	
	# script_start_town_conversation
	# INPUT	: troop_slot_no, entry_no
	# OUTPUT : none
	procedure_AD1257_utils.start_town_conversation,
	
	# script_get_book_read_slot
	# INPUT	: troop_no, item_no
	# OUTPUT : slot_no
	function_AD1257_utils.get_book_read_slot,
	
	# script_get_troop_max_hp
	# INPUT	: troop_no
	# OUTPUT : skill
	function_AD1257_utils.get_troop_max_hp,

	# script_get_current_item_for_autoloot
	# INPUT	: wpn_set, slot_no
	# OUTPUT : s10 item name
	function_mod_autoloot.get_current_item_for_autoloot,

	# script_prsnt_lines
	# NOTE: draws a black line
	# INPUT	: size_x, size_y, pos_x, pos_y
	# OUTPUT : NONE
	procedure_AD1257_ui.prsnt_lines,
	
	#script_copy_inventory
	# INPUT: source, target
	# OUTPUT: NONE
	procedure_AD1257_utils.copy_inventory,
	
	#script_sell_all_prisoners
	# INPUT: NONE
	# OUTPUT: NONE
	procedure_AD1257_utils.sell_all_prisoners,
	

	#script_get_dest_color_from_rgb
	# INPUT: red, green, blue
	# OUTPUT: cur_color (in hex value)
	function_AD1257_utils.get_dest_color_from_rgb,
	
	#script_convert_rgb_code_to_html_code
	# NOTE: modded2x: (redundant? )
	# INPUT: red, green, blue
	# OUTPUT: s0 
	function_AD1257_utils.convert_rgb_code_to_html_code,
		
		#script_convert_slot_no_to_color
		# INPUT: red, green, blue
		# OUTPUT: dest_color 							
		function_AD1257_utils.convert_slot_no_to_color,
		
		#script_raf_send_messenger_to_companion
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: target_party, orders_object
		# OUTPUT: NONE 		
		procedure_AD1257.raf_send_messenger_to_companion,
		
		#script_raf_troop_get_religion
		# INPUT: troop
		# OUTPUT: religion	 		
		function_AD1257.raf_troop_get_religion,
		
		#script_prsnt_upgrade_tree_switch
		# WARNING: some part of this script are disabled.
		# INPUT: object, value
		# OUTPUT: NONE	
		procedure_AD1257_ui.prsnt_upgrade_tree_switch,

		#script_prsnt_upgrade_tree_ready
		# WARNING: some part of this script are disabled.
		# INPUT: NONE
		# OUTPUT: NONE	
		procedure_AD1257_ui.prsnt_upgrade_tree_ready,
		
		#script_prsnt_upgrade_tree_troop_and_name
		# INPUT: NONE
		# OUTPUT: NONE	
		procedure_AD1257_ui.prsnt_upgrade_tree_troop_and_name,
		
		#script_prsnt_upgrade_tree_troop_cost
		# INPUT: NONE
		# OUTPUT: NONE
		procedure_AD1257_ui.prsnt_upgrade_tree_troop_cost,
		
		#script_raf_religion_to_s11
		# INPUT: faction
		# OUTPUT: s11 religion string
		function_AD1257.raf_religion_to_s11,

	# #Formations Scripts	  
	# script_division_reset_places by motomataru
	# Input: none
	# Output: none
	# Resets globals for placing divisions around player for script_battlegroup_place_around_leader
	procedure_mod_formation.division_reset_places,
	 
	# script_battlegroup_place_around_leader by motomataru
	# WARNING: some part of this script are disabled.
	# Input: team, division
	# Output: pos61 division position
	function_mod_formation.battlegroup_place_around_leader,
	
	# script_form_cavalry by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing
	# Output: none
	# Form in wedge, (now not) excluding horse archers
	# Creates formation starting at pos1
	procedure_mod_formation.form_cavalry,
		 
	# script_form_archers by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing, formation
	# Output: none
	# Form in line, staggered if formation = formation_ranks
	# Creates formation starting at pos1
	procedure_mod_formation.form_archers,
		 
	# script_form_infantry by motomataru
	# Input: (pos1), team, division, agent number of team leader, spacing, formation
	# Output: none
	# If input "formation" is formation_default, will select a formation based on faction
	# Creates formation starting at pos1
	procedure_mod_formation.form_infantry,
		 
	# script_get_default_formation by motomataru
	# WARNING: some part of this script are disabled.
	# Input: team id
	# Output: reg0 default formation
	function_mod_formation.get_default_formation,

	# script_equip_best_melee_weapon by motomataru
	# WARNING: THIS MIGHT ALSO SOURCE OF GLITCHY SIEGE AI!
	# Input: agent id, flag to force shield, flag to force for length ALONE
	# Output: none
	procedure_mod_formation.equip_best_melee_weapon,

	# script_formation_current_position by motomataru
	# Input: destination position (not pos0), team, division
	# Output: in destination position
	function_mod_formation.formation_current_position,

	# script_get_centering_amount by motomataru
	# Input: formation type, number of troops, extra spacing
	#        Use formation type formation_default to use script for archer line
	# Output: reg0 number of centimeters to adjust x-position to center formation
	function_mod_formation.get_centering_amount,

	# script_formation_end
	# Input: team, division
	# Output: none
	procedure_mod_formation.formation_end,

	# script_formation_move_position by motomataru
	# Input: team, division, formation current position, (1 to advance or -1 to withdraw or 0 to redirect)
	# Output: pos1 (offset for centering)
	function_mod_formation.formation_move_position,

	# script_set_formation_position by motomataru
	# Input: team, troop class, position
	# Output: none
	# Kluge around buggy *_order_position functions for teams 0-3
	procedure_mod_formation.set_formation_position,	

	# script_get_formation_position by motomataru
	# Input: position, team, troop class
	# Output: input position (pos0 used)
	# Kluge around buggy *_order_position functions for teams 0-3
	function_mod_formation.get_formation_position,	

	# script_cf_battlegroup_valid_formation by Caba'drin
	# Input: team, division, formation
	# Output: reg0: troop count/1 if too few troops/0 if wrong type
	cfunction_mod_formation.cf_battlegroup_valid_formation,

	# script_cf_valid_formation_member by motomataru #CABA - Modified for Classify_agent phase out
	# Input: team, division, agent number of team leader, test agent
	# Output: failure indicates agent is not member of formation
	cfunction_mod_formation.cf_valid_formation_member,

# #Player team formations functions
	# script_player_attempt_formation
	# Inputs:	arg1: division
	#			arg2: formation identifier (formation_*)
	# Output: none
	procedure_mod_formation.player_attempt_formation,

	# script_str_store_division_type_name by motomataru
	# Input:	destination, division type (sdt_*)
	# Output: none
	procedure_mod_formation.str_store_division_type_name,
	
	# script_player_order_formations by motomataru
	# Inputs:	arg1: order to formation (mordr_*)
	# Output: none
	procedure_mod_formation.player_order_formations,

	
# #Utilities used by formations
	# script_point_y_toward_position by motomataru
	# Input: from position, to position
	# Output: reg0 fixed point distance
	function_mod_formation_util.point_y_toward_position,

	# script_store_battlegroup_type by Caba'drin   ##NEEDS EDIT per PMs with moto
	# Input: team, division
	# Output: reg0 and slot_team_dx_type with sdt_* value
	# Automatically called from store_battlegroup_data
	function_mod_formation_util.store_battlegroup_type,

	# script_store_battlegroup_data by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
	# Input: none
	# Output: sets positions and globals to track data on ALL groups in a battle
	# Globals used: pos1, reg0, reg1, #CABA - NO LONGER USED: positions 24-45
	procedure_mod_formation_util.store_battlegroup_data,

	# script_team_get_position_of_enemies by motomataru
	# Input: destination position, team, troop class/division
	# Output: destination position: average position if reg0 > 0
	#			reg0: number of enemies
	# WARNING: Run script_store_battlegroup_data before calling!
	function_mod_formation_util.team_get_position_of_enemies,

# # M&B Standard AI with changes for formations #CABA - OK; Need expansion when new AI divisions to work with
	# script_formation_battle_tactic_init_aux
	# Input: team_no, battle_tactic
	# Output: none
	procedure_mod_formation_ai.formation_battle_tactic_init_aux,
	
	# script_formation_battle_tactic_apply_aux #CABA - OK; Need expansion when new AI divisions to work with
	# Input: team_no, battle_tactic
	# Output: battle_tactic
	function_mod_formation_ai.formation_battle_tactic_apply_aux,
	
	# Replacement script for battle_tactic_init_aux to switch between using
	# M&B Standard AI with changes for formations and original based on
	# NOTE: original script "battle_tactic_init_aux" should be renamed to "orig_battle_tactic_init_aux"
	# constant formation_native_ai_use_formation ( 0: original, 1: use formation )
	# script_battle_tactic_init_aux
	# Input: team_no, battle_tactic
	# Output: none
	procedure_mod_formation_ai.battle_tactic_init_aux,

	# Replacement script for battle_tactic_init_aux to switch between using
	# M&B Standard AI with changes for formations and original based on
	# NOTE: original script "battle_tactic_apply_aux" should be renamed to "orig_battle_tactic_apply_aux"
	# constant formation_native_ai_use_formation ( 0: original, 1: use formation )
	# script_battle_tactic_apply_aux
	# Input: team_no, battle_tactic
	# Output: battle_tactic
	function_mod_formation_ai.battle_tactic_apply_aux,
	
# # AI with Formations Scripts
	# script_calculate_decision_numbers by motomataru
	# Input: AI team, size relative to battle in %
	# Output: reg0 - battle presence plus level bump, reg1 - level bump (team avg level / 3)
	function_mod_formation_ai.calculate_decision_numbers,
	

	# script_team_field_ranged_tactics by motomataru
	# Input: AI team, size relative to largest team in %, size relative to battle in %
	# Output: none
	procedure_mod_formation_ai.team_field_ranged_tactics,
															
	# script_team_field_melee_tactics by motomataru #EDITED FOR SLOTS BY CABA...many divisions changes necessary
	# Input: AI team, size relative to largest team in %, size relative to battle in %
	# Output: none
	procedure_mod_formation_ai.team_field_melee_tactics,
					
								
	# script_field_tactics by motomataru
	# WARNING: modified by 1257AD devs
	# Input: flag 1 to include ranged
	# Output: none
	procedure_mod_formation_ai.field_tactics,
		
	# script_find_high_ground_around_pos1_corrected by motomataru
	# Input:	arg1: destination position
	#			arg2: search_radius (in meters)
	#			pos1 should hold center_position_no
	# Output:	destination contains highest ground within a <search_radius> meter square around pos1
	# Also uses position registers: pos0
	function_mod_formation_ai.find_high_ground_around_pos1_corrected,
			
	# script_cf_count_casualties by motomataru
	# Input: none
	# Output: evalates T/F, reg0 num casualties
	cfunction_mod_formation.cf_count_casualties,
	
		
	# script_battlegroup_get_position by motomataru #CABA - EDITED TO USE SLOTS, NOT STORED POS NUMBERS
#MOTO need rotation?
	# Input: destination position, team, battle group (troop class)
	# Output:	battle group position
	#			average team position if "troop class" input NOT set to 0-8
	# NB: Assumes that battle groups beyond 2 are PLAYER team
	# Positions 24-45 reserved (!)  NOW none are reserved...all calculated with slots
	function_mod_formation.battlegroup_get_position,	
		
	# script_get_nearest_enemy_battlegroup_location by motomataru
	# Input: destination position, fron team, from position
	# Output:	destination position, reg0 with distance
	# Run script_store_battlegroup_data before calling!
	function_mod_formation_util.get_nearest_enemy_battlegroup_location,
		
# # Line added to clear scripted mode right before each (agent_start_running_away, ":cur_agent")
	# script_decide_run_away_or_not
	# Input: none
	# Output: none
	procedure_ai.decide_run_away_or_not, 
		
		#script_tom_process_player_enterprise
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: enterprise_product, enterprise_center, future_cost
		#OUTPUT: none
		procedure_AD1257_economy.tom_process_player_enterprise,
		
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
		
		# script_raf_process_alarms
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
		#called from triggers
		procedure_AD1257_campaign.raf_process_alarm,
		
		#script_game_get_troop_wage
		# WARNING : HEAVILY Modified by 1257AD devs
		# INPUT: troop_id, party_id
		# OUTPUT: wage set trigger register reg0
		function_game.game_get_troop_wage,
		
		# script_get_closest_enemy_distance - tom
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: agent to find from
		# Output: reg1: distance in cms, reg4 glosest agent
		function_AD1257_battle_ai.get_closest_enemy_distance,
		
		# script_get_first_closest_enemy_distance - tom
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: agent to find from
		# Output: reg1: distance in cms, reg4 glosest agent
		function_AD1257_battle_ai.get_first_closest_enemy_distance,
		
		# script_get_closest_enemy_distance_new - tom
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: agent to find from, team, minimum distance in cms to find
		# Output: reg1: distance in cms, reg4 glosest agent
		function_AD1257_battle_ai.get_closest_enemy_distance_new,
		
		##script_tom_agent_skirmish
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		##description: sets the agent to skirmish
		###input: agent, closest_agent id, nearest_enemy, radius, skrimish_start, skrimish_angle
		###output: none
		procedure_AD1257_battle_ai.tom_agent_skirmish,
		
		#script_raf_set_troop_classes
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: none
		#OUTPUT: none
		procedure_AD1257_battle.raf_set_troop_classes,

		#script_party_calculate_regular_strength:
		# INPUT:
		# param1: Party-id
		# OUTPUT: stack_strength
		function_party.party_calculate_regular_strength,
		
		#script_party_calculate_strength:
		# INPUT: arg1 = party_id, arg2 = exclude leader
		# OUTPUT: reg0 = strength
		function_party.party_calculate_strength,
		
		#script_change_rain_or_snow
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: none
		# OUTPUT: none
		procedure_AD1257_weather.change_rain_or_snow,
		
		#script_vector_length
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: position vector
		#OUTPUT: length
		function_AD1257_utils.vector_length,
		
		#script_maintain_broken_items
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: none
		#OUTPUT: none
		procedure_AD1257_item.maintain_broken_items,
		
		#script_first_formation_member_sound_horn
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#tom-script
		#input: team, group, formation_type
		#output: none
		#first formation member sounds the horn. Used mainly for player armies(ai use them diffrently)
		procedure_AD1257_additional_formation.first_formation_member_sound_horn,

		#script_set_flag_carriers
		#tom-script
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#input: nothing
		#output: nothing
		procedure_AD1257_additional_formation.set_flag_carriers,
		
	##TOM freelancer addon
	## script_freelancer_get_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# freelancer script here!
	##input: troop, faction
	##output: reg1 - troop
	function_AD1257_freelancer.freelancer_get_troop,	  
	
	###script_pass_all_posetions_from_lord_to_lord
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	###input: lord_from, lord_to
	###output: none
	##gives all the posetion(except items) to the order lord. Items are remvoed and bread is added
	procedure_AD1257_freelancer.pass_all_posetions_from_lord_to_lord,
	
	###script_desert_order
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: checks if player is in an crusader order and if so does the penalty for deserting
	#input: none
	#output: none
	procedure_AD1257_freelancer.desert_order,
	#tom freelancer addon

	#script_freelancer_attach_party
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none	
	#+freelancer start
	 procedure_AD1257_freelancer.freelancer_attach_party,

	 #script_freelancer_detach_party
	 # WARNING: this is totally new procedure (not present in native). 1257AD devs
	 # INPUT: none
	 # OUTPUT: none	
	 procedure_AD1257_freelancer.freelancer_detach_party,

	# script_event_player_enlists
	# ADDS THE PLAYER TO THE LORD'S PARTY  
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: tier
	# OUTPUT: none
		procedure_AD1257_freelancer.event_player_enlists,


    #script_event_player_discharge
	#  RUNS IF THE PLAYER LEAVES THE ARMY
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	 procedure_AD1257_freelancer.event_player_discharge,
	
		#script_event_player_vacation
		#  RUNS IF THE PLAYER GOES ON VACATION
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: none
		# OUTPUT: none
	procedure_AD1257_freelancer.event_player_vacation,

	#script_event_player_returns_vacation
	# RUNS WHEN PLAYER RETURNS FROM VACATION
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_freelancer.event_player_returns_vacation,
	
	#script_event_player_deserts
	# RUNS IF PLAYER DESERTS OR IS AWOL
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_freelancer.event_player_deserts,	
	
		
		#script_party_restore
		# RETURNS PART OF THE ORIGINAL PARTY
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: none
		# OUTPUT: none
		procedure_AD1257_freelancer.party_restore,

	#script_get_desert_troops
	#  CALCULATES NUMBER OF DESERTING TROOPS
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	 procedure_AD1257_freelancer.get_desert_troops,

	#script_freelancer_keep_field_loot
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_freelancer.freelancer_keep_field_loot,
	
	#script_cf_freelancer_player_can_upgrade
	 #Reg0 outputs reason for failure
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: source_troop
	# OUTPUT: none
	cfunction_AD1257_freelancer.cf_freelancer_player_can_upgrade,
	 
	 #script_freelancer_equip_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs 
	# INPUT: source_troop
	# OUTPUT: none
	procedure_AD1257_freelancer.freelancer_equip_troop,
	
	#script_freelancer_unequip_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs 
	# INPUT: source_troop
	# OUTPUT: none
	procedure_AD1257_freelancer.freelancer_unequip_troop, 
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
# WARNING: this is totally new procedure (not present in native). 1257AD devs
# INPUT: none
# OUTPUT: none
	procedure_AD1257_economy.refresh_center_inventories, 
		
	# script_refresh_center_armories
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_economy.refresh_center_armories,

	# script_refresh_center_weaponsmiths
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_economy.refresh_center_weaponsmiths,

	# script_refresh_center_stables
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_economy.refresh_center_stables,
	
	#script_tom_command_cheer
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_misc.tom_command_cheer,
	
	#script_update_manor_infested_by_bandits
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: none
	#output: none
	#description: updates the manors with possible crysis. Called from triggers
	#0 - none
	#1 - regular bandits
	#2 - mercenery band rampaging
	#3 - two nobles conflicting
	#4 - angry peasents are angry for some reason
	#5 - 
	procedure_AD1257_manor_system.update_manor_infested_by_bandits,
	 
	 #script_get_mercenary_troop_for_manor - tom made
	 # WARNING: this is totally new procedure (not present in native). 1257AD devs
	 #input: faction of the manor
	 #output: reg0 - troop id
	 #called to determine the faction mercenary troop, to raid the center. Does not include the special troops, such as the varangian guard
	function_AD1257_manor_system.get_mercenary_troop_for_manor,
	 
	 
		# script_init_manor_agents #init_town_walkers as template
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: manor_id
		# Output: none
	procedure_AD1257_manor_scene.init_manor_agents,
	
	# script_manor_refresh_inventories
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: manor_id
		# Output: none
	procedure_AD1257_manor_economy.manor_refresh_inventories,
	
	# script_init_town_walker_agents
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
	procedure_AD1257_manor_scene.init_manor_walker_agents,
	
	# script_tick_manor_walkers
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
	procedure_AD1257_manor_scene.tick_manor_walkers,
	
	#script_select_mercenary_troop - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT: arg1 = center_no
		# OUTPUT: reg1 = troop_no
	function_AD1257_mercenary.select_mercenary_troop ,

	##script_cf_recruit_individual_merc - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: recruits several troops of the center the lord is in
	#input: party_no to recruit to
	#output: none
	#TODO: crusaders, mercs
	cfunction_AD1257_mercenary.cf_recruit_individual_merc,
	
	##script_cf_recruit_merc_lance_for_npc - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: selects a owned center of the lord and then recruits lance
	#input: party_no to recruit to.
	#output: none
	#TODO: crusaders, mercs
	cfunction_AD1257_mercenary.cf_recruit_merc_lance_for_npc,
	
	##script_cf_recruit_lance_for_npc - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: selects a owned center of the lord and then recruits lance
	#input: party_no to recruit to.
	#output: none
	#TODO: crusaders, mercs
	cfunction_AD1257_mercenary.cf_recruit_lance_for_npc,
	
	#script_get_random_merc_company_from_center
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: center
	#output: reg0 random merc company
	#decription: gets a random mect company from the specified center. Does not consume merc resources. Used for kingdom parties
	function_AD1257_mercenary.get_random_merc_company_from_center,
	
	
	#script_get_orig_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: auxilary script to get the culture to recruit troops
	#input: original faction, cur faction, original culture
	#output reg0 - culture to use for troops
	function_AD1257_regions.get_orig_culture,
	
	#script_check_agents_for_lances
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: checks all the agents on the battlefield and removes the dead ones from the arrays.
	#input: none
	#output: none
	procedure_AD1257_lance_system.check_agents_for_lances,
	
	#script_balance_lance_storage
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: removes the dead troops in the lance storage. Both in reserve and the combatans
	#input: none
	#output:none
	procedure_AD1257_lance_system.balance_lance_storage,
	
	
	##script_count_nobles_commoners_for_center
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: count nobles and commoners for each center. Increase lances if there are troop uncounted
	##input: none
	##output: none
	procedure_AD1257_lance_system.count_nobles_commoners_for_center,
	
	#script_get_noble_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: center to earch for
	#output: reg1- the troop, -1 if not found
	function_AD1257_lance_system.get_noble_troop,
	
	#script_get_commoner_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: center to earch for
	#output: reg1- the troop, -1 if not found
	function_AD1257_lance_system.get_commoner_troop,
	
	
	#script_add_lance_troop_to_regulars
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: adds the current troop to regulars(serving in players party), increases the counter
	#input: troop, center recruited from
	#output: none
	procedure_AD1257_lance_system.add_lance_troop_to_regulars,
	
	#script_search_for_troop
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: searches for such a troop in service and returns the it's index in the array
	#input: troop
	#output: reg0- troop index at the array
	function_AD1257_lance_system.search_for_troop,
	
	#script_clear_troop_array
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: clears the troop array
	#input: troop, begin_index, end_index
	#output: none
	procedure_AD1257_utils.clear_troop_array,
	
	#script_fill_lance
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: select the troop for recruitment
	#input: spawn_center, party_to_fill
	#output: spawned party_id
	function_AD1257_lance_system.fill_lance,
	
	##script_choose_random_troop_for_lance - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: gets a random troop for the lance. Either one of the two upgrade troops, 
	##the only one if one is available, or just returns the orignal troop if non upgradable
	##input: original_troop to upgrade from, which tier to return
	##output: returns via reg0
	function_AD1257_lance_system.choose_random_troop_for_lance,
	
	##script_feudal_lance_manpower_update - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: party_id(village/town/castle)
	##output: none
	##description: updates the feudal recruits for the lance system in villages. max lances per village - 10.
	procedure_AD1257_lance_system.feudal_lance_manpower_update,

	###script_fill_company - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	###input: center, party, merc_type
	###output: none
	###description: company size - 30 men; 1 seargant, ~10 crossbow
	procedure_AD1257_lance_system.fill_company,
	
	## script_get_lance_size
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	## description: returns the size of the lance
		## Input: item_no, agent_no
		## Output: reg0 - tottal size, reg1 - noble size, reg2 - commoner size 
	function_AD1257_lance_system.get_lance_size,
	
	## script_get_lance_precentage
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	## description: returns the precentage for lance troop tier chance
		## Input: item_no, agent_no
		## Output: reg1 - tier1, reg2 - tier2, reg3 - tier3, reg4 - tier4, reg5 - tier5 
	function_AD1257_lance_system.get_lance_precentage,
	
	##script_check_if_faction_is_at_war - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: faction_id
	##output: reg0 - sets 1 if at war, 0 if not
	##description: Check if at war with any other major faction. 
	function_AD1257.check_if_faction_is_at_war,
	
	##script_set_sea_icons - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: none
	##output: none
	##description: Option trigger - moving party icons to default
	procedure_AD1257_campaign.set_sea_icons,
	
	##script_get_party_campsite - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: party
	##output: reg0 - campsite scene
	##description: Sets the scene based on the current party terrain
	function_AD1257_campsite.get_party_campsite,
	
	##script_cf_hire_npc_specialist - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: companion, companion_culture
	##output: none
	##description: Hires the specialist for the players party
	cfunction_AD1257_companion.cf_hire_npc_specialist,
	
	
	##script_equip_companion - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##Input: companion, troop
	##output: none
	##description: Sets the equipment of the hero character to the specified troop
	procedure_AD1257_companion.equip_companion,
	
	##script_set_troop_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: sets the culture for the regular troops.
	##Input: none
	##output: none
	procedure_AD1257_troop.set_troop_culture,
	
	##script_troop_find_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description
	##input: troop to search for, culture
	##output: reg0 returns -1 if the troop does not belong to the culture, 0 if belongs(village), 1(town), 2(noble)
	function_AD1257_troop.troop_find_culture,
	
	##script_troop_tree_search
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description
	## recursively search a troop.
	##input: target target_troop - the troop to search for, troop - current troop in the tree path
	##output: reg10 returns the assigned troop if found. IF not reg10 is unchanged.
	function_AD1257_troop.troop_tree_search,
	
	
	###tom - tournament scripts
	##script_init_tournament_participents
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: set up tournament participents in trp_tournament_participants
	##input: center_no
	##output: none
	procedure_AD1257_tournament.init_tournament_participents,	
	
	# script_end_tournament_fight_new
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: arg1 = player_team_won (1 or 0)
		# Output: none
	procedure_AD1257_tournament.end_tournament_fight_new,	
	
	# script_simulate_next_battle
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: arg1 = player opponent
		# Output: none
	procedure_AD1257_tournament.simulate_next_battle,	
	
	# script_simulate_next_battle_auxiliary
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: oponnent1 slot , opponent2 slot, reduce by 1 slot values(1-no, 0-yes)
		# Output: none
	procedure_AD1257_tournament.simulate_next_battle_auxiliary,	
	
	## script_get_and_remove_member
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: party_to_do_so
		## Output: reg1 - troop
	function_AD1257_party.get_and_remove_member,	
	
	## script_set_matching_sexy_boots
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: item_no, agent_no
		## Output: none
	procedure_AD1257_agent_looks.set_matching_sexy_boots,
	
	## script_set_prsnt_debug
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# NOTE: basically just draws grid lines in presentation window
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_debug.set_prsnt_debug,
	
	
	## script_economy_get_buildings
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		## Input: none
		## Output: s1..s27
	function_AD1257_economy.economy_get_buildings,		
	
	
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
	
	#script_script_check_pope_crown
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	("script_check_pope_crown",
	[
		#modde2x... hmm maybe we should implement this
	]),
	
	##script_add_item_to_pool
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: item, pool
	# OUTPUT: none
	procedure_AD1257_pool.add_item_to_pool,
	
	
	##script_cf_add_item_to_pool
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# DEPRECATED, not in use anymore.
	# INPUT: item, pool
	# OUTPUT: none
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
	]),
	
	
	##script_extract_armor_from_tree
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# input: troop, pool
	# output: none
	procedure_AD1257_pool.extract_armor_from_tree,
	
	##script_fill_pools_by_culture
	##description: initialize culture pools
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: culture, pool_commoner, pool_noble
	# OUTPUT: none
	procedure_AD1257_pool.fill_pools_by_culture,	
	
	##script_initialize_culture_pools
	##description: initialize culture pools
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_pool.initialize_culture_pools,	
	
	
	##script_cf_add_troop_items_armor
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: troop, pool, armor_from, armor_to
	# OUTPUT: nothing (can fail)
	cfunction_AD1257_pool.cf_add_troop_items_armor,
	
	##script_cf_add_troop_items_helmet
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: troop, pool, armor_from, armor_to
	# OUTPUT: nothing (can fail)
	cfunction_AD1257_pool.cf_add_troop_items_helmet,	
	
	##script_equip_troops_by_tier
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: troop, pool, tier
	# OUTPUT: none
	procedure_AD1257_pool.equip_troops_by_tier,
	
	##script_rebalance_troop_trees
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: rebalancing system. modded2x: need 2 disable this, /mbg/ folks arent' happy
	# INPUT: troop, pool, tier
	# OUTPUT: none
	procedure_AD1257_pool.rebalance_troop_trees,
	
	##script_rebalance_troops_by_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: description: rebalancing system. modded2x: need 2 disable this, /mbg/ folks arent' happy
	# INPUT: none
	# OUTPUT: none
	procedure_AD1257_pool.rebalance_troops_by_culture,

	#script_modded2x_print_fizzbuzz
	# DESCRIPTION: just a test lol
	#INPUT: input_size
	#OUTPUT: none
	procedure_modded2x.modded2x_print_fizzbuzz,

	#script_modded2x_Int2Bin
	#INPUT: a number
	#OUTPUT: s1, binary string
	function_modded2x.modded2x_Int2Bin
	]
