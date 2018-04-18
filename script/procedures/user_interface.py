from header import *


		#script_game_context_menu_get_buttons:
		# This script is called from the game engine when the player clicks the right mouse button over a party on the map.
		# INPUT: arg1 = party_no
		# OUTPUT: none, fills the menu buttons
game_context_menu_get_buttons =	(
	"game_context_menu_get_buttons",
			[
				(store_script_param, ":party_no", 1),
				(try_begin),
					(neq, ":party_no", "p_main_party"),
					(context_menu_add_item, "@Move here", cmenu_move),
				(try_end),
				
				(try_begin),
					(is_between, ":party_no", centers_begin, centers_end),
					(context_menu_add_item, "@View notes", 1),
				(else_try),
					(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
					(gt, ":num_stacks", 0),
					(party_stack_get_troop_id, ":troop_no", ":party_no", 0),
					(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
					(context_menu_add_item, "@View notes", 2),
				(try_end),
				
				(try_begin),
					(neq, ":party_no", "p_main_party"),
					(store_faction_of_party, ":party_faction", ":party_no"),
					
					(store_relation, ":rel", ":party_faction", "fac_player_supporters_faction"),
					(this_or_next | ge, ":rel", 0),
					# rafi - accompany whoever I wish (this_or_next|eq, ":party_faction", "$players_kingdom"),
					# rafi - accompany whoever I wish (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
					(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
					
					(neg|is_between, ":party_no", centers_begin, centers_end),
					
					(context_menu_add_item, "@Accompany", cmenu_follow),
				(try_end),
		])
		
		#script_game_event_context_menu_button_clicked:
		# This script is called from the game engine when the player clicks on a button at the right mouse menu.
		# INPUT: arg1 = party_no, arg2 = button_value
		# OUTPUT: none
game_event_context_menu_button_clicked = (
	"game_event_context_menu_button_clicked",
			[(store_script_param, ":party_no", 1),
				(store_script_param, ":button_value", 2),
				(try_begin),
					(eq, ":button_value", 1),
					(change_screen_notes, 3, ":party_no"),
				(else_try),
					(eq, ":button_value", 2),
					(party_stack_get_troop_id, ":troop_no", ":party_no", 0),
					(change_screen_notes, 1, ":troop_no"),
				(try_end),
		])