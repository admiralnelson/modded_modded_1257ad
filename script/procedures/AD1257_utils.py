from header import *

# script_get_inventory_weight_of_whole_party
	# INPUT	: none
	# OUTPUT : none
get_inventory_weight_of_whole_party =	(
	"get_inventory_weight_of_whole_party",
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
	])

	# script_sort_food
	# INPUT	: troop_no
	# OUTPUT : none
sort_food =	(
	"sort_food",
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
	])
	

	# script_auto_sell
	# INPUT	: customer, merchant
	# OUTPUT : none
auto_sell =	(
	"auto_sell", [
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
	])
	
	# script_start_town_conversation
	# INPUT	: troop_slot_no, entry_no
	# OUTPUT : none
start_town_conversation =	(
	"start_town_conversation",
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
	])

	#script_copy_inventory
	# INPUT: source, target
	# OUTPUT: NONE
copy_inventory =	(
	"copy_inventory",
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
	])
	
	#script_sell_all_prisoners
	# INPUT: NONE
	# OUTPUT: NONE
sell_all_prisoners =	(
	"sell_all_prisoners",
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
	])
	

	#script_clear_troop_array
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#description: clears the troop array
	#input: troop, begin_index, end_index
	#output: none
clear_troop_array =	(
	"clear_troop_array",
		[
		(store_script_param, ":troop_array", 1),
		(store_script_param, ":begin_index", 2),
		(store_script_param, ":end_index", 3),
		(try_for_range, ":index", ":begin_index", ":end_index"),
			(troop_set_slot, ":troop_array", ":index", 0),
		(try_end),
	])