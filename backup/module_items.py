# -*- coding: utf-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

hai = 1

#weight = 0.018 * length
#speed = 15665.5/(weight * length)

def get_w_weight(length):
  weight = 0.018 * length
  return weight

def get_axe_weight(length):
  weight = 0.025 * length
  return weight

def get_mace_weight(length):
  weight = 0.022 * length
  return weight

def get_1hmace_speed(length):
  weight = get_mace_weight (length)
  speed = 100 - (weight*weight*weight)
  return (int) (round(speed))

def get_1haxe_speed(length):
  weight = get_axe_weight (length)
  speed = 100 - (weight*weight*weight)
  return (int) (round(speed))

def get_2haxe_speed(length):
  weight = get_axe_weight (length)
  speed = 99 - (weight*weight*weight)
  return (int) (round(speed))

def get_1hw_speed(length):
  weight = get_w_weight (length)
  speed = 103 - (weight*weight*weight)
  return (int) (round(speed))

def get_2hw_speed(length):
  weight = get_w_weight (length)
  speed = 99 - (weight*weight*weight)
  return (int) (round(speed))

def get_polew_speed(length):
  weight = get_w_weight (length)
  speed = 96 - (weight*weight*weight)
  return (int) (round(speed))

def get_w_price (length, weight, speed, damage_cut, damage_thrust):

  if damage_cut > damage_thrust:
    damage = damage_cut
  if damage_thrust > damage_cut:
    damage = damage_thrust
  price = (damage) * speed * length * length / (weight * 100)
  price = price * price
  price = price /10000000
  return (int) (round(price))

def get_barmour_price (weight, body_a, leg_a):
  #new_weight = weight ** 0.5
  price = 3*(body_a + leg_a)*(body_a + leg_a)/2#/new_weight
  if body_a < 30:
    price = price - price/3 
  if body_a >= 30 and body_a < 50:
    price = price - price/5
  if body_a < 35: #tom reduce - basic armor should be almost free
	price = price/3	
  return (int) (round(price))
 
# def tier_6_body_armor_price:
  # price = get_barmour_price(25, 72, 31)
  # return price
  
def get_footwear_price (armour):
  price = armour * 72
  if armour < 10:
    price = price - price/3
  return (int(round(price)))
  
def get_headgear_price (armour):
  price = armour ** 2
  if armour < 25:
    price = price - price/3
  return (int(round(price)))

def get_gloves_price (armour):
  price = 10 * armour ** 2
  return (int(round(price)))

def get_shield_price (armour, width, height):
  if height == 0:
    width = width/2
    area = 3.14 * width * width
  else:
    area = width * height
  price = area * area * area * armour * armour * armour
  price = price / 10000000000000
  price = price * 2
  
  if armour < 71:
    price = price / 3
  elif armour < 76:
    price = price /2
  elif armour > 80:
    price = price * 1.5
  return (int(round(price)))
  
# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

imodbits_missile_mon = imodbit_bent

warhorse_price = 3800
warhorse_hp = 120 #was 85
warhorse_armour = 45
warhorse_speed = 38 #was 38
warhorse_maneuver = 40
warhorse_charge = 38
warhorse_scale = 110
warhorse_abundance = 10
horse_hp = 65

bastard_abundance = 100

shield_t1_res = 48
shield_t2_res = 55
shield_t3_res = 61
shield_t4_res = 67

tier_0_body_armor_price = get_barmour_price(6,17,7)
tier_0_body_armor = weight(6)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(1)

tier_1_body_armor_price = get_barmour_price(11,21,10)
tier_1_body_armor = weight(11)|abundance(50)|head_armor(0)|body_armor(21)|leg_armor(10)|difficulty(3)

tier_2_body_armor_price = get_barmour_price(14,26,12)
tier_2_body_armor = weight(14)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(12)|difficulty(5)

tier_3_body_armor_price = get_barmour_price(18,33,14)
tier_3_body_armor = weight(18)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(14)|difficulty(8)

tier_4_body_armor_price = get_barmour_price(21,41,17)
tier_4_body_armor = weight(21)|abundance(80)|head_armor(0)|body_armor(41)|leg_armor(17)|difficulty(9)

tier_5_body_armor_price = get_barmour_price(26,51,20)
tier_5_body_armor = weight(26)|abundance(60)|body_armor(51)|leg_armor(20)|difficulty(10)

tier_6_body_armor_price = get_barmour_price(31,64,24)
tier_6_body_armor = weight(31)|abundance(40)|body_armor(64)|leg_armor(24)|difficulty(12)

tier_7_body_armor_price = get_barmour_price(36, 80, 29)
tier_7_body_armor = weight(36)|abundance(10)|head_armor(0)|body_armor(80)|leg_armor(29)|difficulty(14)

tier_arena_armor = weight(26)|abundance(60)|body_armor(51)|leg_armor(20)|difficulty(3)
#tier_6_body_armor_price = 2800

#crown, linen coif
head_armor_no_price = get_headgear_price(2)
head_armor_no = weight(0.5)|abundance(30)|head_armor(4)

#fur hats, head wrapings
head_armor_hat_price = get_headgear_price(8)
head_armor_hat = weight(0.5)|abundance(60)|head_armor(8)

#padded hat
head_armor_light_price = get_headgear_price(20)
head_armor_light = weight(1)|abundance(80)|head_armor(20)

#a peasant helmet
head_armor_average_price = get_headgear_price(40)
head_armor_average = weight(1.5)|abundance(100)|head_armor(40)

#a decent peasant helmet - kettlehat
head_armor_decent_price = get_headgear_price(50)
head_armor_decent = weight(1.8)|abundance(80)|head_armor(50)

#proper good helmet
head_armor_proper_price = get_headgear_price(60)
head_armor_proper = weight(2)|abundance(80)|head_armor(60)

#good helmet, covering face - slonim, old great helmets
head_armor_hevy_price = get_headgear_price(70)
head_armor_hevy = weight(2.5)|abundance(60)|head_armor(70)

#bucket
head_armor_full_price = get_headgear_price(90)
head_armor_full = weight(3)|abundance(30)|head_armor(90)



# mongol_factions = [fac_kingdom_3, fac_kingdom_27]
# euro_factions = [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
# eastern_factions = [fac_kingdom_8, fac_kingdom_15, fac_kingdom_26, fac_kingdom_29, fac_kingdom_30]
# byzantine_factions = [ fac_kingdom_22 ]
# iberian_factions = [ fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]
# italy_factions = [ fac_papacy, fac_kingdom_24, fac_kingdom_32, fac_kingdom_38, fac_kingdom_39, fac_kingdom_40, fac_kingdom_41]
# balt_factions = [ fac_kingdom_2, fac_kingdom_33 ]
# nordic_factions = [fac_kingdom_4, fac_kingdom_11, fac_kingdom_14]
# gaelic_factions = [fac_kingdom_12, fac_kingdom_13, fac_kingdom_37]
# berber_factions = [fac_kingdom_28, fac_kingdom_31]
# andalusian_factions = berber_factions + [fac_kingdom_20]
# mamluk_factions = [fac_kingdom_25]
# arab_factions = andalusian_factions + mamluk_factions
# latin_factions = iberian_factions + italy_factions
# all_euro_factions = euro_factions + [fac_kingdom_23] + iberian_factions + [fac_kingdom_26] #+ nordic_factions
##new
mongol_factions = [fac_culture_mongol]
euro_factions = [fac_culture_mazovian, fac_culture_teutonic,  fac_culture_western]
eastern_factions = [fac_culture_rus]
byzantine_factions = [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]
iberian_factions = [fac_culture_iberian]
italy_factions = [fac_culture_italian, fac_culture_anatolian_christian]
balt_factions = [fac_culture_mazovian, fac_culture_baltic]
nordic_factions = [fac_culture_finnish, fac_culture_nordic]
gaelic_factions = [ fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]
berber_factions = [fac_culture_marinid]
andalusian_factions = [fac_culture_andalus]
mamluk_factions = [fac_culture_mamluke, fac_culture_anatolian]
arab_factions = andalusian_factions + mamluk_factions
latin_factions = iberian_factions + italy_factions
all_euro_factions = euro_factions + latin_factions + nordic_factions

## CC
missile_distance_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter_agent"),
      
      #(eq, "$g_report_shot distance", 1),
      (get_player_agent_no, ":player_agent"),
      (try_begin),
        (eq, ":shooter_agent", ":player_agent"),
        (agent_get_position, pos2, ":shooter_agent"),
        (agent_get_horse, ":horse_agent", ":player_agent"),
        (try_begin),
          (gt, ":horse_agent", -1),
          (position_move_z, pos2, 220),
        (else_try),
          (position_move_z, pos2, 150),
        (try_end),
        (get_distance_between_positions, ":distance", pos1, pos2),
        (store_div, reg61, ":distance", 100),
        (store_mod, reg62, ":distance", 100),
        (try_begin),
          (lt, reg62, 10),
          (str_store_string, s1, "@{reg61}.0{reg62}"),
        (else_try),
          (str_store_string, s1, "@{reg61}.{reg62}"),
        (try_end),
        (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC),
      (try_end),
    ])]
       
## CC
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive)
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile,missile_distance_trigger],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile,missile_distance_trigger],
 ["tutorial_short_bow", "Self Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile,missile_distance_trigger],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile,missile_distance_trigger],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile,missile_distance_trigger],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile,missile_distance_trigger],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile,missile_distance_trigger],
 ["practice_boots", "Practice Boots", [("woolen_hose_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],

 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50*3),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30*3),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30*3),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40*3),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50*3),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50*3),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50*3),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10*3),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10*3),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50*3),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],


 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],



# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.

 # HORSES BEGIN
 #["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
 ["sumpter_horse","Packhorse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(horse_hp)|body_armor(17)|difficulty(1)|horse_speed(40)|horse_maneuver(43)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],

 #["saddle_horse","Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(41)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["saddle_horse","Rouncey", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(horse_hp)|body_armor(14)|difficulty(1)|horse_speed(42)|horse_maneuver(46)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(horse_hp)|body_armor(15)|difficulty(2)|horse_speed(44)|horse_maneuver(51)|horse_charge(8)|horse_scale(90),imodbits_horse_basic, [], mongol_factions],
 ["arabian_horse_a","Arabian Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(horse_hp)|body_armor(15)|difficulty(2)|horse_speed(48)|horse_maneuver(45)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], arab_factions],
 ["courser","Palfrey", [("courser",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(12)|hit_points(horse_hp)|difficulty(2)|horse_speed(48)|horse_maneuver(47)|horse_charge(22)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Arabian Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(80)|hit_points(horse_hp)|body_armor(15)|difficulty(3)|horse_speed(44)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], arab_factions],
 #["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["hunter","Courser", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(horse_hp)|body_armor(18)|difficulty(3)|horse_speed(45)|horse_maneuver(46)|horse_charge(28)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
["warhorse", "War Horse", [("warhorse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_white", "Barded Destrier", [("covered_horse_white", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_red", "Barded Destrier", [("covered_horse_red", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_blue", "Barded Destrier", [("covered_horse_blue", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_yellow", "Barded Destrier", [("covered_horse_yellow", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_player", "Custom Barded Destrier", [("covered_horse_player", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_lionel", "Barded Destrier", [("covered_horse_lionel", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_lethwin", "Barded Destrier", [("covered_horse_lethwin", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_01", "Caparisoned Destrier", [("rnd_horse_01", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_02", "Caparisoned Destrier", [("rnd_horse_02", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_03", "Caparisoned Destrier", [("rnd_horse_03", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_04", "Caparisoned Destrier", [("rnd_horse_04", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_05", "Caparisoned Destrier", [("rnd_horse_05", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_06", "Caparisoned Destrier", [("rnd_horse_06", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_07", "Caparisoned Destrier", [("rnd_horse_07", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_08", "Caparisoned Destrier", [("rnd_horse_08", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_09", "Caparisoned Destrier", [("rnd_horse_09", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_10", "Caparisoned Destrier", [("rnd_horse_10", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_11", "Caparisoned Destrier", [("rnd_horse_11", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_12", "Caparisoned Destrier", [("rnd_horse_12", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_13", "Caparisoned Destrier", [("rnd_horse_13", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_14", "Caparisoned Destrier", [("rnd_horse_14", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_15", "Caparisoned Destrier", [("rnd_horse_15", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_16", "Caparisoned Destrier", [("rnd_horse_16", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_17", "Caparisoned Destrier", [("rnd_horse_17", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_18", "Caparisoned Destrier", [("rnd_horse_18", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_19", "Caparisoned Destrier", [("rnd_horse_19", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_20", "Caparisoned Destrier", [("rnd_horse_20", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_21", "Caparisoned Destrier", [("rnd_horse_21", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_22", "Caparisoned Destrier", [("rnd_horse_22", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["rnd_horse_23", "Caparisoned Destrier", [("rnd_horse_23", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["warhorse_denmark_a", "Danish Destrier", [("warhorse_denmark_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_4]],

  ["warhorse_england_a", "English Destrier", [("warhorse_england_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_devalence", "English Destrier", [("warhorse_devalence", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_demontfort", "English Destrier", [("warhorse_demontfort", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_mortimer", "English Destrier", [("warhorse_mortimer", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_bigod", "English Destrier", [("warhorse_bigod", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_dewarenne", "English Destrier", [("warhorse_dewarenne", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_france_a", "French Destrier", [("warhorse_france_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_9]],

  ["warhorse_hre_a", "HRE Destrier", [("warhorse_hre_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_6]],

  ["warhorse_bohemia", "Bohemian Destrier", [("warhorse_bohemia", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_6]],

  ["warhorse_hungary_a", "Hungarian Destrier", [("warhorse_hungary_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_7]],

  ["warhorse_ireland_a", "Irish Destrier", [("warhorse_gaelic", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_13]],

  ["warhorse_lithuania_a", "Lithuanian Destrier", [("warhorse_lithuania_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_2]],

  ["warhorse_norway_a", "Norwegian Destrier", [("warhorse_norway_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_11]],

  ["warhorse_novgorod_a", "Novgorod Destrier", [("warhorse_novgorod_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_8]],

  ["warhorse_scotland_a", "Scottish Destrier", [("warhorse_scotland_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_12]],

  ["warhorse_sweden_a", "Swedish Destrier", [("warhorse_sweden_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_14]],

  ["warhorse_przemysl2", "Polish Destrier", [("warhorse_przemysl2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_czersk", "Polish Destrier", [("warhorse_czersk", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_slask_a", "Caparisoned Destrier", [("warhorse_slask_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_siemowit_a", "Caparisoned Destrier", [("warhorse_siemowit_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_poland_a", "Polish Destrier", [("warhorse_poland_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_poland_b", "Polish Destrier", [("warhorse_poland_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_kaliskie_a", "Welsh Destrier", [("warhorse_kaliskie_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(25)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_welsh]],

  ["warhorse_gslask", "Polish Destrier", [("warhorse_gslask", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_swietopelk", "Polish Destrier", [("warhorse_swietopelk", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_pol_a", "Polish Destrier", [("warhorse_pol_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_pol_b", "Polish Destrier", [("warhorse_pol_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_pol_c", "Polish Destrier", [("warhorse_pol_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_pol_d", "Polish Destrier", [("warhorse_pol_d", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_pol_e", "Polish Destrier", [("warhorse_pol_e", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_pol_g", "Polish Destrier", [("warhorse_pol_g", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["warhorse_swidnica", "Polish Destrier", [("warhorse_swidnica", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_5]],

  ["teu_warhorse_c", "Teutonic Destrier", [("teu_war_horse_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_1]],

  ["teu_warhorse_b", "Teutonic Destrier", [("teu_war_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_1]],

  ["teu_warhorse_a", "Teutonic Destrier", [("teu_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_1]],

  ["mon_lamellar_horse_a", "Lamellar Destrier", [("warhorse_lamellar_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],
  
  ["mon_lamellar_horse_b", "Lamellar Destrier", [("warhorse_lamellar_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

  ["mon_lamellar_horse_c", "Lamellar Destrier", [("warhorse_lamellar_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

  ["kau_montcada_horse", "Montcada Destrier", [("kau_montcada_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_alego_horse", "Alego Destrier", [("kau_alego_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_cervello_horse", "Cervello Destrier", [("kau_cervello_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_cruilles_horse", "Cruilles Destrier", [("kau_cruilles_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_epyres_horse", "Epyres Destrier", [("kau_epyres_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_luna_horse", "Luna Destrier", [("kau_luna_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_reino_horse", "Reino Destrier", [("kau_reino_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["kau_urgell_horse", "Urgell Destrier", [("kau_urgell_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_iberian]],

  ["templar_warhorse_a", "Caparisoned Destrier", [("templar_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

  ["hospitaller_warhorse_a", "Caparisoned Destrier", [("hospitaller_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

  ["hospitaller_warhorse_b", "Caparisoned Destrier", [("hospitaller_war_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

  ["warhorse_sarranid", "Lamellar War Horse", [("warhorse_sarranid", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["warhorse_steppe", "Lamellar War Horse", [("warhorse_steppe", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mongol]],

  ["byz_warhorse", "Lamellar War Horse", [("byz_warhorse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 5400, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(60)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["jerusalem_horse", "Caparisoned Destrier", [("jerusalem_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

  ["tripoli_horse", "Caparisoned Destrier", [("tripoli_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_23]],

  ["portugal_horse", "Caparisoned Destrier", [("portugal_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_16]],

  ["castile_horse", "Caparisoned Destrier", [("castile_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_18]],

  #["camel","Camel", [("camel",0)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(50)|body_armor(14)|difficulty(1)|horse_speed(19)|horse_maneuver(46)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
  # HORSES END
  ["arrows", "Arrows", [("vik_arrow", imodbits_none), ("vik_arrow", ixmesh_flying_ammo), ("vik_quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 200, thrust_damage(24, cut)|max_ammo(60)|abundance(100)|weight(3.0)|weapon_length(96), imodbit_large_bag, 
    missile_distance_trigger
  ],

  ["khergit_arrows", "War Arrows", [("vik_arrow_b", imodbits_none), ("vik_arrow_b", ixmesh_flying_ammo), ("vik_quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 600, thrust_damage(28, cut)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(96), imodbit_large_bag, [], [fac_culture_mongol]],

  ["barbed_arrows", "Barbed Arrows", [("vik_barbed_arrow", imodbits_none), ("vik_barbed_arrow", ixmesh_flying_ammo), ("vik_quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 400, thrust_damage(26, cut)|max_ammo(60)|abundance(75)|weight(3.0)|weapon_length(92), imodbit_large_bag, 
    missile_distance_trigger
  ],

  ["bodkin_arrows", "Bodkin Arrows", [("vik_piercing_arrow", imodbits_none), ("vik_piercing_arrow", ixmesh_flying_ammo), ("vik_quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 600, thrust_damage(28, pierce)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(92), imodbit_large_bag],

  ["bolts", "Bolts", [("vik_bolt", imodbits_none), ("vik_bolt", ixmesh_flying_ammo), ("vik_bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 300, thrust_damage(25, pierce)|max_ammo(29)|abundance(100)|weight(1.5)|weapon_length(63), imodbit_large_bag, 
    missile_distance_trigger
  ],

  ["strely", "Munitions Arrows", [("vik_munitions_arrow", imodbits_none), ("vik_munitions_arrow", ixmesh_flying_ammo), ("vik_arena_quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 100, thrust_damage(22, cut)|max_ammo(60)|abundance(100)|weight(3.0)|weapon_length(96), imodbit_large_bag],

 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],

# ["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
# ["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["pilgrim_disguise", "Pilgrim Disguise", [("peasant_man_a",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("hood_new",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


### modded2x begin, item by anon modded 1257
  ["kettle_helm_with_mail_coif", "Kettle Helm with Mail Coif", [("kettlehat1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["kettle_helm_with_padding0", "Kettle Helm with Padding", [("kettlehat_c_green", imodbits_none), ("inv_kettlehat_c_green", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["kettle_helm_with_padding1", "Kettle Helm with Padding", [("chapel-de-fer_cloth3", imodbits_none), ("inv_chapel-de-fer_cloth3", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

  ["kettle_helm_with_padding2", "Kettle Helm with Padding", [("chapel-de-fer_cloth2", imodbits_none), ("inv_chapel-de-fer_cloth2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

  ["kettle_helm_with_padding3", "Kettle Helm with Padding", [("chapel-de-fer_cloth1", imodbits_none), ("inv_chapel-de-fer_cloth1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

  ["surcoat_over_mail_haubergeon0", "Surcoat over Mail Haubergeon", [("rnd_surcoat2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon1", "Surcoat over Mail Haubergeon", [("rnd_surcoat3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon2", "Surcoat over Mail Haubergeon", [("rnd_surcoat4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon3", "Surcoat over Mail Haubergeon", [("rnd_surcoat5", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon4", "Surcoat over Mail Haubergeon", [("rnd_surcoat6", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon5", "Surcoat over Mail Haubergeon", [("rnd_surcoat7", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon6", "Surcoat over Mail Haubergeon", [("rnd_surcoat8", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon7", "Surcoat over Mail Haubergeon", [("rnd_surcoat9", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon8", "Surcoat over Mail Haubergeon", [("rnd_surcoat10", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon9", "Surcoat over Mail Haubergeon", [("rnd_surcoat11", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon10", "Surcoat over Mail Haubergeon", [("rnd_surcoat12", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon11", "Surcoat over Mail Haubergeon", [("rnd_surcoat_02_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon12", "Surcoat over Mail Haubergeon", [("rnd_surcoat_03_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon13", "Surcoat over Mail Haubergeon", [("rnd_surcoat_06_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon14", "Surcoat over Mail Haubergeon", [("rnd_surcoat_13_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon15", "Surcoat over Mail Haubergeon", [("rnd_surcoat_14_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon16", "Surcoat over Mail Haubergeon", [("rnd_surcoat_17_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["surcoat_over_mail_haubergeon17", "Surcoat over Mail Haubergeon", [("rnd_surcoat_19_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],


  ["shillelagh", "Shillelagh", [("long_stick", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 300, thrust_damage(24, blunt)|hit_points(27648)|spd_rtng(78)|abundance(100)|weight(3.0)|swing_damage(24, blunt)|difficulty(6)|weapon_length(101), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_gaelic, fac_kingdom_13]],

  ["templar_surcoat_over_mail_haubergeon", "Templar Surcoat over Mail Haubergeon", [("Chinese_Hochmeister", imodbits_none), ("Chinese_Templar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_western]],

  ["billhook_fork", "Billhook-fork", [("1429_bill_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["billhook_fork2", "Billhook-fork", [("1429_glaive_fork", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

  ["cleaving_voulge", "Cleaving Voulge", [("1429_voulge_6", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_poleaxe, 400, thrust_damage(45, cut)|hit_points(14029)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(152), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["fauchard", "Fauchard", [("1429_fauchard_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_no_blur, itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(28672)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(186), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["broken_spear", "Broken Spear", [("vik_broken_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 15, thrust_damage(20, cut)|hit_points(33792)|spd_rtng(100)|abundance(100)|weight(1.0)|swing_damage(15, blunt)|weapon_length(108), imodbit_cracked|imodbit_bent],

  ["fauchard_glaive", "Fauchard-glaive", [("1429_fauchard_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 440, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(171), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

  ["wooden_shield", "Wooden Shield", [("lithuanian_shield_old", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 114, hit_points(47)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield],

  ["club", "Club", [("caribbean_club_2h", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 300, thrust_damage(24, blunt)|hit_points(27648)|spd_rtng(82)|abundance(100)|weight(3.0)|swing_damage(24, blunt)|difficulty(6)|weapon_length(87), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_gaelic, fac_kingdom_13]],

  ["fauchard_fork0", "Fauchard-fork", [("1429_fauchard_fork_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(197), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

  ["fauchard_fork1", "Fauchard-fork", [("1429_fauchard_fork_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(200), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],
 
  ["glaive_fork", "Glaive-fork", [("1429_glaive_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(29696)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

  ["glaive_guisarme", "Glaive-guisarme", [("1429_glaive_guisarme_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(206), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],


  ["truncheon", "Truncheon", [("caribbean_club", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(50), imodbits_none],
  
  ["voulge1", "Voulge", [("mackie_voulge", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(40960)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["fustibalus", "Fustibalus", [("vc_Staf_Sling_fustibalus_2", imodbits_none)], itp_type_musket|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_knock_down, itcf_shoot_musket|itcf_reload_pistol, 100, thrust_damage(30, blunt)|max_ammo(1)|spd_rtng(85)|abundance(100)|weight(1.25)|leg_armor(85)|shoot_speed(65), imodbits_none],

  ["long_axe_3_alt", "Long War Axe", [("vik_long_hedmarkox", imodbits_none)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_civilian|itp_next_item_as_melee|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itc_parry_polearm, 245, thrust_damage(41, cut)|hit_points(44032)|spd_rtng(73)|abundance(100)|weight(3.625)|swing_damage(41, cut)|difficulty(12)|weapon_length(127), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["long_axe_4_alt", "Long War Axe", [("vik_long_hedmarkox_alt", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_thrust_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 0, thrust_damage(32, pierce)|hit_points(44032)|spd_rtng(83)|weight(3.625)|swing_damage(20, blunt)|difficulty(12)|weapon_length(127), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],



### modded2x end, item by anon modded 1257AD


# ARMOR
#handwear
 ["leather_gloves", "Hand Wraps", [("gf_tekko_1_L", imodbits_none)], itp_type_hand_armor, 0, 40, abundance(100)|weight(0.12)|body_armor(1), imodbits_cloth],

 ["mail_mittens", "Mail Mittens", [("mail_mittens_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 360, abundance(60)|weight(0.5)|difficulty(6)|body_armor(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0,
  get_gloves_price(9),
  weight(0.75)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor,
  [], eastern_factions + byzantine_factions ],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0,
  get_gloves_price(10),
  weight(0.75)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor,
  [], eastern_factions + byzantine_factions ],
#["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor],

# boots begin
#["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
["wrapping_boots", "Ankle Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],

["hunter_boots", "Hunter Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
  get_footwear_price(9),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
#["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
["ankle_boots", "Ankle Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
  get_footwear_price(6),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
["nomad_boots", "Nomad Boots", [("rus_boots_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),  
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(10),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["splinted_leather_greaves", "Mail with Shoes", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
  get_footwear_price(24),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor,
  [], latin_factions],
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(26),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor,
  [], all_euro_factions],
["splinted_greaves", "Splinted Greaves", [("kua_splinted_greaves_a",0)],  itp_type_foot_armor | itp_attach_armature,0,
  get_footwear_price(28),
  weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor,
  [], eastern_factions + balt_factions + byzantine_factions],
["splinted_greaves_long", "Splinted Greaves", [("kua_splinted_greaves_long",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
  get_footwear_price(28),
  weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor,
  [], eastern_factions + balt_factions + byzantine_factions],
["mail_boots", "Mail Boots", [("mail_spurs_cp1257",0)], itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(35),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(8) ,imodbits_armor, 
  [], all_euro_factions ],
["mail_boots_long", "Mail Boots", [("mail_spurs_cp1257_long",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(35),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(8) ,imodbits_armor, 
  [], all_euro_factions ],
["kau_mail_boots_dark", "Hardened Hose", [("kau_mail_boots_a_dark",0)], itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(25),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(4) ,imodbits_armor, 
  [], all_euro_factions ],
["kau_mail_boots_dark_long", "Hardened Hose", [("kau_mail_boots_a_dark_long",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(25),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(4) ,imodbits_armor, 
  [], all_euro_factions ],
# ["khergit_leather_boots", "Mongol Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  # get_footwear_price(14),
  # weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth,
  # [], mongol_factions],
["sarranid_boots_a", "Saracen Shoes", [("sarranid_shoes",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(8),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_a_long", "Saracen Shoes", [("cuman_boots",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(8),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_b", "Saracen Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(14),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_b_long", "Saracen Leather Boots", [("cuman_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(14),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_c", "Saracen camel boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(24),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_d", "Saracen Mail Boots", [("sarranid_mail_chausses",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(35),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_d_long", "Saracen Mail Boots", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(35),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["raf_mail_chausses", "Mail Chausses With Padding", [("raf_chausses",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(26),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor, [], all_euro_factions],
["kau_mail_boots", "Hardened Hose", [("kau_mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(25),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(4) ,imodbits_armor, [], all_euro_factions ],

### modded2x begin, item by anon 1257AD

  ["tan_hose1", "Tan Hose", [("hose_tan_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["red_hose1", "Red Hose", [("kau_mail_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["red_hose_with_kneecaps", "Red Hose with Kneecaps", [("hose_kneecops_red", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],


### modded2x end


["mamluke_boots", "Mameluke Boots", [("mamluke_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], arab_factions ],
["cuman_boots", "Cuman Boots", [("cuman_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_7]],
["byz_lord_boots", "Byzantine Boots", [("byz_lord_boots",0)], itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(35),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(8) ,imodbits_armor,
  [], byzantine_factions],
["byz_lord_boots_long", "Byzantine Boots", [("rus_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
  get_footwear_price(35),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(8) ,imodbits_armor,
  [], byzantine_factions],
# ["peasant_boots_a", "Shoes", [("peasant_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  # get_footwear_price(8),
  # weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
# ["peasant_boots_b", "Shoes", [("peasant_boots_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  # get_footwear_price(8),
  # weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["lapcie", "Eastern Wrapping Shoes", [("lapcie",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], eastern_factions + balt_factions],  
["byz_boots_c", "Byzantine Leather Boots", [("byz_leather_boots_c",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], byzantine_factions ],
["byz_cavalry_boots", "Byzantine Leather Boots", [("byz_cavalry_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(18),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth,
  [], byzantine_factions],
["byz_boots_a", "Byzantine Leather Boots", [("byz_leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], byzantine_factions],
["byz_boots_b", "Byzantine Leather Boots", [("byz_leather_boots_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], byzantine_factions],
["byzantine_greaves", "Byzantine Graves", [("byzantine_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
  get_footwear_price(24),
  weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor,
  [], byzantine_factions],
["leather_fur_boots", "Boots With Fur", [("leather_fur_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["red_hose", "Hose", [("red_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["green_hose", "Hose", [("green_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["grey_hose", "Hose", [("grey_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["dark_grey_hose", "Hose", [("dark_grey_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["yellow_hose", "Hose", [("yellow_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["green_hose_b", "Hose", [("green_hose_b",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],  #tied_up_shoes
["tied_up_shoes", "Hose", [("grey_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
["blue_hose_mod", "Hose", [("blue_hose_mod",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
 ["berber_shoes", "Berber Shoes", [("berber_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], andalusian_factions],
 ["legs_with_shoes", "Shoes", [("legs_with_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
  
  ["bare_legs", "Sandals", [("calrad_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 48, abundance(100)|weight(0.5)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_iberian, fac_culture_italian, fac_culture_andalus]],

  

["shoes", "Shoes", [("shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
# ["priest_1_boots", "Sandals", [("priest_1_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  # get_footwear_price(2),
  # weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth, [], all_euro_factions ],
["priest_2_boots", "Hose", [("priest_2_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth, [], all_euro_factions ],
["blue_hose", "Blue Hose", [("blue_hose_mod",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], all_euro_factions],
  
["rus_cav_boots", "Nomad Boots", [("rus_cav_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], [fac_kingdom_7]],
["rus_boots_a", "Rus' Boots", [("rus_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ,
  [], eastern_factions],
["rus_boots_b", "Rus' Boots", [("rus_boots_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], eastern_factions],
# boots end

# body begin
# ["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
# ["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
# ["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Mongol Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
 [], mongol_factions],
["khergit_lady_dress_b", "Mongol Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
 [], mongol_factions],
["sarranid_lady_dress", "Saracen Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[], arab_factions],
["sarranid_lady_dress_b", "Saracen Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[], arab_factions],
["sarranid_common_dress", "Saracen Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[], arab_factions],
["sarranid_common_dress_b", "Saracen Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[], arab_factions],
#["courtly_outfit", "Courtly Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor   ,0,
  get_barmour_price(2, 10, 0),
  weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], mongol_factions],
["khergit_armor", "Mongol Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor ,0,
  get_barmour_price(2, 14, 0),
  weight(2)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], mongol_factions],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor  |itp_civilian ,0,
  get_barmour_price(3, 15, 0),
  weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(5, 6, 0),
  weight(5)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
# ["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0,
  # get_barmour_price(7, 10, 0),
  # weight(7)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
  get_barmour_price(6, 8, 6),
  weight(6)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_armor ],

#for future:
# ["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["sleeveless_mail_coat", "Sleeveless Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["sleeveless_coat", "Sleeveless Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  get_barmour_price(4, 14, 10),
  weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["nordic_outfit", "Nordic Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["nordic_armor", "Nordic Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

#["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
#["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
# 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
# ["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 # 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(1, 6, 1),
  weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 #NEW was cvl_costume_a
["short_tunic", "Tunic With Felt Vest", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(1, 7, 1),
  weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#TODO:
 ["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(1, 7, 1),
  weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 # ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 # 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 # ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 # 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 # ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 # 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
  get_barmour_price(1.5, 8, 6),
  weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with Cape", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(2, 11, 6),
  weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
# 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
# ["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
  # get_barmour_price(3, 6, 1),
  # weight(3)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Linen Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  get_barmour_price(4, 9, 0),
  weight(4)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  get_barmour_price(5, 22, 4),
  weight(5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(4)|difficulty(0) ,imodbits_cloth,
 [], mongol_factions
 ],

["gambeson_a", "Gambeson", [("gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["gambeson_b", "Gambeson", [("gambeson_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["gambeson_c", "Gambeson", [("gambeson_c",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["gambeson_d", "Gambeson", [("gambeson_d",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], all_euro_factions ],

 #NEW: was aketon_a
["padded_cloth", "Leather Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], all_euro_factions ],
#NEW:
 # ["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # tier_2_body_armor_price,
  # tier_2_body_armor, imodbits_cloth,
  # [], all_euro_factions ],
 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(6, 15, 6),
  weight(6)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  get_barmour_price(7, 9, 5),
  weight(7)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
[], mongol_factions ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(7, 13, 9),
  weight(7)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
# ["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
  # get_barmour_price(12, 28, 10),
  # weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth ],
# ["nomad_robe", "Nomad Studded Leather Armour", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
  # get_barmour_price(15, 43, 18),
  # weight(15)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(18)|difficulty(0) ,imodbits_cloth,
# [], mongol_factions],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
# ["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # get_barmour_price(14, 30, 15),
  # weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(7) ,imodbits_armor ],

# ["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # get_barmour_price(17, 53, 10),
  # weight(17)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
#["blackwhite_surcoat", "Black and White Surcoat", [("surcoat_blackwhite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["green_surcoat", "Green Surcoat", [("surcoat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["blue_surcoat", "Blue Surcoat", [("surcoat_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["red_surcoat", "Red Surcoat", [("surcoat_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "haubergeon_a"
["haubergeon", "Haubergeon", [("kau_mail_shirt_cloak",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], euro_factions ],

["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_cloth,
  [], eastern_factions],

["lamellar_vest_khergit", "Mongol Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_cloth,
 [], mongol_factions],

 
["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], euro_factions ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], euro_factions ],

["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_7_body_armor_price,
  tier_7_body_armor ,imodbits_armor,
 [], euro_factions],
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red_mod",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_7_body_armor_price,
  tier_7_body_armor ,imodbits_armor,
 [], euro_factions],
#["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(90)|leg_armor(55)|difficulty(9) ,imodbits_plate ],
#["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
# 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(93)|leg_armor(58)|difficulty(10) ,imodbits_plate ],

##armors_d
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  get_barmour_price(2, 9, 1),
  weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
##armors_e
# ["khergit_elite_armor", "Mongol Elite Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(75)|leg_armor(31)|difficulty(8) ,imodbits_armor,
 # [], mongol_factions],
# ["vaegir_elite_armor", "Rus Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(75)|leg_armor(31)|difficulty(8) ,imodbits_armor,
 # [], eastern_factions],
# ["sarranid_elite_armor", "Arab Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(75)|leg_armor(31)|difficulty(8) ,imodbits_armor ],

["bishop_cop", "Coat of Plates", [("bishop_CoP",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_7_body_armor_price,
  tier_7_body_armor ,imodbits_armor,
  [], euro_factions ],


 # ["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_armor,
  # [], arab_factions ],
 # ["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_armor,
  # [], arab_factions ],
["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  get_barmour_price(1, 9, 9),
  weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_armor,
  [], arab_factions ],
["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  get_barmour_price(1, 9, 9),
  weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_armor,
  [], arab_factions ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  get_barmour_price(3, 15, 9),
  weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_armor,
  [], arab_factions ],
["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], arab_factions ],
["sarranid_leather_armor", "Saracen Padded Kaftan", [("kaftan",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
 [], arab_factions],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_cloth,
 [], arab_factions],
["arabian_armor_b", "Saracen Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
 [], arab_factions],
["sarranid_mail_shirt", "Saracen Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], arab_factions],

["mamluke_mail", "Mamluke Mail", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_cloth,
  [], arab_factions],

# ["player_surcoat_over_mail", "Custom_Surcoat_over_Mail", [("surcoat_civan", 0)], itp_type_body_armor|itp_covers_legs|itp_merchandise, 0,
  # tier_5_body_armor_price,
  # tier_5_body_armor, imodbits_armor,
  # [], euro_factions ],
["veteran_surcoat_a", "Surcoat_over_Mail", [("surcoat_cop_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor,  imodbits_armor,
  [], euro_factions ],
["veteran_surcoat_b", "Surcoat_over_Mail", [("surcoat_cop_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], euro_factions ],
["veteran_surcoat_c", "Surcoat_over_Mail", [("surcoat_cop_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], euro_factions ],
["veteran_surcoat_d", "Surcoat_over_Mail", [("surcoat_cop_d", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], euro_factions ],
["veteran_surcoat_e", "Surcoat_over_Mail", [("surcoat_cop_e", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], euro_factions ],
  
["arena_outfit_a", "Surcoat_over_Mail", [("arena_outfit_blue", 0)], itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_arena_armor, imodbits_armor,
  [], euro_factions ],
["arena_outfit_b", "Surcoat_over_Mail", [("arena_outfit_green", 0)], itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_arena_armor, imodbits_armor,
  [], euro_factions ],
["arena_outfit_c", "Surcoat_over_Mail", [("arena_outfit_red", 0)], itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_arena_armor, imodbits_armor,
  [], euro_factions ],
["arena_outfit_d", "Surcoat_over_Mail", [("arena_outfit_yellow", 0)], itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_arena_armor, imodbits_armor,
  [], euro_factions ],

# ["player_plated_surcoat_over_mail", "Plated_Custom_Surcoat_over_Mail", [("surcoat_civan", 0)], itp_type_body_armor|itp_covers_legs, 0,
  # tier_6_body_armor_price
  # tier_6_body_armor, imodbits_armor ],
["kau_aragon_knight", "Aragonian Mail", [("kau_aragon_knight", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_aragon_a", "Aragonian Mail", [("kau_aragon_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_aragon_b", "Aragonian Mail", [("kau_aragon_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_aragon_c", "Aragonian Mail", [("kau_aragon_c", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_montcada_surcoat", "Montcada Surcoat", [("kau_montcada_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_alego_surcoat", "Alego Surcoat", [("kau_alego_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_cervello_surcoat", "Cervello Surcoat", [("kau_cervello_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_cruilles_surcoat", "Cruilles Surcoat", [("kau_cruilles_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_entenca_surcoat", "Entensa Surcoat", [("kau_entenca_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_epyres_surcoat", "Epyres Surcoat", [("kau_epyres_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_luna_surcoat", "Luna Surcoat", [("kau_luna_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
["kau_pons_surcoat", "Pons Surcoat", [("kau_pons_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], latin_factions],
# ["kau_urgell_surcoat", "Urgell Surcoat", [("kau_urgell_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  # [], latin_factions],

["kau_castile_knight", "Crown of Castile Mail", [("kau_castile_knight", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_18]],
["kau_castile_a", "Crown of Castile Mail", [("kau_castile_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_18]],
["kau_castile_b", "Crown of Castile Mail", [("kau_castile_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_18]],
["kau_castile_c", "Crown of Castile Mail", [("kau_castile_c", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_18]],

  # ["kau_navarra_a", "Navarra Mail", [("kau_navarra_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    # [], [fac_kingdom_19]],
  # ["kau_navarra_b", "Navarra Mail", [("kau_navarra_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    # [], [fac_kingdom_19]],

["kau_santiago", "Santiago Mail", [("kau_santiago", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_16]],

["kau_portugal_a", "Portugese Mail", [("kau_portugal_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_16]],
["kau_portugal_b", "Portugese Mail", [("kau_portugal_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_16]],
["kau_portugal_c", "Portugese Mail", [("kau_portugal_c", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_16]],
["kau_portugal_d", "Portugese Mail", [("kau_portugal_d", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_16]],

["kau_papal", "Papal Surcoat over Mail", [("kau_papal", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_papacy]],
["kau_sicily_a", "Sicilian Mail", [("kau_sicily_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_24]],
["kau_sicily_b", "Sicilian Mail", [("kau_sicily_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_24]],

["kau_antioch", "Antioch Mail", [("kau_antioch", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],
["kau_cyprus", "Cyprus Mail", [("kau_cyprus", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],
["kau_antioch", "Antioch Mail", [("kau_antioch", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],
["kau_jerusalem", "Jerusalem Mail", [("kau_jerusalem", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],

["kau_latin_a", "Latin Empire Mail", [("kau_latin_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_26]],
["kau_latin_b", "Latin Empire Mail", [("kau_latin_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_26]],
["kau_athens", "Latin Empire Mail", [("kau_athens", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_26]],
["kau_courtenay", "Latin Empire Mail", [("kau_courtenay", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_26]],

["rnd_surcoat_01", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_01", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [
      (ti_on_init_item,
        [
          (assign ,":item_no", "itm_rnd_surcoat_01"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ],
      )
    ],
    euro_factions
  ],
	["rnd_surcoat_02", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_02", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign, ":item_no", "itm_rnd_surcoat_02"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_03", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_03", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign ,":item_no", "itm_rnd_surcoat_03"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_04", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_04", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign ,":item_no", "itm_rnd_surcoat_04"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),

        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_05", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_05", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign, ":item_no", "itm_rnd_surcoat_05"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_06", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_06", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign ,":item_no", "itm_rnd_surcoat_06"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_07", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_07", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_07"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_08", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_08", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_08"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_09", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_09", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_09"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_10", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_10", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_10"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_11", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_11", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_11"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_12", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_12", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_12"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_13", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_13", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_13"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_14", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_14", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_14"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],

	["rnd_surcoat_15", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_15", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_15"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],

	["rnd_surcoat_16", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_16", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_16"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],

	["rnd_surcoat_17", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_17", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_17"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_18", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_18", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_18"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],

	["rnd_surcoat_19", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_19", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_19"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_20", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_20", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_20"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_21", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_21", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_21"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_22", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_22", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_22"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],
	["rnd_surcoat_23", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_23", 0)], itp_type_body_armor| itp_covers_legs | itp_merchandise, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
    [
      (ti_on_init_item,
        [
          (assign,":item_no", "itm_rnd_surcoat_23"),
          (store_trigger_param_1, ":agent_no"),
          (store_trigger_param_2, ":troop_no"),
          (call_script, "script_set_matching_items", ":item_no", ":agent_no", ":troop_no"),
        ])
    ],
    euro_factions
  ],

  # Denmark
["surcoat_denmark_a", "Plated_Surcoat_over_Mail", [("surcoat_denmark_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_4] ],


  # England
["surcoat_england_a", "Plated_Surcoat_over_Mail", [("surcoat_england_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_9] ],
["surcoat_devalence", "Plated_Surcoat_over_Mail", [("surcoat_devalence", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_demontfort", "Plated_Surcoat_over_Mail", [("surcoat_demontfort", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_mortimer", "Plated_Surcoat_over_Mail", [("surcoat_mortimer", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_bigod", "Plated_Surcoat_over_Mail", [("surcoat_bigod", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_dewarenne", "Plated_Surcoat_over_Mail", [("surcoat_dewarenne", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_france_a", "Plated_Surcoat_over_Mail", [("surcoat_france_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_10] ],
["surcoat_hre_a", "Plated_Surcoat_over_Mail", [("surcoat_hre_wb", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_6] ],
["richard_of_cornwall_surcoat_over_mail", "Plated_Surcoat_over_Mail", [("surcoat_richard_of_cornwall_wb", 0)], itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_bohemia", "Plated_Surcoat_over_Mail", [("surcoat_bohemia_wb", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_6] ],
["surcoat_hungary_a", "Plated_Surcoat_over_Mail", [("surcoat_hungary_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_7] ],
["surcoat_ireland_a", "Plated_Surcoat_over_Mail", [("surcoat_gaelic_kingdoms", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_13] ],
["surcoat_lithuania_a", "Scale Armour", [("surcoat_lithuania_a", 0)], itp_merchandise |itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_2 ] ],
["surcoat_lithuania_b", "Leather Scale Armour", [("surcoat_lithuania_b", 0)], itp_merchandise |itp_type_body_armor|itp_covers_legs, 0, tier_4_body_armor_price, tier_4_body_armor, imodbits_armor,
  [], [ fac_kingdom_2 ] ],
["surcoat_norway_a", "Plated_Surcoat_over_Mail", [("surcoat_norway", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_11] ],
  # Novgorod
["surcoat_novgorod", "Novgorod Lamellar Armour", [("surcoat_novgorod", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_5_body_armor_price, tier_5_body_armor, imodbits_armor,
 [], eastern_factions ],
  # Scotland
["surcoat_scotland_a", "Plated_Surcoat_over_Mail", [("surcoat_scotland", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_12] ],
  # Sweden
["surcoat_sweden_a", "Plated_Surcoat_over_Mail", [("surcoat_sweden_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_14] ],
  # Polish stuff
["surcoat_kaliskie", "Plated_Surcoat_over_Mail", [("surcoat_kaliskie_wb", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_poland_a", "Plated_Surcoat_over_Mail", [("surcoat_poland_wb_a", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["siemowit_surcoat_over_mail", "Plated_Surcoat_over_Mail", [("surcoat_siemowit_wb", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
#["slask_surcoat_over_mail", "Plated_Surcoat_over_Mail", [("slask_surcoat", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],
["surcoat_gslask", "Plated_Surcoat_over_Mail", [("surcoat_gslask_wb", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_dslask", "Plated_Surcoat_over_Mail", [("surcoat_dslask_wb", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_mazowsze", "Plated_Surcoat_over_Mail", [("surcoat_mazowsze_wb", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_swidnica", "Plated_Surcoat_over_Mail", [("surcoat_swidnica_wb", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_swietopelk", "Plated_Surcoat_over_Mail", [("surcoat_swietopelk_wb", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_henry3", "Plated_Surcoat_over_Mail", [("surcoat_henry3_wb", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_a", "Plated_Surcoat_over_Mail", [("surcoat_pol_wb_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_b", "Scale Armour", [("surcoat_pol_wb_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_c", "Plated_Surcoat_over_Mail", [("surcoat_pol_wb_c", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_d", "Plated_Surcoat_over_Mail", [("surcoat_pol_wb_d", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_e", "Plated_Surcoat_over_Mail", [("surcoat_pol_wb_e", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_f", "Plated_Surcoat_over_Mail", [("surcoat_pol_wb_f", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_pol_g", "Plated_Surcoat_over_Mail", [("surcoat_pol_wb_g", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_czersk", "Plated_Surcoat_over_Mail", [("surcoat_czersk_wb", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],
["surcoat_przemysl2", "Plated_Surcoat_over_Mail", [("surcoat_przemysl2_wb", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_5] ],


  # Teutonic stuff
["teu_hochmeister_surcoat", "Plated_Mail_with_Surcoat", [("teu_hochmeister_surcoat", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  get_barmour_price(25,74,33),
  weight(25.00)|body_armor(74)|leg_armor(33)|difficulty(9), imodbit_reinforced|imodbit_crude|imodbit_rusty|imodbit_thick|imodbit_battered ],    

["teu_brother_surcoat_a", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_a",0)],  itp_merchandise | itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_1, fac_kingdom_23 ]],
["teu_brother_surcoat_b", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_b",0)],  itp_merchandise | itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], [fac_kingdom_1, fac_kingdom_23]],
["teu_brother_surcoat_c", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_c",0)],  itp_merchandise | itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], [fac_kingdom_1, fac_kingdom_23]],
["teu_brother_surcoat_d", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_d",0)],  itp_merchandise | itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_1, fac_kingdom_23 ]],
["teu_brother_surcoat_e", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_e",0)],  itp_merchandise | itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], [fac_kingdom_1, fac_kingdom_23]],
["teu_sariant_mail", "Mail_with_Surcoat", [("teu_sariant_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [],[fac_kingdom_1, fac_kingdom_23]],
["teu_postulant_a", "Postulant Tunic", [("teu_postulant", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [],[fac_kingdom_1, fac_kingdom_23]],
["teu_hbrother_mail", "Gambeson", [("teu_hbrother_mail", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], [ fac_kingdom_1, fac_kingdom_23 ] ],
["teu_sergeant", "Gambeson", [("teutonic_sergeant", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [],[fac_kingdom_1, fac_kingdom_23]],
["liv_sergeant", "Gambeson", [("livonian_sergeant", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [],[fac_kingdom_1, fac_kingdom_23]],


["teu_monk_surcoat_a", "Livonian gambeson", [("teu_monk", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], [fac_kingdom_1, fac_kingdom_23]],
["liv_tunic_a", "Livonian Tunic", [("liv_tunic_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], [fac_kingdom_1, fac_kingdom_23]],
["teu_gambeson", "Gambeson", [("teu_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], [ fac_kingdom_1, fac_kingdom_23 ]],
["teu_coat_of_plates", "Coat of Plates", [("teu_coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_7_body_armor_price,
  tier_7_body_armor ,imodbits_armor,
  [], [ fac_kingdom_1, fac_kingdom_23 ]],

["scale_shirt_a", "Scale_Shirt", [("raf_scale_armour_a", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor, [],  eastern_factions + balt_factions],

["kau_padded_mail_a", "Padded Aketon", [("kau_padded_mail_a", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], euro_factions],
["kau_mail_a", "Mail", [("kau_mail_a", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], euro_factions],
["kau_mail_b", "Maille", [("kau_mail_b", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], euro_factions],
["kau_haubergeon_a", "Rich Aketon", [("kau_haubergeon_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], euro_factions],
["kau_mail_shirt_a", "Aketon", [("kau_mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], euro_factions],
["kau_mail_shirt_b", "Mail Shirt", [("kau_mail_shirt_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], euro_factions],
["kau_mail_shirt_c", "Rich Aketon", [("kau_mail_shirt_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], euro_factions],
["kau_mail_shirt_d", "Padded Shirt", [("kau_mail_shirt_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], euro_factions],

# tier 4
["kau_rus_a", "Rus Heraldic Shirt With Mail", [("kau_rus_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], eastern_factions],
["kau_rus_b", "Eastern Scale Armor", [("kau_rus_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], eastern_factions],
["kau_rus_d", "Eastern Padded Armor", [("kau_rus_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], eastern_factions],
["kau_rus_scale_a", "Eastern Nobleman Scale Armor", [("kau_rus_nobleman_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], eastern_factions],
["kau_rus_noble_b", "Eastern Nobleman Lamellar Armor", [("kau_rus_nobleman_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], eastern_factions],

# tier 3
["kau_rus_lamellar_vest", "Eastern Lamellar Vest", [("kau_rus_nobleman_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_cloth,
  [], eastern_factions],
["kau_rus_noble_a", "Eastern Mail", [("kau_rus_nobleman_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], eastern_factions],

# tier 2
["kau_rus_c", "Eastern Leather Lamellar Armor with Maille", [("kau_rus_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], eastern_factions],  
["kau_rus_mail_shirt_a", "Leather Scale Armour", [("kau_rusmilitia",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], eastern_factions],
["kau_rus_mail_shirt_b", "Rus Middle Class Aketon", [("kau_rus_aketon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], eastern_factions],
["rus_mail_shirt_c", "Rus Mail Shirt", [("rus_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], eastern_factions + balt_factions],  

# tier 1
["kau_rus_e", "Eastern Shirt", [("kau_rus_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor, imodbits_cloth,
  [], eastern_factions],

# tier 2
["kau_lit_mail", "Baltic lamellar", [("balt_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], balt_factions + eastern_factions],

# ["lit_outfit", "Balt Lamellar Vest", [("lit_outfit",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  # tier_4_body_armor_price,
  # tier_4_body_armor, imodbits_armor,
  # [], [ fac_kingdom_2 ]],

#["surcoat_civan", "Plated_Surcoat_over_Mail", [("surcoat_civan", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor ],

# ["balt_gambeson", "Linen Gambeson", [("balt_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  # tier_2_body_armor_price,
  # tier_2_body_armor, imodbits_cloth,
  # [], [fac_kingdom_2]],

["kau_rus_tunic_a", "Rus' Tunic", [("kau_rus_tunic_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  get_barmour_price(4,9,0),
  weight(4)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], eastern_factions],
["kau_rus_tunic_b", "Rus' Tunic", [("kau_rus_tunic_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  get_barmour_price(4,9,0),
  weight(4)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], eastern_factions],
["kau_rus_tunic_c", "Rus' Tunic", [("kau_rus_tunic_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  get_barmour_price(4,9,0),
  weight(4)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(0)|difficulty(0) ,imodbits_cloth,
  [], eastern_factions],

# ARABIC
["kau_arab_aketon_blue", "Scale Vest", [("kau_arab_aketon_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_cloth,
  [], arab_factions],
["kau_arab_aketon", "Padded Cloth", [("kau_arab_aketon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["kau_arab_aketon_red", "Padded Cloth", [("kau_arab_aketon_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], arab_factions],
["kau_arab_aketon_green", "Padded Cloth", [("kau_arab_aketon_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], arab_factions],

["kau_arab_lamellar_vest_a", "Tunic", [("kau_ayubbid",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth,
  [], arab_factions],
["kau_arab_lamellar_vest_b", "Tunic", [("kau_ayubbid_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth,
  [], arab_factions],
["kau_arab_lamellar_vest_c", "Tunic", [("kau_ayubbid_copy",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth,
  [], arab_factions],

 ["arab_mail_a", "Lamellar Vest", [("arab_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_cloth,
  [], arab_factions],
["arab_mail_b", "Lamellar Vest", [("arab_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_cloth,
  [], arab_factions],
["arab_mail_c", "Lamellar Vest", [("arab_mail_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_cloth,
  [], arab_factions],
["arab_mail_d", "Lamellar Vest", [("arab_mail_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_cloth,
  [], arab_factions], 
  
["kau_arab_mail_shirt_a", "Kaftan", [("kau_mail_sara",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_armor,
  [], arab_factions],
["kau_arab_mail_shirt_b", "Mail Shirt", [("kau_mail_saracen",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], arab_factions],
["kau_arab_mail_shirt_c", "Mail Shirt", [("kau_mail_saracen_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], arab_factions],
["kau_arab_mail_shirt_d", "Hardened Kaftan", [("kau_mail_saracen_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], arab_factions],

["kau_arab_tunic_a", "Bedouin Tunic", [("kau_muslim", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["kau_arab_tunic_b", "Bedouin Tunic", [("kau_muslim_a", 0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],

["arab_banded_a", "Saracen Banded Armour", [("kau_banded_armor_a",0)],   itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], arab_factions],
["arab_banded_b", "Saracen Banded Armour", [("kau_banded_armor_muslim",0)],   itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], arab_factions],
["arab_banded_c", "Saracen Banded Armour", [("kau_banded_armor_muslima",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], arab_factions],
  

["templar_sarjeant_surcoat", "Surcoat_over_Mail", [("templar_serjeant_surcoat_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [],[ fac_kingdom_23 ]],
["templar_sarjeant_mail", "Mail_Hauberk", [("templar_serjeant_mail", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["templar_mail_a", "Templar gambeson", [("templar_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], [ fac_kingdom_23 ]],
["templar_tunic_a", "Postulant_Tunic", [("templar_postulant_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], [ fac_kingdom_23 ]],
["templar_knight_a", "Templar Mail with Surcoat", [("templar_knight_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["templar_knight_b", "Templar Mail with Surcoat", [("templar_knight_b",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["templar_knight_c", "Templar Mail with Surcoat", [("templar_knight_c",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ] ],
["templar_gambeson_a", "Gambeson", [("templar_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], [ fac_kingdom_23 ]],

["hospitaller_knight_a", "Mail with Surcoat", [("hospitaller_knight_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_knight_b", "Mail with Surcoat", [("hospitaller_knight_b",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_knight_c", "Mail with Surcoat", [("hospitaller_knight_c",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_knight_d", "Mail with Surcoat", [("hospitaller_knight_d",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_knight_e", "Mail with Surcoat", [("hospitaller_knight_e",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_knight_f", "Mail with Surcoat", [("hospitaller_knight_f",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_sarjeant_surcoat", "Surcoat_over_Mail", [("templar_serjeant_surcoat_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_sarjeant_mail", "Mail_Hauberk", [("templar_serjeant_mail", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hospitaller_tunic_a", "Postulant_Tunic", [("templar_postulant_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], [ fac_kingdom_23 ]],
["hospitaller_gambeson_a", "Gambeson", [("templar_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], [ fac_kingdom_23 ]],
["hospitaller_knight_a", "Mail with Surcoat", [("hospitaller_knight_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], [ fac_kingdom_23 ]],
["hirdman_a", "Coat of Plates", [("kau_hirdman_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_7_body_armor_price,
  tier_7_body_armor, imodbits_armor,
  [], all_euro_factions ],

["cuman_shirt_a", "Cuman Tunic", [("cuman_shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], [fac_kingdom_7]],
["cuman_shirt_b", "Cuman Tunic", [("cuman_shirt_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], [fac_kingdom_7]],
["cuman_shirt_c", "Cuman Tunic", [("cuman_shirt_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], [fac_kingdom_7]],
["cuman_shirt_d", "Cuman Tunic", [("cuman_shirt_d",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], [fac_kingdom_7]],

["kipchak_shirt_a", "Kipchak Tunic", [("kipchak_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], [fac_kingdom_7]],
["kipchak_shirt_b", "Kipchak Tunic", [("kipchak_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], [fac_kingdom_7]],
["kipchak_mail_a", "Kipchak Mail Shirt", [("kipchak_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 tier_4_body_armor_price,
 tier_4_body_armor ,imodbits_armor,
 [], [fac_kingdom_7]],

["mongol_warrior_a", "Mongol Tunic", [("mongol_light_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], mongol_factions],
["mongol_warrior_b", "Mongol Kaftan", [("mongol_light_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], mongol_factions],
["mongol_warrior_c", "Mongol Leather Vest", [("mongol_leather_armour",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], mongol_factions],
["mongol_warrior_d", "Chinese Kaftan", [("mongol_warrior_d",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], mongol_factions],
["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_cloth,
  [], mongol_factions],
["mongol_tunic_b", "Mongol Tunic", [("mongol_warrior_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], mongol_factions],
["mongol_warrior_ilkhanate", "Mongol Mail", [("ilkhanate_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_cloth,
  [], mongol_factions],
  
["mamluk_shirt_a", "Mamluk shirt", [("mamluk_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_armor,
  [], mamluk_factions],
["mamluk_shirt_b", "Mail Shirt", [("mamluk_shirt_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], mamluk_factions],
["mamluk_shirt_c", "Mail Shirt", [("mamluk_shirt_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], mamluk_factions],
["mamluk_shirt_d", "Lamellar", [("mamluk_shirt_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], mamluk_factions],
["mamluk_shirt_e", "Seljuk Mail Shirt", [("mamluk_shirt_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], mamluk_factions],
["mamluk_shirt_f", "Arab scale Armour", [("mamluk_shirt_f",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], mamluk_factions],

["peasant_tunic_a", "Linen Tunic", [("peasant_outfit_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth],
["peasant_b", "Linen Tunic", [("peasant_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],
["peasant_c", "Linen Tunic", [("peasant_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],
["peasant_d", "Tunic with Cape", [("peasant_man_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],
["ragged_cloth_b", "Ragged Cloth", [("ragged_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],
["peasant_f", "Linen Tunic", [("ragged_cloth_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

 ["peasant_g", "Linen Tunic with Cape", [("peasant_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["byz_lord", "Byzantine Armour", [("byz_lord", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], byzantine_factions],
["byz_emperor", "Byzantine Armour", [("byz_emperor", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], byzantine_factions],

["bishop_a", "Bishop Mail", [("bishop_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], all_euro_factions],

["varangian_a", "Varangian Mail Hauberk", [("varangian_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], [fac_kingdom_22]],
["varangian_b", "Varangian Lamellar", [("varangian_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_22]],
["varangian_c", "Varangian Lamellar", [("varangian_c", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_22]],

["kau_rus_noble_d", "Eastern Nobleman Lamellar Armor", [("kau_rus_nobleman_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], eastern_factions],

["balt_lamellar_vest_a", "Baltic Shirt", [("balt_lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], balt_factions],
["balt_lamellar_vest_b", "Baltic Shirt", [("balt_lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], balt_factions],
["balt_lamellar_vest_c", "Baltic Lamellar Vest", [("balt_lamellar_vest_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_cloth,
  [], balt_factions],
["byz_mail_a", "Byzantine Mail", [("byzantine_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], byzantine_factions ],
["byz_lamellar_a", "Byzantine Lamellar Leather Armour", [("byz_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], byzantine_factions ],
["byz_lamellar_b", "Byzantine Lamellar Leather Armour", [("byz_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], byzantine_factions ],
["byz_leather_a", "Byzantine Leather Armour", [("byz_leather_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], byzantine_factions ],
["byz_leather_b", "Byzantine Leather Armour", [("byz_leather_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], byzantine_factions ],
["byz_padded_leather", "Byzantine Padded Leather Armour", [("byz_padded_cloth",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], byzantine_factions ],
["byz_scale_armor", "Byzantine Scale Armor", [("byz_cavalry",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], [fac_kingdom_22] ],
["byz_cavalry_a", "Byzantine Cavalry Armour", [("byz_cavalry_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],
["byz_cavalry_b", "Byzantine Cavalry Armour", [("byz_cavalry_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],
["byz_mail_b", "Byzantine Mail", [("byz_mail_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_5_body_armor_price,
  tier_5_body_armor,  imodbits_armor,
  [], byzantine_factions ],
["byz_hcavalry_a", "Byzantine Heavy Cavalry Armour", [("byz_hcavalry_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],
["byz_hcavalry_b", "Byzantine Heavy Cavalry Armour", [("byz_hcavalry_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],
["byz_hcavalry_c", "Byzantine Heavy Cavalry Armour", [("byz_hcavalry_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],
["byz_psiloi_a", "Linen Tunic", [("byz_psiloi_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],
["byz_psiloi_b", "Linen Tunic", [("byz_psiloi_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],
["byz_kataphrakt", "Cataphract Armour", [("byz_kataphrakt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], byzantine_factions],

["kipchak_lamellar_a", "Kipchak Mail", [("kipchak_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], eastern_factions + byzantine_factions], 
["kipchak_lamellar_b", "Kipchak Lamellar Armor", [("kipchak_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], eastern_factions + byzantine_factions],
 
["balt_shirt_a", "Shirt With Fur Vest", [("balt_shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth, [],  balt_factions],
["balt_shirt_b", "Shirt", [("balt_shirt_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], balt_factions],
["balt_shirt_e", "Shirt", [("balt_shirt_e",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], balt_factions],
["balt_shirt_d", "Shirt", [("balt_shirt_d",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], balt_factions],
["balt_fur_coat_a", "Fur Coat", [("balt_fur_coat_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], balt_factions],
["balt_fur_coat_b", "Fur Coat", [("balt_fur_coat_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth, 
  [], balt_factions],

["mon_lamellar_a", "Mongol Lamellar Armor", [("mon_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], mongol_factions],
["mon_lamellar_b", "Mongol Lamellar Armor", [("mon_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], mongol_factions],

["byz_footman_a", "Byzantine Mail", [("byz_footman_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor,
  [], byzantine_factions ],
["byz_footman_b", "Byzantine Padded Cloth", [("byz_footman_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], byzantine_factions ],
["byz_footman_c", "Byzantine Mail", [("byz_footman_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor,
  [], byzantine_factions ],
# ["byz_swordsman", "Byzantine Scoutati Armour", [("byz_swordsman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # tier_4_body_armor_price,
  # tier_4_body_armor ,imodbits_armor,
  # [], byzantine_factions ],
  ["byz_swordsman_1", "Byzantine Scoutati Armour", [("byz_swordsman_r",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],

  ["byz_swordsman_2", "Byzantine Scoutati Armour", [("byz_swordsman_w",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],

  ["byz_swordsman_3", "Byzantine Scoutati Armour", [("byz_swordsman_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],
  ["byz_swordsman_4", "Byzantine Scoutati Armour", [("byz_swordsman_p",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions ],


["byz_guard_a", "Byzantine Guard Armour", [("byz_guard_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], byzantine_factions],
["byz_guard_b", "Byzantine Guard Armour", [("byz_guard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], byzantine_factions],
["kau_arab_nobleman", "Saracen Noble Armour", [("kau_arab_nobleman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], arab_factions],

# ["vik_byrnie", "Byrnie", [("vikingbyrnie",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # get_barmour_price(17, 53, 10),
  # weight(17)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
["almogavar_a", "Pelt Coat", [("almogavar_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], iberian_factions],
["almogavar_b", "Pelt Coat", [("almogavar_b",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], iberian_factions],
["almogavar_c", "Pelt Coat", [("almogavar_c",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 tier_0_body_armor_price,
 tier_0_body_armor ,imodbits_cloth,
  [], iberian_factions],

#Quest-specific - perhaps can be used for prisoners,
["burlap_tunic", "Burlap Tunic", [("shirt_a",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],

["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
 tier_5_body_armor ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])],
 euro_factions],
# ["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # tier_5_body_armor_price,
  # tier_5_body_armor, imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])],
 # euro_factions],
# ["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # tier_5_body_armor_price,
  # tier_5_body_armor, imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])],
 # euro_factions],
# ["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  # tier_5_body_armor_price,
  # tier_5_body_armor, imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])],
 # euro_factions],
 

# headwear begin 
["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_merchandise|itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], arab_factions],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_merchandise|itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], arab_factions],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], arab_factions],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], arab_factions],

# ["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth],
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_civilian|itp_type_head_armor|itp_fit_to_head,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth],
#["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_civilian|itp_type_head_armor|itp_fit_to_head,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_civilian|itp_type_head_armor|itp_fit_to_head,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth],
# ["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
  # get_headgear_price(10),
  # weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_type_head_armor  |itp_civilian ,0, 
  head_armor_no_price,
  head_armor_no ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("1257_arming_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_no_price,
  head_armor_no,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth,
  [], mongol_factions],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth,
  [], mongol_factions],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_light_price,
  head_armor_light, imodbits_cloth,
  [], mongol_factions],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light, imodbits_cloth,
  [], all_euro_factions],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0,
  head_armor_hat_price,
  head_armor_hat, imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0,
  head_armor_light_price,
  head_armor_light,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
  head_armor_hat_price,
  head_armor_hat,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light,imodbits_cloth,
  [], mongol_factions],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light,imodbits_cloth,
  [], mongol_factions],
["leather_steppe_cap_c", "Steppe Cap", [("nomad_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth,
  [], mongol_factions],
["mail_coif", "Mail Coif with skullcap", [("coif_1257",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor, [], all_euro_factions ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate ],
#["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(35*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
# ["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
  # get_headgear_price(50),
  # weight(1.25)|abundance(100)|head_armor(50*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], all_euro_factions ],
# ["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(40),
  # weight(1.25)|abundance(100)|head_armor(40*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
# ["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(55),
  # weight(1.5)|abundance(100)|head_armor(55*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
# ["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(60),
  # weight(1.75)|abundance(100)|head_armor(60*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], all_euro_factions ],
# ["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(60),
  # weight(2)|abundance(100)|head_armor(60*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions ],

["khergit_lady_hat", "Mongol Lady Hat", [("khergit_lady_hat",0)],  itp_merchandise|itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], mongol_factions],
["khergit_lady_hat_b", "Mongol Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_merchandise|itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], mongol_factions],
["sarranid_felt_hat", "Saracen Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth,
  [], arab_factions],
["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth,
  [], arab_factions],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth,
  [], arab_factions],
  
["turban_a", "Turban", [("arab_turban_a",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth,
  [], arab_factions],
["turban_b", "Turban", [("arab_turban_b",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth,
  [], arab_factions],
["turban_c", "Turban", [("arab_turban_c",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light,imodbits_cloth,
  [], arab_factions],
["arab_mail_coif", "Saracen Mail Coif", [("arabic_coif",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor,
  [], arab_factions],
["seljuk_helmet", "Seljuk Helmet", [("seljuk_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_armor,
  [], arab_factions],
# ["arab_helmet_a", "Saracen Hood", [("arab_helmet_a",0)], itp_merchandise| itp_type_head_armor ,0,
  # head_armor_hat_price,
  # head_armor_hat ,imodbits_armor,
  # [], arab_factions],
# ["arab_helmet_c", "Saracen Helmet", [("arab_helmet_c",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
  # head_armor_proper_price,
  # head_armor_proper,imodbits_armor,
  # [], arab_factions],

["sarranid_warrior_cap", "Saracen Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average,imodbits_plate,
  [], arab_factions],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], arab_factions],
["sarranid_helmet1", "Saracen Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], arab_factions],
["sarranid_mail_coif", "Saracen Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], arab_factions],
["sarranid_veiled_helmet", "Saracen Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], arab_factions],

# ["vaegir_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(30),
  # weight(2)|abundance(100)|head_armor(30*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions],
# ["vaegir_fur_helmet", "Rus Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(40),
  # weight(2)|abundance(100)|head_armor(40*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions],
# ["vaegir_spiked_helmet", "Spiked Cap", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(60),
  # weight(2)|abundance(100)|head_armor(60*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions],
# ["vaegir_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(45),
  # weight(2)|abundance(100)|head_armor(45*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions],
# ["vaegir_noble_helmet", "Rus Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(65),
  # weight(2)|abundance(100)|head_armor(65*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions],
# ["vaegir_war_helmet", "Rus War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(70),
  # weight(2)|abundance(100)|head_armor(70*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions],
["vaegir_mask", "Rus War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_plate,
  [], eastern_factions],


# ["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
  # get_headgear_price(47),
  # weight(2.5)|abundance(100)|head_armor(47*hai)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
  # [], euro_factions + [ fac_kingdom_23 ] ],
# ["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0,
  # get_headgear_price(75),
  # weight(2.5)|abundance(100)|head_armor(75*hai)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,
  # [], euro_factions + [ fac_kingdom_23 ] ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,
  head_armor_full_price,
  head_armor_full ,imodbits_plate,
  [], euro_factions + [ fac_kingdom_23 ] ],
["osp_great_helm_a", "Great_Helm", [("osp_greathelm_a", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions + [ fac_kingdom_23 ] ],
["osp_great_helm_b", "Great_Helm", [("osp_greathelm_b", 0)], itp_merchandise |itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions + [ fac_kingdom_23 ] ],
["osp_byzantion_a", "Brimmed_Helmet", [("osp_byzantion_a", 0)], itp_merchandise | itp_type_head_armor | itp_covers_beard, 0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_cloth,
  [], byzantine_factions  ],

["vik_norman_helmet_a", "Norman Helmet", [("vik_coifedpointyhelm",0),("inv_vik_coifedpointyhelm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  all_euro_factions ],

["vik_norman_helmet_b", "Norman Helmet", [("vik_normanhelmet",0),("inv_vik_normanhelmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [],  all_euro_factions ],
["vik_norman_helmet_c", "Norman_Helmet", [("vik_pointedhelmet", 0)], itp_merchandise |itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  all_euro_factions ],

["vik_norman_helmet_e", "Plain_Helm", [("viki_plainhelm", 0)], itp_merchandise |itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_armor|imodbit_cracked,
  [],  all_euro_factions ],
["vik_spangen_a", "Spangen_Helm", [("vik_norskspangen1", 0)], itp_merchandise |itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_armor|imodbit_cracked,
  [],  all_euro_factions ],
["vik_spangen_b", "Spangen_Helm", [("vik_norskspangendecorated",0),("inv_vik_norskspangendecorated",ixmesh_inventory)], itp_merchandise |itp_type_head_armor | itp_attach_armature, 0,
  head_armor_average_price,
  head_armor_average, imodbits_armor|imodbit_cracked,
  [],  all_euro_factions],
["balt_spiked_helmet", "Balt Spiked Cap", [("pointy_helmet",0)], itp_merchandise |itp_type_head_armor   ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], balt_factions ],
["balt_footman_helmet", "Balt Footman Helmet", [("lit_segmented_helmet",0)], itp_merchandise |itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], balt_factions ],
["balt_helmet_a", "Balt Helmet", [("lit_segmented_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], balt_factions ],
["balt_helmet_b", "Balt Helmet", [("pointy_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], balt_factions ],
["balt_helmet_c", "Balt Helmet", [("rusiu_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], balt_factions ],

# ["pol_helm_05", "Great_Helm", [("pol_helm_05", 0)], itp_type_head_armor|itp_covers_head, 0,
  # get_headgear_price(90),
  # weight(2.75)|head_armor(90*hai)|difficulty(10), imodbits_armor|imodbit_cracked ],
# ["pol_helm_08", "Great_Helm", [("pol_helm_08", 0)], itp_type_head_armor|itp_covers_head, 0,
  # get_headgear_price(90),
  # weight(2.75)|head_armor(90*hai)|difficulty(10), imodbits_armor|imodbit_cracked ],

["teu_kettle_hat_a", "Kettle_Helm", [("teu_kettle_hat_cloth_a", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_decent_price,
  head_armor_decent, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], [ fac_kingdom_1, fac_kingdom_23 ] ],
["teu_kettle_hat_b", "Kettle_Helm", [("teu_kettle_hat_b", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_decent_price,
  head_armor_decent, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], [ fac_kingdom_1, fac_kingdom_23 ] ],


["slonim", "Slonim", [("slonim",0),("inv_slonim",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_armor|imodbit_cracked,
  [], balt_factions ],
["osp_faceplate", "Chapel de fer", [("osp_faceplate",0),("inv_osp_faceplate",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [], euro_factions ],

["rnd_helm_01", "Winged_Great_Helmet", [("rnd_helm_01", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],
["rnd_helm_02", "Winged_Great_Helmet", [("rnd_helm_02", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],
["rnd_helm_03", "Great_Helmet", [("rnd_helm_03", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],
["rnd_helm_04", "Great_Helm", [("civan_helm_a", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],
["rnd_helm_05", "Great_Helm", [("civan_helm_b", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],
["rnd_helm_06", "Great_Helm", [("civan_helm_c", 0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],

# ["kau_montcada_helmet", "Aragonese Helmet_REMOVE", [("kau_montcada_helmet", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  # get_headgear_price(60),
  # weight(1.50)|head_armor(60*hai)|difficulty(7), imodbits_shield|imodbit_crude|imodbit_rusty,
  # [], [ fac_kingdom_17] ],
["kau_alego_helmet", "Aragonese Helmet", [("kau_alego_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], latin_factions ],
# ["kau_cervello_helmet", "Aragonese Helmet_REMOVE", [("kau_cervello_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  # get_headgear_price(60),
  # weight(1.50)|head_armor(60*hai)|difficulty(7), imodbits_shield|imodbit_crude|imodbit_rusty,
  # [], [ fac_kingdom_17] ],
# ["kau_cruilles_helmet", "Aragonese Helmet_REMOVE", [("kau_cruilles_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  # get_headgear_price(60),
  # weight(1.50)|head_armor(60*hai)|difficulty(7), imodbits_shield|imodbit_crude|imodbit_rusty,
  # [], [ fac_kingdom_17] ],
# ["kau_entenca_helmet", "Aragonese Helmet_REMOVE", [("kau_entenca_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  # get_headgear_price(60),
  # weight(1.50)|head_armor(60*hai)|difficulty(7), imodbits_shield|imodbit_crude|imodbit_rusty,
  # [], [ fac_kingdom_17] ],
["kau_epyres_helmet", "Aragonese Helmet", [("kau_epyres_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], latin_factions ],
# ["kau_luna_helmet", "Aragonese Helmet_REMOVE", [("kau_luna_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  # get_headgear_price(60),
  # weight(1.50)|head_armor(60*hai)|difficulty(7), imodbits_shield|imodbit_crude|imodbit_rusty,
  # [], [ fac_kingdom_17] ],
["kau_pons_helmet", "Aragonese Helmet", [("kau_pons_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], latin_factions],
# ["kau_reino_helmet", "Aragonese Helmet_REMOVE", [("kau_reino_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  # get_headgear_price(60),
  # weight(1.50)|head_armor(60*hai)|difficulty(7), imodbits_shield|imodbit_crude|imodbit_rusty,
  # [], [ fac_kingdom_17] ],
["kau_urgell_helmet", "Aragonese Helmet", [("kau_urgell_helm", 0)], itp_merchandise|itp_type_head_armor|itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], latin_factions ],
  
["byz_yoman_a", "Byzantine Helmet", [("facecovermail_plume",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_armor|imodbit_cracked,
  [], byzantine_factions],
["byz_yoman_b", "Byzantine Helmet", [("facecovermail_kettlehat",0), ("inv_facecovermail_kettlehat",ixmesh_inventory)], itp_merchandise| itp_type_head_armor |itp_covers_beard| itp_attach_armature ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_armor|imodbit_cracked,
  [], byzantine_factions],
["byz_yoman_c", "Byzantine Skullcap Helmet", [("facecovermail_helmet",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_armor|imodbit_cracked,
  [], byzantine_factions],
["byz_yoman_d", "Byzantine Helmet", [("facecovermail",0),("inv_facecovermail",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent ,imodbits_armor|imodbit_cracked,
  [], byzantine_factions],

["templar_kettlehat_a", "Kettle_Helm", [("templar_kettle_cloth", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [],[fac_kingdom_23]],
["hospitaller_kettlehat_a", "Kettle_Helm", [("templar_kettle_cloth", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [],[fac_kingdom_23]],

["elm1", "Skullcap with Ventail", [("elm_type1", 0)], itp_merchandise | itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_cloth,
  [], all_euro_factions ],
["elm2", "Skullcap with Arming Cap", [("elm_type2", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_cloth,
  [], all_euro_factions ],
["elm3", "Mail Coif with Noseguard", [("elm_type3", 0)], itp_merchandise | itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_cloth,
  [], all_euro_factions ],
["elm5", "Aragonese Helmet", [("elm_type5", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_cloth,
  [], iberian_factions ],
["elm6", "Flutted Spangen Helmet", [("elm_type6", 0)], itp_merchandise | itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_cloth,
  [], all_euro_factions ],
["elm7", "Reinforced Mail Coif", [("elm_type7", 0)], itp_merchandise | itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_cloth,
  [], byzantine_factions ],
["elm8", "Spangen Helmet", [("elm_type8", 0)], itp_merchandise | itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_cloth,
  [], all_euro_factions ],
["elm9", "Yesenovo Helm", [("elm_type9", 0)], itp_merchandise | itp_type_head_armor , 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_cloth,
  [], byzantine_factions  ],
["elm10", "Byzantine_Brimmed_Helmet", [("byz_kettle",0),("inv_byz_kettle",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor|imodbit_cracked,
  [], byzantine_factions ],
["byz_helmet_a", "Byzantine Footman's Helmet", [("byz_helmet_a",0),("inv_byz_helmet_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor|imodbit_cracked,
  [], byzantine_factions ],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_plate ],
["raf_spangen", "Spangen_Helm", [("spangen", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [], all_euro_factions],
["arab_helmet_a", "Andalusian Tiara", [("arab_helmet_a", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_hat_price,
  head_armor_hat, imodbits_armor|imodbit_cracked,
  [], arab_factions],
["arab_helmet_b", "Saracen Helm", [("arab_helmet_b", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], arab_factions],
["arab_helmet_c", "Saracen Helm", [("arab_helmet_c", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], arab_factions],
["berber_helmet_a", "Berber Helm", [("berber_helmet", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_hat_price,
  head_armor_hat, imodbits_cloth,
  [], andalusian_factions],
["maciejowski_helm", "Decorated Great_Helm", [("maciejowskihelm", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions + [ fac_kingdom_23 ] ],
["talak_litchina", "Litchina Helmet", [("talak_litchina",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_plate,
  [], eastern_factions],
["crown_coif", "Crown", [("coif_crown_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], all_euro_factions],
["aragon_crown", "Crown", [("aragon_crown",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], iberian_factions],
["talak_crown_ornate", "Ornate_Crowned_Helm", [("talak_crown_ornate", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], all_euro_factions],
  
["cuman_cap_a", "Cuman Hat", [("cuman_cap_a",0),("inv_cuman_cap_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_light_price,
  head_armor_light, imodbits_armor,
  [], [fac_kingdom_7]],
["cuman_cap_b", "Cuman Hat", [("cuman_cap_b", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0,
  head_armor_average_price,
  head_armor_average, imodbits_armor,
  [], [fac_kingdom_7]],
["cuman_cap_c", "Cuman Hat", [("cuman_cap_c", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0,
  head_armor_light_price,
  head_armor_light, imodbits_armor,
  [], [fac_kingdom_7]],

["maciejowski_kettle_hat_a", "Kettle Hat", [("maciejowski_kettle_a",0),("inv_maciejowski_kettle_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],
["maciejowski_kettle_hat_b", "Kettle Hat", [("maciejowski_kettle_b",0),("inv_maciejowski_kettle_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["norman_coif_a", "Kettle Hat", [("red_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_decent_price,
  head_armor_decent,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["maciejowski_crown", "Crowned Great Helm", [("crown_helm",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_full_price,
  head_armor_full ,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["crowned_norman", "Crowned Norman Helm", [("crown_helmtet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper  ,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["norman_coif_b", "Kettle Hat", [("norman_helmtet",0), ("inv_norman_helmtet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_covers_beard | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["rus_helm_a", "Gnezdovo Helm", [("gnezdovo_helm_a",0),("inv_gnezdovo_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper , imodbits_armor|imodbit_cracked,
  [], eastern_factions ],

["rus_helmet_b", "Slavic Helm", [("rus_helmet_b",0),("inv_rus_helmet_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper , imodbits_armor|imodbit_cracked,
  [], eastern_factions ],

["norman_coif_c", "Kettle Helmet", [("blue_helmet",0),("inv_blue_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_average_price,
  head_armor_average ,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["norman_coif_d", "Kettle Hat", [("green_helmet",0)], itp_merchandise| itp_type_head_armor  ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["norman_coif_e", "Norman Helmet", [("white_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_average_price,
  head_armor_average ,imodbits_armor|imodbit_cracked,
  [], all_euro_factions ],

["teu_kettle_hat_a_mail", "Kettle_Helm", [("teu_kettle_mail", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_average_price,
  head_armor_average, imodbits_armor|imodbit_cracked,
  [], [ fac_kingdom_1, fac_kingdom_23 ] ],
  
["templar_kettlehat_a_mail", "Kettle_Helm", [("templar_kettle_mail", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_average_price,
  head_armor_average, imodbits_shield|imodbit_crude|imodbit_rusty,
  [],[fac_kingdom_23]],
["hospitaller_kettlehat_a_mail", "Kettle_Helm", [("templar_kettle_mail", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_shield|imodbit_crude|imodbit_rusty,
  [],[fac_kingdom_23]],
["kolpak_mail", "Cervilliere", [("kolpak_mail", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_shield|imodbit_crude|imodbit_rusty,
  [],[fac_kingdom_23]],
["mail_coif_b", "Decorated Mail Coif", [("bandage_coif_a",0)], itp_merchandise| itp_type_head_armor| itp_fit_to_head| itp_covers_beard ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor ],
["mail_coif_c", "Decorated Mail Coif", [("bandage_coif_b",0)], itp_merchandise| itp_type_head_armor| itp_fit_to_head| itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy,imodbits_armor ],
["norman_faceplate", "Scullcap wth Nose Guard", [("norman_faceplate_a", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [],all_euro_factions],
["varangian_helm", "Varangian Helmet", [("varangian_helmet",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy,imodbits_plate,
  [], byzantine_factions],

["mamluke_helm", "Mamluke Helmet", [("mamluk_helmet",0),("inv_baltic_ponted_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper  ,imodbits_plate,
  [], mamluk_factions],

# helmets end #############################################################################
  
# weapons begin
#["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
#  get_w_price(62, get_mace_weight(62), get_1hmace_speed(62), 9, 0),
#  weight(get_mace_weight(62))|difficulty(0)|spd_rtng(get_1hmace_speed(62)) | weapon_length(62)|swing_damage(9 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
#["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
#  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 18, 0),
#  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(18 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
#["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
#  get_w_price(58, get_mace_weight(58), get_1hmace_speed(58), 13, 0),
#  weight(get_mace_weight(58))|difficulty(0)|spd_rtng(get_1hmace_speed(58)) | weapon_length(58)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
#[], all_euro_factions  ],
#["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
#  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 18, 0),
#  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(18 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
#[], all_euro_factions  ],
#["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
#  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 22, 0),
#  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
#[], all_euro_factions  ],
#["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
#  get_w_price(68, get_mace_weight(73), get_1hmace_speed(73), 24, 0),
#  weight(get_mace_weight(73))|difficulty(0)|spd_rtng(get_1hmace_speed(73)) | weapon_length(73)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick,
#[], all_euro_factions  ],
#["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#  get_w_price(58, get_mace_weight(58), get_1hmace_speed(58), 27, 0),
#  weight(get_mace_weight(58))|difficulty(0)|spd_rtng(get_1hmace_speed(58)) | weapon_length(58)|swing_damage(27 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
#[], all_euro_factions  ],
#["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
#  97 , weight(6)|difficulty(11)|spd_rtng(87) | weapon_length(69)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
#["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
#  101 , weight(7)|difficulty(12)|spd_rtng(86) | weapon_length(69)|swing_damage(41, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
#["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
#  290 , weight(9)|difficulty(14)|spd_rtng(83) | weapon_length(68)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
#["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 25, 0),
#  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick,
#[], all_euro_factions  ],
#["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
#  get_w_price(79, get_mace_weight(79), get_1hmace_speed(79), 16, 0),
#  weight(get_mace_weight(79))|difficulty(0)|spd_rtng(get_1hmace_speed(79)) | weapon_length(79)|swing_damage(16 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace,
#[], all_euro_factions  ],
#["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 25, 0),
#  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick,
#[], all_euro_factions  ],
#["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#  get_w_price(64, get_mace_weight(64), get_1hmace_speed(64), 27, 0),
#  weight(get_mace_weight(64))|difficulty(0)|spd_rtng(get_1hmace_speed(64)) | weapon_length(64)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick,
#[], all_euro_factions  ],
#["morningstar",         "Flanged Mace", [("bb_serbian_flanged_mace_1",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_axe_left_hip,
#  get_w_price(87, get_mace_weight(87), get_1hmace_speed(87), 31, 0),
#  weight(get_mace_weight(87))|difficulty(13)|spd_rtng(get_1hmace_speed(87)) | weapon_length(87)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace,
#[], all_euro_factions  ],

## modded2x begin, item by anon 1257AD

  ["hammer", "One Handed Long Danish Axe", [("axe_d", imodbits_none), ("axe_d_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(43008)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(71), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["wooden_stick", "European Arming Sword", [("bb_arming_sword", imodbits_none), ("bb_arming_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["winged_mace", "One Handed Angle Axe", [("axe_c", imodbits_none), ("axe_c_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(41984)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["spiked_mace", "One Handed Hooked Axe", [("axe_b", imodbits_none), ("axe_b_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(39936)|spd_rtng(87)|abundance(100)|weight(1.875)|swing_damage(27, cut)|difficulty(6)|weapon_length(58), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["military_hammer", "One Handed Broad Axe", [("axe_a", imodbits_none), ("axe_a_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(39936)|spd_rtng(87)|abundance(100)|weight(1.875)|swing_damage(27, cut)|difficulty(6)|weapon_length(56), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["maul", "Winged Glaive", [("glaive3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 400, thrust_damage(35, pierce)|hit_points(40960)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(155), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sledgehammer", "Long Glaive", [("1429_bill_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 520, thrust_damage(41, pierce)|hit_points(35840)|spd_rtng(69)|abundance(100)|weight(6.2)|swing_damage(51, cut)|difficulty(12)|weapon_length(219), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["warhammer", "One Handed Boarding Axe", [("mackie_tomahawk", imodbits_none), ("mackie_tomahawk_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(36864)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(45), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["pickaxe", "One Handed Cutting Axe", [("heavy_cutting_axe", imodbits_none), ("heavy_cutting_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(36864)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(47), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["spiked_club", "One Handed Old Axe", [("gael_beard_axe", imodbits_none), ("gael_beard_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(43008)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(47), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["fighting_pick", "One Handed Small Bearded Axe", [("vik_axe_f", imodbits_none), ("vik_axe_f_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 170, hit_points(36864)|spd_rtng(88)|abundance(100)|weight(1.75)|swing_damage(26, cut)|difficulty(6)|weapon_length(54), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["military_pick", "One Handed Small Danish Axe", [("vik_axe_e", imodbits_none), ("vik_axe_e_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 170, hit_points(36864)|spd_rtng(88)|abundance(100)|weight(1.75)|swing_damage(26, cut)|difficulty(6)|weapon_length(50), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["morningstar", "Winged Mace", [("newmace_bronze3", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_sword_left_hip|itc_cleaver|itc_parry_polearm, 1250, hit_points(31744)|spd_rtng(80)|abundance(25)|weight(5.0)|swing_damage(36, blunt)|difficulty(12)|weapon_length(85), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

## modded2x end


#["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
#  9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(53)|swing_damage(22 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
#["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
#  14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(29)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
#["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
#  18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword ],
#["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
#  23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(61)|swing_damage(25 , cut) | thrust_damage(30 ,  pierce),imodbits_sword ],
#["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
#  37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_high ],
#["nordic_sword", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
#["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
#  get_w_price(71, get_w_weight(71), get_1hw_speed(71), 41, 5),
#  weight(get_w_weight(71))|difficulty(8)|spd_rtng(get_1hw_speed(71)) | weapon_length(71)|swing_damage(41 , cut) | thrust_damage(5 ,  pierce),imodbits_sword,
#[], all_euro_factions  ],
##["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
##["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
##108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
#["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(97, get_w_weight(97), get_1hw_speed(97), 38, 0),
#  weight(get_w_weight(97))|difficulty(0)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
# [], eastern_factions],
#["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(100, get_w_weight(100), get_1hw_speed(100), 39, 0),
#  weight(get_w_weight(100))|difficulty(0)|spd_rtng(get_1hw_speed(100)) | weapon_length(100)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
# [], eastern_factions],

### modded2x begin, item by anon 1257AD

  ["sickle", "Hoe", [("war_hoe", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_unbalanced|itp_no_blur, itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itc_parry_polearm, 50, hit_points(33792)|spd_rtng(80)|abundance(100)|weight(1.5)|swing_damage(30, cut)|weapon_length(100), imodbit_cracked|imodbit_bent],

  ["cleaver", "One Handed Chopping Axe", [("vik_throwing_axe", imodbits_none), ("vik_throwing_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 155, hit_points(36864)|spd_rtng(91)|abundance(100)|weight(1.375)|swing_damage(23, cut)|difficulty(6)|weapon_length(37), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["knife", "Seax", [("seax_1_1", imodbits_none), ("seax_1_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_wakizashi|itcf_show_holster_when_drawn|itc_longsword, 58, thrust_damage(17, pierce)|hit_points(14336)|spd_rtng(115)|abundance(100)|weight(0.5)|swing_damage(22, cut)|weapon_length(40), imodbit_fine|imodbits_sword_high, [], [fac_culture_welsh, fac_culture_italian, fac_culture_gaelic]],

  ["butchering_knife", "Broad Dagger", [("norman_dagger", imodbits_none), ("norman_dagger_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_longsword, 75, thrust_damage(20, pierce)|hit_points(14336)|spd_rtng(115)|abundance(100)|weight(0.75)|swing_damage(20, cut)|weapon_length(44), imodbit_fine|imodbits_sword_high],

  ["dagger", "Scian", [("scian", imodbits_none), ("scian_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_overswing_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itcf_overswing_spear|itcf_overswing_musket|itcf_thrust_musket|itc_parry_onehanded, 250, thrust_damage(30, pierce)|hit_points(14336)|spd_rtng(115)|abundance(100)|weight(0.5)|swing_damage(15, cut)|weapon_length(54), imodbit_fine|imodbits_sword_high, [], [fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_gaelic, fac_culture_scotish, fac_culture_western]],

  ["falchion", "Straight Falchion", [("falchion_1", imodbits_none), ("falchion_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(25600)|spd_rtng(90)|abundance(40)|weight(2.75)|swing_damage(34, cut)|difficulty(9)|weapon_length(72), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["scimitar", "Falchion", [("falchion_2", imodbits_none), ("falchion_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(26, cut)|hit_points(34816)|spd_rtng(87)|abundance(40)|weight(3.25)|swing_damage(36, cut)|difficulty(9)|weapon_length(74), imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["scimitar_b", "Arabic Sabre", [("sword_arabic_1", imodbits_none), ("sword_arabic_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(22, cut)|hit_points(38912)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(91), imodbit_fine|imodbits_sword_high, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],


### modded2x end



["arabian_sword_a",         "Saracen Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(97, get_w_weight(97), get_1hw_speed(97), 36, 19),
  weight(get_w_weight(97))|difficulty(0)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(36 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high,
  [], arab_factions],
["arabian_sword_b",         "Saracen Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(97, get_w_weight(97), get_1hw_speed(97), 30, 25),
  weight(get_w_weight(97))|difficulty(0)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high,
  [], arab_factions],
["sarranid_cavalry_sword",         "Saracen Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(105, get_w_weight(105), get_1hw_speed(105), 39, 9),
  weight(get_w_weight(105))|difficulty(0)|spd_rtng(get_1hw_speed(105)) | weapon_length(105)|swing_damage(39 , cut) | thrust_damage(9 ,  pierce),imodbits_sword_high,
  [], arab_factions],
["arabian_sword_d",         "Saracen Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(97, get_w_weight(97), get_1hw_speed(97), 37, 20),
  weight(get_w_weight(97))|difficulty(0)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(37 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high,
  [], arab_factions],
["andalusian_sword",         "Andalusian Sword", [("andalusian_sword",0),("scab_andalusian_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(96, get_w_weight(96), get_1hw_speed(96), 35, 18),
  weight(get_w_weight(96))|difficulty(0)|spd_rtng(get_1hw_speed(96)) | weapon_length(96)|swing_damage(35 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high,
  [], andalusian_factions],


#["nomad_sabre",         "Nomad Sabre", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 115 , weight(1.75)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],

# ["great_sword",         "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 # 423 , weight(2.75)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(56 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],

# ["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 # 524 , weight(3)|difficulty(11)|spd_rtng(75) | weapon_length(120)|swing_damage(60 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],

  ["hatchet", "One Handed Thin Axe", [("vik_einhendi_hoggox", imodbits_none), ("vik_einhendi_hoggox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 165, hit_points(32768)|spd_rtng(89)|abundance(100)|weight(1.625)|swing_damage(25, cut)|difficulty(6)|weapon_length(47), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["long_spiked_mace", "Long Spiked Mace", [("spikemace3", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_sword_left_hip|itc_cleaver|itc_poleaxe, 750, thrust_damage(35, pierce)|hit_points(81744)|spd_rtng(82)|abundance(25)|weight(4.0)|swing_damage(34, blunt)|difficulty(9)|weapon_length(98), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],



#["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#  13 , weight(2)|difficulty(0)|spd_rtng(102) | weapon_length(60)|swing_damage(16 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
#65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
# 129 , weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
#240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
#264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

# talak items
["talak_warhammer", "Warhammer", [("warhammer", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_longsword,
  get_w_price(76, get_mace_weight(76), get_1hmace_speed(76), 30, 10),
  weight(get_mace_weight(69))|abundance(2)|difficulty(7)|spd_rtng(get_1hmace_speed(69))|weapon_length(69)|thrust_damage(10, blunt)|swing_damage(30, blunt), imodbits_pick ],

  ["talak_bastard_sword", "Godenak", [("falchion_godenak", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_sword_left_hip|itc_longsword, 1750, thrust_damage(22, blunt)|spd_rtng(84)|abundance(25)|weight(3.0)|swing_damage(38, cut)|difficulty(12)|weapon_length(72), imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_rus]],

# ["talak_morningstar", "Two-Handed_Morningstar", [("talak_morningstar", 0)], itp_type_two_handed_wpn|itp_wooden_attack|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_spear|itc_nodachi,
  # 401, weight(get_mace_weight(90))|abundance(1)|difficulty(12)|spd_rtng(72)|weapon_length(90)|swing_damage(30, pierce), imodbits_pick ],
# ["talak_mace", "Flanged_Mace", [("talak_mace", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
 # get_w_price(74, get_mace_weight(74), get_1hmace_speed(74), 27, 0),
 # weight(get_mace_weight(74))|abundance(30)|spd_rtng(get_1hmace_speed(74))|weapon_length(74)|swing_damage(27, blunt), imodbits_pick ],
# ["talak_seax", "Seax", [("talak_seax", 0, 0), ("talak_scab_seax", ixmesh_carry)], itp_merchandise | itp_type_one_handed_wpn|itp_secondary|itp_merchandise|itp_primary, itcf_carry_dagger_front_left|itc_longsword|itcf_show_holster_when_drawn|itcf_horseback_thrust_onehanded, 93, weight(1.00)|spd_rtng(110)|weapon_length(50)|thrust_damage(16, pierce)|swing_damage(16, cut), imodbits_sword_high ],
# ["talak_long_mace", "Two-Handed_Mace", [("talak_long_mace", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_axe_back|itc_nodachi,
  # 520, weight(2.50)|abundance(1)|spd_rtng(58)|weapon_length(96)|swing_damage(28, blunt), imodbits_pick ],

#["raf_one_handed_axe_a", "One Handed Axe", [("vik_einhendi_danox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(67, get_axe_weight(67), get_1haxe_speed(67), 31, 0),
#  weight(get_axe_weight(67))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(67))|weapon_length(67)|swing_damage(31, pierce), imodbits_pick ],
#["raf_one_handed_axe_b", "One Handed Axe", [("vik_einhendi_breithofudox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(70, get_axe_weight(70), get_1haxe_speed(70), 33, 0),
#  weight(get_axe_weight(70))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(70))|weapon_length(70)|swing_damage(33, pierce), imodbits_pick ],
#["raf_one_handed_axe_c", "One Handed Axe", [("vik_einhendi_haloygox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(67, get_axe_weight(67), get_1haxe_speed(67), 31, 0),
#  weight(get_axe_weight(67))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(67))|weapon_length(67)|swing_damage(31, pierce), imodbits_pick ],
#["raf_one_handed_axe_d", "One Handed Axe", [("vik_einhendi_hedmarkrox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(52, get_axe_weight(52), get_1haxe_speed(52), 24, 0),
#  weight(get_axe_weight(52))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(52))|weapon_length(52)|swing_damage(24, pierce), imodbits_pick ],
#["raf_one_handed_axe_e", "One Handed Axe", [("vik_einhendi_trondrox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(67, get_axe_weight(67), get_1haxe_speed(67), 31, 0),
#  weight(get_axe_weight(67))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(67))|weapon_length(67)|swing_damage(31, pierce), imodbits_pick ],
#["raf_one_handed_axe_f", "One Handed Axe", [("vik_einhendi_vendelox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(50, get_axe_weight(50), get_1haxe_speed(50), 23, 0),
#  weight(get_axe_weight(50))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(50))|weapon_length(50)|swing_damage(23, pierce), imodbits_pick ],
#["raf_one_handed_axe_g", "One Handed Axe", [("vik_hoggox", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(48, get_axe_weight(48), get_1haxe_speed(48), 22, 0),
#  weight(get_axe_weight(48))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(48))|weapon_length(48)|swing_damage(22, pierce), imodbits_pick ],
#["raf_one_handed_axe_h", "Bearded_Axe", [("talak_bearded_axe", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
#  get_w_price(55, get_axe_weight(55), get_1haxe_speed(55), 25, 0),
#  weight(get_axe_weight(55))|abundance(20)|difficulty(7)|spd_rtng(get_1haxe_speed(55))|weapon_length(55)|swing_damage(25, pierce), imodbits_pick ],

#["raf_two_handed_axe_a", "Two_Handed_Axe", [("vik_tveirhendr_hedmarkox", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_axe_back|itc_nodachi,
#  get_w_price(94, get_axe_weight(94), get_2haxe_speed(94), 43, 0),
#  weight(get_axe_weight(94))|abundance(25)|difficulty(10)|spd_rtng(get_2haxe_speed(94))|weapon_length(94)|swing_damage(43, pierce), imodbits_pick ],
#["raf_two_handed_axe_b", "Two_Handed_Axe", [("vik_tveirhendr_danox", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_axe_back|itc_nodachi,
#  get_w_price(94, get_axe_weight(94), get_2haxe_speed(94), 43, 0),
#  weight(get_axe_weight(94))|abundance(25)|difficulty(10)|spd_rtng(get_2haxe_speed(94))|weapon_length(94)|swing_damage(43, pierce), imodbits_pick ],
#["raf_two_handed_axe_c", "Nordic_Axe", [("talak_nordic_axe", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_axe_back|itc_nodachi,
#  get_w_price(98, get_axe_weight(98), get_2haxe_speed(98), 45, 0),
#  weight(get_axe_weight(98))|abundance(2)|difficulty(12)|spd_rtng(get_2haxe_speed(98))|weapon_length(98)|swing_damage(45, pierce), imodbits_pick ],

#["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
# get_w_price(71, get_mace_weight(71), get_1hmace_speed(71), 31, 0),
# weight(get_mace_weight(71))|difficulty(0)|spd_rtng(get_1hmace_speed(71)) | weapon_length(71)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
#  [], byzantine_factions ],

#["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
# get_w_price(71, get_axe_weight(71), get_1haxe_speed(71), 32, 0),
# weight(get_axe_weight(71))|difficulty(9)|spd_rtng(get_1haxe_speed(71)) | weapon_length(71)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
# [], byzantine_factions ],
#["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
# get_w_price(70, get_axe_weight(70), get_1haxe_speed(70), 31, 0),
# weight(get_axe_weight(70))|difficulty(9)|spd_rtng(get_1haxe_speed(70)) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe,
#  [], byzantine_factions ],

#["sword_type_xii", "Counter Point Series Type XII Sword", [("sword_type_xii_low", 0, 0), ("sword_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(95, get_w_weight(95), get_1hw_speed(95), 36, 22),
#  weight(get_w_weight(95))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(95))|weapon_length(95)|thrust_damage(22, pierce)|swing_damage(36, cut), imodbits_sword_high,
#  [], all_euro_factions ],
#["sword_type_xiia", "Counter Point Series Type XIIA Sword", [("sword_type_xiia_low", 0, 0), ("sword_bastard_1257_scabbard", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_bastardsword|itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_show_holster_when_drawn|itcf_slashright_onehanded|itcf_thrust_twohanded|itcf_slashleft_onehanded,
#  get_w_price(103, get_w_weight(103), get_2hw_speed(103), 43, 25),
#  weight(get_w_weight(103))|abundance(80)|difficulty(8)|spd_rtng(get_2hw_speed(103))|weapon_length(103)|thrust_damage(25, pierce)|swing_damage(43, cut), imodbits_sword_high,
#  [], all_euro_factions ],

#["sword_type_xiii", "Counter Point Series Type XIII Sword", [("sword_type_xiii_low", 0, 0), ("sword_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(95, get_w_weight(95), get_1hw_speed(95), 36, 22),
#  weight(get_w_weight(95))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(95))|weapon_length(95)|thrust_damage(22, pierce)|swing_damage(36, cut), imodbits_sword_high,
#  [], all_euro_factions ],
#["sword_type_xiiia", "Counter Point Series Type XIIIA Sword", [("sword_type_xiiia_low", 0, 0), ("sword_bastard_1257_scabbard", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_bastardsword|itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_show_holster_when_drawn|itcf_slashright_onehanded|itcf_thrust_twohanded|itcf_slashleft_onehanded,
#  get_w_price(105, get_w_weight(105), get_2hw_speed(105), 44, 25),
#  weight(get_w_weight(105))|abundance(80)|difficulty(8)|spd_rtng(get_2hw_speed(105))|weapon_length(105)|thrust_damage(25, pierce)|swing_damage(44, cut), imodbits_sword_high,
#  [], all_euro_factions ],
  
#["sword_type_xiiib", "Counter Point Series Type XIIIB Sword", [("sword_type_xiiib_low", 0, 0), ("sword_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(95, get_w_weight(95), get_1hw_speed(95), 36, 22),
#  weight(get_w_weight(95))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(95))|weapon_length(95)|thrust_damage(22, pierce)|swing_damage(36, cut), imodbits_sword_high,
#  [], all_euro_factions ],

#["sword_type_xiv", "Counter Point Series Type XIV Sword", [("sword_type_xiv_low", 0, 0), ("sword_short_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(80, get_w_weight(80), get_1hw_speed(80), 36, 25),
#  weight(get_w_weight(80))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(80))|weapon_length(80)|thrust_damage(36, pierce)|swing_damage(25, cut), imodbits_sword_high,
#  [], all_euro_factions ],

#["cp391_sword", "Counter Point Series Knightly Sword", [("cp391_sword1", 0, 0), ("cp391_sword1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(88, get_w_weight(88), get_1hw_speed(88), 37, 26),
#  weight(get_w_weight(88))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(88))|weapon_length(88)|thrust_damage(26, pierce)|swing_damage(37, cut), imodbits_sword_high,
#  [], all_euro_factions ],

#["spatha", "Spatha", [("spatha", 0, 0), ("spatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(81, get_w_weight(81), get_1hw_speed(81), 32, 33),
#  weight(get_w_weight(81))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(81))|weapon_length(81)|thrust_damage(32, pierce)|swing_damage(33, cut), imodbits_sword_high,
#  [], byzantine_factions  ],
  
#["bb_serbian_sword_1", "Serbian Sword ", [("bb_serbian_sword_1", 0, 0), ("bb_serbian_sword_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(90, get_w_weight(90), get_1hw_speed(90), 34, 20),
#  weight(get_w_weight(90))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(90))|weapon_length(90)|thrust_damage(20, pierce)|swing_damage(34, cut), imodbits_sword_high,
#  [], [fac_kingdom_10]],

#["bb_serbian_sword_5", "Serbian Sword", [("bb_serbian_sword_5", 0, 0), ("bb_serbian_sword_5_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # get_w_price(90, get_w_weight(90), get_1hw_speed(90), 34, 20),
 # weight(get_w_weight(90))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(90))|weapon_length(90)|thrust_damage(20, pierce)|swing_damage(34, cut), imodbits_sword_high,
 # [], [fac_kingdom_10]],

#["bb_rus_sword_6", "Rus Sword", [("bb_rus_sword_6", 0, 0), ("bb_rus_sword_6_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(90, get_w_weight(90), get_1hw_speed(90), 34, 20),
#  weight(get_w_weight(90))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(90))|weapon_length(90)|thrust_damage(20, pierce)|swing_damage(34, cut), imodbits_sword_high,
#  [], [fac_kingdom_10]],

#["bb_rus_sword_1", "Rus Sword", [("bb_rus_sword_1", 0, 0), ("bb_rus_sword_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(90, get_w_weight(90), get_1hw_speed(90), 34, 20),
#  weight(get_w_weight(90))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(90))|weapon_length(90)|thrust_damage(20, pierce)|swing_damage(34, cut), imodbits_sword_high,
#  [], [fac_kingdom_10]],
 
#["bb_rus_sword_3", "Rus Sword", [("bb_rus_sword_3", 0, 0), ("bb_rus_sword_3_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(90, get_w_weight(90), get_1hw_speed(90), 34, 20),
#  weight(get_w_weight(90))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(90))|weapon_length(90)|thrust_damage(20, pierce)|swing_damage(34, cut), imodbits_sword_high,
#  [], [fac_kingdom_10]],

#["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
# 350,
# weight(get_axe_weight(97))|difficulty(10)|spd_rtng(get_2haxe_speed(97)) | weapon_length(97)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high,
# [], latin_factions],
#["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
# 360,
# weight(get_axe_weight(91))|difficulty(0)|spd_rtng(get_1haxe_speed(91)) | weapon_length(91)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
# [], latin_factions],
#["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
# 370,
# weight(get_axe_weight(91))|difficulty(0)|spd_rtng(get_1haxe_speed(91)) | weapon_length(91)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
# [], latin_factions],

#["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
# 340,
# weight(get_w_weight(75))|difficulty(9)|spd_rtng(get_1hw_speed(75)) | weapon_length(75)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],


### modded2x begin, item by anon 1257AD
  ["raf_one_handed_axe_a", "One Handed Danish Axe", [("vik_einhendi_danox", imodbits_none), ("vik_einhendi_danox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(39936)|spd_rtng(87)|abundance(100)|weight(1.875)|swing_damage(27, cut)|difficulty(6)|weapon_length(57), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_b", "One Handed Quarter Axe", [("vik_einhendi_breithofudox", imodbits_none), ("vik_einhendi_breithofudox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(44032)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(72), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_c", "One Handed Bearded Axe", [("vik_einhendi_haloygox", imodbits_none), ("vik_einhendi_haloygox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(39936)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_d", "One Handed Small Axe", [("vik_einhendi_hedmarkrox", imodbits_none), ("vik_einhendi_hedmarkrox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(36864)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(67), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_e", "One Handed Decorated Axe", [("vik_einhendi_trondrox", imodbits_none), ("vik_einhendi_trondrox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 185, hit_points(41984)|spd_rtng(85)|abundance(100)|weight(2.125)|swing_damage(29, cut)|difficulty(6)|weapon_length(67), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_f", "One Handed Battle Axe", [("vik_einhendi_vendelox", imodbits_none), ("vik_einhendi_vendelox_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 180, hit_points(41984)|spd_rtng(86)|abundance(100)|weight(2.0)|swing_damage(28, cut)|difficulty(6)|weapon_length(61), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_g", "One Handed Spiked Axe", [("slim_axe", imodbits_none), ("slim_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 180, hit_points(43008)|spd_rtng(86)|abundance(100)|weight(2.0)|swing_damage(28, cut)|difficulty(6)|weapon_length(62), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_one_handed_axe_h", "One Handed Long Bearded Axe", [("rus_axe_a", imodbits_none), ("rus_axe_a_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(44032)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(72), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_two_handed_axe_a", "Two Handed War Axe", [("vik_tveirhendr_hedmarkrox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(64032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(109), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_two_handed_axe_b", "Two Handed Danish Axe", [("vik_tveirhendr_danox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(44032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(109), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["raf_two_handed_axe_c", "Two Handed GallÃ³glach Axe", [("talak_nordic_axe", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 230, thrust_damage(38, cut)|hit_points(64032)|spd_rtng(76)|abundance(100)|weight(3.25)|swing_damage(38, cut)|difficulty(9)|weapon_length(111), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["sarranid_mace_1", "Billhook", [("1429_guisarme", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 500, thrust_damage(25, blunt)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(207), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace],

  ["sarranid_axe_a", "Glaive-fork", [("1429_lochaber_axe_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(29696)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(188), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sarranid_axe_b", "Hooked Voulge", [("1429_lochaber_axe_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(40960)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sarranid_axe_a", "Glaive-fork", [("1429_lochaber_axe_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(29696)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(188), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sarranid_axe_b", "Hooked Voulge", [("1429_lochaber_axe_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(40960)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_type_xii", "European Arming Sword", [("senlac", imodbits_none), ("senlac_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_type_xiia", "Ornate European Sword", [("alsacian_sword", imodbits_none), ("alsacian_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(45056)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(90), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_type_xiii", "European Arming Sword", [("norman_sword", imodbits_none), ("norman_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_type_xiiia", "European Longsword", [("gaddhjalt", imodbits_none), ("gaddhjalt_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3250, thrust_damage(35, pierce)|hit_points(43008)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(33, cut)|difficulty(9)|weapon_length(104), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_type_xiiib", "European Sword", [("norman_sverd", imodbits_none), ("norman_sverd_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_type_xiv", "Scandinavian Sword", [("the_stamford2", imodbits_none), ("the_stamford2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(36864)|spd_rtng(95)|abundance(10)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["cp391_sword", "Templar Arming Sword", [("bb_templar_sword_a", imodbits_none), ("bb_templar_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(10)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_anatolian_christian]],

  ["spatha", "Spatha", [("sword_balkan_1", imodbits_none), ("sword_balkan_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, cut)|hit_points(39936)|spd_rtng(95)|abundance(40)|weight(2.5)|swing_damage(32, cut)|difficulty(9)|weapon_length(85), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["bb_serbian_sword_1", "European Sidesword", [("sword_euro_5", imodbits_none), ("sword_euro_5_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1700, thrust_damage(30, pierce)|hit_points(37888)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(34, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["bb_serbian_sword_5", "European Arming Sword", [("sword_euro_6", imodbits_none), ("sword_euro_6_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["bb_rus_sword_6", "Rus Shortsword", [("short_rus_sword", imodbits_none), ("scab_short_rus_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 750, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(82), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["bb_rus_sword_1", "Rus Sword", [("sword_rus_6", imodbits_none), ("sword_rus_6_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.5)|swing_damage(32, cut)|difficulty(9)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["bb_rus_sword_3", "Rus Scimitar", [("rus_scimitar", imodbits_none), ("rus_scimitar_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(34816)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(97), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["two_handed_cleaver", "Rus Sword", [("sword_rus_5", imodbits_none), ("sword_rus_5_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(28, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.5)|swing_damage(32, cut)|difficulty(9)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["military_cleaver_b", "Baltic Sword", [("sword_rus_4", imodbits_none), ("sword_rus_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(26, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(93), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["military_cleaver_c", "Baltic Sword", [("sword_rus_3", imodbits_none), ("sword_rus_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(26, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(93), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["military_sickle_a", "One Handed Cavalry Axe", [("rus_cav_axe", imodbits_none), ("rus_cav_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(43008)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(73), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  
### modded2x end

# ["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 # 670 , weight(2.75)|difficulty(10)|spd_rtng(80) | weapon_length(108)|swing_damage(58 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
# ["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 # 1123 , weight(2.75)|difficulty(10)|spd_rtng(75) | weapon_length(118)|swing_damage(60 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],


# ["khergit_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 # get_w_price(112, get_w_weight(112), get_2hw_speed(112), 62, 0),
 # weight(get_w_weight(112))|difficulty(10)|spd_rtng(get_2hw_speed(112)) | weapon_length(112)|swing_damage(62 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
 # [], mongol_factions],
# ["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 # get_w_price(114, get_w_weight(114), get_2hw_speed(114), 64, 0),
 # weight(get_w_weight(114))|difficulty(10)|spd_rtng(get_2hw_speed(114)) | weapon_length(114)|swing_damage(64 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
 # [], mongol_factions],

# ["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 294 , weight(2.0)|difficulty(9)|spd_rtng(93) | weapon_length(98)|swing_damage(43 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# ["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 526 , weight(2.25)|difficulty(9)|spd_rtng(91) | weapon_length(105)|swing_damage(45 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],

# ["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 87 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 142 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 190 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 230 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 550 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


#["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
# 90 , weight(4.5)|difficulty(10)|spd_rtng(92) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
# 152 , weight(4.5)|difficulty(10)|spd_rtng(92) | weapon_length(91)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
  400,
  weight(get_w_weight(99))|difficulty(10)|spd_rtng(get_2hw_speed(99)) | weapon_length(99)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], all_euro_factions ],
  
#["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
# 316 , weight(4.5)|difficulty(10)|spd_rtng(90) | weapon_length(89)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


#["long_axe",         "Long Axe", [("long_danox",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_wooden_parry|itp_next_item_as_melee|itp_merchandise,itc_staff|itcf_carry_axe_back,
#  1300,
#  weight(get_axe_weight(115))|difficulty(10)|spd_rtng(get_2haxe_speed(115)) | weapon_length(115)|swing_damage(53 , cut) | thrust_damage(19 ,  blunt),imodbits_axe,
#  [], nordic_factions + balt_factions],
#["long_axe_alt",         "Long Axe", [("long_danox",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced|itp_merchandise, itc_nodachi|itcf_carry_axe_back,
#  1300,
#  weight(get_axe_weight(115))|difficulty(10)|spd_rtng(get_2haxe_speed(115)) | weapon_length(115)|swing_damage(53 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
#  [], nordic_factions + balt_factions],
#["long_axe_b",         "Long War Axe", [("long_hedmarkox",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_wooden_parry|itp_next_item_as_melee|itp_merchandise, itc_staff|itcf_carry_axe_back,
#  1100,
# weight(get_axe_weight(122))|difficulty(10)|spd_rtng(get_2haxe_speed(122)) | weapon_length(122)|swing_damage(57 , cut) | thrust_damage(18 ,  blunt),imodbits_axe,
#  [], nordic_factions + balt_factions],
#["long_axe_b_alt",         "Long War Axe", [("long_hedmarkox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced|itp_merchandise, itc_nodachi|itcf_carry_axe_back,
#  1100,
#  weight(get_axe_weight(122))|difficulty(10)|spd_rtng(get_2haxe_speed(122)) | weapon_length(122)|swing_damage(57 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
#  [], nordic_factions + balt_factions],
## ["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_merchandise, itc_staff|itcf_carry_axe_back,
## 660 , weight(4.5)|difficulty(10)|spd_rtng(82) | weapon_length(130)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
## ["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
## 660 , weight(4.5)|difficulty(10)|spd_rtng(82) | weapon_length(130)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

## modded2x begin, troop by anon 1257ad
  ["long_axe", "Two Handed Hooked Axe", [("axe_b_2h", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(44032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(106), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["tutorial_battle_axe", "European Shortsword", [("sword_euro_1", imodbits_none), ("sword_euro_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(77), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["long_axe_b", "Two Handed Angle Axe", [("axe_c_2h", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 230, thrust_damage(38, cut)|hit_points(44032)|spd_rtng(76)|abundance(100)|weight(3.25)|swing_damage(38, cut)|difficulty(9)|weapon_length(113), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

  ["tutorial_axe", "European Arming Sword", [("sword_euro_2", imodbits_none), ("sword_euro_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["bardiche", "Bardiche", [("euro_axe_02", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 1000, thrust_damage(45, cut)|hit_points(28697)|spd_rtng(74)|abundance(50)|weight(5.87)|swing_damage(45, cut)|difficulty(12)|weapon_length(95), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_teutonic, fac_culture_rus, fac_culture_baltic]],
## modded2x end

# ["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 # 617 , weight(4.5)|difficulty(10)|spd_rtng(86) | weapon_length(116)|swing_damage(51 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
    # [], eastern_factions ],
#["voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
# 120 , weight(3.0)|difficulty(10)|spd_rtng(76) | weapon_length(176)|swing_damage(51 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],
# ["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_wooden_parry, itc_staff,
  # get_w_price(140, get_axe_weight(140), get_2haxe_speed(140), 66, 0),
  # weight(get_axe_weight(140))|difficulty(11)|spd_rtng(get_2haxe_speed(140)) | weapon_length(140)|swing_damage(66 , cut) | thrust_damage(15 ,  pierce),imodbits_axe,
  # [], eastern_factions ],
# ["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 # 660 , weight(5.0)|difficulty(12)|spd_rtng(80) | weapon_length(155)|swing_damage(42 , cut) | thrust_damage(17 ,  pierce),imodbits_axe,
    # [], eastern_factions ],

#["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,  500,
# weight(get_w_weight(130))|difficulty(0)|spd_rtng(get_polew_speed(130)) | weapon_length(130)|swing_damage(51 , cut) | thrust_damage(15 ,  pierce),imodbits_polearm,
# [], mongol_factions],
#["hafted_blade_a",         "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
#  500,
#  weight(get_w_weight(153))|difficulty(0)|spd_rtng(get_polew_speed(153)) | weapon_length(153)|swing_damage(54 , cut) | thrust_damage(16 ,  pierce),imodbits_polearm,
#  [], mongol_factions],

#["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
#  1000,
#  weight(get_w_weight(114))|difficulty(10)|spd_rtng(get_2hw_speed(114)) | weapon_length(114)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
#  [], all_euro_factions],

## modded2x begin, item by anon 1257AD

  ["hafted_blade_b", "European Shortsword", [("sword_euro_7", imodbits_none), ("sword_euro_7_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(76), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["hafted_blade_a", "European Arming Sword", [("sword_euro_8", imodbits_none), ("sword_euro_8_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["shortened_military_scythe", "European Longsword", [("the_gaddhjalt", imodbits_none), ("the_gaddhjalt_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3250, thrust_damage(35, pierce)|hit_points(43008)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(33, cut)|difficulty(9)|weapon_length(104), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],


## modded2x end


# ["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(41 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# #["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
# ["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 243 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(38 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# ["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 152 , weight(1.5)|difficulty(0)|spd_rtng(108) | weapon_length(82)|swing_damage(35, cut) | thrust_damage(24, pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# ["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 410 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(39 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# ["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 243 , weight(1.5)|difficulty(0)|spd_rtng(108) | weapon_length(81)|swing_damage(35, cut) | thrust_damage(35 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# ["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_1257_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 410 , weight(1.5)|difficulty(0)|spd_rtng(94) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high,
    # [], all_euro_factions ],
# ["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 156 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(103)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_sword,
    # [], all_euro_factions ],

#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

#["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(96, get_w_weight(96), get_1hw_speed(96), 33, 21),
#  weight(get_w_weight(96))|difficulty(0)|spd_rtng(get_1hw_speed(96)) | weapon_length(96)|swing_damage(33 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high,
  #[], balt_factions ] ,
#["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(95, get_w_weight(95), get_1hw_speed(95), 34, 21),
#  weight(get_w_weight(95))|difficulty(0)|spd_rtng(get_1hw_speed(95)) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high,
#  [], balt_factions ],
#["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(82, get_w_weight(82), get_1hw_speed(82), 31, 21),
#  weight(get_w_weight(82))|difficulty(0)|spd_rtng(get_1hw_speed(82)) | weapon_length(82)|swing_damage(31 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high,
#  [], balt_factions ],
#["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(95, get_w_weight(95), get_1hw_speed(95), 36, 21),
#  weight(get_w_weight(95))|difficulty(0)|spd_rtng(get_1hw_speed(95)) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high,
#  [], balt_factions ],
#["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#  get_w_price(82, get_w_weight(82), get_1hw_speed(82), 29, 33),
#  weight(get_w_weight(82))|difficulty(0)|spd_rtng(get_1hw_speed(82)) | weapon_length(82)|swing_damage(29 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high,
#  [], balt_factions ],

## modded2x begin, item by anon 1257AD

  ["sword_viking_1", "Baltic Old Sword", [("sword_rus_1", imodbits_none), ("sword_rus_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 875, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(6)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["sword_viking_2", "Baltic Old Sword", [("sword_rus_2", imodbits_none), ("sword_rus_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 875, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(6)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["sword_viking_2_small", "Baltic Old Shortsword", [("viking_short_sword", imodbits_none), ("viking_short_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 750, thrust_damage(22, pierce)|hit_points(36864)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(75), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

  ["sword_viking_3", "Scandinavian Arming Sword", [("sword_euro_3", imodbits_none), ("sword_euro_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["sword_viking_3_small", "Scandinavian Arming Sword", [("sword_euro_4", imodbits_none), ("sword_euro_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

## modded2x end

#["sword_viking_a_long", "sword_viking_a_long", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ] ,

  ["sword_khergit_1", "Eastern Sword", [("sword_mongol_1", imodbits_none), ("sword_mongol_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.25)|swing_damage(26, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["sword_khergit_2", "Eastern Sabre", [("sword_mongol_2", imodbits_none), ("sword_mongol_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(22, cut)|hit_points(40960)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["sword_khergit_3", "Mongol Sabre", [("sword_mongol_3", imodbits_none), ("sword_mongol_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(24, cut)|hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["sword_khergit_4", "Mongol Sword", [("sword_mongol_4", imodbits_none), ("sword_mongol_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(41984)|spd_rtng(100)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],


  ["mace_1", "HÃ¦ftmace", [("haeftmace", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_blur, itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 380, thrust_damage(34, pierce)|hit_points(64032)|spd_rtng(91)|abundance(50)|weight(3.4)|swing_damage(34, cut)|difficulty(9)|weapon_length(143), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_welsh, fac_culture_nordic, fac_culture_gaelic, fac_culture_scotish]],

  ["mace_2", "Knobbed Mace", [("mace_knobbed", imodbits_none), ("mace_knobbed_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 370, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(2.5)|swing_damage(30, blunt)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["mace_3", "Spiral Mace", [("mace_spiral", imodbits_none), ("mace_spiral_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 370, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(2.5)|swing_damage(30, blunt)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["mace_4", "Iberian Mace", [("Faradon_IberianMace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_mace_left_hip|itc_cleaver|itc_parry_two_handed, 560, hit_points(31744)|spd_rtng(85)|abundance(100)|weight(3.5)|swing_damage(32, blunt)|difficulty(9)|weapon_length(81), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_iberian]],

  ["club_with_spike_head", "Billhook", [("Rathos_bill_hook", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 440, thrust_damage(23, blunt)|hit_points(14029)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(172), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

# Goedendag
 ["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 122 , weight(get_mace_weight(115))|difficulty(9)|spd_rtng(72) | weapon_length(115)|swing_damage(21 , blunt) | thrust_damage(24 ,  pierce),imodbits_mace,
 [], [fac_kingdom_6]],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
  200,
  weight(get_mace_weight(126))|difficulty(0)|spd_rtng(get_1hmace_speed(126)) | weapon_length(126)|swing_damage(59 , blunt) | thrust_damage(6 ,  blunt),imodbits_mace,
  [], eastern_factions ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_merchandise, itc_staff|itcf_carry_axe_back,
  250,
  weight(get_mace_weight(133))|difficulty(0)|spd_rtng(get_1hmace_speed(126)) | weapon_length(133)|swing_damage(62 , blunt) | thrust_damage(7 ,  blunt),imodbits_mace,
  [], eastern_factions ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
  300,
  weight(get_mace_weight(140))|difficulty(0)|spd_rtng(get_1hmace_speed(140)) | weapon_length(140)|swing_damage(66 , blunt) | thrust_damage(8 ,  blunt),imodbits_mace,
  [], eastern_factions ],

["studded_club",         "Studded Club", [("studded_club",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
  260,
  weight(get_mace_weight(92))|difficulty(8)|spd_rtng(get_1hmace_speed(92)) | weapon_length(92)|swing_damage(38 , blunt) | thrust_damage(8 ,  blunt),imodbits_mace,
  [], eastern_factions ],

# ["sarranid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
# 470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(97)|swing_damage(30 , blunt) | thrust_damage(12 ,  blunt),imodbits_mace ],


# ["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 # 45 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(71)|swing_damage(25 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# ["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 250 , weight(1.75)|difficulty(9)|spd_rtng(90) | weapon_length(71)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 # 360 , weight(1.75)|difficulty(9)|spd_rtng(90) | weapon_length(70)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

# ["sarranid_two_handed_axe_a",         "Arab Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 # 350 , weight(3.0)|difficulty(10)|spd_rtng(78) | weapon_length(95)|swing_damage(36 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["sarranid_two_handed_axe_b",         "Arab War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 # 280 , weight(3.0)|difficulty(10)|spd_rtng(83) | weapon_length(90)|swing_damage(38, pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],




["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
  43 , weight(3)|difficulty(0)|spd_rtng(88) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(25 ,  cut),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 19 , weight(3.5)|difficulty(0)|spd_rtng(91) | weapon_length(154)|swing_damage(0 , blunt) | thrust_damage(23,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 153 , weight(4.5)|difficulty(0)|spd_rtng(91) | weapon_length(135)|swing_damage(0 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 282 , weight(4.5)|difficulty(0)|spd_rtng(93) | weapon_length(142)|swing_damage(0 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
# ["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_carry_spear,
# 76 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(36 ,  pierce),imodbits_polearm ],
#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],


#["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(226)|swing_damage(0 , cut) | thrust_damage(12 ,  blunt),imodbits_polearm ],
#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
#["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(5.5)|difficulty(0)|spd_rtng(80) | weapon_length(128)|swing_damage(25 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
  700,
  weight(get_w_weight(160))|difficulty(0)|spd_rtng(get_polew_speed(160)) | weapon_length(160)|swing_damage(52 , cut) | thrust_damage(35 ,  cut),imodbits_polearm,
  [], all_euro_factions ],
# ["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 # 384 , weight(6.5)|difficulty(0)|spd_rtng(77) | weapon_length(180)|swing_damage(37 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
# ["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 # 169 , weight(7)|difficulty(14)|spd_rtng(73) | weapon_length(130)|swing_damage(29 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|difficulty(0)|spd_rtng(94) | weapon_length(128)|swing_damage(10 , blunt) | thrust_damage(8 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|difficulty(0)|spd_rtng(93) | weapon_length(137)|swing_damage(13 , blunt) | thrust_damage(10 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance| itp_primary, itc_staff|itcf_carry_sword_back,
 202 , weight(2)|difficulty(0)|spd_rtng(89) | weapon_length(128)|swing_damage(17 , blunt) | thrust_damage(12 ,  blunt),imodbits_polearm ],

#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


# ["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 # 53 , weight(2.0)|difficulty(0)|spd_rtng(92) | weapon_length(120)|swing_damage(25 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],
# ["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 # 85 , weight(2.25)|difficulty(0)|spd_rtng(90) | weapon_length(135)|swing_damage(25 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],

# ["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 # 140 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(149)|swing_damage(28 , cut) | thrust_damage(38 ,  pierce),imodbits_polearm ],
#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 155 , weight(2.5)|difficulty(10)|spd_rtng(89) | weapon_length(153)|swing_damage(41 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , abundance(100) | weight(4.5)|difficulty(0)|spd_rtng(86) | weapon_length(250)|swing_damage(10 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 135 , abundance(100) | weight(4.75)|difficulty(0)|spd_rtng(85) | weapon_length(255)|swing_damage(10 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , abundance(100) | weight(5.0)|difficulty(10)|spd_rtng(82) | weapon_length(260)|swing_damage(10 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm],
["muslim_lance",         "Heavy Lance", [("muslim_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , abundance(100) | weight(5.0)|difficulty(10)|spd_rtng(80) | weapon_length(262)|swing_damage(11 , cut) | thrust_damage(36 ,  pierce),imodbits_polearm,
 [], arab_factions],
 # ["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 # 410 , weight(5)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear,
# 125 , weight(3.0)|difficulty(0)|spd_rtng(63) | weapon_length(245)|swing_damage(10 , cut) | thrust_damage(38 ,  cut),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
# 205 , weight(3.5)|difficulty(11)|spd_rtng(75) | weapon_length(168)|swing_damage(10 , cut) | thrust_damage(35,  cut),imodbits_polearm ],
#["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 345 , weight(2.25)|difficulty(0)|spd_rtng(76) | weapon_length(165)|swing_damage(10 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
#["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 385 , weight(2.25)|difficulty(0)|spd_rtng(68) | weapon_length(185)|swing_damage(10 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm ],
#["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(30 , cut) | thrust_damage(31 ,  pierce),imodbits_polearm ],
# ["bec_de_corbin_a",         "War Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear,
 # 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

 ["heraldic_lance",         "Heraldic Lance", [("heraldic_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 200 , abundance(100) | weight(2.75)|difficulty(10)|spd_rtng(82) | weapon_length(260)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner_old", "tableau_heraldic_lance_1", ":agent_no", ":troop_no")])]],

 
["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 80 , weight(2.0)|difficulty(0)|spd_rtng(87) | weapon_length(200)|swing_damage(12 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm,
 [], arab_factions],
["berber_spear",         "Berber Spear", [("berber_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 80 , weight(2.0)|difficulty(0)|spd_rtng(87) | weapon_length(200)|swing_damage(12 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm,
  [], arab_factions],
["spear_a",         "Spear", [("vik_atgeirr1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 156 , weight(2.3)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(29 , cut) | thrust_damage(46 ,  pierce),imodbits_polearm ],
["spear_b",         "Spear", [("vik_bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 155 , weight(1.25)|difficulty(0)|spd_rtng(98) | weapon_length(76)|swing_damage(33 , cut) | thrust_damage(51 ,  pierce),imodbits_polearm ],
["spear_c",         "Spear", [("vik_bryntvari2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 135 , weight(2.3)|difficulty(0)|spd_rtng(99) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(45 ,  pierce),imodbits_polearm ],
["spear_d",         "Spear", [("vik_fjadraspjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 143 , weight(2.75)|difficulty(0)|spd_rtng(91) | weapon_length(124)|swing_damage(23 , cut) | thrust_damage(41 ,  pierce),imodbits_polearm ],
["spear_e",         "Spear", [("vik_hoggkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 142 , weight(2.75)|difficulty(0)|spd_rtng(91) | weapon_length(121)|swing_damage(23 , cut) | thrust_damage(41,  pierce),imodbits_polearm ],
["spear_f",         "Spear", [("vik_kastad_krokaspjott",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 146 , weight(2.3)|difficulty(0)|spd_rtng(89) | weapon_length(155)|swing_damage(29 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm ],
["spear_g",         "Spear", [("vik_kastspjottmidtaggir",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 142 , weight(2.3)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(29 , cut) | thrust_damage(46 ,  pierce),imodbits_polearm ],
["spear_h",         "Spear", [("vik_krokaspjott1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 145 , weight(2.75)|difficulty(0)|spd_rtng(90) | weapon_length(152)|swing_damage(22 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["spear_i",         "Spear", [("vik_krokaspjott2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 141 , weight(2.5)|difficulty(0)|spd_rtng(91) | weapon_length(126)|swing_damage(25 , cut) | thrust_damage(41 ,  pierce),imodbits_polearm ],
["spear_j",         "Spear", [("vik_langr_bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 170 , weight(3.70)|difficulty(0)|spd_rtng(91) | weapon_length(192)|swing_damage(17 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["spear_k",         "Spear", [("vik_langr_hoggspjott1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 160 , weight(3.5)|difficulty(0)|spd_rtng(92) | weapon_length(187)|swing_damage(18 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm ],
["spear_l",         "Spear", [("vik_langr_svia",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 170 , weight(3.75)|difficulty(0)|spd_rtng(91) | weapon_length(195)|swing_damage(16 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["spear_m",         "Spear", [("vik_spjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 160 , weight(2.75)|difficulty(0)|spd_rtng(93) | weapon_length(119)|swing_damage(24 , cut) | thrust_damage(41 ,  pierce),imodbits_polearm ],
["spear_n",         "Spear", [("vik_spjotkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 175 , weight(3.75)|difficulty(0)|spd_rtng(88) | weapon_length(193)|swing_damage(16 , cut) | thrust_damage(29 ,  pierce),imodbits_polearm ],
["spear_o",         "Spear", [("vik_svia2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 150 , weight(2.75)|difficulty(0)|spd_rtng(112) | weapon_length(120)|swing_damage(23 , cut) | thrust_damage(41 ,  pierce),imodbits_polearm ],
["spear_p",         "Spear", [("vik_sviar",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 160 , weight(2.3)|difficulty(0)|spd_rtng(94) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(43 ,  pierce),imodbits_polearm ],
# SHIELDS

["wooden_shield", "Wooden Shield",
  [("shield_round_a",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield ],

  ##["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield,
#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["nordic_shield", "Nordic Shield", [("shield_round_b",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (38, 50, 0), weight(2)|hit_points(44)|body_armor(38)|spd_rtng(100)|shield_width(50),imodbits_shield ],

#["kite_shield",         "Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],

# ["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)],
  # itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  # get_shield_price (40, 81, 0), weight(3.5)|hit_points(60)|body_armor(40)|spd_rtng(76)|shield_width(81),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],

# ["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
# 697 , weight(4)|hit_points(70)|body_armor(100)|spd_rtng(61)|shield_width(40),imodbits_shield ],

#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],

# ["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)],
# itp_type_shield, itcf_carry_round_shield,
# 140 , weight(4)|hit_points(33)|body_armor(60)|spd_rtng(90)|shield_width(40),imodbits_shield ],

["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)],
itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price (34, 40, 0), weight(2.5)|hit_points(31)|body_armor(34)|spd_rtng(41)|shield_width(40),imodbits_shield ],

["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)],
itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price (32, 40, 0), weight(2)|hit_points(26)|body_armor(32)|spd_rtng(100)|shield_width(40),imodbits_shield ],

# ["shield_heater_c", "Heater Shield", [("shield_heater_c",0)],
# itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 277 , weight(3.5)|hit_points(41)|body_armor(51)|spd_rtng(80)|shield_width(50),imodbits_shield ],

#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
#["shield_kite_g",         "Kite Shield g", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_h",         "Kite Shield h", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_i",         "Kite Shield i ", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_k",         "Kite Shield k", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)],
# itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
# 118, weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

# ["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)],
 # itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 # 118 , weight(2.5)|hit_points(48)|body_armor(48)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["tab_shield_small_round_n", "Plain Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (35, 40, 0), weight(2)|hit_points(31)|body_armor(35)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
 
["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (shield_t1_res, 50, 0), weight(2.5)|hit_points(35)|body_armor(shield_t1_res)|spd_rtng(93)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],

["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (shield_t2_res, 50, 0), weight(3)|hit_points(41)|body_armor(shield_t2_res)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],

["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],

["tab_shield_round_d", "Well Made Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (shield_t4_res, 50, 0), weight(4)|hit_points(51)|body_armor(shield_t4_res)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_round_e", "Heavy Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
 
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2)|hit_points(31)|body_armor(shield_t4_res)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res+3, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res+3)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2)|hit_points(30)|body_armor(shield_t4_res)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res+3, 30, 50), weight(2.5)|hit_points(36)|body_armor(shield_t4_res+3)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],


 # ["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
# 60 , weight(3.5)|hit_points(51)|body_armor(60)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],

 # ["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
# 114 , weight(4)|hit_points(64)|body_armor(62)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],

 # ["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
# 210 , weight(4.5)|hit_points(76)|body_armor(64)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

 ["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
 get_shield_price (shield_t4_res, 43, 100), weight(5)|hit_points(98)|body_armor(shield_t4_res)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

 ["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (shield_t3_res, 40, 0), weight(2)|hit_points(31)|body_armor(shield_t3_res)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],

 ["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 get_shield_price (shield_t4_res, 40, 0), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],

 ["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+3, 40, 0), weight(3)|hit_points(42)|body_armor(shield_t4_res+3)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],

 ["lit_pavise_a_3", "Lithuanian Shield",   [("lithuanian_shield" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_b_3", "Lithuanian Shield",   [("lithuanian_shield2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_c_3", "Lithuanian Shield",   [("lithuanian_shield3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_d_3", "Lithuanian Shield",   [("lithuanian_shield4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_e_3", "Lithuanian Shield",   [("lithuanian_shield5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_f_3", "Lithuanian Shield",   [("lithuanian_shield6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_g_3", "Lithuanian Shield",   [("lithuanian_shield7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lit_pavise_h_3", "Lithuanian Shield",   [("lithuanian_shield8" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t3_res, 40, 60), weight(5.5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
 ["lithuanian_shield9", "Heavy Lithuanian Shield",   [("lithuanian_shield9" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
  get_shield_price (shield_t4_res, 40, 60), weight(5.5)|hit_points(70)|body_armor(shield_t4_res)|spd_rtng(81)|shield_width(40)|shield_height(60),imodbits_shield,
  [], [fac_kingdom_2]],
  
["arab_shield_a_3", "Saracen Round Shield", [("arab_shield_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_b_3", "Saracen Round Shield", [("arab_shield_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_c_3", "Saracen Round Shield", [("arab_shield_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_d_3", "Saracen Round Shield", [("arab_shield_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_e_3", "Saracen Round Shield", [("arab_shield_e",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_f_3", "Saracen Round Shield", [("arab_shield_f",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_g_3", "Saracen Round Shield", [("arab_shield_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_h_3", "Saracen Round Shield", [("arab_shield_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],
["arab_shield_i_3", "Saracen Round Shield", [("arab_shield_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], arab_factions],

["cuman_shield_a_3", "Cuman Round Shield", [("cuman_shield_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], [fac_kingdom_7]],
["cuman_shield_b_3", "Cuman Round Shield", [("cuman_shield_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], [fac_kingdom_7]],
["cuman_shield_c_3", "Cuman Round Shield", [("cuman_shield_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(54)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
  [], [fac_kingdom_7]],
["talak_buckler", "Buckler", [("talak_buckler", 0)], itp_type_shield|itp_merchandise, itcf_carry_dagger_front_left,
  get_shield_price (24, 32, 0), weight(1.00)|body_armor(24)|hit_points(25)|spd_rtng(140)|weapon_length(32), imodbits_shield,
  [], all_euro_factions],
 ["tab_shield_iberia_c", "Iberian Shield",   [("tableau_shield_iberia" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_iberia_shield", ":agent_no", ":troop_no")])], iberian_factions],
["berber_shield_3", "Berber Shield",   [("berber_shield" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t3_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], berber_factions ], 
 ["byz_shield", "Heavy Byzantine Kite Shield",   [("byz_shield" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t4_res, 36, 70), weight(2.5)|hit_points(51)|body_armor(shield_t4_res)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
  [], byzantine_factions],
["byz_shield_kite", "Kite Shield",   [("tableau_shield_kite_byz" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(5.5)|hit_points(64)|body_armor(shield_t4_res)|spd_rtng(85)|shield_width(40)|shield_height(65),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_byz", ":agent_no", ":troop_no")])],  eastern_factions + balt_factions],
["byz_shield_round", "Round Shield",   [("tableau_shield_round_byz" ,0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+3, 30, 50), weight(5)|hit_points(64)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":agent_no", ":troop_no")])], eastern_factions],
["adarga_a", "Moorish Shield", [("adarga_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t3_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],
["adarga_b", "Moorish Shield", [("adarga_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t3_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],
["byz_shield_1", "Byzantine Shield", [("byz_shield_1",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["byz_shield_2", "Byzantine Shield", [("byz_shield_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["byz_shield_3", "Byzantine Cavalry Shield", [("byz_shield_3",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["byz_shield_4", "Byzantine Infantry Shield", [("byz_shield_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["byz_shield_5", "Byzantine Infantry Shield", [("byz_shield_5",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["rus_shield_1", "Almond Shield",   [("rus_shield_1" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ],
["rus_shield_2", "Almond Shield",   [("rus_shield_2" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ],
["reiforced_shield_horse", "Almond Shield",   [("reiforced_shield_horse" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ], 
["reiforced_shield_infantry", "Almond Shield",   [("reiforced_shield_infantry" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ],
["1257_pavise", "Pavise Shield",   [("1257_pavise" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(40)|shield_height(80),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
  
# shields end #########################################################################
  

# ranged begin #########################################################################
["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
560 , weight(4)|difficulty(2)|spd_rtng(89) | shoot_speed(27) | thrust_damage(58,  cut)|max_ammo(5)|weapon_length(65)|accuracy(95),imodbits_thrown,missile_distance_trigger,
  arab_factions ],
# ["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff,
# 560 , weight(1)|difficulty(2)|spd_rtng(102) | swing_damage(16, cut) | thrust_damage(40 ,  pierce)|weapon_length(65),imodbits_thrown,
    # [], arab_factions ],

["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,
155 , weight(5)|difficulty(1)|spd_rtng(95) | shoot_speed(26) | thrust_damage(36,  cut)|max_ammo(7)|weapon_length(32),imodbits_thrown,missile_distance_trigger ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
285 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(25) | thrust_damage(38 ,  cut)|max_ammo(7)|weapon_length(45),imodbits_thrown,missile_distance_trigger ],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_merchandise|itp_type_thrown | itp_primary,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, weight(5)|difficulty(1)|spd_rtng(91) | shoot_speed(28) | thrust_damage(63,  cut)|accuracy(98)|max_ammo(5)|weapon_length(75),imodbits_thrown,missile_distance_trigger ],
# ["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff,
# 300, weight(1)|difficulty(0)|spd_rtng(98) |swing_damage(12, cut)| thrust_damage(36,  pierce)|weapon_length(75),imodbits_polearm ],

["balt_javelin",         "Balt Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_merchandise|itp_type_thrown | itp_primary,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, weight(5)|difficulty(1)|spd_rtng(91) | shoot_speed(28) | thrust_damage(63 ,  cut)|max_ammo(10)|weapon_length(75)|accuracy(98),imodbits_thrown,missile_distance_trigger,
    balt_factions ],
# ["balt_javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff,
# 300, weight(1)|difficulty(0)|spd_rtng(98) |swing_damage(12, cut)| thrust_damage(36,  pierce)|weapon_length(75),imodbits_polearm,
    # [], balt_factions ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
525 , weight(4)|difficulty(2)|spd_rtng(87) | shoot_speed(23) | thrust_damage(72 ,  cut)|max_ammo(5)|weapon_length(65)|accuracy(98),imodbits_thrown,missile_distance_trigger ],
# ["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff,
# 525 , weight(1)|difficulty(1)|spd_rtng(98) | swing_damage(18, cut) | thrust_damage(43 ,  pierce)|weapon_length(75),imodbits_thrown ],

# ["balt_throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_merchandise|itp_type_thrown | itp_primary,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
# 525 , weight(4)|difficulty(2)|spd_rtng(87) | shoot_speed(23) | thrust_damage(72 ,  cut)|max_ammo(10)|weapon_length(65)|accuracy(98),imodbits_thrown,missile_distance_trigger,
    # balt_factions ],
# ["balt_throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff,
# 525 , weight(1)|difficulty(1)|spd_rtng(98) | swing_damage(18, cut) | thrust_damage(43 ,  pierce)|weapon_length(75),imodbits_thrown,
    # [], balt_factions ],

#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(9) | thrust_damage(4 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag,missile_distance_trigger ],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(3.5)|difficulty(0)|spd_rtng(110) | shoot_speed(9) | thrust_damage(13,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(11) | thrust_damage(15 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
 360, abundance(5)|weight(5)|difficulty(2)|spd_rtng(90) | shoot_speed(11) | thrust_damage(35,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown_minus_heavy ],
 ["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
 360, abundance(5)|weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
# ["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
# 490, abundance(5)|weight(5)|difficulty(3)|spd_rtng(89) | shoot_speed(11) | thrust_damage(40,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
# ["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
# 490, abundance(5)|weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
# ["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
# 620, abundance(5)|weight(5)|difficulty(4)|spd_rtng(88) | shoot_speed(11) | thrust_damage(50,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
# ["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
# 620, abundance(5)|weight(1)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],

["hunting_bow",         "Hunting Self Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,
17 , weight(1)|difficulty(0)|spd_rtng(75) | shoot_speed(45) | thrust_damage(5 ,  cut) | accuracy(97),imodbits_bow ],

["short_bow",         "Self Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
58 , weight(1)|difficulty(3)|spd_rtng(70) | shoot_speed(68) | thrust_damage(6 ,  cut  ) | accuracy(95),imodbits_bow ],

["nomad_bow",         "Hun Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
164 , weight(1.25)|difficulty(4)|spd_rtng(60) | shoot_speed(75) | thrust_damage(9 ,  cut) | accuracy(94),imodbits_bow,
  [], mongol_factions + byzantine_factions + [fac_kingdom_7,fac_kingdom_31] ],

  ["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,
145 , weight(1.75)|difficulty(5)|spd_rtng(45) | shoot_speed(82) | thrust_damage(8 ,  cut)|accuracy(91),imodbits_bow,
  [], [fac_kingdom_6,fac_kingdom_4,fac_kingdom_11,fac_kingdom_14,fac_kingdom_9,fac_kingdom_12,fac_kingdom_13]],

["khergit_bow",         "Mongol Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
269 , weight(1.25)|difficulty(6)|spd_rtng(50) | shoot_speed(79) | thrust_damage(8 ,cut)|accuracy(93),imodbits_bow,
 [], mongol_factions],

 ["strong_bow",         "Composite Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
437 , weight(1.25)|difficulty(2)|spd_rtng(47) | shoot_speed(70) | thrust_damage(7, cut)|accuracy(95),imodbit_cracked | imodbit_bent | imodbit_masterwork,
 [], byzantine_factions + arab_factions  + eastern_factions ],

# ["war_bow",         "Warbow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
# 728 , weight(1.5)|difficulty(6)|spd_rtng(40) | shoot_speed(90) | thrust_damage(12 ,cut)|accuracy(83),imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crossbow_new",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
22 , weight(2.25)|difficulty(0)|spd_rtng(45) | shoot_speed(45) | thrust_damage(30 ,  cut)|max_ammo(1),imodbits_crossbow,
    [] ],
["light_crossbow", "Light Crossbow", [("crossbow_new",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
67 , weight(2.5)|difficulty(7)|spd_rtng(35) | shoot_speed(52) | thrust_damage(32 ,  cut)|max_ammo(1),imodbits_crossbow,
    [] ],
["crossbow",         "Crossbow",         [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
182 , weight(3)|difficulty(8)|spd_rtng(30) | shoot_speed(75) | thrust_damage(36,cut)|max_ammo(1),imodbits_crossbow,
    [] ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
349 , weight(3.5)|difficulty(9)|spd_rtng(25) | shoot_speed(80) | thrust_damage(44 ,cut)|max_ammo(1),imodbits_crossbow,
    [] ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
683 , weight(3.75)|difficulty(10)|spd_rtng(20) | shoot_speed(90) | thrust_damage(50 ,cut)|max_ammo(1),imodbits_crossbow,
    [] ],
# ["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(45 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 # [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],


["khergit_war_helmet", "Mongol War Helmet", [("tattered_steppe_cap_a_new",0)],  itp_merchandise|itp_type_head_armor   ,0, 
head_armor_proper_price , 
head_armor_proper,imodbits_cloth,
 [], mongol_factions],
["khergit_guard_helmet", "Mongol Guard Helmet", [("lamellar_helmet_a",0)],  itp_merchandise|itp_type_head_armor   ,0, 
head_armor_proper_price , 
head_armor_proper ,imodbits_cloth,
 [], mongol_factions],
["khergit_cavalry_helmet", "Mongol Cavalry Helmet", [("lamellar_helmet_b",0)],  itp_merchandise|itp_type_head_armor   ,0, 
head_armor_proper_price , 
head_armor_proper ,imodbits_cloth,
 [], mongol_factions],
["khergit_guard_boots",  "Mongol Guard Boots", [("lamellar_boots_a",0)],  itp_merchandise|itp_type_foot_armor | itp_attach_armature,0, 
get_footwear_price(35) , 
weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_cloth,
 [], mongol_factions], 

["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
# ["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 # 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],


# ["heraldic_lance", "Lance", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3454 , tier_5_body_armor ,imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])],
 # euro_factions],

  
["almogavar_sword", "Almogavar Cleaver", [("almogavar_sword", 0),("almogavar_sword_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(51, get_w_weight(51), get_1hw_speed(51), 39, 15),
  weight(get_w_weight(51))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(51))|weapon_length(51)|swing_damage(39, cut)|thrust_damage(15, cut), imodbits_sword,
  [], all_euro_factions ],

["welsh_archer", "Welsh Bowman Tunic", [("welsh_archer",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  get_barmour_price(16,35,8),
  weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], [ fac_kingdom_9] ],

["armenian_knight_a", "Armenian Knight Mail", [("armenian_knight_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],
["armenian_knight_b", "Armenian Knight Mail", [("armenian_knight_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],
["armenian_knight_c", "Armenian Knight Mail", [("armenian_knight_c", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_23]],

["archer_a", "Tunic with Hood", [("archer_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_0_body_armor_price,
  tier_0_body_armor, imodbits_cloth,
  [], all_euro_factions],
["archer_b", "Tunic ", [("archer_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_0_body_armor_price,
  tier_0_body_armor, imodbits_cloth,
  [], all_euro_factions],
["archer_c", "Tunic", [("archer_c",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_0_body_armor_price,
  tier_0_body_armor, imodbits_cloth,
  [], all_euro_factions],

["surcoat_a", "Gambeson", [("surcoat_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["surcoat_b", "Gambeson", [("surcoat_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["surcoat_c", "Gambeson", [("surcoat_c",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["surcoat_d", "Gambeson", [("surcoat_d",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["surcoat_e", "Gambeson", [("surcoat_e",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], all_euro_factions ],
  

["surcoat_f", "Mail", [("surcoat_f", 0)], itp_merchandise| itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], euro_factions],
["surcoat_g", "Cloth Over Mail", [("surcoat_g", 0)], itp_merchandise| itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], euro_factions],

["teu_hbrother_a", "Halbbrudder Surcoat_over_Mail", [("teu_hbrother_a", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_1, fac_kingdom_23 ]],
["teu_hbrother_b", "Halbbrudder Surcoat_over_Mail", [("teu_hbrother_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price,
  tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_1, fac_kingdom_23 ]],
  
["flat_kettle_hat", "Flattop Kettle Hat", [("flat_kettle", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],

["seljuk_horse", "Seljuk Horse", [("seljuk_horse", 0)], itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], [fac_kingdom_22] ],
["seljuk_armour", "Seljuk Armour", [("seljuk_armour", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], [fac_kingdom_22]],
["seljuk_lamellar_a", "Seljuk Lamellar Vest", [("seljuk_lamellar_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor,
  [], [fac_kingdom_22]],
["seljuk_lamellar_b", "Seljuk Lamellar Vest", [("seljuk_lamellar_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor,
  [], [fac_kingdom_22]],

["andalus_helmet_a", "Andalusian Helm", [("andalus_helmet_a", 0)], itp_merchandise|itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], andalusian_factions],

["andalus_infantry_helmet", "Andalusian Helm", [("andalus_infantry_helmet", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], andalusian_factions],

["andalusian_knight", "Andalusian Surcoat over Mail", [("andalusian_knight", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], andalusian_factions],

["gaelic_mail_shirt_a", "Gaelic gambeson", [("gaelic_mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], gaelic_factions],

["targe_1", "Targe",
  [("s_h1",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield,
  [], gaelic_factions],

["highlander_boots_1", "Highlander Boots", [("highlander_boots_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
  get_footwear_price(8),
  weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], gaelic_factions],

["gaelic_byrnie_a", "Gaelic Byrnie", [("gaelic_byrnie_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], gaelic_factions ],
["gaelic_byrnie_b", "Gaelic Byrnie", [("gaelic_byrnie_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], gaelic_factions ],

["genoa_padded_a", "Padded Armour", [("genoa_padded_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_cloth,
  [], latin_factions],
["genoa_padded_b", "Padded Armour", [("genoa_padded_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], latin_factions],
["genoa_padded_c", "Padded Armour", [("genoa_padded_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_cloth,
  [], latin_factions],

["genoa_mail_b", "Genoese Armour", [("genoa_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], latin_factions],
["genoa_mail_c", "Genoese Armour", [("genoa_mail_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], latin_factions],

["andalusian_shield_1", "Old Moorish Shield", [("andalusian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t1_res, 36, 70), weight(2)|hit_points(28)|body_armor(shield_t1_res)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],
["andalusian_shield_2", "Plain Moorish Shield", [("andalusian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t2_res, 36, 70), weight(2.5)|hit_points(36)|body_armor(shield_t2_res)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],
["andalusian_shield_3", "Moorish Shield", [("andalusian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t3_res, 36, 70), weight(3)|hit_points(43)|body_armor(shield_t3_res)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],
["andalusian_shield_4", "Heavy Moorish Shield", [("heavy_adarga",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t4_res, 36, 70), weight(3.5)|hit_points(51)|body_armor(shield_t4_res)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],

["andalusian_helmet_a", "Andalusian Helmet", [("andalusian_helmet_a",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  get_headgear_price(70),
  weight(1.75)|abundance(100)|head_armor(70*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  [], andalusian_factions],
["andalusian_helmet_b", "Iberian Helmet", [("andalusian_helmet_b",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  get_headgear_price(70),
  weight(1.75)|abundance(100)|head_armor(70*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  [], andalusian_factions],



["noble_cloak", "Nobleman Outfit", [("noble_cloak",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 
  tier_0_body_armor_price,
  tier_0_body_armor, imodbits_cloth,
  [], all_euro_factions],

["meghrebi_leather_a", "Meghrebi Padded Armour", [("meghrebi_leather_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], berber_factions],
["meghrebi_leather_b", "Meghrebi Leather Armour", [("meghrebi_leather_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], berber_factions],
["meghrebi_leather_c", "Meghrebi Kaftan with Cape", [("meghrebi_leather_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth,
  [], berber_factions],
["meghrebi_vest", "Meghrebi Kaftan", [("meghrebi_vest", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], berber_factions],
["buff_leather", "Buff Leather Armour", [("buff_leather", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], berber_factions],

["black_guard", "Kaftan", [("black_guard", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],
["black_guard_helmet", "Saracen Fluted Helmet", [("black_guard_helmet", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], andalusian_factions],

["gaelic_mail_shirt_b", "Gaelic Scale", [("gaelic_mail_shirt_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], gaelic_factions],

["surcoat_gaelic", "Gaelic Mail", [("gaelic_surcoat", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [fac_kingdom_13] ],
  
["almohad_robe_a", "Almohad Robe", [("almohad_robe_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_robe_b", "Almohad Robe", [("almohad_robe_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_robe_c", "Almohad Robe", [("almohad_robe_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_robe_d", "Almohad Robe", [("almohad_robe_d", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_padded_a", "Almohad Padded Armour", [("almohad_padded_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_padded_b", "Almohad Padded Armour", [("almohad_padded_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_padded_c", "Almohad Padded Armour", [("almohad_padded_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], andalusian_factions],
["almohad_cavalry_a", "Almohad Cavalry Robe", [("almohad_cavalry_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions], 
["almohad_cavalry_b", "Almohad Cavalry Robe", [("almohad_cavalry_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions], 

["andalusian_archers_vest", "Andalusian Robe", [("andalusianarchers_vest", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions], 
["andalusian_skirmisher_armor", "Andalusian Mail", [("andalusianskirmisher_armor", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor,
  [],andalusian_factions],
["arabian_lamellar", "Felt Vest", [("arabian_lamellar",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_cloth,
  [], arab_factions],

["horse_d","Courser", [("horse_d",0),("horse_d",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(horse_hp)|body_armor(18)|difficulty(3)|horse_speed(45)|horse_maneuver(46)|horse_charge(28)|horse_scale(108),imodbits_horse_basic|imodbit_champion],  

["arab_nobleman_a", "Arabian Nobleman Robe", [("arab_nobleman_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["arab_nobleman_b", "Arabian Nobleman Robe", [("arab_nobleman_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["arab_nobleman_c", "Arabian Nobleman Robe", [("arab_nobleman_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],

["andalusian_heavy_a", "Andalusian Scale Armour", [("andalusian_heavy_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], andalusian_factions],
["andalusian_heavy_b", "Andalusian Scale Armour", [("andalusian_heavy_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], andalusian_factions],

["berber_tunic_a", "Berber Robe", [("berber_tunic_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],
["berber_tunic_b", "Scale Vest", [("berber_tunic_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_cloth,
  [], andalusian_factions],
["berber_tunic_c", "Berber Robe", [("berber_tunic_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], andalusian_factions],

["berber_turban", "Moorish Turban", [("berber_turban",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth,
  [], andalusian_factions],


["iberian_leather_armour_a", "Iberian Leather Armour", [("iberian_leather_armour_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_armor,
  [], latin_factions],
["iberian_leather_armour_b", "Iberian Leather Armour", [("iberian_leather_armour_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_armor,
  [], latin_factions],
["iberian_leather_armour_c", "Iberian Leather Armour", [("iberian_leather_armour_c", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_armor,
  [], latin_factions],

["andalusi_horseman_robe", "Moorish Horseman Robe", [("andalusi_horseman_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], andalusian_factions],

["galloglass_mail", "Gallóglach Mail Armour", [("galloglass_mail",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], andalusian_factions],
["galloglass_padded", "Gallóglach Padded Armour", [("galloglass_padded",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], gaelic_factions],

["baltic_sword", "Baltic Sword", [("baltic_sword",0),("sword_medieval_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(91, get_w_weight(91), get_1hw_speed(91), 34, 0),
  weight(get_w_weight(91))|difficulty(0)|spd_rtng(get_1hw_speed(91)) | weapon_length(91)|swing_damage(34 , cut),imodbits_sword_high,
  [], balt_factions ],

["man_at_arms_a", "Cloth over Aketon", [("man_at_arms_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], all_euro_factions],
["man_at_arms_b", "Rich Cloth over Mail", [("man_at_arms_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], all_euro_factions],
["man_at_arms_c", "Rich Cloth over Mail", [("man_at_arms_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], all_euro_factions],

["arab_padded_vest", "Saracen Padded Vest", [("arab_padded_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions ],
["arab_archer", "Saracen Archer Vest", [("arab_archer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions ],

["mamluk_infantry_lamellar_a", "Mail with Lamellar Vest", [("mamluk_infantry_lamellar_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_cloth,
  [], arab_factions],
["mamluk_infantry_lamellar_b", "Mail with Lamellar Vest", [("mamluk_infantry_lamellar_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_cloth,
  [], arab_factions],

["targe_2", "Targe",
  [("s_h1_1",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield,
  [], gaelic_factions],
["targe_3", "Targe",
  [("s_h1_2",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield,
  [], gaelic_factions],
["targe_4", "Targe",
  [("s_h2",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield,
  [], gaelic_factions],
["targe_5", "Targe",
  [("s_h2_1",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield,
  [], gaelic_factions],
["targe_6", "Targe",
  [("s_h2_2",0)],
  itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
  get_shield_price (35, 50, 0), weight(2)|hit_points(36)|body_armor(35)|spd_rtng(100)|shield_width(50),imodbits_shield,
  [], gaelic_factions],
  
["balt_lamellar_coat_a", "Fur Coat with Lamellar Vest", [("baltic_lamellar_coat_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], balt_factions],
["balt_lamellar_coat_b", "Fur Coat with Lamellar Vest", [("baltic_lamellar_coat_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], balt_factions],
  
["rus_padded", "Eastern Scale Armour", [("rus_padded", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_armor,
  [], eastern_factions],

["baltic_sword_b", "Baltic Sword (Brador)", [("baltic_sword_b",0),("baltic_sword_b_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(94, get_w_weight(91), get_1hw_speed(94), 36, 0),
  weight(get_w_weight(91))|difficulty(0)|spd_rtng(get_1hw_speed(94)) | weapon_length(94)|swing_damage(36 , cut),imodbits_sword_high,
  [], balt_factions ],

["mongol_helmet_a", "Mongol Helmet", [("mongol_helmet_a",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_plate,
  [], mongol_factions ],
["mongol_helmet_b", "Mongol Helmet", [("mongol_helmet_b",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], mongol_factions ],
["mongol_helmet_c", "Mongol Helmet", [("mongol_helmet_c",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], mongol_factions ],
["steppe_helmet", "Eastern Helmet", [("steppe_helmet",0),("inv_steppe_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], mongol_factions ],

["priest_cap_1", "Cap", [("1257_arming_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth, [], all_euro_factions ],

["priest_cap_2", "Cap", [("1257_arming_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_no_price,
  head_armor_no ,imodbits_cloth, [], all_euro_factions ],

["priest_robe_1", "Priest Robe", [("priest_1",0)], itp_merchandise| itp_type_body_armor  |itp_civilian ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth, [], all_euro_factions ],
["priest_robe_2", "Priest Robe", [("priest_2",0)], itp_merchandise| itp_type_body_armor  |itp_civilian ,0,
  tier_1_body_armor_price,
 tier_1_body_armor ,imodbits_cloth ],
["priest_robe_3", "Priest Robe", [("priest_2_1",0)], itp_merchandise| itp_type_body_armor  |itp_civilian ,0,
  tier_1_body_armor_price,
  tier_1_body_armor,imodbits_cloth, [], all_euro_factions ],
  
["surgeon", "Surgeon Outfit", [("surgeon",0)], itp_merchandise| itp_type_body_armor  |itp_civilian ,0,
  tier_1_body_armor_price,
  tier_1_body_armor ,imodbits_cloth ],


["bishop_great_helm", "Bishop Great_Helm", [("bishop_tophelm", 0)], itp_merchandise | itp_type_head_armor|itp_covers_head, 0,
  head_armor_full_price,
  head_armor_full, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions + [ fac_kingdom_23 ] ],
  
["bishop_armour", "Bishop Armour", [("bishop",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_7_body_armor_price,
  tier_7_body_armor ,imodbits_armor,
 [], euro_factions],

["bishop_mitre", "Bishop mittre", [("bishop_mitre",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_average_price,
  head_armor_average ,imodbits_cloth ],
["bishop_staff","Bishop Staff", [("bishop_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],

["varangian_shield_a", "Varangian Shield", [("varangian_shield_a",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["varangian_shield_b", "Varangian Shield", [("varangian_shield_b",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],
["varangian_shield_c", "Varangian Shield", [("varangian_shield_c",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], byzantine_factions],

["byzantine_sabre", "Byzantine Sabre", [("byzantine_sabre",0),("byzantine_sabre_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 39, 0),
  weight(get_w_weight(93))|difficulty(0)|spd_rtng(get_1hw_speed(93)) | weapon_length(93)|swing_damage(39 , cut),imodbits_sword_high,
  [], byzantine_factions ],

["byzantine_sword", "Byzantine Sword", [("byzantine_sword_a", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(93))|weapon_length(93)|thrust_damage(23, pierce)|swing_damage(38, cut), imodbits_sword_high,
  [], byzantine_factions ],

["byzantine_sword_1", "Byzantine Sword", [("byzantine_sword_1", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(98))|weapon_length(95)|thrust_damage(23, pierce)|swing_damage(39, cut), imodbits_sword_high,
  [], byzantine_factions ],
["byzantine_sword_3", "Byzantine Sword", [("byzantine_sword_3", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(100))|weapon_length(94)|thrust_damage(23, pierce)|swing_damage(38, cut), imodbits_sword_high,
  [], byzantine_factions ],
["byzantine_sword_4", "Byzantine Sword", [("byzantine_sword_4", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(98))|weapon_length(95)|thrust_damage(23, pierce)|swing_damage(40, cut), imodbits_sword_high,
  [], byzantine_factions ],
["byzantine_sword_5", "Byzantine Sword", [("byzantine_sword_5", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(99))|weapon_length(94)|thrust_damage(23, pierce)|swing_damage(38, cut), imodbits_sword_high,
  [], byzantine_factions ],
["byzantine_sword_7", "Byzantine Sword", [("byzantine_sword_7", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(100))|weapon_length(95)|thrust_damage(24, pierce)|swing_damage(39, cut), imodbits_sword_high,
  [], byzantine_factions ],
["byzantine_sword_extra", "Byzantine Sword", [("byzantine_sword_extra", 0, 0), ("byzantine_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(93, get_w_weight(93), get_1hw_speed(93), 38, 23),
  weight(get_w_weight(93))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(93))|weapon_length(93)|thrust_damage(25, pierce)|swing_damage(38, cut), imodbits_sword_high,
  [], byzantine_factions ],

["rus_shield_a_3", "Almond Shield",   [("rus_shield_a" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t3_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ], 
["rus_shield_b_3", "Almond Shield",   [("rus_shield_b" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t3_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ], 
["rus_shield_c_3", "Almond Shield",   [("rus_shield_c" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t3_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ], 
["rus_shield_d_3", "Almond Shield",   [("rus_shield_d" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t3_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t3_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], eastern_factions ], 

["cuman_noble_helmet", "Cuman Noble Helmet", [("cuman_noble",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_plate,
  [], eastern_factions],

["ghulam_helmet", "Ghulam Helmet", [("ghulam_helmet",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_plate,
  [], eastern_factions],
  
["ilkhanate_mongol_helmet", "Mongol Helmet", [("ilkhanate_mongol_helmet",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], mongol_factions],

["polski_helm", "Polish Helmet", [("polska_helma",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_proper_price,
  head_armor_proper  ,imodbits_plate,
  [], [fac_kingdom_5]],

["mamluke_helm_b", "Mighfar", [("mamluke_helm_b",0),("inv_mamluke_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], mamluk_factions],

["mongol_helmet_d", "Mongol Leather Helmet", [("mongol_leather_helm",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_proper_price,
  head_armor_proper  ,imodbits_plate,
  [], mongol_factions ],

["nikloskoe_helmet_warrior", "Nikloskoe Helmet", [("nikloskoe_helmet_warrior",0), ("inv_nikloskoe_helmet_warrior",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hevy_price,
  head_armor_hevy  ,imodbits_plate,
  [], eastern_factions ],
["kiev_helmet_2_facemail", "Rus Helmet", [("kiev_helmet_2_facemail",0), ("inv_kiev_helmet_2_facemail",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hevy_price,
  head_armor_hevy  ,imodbits_plate,
  [], eastern_factions ],
["kiev_helmet_1_facemail_1", "Rus Helmet", [("kiev_helmet_1_facemail_1",0), ("inv_kiev_helmet_1_facemail_1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hevy_price,
  head_armor_hevy  ,imodbits_plate,
  [], eastern_factions ],
  
["rus_byzantinenoble_kettle", "Byzantine Kettle_Helm", [("rus_byzantinenoble_kettle",0),("inv_byzantinenoble_kettle",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor,
  [], eastern_factions + byzantine_factions ],

["rus_helmet_a", "Eastern Helmet", [("rus_helmet_a",0),("inv_rus_helmet_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper  ,imodbits_armor,
  [], eastern_factions ],

["rus_infantry_helmet", "Eastern Infantry Helmet", [("rus_infantry_helmet",0), ("inv_rus_infantry_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent  ,imodbits_plate,
  [], eastern_factions ],

["rus_militia_helmet", "Eastern Militia Helmet", [("rus_militia_helmet",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_average_price,
  head_armor_average  ,imodbits_plate,
  [], eastern_factions ],

["rus_noble_helmet", "Yesenovo Helmet", [("rus_noble_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor,
  [], eastern_factions ],

["seljuk_archer_cap", "Seljuk Cap", [("seljuk_archer_cap",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_light_price,
  head_armor_light  ,imodbits_cloth,
  [], byzantine_factions ],
  
["ilkhanate_cap", "Ilkanate Hat", [("ilkhanate_cap",0),("inv_ilkhanate_cap",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_light_price,
  head_armor_light , imodbits_cloth,
  [], mongol_factions ],

["cuman_cap_d", "Cuman Hat Coif", [("cuman_cap_d",0),("inv_cuman_cap_d",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_average_price,
  head_armor_average , imodbits_armor,
  [], [fac_kingdom_7]],

["anatolian_horseman_lamellar", "Anatolian Lamellar Armor", [("anatolian_horseman_lamellar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], byzantine_factions],

["anatolian_leather_lamellar", "Anatolian Leather Lamellar Armor", [("anatolian_leather_lamellar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_armor,
  [], byzantine_factions],

["anatolian_mail", "Anatolian Mail Shirt", [("anatolian_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions],

["arab_headcloth", "Headcloth", [("arab_headcloth",0)], itp_merchandise| itp_type_head_armor,0, 
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth ],

["seljuk_tunic", "Seljuk Tunic With Mail", [("seljuk_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions],
["seljuk_tunic_b", "Seljuk Tunic With Mail", [("seljuk_tunic_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions],
["seljuk_tunic_c", "Seljuk Tunic With Mail", [("seljuk_tunic_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions],

["rus_noble_mail", "Rus Nobleman Mail", [("rus_noble_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], eastern_factions],

["rus_mask_helmet", "Rus Mask Helmet", [("mask_helmet",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
  head_armor_hevy_price,
  head_armor_hevy ,imodbits_plate,
  [], eastern_factions],

["mamluk_lamellar", "Mamluk Lamellar Armour", [("mamluk_lamellar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price,
  tier_6_body_armor ,imodbits_armor,
  [], mamluk_factions],

["rus_leather_scale", "Rus Scale Armour", [("rus_scale_a", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_4_body_armor_price,
  tier_4_body_armor, imodbits_armor,
  [], eastern_factions],
["rus_leather_scale_b", "Rus Leather Scale Armour", [("rus_scale_b", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_armor,
  [], eastern_factions],

["rohatyna", "Rohatyna", [("bear_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 146 , weight(2.6)|difficulty(8)|spd_rtng(95) | weapon_length(155)|swing_damage(32 , cut) | thrust_damage(39 ,  pierce),imodbits_polearm ],

["flat_topped_helmet_a", "Spangen Helmet", [("flattop_a",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], all_euro_factions ],
["flat_topped_helmet_b", "Spangen Helmet", [("flattop_b",0)], itp_merchandise| itp_type_head_armor   ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], all_euro_factions ],

["great_helmet_a", "Great_Helm", [("greathelmet_a", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full , imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["great_helmet_b", "Great_Helm", [("greathelmet_b", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full , imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["great_helmet_c", "Great_Helm", [("greathelmet_c", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full , imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["great_helmet_d", "Creveille", [("greathelmet_d", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper , imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["great_helmet_decorative", "Phrigian_Helm", [("greathelmet_decorative", 0)], itp_merchandise | itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper , imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],

["bill",         "Bill", [("bill",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
  200,
  weight(get_w_weight(128))|difficulty(8)|spd_rtng(get_polew_speed(128)) | weapon_length(128)|swing_damage(43 , cut),imodbits_polearm,
  [], all_euro_factions ],

["almogavar_helmet", "Almoghavar Helmet", [("almogavar_helmet",0)],  itp_type_head_armor |itp_fit_to_head,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], latin_factions],
  
["curonian_helmet", "Curonian Helmet", [("curonian_helmet", 0)], itp_type_head_armor, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], balt_factions ],
  
["balt_padded_a", "Balt Padded Armour", [("balt_padded_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], [fac_kingdom_2]],
["balt_padded_b", "Balt Leather Vest", [("balt_padded_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], [fac_kingdom_2]],
["thomas_padded_armour", "Tomgirtas, the famous drunk warrior padded armor", [("thomas_padded_armour",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_3_body_armor_price,
  tier_3_body_armor, imodbits_cloth,
  [], [fac_kingdom_2]],

["militia_tunic_a", "Militia Tunic", [("militia_tunic_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], all_euro_factions ],
["militia_tunic_b", "Militia Tunic", [("militia_tunic_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], all_euro_factions ],

["rus_militia_padded_a", "Rus Padded Armour", [("rus_militia_padded_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], eastern_factions ],

["little_samogitian","Žemaitukas", [("horse_d",0),("horse_d",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 512,abundance(60)|hit_points(horse_hp)|body_armor(17)|difficulty(3)|horse_speed(45)|horse_maneuver(49)|horse_charge(10)|horse_scale(95),imodbits_horse_basic|imodbit_champion,
[], balt_factions ],  

["kettlehat_a", "Kettle_Helm", [("kettlehat", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], all_euro_factions ],
["kettlehat_b", "Kettle_Helm", [("kettlehat_b", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], all_euro_factions ],
["kettlehat_c", "Kettle_Helm", [("kettlehat_cheek", 0)], itp_merchandise|itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], all_euro_factions ],
  
 ["andalus_marinid_hasfid_elite_a", "Moorish Robe over Mail", [("andalus_marinid_hasfid_elite_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], berber_factions],
 ["andalus_marinid_hasfid_elite_b", "Moorish Robe over Mail", [("andalus_marinid_hasfid_elite_b",0)],  itp_type_body_armor  |itp_covers_legs ,0,
  tier_6_body_armor_price, tier_6_body_armor ,imodbits_armor,
  [], berber_factions],

["berber_kaftan", "Moorish Kaftan", [("berber_kaftan",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], berber_factions],

["berber_mail_a", "Moorish Robe over Mail", [("berber_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], berber_factions],

["berber_mail_b", "Moorish Robe over Mail", [("berber_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], berber_factions],

["seljuk_hauberk_jawshan", "Seljuk Jawshan", [("seljuk_hauberk_jawshan",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_cloth,
  [], arab_factions],

["mamluk_jawshan_leather", "Leather Jawshan", [("mamluk_jawshan_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], arab_factions ],
  
 ["horse_e","Courser", [("horse_e",0),("horse_e",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(horse_hp)|body_armor(18)|difficulty(3)|horse_speed(45)|horse_maneuver(46)|horse_charge(28)|horse_scale(108),imodbits_horse_basic|imodbit_champion],

["gaelic_shirt_blue", "Gaelic Shirt", [("gaelic_shirt_blue",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],

["gaelic_shirt_green", "Gaelic Shirt", [("gaelic_shirt_green_muted",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],

["gaelic_shirt_red", "Gaelic Shirt", [("gaelic_shirt_red",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],

  ["andalusian_helmet_c", "Andalusian Helmet", [("andalusian_helmet_c",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], andalusian_factions],

  ["andalusian_helmet_d", "Andalusian Helmet", [("andalusian_helmet_d",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], andalusian_factions],

["arab_helmet_d", "Saracen Helmet", [("arab_helmet_d",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_armor,
  [], arab_factions],

["mamluk_helm_b", "Tawashi Helmet", [("mamluk_helmet_4",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], mamluk_factions],

["iberian_cleaver", "Iberian Cleaver", [("iberian_cleaver",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 get_w_price(77, get_axe_weight(77), get_1haxe_speed(77), 35, 0),
 weight(get_axe_weight(77))|difficulty(0)|spd_rtng(get_1haxe_speed(77)) | weapon_length(77)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
 [], latin_factions],

["moorish_hat", "Moorish Hat", [("moorish_hat",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
  head_armor_no_price,
  head_armor_no,imodbits_cloth],
  
["alsacian_sword", "Alsatian Sword (Al Mansur)", [("alsacian_sword", 0, 0), ("alsacian_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(90, get_w_weight(90), get_1hw_speed(90), 34, 20),
  weight(get_w_weight(90))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(90))|weapon_length(90)|thrust_damage(20, pierce)|swing_damage(34, cut), imodbits_sword_high,
  [], [fac_kingdom_10]],
["moorish_axe", "Moorish Axe", [("moorish_axe", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
  get_w_price(74, get_axe_weight(74), get_1haxe_speed(74), 33, 0),
  weight(get_axe_weight(74))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(74))|weapon_length(74)|swing_damage(34, pierce), imodbits_pick ],  
  
["kettle_cloth", "Kettle_Helm", [("kettle_cloth", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], all_euro_factions ],

  ["1257_hood", "Hood", [("1257_hood",0),("inv_1257_hood",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_light_price,
  head_armor_light ,imodbits_plate,
  [], all_euro_factions],
  
["rus_helmet", "Rus Helmet", [("rus_helmet",0), ("inv_rus_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], eastern_factions ],  
# ["rus_helmet", "Rus Helmet", [("rus_helmet",0)], itp_merchandise| itp_type_head_armor,0,
  # get_headgear_price(75),
  # weight(1.75)|abundance(100)|head_armor(75*hai)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
  # [], eastern_factions ],
["rus_helmet_1", "Rus Helmet", [("rus_helmet1",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], eastern_factions ],
["rus_helmet_2", "Rus Helmet", [("rus_helmet2",0), ("inv_rus_helmet2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hevy_price,
  head_armor_hevy  ,imodbits_plate,
  [], eastern_factions ],
["rus_helmet_3", "Rus Helmet", [("rus_helmet3",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_hevy_price,
  head_armor_hevy  ,imodbits_plate,
  [], eastern_factions ],
["balt_rus_cap", "Leather Cap", [("balt_rus_hat",0), ("inv_balt_rus_hat",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0,
  head_armor_light_price,
  head_armor_light  ,imodbits_cloth,
  [], eastern_factions ],

["moors_quilted_kaftan_blue", "Moorish Padded Kaftan", [("moors_quilted_kaftan_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], berber_factions ],
["moors_quilted_kaftan_brown", "Moorish Padded Kaftan", [("moors_quilted_kaftan_brown",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], berber_factions ],

["czekan", "Czekan", [("czekan", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
  get_w_price(75, get_axe_weight(75), get_1haxe_speed(75), 35, 0),
  weight(get_axe_weight(75))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(75))|weapon_length(75)|swing_damage(35, pierce), imodbits_pick,
  [], [ fac_kingdom_5, fac_kingdom_8, fac_kingdom_15]],
  
["ilkhanate_kaftan", "Mongol Kaftan", [("mongol_ilkhanate_kaftan",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], mongol_factions ],
["turk_kaftan_beige", "Turkic Kaftan", [("turk_kaftan_beige",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], [fac_kingdom_22, fac_kingdom_7, fac_kingdom_29, fac_kingdom_30, fac_kingdom_15] ],
["turk_kaftan_furtrim", "Turkic Kaftan", [("turk_kaftan_furtrim",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], [fac_kingdom_22, fac_kingdom_7, fac_kingdom_29, fac_kingdom_30, fac_kingdom_15] ],
["turk_kaftan_green", "Turkic Lamellar Armour", [("turk_kaftan_green",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_cloth,
  [], [fac_kingdom_22, fac_kingdom_7, fac_kingdom_29, fac_kingdom_30, fac_kingdom_15] ],
["saracen_mail", "Saracen Mail", [("kau_arabian_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], arab_factions ],  

["jineta_sword", "Jineta Sword", [("jineta_sword", 0, 0), ("jineta_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(96, get_w_weight(96), get_1hw_speed(96), 37, 23),
  weight(get_w_weight(96))|abundance(100)|difficulty(8)|spd_rtng(get_1hw_speed(96))|weapon_length(96)|thrust_damage(23, pierce)|swing_damage(37, cut), imodbits_sword_high,
  [], iberian_factions ],
  
# ["flag_shield_round_1", "Flag Shield", [("flag_shield_round_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],
# ["flag_shield_round_2", "Flag Shield", [("flag_shield_round_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],
# ["flag_shield_round_3", "Flag Shield", [("flag_shield_round_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],

 # ["flag_shield_norman_1", "Flag Shield", [("flag_shield_norman_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],
# ["flag_shield_norman_2", "Flag Shield", [("flag_shield_norman_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],
# ["flag_shield_norman_3", "Flag Shield", [("flag_shield_norman_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],

 
 # ["flag_shield_kite_1", "Flag Shield", [("flag_shield_kite_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],
# ["flag_shield_kite_2", "Flag Shield", [("flag_shield_kite_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],
# ["flag_shield_kite_3", "Flag Shield", [("flag_shield_kite_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 # get_shield_price (shield_t3_res, 50, 0), weight(3.5)|hit_points(47)|body_armor(shield_t3_res)|spd_rtng(87)|shield_width(50),imodbits_shield,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_shield", ":agent_no", ":troop_no")])]],

 

["gaelic_helmet_a", "Gaelic_Helmet", [("gaelic_helmet_a", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head , 0,
  head_armor_average_price,
  head_armor_average, imodbits_cloth,
  [],[fac_kingdom_13]],
["priest_cap_2", "Cap", [("priest_cap_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth, [], all_euro_factions ],

["byz_helmet_b", "Byzantine Helmet", [("byz_helmet_b", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head | itp_covers_beard, 0,
  head_armor_average_price,
  head_armor_average, imodbits_cloth,
  [], byzantine_factions  ],
["pilgrim_hat", "Hat", [("pilgrim_hat",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth, [], all_euro_factions ],
["gaelic_long_tunic_a", "Tunic", [("gaelic_long_tunic_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], gaelic_factions],
["gaelic_long_tunic_b", "Tunic", [("gaelic_long_tunic_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], gaelic_factions],
["gaelic_long_tunic_c", "Tunic", [("gaelic_long_tunic_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth,
  [], gaelic_factions],
["gaelic_shield_a", "Gaelic Infantry Shield", [("gaelic_shield_a",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 get_shield_price (shield_t4_res+2, 50, 0), weight(4.5)|hit_points(55)|body_armor(shield_t4_res+2)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [], gaelic_factions],
["gaelic_shield_b", "Gaelic Shield",   [("gaelic_shield_b" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], gaelic_factions ],
["gaelic_shield_c", "Gaelic Shield",   [("gaelic_shield_c" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
 get_shield_price (shield_t4_res, 30, 50), weight(2.5)|hit_points(37)|body_armor(shield_t4_res)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [], gaelic_factions ],
["rhodok_great_helmet", "Great Helm", [("rhodok_great_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_full_price,
  head_armor_full ,imodbits_plate,
  [], all_euro_factions ],
["rhodok_four_plated_helmet", "Norman Helm", [("rhodok_four_plated_helmet",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], all_euro_factions ],
["rhodok_kettle_hat_c", "Kettle Hat", [("rhodok_kettle_hat_c",0), ("inv_rhodok_kettle_hat_c",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature ,0,
  head_armor_decent_price,
  head_armor_decent ,imodbits_plate,
  [], all_euro_factions ],
["rhodok_nasal_helmet_a", "Norman Helm", [("rhodok_nasal_helmet_a",0), ("inv_rhodok_nasal_helmet_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature ,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], all_euro_factions ],
["saint_thomas_knight", "Order_Mantle", [("saint_thomas_knight",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["lazarus_serjeant_tunic", "Order_Mantle", [("lazarus_serjeant_tunic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["calatrava_knight", "Order_Mantle", [("calatrava_knight",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["santiago_knight", "Order_Mantle", [("santiago_knight",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], [ fac_kingdom_23 ]],
["studden_leather_armour_a", "Padded Leather Armour", [("studden_leather_armour_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], gaelic_factions],
["faris_helmet", "Saracen Helm", [("faris_helmet", 0)], itp_type_head_armor , 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], arab_factions],
["arab_mail_e", "Saracen Lamellar Armour", [("arab_mail_e",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], arab_factions],
["georgian_mail", "Armenian Mail Shirt", [("georgian_mail",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], arab_factions],
["seljuk_scale_a", "Saracen Lamellar Armour", [("seljuk_scale_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], arab_factions],
["balt_shirt_c", "Fur Vest", [("balt_shirt_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor, imodbits_cloth,
  [], balt_factions],
["armenian_mail_b", "Armenian Mail Shirt", [("armenian_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_4_body_armor_price,
  tier_4_body_armor ,imodbits_armor,
  [], byzantine_factions],
["kau_turcopole_a", "Padded Armour", [("kau_turcopole_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], gaelic_factions],
["kau_turcopole_b", "Padded Armour", [("kau_turcopole_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_cloth,
  [], gaelic_factions],
["mamluk_cap", "Seljuk Cap", [("mamluk_cap",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_cloth,
  [], arab_factions ],
["1257_hood", "Hood", [("1257_hood",0),("inv_1257_hood",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hat_price,
  head_armor_hat  ,imodbits_cloth,
  [], all_euro_factions],
["berber_turban_cape", "Berber Turban", [("berber_turban_cape",0),("inv_berber_turban_cape",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hat_price,
  head_armor_hat  ,imodbits_cloth,
  [], andalusian_factions],
["bulgar_warrior_a", "Scale Armour", [("bulgar_warrior_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor ,imodbits_armor,
  [], eastern_factions + byzantine_factions],
["bulgar_warrior_b", " Leather Armour", [("bulgar_warrior_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_cloth,
  [], eastern_factions ],
["bulgar_helm", "Bulgar Helm", [("bulgar_helm",0),("inv_bulgar_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_cloth,
  [], eastern_factions],
["bulgar_helm_b", "Bulgar Helm", [("bulgar_helm_b",0),("inv_bulgar_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_average_price,
  head_armor_average ,imodbits_cloth,
  [], eastern_factions],
["berber_robe_a", "Berber Bobe", [("berber_robe_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], berber_factions],
["berber_robe_b", "Berber Bobe", [("berber_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], berber_factions],
["berber_robe_c", "Berber Bobe", [("berber_robe_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], berber_factions],
["saracen_kaftan_a", "Kaftan", [("saracen_kaftan_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["saracen_kaftan_b", "Kaftan", [("saracen_kaftan_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["saracen_kaftan_c", "Kaftan", [("saracen_kaftan_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["saracen_kaftan_d", "Kaftan", [("saracen_kaftan_d",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], arab_factions],
["rus_hat_with_padding", "Rus Hat", [("rus_hat_with_padding",0),("inv_rus_hat_with_padding",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_light_price,
  head_armor_light, imodbits_cloth,
  [],  eastern_factions ],
["mongol_fur_hat", "Mongol Tribal Hat", [("mongol_fur_hat", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0,
  head_armor_light_price,
  head_armor_light, imodbits_cloth,
  [], mongol_factions],
["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_5_body_armor_price,
  tier_5_body_armor, imodbits_armor,
  [], mongol_factions],
["gaelic_tunic_cape_a", "Gaelic Tunic", [("gaelic_tunic_cape_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  tier_1_body_armor_price,
  tier_1_body_armor, imodbits_cloth,
  [], gaelic_factions ],
["kettle_cloth_cape_b", "Kettle Hat", [("kettle_cloth_cape_b",0),("inv_kettle_cloth_cape_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [],  euro_factions ],
["kettle_cloth_cape", "Kettle Hat", [("kettle_cloth_cape",0),("inv_kettle_cloth_cape",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [],  euro_factions ],
["wenceslav_helmet", "Saint_Wenceslav_Helmet", [("wenceslav_helmet",0),("inv_wenceslav_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  euro_factions ],
["baltic_ponted_helmet", "Balt_Helmet", [("baltic_ponted_helmet",0),("inv_baltic_ponted_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  balt_factions ],
["berber_white_turban", "Turban Helm", [("berber_white_turban",0),("inv_berber_white_turban",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  arab_factions ],
["surcoat_france_b", "Surcoat With Golden Mail", [("surcoat_france_b", 0)], itp_merchandise | itp_type_body_armor|itp_covers_legs, 0, tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [], [ fac_kingdom_10] ],
["byzantine_crown", "Crown", [("byzantine_crown",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_no_price * 100,
  head_armor_no ,imodbits_plate,
  [], eastern_factions],
["rus_coat", "Rus Coat", [("rus_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
  tier_2_body_armor_price,
  tier_2_body_armor ,imodbits_armor,
  [], eastern_factions],
["moor_helmet_a", "Andalusian Helmet", [("moor_helmet_a",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], andalusian_factions],
["moor_helmet_b", "Andalusian Helmet", [("moor_helmet_b",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper,imodbits_plate,
  [], andalusian_factions],
["moor_helmet_c", "Andalusian Helmet", [("moor_helmet_c",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], andalusian_factions],
["moor_helmet_d", "Andalusian Helmet", [("moor_helmet_d",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], andalusian_factions],
["berber_helmet_g", "Berber Helm", [("berber_helmet_g", 0)], itp_type_head_armor | itp_covers_beard, 0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [], andalusian_factions],
["andalusian_helmet_e", "Andalusian Helmet", [("andalusian_helmet_e",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], andalusian_factions],
["megreb_spangen", "Plain_Helm", [("megreb_spangen", 0)], itp_merchandise |itp_type_head_armor, 0,
  head_armor_average_price,
  head_armor_average, imodbits_armor|imodbit_cracked,
  [],  andalusian_factions ],
["mamluke_helm_ventail", "Mamluke Helmet", [("mamluke_helm_ventail",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_average_price,
  head_armor_average ,imodbits_plate,
  [], mamluk_factions],
["mongol_kettle", "Mongol Kettle Hat", [("mongol_kettle",0)], itp_merchandise| itp_type_head_armor,0,
  head_armor_decent_price,
  head_armor_decent ,imodbits_plate,
  [], mongol_factions ],
["kipchak_steppe_helmet", "Kiphak steppe helmet", [("kipchak_steppe_helmet",0),("inv_kipchak_steppe_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_armor|imodbit_cracked,
  [],  mongol_factions ],
["mongol_warrior_de", "Mongol Lamellar Armour", [("mongol_warrior_de",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
  tier_3_body_armor_price,
  tier_3_body_armor ,imodbits_armor,
  [], mongol_factions],

["yaroslav_helmet", "Rus Noble Helmet", [("yaroslav_helmet",0),("inv_yaroslav_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  eastern_factions ],
["polovtsian_helmet", "Volga Bulgar Noble Helmet", [("polovtsian_helmet",0),("inv_polovtsian_helmet",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper, imodbits_armor|imodbit_cracked,
  [],  eastern_factions ],
["byz_helmet_golden", "Byzantine Helmet", [("byz_helmet_golden",0),("inv_byz_helmet_golden",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_proper_price,
  head_armor_proper ,imodbits_plate,
  [], byzantine_factions ],
["nordic_fur_cap", "Nordic Hat", [("nordic_fur_cap", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0,
  head_armor_hat_price,
  head_armor_hat, imodbits_cloth,
  [], eastern_factions],
["gaelic_crown", "Crown", [("gaelic_crown",0)], itp_merchandise| itp_type_head_armor ,0,
  head_armor_no_price * 100,
  head_armor_no ,imodbits_plate,
  [], gaelic_factions],
["helmet_with_feathers", "Winged_Great_Helmet", [("helmet_with_feathers", 0)], itp_merchandise|itp_type_head_armor, 0,
  head_armor_full_price,
  head_armor_full, imodbits_armor|imodbit_cracked,
  [], euro_factions ],
["frenchpepperpot2", "Great_Helm", [("frenchpepperpot2", 0)],  itp_merchandise| itp_type_head_armor| itp_covers_beard,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["frenchpepperpot3", "Great_Helm", [("frenchpepperpot3", 0)],  itp_merchandise| itp_type_head_armor| itp_covers_beard,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["munitionshelm2", "Great_Helm", [("munitionshelm2", 0)],  itp_merchandise| itp_type_head_armor| itp_covers_beard,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["pepperpothelm1", "Great_Helm", [("pepperpothelm1", 0)],  itp_merchandise| itp_type_head_armor| itp_covers_beard,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["munitionshelm1", "Great_Helm", [("munitionshelm1", 0)],  itp_merchandise| itp_type_head_armor| itp_covers_beard,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["frenchpepperpot", "Great_Helm", [("frenchpepperpot", 0)],  itp_merchandise| itp_type_head_armor| itp_covers_beard,0,
  head_armor_hevy_price,
  head_armor_hevy, imodbits_shield|imodbit_crude|imodbit_rusty,
  [], euro_factions ],
["strely","Strely", [("strely",0),("flying_arrow",ixmesh_flying_ammo),("rus_strely_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
  124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(31,cut)|max_ammo(60),imodbits_missile,missile_distance_trigger],
["new_turban_a", "Turban", [("new_turban_a",0),("inv_new_turban_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_plate,
  [], arab_factions ],
["new_turban_b", "Turban", [("new_turban_b",0),("inv_new_turban_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hat_price,
  head_armor_hat ,imodbits_plate,
  [], arab_factions ],
  
["kufia_berber_black", "Berber_Helm", [("kufia_berber_black", 0)], itp_merchandise |itp_type_head_armor|itp_covers_head ,0,
  head_armor_decent_price,
  head_armor_decent, imodbits_armor|imodbit_cracked,
  [],  andalusian_factions ],
["african_spangen", "Spangen_Helm", [("african_spangen", 0)], itp_type_head_armor|itp_covers_head ,0,
  head_armor_average_price,
  head_armor_average, imodbits_armor|imodbit_cracked,
  [], berber_factions ], 
["african_turban", "African Turban", [("african_turban",0)], itp_type_head_armor|itp_covers_head ,0,
  head_armor_light_price,
  head_armor_light ,imodbits_cloth,
  [], berber_factions ], 

["head_african", "African Head", [("head_african",0)],itp_type_head_armor|itp_civilian|itp_covers_head ,0,
  get_headgear_price(3),
  weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
  [], berber_factions ],
["african_hat", "African Hat", [("african_hat",0)],itp_type_head_armor|itp_civilian|itp_covers_head ,0,
  head_armor_no_price,
  head_armor_no,imodbits_cloth,
  [], berber_factions ],
["legs_african", "African Boots", [("legs_african",0)],  itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], berber_factions ],
["hands_african","Hands_African", [("hands_african_L",0)], itp_type_hand_armor,0,
  get_gloves_price(2),
  weight(0.25)|abundance(120)|body_armor(0)|difficulty(0),imodbits_cloth,
  [], berber_factions ], 
  
["african_trousers", "Trousers", [("african_trousers",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  get_footwear_price(2),
  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth,
  [], berber_factions ],
["irish_surcoat", "Surcoat_over_Mail", [("irish_surcoat", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0,
  tier_6_body_armor_price, tier_6_body_armor, imodbits_armor,
  [],gaelic_factions ],
 ["crown_european", "Crown", [("crown_european",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
  get_headgear_price(2) *100,
  weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
  [],euro_factions ],
 ["crown", "Crown", [("crown",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,
  get_headgear_price(2) * 100,
  weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
  [],euro_factions ],
 ["seljuk_hair", "Seljuk Hairstyle", [("seljuk_hair",0)],itp_merchandise|itp_type_head_armor|itp_civilian| itp_fit_to_head| itp_covers_beard,0,
  get_headgear_price(2),
  weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,
  [],arab_factions ],
 ["flag_pole_1","Flag", [("flag_pole_1",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm,40000, 
 weight(80.5)|spd_rtng(60) | weapon_length(155)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner_old","tableau_flag_pole", ":agent_no", ":troop_no")])]],
 ["flag_pole_2","Flag", [("flag_pole_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm,40000, 
 weight(80.5)|spd_rtng(60) | weapon_length(155)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner_old","tableau_flag_pole", ":agent_no", ":troop_no")])]],
 ["flag_pole_3","Flag", [("flag_pole_3",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm,40000, 
 weight(80.5)|spd_rtng(60) | weapon_length(155)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner_old","tableau_flag_pole", ":agent_no", ":troop_no")])]],
 ["cross","Cross", [("true_cross",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm,40000, 
 weight(80.5)|spd_rtng(60) | weapon_length(155)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none,
 []],

 
["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
]
