from header import *

##script_equip_troops_by_tier
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: troop, pool, tier
	# OUTPUT: none
equip_troops_by_tier = (
	"equip_troops_by_tier",
	[
		(store_script_param, ":troop", 1),
			(store_script_param, ":pool", 2),
			(store_script_param, ":tier", 3),
		
		#addjust tier for range and mounted
		(try_begin),
			(this_or_next|eq, ":troop", "trp_welsh_horse_1"), #welsh are poor modded2x: lol
			(troop_is_guarantee_ranged, ":troop"),
			(val_sub, ":tier", 1),
		(else_try),
			(this_or_next|troop_is_guarantee_horse, ":troop"),
			(is_between, ":troop", "trp_balt_noble_recruit", "trp_marinid_village_rabble"), #batl nobility is not mounted
			(neq, ":troop", "trp_tatar_tribesman"),
			(neq, ":troop", "trp_tatar_skirmisher"),
			(neq, ":troop", "trp_tatar_horse_archer"),
			(neq, ":troop", "trp_tatar_veteran_horse_archer"),
			(val_add, ":tier", 1),
		(try_end),		
		#body armor
		(try_begin), # tier_5_body_armor(51)++
			(ge, ":tier", 5),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 51, 200),
			(gt, reg0, 2),
		(else_try), # tier_4_body_armor(41)++
			(ge, ":tier", 4),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 41, 200),
			(gt, reg0, 2),
		(else_try), # tier_2_body_armor(26) - tier_4_body_armor(41)
			(ge, ":tier", 3),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 26, 41),
			(gt, reg0, 2),
		(else_try), # tier_2_body_armor(26) - tier_3_body_armor(33)
			(ge, ":tier", 2),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 26, 33),
			(gt, reg0, 2),
		(else_try),  #tier 1 <tier_2_body_armor(26) 
			#(le, ":tier", 1),
			(call_script, "script_cf_add_troop_items_armor", ":troop", ":pool", 0, 26),
			(try_end),
		##helmet
		(try_begin), # 70+
			(ge, ":tier", 5),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 70, 200),
			(gt, reg0, 2),
		(else_try), # 60 - 70
			(ge, ":tier", 4),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 60, 70),
			(gt, reg0, 2),
		(else_try), # 40-60
			(ge, ":tier", 3),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 50, 60),
			(gt, reg0, 2),
		(else_try), # <40-50
			(ge, ":tier", 2),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 40, 50),
			(gt, reg0, 2),
		(else_try),  #tier 1 <40
			#(le, ":tier", 1),
			(call_script, "script_cf_add_troop_items_helmet", ":troop", ":pool", 0, 40),
			(try_end),
	])
##script_add_item_to_pool
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: item, pool
	# OUTPUT: none
add_item_to_pool =	(
	"add_item_to_pool",
	[
		(store_script_param, ":item_to_add", 1),
			(store_script_param, ":pool", 2),
		
		#get number of items
		(troop_get_slot, ":number", ":pool", 0),
		(val_add, ":number", 1), 
		
		#check if the item is in the pool
		(assign, ":add", 0), 
		(try_for_range, ":slot", 1, ":number"),
			(troop_get_slot, ":item", ":pool", ":slot"),
			(eq, ":item", ":item_to_add"),
			(assign, ":add", 1),
		(try_end),
		(try_begin),
			(eq, ":add", 0),
			#not in the pool, add the item
			(troop_set_slot, ":pool", ":number", ":item_to_add"),
			(troop_set_slot, ":pool", 0, ":number"),
		(try_end),  
	])

	##script_extract_armor_from_tree
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# input: troop, pool
	# output: none
extract_armor_from_tree =	(
	"extract_armor_from_tree",
	[
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		#(store_script_param, ":tier", 3),
		
		(try_begin),
			(gt, ":troop", 0),
			(troop_get_inventory_capacity, ":capacity", ":troop"),
			(try_for_range, ":slot", 0, ":capacity"),
				(troop_get_inventory_slot, ":item", ":troop", ":slot"),
				(gt, ":item", 0),
				(item_get_type, ":type", ":item"),
				(try_begin),
					# (this_or_next|eq, ":type", itp_type_foot_armor),
					# (this_or_next|eq, ":type", itp_type_hand_armor),
					(this_or_next|eq, ":type", itp_type_head_armor),
				(eq, ":type", itp_type_body_armor),
				(call_script, "script_cf_add_item_to_pool", ":item", ":pool"),
				(try_end),
			(try_end),
			(troop_get_upgrade_troop,":upgrade1",":troop", 0),
			(troop_get_upgrade_troop,":upgrade2",":troop", 1),
			(try_begin),
			(gt, ":upgrade1", 0),
			(neq, ":upgrade1", "trp_teu_balt_1"),
			(call_script, "script_extract_armor_from_tree", ":upgrade1", ":pool"),
			(try_end),
			(try_begin),
				(gt, ":upgrade2", 0),
				(neq, ":upgrade2", "trp_teu_balt_1"),
			(call_script, "script_extract_armor_from_tree", ":upgrade2", ":pool"),
			(try_end),
		(try_end),
	])

	##script_fill_pools_by_culture
	##description: initialize culture pools
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: culture, pool_commoner, pool_noble
	# OUTPUT: none
fill_pools_by_culture =	(
	"fill_pools_by_culture",
	[
		(store_script_param, ":culture", 1),
		(store_script_param, ":pool_commoner", 2),
		(store_script_param, ":pool_noble", 3),
		(faction_get_slot, ":village", ":culture",slot_faction_tier_1_troop),
		(faction_get_slot, ":town", ":culture",slot_faction_tier_1_town_troop),
		(faction_get_slot, ":castle", ":culture",slot_faction_tier_1_castle_troop),
		
		(call_script, "script_extract_armor_from_tree", ":village", ":pool_commoner"),
		(call_script, "script_extract_armor_from_tree", ":town", ":pool_commoner"),
		(call_script, "script_extract_armor_from_tree", ":castle", ":pool_noble"),
	])	

	##script_initialize_culture_pools
	##description: initialize culture pools
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	# INPUT: none
	# OUTPUT: none
initialize_culture_pools =	(
	"initialize_culture_pools",
	[
		(try_for_range, ":culture", "fac_culture_finnish", "fac_player_faction"),
			(store_sub, ":adjust", ":culture", "fac_culture_finnish"),
		(store_add, ":commoner_pool", "trp_pool_commoner_finnish", ":adjust"),
		(store_add, ":noble_pool", "trp_pool_noble_finnish", ":adjust"),
		(neq, ":culture", "fac_culture_scotish"),
		(call_script, "script_fill_pools_by_culture", ":culture", ":commoner_pool", ":noble_pool"),
		(try_end),
		##extra pools
		(call_script, "script_extract_armor_from_tree", "trp_teu_balt_1", "trp_pool_teutonic_auxiliary"),
		(call_script, "script_extract_armor_from_tree", "trp_scottish_village_recruit", "trp_pool_commoner_scotish"),
		##extra items for magrebs
		(call_script, "script_add_item_to_pool", "itm_new_turban_a", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_new_turban_a", "trp_pool_noble_marinid"),
		(call_script, "script_add_item_to_pool", "itm_new_turban_b", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_new_turban_b", "trp_pool_noble_marinid"),
		(call_script, "script_add_item_to_pool", "itm_megreb_spangen", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_megreb_spangen", "trp_pool_noble_marinid"),
		(call_script, "script_add_item_to_pool", "itm_berber_white_turban", "trp_pool_commoner_marinid"),
		(call_script, "script_add_item_to_pool", "itm_berber_white_turban", "trp_pool_noble_marinid"),
		##teutonic knights need more cloths
		(call_script, "script_add_item_to_pool", "itm_teu_monk_surcoat_a", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_teu_gambeson", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_liv_sergeant", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_teu_sergeant", "trp_pool_noble_teutonic"),
		(call_script, "script_add_item_to_pool", "itm_teu_hbrother_mail", "trp_pool_noble_teutonic"),
		##merc rebalance
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_spearman", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_guisarmer", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_range", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_euro_horse", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_spearman", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_guisarmer", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_range", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balt_horse", "trp_pool_commoner_baltic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_spearman", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_javalin", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_range", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_mamluke_syrian", "trp_pool_commoner_mamluke"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_maghreb_spearman", "trp_pool_commoner_marinid"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_maghreb_range", "trp_pool_commoner_marinid"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_maghreb_horse", "trp_pool_commoner_marinid"),
		#(call_script, "script_extract_armor_from_tree", "trp_merc_almogabar", "trp_pool_commoner_marinid"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_spearman", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_guisarmer", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_range", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_rus_horse", "trp_pool_commoner_rus"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_spearman", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_guisarmer", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_range", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_horse", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_latin_light", "trp_pool_commoner_iberian"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_spearman", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_guisarmer", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_range", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_balkan_horse", "trp_pool_commoner_balkan"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_spearman", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_guisarmer", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_range", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_scan_horse", "trp_pool_commoner_nordic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_spearman", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_axeman_1", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_spearman_2", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_gaelic_axeman_2", "trp_pool_commoner_gaelic"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_brabantine_spearman", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_brabantine_xbow", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_brabantine_guisarm", "trp_pool_commoner_western"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_foot_archer_1", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_foot_archer_2", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_infantry_1", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_infantry_2", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_horse_archer_1", "trp_pool_sicily_muslims"),
		(call_script, "script_extract_armor_from_tree", "trp_merc_sicily_horse_archer_2", "trp_pool_sicily_muslims"),
		
		(call_script, "script_extract_armor_from_tree", "trp_cuman_tribesman", "trp_pool_cuman"),
		(call_script, "script_extract_armor_from_tree", "trp_cuman_horseman", "trp_pool_cuman"),
		(call_script, "script_extract_armor_from_tree", "trp_goergian_horse_archer", "trp_pool_georgian"),
		(call_script, "script_extract_armor_from_tree", "trp_kwarezmian_range", "trp_pool_kwarezmian"),
		(call_script, "script_extract_armor_from_tree", "trp_kwarezmian_light_horse", "trp_pool_kwarezmian"),
		(call_script, "script_extract_armor_from_tree", "trp_kwarezmian_medium_horse", "trp_pool_kwarezmian"),
		(call_script, "script_extract_armor_from_tree", "trp_mordovian_foot", "trp_pool_mordovian"),
		(call_script, "script_extract_armor_from_tree", "trp_mordovian_range", "trp_pool_mordovian"),
		(call_script, "script_extract_armor_from_tree", "trp_mordovian_horse", "trp_pool_mordovian"),
		(call_script, "script_extract_armor_from_tree", "trp_kipchak_range", "trp_pool_kipchak"),
		(call_script, "script_extract_armor_from_tree", "trp_kipchak_light_horse", "trp_pool_kipchak"),
		(call_script, "script_extract_armor_from_tree", "trp_kipchak_medium_horse", "trp_pool_kipchak"),

		(display_message, "@Cultural troop pools initalized"),
	])	
	


	##script_rebalance_troop_trees
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description: rebalancing system. modded2x: need 2 disable this, /mbg/ folks arent' happy
	# INPUT: troop, pool, tier
	# OUTPUT: none
rebalance_troop_trees =	(
	"rebalance_troop_trees",
	[
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		(store_script_param, ":tier", 3),		
		
		(try_begin),
			(gt, ":troop", 0),
			
			##remove current items
			(try_for_range, ":item", "itm_tutorial_spear", "itm_items_end"),
				(item_get_type, ":type", ":item"),
			(this_or_next|eq, ":type", itp_type_head_armor),
			(eq, ":type", itp_type_body_armor),
				(troop_remove_item, ":troop", ":item"),
			(try_end),
			##add new items from pool by tier
			(call_script, "script_equip_troops_by_tier", ":troop", ":pool", ":tier"),
			(troop_equip_items, ":troop"),
			(val_add, ":tier", 1),
			(troop_get_upgrade_troop,":upgrade1",":troop", 0),
			(troop_get_upgrade_troop,":upgrade2",":troop", 1),
			(try_begin),
			(gt, ":upgrade1", 0),
			(neq, ":upgrade1", "trp_teu_balt_1"),
			(call_script, "script_rebalance_troop_trees", ":upgrade1", ":pool", ":tier"),
			(try_end),
			(try_begin),
				(gt, ":upgrade2", 0),
			(neq, ":upgrade2", "trp_teu_balt_1"),
			(call_script, "script_rebalance_troop_trees", ":upgrade2", ":pool", ":tier"),
			(try_end),
		(try_end),
	])
	
		##script_rebalance_troops_by_culture
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
	##description:
	# INPUT: none
	# OUTPUT: none
rebalance_troops_by_culture =	(
	"rebalance_troops_by_culture",
	[
		(try_for_range, ":culture", "fac_culture_finnish", "fac_player_faction"),
			(store_sub, ":adjust", ":culture", "fac_culture_finnish"),
		(store_add, ":commoner_pool", "trp_pool_commoner_finnish", ":adjust"),
		(store_add, ":noble_pool", "trp_pool_noble_finnish", ":adjust"),
		(neq, ":culture", "fac_culture_scotish"),
			(faction_get_slot, ":village", ":culture",slot_faction_tier_1_troop),
			(faction_get_slot, ":town", ":culture",slot_faction_tier_1_town_troop),
			(faction_get_slot, ":castle", ":culture",slot_faction_tier_1_castle_troop),
		(call_script, "script_rebalance_troop_trees", ":village", ":commoner_pool", 1),
		(call_script, "script_rebalance_troop_trees", ":town", ":commoner_pool", 1),
		(call_script, "script_rebalance_troop_trees", ":castle", ":noble_pool", 1),
		(try_end),
		##extra rebalance
		(call_script, "script_rebalance_troop_trees", "trp_teu_balt_1", "trp_pool_teutonic_auxiliary", 2),
		(call_script, "script_rebalance_troop_trees", "trp_scottish_village_recruit", "trp_pool_commoner_scotish", 1),

		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_spearman", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_guisarmer", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_range", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_euro_horse", "trp_pool_commoner_western", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_spearman", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_guisarmer", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_range", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balt_horse", "trp_pool_commoner_baltic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_spearman", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_javalin", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_range", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_mamluke_syrian", "trp_pool_commoner_mamluke", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_maghreb_spearman", "trp_pool_commoner_marinid", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_maghreb_range", "trp_pool_commoner_marinid", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_maghreb_horse", "trp_pool_commoner_marinid", 3),
		#(call_script, "script_rebalance_troop_trees", "trp_merc_almogabar", "trp_pool_commoner_marinid", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_spearman", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_guisarmer", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_range", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_rus_horse", "trp_pool_commoner_rus", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_spearman", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_guisarmer", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_range", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_horse", "trp_pool_commoner_iberian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_latin_light", "trp_pool_commoner_iberian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_spearman", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_guisarmer", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_range", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_balkan_horse", "trp_pool_commoner_balkan", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_spearman", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_guisarmer", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_range", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_scan_horse", "trp_pool_commoner_nordic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_spearman", "trp_pool_commoner_gaelic", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_axeman_1", "trp_pool_commoner_gaelic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_spearman_2", "trp_pool_commoner_gaelic", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_gaelic_axeman_2", "trp_pool_commoner_gaelic", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_brabantine_spearman", "trp_pool_commoner_western", 4),
		(call_script, "script_rebalance_troop_trees", "trp_merc_brabantine_xbow", "trp_pool_commoner_western", 4),
		(call_script, "script_rebalance_troop_trees", "trp_merc_brabantine_guisarm", "trp_pool_commoner_western", 4),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_foot_archer_1", "trp_pool_sicily_muslims", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_foot_archer_2", "trp_pool_sicily_muslims", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_infantry_1", "trp_pool_sicily_muslims", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_infantry_2", "trp_pool_sicily_muslims", 3),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_horse_archer_1", "trp_pool_sicily_muslims", 2),
		(call_script, "script_rebalance_troop_trees", "trp_merc_sicily_horse_archer_2", "trp_pool_sicily_muslims", 3),
		
		(call_script, "script_rebalance_troop_trees", "trp_cuman_tribesman", "trp_pool_cuman", 1),
		(call_script, "script_rebalance_troop_trees", "trp_cuman_horseman", "trp_pool_cuman", 1),
		(call_script, "script_rebalance_troop_trees", "trp_goergian_horse_archer", "trp_pool_georgian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kwarezmian_range", "trp_pool_kwarezmian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kwarezmian_light_horse", "trp_pool_kwarezmian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kwarezmian_medium_horse", "trp_pool_kwarezmian", 3),
		(call_script, "script_rebalance_troop_trees", "trp_mordovian_foot", "trp_pool_mordovian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_mordovian_range", "trp_pool_mordovian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_mordovian_horse", "trp_pool_mordovian", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kipchak_range", "trp_pool_kipchak", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kipchak_light_horse", "trp_pool_kipchak", 2),
		(call_script, "script_rebalance_troop_trees", "trp_kipchak_medium_horse", "trp_pool_kipchak", 3),
		
		(display_message, "@Troop rebalanced"),
	])
	