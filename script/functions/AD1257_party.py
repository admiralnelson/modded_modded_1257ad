from header import *
## script_get_and_remove_member
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	## description: selects the first member from the party and removes it from the party, but returns the id
		## Input: party_to_do_so
		## Output: reg1 - troop
get_and_remove_member =	(
	"get_and_remove_member",
	[
		(store_script_param, ":party", 1),
		(assign, reg1, -1),
		(party_get_num_companion_stacks, ":num_stacks",":party"),
		(try_begin),
			(gt, ":num_stacks", 0),
		(party_stack_get_troop_id, ":stack_troop",":party",0),
		(assign, reg1, ":stack_troop"),
		(party_remove_members,":party",":stack_troop",1),
		(try_end),
	])