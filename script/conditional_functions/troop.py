from header import *

# script_cf_is_quest_troop
		# Input: arg1 = troop_no
		# Output: none (can fail)
cf_is_quest_troop = (
	"cf_is_quest_troop",
			[
				(store_script_param_1, ":troop_no"),
				(assign, ":is_quest_troop", 0),
				(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
					(check_quest_active, ":cur_quest"),
					(quest_get_slot, ":quest_troop_1", ":cur_quest", slot_quest_target_troop),
					(quest_get_slot, ":quest_troop_2", ":cur_quest", slot_quest_object_troop),
					(quest_get_slot, ":quest_troop_3", ":cur_quest", slot_quest_giver_troop),
					(this_or_next|eq, ":quest_troop_1", ":troop_no"),
					(this_or_next|eq, ":quest_troop_2", ":troop_no"),
					(eq, ":quest_troop_3", ":troop_no"),
					(assign, ":is_quest_troop", 1),
				(try_end),
				(eq, ":is_quest_troop", 1),
		])

		# script_cf_troop_check_troop_is_enemy
		# Input: arg1 = troop_no, arg2 = checked_troop_no
		# Output: none (Can fail)
cf_troop_check_troop_is_enemy = (
	"cf_troop_check_troop_is_enemy",
			[
				(store_script_param_1, ":troop_no"),
				(store_script_param_2, ":checked_troop_no"),
				(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":checked_troop_no"),
				(lt, reg0, -10),
		])