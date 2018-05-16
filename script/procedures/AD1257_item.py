from header import *

#script_maintain_broken_items
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		#INPUT: none
		#OUTPUT: none
maintain_broken_items =	(
	"maintain_broken_items",
			[
			(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
			(troop_get_inventory_capacity, ":inv_cap_b", "trp_broken_items"),
			(try_for_range, ":i_slot_b", 0, ":inv_cap_b"),
				(assign, ":dont_remove", 0),
				(troop_get_inventory_slot, ":item_b", "trp_broken_items", ":i_slot_b"),
				(try_for_range, ":i_slot", 0, ":inv_cap"),
				(troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
				(troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
				(eq, ":modifier", imod_poor),
				(eq, ":item", ":item_b"),
				(assign, ":dont_remove", 1),
				(try_end),
				(eq, ":dont_remove", 0),
				(troop_remove_item, "trp_broken_items", ":item_b"),
			(try_end),
			])