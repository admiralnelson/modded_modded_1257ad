from header import *


	#script_remove_manor_objects - tommade
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT:none
	# OUTPUT:none
	#description: removes the objects from unique manor scenes which suppose to be not used
remove_manor_objects= (
	"remove_manor_objects",
			[
		(store_current_scene,":scene"),
		(try_begin),
			(eq, ":scene", "scn_manor_fortified_teutonic"),
			(try_begin), #house 1
			(party_slot_eq, "$g_encountered_party", manor_slot_houses, 0),
			(replace_scene_props, "spr_earth_house_c", "spr_empty"),
			(replace_scene_props, "spr_chair_trunk_c", "spr_empty"),
		(try_end),
			(try_begin), #house 2
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_houses, 2),
			(replace_scene_props, "spr_to_fake_house_f", "spr_empty"),
			(replace_scene_props, "spr_passage_house_a", "spr_empty"),
			(replace_scene_props, "spr_chair_trunk_a", "spr_empty"), 
		(try_end),
		(try_begin), #temple
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_Monastery, manor_building_operational),
			(replace_scene_props, "spr_1257_chapel", "spr_empty"),
			(replace_scene_props, "spr_village_wall_a", "spr_empty"),
			(replace_scene_props, "spr_village_wall_b", "spr_empty"),
		(try_end), 
		(try_begin), #marketplace
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_marketplace, manor_building_operational),
			(replace_scene_props, "spr_wooden_stand", "spr_empty"),
			(replace_scene_props, "spr_cart", "spr_empty"),
		(try_end), 
		(try_begin), #tavern
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_tavern, manor_building_operational),
			(replace_scene_props, "spr_to_town_house_u", "spr_empty"),
			(replace_scene_props, "spr_tavern_barrel", "spr_empty"),
			(replace_scene_props, "spr_tavern_sign", "spr_empty"),
		(try_end), 
		(try_begin), #whorehouse
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_whorehouse, manor_building_operational),
			(replace_scene_props, "spr_earth_house_a", "spr_empty"),
			# (replace_scene_props, "spr_tavern_chair_a", "spr_empty"),
			# (replace_scene_props, "spr_tavern_chair_b", "spr_empty"),
		(try_end), 
		(try_begin), #blacksmith
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_blacksmith, manor_building_operational),
			(replace_scene_props, "spr_town_house_aa", "spr_empty"),
			(replace_scene_props, "spr_stand_thatched", "spr_empty"),
			#(replace_scene_props, "spr_smithy_anvil", "spr_empty"),
			(replace_scene_props, "spr_smithy_forge", "spr_empty"),
		(try_end), 
		(try_begin), #weaponsmith
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_weaponsmith, manor_building_operational),
			(replace_scene_props, "spr_gatehouse_new_a", "spr_empty"),
			(replace_scene_props, "spr_smithy_forge", "spr_empty"),
		(try_end), 
		(try_begin), #armor_smith
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_armorsmith, manor_building_operational),
			(replace_scene_props, "spr_town_house_d", "spr_empty"),
			(replace_scene_props, "spr_smithy_grindstone_wheel", "spr_empty"),
		(try_end), 
		(try_begin), #fletcher
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fletcher, manor_building_operational),
			#(replace_scene_props, "spr_town_house_h", "spr_empty"),
			(replace_scene_props, "spr_arena_archery_target_a", "spr_empty"),
			(replace_scene_props, "spr_archery_target_with_hit_a", "spr_empty"),
		(try_end), 
		(try_begin), #potter
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_potter, manor_building_operational),
			(replace_scene_props, "spr_to_castle_courtyard_house_b", "spr_empty"),
			(replace_scene_props, "spr_cup", "spr_empty"),
			(replace_scene_props, "spr_jug", "spr_empty"),
		(try_end), 
		(try_begin), #baker
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_bakery, manor_building_operational),
			(replace_scene_props, "spr_to_town_house_t", "spr_empty"),
			(replace_scene_props, "spr_bread_a", "spr_empty"),
		(try_end), 
		(try_begin), #butcher
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_butcher, manor_building_operational),
			(replace_scene_props, "spr_to_castle_courtyard_house_c", "spr_empty"),
		(try_end), 
		(try_begin), #brewer
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_brewery, manor_building_operational),
			(replace_scene_props, "spr_brewery_big_bucket", "spr_empty"),
			#(replace_scene_props, "spr_brewery_pool", "spr_empty"),
			(replace_scene_props, "spr_to_courtyard_gate_b", "spr_empty"),
			#(replace_scene_props, "spr_brewery_bucket_platform_b", "spr_empty"),
		(try_end),
		(try_begin), #winery
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_winery, manor_building_operational),
			(replace_scene_props, "spr_to_gatehouse_b", "spr_empty"),
			(replace_scene_props, "spr_winery_middle_barrel", "spr_empty"),
			(replace_scene_props, "spr_winery_wine_press", "spr_empty"),
			(replace_scene_props, "spr_winery_barrel_shelf", "spr_empty"),
		(try_end), 
		(try_begin), #prison
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_prison, manor_building_operational),
			(replace_scene_props, "spr_to_castle_h_house_b", "spr_empty"),
		(try_end), 
		(try_begin), #stables
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_breeder, manor_building_operational),
			(replace_scene_props, "spr_to_castle_h_house_c", "spr_empty"),
			(replace_scene_props, "spr_feeding_trough_a", "spr_empty"),
		(try_end), 
		(try_begin), #linen_workshop
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_linenworkshop, manor_building_operational),
			(replace_scene_props, "spr_to_town_house_y", "spr_empty"),
		(try_end), 
		(try_begin), #wool_workshop
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_woolworkshop, manor_building_operational),
			(replace_scene_props, "spr_to_town_house_r", "spr_empty"),
		(try_end), 
		(try_begin), #tanery
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_tannery, manor_building_operational),
			(replace_scene_props, "spr_to_town_house_w", "spr_empty"),
			(replace_scene_props, "spr_tannery_hide_a", "spr_empty"),
			(replace_scene_props, "spr_to_passage_house_c", "spr_empty"),
		(try_end), 
		(try_begin), #olive press
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_oilmaker, manor_building_operational),
			(replace_scene_props, "spr_to_town_house_z", "spr_empty"),
		(try_end), 
		(try_begin), #walls
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_operational),
			(replace_scene_props, "spr_to_castle_gate_house_a", "spr_empty"),
			(replace_scene_props, "spr_to_castle_f_battlement_a", "spr_empty"),
			(replace_scene_props, "spr_to_castle_round_tower_a", "spr_empty"),
		(try_end), 
		(try_begin), #grainfram
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_grainfarm, manor_building_operational),
			(replace_scene_props, "spr_farm_house_a", "spr_empty"),
			# (replace_scene_props, "spr_angry_wheat", "spr_empty"),
			# (replace_scene_props, "spr_cabbage_b", "spr_empty"),
		(try_end), 
		(try_begin), #fruitfarm
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fruitfarm, manor_building_operational),
			(replace_scene_props, "spr_farm_house_b", "spr_empty"),
		(try_end), 
		(try_begin), #livestockfarm
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_livestock, manor_building_operational),
			(replace_scene_props, "spr_farm_house_c", "spr_empty"),
		(try_end), 
		(try_begin), #fisher
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fisher, manor_building_operational),
			(replace_scene_props, "spr_village_house_d", "spr_empty"),
			(replace_scene_props, "spr_net_a", "spr_empty"),
			(replace_scene_props, "spr_net_b", "spr_empty"),
		(try_end),  
		(try_begin), #well
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_well, manor_building_operational),
			(replace_scene_props, "spr_water_well_a", "spr_empty"),
		(try_end),
		(else_try),
			#(party_slot_eq, "$g_encountered_party", manor_slot_unique, 1),
		(try_begin), #house 1
			(party_slot_eq, "$g_encountered_party", manor_slot_houses, 0),
			(replace_scene_props, "spr_earth_house_c", "spr_empty"),
		(try_end),
			(try_begin), #house 2
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_houses, 2),
			(replace_scene_props, "spr_village_house_g", "spr_empty"),
			(replace_scene_props, "spr_village_house_h", "spr_empty"),
			(replace_scene_props, "spr_village_house_i", "spr_empty"),
			(replace_scene_props, "spr_village_house_j", "spr_empty"),
			(replace_scene_props, "spr_small_wall_f", "spr_empty"), #ka su situo daryt?
			
			(replace_scene_props, "spr_chair_trunk_c", "spr_empty"),
			(replace_scene_props, "spr_barrel", "spr_empty"),
			(replace_scene_props, "spr_box_a", "spr_empty"),
			(replace_scene_props, "spr_chair_trunk_a", "spr_empty"), 
		(try_end),
		(try_begin), #temple
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_Monastery, manor_building_operational),
			(replace_scene_props, "spr_church_a", "spr_empty"),
			(replace_scene_props, "spr_church_tower_a", "spr_empty"),
		(try_end), 
		(try_begin), #marketplace
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_marketplace, manor_building_operational),
			(replace_scene_props, "spr_wooden_stand", "spr_empty"),
			(replace_scene_props, "spr_cart", "spr_empty"),
		(try_end), 
		(try_begin), #tavern
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_tavern, manor_building_operational),
			(replace_scene_props, "spr_timber_frame_house_b", "spr_empty"),
			(replace_scene_props, "spr_tavern_barrel", "spr_empty"),
			(replace_scene_props, "spr_tavern_sign", "spr_empty"),
		(try_end), 
		(try_begin), #whorehouse
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_whorehouse, manor_building_operational),
			(replace_scene_props, "spr_timber_frame_house_c", "spr_empty"),
			(replace_scene_props, "spr_tavern_chair_a", "spr_empty"),
			(replace_scene_props, "spr_tavern_chair_b", "spr_empty"),
		(try_end), 
		(try_begin), #blacksmith
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_blacksmith, manor_building_operational),
			(replace_scene_props, "spr_town_house_aa", "spr_empty"),
			(replace_scene_props, "spr_stand_thatched", "spr_empty"),
			(replace_scene_props, "spr_smithy_anvil", "spr_empty"),
			(replace_scene_props, "spr_smithy_forge", "spr_empty"),
		(try_end), 
		(try_begin), #weaponsmith
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_weaponsmith, manor_building_operational),
			(replace_scene_props, "spr_town_house_c", "spr_empty"),
			(replace_scene_props, "spr_smithy_grindstone_wheel", "spr_empty"),
		(try_end), 
		(try_begin), #armor_smith
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_armorsmith, manor_building_operational),
			(replace_scene_props, "spr_town_house_d", "spr_empty"),
			(replace_scene_props, "spr_smithy_forge_bellows", "spr_empty"),
		(try_end), 
		(try_begin), #fletcher
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fletcher, manor_building_operational),
			(replace_scene_props, "spr_town_house_h", "spr_empty"),
			(replace_scene_props, "spr_arena_archery_target_a", "spr_empty"),
			(replace_scene_props, "spr_archery_target_with_hit_a", "spr_empty"),
		(try_end), 
		(try_begin), #potter
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_potter, manor_building_operational),
			(replace_scene_props, "spr_town_house_e", "spr_empty"),
			(replace_scene_props, "spr_table_small", "spr_empty"),
			(replace_scene_props, "spr_village_oven", "spr_empty"),
			(replace_scene_props, "spr_cup", "spr_empty"),
			(replace_scene_props, "spr_jug", "spr_empty"),
		(try_end), 
		(try_begin), #baker
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_bakery, manor_building_operational),
			(replace_scene_props, "spr_town_house_f", "spr_empty"),
			(replace_scene_props, "spr_fireplace_a", "spr_empty"),
			(replace_scene_props, "spr_table_small_b", "spr_empty"),
			(replace_scene_props, "spr_bread_a", "spr_empty"),
		(try_end), 
		(try_begin), #butcher
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_butcher, manor_building_operational),
			(replace_scene_props, "spr_town_house_g", "spr_empty"),
		(try_end), 
		(try_begin), #brewer
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_brewery, manor_building_operational),
			(replace_scene_props, "spr_brewery_big_bucket", "spr_empty"),
			(replace_scene_props, "spr_brewery_pool", "spr_empty"),
			(replace_scene_props, "spr_town_house_o", "spr_empty"),
			(replace_scene_props, "spr_brewery_bucket_platform_b", "spr_empty"),
		(try_end),
		(try_begin), #winery
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_winery, manor_building_operational),
			(replace_scene_props, "spr_town_house_za", "spr_empty"),
			(replace_scene_props, "spr_winery_middle_barrel", "spr_empty"),
			(replace_scene_props, "spr_winery_wine_press", "spr_empty"),
			(replace_scene_props, "spr_winery_wine_cart_loaded", "spr_empty"),
			(replace_scene_props, "spr_winery_wine_cart_small_loaded", "spr_empty"),
		(try_end), 
		(try_begin), #prison
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_prison, manor_building_operational),
			(replace_scene_props, "spr_torture_tool_a", "spr_empty"),
			(replace_scene_props, "spr_torture_tool_b", "spr_empty"),
			(replace_scene_props, "spr_torture_tool_c", "spr_empty"),
			(replace_scene_props, "spr_castle_courtyard_house_a", "spr_empty"),
		(try_end), 
		(try_begin), #stables
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_breeder, manor_building_operational),
			(replace_scene_props, "spr_village_shed_b", "spr_empty"),
			(replace_scene_props, "spr_village_stable_a", "spr_empty"),
			(replace_scene_props, "spr_open_stable_a", "spr_empty"),
			(replace_scene_props, "spr_open_stable_b", "spr_empty"),
			(replace_scene_props, "spr_feeding_trough_a", "spr_empty"),
		(try_end), 
		(try_begin), #linen_workshop
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_linenworkshop, manor_building_operational),
			(replace_scene_props, "spr_town_house_y", "spr_empty"),
		(try_end), 
		(try_begin), #wool_workshop
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_woolworkshop, manor_building_operational),
			(replace_scene_props, "spr_town_house_z", "spr_empty"),
		(try_end), 
		(try_begin), #tanery
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_tannery, manor_building_operational),
			(replace_scene_props, "spr_town_house_i", "spr_empty"),
			(replace_scene_props, "spr_tannery_hide_a", "spr_empty"),
			(replace_scene_props, "spr_tannery_hide_b", "spr_empty"),
			(replace_scene_props, "spr_tannery_pools_a", "spr_empty"),
			(replace_scene_props, "spr_tannery_pools_b", "spr_empty"),
		(try_end), 
		(try_begin), #olive press
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_oilmaker, manor_building_operational),
			(replace_scene_props, "spr_town_house_a", "spr_empty"),
		(try_end), 
		(try_begin), #walls
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_operational),
			(replace_scene_props, "spr_castle_f_battlement_a", "spr_empty"),
			(replace_scene_props, "spr_castle_gate_house_a", "spr_empty"),
		(try_end), 
		(try_begin), #grainfram
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_grainfarm, manor_building_operational),
			(replace_scene_props, "spr_farm_house_a", "spr_empty"),
			(replace_scene_props, "spr_angry_wheat", "spr_empty"),
			(replace_scene_props, "spr_cabbage_b", "spr_empty"),
		(try_end), 
		(try_begin), #fruitfarm
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fruitfarm, manor_building_operational),
			(replace_scene_props, "spr_farm_house_b", "spr_empty"),
		(try_end), 
		(try_begin), #livestockfarm
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_livestock, manor_building_operational),
			(replace_scene_props, "spr_farm_house_c", "spr_empty"),
		(try_end), 
		(try_begin), #fisher
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fisher, manor_building_operational),
			(replace_scene_props, "spr_earth_house_b", "spr_empty"),
			(replace_scene_props, "spr_net_a", "spr_empty"),
			(replace_scene_props, "spr_net_b", "spr_empty"),
		(try_end),  
		(try_begin), #well
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_well, manor_building_operational),
			(replace_scene_props, "spr_water_well_a", "spr_empty"),
		(try_end),
	(try_end),	
		
	#tier 2 goods - seperate for aditional cultures
	(try_begin),
		(party_slot_eq, "$g_encountered_party", manor_slot_marketplace, manor_building_operational),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_fisher, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_smoked_fish","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_oilmaker, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_oil","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_potter, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_pottery","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_linenworkshop, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_linen","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_woolworkshop, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_wool_cloth","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_blacksmith, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_tools","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_tannery, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_raw_leather","spr_empty"),
			(replace_scene_items_with_scene_props,"itm_leatherwork","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_winery, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_wine","spr_empty"), 
		(replace_scene_items_with_scene_props,"itm_quest_wine","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_brewery, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_ale","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_quest_ale","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_butcher, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_dried_meat","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_sausages","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_bakery, manor_building_operational),
			(replace_scene_items_with_scene_props,"itm_bread","spr_empty"),
		(try_end),
		
		##traders
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, "trp_manor_trader_furs"), 
			(replace_scene_items_with_scene_props,"itm_furs","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, "trp_manor_trader_salt"), 
			(replace_scene_items_with_scene_props,"itm_salt","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, "trp_manor_trader_silk"),  
			(replace_scene_items_with_scene_props,"itm_raw_silk","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, "trp_manor_trader_dyes"), 
			(replace_scene_items_with_scene_props,"itm_raw_dyes","spr_empty"),
		(try_end),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, "trp_manor_trader_spice"), 
			(replace_scene_items_with_scene_props,"itm_spice","spr_empty"),
		(try_end),
	(else_try),
		#tier 1 goods
		(replace_scene_items_with_scene_props,"itm_grain","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_honey","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_cabbages","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_apples","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_wool","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_butter","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_cheese","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_cattle_meat","spr_empty"),
			
		(replace_scene_items_with_scene_props,"itm_smoked_fish","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_oil","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_pottery","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_linen","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_wool_cloth","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_tools","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_raw_leather","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_leatherwork","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_wine","spr_empty"), 
		(replace_scene_items_with_scene_props,"itm_quest_wine","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_ale","spr_empty"),
			(replace_scene_items_with_scene_props,"itm_quest_ale","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_dried_meat","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_sausages","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_bread","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_furs","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_salt","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_raw_silk","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_raw_dyes","spr_empty"),
		(replace_scene_items_with_scene_props,"itm_spice","spr_empty"),
	(try_end),

		])


	
	#script_manor_set_unique_scene
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# NOTE: modded2x: might be cool to alter the terrain algorithms
	#input:manor_party_id, center
	#output: none
	#description: sets the manor scene based on it's terrain type
manor_set_unique_scene = (
	"manor_set_unique_scene",
		[
		(store_script_param, ":manor_party_id", 1),
		(store_script_param, ":center", 2),
		(party_get_slot, ":culture", ":center", slot_center_culture),
		
		(party_get_current_terrain, ":terrain", ":manor_party_id"),
		(try_begin),
			(this_or_next|eq, ":culture", "fac_culture_finnish"),
			(this_or_next|eq, ":culture", "fac_culture_mazovian"),
			(this_or_next|eq, ":culture", "fac_culture_teutonic"),
			(eq, ":culture", "fac_culture_baltic"),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_teutonic"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_snow),
			(eq, ":terrain", rt_snow_forest),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_snow"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_desert),
			(eq, ":terrain", rt_desert_forest),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_desert"),
		(else_try),
			(this_or_next|eq, ":terrain", rt_steppe),
			(eq, ":terrain", rt_steppe_forest),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_steppe"),
		(else_try),
			(party_set_slot, ":manor_party_id", slot_castle_exterior, "scn_manor_fortified_euro_plains"),
		(try_end),
		])

# script_init_manor_agents #init_town_walkers as template
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: manor_id
		# Output: none
init_manor_agents = (
	"init_manor_agents",
			[
		(store_script_param, ":manor_id", 1),

			(party_get_slot, ":village", ":manor_id", slot_village_bound_center), 
			(party_get_slot, ":village_lord", ":village", slot_town_lord), 
		
		(store_faction_of_party, ":manor_faction", ":manor_id"),
		(try_begin),
			(eq, ":manor_faction", "fac_player_supporters_faction"),
			(assign, ":manor_faction", "$g_player_culture"),
		(try_end),
		(party_get_slot, ":population", ":manor_id", manor_slot_population),
		(try_begin),
			(le, ":population", 200),
			(assign, ":peasents", 1),
			(assign, ":burgers", 0),
			(assign, ":nobles", 0),
		(else_try),
			(le, ":population", 400),
			(assign, ":peasents", 2),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 1),
				(assign, ":nobles", 0),
			(try_end),
		(else_try),
			(le, ":population", 600),
			(assign, ":peasents", 3),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 2),
				(assign, ":nobles", 0),  
			(try_end),
		(else_try),
			(le, ":population", 800),
			(assign, ":peasents", 4),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 3),
				(assign, ":nobles", 0),
			(try_end),
		(else_try),
			(gt, ":population", 800),
			(assign, ":peasents", 4),
			(try_begin),
				(party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
				(assign, ":burgers", 4),
				(assign, ":nobles", 1),  
			(try_end),
		(try_end),
			# (assign, ":peasents", 4),
		# (assign, ":burgers", 4),
		# (assign, ":nobles", 1),
		(try_begin),
			(eq, ":village_lord", "trp_player"),
				(set_visitor, 10, "trp_manor_seneschal"),
			(set_visitor, 11, "trp_manor_storage"),
			(set_visitor, 12, "trp_manor_marshal"),
		(try_end),
		
				(try_begin), #daytime
					(eq, "$town_nighttime", 0),
			(faction_get_slot,":culture",":manor_faction",slot_faction_culture),
			(faction_get_slot,":walker1",":culture",slot_faction_village_walker_male_troop),
			(faction_get_slot,":walker2",":culture",slot_faction_village_walker_female_troop),
					(try_for_range, ":entry_no", 31, 40), #peasents
				(try_for_range, reg0, 0, ":peasents"),
				#(store_random_in_range, ":random", 0, 6),
				#(store_add, ":troop", ":random", "trp_manor_peasent"),
				(store_random_in_range, ":troop", ":walker1", ":walker2"),
				(set_visitor, ":entry_no", ":troop"),
				# (try_begin),
					# (eq, ":random", 0),
								# (set_visitor, ":entry_no", "trp_manor_peasent", ":peasents"),
				# (else_try),
					# (set_visitor, ":entry_no", "trp_manor_peasent2", ":peasents"),
				# (try_end),
			(try_end), 
					(try_end), 
			(faction_get_slot,":culture",":manor_faction",slot_faction_culture),
			(faction_get_slot,":walker1",":culture",slot_faction_town_walker_male_troop),
			(faction_get_slot,":walker2",":culture",slot_faction_town_walker_female_troop),
			(try_for_range, ":entry_no", 20, 25), #burgers
				(try_for_range, reg0, 0, ":burgers"),
					(store_random_in_range, ":troop", ":walker1", ":walker2"),
				(set_visitor, ":entry_no", ":troop"),
			(try_end),
					(try_end), 
			
			(try_for_range, ":entry_no", 25, 30), #nobles
				(try_for_range, reg0, 0, ":nobles"),
				(store_add, ":troop_upper", "trp_manor_noble2", 1),
					(store_random_in_range, ":troop", "trp_manor_noble", ":troop_upper"),
				#(store_add, ":troop", ":random", "trp_manor_noble"),
				(set_visitor, ":entry_no", ":troop"),
			(try_end),
					(try_end), 
			
			#pedlers and craftsman
			(try_for_range, ":slot", 0, manor_slot_prison - manor_slot_grainfarm),
				(store_add, ":building_slot", ":slot", manor_slot_grainfarm),
			(store_add, ":entry_point", ":slot", 41),
			(store_add, ":troop", ":slot", "trp_manor_grain"),
				(party_slot_eq, "$g_encountered_party", ":building_slot", manor_building_operational),
			(set_visitor, ":entry_point", ":troop"),
			(party_slot_eq, "$g_encountered_party", manor_slot_marketplace, manor_building_operational),
			(store_add, ":entry_point", ":slot", 81),
			(set_visitor, ":entry_point", "trp_manor_seller"),
					(try_end),
			
			#priest
			(faction_get_slot, ":religion", ":manor_faction", slot_faction_religion),
			(try_begin),
				#(eq, ":village_lord", "trp_player"),
				(party_slot_eq, "$g_encountered_party", manor_slot_Monastery, manor_building_operational),
			(store_add, ":troop", ":religion", "trp_priest_catholic"),
				(set_visitor, 71, ":troop"),
			(try_end),
			
			#armor weapon fletcher stables - need to do order
			(try_for_range, ":slot", 0, 4),
				 #(eq, ":village_lord", "trp_player"),
				 (store_add, ":building_slot", ":slot", manor_slot_armorsmith),
			 (store_add, ":troop", ":slot", "trp_manor_armorsmith"),
			 (store_add, ":entry_point", ":slot", 13),
				 (party_slot_eq, "$g_encountered_party", ":building_slot", manor_building_operational),
			 (set_visitor, ":entry_point", ":troop"),
			(try_end),
			
			#traders
			(try_begin),
				(eq, ":village_lord", "trp_player"),
				#(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, -1),
			(party_get_slot, ":troop", "$g_encountered_party", manor_slot_trader),
			(gt, ":troop", 0),
			(set_visitor, 72, ":troop"),
			(try_end),
			
			#bookseler or crusader?
			(try_begin),
				(eq, ":village_lord", "trp_player"),
				#(neg|party_slot_eq, "$g_encountered_party", manor_slot_trader, -1),
			(party_slot_eq, "$g_encountered_party", manor_slot_Monastery_upgrade, manor_Monastery_scriptorium),
			(set_visitor, 73, "trp_manor_trader_book"),
			(try_end),
				(try_end),
		
		(try_begin), #night or day
			(try_begin),
				(party_slot_eq, "$g_encountered_party", manor_slot_whorehouse, manor_building_operational),
				(set_visitor, 70, "trp_whore"),
			(try_end),
			
			 #merc dirty code ministrel
			 (try_for_range, ":entry_point", 66, 70),
				(party_slot_eq, "$g_encountered_party", manor_slot_tavern, manor_building_operational),
			 
			 (store_random_in_range, ":random", "trp_tavern_minstrel_1", "trp_kingdom_heroes_including_player_begin"),
			 (set_visitor, ":entry_point", ":random"),
			#(call_script, "script_get_mercenary_troop_for_manor", ":manor_faction"),
			#(set_visitor, ":entry_point", reg0),
					(try_end),
			
			#guard dirty code
			(faction_get_slot, ":troop" ,":manor_faction", slot_faction_tier_2_troop),
			(try_for_range, ":entry_point", 60, 66),
				(party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_operational),
				(set_visitor, ":entry_point", ":troop"),
			(try_end),
			
			#prison
			(try_begin),
				(party_slot_eq, "$g_encountered_party", manor_slot_prison, manor_building_operational),
				(store_random_in_range, ":troop", "trp_ransom_broker_1", "trp_tavern_traveler_1"),
			(set_visitor, 17, ":troop"),
			(try_end),
			
		(try_end),
		])


	# script_init_town_walker_agents
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
init_manor_walker_agents = (
	"init_manor_walker_agents",
			[(assign, ":num_walkers", 0),
				(try_for_agents, ":cur_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			# (try_begin),
				# (eq, ":cur_troop", "trp_manor_seneschal"),
				# (agent_set_stand_animation, ":cur_agent", "anim_sit_drink"),
			
			# (entry_point_get_position, pos0, 11 ),
			# (agent_set_look_target_position, ":cur_agent", pos0), 
			# (try_end),
			(this_or_next|is_between, ":cur_troop", walkers_begin, walkers_end),
					(this_or_next|is_between, ":cur_troop", "trp_manor_noble", "trp_manor_trader_silk"), #manor walkers
			(is_between, ":cur_troop", "trp_farmer", "trp_kingdom_heroes_including_player_begin"), #manor walkers
			(neg|is_between, ":cur_troop", "trp_ransom_broker_1", "trp_tavern_traveler_1"), #manor walkers
					(val_add, ":num_walkers", 1),
					(agent_get_position, pos1, ":cur_agent"),
			
			(store_random_in_range, ":r", 0, 2),
			(try_begin),
				(eq, ":r", 0),
				(store_random_in_range, ":i_e_p", 20, 72),
			(else_try),
				(store_random_in_range, ":i_e_p", 81, 95),
			(try_end),
			
					#(try_for_range, ":i_e_p", 20, 94),#Entry points
			#  (neg|is_between, ":i_e_p", 73, 81),
						#(entry_point_get_position, pos2, ":i_e_p"),
						#(get_distance_between_positions, ":distance", pos1, pos2),
						#(lt, ":distance", 200),
						(agent_set_slot, ":cur_agent", 0, ":i_e_p"),
				 # (try_end),
					(call_script, "script_set_town_walker_destination", ":cur_agent"),
				(try_end),
		])
	

	# script_tick_manor_walkers
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# Input: none
		# Output: none
tick_manor_walkers = (
	"tick_manor_walkers",
			[
			(try_for_agents, ":cur_agent"),
					(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(this_or_next|is_between, ":cur_troop", walkers_begin, walkers_end),
					(this_or_next|is_between, ":cur_troop", "trp_manor_noble", "trp_manor_trader_silk"), #manor walkers
			(is_between, ":cur_troop", "trp_farmer", "trp_kingdom_heroes_including_player_begin"), #manor walkers
					(agent_get_slot, ":target_entry_point", ":cur_agent", 0),
					(entry_point_get_position, pos1, ":target_entry_point"),
					(try_begin),
						#(lt, ":target_entry_point", 32),
			(this_or_next|is_between, ":target_entry_point", 41, 61), #manor walkers
				(is_between, ":target_entry_point", 80, 95), 
			
						(init_position, pos2),
						(position_set_y, pos2, 250),
						(position_transform_position_to_parent, pos1, pos1, pos2),
					(try_end),
					(agent_get_position, pos2, ":cur_agent"),
					(get_distance_between_positions, ":distance", pos1, pos2),
					(lt, ":distance", 400),
					(assign, ":random_no", 0),
					(try_begin),
						#(lt, ":target_entry_point", 32),
			(this_or_next|is_between, ":target_entry_point", 41, 61), #manor walkers
				(is_between, ":target_entry_point", 80, 95), 
			
						(store_random_in_range, ":random_no", 0, 100),
					(try_end),
					(lt, ":random_no", 20),
					(call_script, "script_set_town_walker_destination", ":cur_agent"),
				(try_end),
		])
	