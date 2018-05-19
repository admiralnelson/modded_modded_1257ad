from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

## CC
from header_skills import *
from header_items import *
from module_items import *
#from module_my_mod_set import *
## CC

from user_interface.AD1257 import *
from user_interface.AD1257_settings import *
from user_interface.arena import *
from user_interface.battle import *
from user_interface.campaign import *
from user_interface.credits import *
from user_interface.custom_banner import *
from user_interface.custom_battle import *
from user_interface.economy import *
from user_interface.main_menu import *
from user_interface.Mod_autoloot import *
from user_interface.Mod_formation import *
from user_interface.Mod_freelancer import *
from user_interface.multiplayer import *
from user_interface.multiplayer_admin_panel import *
from user_interface.multiplayer_welcome import *
from user_interface.profile import *
from user_interface.quit import *
from user_interface.slider import *
from user_interface.tutorial import *
from user_interface.Modded2x import *
####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
	game_start,
	game_credits,
	game_profile_banner_selection,
	game_custom_battle_designer,
	game_multiplayer_admin_panel,
	#multiplayer crap :&)
	multiplayer_welcome_message, 
	multiplayer_team_select,
	multiplayer_troop_select,
	multiplayer_item_select,
	multiplayer_message_1,
	multiplayer_message_2,
	multiplayer_message_3,
	multiplayer_round_time_counter,
	multiplayer_team_score_display,
	multiplayer_flag_projection_display,
	multiplayer_flag_projection_display_bt,
	multiplayer_destructible_targets_display,
	multiplayer_respawn_time_counter,
	multiplayer_stats_chart,
	#this score table is used in only deathmatch
	multiplayer_stats_chart_deathmatch,
	multiplayer_escape_menu,
	multiplayer_poll_menu,
	multiplayer_show_players_list,
	multiplayer_show_maps_list,
	multiplayer_show_factions_list,
	multiplayer_show_number_of_bots_list,
	multiplayer_poll,
	#multiplayer crap :&)
	tutorial_show_mouse_movement,
	name_kingdom,
	banner_selection,
	#Modded2x: custom banner uis, Currently disabled. hmm, interesting...
	custom_banner,
	banner_charge_positioning,
	banner_charge_selection,
	banner_background_selection,
	banner_flag_type_selection,
	banner_flag_map_type_selection,
	color_selection,
	marshall_selection,
	#WARNING: modified by 1257AD devs
	battle,
	sliders,
	arena_training,
	#Modded2x: retirement window, might be interesting.
	retirement,
	#WARNING: modified by 1257AD devs
	budget_report,
	game_before_quit, 
	multiplayer_duel_start_counter,
	#WARNING: modified by 1257AD devs
	faction_selection,
	#WARNING: does not exist in native, made by  1257AD devs
	autoloot_upgrade_management,
	#WARNING: does not exist in native, made by  1257AD devs
	auto_sell_options,
	#WARNING: does not exist in native, made by  1257AD devs
	change_all_factions_color,
	#WARNING: does not exist in native, made by  1257AD devs
	troop_note,
	#WARNING: does not exist in native, made by  1257AD devs
	recruit_npc,
	#WARNING: does not exist in native, made by  1257AD devs
	mod_options,
	#WARNING: does not exist in native, made by  1257AD devs
	economy_build,
	#WARNING: does not exist in native, made by  1257AD devs
	taragoth_lords_report,
	#WARNING: does not exist in native, made by  1257AD devs	
	#NOte: additional formation options in battle
	order_display,
	character_creation1, 
	#Modded2x
	fizzbuzz
	
]
