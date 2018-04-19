from header import *


		# script_calculate_battle_advantage
		# Output: reg0 = battle advantage
calculate_battle_advantage = (
	"calculate_battle_advantage",
			[
				(call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
				(assign, ":friend_count", reg(0)),
				
				(party_get_skill_level, ":player_party_tactics",  "p_main_party", skl_tactics),
				(party_get_skill_level, ":ally_party_tactics",  "p_collective_friends", skl_tactics),
				(val_max, ":player_party_tactics", ":ally_party_tactics"),
				
				(call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
				(assign, ":enemy_count", reg(0)),
				
				(party_get_skill_level, ":enemy_party_tactics",  "p_collective_enemy", skl_tactics),
				
				(val_add, ":friend_count", 1),
				(val_add, ":enemy_count", 1),
				
				(try_begin),
					(ge, ":friend_count", ":enemy_count"),
					(val_mul, ":friend_count", 100),
					(store_div, ":ratio", ":friend_count", ":enemy_count"),
					(store_sub, ":raw_advantage", ":ratio", 100),
				(else_try),
					(val_mul, ":enemy_count", 100),
					(store_div, ":ratio", ":enemy_count", ":friend_count"),
					(store_sub, ":raw_advantage", 100, ":ratio"),
				(try_end),
				(val_mul, ":raw_advantage", 2),
				
				(val_mul, ":player_party_tactics", 30),
				(val_mul, ":enemy_party_tactics", 30),
				(val_add, ":raw_advantage", ":player_party_tactics"),
				(val_sub, ":raw_advantage", ":enemy_party_tactics"),
				(val_div, ":raw_advantage", 100),
				
				
				(assign, reg0, ":raw_advantage"),
				(display_message, "@Battle Advantage = {reg0}.", 0xFFFFFFFF),
		])
		