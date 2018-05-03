from header import *

	#script_game_get_item_extra_text:
		# This script is called from the game engine when an item's properties are displayed.
		# WARNING: modified by 1257AD devs
		# INPUT: arg1 = item_no, arg2 = extra_text_id (this can be between 0-7 (7 included)), arg3 = item_modifier
		# OUTPUT: result_string = item extra text, trigger_result = text color (0 for default)
game_get_item_extra_text = (
	"game_get_item_extra_text",
			[
				(store_script_param, ":item_no", 1),
				(store_script_param, ":extra_text_id", 2),
				(store_script_param, ":item_modifier", 3),
				
		#tom
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg0, ":item_no"),
			(set_result_string, "@ID {reg0}"),
					(set_trigger_result, 0xff0000),
		(try_end),
		#tom
				#rafi
				(try_begin),
					(eq, ":item_modifier", imod_poor),
					(eq, ":extra_text_id", 0),
					(set_result_string, "@This item is severely damaged!"),
					(set_trigger_result, 0xff0000),
				(try_end),
				#end rafi
				(try_begin),
					(is_between, ":item_no", food_begin, food_end),
					(try_begin),
						(eq, ":extra_text_id", 0),
						(assign, ":continue", 1),
						(try_begin),
							(this_or_next|eq, ":item_no", "itm_cattle_meat"),
							(this_or_next|eq, ":item_no", "itm_pork"),
							(eq, ":item_no", "itm_chicken"),
							
							(eq, ":item_modifier", imod_rotten),
							(assign, ":continue", 0),
						(try_end),
						(eq, ":continue", 1),
						(item_get_slot, ":food_bonus", ":item_no", slot_item_food_bonus),
						(assign, reg1, ":food_bonus"),
						(set_result_string, "@+{reg1} to party morale"),
						(set_trigger_result, 0x4444FF),
					(try_end),
				(else_try),
					(is_between, ":item_no", readable_books_begin, readable_books_end),
					(try_begin),
						(eq, ":extra_text_id", 0),
						(item_get_slot, reg1, ":item_no", slot_item_intelligence_requirement),
						(set_result_string, "@Requires {reg1} intelligence to read"),
						(set_trigger_result, 0xFFEEDD),
					(else_try),
						(eq, ":extra_text_id", 1),
						(item_get_slot, ":progress", ":item_no", slot_item_book_reading_progress),
						(val_div, ":progress", 10),
						(assign, reg1, ":progress"),
						(set_result_string, "@Reading Progress: {reg1}%"),
						(set_trigger_result, 0xFFEEDD),
					(try_end),
				(else_try),
					(is_between, ":item_no", reference_books_begin, reference_books_end),
					(try_begin),
						(eq, ":extra_text_id", 0),
						(try_begin),
							(eq, ":item_no", "itm_book_wound_treatment_reference"),
							(str_store_string, s1, "@wound treament"),
						(else_try),
							(eq, ":item_no", "itm_book_training_reference"),
							(str_store_string, s1, "@trainer"),
						(else_try),
							(eq, ":item_no", "itm_book_surgery_reference"),
							(str_store_string, s1, "@surgery"),
						(try_end),
						(set_result_string, "@+1 to {s1} while in inventory"),
						(set_trigger_result, 0xFFEEDD),
					(try_end),
				(try_end),
		])


