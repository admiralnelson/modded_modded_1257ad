from header import *

	###tom - tournament scripts
	##script_init_tournament_participents
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: set up tournament participents in trp_tournament_participants
	##input: center_no
	##output: none
init_tournament_participents = (
	"init_tournament_participents",
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
	])	
	
	# script_end_tournament_fight_new
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: arg1 = player_team_won (1 or 0)
		# Output: none
end_tournament_fight_new = (
	"end_tournament_fight_new",
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
	])	
	
	# script_simulate_next_battle
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: arg1 = player opponent
		# Output: none
simulate_next_battle = (
	"simulate_next_battle",
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
	])	
	
	# script_simulate_next_battle_auxiliary
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: oponnent1 slot , opponent2 slot, reduce by 1 slot values(1-no, 0-yes)
		# Output: none
simulate_next_battle_auxiliary = (
	"simulate_next_battle_auxiliary",
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
	])	