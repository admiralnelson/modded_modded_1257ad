from header import *

	#script_modded2x_print_fizzbuzz
	# DESCRIPTION: just a test lol
	#INPUT: input_size
	#OUTPUT: none
modded2x_print_fizzbuzz =	(
	"modded2x_print_fizzbuzz",
	[
		(store_script_param, ":input_size", 1),
		(try_for_range, ":i", 1, ":input_size"),
		    (store_mod, reg0, ":i", 3),
		    (store_mod, reg1, ":i", 5),
		    (str_clear, s1),
		    (try_begin),
		        (eq, reg0,0),
		        	(str_store_string, s1, "@{s1}Fizz"),
		    (try_end),
		    (try_begin),
		        (eq, reg1,0),
		        	(str_store_string, s1, "@{s1}Buzz"),
		    (try_end),
		    (try_begin),
		    	(neq, reg0,0),(neq, reg1,0),
		    		(assign, reg0, ":i"),
		        	(str_store_string, s1, "@{reg0}"),
		    (try_end),
		    (display_message, s1),
		(try_end),
		
	])

modded2x_print_debug = (
	"modded2x_print_debug",
	[
		(store_script_param, ":stringToOutput", 1),
		(try_for_range, ":i", 1, ":input_size"),
		    (store_mod, reg0, ":i", 3),
		    (store_mod, reg1, ":i", 5),
		    (str_clear, s1),
		    (try_begin),
		        (eq, reg0,0),
		        	(str_store_string, s1, "@{s1}Fizz"),
		    (try_end),
		    (try_begin),
		        (eq, reg1,0),
		        	(str_store_string, s1, "@{s1}Buzz"),
		    (try_end),
		    (try_begin),
		    	(neq, reg0,0),(neq, reg1,0),
		    		(assign, reg0, ":i"),
		        	(str_store_string, s1, "@{reg0}"),
		    (try_end),
		    (display_message, s1),
		(try_end),
		
	])