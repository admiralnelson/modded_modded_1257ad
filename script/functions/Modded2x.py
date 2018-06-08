from header import *


#script_modded2x_Int2Bin
#INPUT: a number
#OUTPUT: s1, binary string
modded2x_Int2Bin = (
	"modded2x_Int2Bin",
	[
		(store_script_param, ":input", 1),

		#var
		(assign, ":while_loop_bound", 2),
		(assign, ":quotient", 0),
		(str_clear, s1),

		(try_for_range, ":while_loop", 0, ":while_loop_bound"),
		  	(try_begin),
		  		(gt, ":input", 0),
		  			(store_mod, reg0, ":input", 2),
		  			(store_div, ":quotient", ":input", 2),
		  			(str_store_string, s1, "@{reg0}{s1}"),
		  			(assign, ":input",":quotient" ),
		  			(val_add, ":while_loop_bound", 1), #inc 1
		  	(else_try),
		  	    	(val_add, ":while_loop_bound", -1), #exit loop
		  	(try_end),
		(try_end),
		(str_store_string, s1, "@0B{s1}"),
	])