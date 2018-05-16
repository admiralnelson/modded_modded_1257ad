from header import *

# script_get_book_read_slot
	# INPUT	: troop_no, item_no
	# OUTPUT : slot_no
get_book_read_slot = (
	"get_book_read_slot",
		[
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":item_no", 2),
		
		(store_sub, ":num_companions", companions_end, companions_begin),
		(store_sub, ":item_offset", ":item_no", readable_books_begin),
		(store_sub, ":troop_offset", ":troop_no", companions_begin),
		
		(store_mul, ":slot_no", ":item_offset", ":num_companions"),
		(val_add, ":slot_no", ":troop_offset"),
		(assign, reg0, ":slot_no"),
	])

	# script_get_troop_max_hp
	# INPUT	: troop_no
	# OUTPUT : skill
get_troop_max_hp = (
	"get_troop_max_hp",
		[
		(store_script_param_1, ":troop"),
		
		(store_skill_level, ":skill", skl_ironflesh, ":troop"),
		(store_attribute_level, ":attrib", ":troop", ca_strength),
		(val_mul, ":skill", 2),
		(val_add, ":skill", ":attrib"),
		(val_add, ":skill", 35),
		(assign, reg0, ":skill"),
	])

	#script_get_dest_color_from_rgb
	# INPUT: red, green, blue
	# OUTPUT: cur_color (in hex value)
get_dest_color_from_rgb = (
	"get_dest_color_from_rgb",
		[
		(store_script_param, ":red", 1),
		(store_script_param, ":green", 2),
		(store_script_param, ":blue", 3),
		
		(assign, ":cur_color", 0xFF000000),
		(val_mul, ":green", 0x100),
		(val_mul, ":red", 0x10000),
		(val_add, ":cur_color", ":blue"),
		(val_add, ":cur_color", ":green"),
		(val_add, ":cur_color", ":red"),
		(assign, reg0, ":cur_color"),
	])
	
	#script_convert_rgb_code_to_html_code
	# NOTE: modded2x: (redundant? )
	# INPUT: red, green, blue
	# OUTPUT: s0 
convert_rgb_code_to_html_code = (
	"convert_rgb_code_to_html_code",
		[
		(store_script_param, ":red", 1),
		(store_script_param, ":green", 2),
		(store_script_param, ":blue", 3),
		
		(str_store_string, s0, "@#"),
			
			(store_div, ":r_1", ":red", 0x10),
			(store_add, ":dest_string", "str_key_0", ":r_1"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_mod, ":r_2", ":red", 0x10),
			(store_add, ":dest_string", "str_key_0", ":r_2"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_div, ":g_1", ":green", 0x10),
			(store_add, ":dest_string", "str_key_0", ":g_1"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_mod, ":g_2", ":green", 0x10),
			(store_add, ":dest_string", "str_key_0", ":g_2"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_div, ":b_1", ":blue", 0x10),
			(store_add, ":dest_string", "str_key_0", ":b_1"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
			
			(store_mod, ":b_2", ":blue", 0x10),
			(store_add, ":dest_string", "str_key_0", ":b_2"),
			(str_store_string, s1, ":dest_string"),
			(str_store_string, s0, "@{s0}{s1}"),
		])
		
		#script_convert_slot_no_to_color
		# INPUT: red, green, blue
		# OUTPUT: dest_color 							
convert_slot_no_to_color = (
		"convert_slot_no_to_color",
		[
			(store_script_param, ":cur_color", 1),
			
			(store_mod, ":blue", ":cur_color", 6),
			(val_div, ":cur_color", 6),
			(store_mod, ":green", ":cur_color", 6),
			(val_div, ":cur_color", 6),
			(store_mod, ":red", ":cur_color", 6),
			(val_mul, ":blue", 0x33),
			(val_mul, ":green", 0x33),
			(val_mul, ":red", 0x33),
			(assign, ":dest_color", 0xFF000000),
			(val_mul, ":green", 0x100),
			(val_mul, ":red", 0x10000),
			(val_add, ":dest_color", ":blue"),
			(val_add, ":dest_color", ":green"),
			(val_add, ":dest_color", ":red"),
			(assign, reg0, ":dest_color"),
		])

		#script_vector_length
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: position vector
		#OUTPUT: length
vector_length =	(
	"vector_length",
			[
			(store_script_param, ":pos", 1),
			
			(set_fixed_point_multiplier, 10),
			(position_get_x, ":x", ":pos"),
			(position_get_y, ":y", ":pos"),
			
			(store_mul, ":xsq", ":x", ":x"),
			(store_mul, ":ysq", ":y", ":y"),
			
			(store_add, ":xysq", ":xsq", ":ysq"),
			(store_pow, reg0, ":xysq", 5),
			
			(val_div, reg0, 10),
			])