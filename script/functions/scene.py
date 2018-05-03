from header import *

#script_game_get_scene_name
	# This script is called from the game engine when a name for the scene is needed.
	# INPUT: arg1 = scene_no
	# OUTPUT: s0 = name
game_get_scene_name =	("game_get_scene_name",
		[
			(store_script_param, ":scene_no", 1),
			(try_begin),
				(is_between, ":scene_no", multiplayer_scenes_begin, multiplayer_scenes_end),
				(store_sub, ":string_id", ":scene_no", multiplayer_scenes_begin),
				(val_add, ":string_id", multiplayer_scene_names_begin),
				(str_store_string, s0, ":string_id"),
			(try_end),
	])

#script_game_get_mission_template_name
	# This script is called from the game engine when a name for the mission template is needed.
	# INPUT: arg1 = mission_template_no
	# OUTPUT: s0 = name
game_get_mission_template_name = (
	"game_get_mission_template_name",
		[
			(store_script_param, ":mission_template_no", 1),
			(call_script, "script_multiplayer_get_mission_template_game_type", ":mission_template_no"),
			(assign, ":game_type", reg0),
			(try_begin),
				(is_between, ":game_type", 0, multiplayer_num_game_types),
				(store_add, ":string_id", ":game_type", multiplayer_game_type_names_begin),
				(str_store_string, s0, ":string_id"),
			(try_end),
	])

#script_get_meeting_scene:
		# INPUT: none
		# OUTPUT: reg0 contain suitable scene_no
		
get_meeting_scene =	(
	"get_meeting_scene",
			[
				(party_get_current_terrain, ":terrain_type", "p_main_party"),
				(assign, ":scene_to_use", "scn_random_scene"),
				(try_begin),
					(eq, ":terrain_type", rt_steppe),
					(assign, ":scene_to_use", "scn_meeting_scene_steppe"),
				(else_try),
					(eq, ":terrain_type", rt_plain),
					(assign, ":scene_to_use", "scn_meeting_scene_plain"),
				(else_try),
					(eq, ":terrain_type", rt_snow),
					(assign, ":scene_to_use", "scn_meeting_scene_snow"),
				(else_try),
					(eq, ":terrain_type", rt_desert),
					(assign, ":scene_to_use", "scn_meeting_scene_desert"),
				(else_try),
					(eq, ":terrain_type", rt_steppe_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_steppe"),
				(else_try),
					(eq, ":terrain_type", rt_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_plain"),
				(else_try),
					(eq, ":terrain_type", rt_snow_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_snow"),
				(else_try),
					(eq, ":terrain_type", rt_desert_forest),
					(assign, ":scene_to_use", "scn_meeting_scene_desert"),
				(else_try),
					(call_script, "script_cf_is_party_on_water", "p_main_party"),
					(assign, ":scene_to_use", "scn_meeting_scene_sea"),
				(else_try),
					(assign, ":scene_to_use", "scn_meeting_scene_plain"),
				(try_end),
				(assign, reg0, ":scene_to_use"),
		])
		
		
		
		# script_cf_center_get_free_walker
		# Input: arg1 = center_no
		# Output: reg0 = walker no (can fail)
cf_center_get_free_walker = (
	"cf_center_get_free_walker",
			[
				(store_script_param, ":center_no", 1),
				(assign, ":num_free_walkers", 0),
				(try_for_range, ":walker_no", 0, num_town_walkers),
					(store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
					(party_slot_eq, ":center_no", ":type_slot", walkert_default),
					(val_add, ":num_free_walkers", 1),
				(try_end),
				(gt, ":num_free_walkers", 0),
				(assign, reg0, -1),
				(store_random_in_range, ":random_rank", 0, ":num_free_walkers"),
				(try_for_range, ":walker_no", 0, num_town_walkers),
					(store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
					(party_slot_eq, ":center_no", ":type_slot", walkert_default),
					(val_sub, ":num_free_walkers", 1),
					(eq, ":num_free_walkers", ":random_rank"),
					(assign, reg0, ":walker_no"),
				(try_end),
		])
		
		# script_center_remove_walker_type_from_walkers
		# Input: arg1 = center_no, arg2 = walker_type,
		# Output: reg0 = 1 if comment found, 0 otherwise; s61 will contain comment string if found
center_remove_walker_type_from_walkers = (
	"center_remove_walker_type_from_walkers",
			[
				(store_script_param, ":center_no", 1),
				(store_script_param, ":walker_type", 2),
				(try_for_range, ":walker_no", 0, num_town_walkers),
					(store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
					(party_slot_eq, ":center_no", ":type_slot", ":walker_type"),
					(call_script, "script_center_set_walker_to_type", ":center_no", ":walker_no", walkert_default),
				(try_end),
		])
		

		# script_agent_get_town_walker_details
		# This script assumes this is one of town walkers.
		# Input: agent_id
		# Output: reg0: town_walker_type, reg1: town_walker_dna
agent_get_town_walker_details = (
	"agent_get_town_walker_details",
			[(store_script_param, ":agent_no", 1),
				(agent_get_entry_no, ":entry_no", ":agent_no"),
				(store_sub, ":walker_no", ":entry_no", town_walker_entries_start),
				
				(store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
				(party_get_slot, ":walker_type", "$current_town", ":type_slot"),
				(store_add, ":dna_slot", slot_center_walker_0_dna,  ":walker_no"),
				(party_get_slot, ":walker_dna", "$current_town", ":dna_slot"),
				(assign, reg0, ":walker_type"),
				(assign, reg1, ":walker_dna"),
				(assign, reg2, ":walker_no"),
		])
		
		#script_town_walker_occupation_string_to_s14
		# WARNING: this is totally new procedure (not present in native). 1257AD devs
		# INPUT : agent_no
		# OUTPUT : s14
town_walker_occupation_string_to_s14 = (
	"town_walker_occupation_string_to_s14",
			[
				(store_script_param, ":agent_no", 1),
				
				#Cairo, approx 1799:
				#adult males = 114,000
				#military, 10,400
				#civil, including religious 5,000
				#commerce 3,500
				#merchants 4,500
				#coffee shops, 1,500 (maybe broaden to inns and taverns)
				#artisans 21,800
				#workmen 4,300
				#itinerants 8,600
				#servants (inc water carriers) 26,400
				(assign, ":check_for_good_price", 0),
				(str_store_string, s14, "str_i_take_what_work_i_can_sirmadame_i_carry_water_or_help_the_merchants_with_their_loads_or_help_build_things_if_theres_things_to_be_built"),
				
				(call_script, "script_agent_get_town_walker_details", ":agent_no"),
				(assign, ":type", reg0),
				(assign, ":walker_dna", reg1),
				
				(assign, ":item", -1),
				(assign, ":total_item_production", 0),
				(try_for_range, ":trade_good", trade_goods_begin, trade_goods_end),
					(call_script, "script_center_get_production", "$g_encountered_party", ":trade_good"),
					(val_add, ":total_item_production", reg0),
				(try_end),
				
				(val_max, ":total_item_production", 1),
				
				(store_mod, ":semi_random_number", ":walker_dna", ":total_item_production"),
				
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(assign, reg4, ":walker_dna"),
					(assign, reg5, ":total_item_production"),
					(assign, reg7, ":semi_random_number"),
					(display_message, "str_dna_reg4_total_production_reg5_modula_reg7"),
				(try_end),
				
				(try_for_range, ":trade_good", trade_goods_begin, trade_goods_end),
					(gt, ":semi_random_number", -1),
					(call_script, "script_center_get_production", "$g_encountered_party", ":trade_good"),
					(val_sub, ":semi_random_number", reg0),
					(lt, ":semi_random_number", 0),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_item_name, s9, ":trade_good"),
						(display_message, "str_agent_produces_s9"),
					(try_end),
					(assign, ":item", ":trade_good"),
				(try_end),
				
				
				(try_begin),
					(eq, ":type", walkert_needs_money),
					(is_between, "$g_encountered_party", towns_begin, towns_end),
					(str_store_string, s14, "str_im_not_doing_anything_sirmadame_theres_no_work_to_be_had_around_here_these_days"),
				(else_try),
					(eq, ":type", walkert_needs_money),
					(str_store_string, s14, "str_im_not_doing_anything_sirmadame_i_have_no_land_of_my_own_and_theres_no_work_to_be_had_around_here_these_days"),
				(else_try),
					(eq, ":type", walkert_needs_money_helped),
					(str_store_string, s14, "str_why_im_still_living_off_of_your_kindness_and_goodness_sirmadame_hopefully_there_will_be_work_shortly"),
				(else_try),
					(eq, ":item", "itm_grain"),
					(is_between, "$g_encountered_party", towns_begin, towns_end),
					(str_store_string, s14, "str_i_work_in_the_fields_just_outside_the_walls_where_they_grow_grain_we_dont_quite_grow_enough_to_meet_our_needs_though_and_have_to_import_grain_from_the_surrounding_countryside"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_grain"),
					(str_store_string, s14, "str_i_work_mostly_in_the_fields_growing_grain_in_the_town_they_grind_it_to_make_bread_or_ale_and_we_can_also_boil_it_as_a_porridge"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_ale"),
					(str_store_string, s14, "str_i_work_in_the_breweries_making_ale_the_poor_folk_drink_a_lot_of_it_as_its_cheaper_than_wine_we_make_it_with_grain_brought_in_from_the_countryside"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_bread"),
					(str_store_string, s14, "str_i_work_in_a_mill_grinding_flour_to_make_bread_bread_is_cheap_keeps_well_and_fills_the_stomach"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_dried_meat"),
					(str_store_string, s14, "str_i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_cheese"),
					(str_store_string, s14, "str_i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk_so_it_doesnt_spoil"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_butter"),
					(str_store_string, s14, "str_i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk_so_it_doesnt_spoil"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_wool"),
					(str_store_string, s14, "str_i_tend_sheep_we_send_the_wool_to_the_cities_to_be_woven_into_cloth_and_make_mutton_sausage_when_we_cull_the_herds"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_sausages"),
					(str_store_string, s14, "str_i_tend_sheep_we_send_the_wool_to_the_cities_to_be_woven_into_cloth_and_make_mutton_sausage_when_we_cull_the_herds"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_wool_cloth"),
					(str_store_string, s14, "str_i_work_at_a_loom_spinning_cloth_from_wool_wool_is_some_of_the_cheapest_cloth_you_can_buy_but_it_will_still_keep_you_warm"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_smoked_fish"),
					(str_store_string, s14, "str_i_crew_a_fishing_boat_we_salt_and_smoke_the_flesh_to_sell_it_far_inland"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_salt"),
					(str_store_string, s14, "str_i_sift_salt_from_a_nearby_flat_they_need_salt_everywhere_to_preserve_meat_and_fish"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_iron"),
					(str_store_string, s14, "str_i_mine_iron_from_a_vein_in_a_nearby_cliffside_they_use_it_to_make_tools_arms_and_other_goods"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_pottery"),
					(str_store_string, s14, "str_i_make_pottery_which_people_use_to_store_grain_and_carry_water"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_tools"),
					(str_store_string, s14, "str_trade_explanation_tools"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_oil"),
					(str_store_string, s14, "str_trade_explanation_oil"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_linen"),
					(str_store_string, s14, "str_trade_explanation_linen"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_velvet"),
					(str_store_string, s14, "str_trade_explanation_velvet"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_spice"),
					(str_store_string, s14, "str_trade_explanation_spice"),
					(assign, ":check_for_good_price", 1),
					
				(else_try),
					(eq, ":item", "itm_apples"),
					(str_store_string, s14, "str_trade_explanation_apples"),
					(assign, ":check_for_good_price", 1),
					
				(try_end),
				
				
				(try_begin),
					(eq, ":check_for_good_price", 1),
					
					(assign, ":trade_destination", -1),
					(store_skill_level, ":trade_skill", "skl_trade", "trp_player"),
					
					(try_begin),
						(is_between, "$g_encountered_party", villages_begin, villages_end),
						(party_get_slot, ":trade_town", "$g_encountered_party", slot_village_market_town),
					(else_try),
						(assign, ":trade_town", "$g_encountered_party"),
					(try_end),
					
					(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
					(store_add, ":cur_good_price_slot", ":item", ":item_to_price_slot"),
					(party_get_slot, ":score_to_beat", ":trade_town", ":cur_good_price_slot"),
					(val_add, ":score_to_beat", 400),
					(store_mul, ":deduction_for_trade_skill", ":trade_skill", 35),
					(try_begin),
						(is_between, "$g_encountered_party", villages_begin, villages_end),
						(val_add, ":score_to_beat", 200),
					(try_end),
					(val_sub, ":score_to_beat", ":deduction_for_trade_skill"),
					
					(try_for_range, ":trade_route_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
						(party_get_slot, ":other_town", ":trade_town", ":trade_route_slot"),
						(party_get_slot, ":price_in_other_town", ":other_town", ":cur_good_price_slot"),
						
						
						(try_begin),
							(eq, "$cheat_mode", 1),
							(assign, reg4, ":price_in_other_town"),
							(assign, reg5, ":score_to_beat"),
							(str_store_party_name, s10, ":other_town"),
							(display_message, "str_s10_has_reg4_needs_reg5"),
						(try_end),
						
						(gt, ":price_in_other_town", ":score_to_beat"),
						
						(assign, ":trade_destination", ":other_town"),
						(assign, ":score_to_beat", ":price_in_other_town"),
					(try_end),
					
					(is_between, ":trade_destination", centers_begin, centers_end),
					
					(str_store_party_name, s15, ":trade_destination"),
					(str_store_string, s14, "str_s14_i_hear_that_you_can_find_a_good_price_for_it_in_s15"),
					
					#Reasons -- raw material
					#Reason -- road cut
					#Reason -- villages looted
					
				(try_end),
				
				
		])

