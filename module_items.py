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
 ["warhorse","War Horse", [("warhorse",0)], itp_merchandise|itp_type_horse, 0, warhorse_price,abundance(warhorse_abundance)|hit_points(warhorse_hp)|body_armor(warhorse_armour)|difficulty(4)|horse_speed(warhorse_speed)|horse_maneuver(warhorse_maneuver)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
 #["charger","Charger", [("charger",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(85)|difficulty(4)|horse_speed(43)|horse_maneuver(warhorse_speed)|horse_charge(32)|horse_scale(115),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],


["warhorse_white", "Barded_Destrier", [("covered_horse_white", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions ],
["warhorse_red", "Barded_Destrier", [("covered_horse_red", 0)], itp_type_horse| itp_merchandise, 0, warhorse_price,abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions ],
["warhorse_blue", "Barded_Destrier", [("covered_horse_blue", 0)], itp_type_horse| itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
# ["warhorse_green", "Barded_Destrier", [("covered_horse_green", 0)], itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
# [], euro_factions ],
["warhorse_yellow", "Barded_Destrier", [("covered_horse_yellow", 0)], itp_type_horse| itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],

["warhorse_player", "Custom_Barded_Destrier", [("covered_horse_player", 0)], itp_type_horse|itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["warhorse_lionel", "Barded_Destrier", [("covered_horse_lionel", 0)], itp_type_horse| itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["warhorse_lethwin", "Barded_Destrier", [("covered_horse_lethwin", 0)], itp_type_horse| itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],

["rnd_horse_01", "Caparisoned Destrier", [("rnd_horse_01", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_02", "Caparisoned Destrier", [("rnd_horse_02", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_03", "Caparisoned Destrier", [("rnd_horse_03", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_04", "Caparisoned Destrier", [("rnd_horse_04", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_05", "Caparisoned Destrier", [("rnd_horse_05", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_06", "Caparisoned Destrier", [("rnd_horse_06", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_07", "Caparisoned Destrier", [("rnd_horse_07", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_08", "Caparisoned Destrier", [("rnd_horse_08", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_09", "Caparisoned Destrier", [("rnd_horse_09", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_10", "Caparisoned Destrier", [("rnd_horse_10", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
[], euro_factions ],
["rnd_horse_11", "Caparisoned Destrier", [("rnd_horse_11", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_12", "Caparisoned Destrier", [("rnd_horse_12", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_13", "Caparisoned Destrier", [("rnd_horse_13", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_14", "Caparisoned Destrier", [("rnd_horse_14", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_15", "Caparisoned Destrier", [("rnd_horse_15", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_16", "Caparisoned Destrier", [("rnd_horse_16", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_17", "Caparisoned Destrier", [("rnd_horse_17", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_18", "Caparisoned Destrier", [("rnd_horse_18", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_19", "Caparisoned Destrier", [("rnd_horse_19", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_20", "Caparisoned Destrier", [("rnd_horse_20", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_21", "Caparisoned Destrier", [("rnd_horse_21", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_22", "Caparisoned Destrier", [("rnd_horse_22", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],
["rnd_horse_23", "Caparisoned Destrier", [("rnd_horse_23", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], euro_factions],

["warhorse_denmark_a", "Danish_Destrier", [("warhorse_denmark_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_4]],

["warhorse_england_a", "English_Destrier", [("warhorse_england_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_devalence", "English_Destrier", [("warhorse_devalence", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_demontfort", "English_Destrier", [("warhorse_demontfort", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_mortimer", "English_Destrier", [("warhorse_mortimer", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_bigod", "English_Destrier", [("warhorse_bigod", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_dewarenne", "English_Destrier", [("warhorse_dewarenne", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_france_a", "French_Destrier", [("warhorse_france_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_9]],
["warhorse_hre_a", "HRE_Destrier", [("warhorse_hre_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_6]],
["warhorse_bohemia", "Bohemian Destrier", [("warhorse_bohemia", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_6]],
["warhorse_hungary_a", "Hungarian_Destrier", [("warhorse_hungary_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_7]],
["warhorse_ireland_a", "Irish_Destrier", [("warhorse_gaelic", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_13]],
["warhorse_lithuania_a", "Lithuanian_Destrier", [("warhorse_lithuania_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_2]],
["warhorse_norway_a", "Norwegian_Destrier", [("warhorse_norway_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_11]],
["warhorse_novgorod_a", "Russian_Destrier", [("warhorse_novgorod_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_8]],
["warhorse_scotland_a", "Scottish_Destrier", [("warhorse_scotland_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_12]],
["warhorse_sweden_a", "Swedish_Destrier", [("warhorse_sweden_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_14]],
["warhorse_przemysl2", "Polish_Destrier", [("warhorse_przemysl2", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_czersk", "Polish_Destrier", [("warhorse_czersk", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_slask_a", "Caparisoned Destrier", [("warhorse_slask_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_siemowit_a", "Caparisoned Destrier", [("warhorse_siemowit_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_poland_a", "Polish_Destrier", [("warhorse_poland_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_poland_b", "Polish_Destrier", [("warhorse_poland_b", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_kaliskie_a", "Polish_Destrier", [("warhorse_kaliskie_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_gslask", "Polish_Destrier", [("warhorse_gslask", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
# ["warhorse_dslask", "Polish_Destrier_REMOVE", [("warhorse_dslask", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  # [], [fac_kingdom_5]],
["warhorse_swietopelk", "Polish_Destrier", [("warhorse_swietopelk", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_pol_a", "Polish_Destrier", [("warhorse_pol_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_pol_b", "Polish_Destrier", [("warhorse_pol_b", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_pol_c", "Polish_Destrier", [("warhorse_pol_c", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_pol_d", "Polish_Destrier", [("warhorse_pol_d", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_pol_e", "Polish_Destrier", [("warhorse_pol_e", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_pol_g", "Polish_Destrier", [("warhorse_pol_g", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["warhorse_swidnica", "Polish_Destrier", [("warhorse_swidnica", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_5]],
["teu_warhorse_c", "Teutonic_Destrier", [("teu_war_horse_c", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_1]],
["teu_warhorse_b", "Teutonic_Destrier", [("teu_war_horse_b", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_1]],
["teu_warhorse_a", "Teutonic_Destrier", [("teu_war_horse_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_1]],
["mon_lamellar_horse_a", "Lamellar_Destrier", [("warhorse_lamellar_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge) | horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], eastern_factions + byzantine_factions ],
["mon_lamellar_horse_b", "Lamellar_Destrier", [("warhorse_lamellar_b", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge) | horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], eastern_factions + byzantine_factions ],
["mon_lamellar_horse_c", "Lamellar_Destrier", [("warhorse_lamellar_c", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge) |horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], eastern_factions + byzantine_factions ],

["kau_montcada_horse", "Montcada Destrier", [("kau_montcada_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_alego_horse", "Alego Destrier", [("kau_alego_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_cervello_horse", "Cervello Destrier", [("kau_cervello_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_cruilles_horse", "Cruilles Destrier", [("kau_cruilles_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_epyres_horse", "Epyres Destrier", [("kau_epyres_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_luna_horse", "Luna Destrier", [("kau_luna_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_reino_horse", "Reino Destrier", [("kau_reino_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],
["kau_urgell_horse", "Urgell Destrier", [("kau_urgell_horse", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], latin_factions ],

["templar_warhorse_a", "Caparisoned Destrier", [("templar_war_horse_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [],[ fac_kingdom_23 ]],

["hospitaller_warhorse_a", "Caparisoned Destrier", [("hospitaller_war_horse_a", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [ fac_kingdom_23 ]],
["hospitaller_warhorse_b", "Caparisoned Destrier", [("hospitaller_war_horse_b", 0)], itp_merchandise|itp_type_horse, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [ fac_kingdom_23 ]],

["warhorse_sarranid","Lamellar War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, warhorse_price,abundance(warhorse_abundance)|hit_points(warhorse_hp)|body_armor(warhorse_armour)|difficulty(4)|horse_speed(warhorse_speed)|horse_maneuver(warhorse_maneuver)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [],  byzantine_factions  ],
["warhorse_steppe","Lamellar War Horse", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, warhorse_price,abundance(warhorse_abundance)|hit_points(warhorse_hp)|body_armor(warhorse_armour)|difficulty(4)|horse_speed(warhorse_speed)|horse_maneuver(warhorse_maneuver)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], mongol_factions ],

["byz_warhorse","Lamellar War Horse", [("byz_warhorse",0)], itp_merchandise|itp_type_horse, 0, warhorse_price,abundance(warhorse_abundance)|hit_points(warhorse_hp)|body_armor(warhorse_armour)|difficulty(4)|horse_speed(warhorse_speed)|horse_maneuver(warhorse_maneuver)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [],  byzantine_factions  ],

["jerusalem_horse", "Caparisoned Destrier", [("jerusalem_horse", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_23] ],
["tripoli_horse", "Caparisoned Destrier", [("tripoli_horse", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_23] ],

["portugal_horse", "Caparisoned Destrier", [("portugal_horse", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_16] ],
["castile_horse", "Caparisoned Destrier", [("castile_horse", 0)], itp_type_horse | itp_merchandise, 0, warhorse_price, abundance(warhorse_abundance)|body_armor(warhorse_armour)|difficulty(4)|hit_points(warhorse_hp)|horse_maneuver(warhorse_maneuver)|horse_speed(warhorse_speed)|horse_charge(warhorse_charge)|horse_scale(warhorse_scale),imodbits_horse_basic|imodbit_champion,
  [], [fac_kingdom_18] ],

  #["camel","Camel", [("camel",0)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(50)|body_armor(14)|difficulty(1)|horse_speed(19)|horse_maneuver(46)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
  # HORSES END

["arrows", "Arrows", [("vik_arrow", imodbits_none), ("vik_arrow", ixmesh_flying_ammo), ("vik_quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 200, thrust_damage(24, cut)|max_ammo(60)|abundance(100)|weight(3.0)|weapon_length(96), imodbit_large_bag, missile_distance_trigger], 
["khergit_arrows", "War Arrows", [("vik_arrow_b", imodbits_none), ("vik_arrow_b", ixmesh_flying_ammo), ("vik_quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 600, thrust_damage(28, cut)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(96), imodbit_large_bag, missile_distance_trigger, [fac_culture_mongol]],
["barbed_arrows", "Barbed Arrows", [("vik_barbed_arrow", imodbits_none), ("vik_barbed_arrow", ixmesh_flying_ammo), ("vik_quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 400, thrust_damage(26, cut)|max_ammo(60)|abundance(75)|weight(3.0)|weapon_length(92), imodbit_large_bag, missile_distance_trigger], 
["bodkin_arrows", "Bodkin Arrows", [("vik_piercing_arrow", imodbits_none), ("vik_piercing_arrow", ixmesh_flying_ammo), ("vik_quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 600, thrust_damage(28, pierce)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(92), imodbit_large_bag, missile_distance_trigger],
["bolts", "Bolts", [("vik_bolt", imodbits_none), ("vik_bolt", ixmesh_flying_ammo), ("vik_bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 300, thrust_damage(25, pierce)|max_ammo(29)|abundance(100)|weight(1.5)|weapon_length(63), imodbit_large_bag, missile_distance_trigger ], 

["strely", "Munitions Arrows", [("vik_munitions_arrow", imodbits_none), ("vik_munitions_arrow", ixmesh_flying_ammo), ("vik_arena_quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical, 100, thrust_damage(22, cut)|max_ammo(60)|abundance(100)|weight(3.0)|weapon_length(96), imodbit_large_bag],

["steel_bolts", "Munitions Bolts", [("vik_munitions_bolt", imodbits_none), ("vik_munitions_bolt", ixmesh_flying_ammo), ("vik_bolt_bag_b", ixmesh_carry)], itp_type_bolts|itp_merchandise, itcf_carry_quiver_right_vertical, 150, thrust_damage(23, cut)|max_ammo(29)|abundance(100)|weight(1.5)|weapon_length(64), imodbit_large_bag,   missile_distance_trigger ],

["cartridges", "Billhook-fork", [("1429_glaive_fork", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

# ["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
# ["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["pilgrim_disguise", "Pilgrim Disguise", [("peasant_man_a",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("hood_new",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,   get_gloves_price(2),   weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth], 
["mail_mittens", "Mail Mittens", [("mail_mittens_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 360, abundance(60)|weight(0.5)|difficulty(6)|body_armor(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],
["scale_gauntlets", "Leather Gloves", [("leather_gloves_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 90, abundance(100)|weight(0.25)|body_armor(2), imodbits_cloth],

["lamellar_gauntlets", "Padded Linen Gloves", [("wantus1_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 180, abundance(60)|weight(0.37)|body_armor(3), imodbits_cloth],

["wrapping_boots", "Ankle Boots", [("wrapping_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["woolen_hose", "Grey Hose", [("peasant_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["hunter_boots", "Blue Hose", [("blue_hose_mod_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["hide_boots", "Green Hose", [("green_hose_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["ankle_boots", "Grey Hose", [("leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 92, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["nomad_boots", "Mongol Boots", [("tied_up_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth],

["leather_boots", "Black Hose", [("green_hose_b_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["splinted_leather_greaves", "Green Hose with Kneecaps", [("hose_kneecops_green", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["mail_chausses", "Mail Chausses", [("mail_chausses_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["splinted_greaves", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["splinted_greaves_long", "Splinted Greaves", [("kua_splinted_greaves_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2520, abundance(100)|weight(4.0)|leg_armor(30)|difficulty(12), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_anatolian_christian, fac_culture_western]],

["mail_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["mail_boots_long", "Mail Boots", [("mail_spurs_cp1257_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["kau_mail_boots_dark", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["kau_mail_boots_dark_long", "Mail Chausses with Padding", [("raf_chausses", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sarranid_boots_a", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["sarranid_boots_a_long", "Black Hose", [("hose_black_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sarranid_boots_b", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["sarranid_boots_b_long", "Black and White Hose", [("hose_grey_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sarranid_boots_c", "Black and White Hose", [("hose_grey_3", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sarranid_boots_d", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["sarranid_boots_d_long", "Mail with Shoes", [("leather_greaves_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["raf_mail_chausses", "Tan Hose", [("hose_tan_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["kau_mail_boots", "Red Hose", [("kau_mail_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["mamluke_boots", "Mamluk Boots", [("mamluke_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["cuman_boots", "Cuman Boots", [("cuman_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_kingdom_7]],

["byz_lord_boots", "Byzantine Boots", [("byz_lord_boots",0)], itp_type_foot_armor | itp_attach_armature  ,0,   get_footwear_price(35),   weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(8) ,imodbits_armor,   [], byzantine_factions], 

["byz_lord_boots_long", "Red Hose with Kneecaps", [("hose_kneecops_red", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["lapcie", "Eastern Wrapping Shoes", [("lapcie", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

["byz_boots_c", "Byzantine Leather Boots", [("byz_leather_boots_c", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_cavalry_boots", "Mail with Boots", [("byz_cavalry_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(24)|difficulty(9), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_anatolian_christian, fac_culture_western]],

["byz_boots_a", "Byzantine Leather Boots", [("byz_leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_boots_b", "Byzantine Leather Boots", [("byz_leather_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byzantine_greaves", "Byzantine Greaves", [("byzantine_greaves", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1200, abundance(100)|weight(2.75)|leg_armor(18)|difficulty(6), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["leather_fur_boots", "Black Hose", [("hose_black_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["red_hose", "Dark Red Hose", [("red_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["green_hose", "Green Hose", [("green_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["grey_hose", "Blue Hose with Wrapping Boots", [("grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["dark_grey_hose", "Grey Hose", [("dark_grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["yellow_hose", "Yellow Hose", [("yellow_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["green_hose_b", "Black Hose", [("green_hose_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["tied_up_shoes", "Green and Purple Hose", [("hose_green_and_purple", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["blue_hose_mod", "Blue Hose", [("blue_hose_mod", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["berber_shoes", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["legs_with_shoes", "Shoes", [("legs_with_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 48, abundance(100)|weight(0.5)|leg_armor(2), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["bare_legs", "Sandals", [("calrad_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 48, abundance(100)|weight(0.5)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_iberian, fac_culture_italian, fac_culture_andalus]],

["shoes", "Boots", [("shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["priest_2_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["blue_hose", "Blue Hose", [("wrapping_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["rus_cav_boots", "Bugged Item", [("invalid_item", imodbits_none)], 0, 0, 0, 0, imodbits_none],

["rus_boots_a", "Rus' Boots", [("rus_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth, [], [fac_culture_rus]],

["rus_boots_b", "Hide Boots", [("hide_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(2.0)|leg_armor(12), imodbits_cloth],

["red_dress", "Red Dress", [("red_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["brown_dress", "Brown Dress", [("brown_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["green_dress", "Green Dress", [("green_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["khergit_lady_dress", "Mongol Lady Dress", [("khergit_lady_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

["khergit_lady_dress_b", "Mongol Leather Lady Dress", [("khergit_lady_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

["sarranid_lady_dress", "Saracen Lady Dress", [("sarranid_lady_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_lady_dress_b", "Saracen Lady Dress", [("sarranid_lady_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_common_dress", "Saracen Dress", [("sarranid_common_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_common_dress_b", "Saracen Dress", [("sarranid_common_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["nomad_armor", "Yellow Rus Tunic", [("rus_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

["khergit_armor", "Black Rus Tunic", [("rus_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mongol]],

["leather_jacket", "Militia Tunic", [("militia_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["rawhide_coat", "Gambeson", [("aketon_acok", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth],

["fur_coat", "Brown Tunic", [("kuauik_dornish_leather_tunic_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["merchant_outfit", "Merchant Outfit", [("nobleman_outfit_b_new", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["blue_dress", "Red Dress", [("blue_dress_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["peasant_dress", "Peasant Dress", [("barkeeper_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["linen_tunic", "Linen Tunic", [("shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["short_tunic", "Tunic With Felt Vest", [("rich_tunic_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["red_shirt", "Linen Tunic", [("kuauik_dornish_leather_tunic_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["robe", "Robe", [("sar_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],


["coarse_tunic", "Tunic", [("coarse_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["leather_vest", "Linen Vest", [("leather_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["steppe_armor", "Steppe Armor", [("lamellar_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

["gambeson_a", "Gambeson", [("gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["gambeson_b", "Gambeson", [("gambeson_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

["gambeson_c", "Gambeson", [("gambeson_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

["gambeson_d", "Gambeson", [("gambeson_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

["padded_cloth", "Aketon", [("padded_cloth_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["leather_jerkin", "Shirt", [("pentoshi_style_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["nomad_vest", "Linen Tunic", [("pentoshi_style_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["ragged_outfit", "Militia Tunic", [("militia_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["tribal_warrior_outfit", "Shirt", [("kuauik_norvoshi_style_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["haubergeon", "Mail Hauberk", [("kau_mail_shirt_cloak", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["lamellar_vest", "Mongolian Gambeson", [("tribal_warrior_outfit_a_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

["lamellar_vest_khergit", "Mongolian Gambeson", [("peltastos_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

["mail_with_surcoat", "Surcoat over Mail Haubergeon", [("rnd_surcoat_12_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["surcoat_over_mail", "Surcoat over Mail Haubergeon", [("rnd_surcoat_15_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["coat_of_plates", "Mail Hauberk", [("norman_short_hauberk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["coat_of_plates_red", "Brown Coat of Plates over Mail", [("coat_of_plates_red_mod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17841, abundance(10)|weight(36.0)|leg_armor(36)|difficulty(15)|body_armor(72), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["pelt_coat", "Blue Rus Tunic", [("rus_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["bishop_cop", "Red Coat of Plates over Mail", [("bishop_CoP", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17841, abundance(10)|weight(36.0)|leg_armor(36)|difficulty(15)|body_armor(72), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["sarranid_cloth_robe", "Worn Robe", [("sar_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["archers_vest", "Archer's Padded Vest", [("archers_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_leather_armor", "Saracen Padded Kaftan", [("kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_cavalry_robe", "Arabic Mail Hauberk", [("cavalle_moro_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arabian_armor_b", "Arabic Mail Hauberk", [("cavalle_moro_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["sarranid_mail_shirt", "Arabic Mail Hauberk", [("cavalle_moro_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["mamluke_mail", "Mamluk Plated Mail", [("sipahi_jawshan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["veteran_surcoat_a", "Surcoat over Mail Haubergeon", [("surcoat_cop_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["veteran_surcoat_b", "Surcoat over Mail Haubergeon", [("surcoat_cop_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["veteran_surcoat_c", "Surcoat over Mail Haubergeon", [("surcoat_cop_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["veteran_surcoat_d", "Surcoat over Mail Haubergeon", [("surcoat_cop_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["veteran_surcoat_e", "Surcoat over Mail Haubergeon", [("surcoat_cop_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["arena_outfit_a", "Surcoat over Mail Haubergeon", [("arena_outfit_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["arena_outfit_b", "Surcoat over Mail Haubergeon", [("arena_outfit_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["arena_outfit_c", "Surcoat over Mail Haubergeon", [("arena_outfit_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["arena_outfit_d", "Surcoat over Mail Haubergeon", [("arena_outfit_yellow", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["kau_aragon_knight", "Aragonian Surcoat over Mail", [("kau_aragon_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

["kau_aragon_a", "Aragonian Surcoat over Mail Haubergeon", [("kau_aragon_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

["kau_aragon_b", "Aragonian Surcoat over Mail", [("kau_aragon_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

["kau_aragon_c", "Aragonian Surcoat over Mail", [("kau_aragon_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17]],

["kau_montcada_surcoat", "Montcada Surcoat over Mail", [("kau_montcada_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_alego_surcoat", "Alego Surcoat over Mail", [("kau_alego_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_cervello_surcoat", "Cervello Surcoat over Mail", [("kau_cervello_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_cruilles_surcoat", "Cruilles Surcoat over Mail", [("kau_cruilles_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_entenca_surcoat", "Entensa Surcoat over Mail", [("kau_entenca_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_epyres_surcoat", "Epyres Surcoat over Mail", [("kau_epyres_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_luna_surcoat", "Luna Surcoat over Mail", [("kau_luna_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_pons_surcoat", "Pons Surcoat over Mail", [("kau_pons_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_castile_knight", "Crown of Castile Surcoat over Mail", [("kau_castile_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

["kau_castile_a", "Crown of Castile Surcoat over Mail Haubergeon", [("kau_castile_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

["kau_castile_b", "Crown of Castile Surcoat over Mail Haubergeon", [("kau_castile_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

["kau_castile_c", "Crown of Castile Surcoat over Mail Haubergeon", [("kau_castile_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_18]],

["kau_santiago", "Santiago Surcoat over Mail Haubergeon", [("kau_santiago", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16, fac_kingdom_17, fac_kingdom_18, fac_kingdom_19]],

["kau_portugal_a", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

["kau_portugal_b", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

["kau_portugal_c", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

["kau_portugal_d", "Portugese Surcoat over Mail Haubergeon", [("kau_portugal_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_16]],

["kau_papal", "Papal Surcoat over Mail Haubergeon", [("kau_papal", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_papacy]],

["kau_sicily_a", "Sicilian Surcoat over Mail Haubergeon", [("kau_sicily_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_24]],

["kau_sicily_b", "Sicilian Surcoat over Mail Haubergeon", [("kau_sicily_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_24]],

["kau_antioch", "Antioch Surcoat over Mail Haubergeon", [("kau_antioch", imodbits_none), ("kau_antioch", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23, fac_kingdom_23]],

["kau_cyprus", "Cyprus Surcoat over Mail Haubergeon", [("kau_cyprus", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["kau_jerusalem", "Jerusalem Surcoat over Mail Haubergeon", [("kau_jerusalem", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["kau_latin_a", "Latin Empire Surcoat over Mail Haubergeon", [("kau_latin_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

["kau_latin_b", "Latin Empire Surcoat over Mail Haubergeon", [("kau_latin_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

["kau_athens", "Latin Empire Surcoat over Mail Haubergeon", [("kau_athens", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

["kau_courtenay", "Latin Empire Surcoat over Mail Haubergeon", [("kau_courtenay", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_26]],

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
["surcoat_denmark_a", "Danish Surcoat over Mail Haubergeon", [("surcoat_denmark_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_4]],

["surcoat_england_a", "English Surcoat over Mail Haubergeon", [("surcoat_england_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

["surcoat_devalence", "English Surcoat over Mail Haubergeon", [("surcoat_devalence", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

["surcoat_demontfort", "English Surcoat over Mail Haubergeon", [("surcoat_demontfort", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

["surcoat_mortimer", "English Surcoat over Mail Haubergeon", [("surcoat_mortimer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

["surcoat_bigod", "English Surcoat over Mail Haubergeon", [("surcoat_bigod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

["surcoat_dewarenne", "English Surcoat over Mail Haubergeon", [("surcoat_dewarenne", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_9]],

["surcoat_france_a", "French Surcoat over Mail Haubergeon", [("surcoat_france_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_10]],

["surcoat_hre_a", "HRE Surcoat over Mail Haubergeon", [("surcoat_hre_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["richard_of_cornwall_surcoat_over_mail", "HRE Surcoat over Mail Haubergeon", [("surcoat_richard_of_cornwall_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["surcoat_bohemia", "Bohemian Surcoat over Golden Mail Haubergeon", [("surcoat_bohemia_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_42]],

["surcoat_hungary_a", "Hungarian Surcoat over Mail Haubergeon", [("surcoat_hungary_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

["surcoat_ireland_a", "Irish Cuir Bouilli over Mail", [("surcoat_gaelic_kingdoms", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_13]],

["surcoat_lithuania_a", "Lithuanian Scale Armour", [("surcoat_lithuania_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_2]],

["surcoat_lithuania_b", "Lithuanian Mail Hauberk", [("surcoat_lithuania_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_2]],

["surcoat_norway_a", "Norwegian Surcoat over Mail Haubergeon", [("surcoat_norway", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_11]],

["surcoat_novgorod", "Novgorod Scale Armour", [("surcoat_novgorod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(60)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["surcoat_scotland_a", "Scottish Surcoat over Mail Haubergeon", [("surcoat_scotland", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_12]],

["surcoat_sweden_a", "Swedish Surcoat over Mail Haubergeon", [("surcoat_sweden_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_14]],

["surcoat_kaliskie", "Polish Surcoat over Mail Haubergeon", [("surcoat_kaliskie_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_poland_a", "Polish Surcoat over Mail Haubergeon", [("surcoat_poland_wb_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["siemowit_surcoat_over_mail", "Polish Surcoat over Mail Haubergeon", [("surcoat_siemowit_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_gslask", "Polish Mail Hauberk with Lamellar Vest", [("surcoat_gslask_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_dslask", "Polish Surcoat over Mail Haubergeon", [("surcoat_dslask_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_mazowsze", "Polish Surcoat over Mail Haubergeon", [("surcoat_mazowsze_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_swidnica", "Polish Surcoat over Mail Haubergeon", [("surcoat_swidnica_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_swietopelk", "Polish Surcoat over Mail Haubergeon", [("surcoat_swietopelk_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_henry3", "Surcoat over Mail Haubergeon", [("surcoat_henry3_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_a", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_b", "Polish Mail Hauberk with Lamellar Vest", [("surcoat_pol_wb_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_c", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_d", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_e", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_f", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_pol_g", "Surcoat over Mail Haubergeon", [("surcoat_pol_wb_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_czersk", "Polish Mail Hauberk with Lamellar Vest", [("surcoat_czersk_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["surcoat_przemysl2", "Polish Surcoat over Mail Haubergeon", [("surcoat_przemysl2_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

["teu_hochmeister_surcoat", "Hochmeister Haubergeon", [("teu_hochmeister_surcoat", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic]],

["teu_brother_surcoat_a", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_brother_surcoat_b", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_brother_surcoat_c", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_brother_surcoat_d", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_brother_surcoat_e", "Teutonic Surcoat over Mail Haubergeon", [("teu_brother_surcoat_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_sariant_mail", "Teutonic Surcoat over Hauberk", [("teu_sariant_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_postulant_a", "HalbbrÃ¼der Surcoat over Mail Haubergeon", [("teu_postulant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_hbrother_mail", "Teutonic Gambeson", [("teu_hbrother_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_sergeant", "Teutonic Gambeson", [("teutonic_sergeant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

["liv_sergeant", "Teutonic Gambeson", [("livonian_sergeant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_monk_surcoat_a", "Livonian Gambeson", [("teu_monk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

["liv_tunic_a", "Livonian Tunic", [("liv_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_gambeson", "Teutonic Gambeson", [("teu_gambeson", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

["teu_coat_of_plates", "White Coat of Plates over Mail", [("teu_coat_of_plates_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17841, abundance(10)|weight(36.0)|leg_armor(36)|difficulty(15)|body_armor(72), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

["scale_shirt_a", "Baltic Scale Shirt", [("raf_scale_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

["kau_padded_mail_a", "White Aketon", [("kau_padded_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_mail_a", "Mail Hauberk", [("kau_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_mail_b", "Mail Hauberk", [("kau_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_haubergeon_a", "Red Aketon", [("kau_haubergeon_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_mail_shirt_a", "Aketon", [("kau_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_mail_shirt_b", "Mail Hauberk", [("kau_mail_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_mail_shirt_c", "Blue Aketon", [("kau_mail_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_mail_shirt_d", "Blue Aketon", [("kau_mail_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["kau_rus_a", "Rus Mail Hauberk", [("kau_rus_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_b", "Eastern Scale Shirt", [("kau_rus_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_d", "Eastern Gambeson", [("kau_rus_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

["kau_rus_scale_a", "Eastern Mail Hauberk with Lamellar Vest", [("kau_rus_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_noble_b", "Eastern Scale Shirt", [("kau_rus_nobleman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(60)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_lamellar_vest", "Leather Lamellar Vest over Mail Hauberk", [("kau_rus_nobleman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_noble_a", "Eastern Mail Hauberk", [("kau_rus_nobleman_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_c", "Eastern Mail Hauberk with Lamellar Vest", [("kau_rus_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["kau_rus_mail_shirt_a", "Leather Scale Shirt", [("kau_rusmilitia", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(80)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

["kau_rus_mail_shirt_b", "Rus Aketon", [("kau_rus_aketon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

["rus_mail_shirt_c", "Rus Mail Hauberk", [("rus_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

["kau_rus_e", "Eastern Shirt", [("kau_rus_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

["kau_lit_mail", "Baltic Leather Scale Vest", [("balt_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_rus, fac_culture_baltic]],

["kau_rus_tunic_a", "Rus' Tunic", [("kau_rus_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

["kau_rus_tunic_b", "Rus' Tunic", [("kau_rus_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

["kau_rus_tunic_c", "Rus' Tunic", [("kau_rus_tunic_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

["kau_arab_aketon_blue", "Arabic Scale Vest", [("kau_arab_aketon_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_aketon", "Arabic Gambeson", [("kau_arab_aketon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_aketon_red", "Arabic Gambeson", [("kau_arab_aketon_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_aketon_green", "Arabic Gambeson", [("kau_arab_aketon_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_lamellar_vest_a", "Arabic Gambeson", [("kau_ayubbid", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_lamellar_vest_b", "Arabic Gambeson", [("kau_ayubbid_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_lamellar_vest_c", "Arabic Gambeson", [("kau_ayubbid_copy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_mail_a", "Arabic Lamellar Vest", [("arab_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_mail_b", "Arabic Lamellar Vest over Mail Hauberk", [("arab_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_mail_c", "Arabic Lamellar Vest", [("arab_mail_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_mail_d", "Arabic Lamellar Vest over Mail Hauberk", [("arab_mail_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_mail_shirt_a", "Arabic Robe", [("kau_mail_sara", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(80)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_mail_shirt_b", "Arabic Mail Hauberk", [("kau_mail_saracen", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_mail_shirt_c", "Arabic Mail Hauberk", [("kau_mail_saracen_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_mail_shirt_d", "Arabic Gambeson", [("kau_mail_saracen_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_tunic_a", "Bedouin Gambeson", [("kau_muslim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["kau_arab_tunic_b", "Bedouin Gambeson", [("kau_muslim_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_banded_a", "Saracen Mail Hauberk", [("kau_banded_armor_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_banded_b", "Saracen Mail Hauberk", [("kau_banded_armor_muslim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["arab_banded_c", "Saracen Mail Hauberk", [("kau_banded_armor_muslima", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["templar_sarjeant_surcoat", "Templar Surcoat over Mail Haubergeon", [("templar_serjeant_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["templar_sarjeant_mail", "Teutonic Mail Hauberk", [("teu_postulant_acok", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["templar_mail_a", "Templar Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_23]],

["templar_tunic_a", "Templar Surcoat over Mail Haubergeon", [("rnd_surcoat_temple", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["templar_knight_a", "Templar Surcoat over Mail Haubergeon", [("templar_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["templar_knight_b", "Templar Surcoat over Mail Haubergeon", [("templar_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["templar_knight_c", "Templar Surcoat over Mail Haubergeon", [("templar_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["templar_gambeson_a", "Templar Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_23]],

["hospitaller_knight_a", "Hospitaller Surcoat over Mail Haubergeon", [("fi_chain_mail_hauberk_heraldic_3", imodbits_none), ("hospitaller_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23, fac_kingdom_23]],

["hospitaller_knight_b", "Hospitaller Surcoat over Mail", [("hospitaller_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_knight_c", "Hospitaller Surcoat over Mail", [("hospitaller_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_knight_d", "Hospitaller Surcoat over Mail", [("hospitaller_knight_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_knight_e", "Hospitaller Surcoat over Mail", [("hospitaller_knight_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_knight_f", "Hospitaller Surcoat over Mail Haubergeon", [("hospitaller_knight_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_sarjeant_surcoat", "Hospitaller Surcoat over Mail Haubergeon", [("Chinese_Hospitaller", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_sarjeant_mail", "Order Mantle of the Knights Hospitaller", [("templar_serjeant_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_tunic_a", "Order Mantle of the Knights Templar", [("templar_postulant_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

["hospitaller_gambeson_a", "Templar Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_23]],

["hirdman_a", "Scandinavian Mail Haubergeon", [("kau_hirdman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_nordic]],

["cuman_shirt_a", "Cuman Mail Hauberk", [("cuman_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

["cuman_shirt_b", "Cuman Gambeson", [("cuman_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7]],

["cuman_shirt_c", "Cuman Gambeson", [("cuman_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7]],

["cuman_shirt_d", "Cuman Gambeson", [("cuman_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7]],

["kipchak_shirt_a", "Kipchak Mail Hauberk", [("kipchak_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

["kipchak_shirt_b", "Kipchak Tunic", [("kipchak_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_kingdom_7]],

["kipchak_mail_a", "Surcoat over Mail Haubergeon", [("rnd_surcoat_09_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["mongol_warrior_a", "Mongol Tunic with Lamellar", [("mongol_light_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(100)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

["mongol_warrior_b", "Mongol Kaftan with Lamellar", [("mongol_light_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(100)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

["mongol_warrior_c", "Mongol Leather Lamellar", [("mongol_leather_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

["mongol_warrior_d", "Chinese Gambeson", [("mongol_warrior_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a", imodbits_none), ("mongol_warrior_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol, fac_culture_mongol]],

["mongol_tunic_b", "Mongol Gambeson", [("mongol_warrior_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

["mongol_warrior_ilkhanate", "Mongol Gambeson", [("ilkhanate_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

["mamluk_shirt_a", "Mamluk Shirt", [("mamluk_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_anatolian]],

["mamluk_shirt_b", "Mamluk Mail Hauberk", [("mamluk_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

["mamluk_shirt_c", "Mamluk Mail Hauberk", [("mamluk_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

["mamluk_shirt_d", "Mamluk Lamellar Vest", [("mamluk_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

["mamluk_shirt_e", "Seljuk Mail Hauberk", [("mamluk_shirt_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

["mamluk_shirt_f", "Arabic Scale Armour", [("mamluk_shirt_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(60)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

["peasant_tunic_a", "Linen Tunic", [("peasant_outfit_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["peasant_b", "Linen Tunic", [("peasant_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["peasant_c", "Linen Tunic", [("peasant_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["peasant_d", "Linen Tunic", [("peasant_man_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["ragged_cloth_b", "Linen Tunic", [("ragged_cloth_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["peasant_f", "Linen Tunic", [("ragged_cloth_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["peasant_g", "Linen Tunic with Cape", [("peasant_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["byz_lord", "Byzantine Lamellar Armour over Mail Hauberk", [("byz_lord", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_emperor", "Byzantine Lamellar Armour over Mail Hauberk", [("byz_emperor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["bishop_a", "Bishop Surcoat over Mail Haubergeon", [("bishop_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["varangian_a", "Varangian Mail Haubergeon", [("varangian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

["varangian_b", "Byzantine Lamellar Vest", [("varangian_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

["varangian_c", "Varangian Mail Hauberk", [("rus_coat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

["kau_rus_noble_d", "Rus Mail Hauberk with Lamellar Vest", [("kau_rus_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["balt_lamellar_vest_a", "Baltic Gambeson", [("balt_lamellar_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_lamellar_vest_b", "Baltic Gambeson", [("balt_lamellar_vest_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_lamellar_vest_c", "Baltic Lamellar Vest", [("balt_lamellar_vest_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

["byz_mail_a", "Byzantine Lamellar over Mail Hauberk", [("byzantine_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_lamellar_a", "Byzantine Lamellar Leather Armour", [("byz_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_lamellar_b", "Byzantine Lamellar Leather Armour", [("byz_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_leather_a", "Byzantine Gambeson", [("byz_leather_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_leather_b", "Byzantine Gambeson", [("byz_leather_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_padded_leather", "Byzantine Mail Hauberk", [("byz_padded_cloth", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(50)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_scale_armor", "Byzantine Scale Shirt", [("byz_cavalry", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

["byz_cavalry_a", "Byzantine Cavalry Mail Hauberk", [("byz_cavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_cavalry_b", "Byzantine Cavalry Mail Hauberk", [("byz_cavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_mail_b", "Byzantine Mail Hauberk", [("byz_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_hcavalry_a", "Byzantine Scale over Mail Hauberk", [("byz_hcavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_hcavalry_b", "Byzantine Scale over Mail Hauberk", [("byz_hcavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_hcavalry_c", "Byzantine Gambeson", [("byz_hcavalry_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(80)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_psiloi_a", "Byzantine Tunic", [("byz_psiloi_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["byz_psiloi_b", "Byzantine Tunic", [("byz_psiloi_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["byz_kataphrakt", "Byzantine Mail Hauberk", [("byz_kataphrakt", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["kipchak_lamellar_a", "Kipchak Mail Hauberk", [("kipchak_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

["kipchak_lamellar_b", "Kipchak Scale Shirt", [("kipchak_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

["balt_shirt_a", "Baltic Tunic", [("balt_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_shirt_b", "Baltic Tunic", [("balt_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_shirt_e", "Baltic Tunic", [("balt_shirt_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_shirt_d", "Baltic Tunic", [("balt_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_fur_coat_a", "Baltic Tunic", [("balt_fur_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["balt_fur_coat_b", "Baltic Tunic", [("balt_fur_coat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["mon_lamellar_a", "Mongol Lamellar Armor", [("mon_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

["mon_lamellar_b", "Mongol Leather Lamellar Armor", [("mon_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(40)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],

["byz_footman_a", "Byzantine Mail Hauberk", [("byz_footman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_footman_b", "Byzantine Gambeson", [("byz_footman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_footman_c", "Byzantine Mail Hauberk", [("byz_footman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_swordsman_1", "Welsh Mail Hauberk", [("galloglass_padded2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

["byz_swordsman_2", "Byzantine Lamellar Armour over Mail Hauberk", [("rathos_lamellar_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_swordsman_3", "Eastern Lamellar over Mail Hauberk", [("leatherovermail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_swordsman_4", "Eastern Lamellar over Mail Hauberk", [("leatherovermail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_guard_a", "Byzantine Mail Hauberk", [("byz_guard_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["byz_guard_b", "Byzantine Mail Hauberk", [("byz_guard_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["kau_arab_nobleman", "Saracen Mirror Armour over Mail Hauberk", [("kau_arab_nobleman", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

["almogavar_a", "Iberian Tunic", [("almogavar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

["almogavar_b", "Iberian Tunic", [("almogavar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

["almogavar_c", "Iberian Tunic", [("almogavar_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

["burlap_tunic", "Linen Tunic", [("shirt_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

["heraldic_mail_with_surcoat", "Mail Hauberk", [("norman_short_hauberk_yellow", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["sarranid_head_cloth", "Lady Head Cloth", [("tulbent", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

["head_wrappings", "Bastard Battle Axe", [("vik_tveirhendr_vendelox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(88), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["turret_hat_green", "Barbette", [("barbette_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

["wimple_a", "Wimple", [("wimple_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

["wimple_with_veil", "Wimple with Veil", [("wimple_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

["straw_hat", "Green Cap", [("rus_hat_03", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

["headcloth", "Headcloth", [("headcloth_a_new", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

["arming_cap", "Arming Cap", [("1257_arming_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

["fur_hat", "Brown Cap", [("rus_hat_01", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

["nomad_cap", "Hood", [("fi_hood_4", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

["nomad_cap_b", "Red Cap", [("cuman_cap_clothing_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

["steppe_cap", "Hood", [("fi_hood_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

["padded_coif", "Black Cap", [("rus_hat_04", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

["woolen_cap", "Blue Cap", [("cuman_cap_clothing_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

["felt_hat", "Felt Hat", [("birka_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

["felt_hat_b", "Blue Cap", [("rus_hat_05", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth],

["leather_cap", "Woolen Cap", [("rus_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

["female_hood", "Lady's Hood", [("ladys_hood_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

["leather_steppe_cap_a", "Steppe Cap", [("rus_fur_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

["leather_steppe_cap_b", "Gold Topped Cap", [("helmetpad", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

["leather_steppe_cap_c", "Woolen Cap", [("saxon_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(80)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mongol]],

["mail_coif", "Mail Coif", [("coif_1257", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["footman_helmet", "Footman's Helmet", [("skull_cap_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

["khergit_lady_hat", "Blue Robe", [("armenian_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["khergit_lady_hat_b", "Mongol Lady Leather Hat", [("khergit_lady_hat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_mongol]],

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
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
  get_w_price(62, get_mace_weight(62), get_1hmace_speed(62), 9, 0),
  weight(get_mace_weight(62))|difficulty(0)|spd_rtng(get_1hmace_speed(62)) | weapon_length(62)|swing_damage(9 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 18, 0),
  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(18 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
  get_w_price(58, get_mace_weight(58), get_1hmace_speed(58), 13, 0),
  weight(get_mace_weight(58))|difficulty(0)|spd_rtng(get_1hmace_speed(58)) | weapon_length(58)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
[], all_euro_factions  ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 18, 0),
  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(18 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
[], all_euro_factions  ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 22, 0),
  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
[], all_euro_factions  ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
  get_w_price(68, get_mace_weight(73), get_1hmace_speed(73), 24, 0),
  weight(get_mace_weight(73))|difficulty(0)|spd_rtng(get_1hmace_speed(73)) | weapon_length(73)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick,
[], all_euro_factions  ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
  get_w_price(58, get_mace_weight(58), get_1hmace_speed(58), 27, 0),
  weight(get_mace_weight(58))|difficulty(0)|spd_rtng(get_1hmace_speed(58)) | weapon_length(58)|swing_damage(27 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,
[], all_euro_factions  ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
  97 , weight(6)|difficulty(11)|spd_rtng(87) | weapon_length(69)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
  101 , weight(7)|difficulty(12)|spd_rtng(86) | weapon_length(69)|swing_damage(41, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
  290 , weight(9)|difficulty(14)|spd_rtng(83) | weapon_length(68)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 25, 0),
  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick,
[], all_euro_factions  ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
  get_w_price(79, get_mace_weight(79), get_1hmace_speed(79), 16, 0),
  weight(get_mace_weight(79))|difficulty(0)|spd_rtng(get_1hmace_speed(79)) | weapon_length(79)|swing_damage(16 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace,
[], all_euro_factions  ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
  get_w_price(68, get_mace_weight(68), get_1hmace_speed(68), 25, 0),
  weight(get_mace_weight(68))|difficulty(0)|spd_rtng(get_1hmace_speed(68)) | weapon_length(68)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick,
[], all_euro_factions  ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
  get_w_price(64, get_mace_weight(64), get_1hmace_speed(64), 27, 0),
  weight(get_mace_weight(64))|difficulty(0)|spd_rtng(get_1hmace_speed(64)) | weapon_length(64)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick,
[], all_euro_factions  ],
["morningstar",         "Flanged Mace", [("bb_serbian_flanged_mace_1",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_axe_left_hip,
  get_w_price(87, get_mace_weight(87), get_1hmace_speed(87), 31, 0),
  weight(get_mace_weight(87))|difficulty(13)|spd_rtng(get_1hmace_speed(87)) | weapon_length(87)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace,
[], all_euro_factions  ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
  9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(53)|swing_damage(22 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
  14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(29)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
  18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
  23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(61)|swing_damage(25 , cut) | thrust_damage(30 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
  37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_high ],
#["nordic_sword", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
  get_w_price(71, get_w_weight(71), get_1hw_speed(71), 41, 5),
  weight(get_w_weight(71))|difficulty(8)|spd_rtng(get_1hw_speed(71)) | weapon_length(71)|swing_damage(41 , cut) | thrust_damage(5 ,  pierce),imodbits_sword,
[], all_euro_factions  ],
#["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(97, get_w_weight(97), get_1hw_speed(97), 38, 0),
  weight(get_w_weight(97))|difficulty(0)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
 [], eastern_factions],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  get_w_price(100, get_w_weight(100), get_1hw_speed(100), 39, 0),
  weight(get_w_weight(100))|difficulty(0)|spd_rtng(get_1hw_speed(100)) | weapon_length(100)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high,
 [], eastern_factions],

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

["hatchet", "Hatchet",
  [
    ("vik_hoggox", 0)
  ],
  itp_type_one_handed_wpn|itp_secondary|itp_wooden_parry|itp_merchandise|
  itp_primary,itcf_carry_mace_left_hip|itc_scimitar,
  get_w_price(48, get_w_weight(48), get_1hw_speed(48), 20, 0),
  weight(get_axe_weight(48))|abundance(25)|difficulty(9)|spd_rtng(get_1haxe_speed(48))|weapon_length(48)|swing_damage(20, pierce),
  imodbits_pick
],

#["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#  13 , weight(2)|difficulty(0)|spd_rtng(102) | weapon_length(60)|swing_damage(16 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
#77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
#65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
# 129 , weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
#240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
#264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

# talak items["talak_warhammer", "War Pick", [("rrr_hammer2", imodbits_none), ("rrr_hammer2_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 500, hit_points(31744)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(34, pierce)|difficulty(9)|weapon_length(60), imodbit_bent|imodbit_chipped|imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_kingdom_9]],
["talak_warhammer", "War Pick", [("rrr_hammer2", imodbits_none), ("rrr_hammer2_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 500, hit_points(31744)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(34, pierce)|difficulty(9)|weapon_length(60), imodbit_bent|imodbit_chipped|imodbit_fine|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_kingdom_9]],

["talak_bastard_sword", "Hand_and_a_Half_Sword", [("talak_bastard_sword", 0, 0), ("talak_scab_bastard_sword", ixmesh_carry), ("talak_bastard_sword", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_back|itc_nodachi|itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_show_holster_when_drawn|itcf_slashright_onehanded|itcf_thrust_twohanded|itcf_slashleft_onehanded,
  get_w_price(100, get_w_weight(100), get_2hw_speed(100), 42, 21),
  weight(get_w_weight(100))|abundance(2)|difficulty(9)|spd_rtng(get_2hw_speed(100))|weapon_length(100)|thrust_damage(21, pierce)|swing_damage(42, cut), imodbits_sword_high,
  [], all_euro_factions ],
# ["talak_morningstar", "Two-Handed_Morningstar", [("talak_morningstar", 0)], itp_type_two_handed_wpn|itp_wooden_attack|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_spear|itc_nodachi,
  # 401, weight(get_mace_weight(90))|abundance(1)|difficulty(12)|spd_rtng(72)|weapon_length(90)|swing_damage(30, pierce), imodbits_pick ],
# ["talak_mace", "Flanged_Mace", [("talak_mace", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,
 # get_w_price(74, get_mace_weight(74), get_1hmace_speed(74), 27, 0),
 # weight(get_mace_weight(74))|abundance(30)|spd_rtng(get_1hmace_speed(74))|weapon_length(74)|swing_damage(27, blunt), imodbits_pick ],
# ["talak_seax", "Seax", [("talak_seax", 0, 0), ("talak_scab_seax", ixmesh_carry)], itp_merchandise | itp_type_one_handed_wpn|itp_secondary|itp_merchandise|itp_primary, itcf_carry_dagger_front_left|itc_longsword|itcf_show_holster_when_drawn|itcf_horseback_thrust_onehanded, 93, weight(1.00)|spd_rtng(110)|weapon_length(50)|thrust_damage(16, pierce)|swing_damage(16, cut), imodbits_sword_high ],
# ["talak_long_mace", "Two-Handed_Mace", [("talak_long_mace", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_merchandise|itp_primary, itcf_carry_axe_back|itc_nodachi,
  # 520, weight(2.50)|abundance(1)|spd_rtng(58)|weapon_length(96)|swing_damage(28, blunt), imodbits_pick ],

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

["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
  400,
  weight(get_w_weight(99))|difficulty(10)|spd_rtng(get_2hw_speed(99)) | weapon_length(99)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,
  [], all_euro_factions ],

["voulge", "Voulge", [("mackie_voulge", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(40960)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_tutorial_battle_axe2", "European Shortsword", [("sword_euro_1", imodbits_none), ("sword_euro_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(77), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_tutorial_axe2", "European Arming Sword", [("sword_euro_2", imodbits_none), ("sword_euro_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_tutorial_battle_axe1", "Kettle Helm with Padding", [("chapel-de-fer_cloth3", imodbits_none), ("inv_chapel-de-fer_cloth3", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

["modded_tutorial_arrows1", "Kettle Helm with Padding", [("chapel-de-fer_cloth2", imodbits_none), ("inv_chapel-de-fer_cloth2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

["modded_tutorial_bolts1", "Kettle Helm with Padding", [("chapel-de-fer_cloth1", imodbits_none), ("inv_chapel-de-fer_cloth1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(50)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

## more items
## modded2x begin


["modded_tutorial_short_bow1", "Surcoat over Mail Haubergeon", [("rnd_surcoat2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_crossbow1", "Surcoat over Mail Haubergeon", [("rnd_surcoat3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_throwing_daggers1", "Surcoat over Mail Haubergeon", [("rnd_surcoat4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_saddle_horse1", "Surcoat over Mail Haubergeon", [("rnd_surcoat5", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_shield1", "Surcoat over Mail Haubergeon", [("rnd_surcoat6", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_staff_no_attack1", "Surcoat over Mail Haubergeon", [("rnd_surcoat7", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_staff1", "Surcoat over Mail Haubergeon", [("rnd_surcoat8", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_sword1", "Surcoat over Mail Haubergeon", [("rnd_surcoat9", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_axe1", "Surcoat over Mail Haubergeon", [("rnd_surcoat10", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_dagger1", "Surcoat over Mail Haubergeon", [("rnd_surcoat11", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_rnd_surcoat_12_1", "Surcoat over Mail Haubergeon", [("rnd_surcoat12", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_sword", "Wooden Club", [("gaelic_stick", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(59), imodbits_none],

["modded_heavy_practice_sword", "Shillelagh", [("long_stick", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 300, thrust_damage(24, blunt)|hit_points(27648)|spd_rtng(78)|abundance(100)|weight(3.0)|swing_damage(24, blunt)|difficulty(6)|weapon_length(101), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_gaelic, fac_kingdom_13]],
  
["modded_tutorial_sword2", "Long Spiked Mace", [("spikemace3", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_sword_left_hip|itc_cleaver|itc_poleaxe, 750, thrust_damage(35, pierce)|hit_points(81744)|spd_rtng(82)|abundance(25)|weight(4.0)|swing_damage(34, blunt)|difficulty(9)|weapon_length(98), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_tutorial_battle_axe2", "European Shortsword", [("sword_euro_1", imodbits_none), ("sword_euro_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(77), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_tutorial_axe2", "European Arming Sword", [("sword_euro_2", imodbits_none), ("sword_euro_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],
  
["modded_items_end", "Surcoat over Mail Haubergeon", [("rnd_surcoat_20_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["modded_practice_dagger", "Wooden Club", [("maglorg", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(58), imodbits_none],

["modded_lyre1", "Templar Surcoat over Mail Haubergeon", [("Chinese_Hochmeister", imodbits_none), ("Chinese_Templar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_teutonic, fac_culture_western]],

["modded_lute1", "Billhook-fork", [("1429_bill_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_arena_axe", "Cleaving Voulge", [("1429_voulge_6", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_poleaxe, 400, thrust_damage(45, cut)|hit_points(14029)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(152), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_arena_lance", "Fauchard", [("1429_fauchard_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_no_blur, itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(28672)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(186), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_practice_staff", "Broken Spear", [("vik_broken_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 15, thrust_damage(20, cut)|hit_points(33792)|spd_rtng(100)|abundance(100)|weight(1.0)|swing_damage(15, blunt)|weapon_length(108), imodbit_cracked|imodbit_bent],

["modded_practice_lance", "Fauchard-glaive", [("1429_fauchard_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 440, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(171), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["modded_practice_shield", "Wooden Shield", [("lithuanian_shield_old", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 114, hit_points(47)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield],

["modded_cudgel", "Club", [("caribbean_club_2h", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 300, thrust_damage(24, blunt)|hit_points(27648)|spd_rtng(82)|abundance(100)|weight(3.0)|swing_damage(24, blunt)|difficulty(6)|weapon_length(87), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_gaelic, fac_kingdom_13]],

["modded_practice_crossbow", "Fauchard-fork", [("1429_fauchard_fork_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(197), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["modded_practice_javelin", "Fauchard-fork", [("1429_fauchard_fork_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(29696)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(200), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["modded_practice_javelin_melee1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_02_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_throwing_daggers1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_03_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_throwing_daggers_100_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_06_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_horse", "Glaive-fork", [("1429_glaive_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(29696)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["modded_club", "Truncheon", [("caribbean_club", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_unbalanced|itp_no_blur, itc_cleaver|itc_parry_two_handed, 11, hit_points(11264)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(50), imodbits_none],

["modded_practice_bolts1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_13_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_arrows_10_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_14_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_arrows_100_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_17_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_practice_bolts_9_amount1", "Surcoat over Mail Haubergeon", [("rnd_surcoat_19_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["fustibalus", "Fustibalus", [("vc_Staf_Sling_fustibalus_2", imodbits_none)], itp_type_musket|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_knock_down, itcf_shoot_musket|itcf_reload_pistol, 100, thrust_damage(30, blunt)|max_ammo(1)|spd_rtng(85)|abundance(100)|weight(1.25)|leg_armor(85)|shoot_speed(65), imodbits_none],

["modded_arena_sword", "European Sidesword", [("sword_euro_9", imodbits_none), ("sword_euro_9_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1700, thrust_damage(34, pierce)|hit_points(37888)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["modded_arena_sword_two_handed", "Ornate European Longsword", [("sword_euro_10", imodbits_none), ("sword_euro_10_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3500, thrust_damage(36, pierce)|hit_points(37888)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(34, cut)|difficulty(9)|weapon_length(102), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["long_axe_3_alt", "Long War Axe", [("vik_long_hedmarkox", imodbits_none)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_civilian|itp_next_item_as_melee|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itc_parry_polearm, 245, thrust_damage(41, cut)|hit_points(44032)|spd_rtng(73)|abundance(100)|weight(3.625)|swing_damage(41, cut)|difficulty(12)|weapon_length(127), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_spear1", "Kettle Helm with Mail Coif", [("kettlehat1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["modded_tutorial_club1", "Kettle Helm with Padding", [("kettlehat_c_green", imodbits_none), ("inv_kettlehat_c_green", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],



## modded2x end

#["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
# 316 , weight(4.5)|difficulty(10)|spd_rtng(90) | weapon_length(89)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe", "Two Handed Hooked Axe", [("axe_b_2h", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 225, thrust_damage(37, cut)|hit_points(44032)|spd_rtng(77)|abundance(100)|weight(3.125)|swing_damage(37, cut)|difficulty(9)|weapon_length(106), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

["long_axe_alt",         "Long Axe", [("long_danox",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced|itp_merchandise, itc_nodachi|itcf_carry_axe_back,   1300,   weight(get_axe_weight(115))|difficulty(10)|spd_rtng(get_2haxe_speed(115)) | weapon_length(115)|swing_damage(53 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,   [], nordic_factions + balt_factions], 
  
["hammer", "One Handed Long Danish Axe", [("axe_d", imodbits_none), ("axe_d_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 190, hit_points(43008)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(30, cut)|difficulty(6)|weapon_length(71), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

["long_axe_b", "Two Handed Angle Axe", [("axe_c_2h", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 230, thrust_damage(38, cut)|hit_points(44032)|spd_rtng(76)|abundance(100)|weight(3.25)|swing_damage(38, cut)|difficulty(9)|weapon_length(113), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_baltic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

["long_axe_b_alt",         "Long War Axe", [("long_hedmarkox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced|itp_merchandise, itc_nodachi|itcf_carry_axe_back,   1100,   weight(get_axe_weight(122))|difficulty(10)|spd_rtng(get_2haxe_speed(122)) | weapon_length(122)|swing_damage(57 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,   [], nordic_factions + balt_factions],  #["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_merchandise, itc_staff|itcf_carry_axe_back,  # 660 , weight(4.5)|difficulty(10)|spd_rtng(82) | weapon_length(130)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ], #["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,  # 660 , weight(4.5)|difficulty(10)|spd_rtng(82) | weapon_length(130)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ], 

["bardiche", "Bardiche", [("euro_axe_02", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 1000, thrust_damage(45, cut)|hit_points(28697)|spd_rtng(74)|abundance(50)|weight(5.87)|swing_damage(45, cut)|difficulty(12)|weapon_length(95), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_teutonic, fac_culture_rus, fac_culture_baltic]],

["hafted_blade_b", "European Shortsword", [("sword_euro_7", imodbits_none), ("sword_euro_7_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(76), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["hafted_blade_a", "European Arming Sword", [("sword_euro_8", imodbits_none), ("sword_euro_8_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1450, thrust_damage(32, pierce)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(87), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["shortened_military_scythe", "European Longsword", [("the_gaddhjalt", imodbits_none), ("the_gaddhjalt_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3250, thrust_damage(35, pierce)|hit_points(43008)|spd_rtng(90)|abundance(25)|weight(2.75)|swing_damage(33, cut)|difficulty(9)|weapon_length(104), imodbit_fine|imodbits_sword_high, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sword_viking_1", "Baltic Old Sword", [("sword_rus_1", imodbits_none), ("sword_rus_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 875, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(6)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

["sword_viking_2", "Baltic Old Sword", [("sword_rus_2", imodbits_none), ("sword_rus_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 875, thrust_damage(22, pierce)|hit_points(34816)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(6)|weapon_length(86), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

["sword_viking_2_small", "Baltic Old Shortsword", [("viking_short_sword", imodbits_none), ("viking_short_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 750, thrust_damage(22, pierce)|hit_points(36864)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(75), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_rus, fac_culture_baltic]],

["sword_viking_3", "Scandinavian Arming Sword", [("sword_euro_3", imodbits_none), ("sword_euro_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sword_viking_3_small", "Scandinavian Arming Sword", [("sword_euro_4", imodbits_none), ("sword_euro_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(32, pierce)|hit_points(25600)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(94), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["sword_khergit_1", "Eastern Sword", [("sword_mongol_1", imodbits_none), ("sword_mongol_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.25)|swing_damage(26, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["sword_khergit_2", "Eastern Sabre", [("sword_mongol_2", imodbits_none), ("sword_mongol_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(22, cut)|hit_points(40960)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["sword_khergit_3", "Mongol Sabre", [("sword_mongol_3", imodbits_none), ("sword_mongol_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(24, cut)|hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.25)|swing_damage(30, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["sword_khergit_4", "Mongol Sword", [("sword_mongol_4", imodbits_none), ("sword_mongol_4_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(26, pierce)|hit_points(41984)|spd_rtng(100)|abundance(40)|weight(2.25)|swing_damage(28, cut)|difficulty(9)|weapon_length(96), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

["mace_1", "Hætmace", [("haeftmace", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_blur, itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 380, thrust_damage(34, pierce)|hit_points(64032)|spd_rtng(91)|abundance(50)|weight(3.4)|swing_damage(34, cut)|difficulty(9)|weapon_length(143), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_welsh, fac_culture_nordic, fac_culture_gaelic, fac_culture_scotish]],

["mace_2", "Knobbed Mace", [("mace_knobbed", imodbits_none), ("mace_knobbed_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 370, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(2.5)|swing_damage(30, blunt)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["mace_3", "Spiral Mace", [("mace_spiral", imodbits_none), ("mace_spiral_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 370, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(2.5)|swing_damage(30, blunt)|difficulty(6)|weapon_length(66), imodbit_cracked|imodbit_chipped|imodbit_heavy|imodbit_strong, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["mace_4", "Iberian Mace", [("Faradon_IberianMace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_mace_left_hip|itc_cleaver|itc_parry_two_handed, 560, hit_points(31744)|spd_rtng(85)|abundance(100)|weight(3.5)|swing_damage(32, blunt)|difficulty(9)|weapon_length(81), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_iberian]],

["club_with_spike_head", "Billhook", [("Rathos_bill_hook", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 440, thrust_damage(23, blunt)|hit_points(14029)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(172), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["long_spiked_club", "Guisarme", [("guisarme_a", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(53248)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(232), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["long_hafted_knobbed_mace", "Bill", [("english_bill", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 560, thrust_damage(43, pierce)|hit_points(35840)|spd_rtng(67)|abundance(100)|weight(6.6)|swing_damage(53, cut)|difficulty(12)|weapon_length(231), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["long_hafted_spiked_mace", "War Spear", [("ped_spjotkesja", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 260, thrust_damage(41, pierce)|hit_points(32768)|spd_rtng(89)|abundance(100)|weight(3.1)|swing_damage(15, blunt)|difficulty(9)|weapon_length(211), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["studded_club", "Studded Club", [("Faradon_StuddedClub", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 1000, thrust_damage(38, blunt)|hit_points(86864)|spd_rtng(76)|abundance(10)|weight(8.0)|swing_damage(38, blunt)|difficulty(9)|weapon_length(102), imodbit_cracked|imodbit_bent|imodbit_heavy|imodbit_strong, [], [fac_culture_teutonic, fac_culture_western]],

["scythe", "Glaive with Rondel", [("glaive1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 380, thrust_damage(34, pierce)|hit_points(40960)|spd_rtng(76)|abundance(100)|weight(4.8)|swing_damage(44, cut)|difficulty(12)|weapon_length(149), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["pitch_fork", "Hooked Voulge", [("1429_lochaber_axe_3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 460, thrust_damage(24, blunt)|hit_points(40960)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(186), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["military_fork", "Couteau de BrÃ¨che", [("war_glaive_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 440, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(73)|abundance(100)|weight(4.8)|swing_damage(47, cut)|difficulty(12)|weapon_length(177), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["battle_fork", "Couteau de BrÃ¨che", [("war_glaive_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 480, thrust_damage(39, pierce)|hit_points(29696)|spd_rtng(71)|abundance(100)|weight(5.8)|swing_damage(49, cut)|difficulty(12)|weapon_length(196), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["glaive", "Glaive", [("hewing_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 420, thrust_damage(36, pierce)|hit_points(40960)|spd_rtng(74)|abundance(100)|weight(5.2)|swing_damage(46, cut)|difficulty(12)|weapon_length(169), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["staff", "Hooked Voulge", [("1429_lochaber_axe_4", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 440, thrust_damage(23, blunt)|hit_points(40960)|spd_rtng(73)|abundance(100)|weight(5.4)|swing_damage(47, cut)|difficulty(12)|weapon_length(192), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["quarter_staff", "Spiked Voulge", [("1429_voulge_3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 460, thrust_damage(38, pierce)|hit_points(44032)|spd_rtng(72)|abundance(100)|weight(5.6)|swing_damage(48, cut)|difficulty(12)|weapon_length(182), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_balkan]],

["iron_staff", "Voulge", [("1429_voulge_5", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(40, pierce)|hit_points(44032)|spd_rtng(70)|abundance(100)|weight(6.0)|swing_damage(50, cut)|difficulty(12)|weapon_length(200), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_balkan]],

["military_scythe", "Bill", [("fi_bill", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_is_pike|itp_no_blur, itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 520, thrust_damage(41, pierce)|hit_points(45056)|spd_rtng(69)|abundance(100)|weight(6.2)|swing_damage(51, cut)|difficulty(12)|weapon_length(215), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["light_lance", "Coloured Lance", [("colored_lance_a", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["lance", "Coloured Lance", [("colored_lance_b", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["heavy_lance", "Coloured Lance", [("colored_lance_c", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["muslim_lance", "Coloured Lance", [("colored_lance_d", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["heraldic_lance",         "Heraldic Lance", [("heraldic_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 200 , abundance(100) | weight(2.75)|difficulty(10)|spd_rtng(82) | weapon_length(260)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner_old", "tableau_heraldic_lance_1", ":agent_no", ":troop_no")])]],

 ["bamboo_spear", "Coloured Lance", [("colored_lance_f", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["berber_spear", "Coloured Lance", [("colored_lance_g", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable|itp_no_blur, itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(1)|spd_rtng(77)|abundance(50)|weight(5.0)|difficulty(9)|weapon_length(230), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_a", "Spear", [("norman_cavalry_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 210, thrust_damage(36, pierce)|hit_points(29696)|spd_rtng(94)|abundance(100)|weight(2.6)|swing_damage(15, blunt)|difficulty(6)|weapon_length(169), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_b", "Spear", [("norman_cavalry_lance", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 250, thrust_damage(40, pierce)|hit_points(23552)|spd_rtng(90)|abundance(100)|weight(3.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(204), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_c", "Spear", [("vik_bryntvari2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 160, thrust_damage(31, pierce)|hit_points(28672)|spd_rtng(99)|abundance(100)|weight(2.1)|swing_damage(15, blunt)|difficulty(6)|weapon_length(118), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_d", "Spear", [("vik_fjadraspjot", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(23552)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(134), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_e", "Spear", [("vik_hoggkesja", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(29696)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(134), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_f", "Spear", [("vik_kastad_krokaspjott", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 220, thrust_damage(37, pierce)|hit_points(29696)|spd_rtng(93)|abundance(100)|weight(2.7)|swing_damage(15, blunt)|difficulty(6)|weapon_length(173), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_g", "Spear", [("vik_kastspjottmidtaggir", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 150, thrust_damage(30, pierce)|hit_points(28672)|spd_rtng(100)|abundance(100)|weight(2.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(109), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_h", "Spear", [("vik_krokaspjott1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 220, thrust_damage(37, pierce)|hit_points(22528)|spd_rtng(93)|abundance(100)|weight(2.7)|swing_damage(15, blunt)|difficulty(6)|weapon_length(173), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_i", "Spear", [("vik_krokaspjott2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(139), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_j", "Spear", [("vik_langr_bryntvari", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 250, thrust_damage(40, pierce)|hit_points(17408)|spd_rtng(90)|abundance(100)|weight(3.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(205), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_k", "Spear", [("vik_langr_hoggspjott", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 240, thrust_damage(39, pierce)|hit_points(18432)|spd_rtng(91)|abundance(100)|weight(2.9)|swing_damage(15, blunt)|difficulty(6)|weapon_length(198), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_l", "Spear", [("vik_langr_svia", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 250, thrust_damage(40, pierce)|hit_points(16384)|spd_rtng(90)|abundance(100)|weight(3.0)|swing_damage(15, blunt)|difficulty(6)|weapon_length(208), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_m", "Spear", [("vik_spjot", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(24576)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(132), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_n", "Spear", [("vik_spjotkesja", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 270, thrust_damage(42, pierce)|hit_points(16384)|spd_rtng(88)|abundance(100)|weight(3.2)|swing_damage(15, blunt)|difficulty(6)|weapon_length(229), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_o", "Spear", [("vik_svia2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 180, thrust_damage(33, pierce)|hit_points(23552)|spd_rtng(97)|abundance(100)|weight(2.3)|swing_damage(15, blunt)|difficulty(6)|weapon_length(132), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["spear_p", "Spear", [("vik_sviar", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 170, thrust_damage(32, pierce)|hit_points(27648)|spd_rtng(98)|abundance(100)|weight(2.2)|swing_damage(15, blunt)|difficulty(6)|weapon_length(122), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

["wooden_shield", "Lithuanian Shield", [("lithuanian_shield10", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

["nordic_shield", "Lithuanian Shield", [("lithuanian_shield11", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

["leather_covered_round_shield", "Assegai", [("assegai", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 140, thrust_damage(43, cut)|hit_points(16384)|spd_rtng(87)|abundance(100)|weight(3.3)|swing_damage(15, blunt)|difficulty(9)|weapon_length(231), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered, [], [fac_culture_mamluke]],

["hide_covered_round_shield", "Lithuanian Shield", [("lithuanian_shield12", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, [], [fac_kingdom_2]],

["tab_shield_small_round_n", "Hungarian Surcoat over Mail Haubergeon", [("surcoat_hungary_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

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

["jarid", "Darts", [("vik_dart", imodbits_none), ("vik_dart_carry", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 200, thrust_damage(30, cut)|max_ammo(10)|spd_rtng(95)|abundance(50)|weight(3.2)|difficulty(1)|weapon_length(43)|shoot_speed(36), imodbit_cracked|imodbit_tempered|imodbits_missile, 
  missile_distance_trigger
  ],

["darts", "Sling Stones", [("vc_throwing_stone", imodbits_none), ("vc_throwing_stone", ixmesh_flying_ammo)], itp_type_bullets|itp_merchandise|itp_can_knock_down, 0, 10, thrust_damage(12, blunt)|max_ammo(60)|abundance(100)|weight(5.0)|weapon_length(4), imodbit_large_bag],

["war_darts", "Javelins", [("vik_heavy_dart", imodbits_none), ("vik_heavy_dart_carry", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 300, thrust_damage(30, pierce)|max_ammo(8)|spd_rtng(93)|abundance(50)|weight(3.6)|difficulty(2)|weapon_length(35)|shoot_speed(32), imodbit_cracked|imodbit_tempered|imodbits_missile, 
  missile_distance_trigger
  ],

["javelin", "Sling", [("vc_Sling2", imodbits_none)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_use_on_horseback, itcf_shoot_pistol|itcf_reload_pistol, 25, thrust_damage(24, blunt)|max_ammo(1)|spd_rtng(85)|abundance(100)|weight(0.25)|leg_armor(75)|shoot_speed(55), imodbits_none],

["balt_javelin", "Throwing Spears", [("vik_atgeirr_thrown", imodbits_none), ("atgeirr_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 480, thrust_damage(33, pierce)|max_ammo(6)|spd_rtng(91)|abundance(20)|weight(3.2)|difficulty(3)|weapon_length(45)|shoot_speed(28), imodbit_cracked|imodbit_tempered|imodbits_missile, 
  missile_distance_trigger
  ],

["throwing_spears", "Falarica", [("vik_bryntvari2_thrown", imodbits_none), ("vik_bryntvari_a_quiver", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_wooden_parry|itp_primary|itp_has_bayonet, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 600, thrust_damage(36, pierce)|max_ammo(4)|spd_rtng(89)|abundance(20)|weight(4.0)|difficulty(4)|weapon_length(50)|shoot_speed(26), imodbit_cracked|imodbit_tempered|imodbits_missile],

["fustibalus", "Fustibalus", [("vc_Staf_Sling_fustibalus_2", imodbits_none)], itp_type_musket|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_knock_down, itcf_shoot_musket|itcf_reload_pistol, 100, thrust_damage(30, blunt)|max_ammo(1)|spd_rtng(85)|abundance(100)|weight(1.25)|leg_armor(85)|shoot_speed(65), imodbits_none],

["throwing_knives", "Rocks with Sling (Thrown)", [("vc_Sling", imodbits_none), ("caribbean_stone", ixmesh_flying_ammo)], itp_type_thrown|itp_primary|itp_cant_use_on_horseback|itp_can_knock_down, itcf_throw_stone, 25, thrust_damage(18, blunt)|max_ammo(30)|spd_rtng(85)|abundance(100)|weight(3.0)|weapon_length(8)|shoot_speed(45), imodbit_large_bag, 
  missile_distance_trigger
  ],

["stones", "Stones", [("vik_rocks", imodbits_none)], itp_type_thrown|itp_primary|itp_secondary|itp_can_knock_down, itcf_throw_knife, 1, thrust_damage(12, blunt)|max_ammo(12)|spd_rtng(97)|abundance(100)|weight(4.0)|weapon_length(6)|shoot_speed(35), imodbit_heavy|imodbit_large_bag],

["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(11) | thrust_damage(15 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],


["light_throwing_axes", "Francisca", [("vik_francisca", imodbits_none), ("vik_francisca_carry", ixmesh_carry)], itp_type_thrown|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_civilian|itp_next_item_as_melee|itp_unbalanced|itp_extra_penetration, itcf_throw_axe|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 160, thrust_damage(24, cut)|max_ammo(1)|spd_rtng(90)|abundance(10)|weight(1.6)|weapon_length(31)|shoot_speed(12), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, 
  missile_distance_trigger
  , [fac_culture_finnish, fac_culture_mazovian, fac_culture_balkan, fac_culture_rus, fac_culture_nordic, fac_culture_baltic, fac_culture_gaelic]],

["light_throwing_axes_melee", "Francisca", [("vik_francisca", imodbits_none), ("vik_francisca_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 0, spd_rtng(90)|weight(1.6)|swing_damage(24, cut)|difficulty(6)|weapon_length(42), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace],

["hunting_bow", "Hunting Bow", [("bow_f_hunting_bow", imodbits_none), ("bow_f_hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 8, thrust_damage(5, cut)|spd_rtng(95)|abundance(100)|weight(1.5)|accuracy(75)|shoot_speed(55), imodbit_heavy|imodbits_crossbow],

["short_bow", "Hunting Self Bow", [("bow_f_simple", imodbits_none), ("bow_f_simple_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 117, thrust_damage(7, cut)|spd_rtng(70)|abundance(100)|weight(2.0)|accuracy(80)|difficulty(1)|shoot_speed(65), imodbit_heavy|imodbits_crossbow],

["nomad_bow", "Composite Bow", [("bow_f_dothraki", imodbits_none), ("bow_f_dothraki_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 269, thrust_damage(8, cut)|spd_rtng(60)|abundance(100)|weight(2.75)|accuracy(90)|difficulty(3)|shoot_speed(95), imodbit_heavy|imodbits_crossbow, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium, fac_culture_anatolian, fac_culture_mongol]],

["long_bow", "Yew Self Long Bow", [("bow_f_longbow_2", imodbits_none), ("bow_f_longbow_2_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 445, thrust_damage(10, pierce)|spd_rtng(45)|abundance(100)|weight(3.0)|accuracy(90)|difficulty(4)|shoot_speed(85), imodbit_heavy|imodbits_crossbow, [], [fac_kingdom_4, fac_kingdom_6, fac_kingdom_9, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14]],

["khergit_bow", "Reflex Bow", [("bow_f_dornish", imodbits_none), ("bow_f_dornish_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 137, thrust_damage(6, cut)|spd_rtng(65)|abundance(100)|weight(2.25)|accuracy(85)|difficulty(2)|shoot_speed(90), imodbit_heavy|imodbits_crossbow, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_mamluke, fac_culture_byzantium, fac_culture_andalus, fac_culture_anatolian]],

["strong_bow", "Self Bow", [("bow_f_longbow_1", imodbits_none), ("bow_f_longbow_1_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 258, thrust_damage(9, cut)|spd_rtng(60)|abundance(100)|weight(2.5)|accuracy(85)|difficulty(2)|shoot_speed(75), imodbit_heavy|imodbits_crossbow],

["hunting_crossbow", "Hunting Crossbow", [("crossbow_new", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 122, thrust_damage(30, pierce)|max_ammo(1)|spd_rtng(45)|abundance(100)|weight(1.75)|accuracy(75)|shoot_speed(55), imodbit_heavy|imodbits_crossbow],

["light_crossbow", "Cavalry Crossbow", [("crossbow_b", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 267, thrust_damage(35, pierce)|max_ammo(1)|spd_rtng(35)|abundance(100)|weight(2.5)|accuracy(80)|shoot_speed(65), imodbit_heavy|imodbits_crossbow],

["crossbow", "Crossbow", [("crossbow_c", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 382, thrust_damage(40, pierce)|max_ammo(1)|spd_rtng(30)|abundance(100)|weight(3.25)|accuracy(85)|shoot_speed(75), imodbit_heavy|imodbits_crossbow],

["heavy_crossbow", "Composite Crossbow", [("crossbow_a", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 949, thrust_damage(45, pierce)|max_ammo(1)|spd_rtng(25)|abundance(80)|weight(4.25)|accuracy(90)|difficulty(6)|shoot_speed(100), imodbit_heavy|imodbits_crossbow],

["sniper_crossbow", "Arbalest", [("xenoargh_arbalest", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_cant_reload_while_moving, itcf_shoot_crossbow|itcf_carry_crossbow_back|itcf_reload_musket, 1083, thrust_damage(50, pierce)|max_ammo(1)|spd_rtng(20)|abundance(40)|weight(6.0)|accuracy(95)|difficulty(9)|shoot_speed(110), imodbit_heavy|imodbits_crossbow],


["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],



  ["khergit_war_helmet", "Mongol Helmet", [("mongolian_helmet", imodbits_none), ("mongolian_helmet_inv", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["khergit_guard_helmet", "Mongol Lamellar Helmet", [("lamellar_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["khergit_cavalry_helmet", "Mongol Helmet", [("lamellar_helmet_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["khergit_guard_boots", "Scandinavian Shortsword", [("norman_short_sword_2", imodbits_none), ("norman_short_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(38912)|spd_rtng(100)|abundance(100)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(82), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["tunic_with_green_cape", "Tunic with Green Cape", [("archer_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

  ["keys", "Bastard Bearded Axe", [("vik_tveirhendr_haloygox", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(88), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

  ["bride_dress", "Bride Dress", [("bride_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth],

  ["bride_crown", "Crown of Flowers", [("bride_crown", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1, abundance(100)|weight(0.5)|head_armor(4), imodbits_cloth],

  ["bride_shoes", "Bride Shoes", [("bride_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 30, abundance(100)|weight(1.0)|leg_armor(8), imodbits_cloth],

  ["practice_bow_2", "One Handed GallÃ³glaigh Axe", [("talak_jomsviking_axe", imodbits_none), ("talak_jomsviking_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_carry_dagger_front_right|itcf_show_holster_when_drawn|itc_cleaver|itc_parry_two_handed, 175, hit_points(43008)|spd_rtng(87)|abundance(100)|weight(1.87)|swing_damage(27, cut)|difficulty(6)|weapon_length(58), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["practice_arrows_2", "Bastard Gaelic Axe", [("gaelic_long_axe", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(85), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

# modded2x
# WARNING: this can cause crash!!
["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],

  
["almogavar_sword", "Iberian Sword", [("varangiansword", imodbits_none), ("varangiansword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(22, cut)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.75)|swing_damage(32, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_iberian, fac_culture_andalus]],

["welsh_archer", "Welsh Bowman Tunic", [("welsh_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_9]],

["armenian_knight_a", "Green Robe", [("armenian_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["armenian_knight_b", "Red Robe", [("armenian_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

["armenian_knight_c", "Bastard Small Axe", [("vik_tveirhendr_hedmarkrox_small", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_cleaver|itc_parry_polearm, 205, thrust_damage(33, cut)|hit_points(64032)|spd_rtng(81)|abundance(100)|weight(2.625)|swing_damage(33, cut)|difficulty(9)|weapon_length(89), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_welsh, fac_culture_teutonic, fac_culture_rus, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_gaelic, fac_culture_anatolian_christian, fac_culture_scotish, fac_culture_western]],

["archer_a", "Nobleman Outfit", [("noble_cloak", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["archer_b", "Tunic", [("archer_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["archer_c", "Shirt", [("archer_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["surcoat_a", "Gambeson", [("surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["surcoat_b", "Gambeson", [("surcoat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["surcoat_c", "Gambeson", [("surcoat_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["surcoat_d", "Gambeson", [("surcoat_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["surcoat_e", "Gambeson", [("surcoat_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["surcoat_f", "Gambeson", [("surcoat_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["surcoat_g", "Mail Hauberk", [("surcoat_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

["teu_hbrother_a", "Halbbrüder Surcoat over Mail Haubergeon", [("teu_hbrother_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

  ["teu_hbrother_b", "HalbbrÃ¼der Surcoat over Mail Haubergeon", [("teu_hbrother_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1, fac_kingdom_23]],

  ["flat_kettle_hat", "Flattop Kettle Helm", [("flat_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["seljuk_horse", "Seljuk Horse", [("seljuk_horse", imodbits_none)], itp_type_horse, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|horse_charge(38)|horse_speed(38)|body_armor(48)|horse_scale(110), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_kingdom_22]],

  ["seljuk_armour", "Seljuk Gambeson", [("seljuk_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_22]],

  ["seljuk_lamellar_a", "Seljuk Lamellar Vest", [("seljuk_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

  ["seljuk_lamellar_b", "Seljuk Lamellar Vest", [("seljuk_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_22]],

  ["andalus_helmet_a", "Andalusian Helm with Full Mail Coif", [("andalus_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["andalus_infantry_helmet", "Andalusian Helm with Full Mail Coif", [("andalus_infantry_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["andalusian_knight", "Andalusian Surcoat over Mail Hauberk", [("andalusian_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["gaelic_mail_shirt_a", "Gaelic Gambeson", [("gaelic_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["targe_1", "Targe", [("s_h1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

["highlander_boots_1", "Highlander Boots", [("highlander_boots_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["gaelic_byrnie_a", "Gaelic Gambeson", [("gaelic_byrnie_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["gaelic_byrnie_b", "Gaelic Gambeson", [("gaelic_byrnie_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["genoa_padded_a", "Italian Gambeson", [("genoa_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["genoa_padded_b", "Italian Gambeson", [("genoa_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["genoa_padded_c", "Italian Gambeson", [("genoa_padded_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],


  ["genoa_mail_b", "Italian Gambeson", [("genoa_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["genoa_mail_c", "Italian Gambeson", [("genoa_mail_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],


["andalusian_shield_1", "Old Moorish Shield", [("andalusian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
  get_shield_price (shield_t1_res, 36, 70), weight(2)|hit_points(28)|body_armor(shield_t1_res)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
  [], andalusian_factions],

  ["andalusian_shield_2", "Finnish Billhook", [("mackie_vesuri", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced|itp_no_blur, itcf_carry_axe_left_hip|itc_cleaver|itc_parry_two_handed, 200, hit_points(36864)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(34, cut)|difficulty(6)|weapon_length(70), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_kingdom_14]],

  ["andalusian_shield_3", "Moorish Shield", [("andalusian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, [], [fac_culture_andalus]],

  ["andalusian_shield_4", "Tough Moorish Shield", [("heavy_adarga", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, hit_points(51)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(36)|resistance(67)|shield_height(70), imodbits_shield, [], [fac_culture_andalus]],


["andalusian_helmet_a", "Andalusian Helmet with Mail Coif", [("andalusian_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["andalusian_helmet_b", "Iberian Helmet with Mail Coif", [("andalusian_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],



["noble_cloak", "Nobleman Outfit", [("noble_cloak",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 
  tier_0_body_armor_price,
  tier_0_body_armor, imodbits_cloth,
  [], all_euro_factions],

["meghrebi_leather_a", "Meghrebi Gambeson", [("meghrebi_leather_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["meghrebi_leather_b", "Meghrebi Gambeson", [("meghrebi_leather_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["meghrebi_leather_c", "Meghrebi Gambeson", [("meghrebi_leather_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  
["meghrebi_vest", "Meghrebi Gambeson", [("meghrebi_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

["buff_leather", "Iberian Gambeson", [("buff_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],


["black_guard", "Arabic Gambeson", [("black_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["black_guard_helmet", "Saracen Fluted Helmet with Full Mail Coif", [("black_guard_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

["gaelic_mail_shirt_b", "Gaelic Gambeson", [("gaelic_mail_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["surcoat_gaelic", "Gaelic Scale Shirt", [("gaelic_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(40)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_13]],

  ["almohad_robe_a", "Almohad Gambeson", [("almohad_robe_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_robe_b", "Almohad Gambeson", [("almohad_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_robe_c", "Almohad Gambeson", [("almohad_robe_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_robe_d", "Almohad Gambeson", [("almohad_robe_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_padded_a", "Almohad Gambeson", [("almohad_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_padded_b", "Almohad Gambeson", [("almohad_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_padded_c", "Almohad Gambeson", [("almohad_padded_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_cavalry_a", "Almohad Gambeson", [("almohad_cavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["almohad_cavalry_b", "Almohad Gambeson", [("almohad_cavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["andalusian_archers_vest", "Andalusian Gambeson", [("andalusianarchers_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["andalusian_skirmisher_armor", "Andalusian Mail Hauberk", [("andalusianskirmisher_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["arabian_lamellar", "Arabic Gambeson", [("arabian_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["horse_d", "Courser", [("horse_d", imodbits_none), ("horse_d", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(120)|horse_maneuver(46)|abundance(60)|difficulty(3)|horse_charge(28)|horse_speed(45)|body_armor(24)|horse_scale(108), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion],

["horse_d","Courser", [("horse_d",0),("horse_d",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(horse_hp)|body_armor(18)|difficulty(3)|horse_speed(45)|horse_maneuver(46)|horse_charge(28)|horse_scale(108),imodbits_horse_basic|imodbit_champion],  

["arab_nobleman_a", "Arabian Mail Hauberk", [("arab_nobleman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(50)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["arab_nobleman_b", "Arabic Gambeson", [("arab_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["arab_nobleman_c", "Arabic Gambeson", [("arab_nobleman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["andalusian_heavy_a", "Andalusian Scale over Mail Hauberk", [("andalusian_heavy_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["andalusian_heavy_b", "Andalusian Scale over Mail Hauberk", [("andalusian_heavy_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

["berber_tunic_a", "Berber Gambeson", [("berber_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["berber_tunic_b", "Berber Leather Scale Vest", [("berber_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["berber_tunic_c", "Berber Gambeson", [("berber_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],

  ["berber_turban", "Moorish Turban", [("berber_turban", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_andalus]],

  ["iberian_leather_armour_a", "Iberian Gambeson", [("iberian_leather_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["iberian_leather_armour_b", "Iberian Gambeson", [("iberian_leather_armour_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["iberian_leather_armour_c", "Iberian Gambeson", [("iberian_leather_armour_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["andalusi_horseman_robe", "Moorish Gambeson", [("andalusi_horseman_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_andalus]],



  ["galloglass_mail", "Gallóglaigh Mail Hauberk", [("galloglass_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["galloglass_padded", "Gallóglach Mail Hauberk", [("galloglass_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(100)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

["baltic_sword", "Baltic Short Falchion", [("dublin3_sword", imodbits_none), ("dublin3_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, cut)|hit_points(34816)|spd_rtng(90)|abundance(40)|weight(2.75)|swing_damage(32, cut)|difficulty(6)|weapon_length(69), imodbit_fine|imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],


["man_at_arms_a", "Gambeson", [("man_at_arms_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(80)|weight(12.0)|leg_armor(12)|body_armor(24), imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_thick|imodbit_hardened, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["man_at_arms_b", "Blue Gambeson over Mail Hauberk", [("man_at_arms_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["man_at_arms_c", "Red Gambeson over Mail Hauberk", [("man_at_arms_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],


["arab_padded_vest", "Saracen Gambeson", [("arab_padded_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["arab_archer", "Saracen Gambeson", [("arab_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],


["mamluk_infantry_lamellar_a", "Mamluk Lamellar over Mail Hauberk", [("mamluk_infantry_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["mamluk_infantry_lamellar_b", "Mamluk Lamellar over Mail Hauberk", [("mamluk_infantry_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],


["targe_2", "Targe", [("s_h1_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["targe_3", "Targe", [("s_h1_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["targe_4", "Targe", [("s_h2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["targe_5", "Targe", [("s_h2_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["targe_6", "Targe", [("s_h2_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

["balt_lamellar_coat_a", "Baltic Leather Lamellar Vest", [("baltic_lamellar_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

  ["balt_lamellar_coat_b", "Baltic Leather Lamellar Vest", [("baltic_lamellar_coat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

["rus_padded", "Eastern Leather Scale", [("rus_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

["baltic_sword_b", "Baltic Falchion", [("berserkr_sword", imodbits_none), ("berserkr_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(28, cut)|hit_points(36864)|spd_rtng(95)|abundance(40)|weight(2.25)|swing_damage(32, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

  ["mongol_helmet_a", "Mongol Lamellar Helmet", [("mongol_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["mongol_helmet_b", "Mongol Helmet", [("mongol_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["mongol_helmet_c", "Mongol Helmet", [("mongol_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["steppe_helmet", "Eastern Cap with Aventail", [("steppe_helmet", imodbits_none), ("inv_steppe_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1920, abundance(100)|weight(1.5)|difficulty(6)|body_armor(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

# modded2x
# WARNING: THIS ITEMS CAN CRASH!

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
  
["surgeon", "Gambeson", [("studden_leather_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth],

  ["bishop_great_helm", "Bishop Great Helm", [("osp_greathelm_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

  ["bishop_armour", "Archbishop Surcoat over Mail Haubergeon", [("bishop", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["bishop_mitre", "Bishop Mittre with Mail Coif", [("bishop_mitre", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 2400, abundance(80)|weight(1.75)|difficulty(6)|head_armor(50), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly],

  ["bishop_staff", "Lance of Longinus", [("fi_cross_spear", imodbits_none)], itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_covers_head|itp_couchable|itp_crush_through|itp_no_blur, itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 100000, thrust_damage(36, pierce)|spd_rtng(94)|weight(3.6)|swing_damage(26, blunt)|difficulty(12)|weapon_length(162), imodbits_none],

  ["varangian_shield_a", "Varangian Shield", [("varangian_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["varangian_shield_b", "Varangian Shield", [("varangian_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["varangian_shield_c", "Varangian Shield", [("varangian_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["byzantine_sabre", "Byzantine Sabre", [("paramerion", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itc_scimitar, 2000, hit_points(36864)|spd_rtng(110)|abundance(40)|weight(2.5)|swing_damage(30, cut)|difficulty(9)|weapon_length(88), imodbit_fine|imodbits_sword_high, [], [fac_culture_byzantium]],

  ["byzantine_sword", "Pike", [("fi_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_pike|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_thrust_polearm|itcf_carry_spear|itcf_overswing_spear|itc_parry_polearm, 500, thrust_damage(50, pierce)|hit_points(10240)|spd_rtng(70)|abundance(30)|weight(5.0)|swing_damage(15, blunt)|difficulty(12)|weapon_length(300), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],

  ["byzantine_sword_1", "Scandinavian Damascus Steel Sword", [("gaelic_fine_sword", imodbits_none), ("gaelic_fine_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 10000, thrust_damage(28, pierce)|hit_points(39936)|spd_rtng(95)|abundance(5)|weight(2.5)|swing_damage(36, cut)|difficulty(9)|weapon_length(90), imodbit_fine|imodbit_balanced|imodbit_tempered|imodbit_masterwork, [], [fac_culture_nordic, fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium]],

  ["byzantine_sword_3", "Balkan Scimitar", [("sabre_rus_2_1", imodbits_none), ("sabre_rus_2_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(99), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["byzantine_sword_4", "Balkan Scimitar", [("sabre_rus_3_1", imodbits_none), ("sabre_rus_3_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(40960)|spd_rtng(105)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["byzantine_sword_5", "Balkan Scimitar", [("sabre_rus_4_1", imodbits_none), ("sabre_rus_4_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(39936)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(99), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["byzantine_sword_7", "Balkan Scimitar", [("sabre_rus_5_1", imodbits_none), ("sabre_rus_5_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(41984)|spd_rtng(105)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["byzantine_sword_extra", "Balkan Scimitar", [("sabre_rus_1_1", imodbits_none), ("sabre_rus_1_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1000, hit_points(39936)|spd_rtng(105)|abundance(40)|weight(2.0)|swing_damage(30, cut)|difficulty(9)|weapon_length(92), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["rus_shield_a_3", "Almond Shield", [("rus_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

  ["rus_shield_b_3", "Almond Shield", [("rus_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

  ["rus_shield_c_3", "Almond Shield", [("rus_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

  ["rus_shield_d_3", "Almond Shield", [("rus_shield_d", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, [], [fac_culture_rus]],

  ["cuman_noble_helmet", "Cuman Enclosed Helmet", [("cuman_noble", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["ghulam_helmet", "Ghulam Helmet with Mail Coif", [("ghulam_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["ilkhanate_mongol_helmet", "Mongol Helmet", [("ilkhanate_mongol_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["polski_helm", "Polish Helmet with Mail Coif", [("polska_helma", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_5]],

  ["mamluke_helm_b", "Mighfar with Aventail", [("mamluke_helm_b", imodbits_none), ("inv_mamluke_helm_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

  ["mongol_helmet_d", "Mongol Helmet", [("mongol_leather_helm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["nikloskoe_helmet_warrior", "Nikloskoe Enclosed Helmet", [("nikloskoe_helmet_warrior", imodbits_none), ("inv_nikloskoe_helmet_warrior", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["kiev_helmet_2_facemail", "Rus Enclosed Helmet", [("kiev_helmet_2_facemail", imodbits_none), ("inv_kiev_helmet_2_facemail", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["kiev_helmet_1_facemail_1", "Rus Enclosed Helmet", [("kiev_helmet_1_facemail_1", imodbits_none), ("inv_kiev_helmet_1_facemail_1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_byzantinenoble_kettle", "Byzantine Kettle Helm with Aventail", [("rus_byzantinenoble_kettle", imodbits_none), ("inv_byzantinenoble_kettle", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

["rus_helmet_a", "Eastern Helmet with Aventail", [("rus_helmet_a", imodbits_none), ("inv_rus_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_infantry_helmet", "Eastern Helmet with Padding", [("rus_infantry_helmet", imodbits_none), ("inv_rus_infantry_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_militia_helmet", "Eastern Helmet with Mail Coif", [("rus_militia_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(1.75)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_noble_helmet", "Yesenovo Enclosed Helmet", [("rus_noble_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

["seljuk_archer_cap", "Seljuk Cap", [("seljuk_archer_cap", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["ilkhanate_cap", "Ilkanate Hat with Padding", [("ilkhanate_cap", imodbits_none), ("inv_ilkhanate_cap", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

  ["cuman_cap_d", "Cuman Hat with Aventail", [("cuman_cap_d", imodbits_none), ("inv_cuman_cap_d", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1920, abundance(100)|weight(1.5)|difficulty(6)|body_armor(6)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7]],

  ["anatolian_horseman_lamellar", "Anatolian Lamellar over Mail Hauberk", [("anatolian_horseman_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["anatolian_leather_lamellar", "Anatolian Lamellar Armour", [("anatolian_leather_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["anatolian_mail", "Anatolian Mail Hauberk", [("anatolian_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["arab_headcloth", "Headcloth", [("arab_headcloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

  ["seljuk_tunic", "Seljuk Mail Hauberk", [("seljuk_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["seljuk_tunic_b", "Seljuk Mail Hauberk", [("seljuk_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["seljuk_tunic_c", "Seljuk Mail Hauberk", [("seljuk_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["rus_noble_mail", "Rus Mail Hauberk", [("rus_noble_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_mask_helmet", "Rus Enclosed Helmet", [("mask_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["mamluk_lamellar", "Mamluk Lamellar Armour", [("mamluk_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

  ["rus_leather_scale", "Rus Lamellar over Mail Hauberk", [("rus_scale_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_leather_scale_b", "Rus Leather Scale over Mail Hauberk", [("rus_scale_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rohatyna", "War Spear", [("ped_fjadraspjot", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_no_blur, itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_carry_spear|itcf_overswing_spear|itcf_overswing_musket|itc_spear, 200, thrust_damage(35, pierce)|hit_points(32768)|spd_rtng(95)|abundance(100)|weight(2.5)|swing_damage(15, blunt)|difficulty(9)|weapon_length(150), imodbit_cracked|imodbit_bent|imodbit_fine|imodbit_tempered],
["flat_topped_helmet_a", "Spangen Helmet with Mail Coif", [("flattop_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["flat_topped_helmet_b", "Spangen Helmet with Mail Coif", [("flattop_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["great_helmet_a", "Great Helm", [("greathelmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["great_helmet_b", "Great Helm", [("greathelmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["great_helmet_c", "Great Helm", [("greathelmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["great_helmet_d", "Cervelliere", [("greathelmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["great_helmet_decorative", "Phrigian Helm with Mail Coif", [("greathelmet_decorative", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["bill", "Billhook", [("billhook", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_spear|itc_poleaxe, 400, thrust_damage(22, blunt)|hit_points(14029)|spd_rtng(75)|abundance(100)|weight(5.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(152), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["almogavar_helmet", "Almoghavar Helmet", [("almogavar_helmet", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

  ["curonian_helmet", "Curonian Helmet with Mail Coif", [("curonian_helmet", imodbits_none)], itp_type_head_armor, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

  ["balt_padded_a", "Baltic Gambeson", [("balt_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_2]],

  ["balt_padded_b", "Baltic Gambeson", [("balt_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_2]],

  ["thomas_padded_armour", "Baltic Gambeson", [("thomas_padded_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_2]],

  ["militia_tunic_a", "Gambeson", [("padded_long_orange", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["militia_tunic_b", "Gambeson", [("padded_long_bge", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["rus_militia_padded_a", "Rus Gambeson", [("rus_militia_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

  ["little_samogitian", "Žemaitukas", [("warmblood", imodbits_none), ("warmblood", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 512, hit_points(120)|horse_maneuver(49)|abundance(60)|difficulty(3)|horse_charge(10)|horse_speed(45)|body_armor(24)|horse_scale(95), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion, [], [fac_culture_mazovian, fac_culture_baltic]],

  ["kettlehat_a", "Kettle Helm with Mail Coif", [("kettlehat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["kettlehat_b", "Kettle Helm with Mail Coif", [("kettlehat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["kettlehat_c", "Kettle Helm with Mail Coif and Rondels", [("kettlehat_cheek", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["andalus_marinid_hasfid_elite_a", "Moorish Mail Hauberk", [("andalus_marinid_hasfid_elite_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

  ["andalus_marinid_hasfid_elite_b", "Moorish Mail Hauberk", [("andalus_marinid_hasfid_elite_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(40)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

  ["berber_kaftan", "Moorish Gambeson", [("berber_kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["berber_mail_a", "Moorish Mail Hauberk", [("berber_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

  ["berber_mail_b", "Moorish Mail Hauberk", [("berber_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_marinid]],

  ["seljuk_hauberk_jawshan", "Seljuk Lamellar Vest", [("seljuk_hauberk_jawshan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["mamluk_jawshan_leather", "Mamluk Gambeson", [("mamluk_jawshan_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["horse_e", "Courser", [("horse_e", imodbits_none), ("horse_e", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(120)|horse_maneuver(46)|abundance(60)|difficulty(3)|horse_charge(28)|horse_speed(45)|body_armor(24)|horse_scale(108), imodbit_lame|imodbit_swaybacked|imodbit_stubborn|imodbit_spirited|imodbit_champion],

## Modded2x:
## WARNING: these items can crash!
["gaelic_shirt_blue", "Gaelic Shirt", [("gaelic_shirt_blue",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],

["gaelic_shirt_green", "Gaelic Shirt", [("gaelic_shirt_green_muted",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],

["gaelic_shirt_red", "Gaelic Shirt", [("gaelic_shirt_red",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
  tier_0_body_armor_price,
  tier_0_body_armor ,imodbits_cloth ],


  ["andalusian_helmet_c", "Andalusian Helmet", [("andalusian_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["andalusian_helmet_d", "Andalusian Helmet with Mail Coif", [("andalusian_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["arab_helmet_d", "Saracen Full Mail Helmet", [("arab_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["mamluk_helm_b", "Tawashi Helmet", [("mamluk_helmet_4", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

  ["iberian_cleaver", "European Shortsword", [("norman_short_sword_p7", imodbits_none), ("norman_short_sword_p7_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1350, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(40)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(78), imodbit_fine|imodbits_sword_high, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["moorish_hat", "Moorish Hat", [("moorish_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

  ["alsacian_sword", "Arabic Damascus Steel Scimitar", [("fi_scimitar_return", imodbits_none), ("fi_scab_scimitar_return", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_blur, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 10000, hit_points(39936)|spd_rtng(100)|abundance(5)|weight(2.5)|swing_damage(38, cut)|difficulty(9)|weapon_length(95), imodbit_fine|imodbit_balanced|imodbit_tempered|imodbit_masterwork, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_byzantium]],

  ["moorish_axe", "Arabic Mace", [("saracen_mace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_unbalanced|itp_can_knock_down|itp_no_blur, itcf_carry_mace_left_hip|itc_cleaver|itc_parry_two_handed, 560, hit_points(31744)|spd_rtng(86)|abundance(100)|weight(3.5)|swing_damage(31, blunt)|difficulty(9)|weapon_length(74), imodbit_cracked|imodbit_chipped|imodbit_tempered|imodbit_masterwork|imodbit_heavy|imodbit_strong, [], [fac_culture_marinid, fac_culture_mamluke, fac_culture_iberian]],

  ["kettle_cloth", "Kettle Helm", [("kettle_cloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],



  ["rus_helmet", "Rus Helmet with Mail Coif", [("rus_helmet", imodbits_none), ("inv_rus_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_helmet_1", "Rus Helmet with Mail Coif", [("rus_helmet1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_helmet_2", "Rus Helmet with Full Mail Coif", [("rus_helmet2", imodbits_none), ("inv_rus_helmet2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_helmet_3", "Rus Enclosed Helmet", [("rus_helmet3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],
["balt_rus_cap", "Balt Cap with Padding", [("balt_rus_hat", imodbits_none), ("inv_balt_rus_hat", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_culture_rus]],

  ["moors_quilted_kaftan_blue", "Moorish Gambeson", [("moors_quilted_kaftan_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["moors_quilted_kaftan_brown", "Moorish Gambeson", [("moors_quilted_kaftan_brown", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_marinid]],

  ["czekan", "Maciejowski Axe", [("euro_axe_01", imodbits_none)], itp_type_two_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_extra_penetration|itp_no_blur, itcf_thrust_twohanded|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_axe_back|itc_parry_polearm, 215, thrust_damage(35, cut)|hit_points(28697)|spd_rtng(79)|abundance(100)|weight(2.875)|swing_damage(35, cut)|difficulty(9)|weapon_length(95), imodbit_cracked|imodbit_bent|imodbit_strong|imodbits_axe|imodbits_mace, [], [fac_culture_teutonic, fac_culture_nordic, fac_culture_western]],

  ["ilkhanate_kaftan", "Mongol Gambeson", [("mongol_ilkhanate_kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mongol]],
["turk_kaftan_beige", "Turkic Gambeson", [("turk_kaftan_beige", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_15, fac_kingdom_22, fac_kingdom_29, fac_kingdom_30]],

  ["turk_kaftan_furtrim", "Turkic Gambeson", [("turk_kaftan_furtrim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_15, fac_kingdom_22, fac_kingdom_29, fac_kingdom_30]],

  ["turk_kaftan_green", "Turkic Lamellar over Mail Hauberk", [("turk_kaftan_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_7, fac_kingdom_15, fac_kingdom_22, fac_kingdom_29, fac_kingdom_30]],

  ["saracen_mail", "Saracen Mail Hauberk", [("kau_arabian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["jineta_sword", "Scandinavian Shortsword", [("norman_short_sword", imodbits_none), ("norman_short_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1250, thrust_damage(24, pierce)|hit_points(38912)|spd_rtng(100)|abundance(100)|weight(2.0)|swing_damage(26, cut)|difficulty(6)|weapon_length(82), imodbit_fine|imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

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

  ["rhodok_great_helmet", "Heaume", [("rhodok_great_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 9300, abundance(30)|weight(4.0)|difficulty(12)|head_armor(100), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["rhodok_four_plated_helmet", "Kettlehelm with Mail Coif", [("kettlehat2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["rhodok_kettle_hat_c", "Kettle Helm with Padding", [("rhodok_kettle_hat_c", imodbits_none), ("inv_rhodok_kettle_hat_c", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["rhodok_nasal_helmet_a", "Norman Helm with Aventail", [("rhodok_nasal_helmet_a", imodbits_none), ("inv_rhodok_nasal_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_finnish, fac_culture_mazovian, fac_culture_teutonic, fac_culture_nordic, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_western]],

  ["saint_thomas_knight", "Order Surcoat of the Knights of Saint Thomas", [("rnd_surcoat_santiago", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

  ["lazarus_serjeant_tunic", "Order Mantle of the Knights of Saint Lazarus", [("lazarus_serjeant_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

  ["calatrava_knight", "Order Surcoat of the Knights of Calatrava", [("rnd_surcoat_calatrava", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

  ["santiago_knight", "Order Mantle of the Knights of Santiago", [("santiago_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_23]],

  ["studden_leather_armour_a", "Mail Hauberk", [("norman_short_hauberk_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["faris_helmet", "Saracen Helm", [("faris_helmet", imodbits_none)], itp_type_head_armor, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["arab_mail_e", "Saracen Lamellar Armour", [("arab_mail_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["georgian_mail", "Armenian Mail Hauberk", [("georgian_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(60)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["seljuk_scale_a", "Saracen Lamellar over Mail Hauberk", [("seljuk_scale_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(20)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["balt_shirt_c", "Baltic Gambeson", [("balt_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

  ["armenian_mail_b", "Armenian Mail Hauberk", [("armenian_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["kau_turcopole_a", "Turcopole Gambeson", [("kau_turcopole_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["kau_turcopole_b", "Turcopole Gambeson", [("kau_turcopole_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["mamluk_cap", "Seljuk Cap", [("mamluk_cap", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],


["1257_hood", "Hood", [("1257_hood",0),("inv_1257_hood",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
  head_armor_hat_price,
  head_armor_hat  ,imodbits_cloth,
  [], all_euro_factions],
["berber_turban_cape", "Berber Turban", [("berber_turban_cape", imodbits_none), ("inv_berber_turban_cape", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus]],

  ["bulgar_warrior_a", "Bulgarian Lamellar Vest", [("bulgar_warrior_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4013, abundance(80)|weight(18.0)|leg_armor(18)|difficulty(6)|body_armor(36), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_rus, fac_culture_byzantium]],

  ["bulgar_warrior_b", "Bulgarian Gambeson", [("bulgar_warrior_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_rus]],

  ["bulgar_helm", "Bulgar Helm with Aventail", [("bulgar_helm", imodbits_none), ("inv_bulgar_helm", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["bulgar_helm_b", "Bulgar Helm with Padding", [("bulgar_helm_b", imodbits_none), ("inv_bulgar_helm_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["berber_robe_a", "Berber Gambeson", [("berber_robe_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["berber_robe_b", "Berber Gambeson", [("berber_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["berber_robe_c", "Berber Gambeson", [("berber_robe_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(100)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_marinid]],

  ["saracen_kaftan_a", "Saracen Gambeson", [("saracen_kaftan_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["saracen_kaftan_b", "Saracen Gambeson", [("saracen_kaftan_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["saracen_kaftan_c", "Saracen Gambeson", [("saracen_kaftan_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["saracen_kaftan_d", "Saracen Gambeson", [("saracen_kaftan_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["rus_hat_with_padding", "Rus Hat with Padding", [("rus_hat_with_padding", imodbits_none), ("inv_rus_hat_with_padding", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 427, abundance(80)|weight(1.0)|body_armor(2)|head_armor(20), imodbits_cloth, [], [fac_culture_rus]],

  ["mongol_fur_hat", "Mongol Tribal Hat", [("mongol_fur_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

  ["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a", imodbits_none), ("mongol_warrior_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol, fac_culture_mongol]],

  ["gaelic_tunic_cape_a", "Gaelic Gambeson", [("gaelic_tunic_cape_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(12.0)|leg_armor(12)|body_armor(24), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["kettle_cloth_cape_b", "Kettle Helm with Padding", [("kettle_cloth_cape_b", imodbits_none), ("inv_kettle_cloth_cape_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["kettle_cloth_cape", "Kettle Helm with Padding", [("kettle_cloth_cape", imodbits_none), ("inv_kettle_cloth_cape", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1760, abundance(100)|weight(1.5)|difficulty(6)|body_armor(2)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["wenceslav_helmet", "Saint Wenceslav Helmet with Aventail", [("wenceslav_helmet", imodbits_none), ("inv_wenceslav_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["baltic_ponted_helmet", "Balt Helmet with Aventail", [("baltic_ponted_helmet", imodbits_none), ("inv_baltic_ponted_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_baltic]],

  ["berber_white_turban", "Turban Helm with Aventail", [("berber_white_turban", imodbits_none), ("inv_berber_white_turban", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_andalus, fac_culture_anatolian]],

  ["surcoat_france_b", "French Plated Surcoat over Golden Mail", [("surcoat_france_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(30)|weight(30.0)|leg_armor(30)|difficulty(12)|body_armor(60), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_10]],

  ["byzantine_crown", "Crown", [("byzantine_crown", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 300, abundance(30)|weight(0.5)|head_armor(4), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["rus_coat", "Rus Coat", [("varangian_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

  ["moor_helmet_a", "Andalusian Helmet with Mail Coif", [("moor_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["moor_helmet_b", "Andalusian Helmet with Mail Coif", [("moor_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["moor_helmet_c", "Andalusian Helmet with Mail Coif", [("moor_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["moor_helmet_d", "Andalusian Helmet with Mail Coif", [("moor_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["berber_helmet_g", "Berber Turban", [("berber_helmet_g", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 267, abundance(100)|weight(1.25)|head_armor(20), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["andalusian_helmet_e", "Andalusian Helmet with Mail Coif", [("andalusian_helmet_e", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4800, abundance(50)|weight(2.5)|difficulty(9)|head_armor(70), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["megreb_spangen", "Plain Helm", [("megreb_spangen", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_andalus]],

  ["mamluke_helm_ventail", "Mamluk Helmet with Mail Coif", [("mamluke_helm_ventail", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|difficulty(9)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mamluke, fac_culture_anatolian]],

  ["mongol_kettle", "Mongol Kettle Helm", [("mongol_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|difficulty(6)|head_armor(40), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["kipchak_steppe_helmet", "Kiphak Helmet with Full Mail Coif", [("kipchak_steppe_helmet", imodbits_none), ("inv_kipchak_steppe_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 6000, abundance(40)|weight(2.75)|difficulty(12)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["mongol_warrior_de", "Mongol Lamellar Armour", [("mongol_warrior_de", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6561, abundance(80)|weight(24.0)|leg_armor(24)|difficulty(9)|body_armor(48), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mongol]],

  ["yaroslav_helmet", "Rus Noble Helmet with Aventail", [("yaroslav_helmet", imodbits_none), ("inv_yaroslav_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["polovtsian_helmet", "Volga Bulgar Veiled Helmet with Aventail", [("polovtsian_helmet", imodbits_none), ("inv_polovtsian_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 6320, abundance(40)|weight(2.75)|difficulty(12)|body_armor(6)|head_armor(80), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_rus]],

  ["byz_helmet_golden", "Byzantine Helmet with Aventail", [("byz_helmet_golden", imodbits_none), ("inv_byz_helmet_golden", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3920, abundance(80)|weight(2.0)|difficulty(9)|body_armor(6)|head_armor(60), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

  ["nordic_fur_cap", "Nordic Hat", [("nordic_fur_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_rus]],

  ["gaelic_crown", "Crown", [("gaelic_crown", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 300, abundance(30)|weight(0.5)|head_armor(4), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

  ["helmet_with_feathers", "Enclosed Helm", [("normanpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["frenchpepperpot2", "Enclosed Helm", [("frenchpepperpot2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["frenchpepperpot3", "Enclosed Helm", [("frenchpepperpot3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["munitionshelm2", "Enclosed Helm", [("munitionshelm2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["pepperpothelm1", "Enclosed Helm", [("pepperpothelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["munitionshelm1", "Enclosed Helm", [("munitionshelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

  ["frenchpepperpot", "Rounded Enclosed Helmet", [("frenchpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|difficulty(12)|head_armor(90), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish, fac_culture_western]],

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
