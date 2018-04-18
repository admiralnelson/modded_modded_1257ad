from header import *

#script_spawn_quick_battle_army
	# Usage on Quick battle window setup
	# INPUT: arg1 = initial_entry_point, arg2 = faction_no, arg3 = infantry_ratio, arg4 = archers_ratio, arg5 = cavalry_ratio, arg6 = divide_archer_entry_points, arg7 = player_team
	# OUTPUT: none
spawn_quick_battle_army =	(
	"spawn_quick_battle_army",
		[
			(store_script_param, ":cur_entry_point", 1),
			(store_script_param, ":faction_no", 2),
			(store_script_param, ":infantry_ratio", 3),
			(store_script_param, ":archers_ratio", 4),
			(store_script_param, ":cavalry_ratio", 5),
			(store_script_param, ":divide_archer_entry_points", 6),
			(store_script_param, ":player_team", 7),
			
			(try_begin),
				(eq, ":player_team", 1),
				(call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_1_size"),
				(assign, ":army_size", reg0),
				(set_player_troop, "$g_quick_battle_troop"),
				(set_visitor, ":cur_entry_point", "$g_quick_battle_troop"),
				(try_begin),
					(eq, ":cur_entry_point", 0),
					(try_begin),
						(is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
						(faction_get_slot, "$g_quick_battle_team_0_banner", ":faction_no", slot_faction_banner),
					(else_try),
						(assign, "$g_quick_battle_team_0_banner", "mesh_banners_default_b"),
					(try_end),
				(else_try),
					(try_begin),
						(is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
						(faction_get_slot, "$g_quick_battle_team_1_banner", ":faction_no", slot_faction_banner),
					(else_try),
						(assign, "$g_quick_battle_team_1_banner", "mesh_banners_default_b"),
					(try_end),
				(try_end),
				(val_add, ":cur_entry_point", 1),
				
			(else_try),
				(call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_2_size"),
				(assign, ":army_size", reg0),
				(try_begin),
					(eq, ":cur_entry_point", 0),
					(assign, "$g_quick_battle_team_0_banner", "mesh_banners_default_a"),
				(else_try),
					(assign, "$g_quick_battle_team_1_banner", "mesh_banners_default_a"),
				(try_end),
				(val_add, ":cur_entry_point", 1),
			(try_end),
			
			(store_mul, ":num_infantry", ":infantry_ratio", ":army_size"),
			(val_div, ":num_infantry", 100),
			(store_mul, ":num_archers", ":archers_ratio", ":army_size"),
			(val_div, ":num_archers", 100),
			(store_mul, ":num_cavalry", ":cavalry_ratio", ":army_size"),
			(val_div, ":num_cavalry", 100),
			
			(try_begin),
				(store_add, ":num_total", ":num_infantry", ":num_archers"),
				(val_add, ":num_total", ":num_cavalry"),
				(neq, ":num_total", ":army_size"),
				(store_sub, ":leftover", ":army_size", ":num_total"),
				(try_begin),
					(gt, ":infantry_ratio", ":archers_ratio"),
					(gt, ":infantry_ratio", ":cavalry_ratio"),
					(val_add, ":num_infantry", ":leftover"),
				(else_try),
					(gt, ":archers_ratio", ":cavalry_ratio"),
					(val_add, ":num_archers", ":leftover"),
				(else_try),
					(val_add, ":num_cavalry", ":leftover"),
				(try_end),
			(try_end),
			
			(store_mul, ":rand_min", ":num_infantry", 15),
			(val_div, ":rand_min", 100),
			(store_mul, ":rand_max", ":num_infantry", 45),
			(val_div, ":rand_max", 100),
			(store_random_in_range, ":num_tier_2_infantry", ":rand_min", ":rand_max"),
			(store_sub, ":num_tier_1_infantry", ":num_infantry", ":num_tier_2_infantry"),
			(store_mul, ":rand_min", ":num_archers", 15),
			(val_div, ":rand_min", 100),
			(store_mul, ":rand_max", ":num_archers", 45),
			(val_div, ":rand_max", 100),
			(store_random_in_range, ":num_tier_2_archers", ":rand_min", ":rand_max"),
			(store_sub, ":num_tier_1_archers", ":num_archers", ":num_tier_2_archers"),
			(store_mul, ":rand_min", ":num_cavalry", 15),
			(val_div, ":rand_min", 100),
			(store_mul, ":rand_max", ":num_cavalry", 45),
			(val_div, ":rand_max", 100),
			(store_random_in_range, ":num_tier_2_cavalry", ":rand_min", ":rand_max"),
			(store_sub, ":num_tier_1_cavalry", ":num_cavalry", ":num_tier_2_cavalry"),
			
			(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_infantry),
			(set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_2_infantry"),
			(val_add, ":cur_entry_point", 1),
			(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_infantry),
			(set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_1_infantry"),
			(val_add, ":cur_entry_point", 1),
			(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_cavalry),
			(set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_2_cavalry"),
			(val_add, ":cur_entry_point", 1),
			(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_cavalry),
			(set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_1_cavalry"),
			(val_add, ":cur_entry_point", 1),
			
			(try_begin),
				(eq, ":divide_archer_entry_points", 0),
				(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_archer),
				(set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_2_archers"),
				(val_add, ":cur_entry_point", 1),
				(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_archer),
				(set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_1_archers"),
				(val_add, ":cur_entry_point", 1),
			(else_try),
				(assign, ":cur_entry_point", 40), #archer positions begin point
				(store_div, ":num_tier_1_archers_ceil_8", ":num_tier_1_archers", 8),
				(val_mul, ":num_tier_1_archers_ceil_8", 8),
				(try_begin),
					(neq, ":num_tier_1_archers_ceil_8", ":num_tier_1_archers"),
					(val_div, ":num_tier_1_archers_ceil_8", 8),
					(val_add, ":num_tier_1_archers_ceil_8", 1),
					(val_mul, ":num_tier_1_archers_ceil_8", 8),
				(try_end),
				(store_div, ":num_tier_2_archers_ceil_8", ":num_tier_2_archers", 8),
				(val_mul, ":num_tier_2_archers_ceil_8", 8),
				(try_begin),
					(neq, ":num_tier_2_archers_ceil_8", ":num_tier_2_archers"),
					(val_div, ":num_tier_2_archers_ceil_8", 8),
					(val_add, ":num_tier_2_archers_ceil_8", 1),
					(val_mul, ":num_tier_2_archers_ceil_8", 8),
				(try_end),
				(store_add, ":num_archers_ceil_8", ":num_tier_1_archers_ceil_8", ":num_tier_2_archers_ceil_8"),
				(store_div, ":num_archers_per_entry_point", ":num_archers_ceil_8", 8),
				(assign, ":left_tier_1_archers", ":num_tier_1_archers"),
				(assign, ":left_tier_2_archers", ":num_tier_2_archers"),
				(assign, ":end_cond", 1000),
				(try_for_range, ":unused", 0, ":end_cond"),
					(try_begin),
						(gt, ":left_tier_2_archers", 0),
						(assign, ":used_tier_2_archers", ":num_archers_per_entry_point"),
						(val_min, ":used_tier_2_archers", ":left_tier_2_archers"),
						(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_archer),
						(set_visitors, ":cur_entry_point", ":cur_troop", ":used_tier_2_archers"),
						(val_add, ":cur_entry_point", 1),
						(val_sub, ":left_tier_2_archers", ":used_tier_2_archers"),
					(else_try),
						(gt, ":left_tier_1_archers", 0),
						(assign, ":used_tier_1_archers", ":num_archers_per_entry_point"),
						(val_min, ":used_tier_1_archers", ":left_tier_1_archers"),
						(faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_archer),
						(set_visitors, ":cur_entry_point", ":cur_troop", ":used_tier_1_archers"),
						(val_add, ":cur_entry_point", 1),
						(val_sub, ":left_tier_1_archers", ":used_tier_1_archers"),
					(else_try),
						(assign, ":end_cond", 0),
					(try_end),
				(try_end),
			(try_end),
	])