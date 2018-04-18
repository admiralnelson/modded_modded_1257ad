from header import *

#script_start_wedding_cutscene
# INPUT: arg1 = groom_troop, arg2 = bride_troop
# OUTPUT: none
start_wedding_cutscene=	("start_wedding_cutscene",
		[
			(store_script_param, "$g_wedding_groom_troop", 1),
			(store_script_param, "$g_wedding_bride_troop", 2),
			
			(assign, "$g_wedding_bishop_troop", "trp_temporary_minister"),
			(try_begin),
				(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
				(neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_wedding_groom_troop"),
				(neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_wedding_bride_troop"),
				(faction_get_slot, ":players_king", "$players_kingdom", slot_faction_leader),
				(troop_get_type, ":troop_type", ":players_king"),
				(eq, ":troop_type", 0), #male
				(neq, ":players_king", "$g_wedding_groom_troop"),
				(assign, "$g_wedding_bishop_troop", ":players_king"),
			(else_try),
				(eq, "$players_kingdom", "fac_player_supporters_faction"),
				(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
				(gt, "$g_player_minister", 0),
				(troop_get_type, ":troop_type", "$g_player_minister"),
				(eq, ":troop_type", 0), #male
				(neq, "$g_player_minister", "$g_wedding_groom_troop"),
				(assign, "$g_wedding_bishop_troop", "$g_player_minister"),
			(try_end),
			
			(assign, "$g_wedding_brides_dad_troop", "trp_temporary_minister"),
			(try_begin),
				(neq, "$g_wedding_bride_troop", "trp_player"),
				(try_begin),
					(troop_get_slot, ":father", "$g_wedding_bride_troop", slot_troop_father),
					(gt, ":father", 0),
					(troop_get_type, ":troop_type", ":father"), #just to make sure
					(eq, ":troop_type", 0), #male
					(neq, ":father", "$g_wedding_groom_troop"), #this might be 0 due to an error
					(neq, ":father", "$g_wedding_bishop_troop"),
					(assign, "$g_wedding_brides_dad_troop", ":father"),
				(else_try),
					(troop_get_slot, ":guardian", "$g_wedding_bride_troop", slot_troop_guardian),
					(gt, ":guardian", 0),
					(troop_get_type, ":troop_type", ":guardian"), #just to make sure
					(eq, ":troop_type", 0), #male
					(neq, ":guardian", "$g_wedding_groom_troop"), #this might be 0 due to an error
					(neq, ":guardian", "$g_wedding_bishop_troop"),
					(assign, "$g_wedding_brides_dad_troop", ":guardian"),
				(try_end),
			(else_try),
				(try_for_range, ":cur_companion", companions_begin, companions_end),
					(this_or_next|troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_player_companion),
					(troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_kingdom_hero),
					(troop_get_type, ":troop_type", ":cur_companion"), #just to make sure
					(eq, ":troop_type", 0), #male
					(neq, ":cur_companion", "$g_wedding_groom_troop"),
					(neq, ":cur_companion", "$g_wedding_bishop_troop"),
					(assign, "$g_wedding_brides_dad_troop", ":cur_companion"),
				(try_end),
			(try_end),
			
			(modify_visitors_at_site,"scn_wedding"),
			(reset_visitors,0),
			(set_visitor, 0, "$g_wedding_groom_troop"),
			(set_visitor, 1, "$g_wedding_bride_troop"),
			(set_visitor, 2, "$g_wedding_brides_dad_troop"),
			(set_visitor, 3, "$g_wedding_bishop_troop"),
			(assign, ":num_visitors", 4),
			(assign, ":num_male_visitors", 0),
			(try_for_range, ":cur_npc", active_npcs_begin, kingdom_ladies_end),
				(lt, ":num_visitors", 32),
				(neq, ":cur_npc", "$g_wedding_groom_troop"),
				(neq, ":cur_npc", "$g_wedding_bride_troop"),
				(neq, ":cur_npc", "$g_wedding_brides_dad_troop"),
				(neq, ":cur_npc", "$g_wedding_bishop_troop"),
				(store_troop_faction, ":npc_faction", ":cur_npc"),
				(is_between, ":npc_faction", kingdoms_begin, kingdoms_end),
				(eq, ":npc_faction", "$players_kingdom"),
				(this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_player_companion),
				(this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_hero),
				(troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_lady),
				(troop_get_type, ":troop_type", ":cur_npc"),
				(assign, ":continue_adding", 1),
				(try_begin),
					(eq, ":troop_type", 0),
					(assign, ":continue_adding", 0),
					(lt, ":num_male_visitors", 16), #limit number of male visitors
					(assign, ":continue_adding", 1),
					(val_add, ":num_male_visitors", 1),
				(try_end),
				(eq, ":continue_adding", 1),
				(set_visitor, ":num_visitors", ":cur_npc"),
				(val_add, ":num_visitors", 1),
			(try_end),
			(set_jump_mission,"mt_wedding"),
			(jump_to_scene,"scn_wedding"),
			(change_screen_mission),
	])