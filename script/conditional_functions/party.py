from header import *

# script_cf_party_under_player_suggestion
		# idk wtf is this. 
		# INPUT: arg1 = party_no
		# OUTPUT: none. Can fail!

cf_party_under_player_suggestion =	(
	"cf_party_under_player_suggestion",
			[
				(store_script_param, ":party_no", 1),
				
				(party_slot_eq, ":party_no", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
				
				(party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
				(party_slot_eq, ":party_no", slot_party_orders_type, ":ai_state"),
				
				(party_get_slot, ":ai_object", ":party_no", slot_party_ai_object),
				(party_slot_eq, ":party_no", slot_party_orders_object, ":ai_object"),
				
				(store_current_hours, ":hours_since_orders_given"),
				(party_get_slot, ":orders_time", ":party_no", slot_party_orders_time),
				
				(val_sub, ":hours_since_orders_given", ":orders_time"),
				(lt, ":hours_since_orders_given", 12),
		])