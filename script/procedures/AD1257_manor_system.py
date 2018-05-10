from header import *

#script_update_manor_array
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: none
	#output: none
	#updates the trp_manor_array troop, which is the storage troop for manor id
update_manor_array = (
	"update_manor_array",
	[
			 (assign, ":slot_nr", 1),
		 (try_for_parties, ":party_id"),
			 (party_get_template_id,":party_template",":party_id"),
		 (eq, ":party_template", "pt_manor"),
		 (troop_set_slot,"trp_manor_array",":slot_nr",":party_id"),
		 (val_add, ":slot_nr", 1),		
		 
		 (party_get_slot, ":center", ":party_id", slot_village_bound_center), #get the village of the manor
		 (party_set_slot,":center",village_slot_manor,":party_id"), #save the manor to the village
		 #assign scenes
		 (call_script, "script_manor_set_unique_scene", ":party_id", ":center"),
		 (try_end), #cycle
		 (troop_set_slot,"trp_manor_array",0,":slot_nr"), #zero hold the total amount of parties
	])

	
	#script_prepare_manor_troops
	#input:none
	#output:none
	#description: this will set the goods of the manor craftsman
prepare_manor_troops = (
	"prepare_manor_troops",
	[
		(troop_set_slot,"trp_manor_grain", manor_troop_slot_good, itm_grain),
		(troop_set_slot,"trp_manor_livestock", manor_troop_slot_good, itm_wool),
		(troop_set_slot,"trp_manor_fruit", manor_troop_slot_good, itm_apples),
		(troop_set_slot,"trp_manor_fisher", manor_troop_slot_good, itm_smoked_fish),
		(troop_set_slot,"trp_manor_baker", manor_troop_slot_good, itm_bread),
		(troop_set_slot,"trp_manor_winer", manor_troop_slot_good, itm_wine),
		(troop_set_slot,"trp_manor_brewer", manor_troop_slot_good, itm_ale),
		(troop_set_slot,"trp_manor_potter", manor_troop_slot_good, itm_pottery),
		(troop_set_slot,"trp_manor_blacksmith", manor_troop_slot_good, itm_tools),
		(troop_set_slot,"trp_manor_butcher", manor_troop_slot_good, itm_dried_meat),
		(troop_set_slot,"trp_manor_oilmaker", manor_troop_slot_good, itm_oil),
		(troop_set_slot,"trp_manor_linen", manor_troop_slot_good, itm_linen),
		(troop_set_slot,"trp_manor_wool", manor_troop_slot_good, itm_wool_cloth),
		(troop_set_slot,"trp_manor_tanner", manor_troop_slot_good, itm_leatherwork),	
		 
		(troop_set_slot,"trp_manor_trader_silk", manor_troop_slot_good, itm_raw_silk),
		(troop_set_slot,"trp_manor_trader_spice", manor_troop_slot_good, itm_spice),
		(troop_set_slot,"trp_manor_trader_dyes", manor_troop_slot_good, itm_raw_dyes),
		(troop_set_slot,"trp_manor_trader_salt", manor_troop_slot_good, itm_salt),
		 
		(troop_set_slot,"trp_manor_grain", manor_troop_slot_tax, manor_slot_tax_grainfarm),
		(troop_set_slot,"trp_manor_livestock", manor_troop_slot_tax, manor_slot_tax_livestock),
		(troop_set_slot,"trp_manor_fruit", manor_troop_slot_tax, manor_slot_tax_fruitfarm),
		(troop_set_slot,"trp_manor_fisher", manor_troop_slot_tax, manor_slot_tax_fisher),
		(troop_set_slot,"trp_manor_baker", manor_troop_slot_tax, manor_slot_tax_bakery),
		(troop_set_slot,"trp_manor_winer", manor_troop_slot_tax, manor_slot_tax_winery),
		(troop_set_slot,"trp_manor_brewer", manor_troop_slot_tax, manor_slot_tax_brewery),
		(troop_set_slot,"trp_manor_potter", manor_troop_slot_tax, manor_slot_tax_potter),
		(troop_set_slot,"trp_manor_blacksmith", manor_troop_slot_tax, manor_slot_tax_blacksmith),
		(troop_set_slot,"trp_manor_butcher", manor_troop_slot_tax, manor_slot_tax_butcher),
		(troop_set_slot,"trp_manor_oilmaker", manor_troop_slot_tax, manor_slot_tax_oilmaker),
		(troop_set_slot,"trp_manor_linen", manor_troop_slot_tax, manor_slot_tax_linenworkshop),
		(troop_set_slot,"trp_manor_wool", manor_troop_slot_tax, manor_slot_tax_woolworkshop),
		(troop_set_slot,"trp_manor_tanner", manor_troop_slot_tax, manor_slot_tax_tannery),	
	])
	
	#script_spawn_manors - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
	# DESCRIPTION: Spawns random manor type to villages, castles and towns
spawn_manors = (
	"spawn_manors",
	[  
		(try_for_range, ":center", centers_begin, centers_end),
			(neg|is_between, ":center", castles_begin, castles_end),
			(store_faction_of_party, ":center_faction", ":center"),
		(is_between, ":center_faction", kingdoms_begin, kingdoms_end),
		(store_random_in_range, ":random", 0, 100),
		(lt, ":random", 50),
		(call_script, "script_spawn_manor_party", "pt_manor", ":center"),
		(try_end),
		
		(call_script, "script_update_manor_array"),
	])
	
	#script_spawn_manor_party - tom made
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	#input: party to spawn, center to bind to and spawn around it, bound and rename party(if 0 - not, only for manors).
	#output: reg0 - party id.
spawn_manor_party = (
	"spawn_manor_party",
	[
		(store_script_param, ":random", 1),
		(store_script_param, ":center", 2),
		
		(set_spawn_radius, 7),
		(store_faction_of_party, ":center_faction", ":center"),
		(spawn_around_party, ":center", ":random"),
		(assign, ":party_id", reg0),
		(try_begin), #this can fail?
			(party_get_position, pos0, ":center"),
			(map_get_land_position_around_position, pos1, pos0, 5),
		(try_end),
		
		(party_get_position, pos0, ":center"),
		(assign, ":upper_bound", 3000),
		(try_for_range, reg1, 0, ":upper_bound"),
			(map_get_land_position_around_position, pos1, pos0, 7),
			(assign, ":bad", 0),
			(try_for_parties, ":parties"),
				(this_or_next|is_between, ":parties", centers_begin, centers_end),
			(eq, ":parties", "pt_manor"),
				(party_get_position, pos2, ":parties"),
			(get_distance_between_positions_in_meters, ":distance", pos2, pos1),
			(try_begin),
				(lt, ":distance", 1),
				(assign, ":bad", 1),
			(try_end),  
			(try_end),
			(try_begin),
				(eq, ":bad", 0),
				(party_set_position,":party_id",pos1),
			(party_get_current_terrain, ":terrain", ":party_id"),
			(try_begin), #bridge/shore - means boo boo
				(eq, ":terrain", rt_bridge),
			(else_try),
				(assign, ":upper_bound", -8),
			(try_end),
			(try_end),	
		(try_end),
		
		##spawn some random buildings in it
		(store_random_in_range, ":random", 1, 5),
		(try_for_range, reg0, 0, ":random"),
			(store_random_in_range, ":random_building", manor_slot_marketplace, manor_slot_walls),
			(party_set_slot, ":party_id", ":random_building", manor_building_operational),
		(try_end),
		
		##add some random stats
		(try_begin),
			(store_random_in_range, ":population", 10, 50),
			(store_random_in_range, ":prosperity", 1, 10),
			(party_set_slot, ":party_id", manor_slot_population, ":population"),
			(party_set_slot, ":party_id", slot_town_prosperity, ":prosperity"),
		(try_end),
		
		#(party_set_position,":party_id",pos1),
		(party_set_faction,":party_id", ":center_faction"),
		(party_set_slot, ":party_id", slot_village_bound_center, ":center"),
		(str_store_party_name, s0, ":center"),
		(str_store_party_name, s1, ":party_id"),
		(str_store_string, s2, "@{s1} of {s0}"),
		(party_set_name, ":party_id", s2),
		(assign, reg0, ":party_id"),
	])
