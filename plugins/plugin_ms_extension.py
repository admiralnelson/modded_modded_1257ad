from compiler import *
register_plugin()


troops = [
	["stack_storage_troop", "{!}disabled", "{!}disabled", tf_hero|tf_inactive, 0, 0, 0, [], 0, 0, 0, 0],
	["timer_storage_troop", "{!}disabled", "{!}disabled", tf_hero|tf_inactive, 0, 0, 0, [], 0, 0, 0, 0],
	["static_data_array",   "{!}disabled", "{!}disabled", tf_hero|tf_inactive, 0, 0, 0, [], 0, 0, 0, 0],
]
stack_storage = trp.stack_storage_troop
timer_storage = trp.timer_storage_troop

_imod_offset_damage      = 0
_imod_offset_armor       = 1
_imod_offset_hp          = 2
_imod_offset_speed       = 3
_imod_offset_difficulty  = 4
_imod_offset_h_charge    = 5
_imod_offset_h_speed     = 6
_imod_offset_h_maneuver  = 7
_imod_offset_value       = 8
_imod_offset_rarity      = 9


scripts = [

	# script_position_aim_at_position by motomataru ( http://forums.taleworlds.com/index.php?topic=324668.0 )
	# Input: from position, to position
	# Output: none
	# Basically, points the first position at the second, so then simple move_y will move back and forth and move_x side to side
	("position_aim_at_position", [
		(store_script_param, ":from_position", 1),
		(store_script_param, ":to_position", 2),
		(assign, ":save_fpm", 1),
		(convert_to_fixed_point, ":save_fpm"),
		(set_fixed_point_multiplier, 100), #to match cm returned by get_distance_between_positions

		#remove current rotation
		(position_get_x, ":from_x", ":from_position"),
		(position_get_y, ":from_y", ":from_position"),
		(position_get_z, ":from_z", ":from_position"),
		(init_position, ":from_position"),
		(position_set_x, ":from_position", ":from_x"),
		(position_set_y, ":from_position", ":from_y"),
		(position_set_z, ":from_position", ":from_z"),

		#horizontal rotation
		(position_get_x, ":change_in_x", ":to_position"),
		(val_sub, ":change_in_x", ":from_x"),
		(position_get_y, ":change_in_y", ":to_position"),
		(val_sub, ":change_in_y", ":from_y"),

		(try_begin),
			(this_or_next|neq, ":change_in_y", 0),
			(neq, ":change_in_x", 0),
			(store_atan2, ":theta", ":change_in_y", ":change_in_x"),
			(assign, ":ninety", 90),
			(convert_to_fixed_point, ":ninety"),
			(val_sub, ":theta", ":ninety"),	#point Y axis at to position
			(position_rotate_z_floating, ":from_position", ":theta"),
		(try_end),

		#vertical rotation
		(get_distance_between_positions, ":distance_between", ":from_position", ":to_position"),
		(try_begin),
			(gt, ":distance_between", 0),
			(position_get_z, ":dist_z_to_sine", ":to_position"),
			(val_sub, ":dist_z_to_sine", ":from_z"),
			(val_div, ":dist_z_to_sine", ":distance_between"),
			(store_asin, ":theta", ":dist_z_to_sine"),
			(position_rotate_x_floating, ":from_position", ":theta"),
		(try_end),

		#(assign, reg0, ":distance_between"),
		(set_fixed_point_multiplier, ":save_fpm"),
	]),

	("plugin_ms_extension_init", [
		(try_begin),
			(troop_slot_eq, trp.static_data_array, 1 * 10 + _imod_offset_damage, 0),
			(troop_set_slot, trp.static_data_array,  1 * 10 + _imod_offset_damage, -5),
			(troop_set_slot, trp.static_data_array,  1 * 10 + _imod_offset_armor, -4),
			(troop_set_slot, trp.static_data_array,  1 * 10 + _imod_offset_hp, -46),
			(troop_set_slot, trp.static_data_array,  2 * 10 + _imod_offset_damage, -3),
			(troop_set_slot, trp.static_data_array,  2 * 10 + _imod_offset_armor, -3),
			(troop_set_slot, trp.static_data_array,  3 * 10 + _imod_offset_damage, -3),
			(troop_set_slot, trp.static_data_array,  3 * 10 + _imod_offset_speed, -3),
			(troop_set_slot, trp.static_data_array,  4 * 10 + _imod_offset_damage, -1),
			(troop_set_slot, trp.static_data_array,  5 * 10 + _imod_offset_armor, -2),
			(troop_set_slot, trp.static_data_array,  5 * 10 + _imod_offset_hp, -26),
			(troop_set_slot, trp.static_data_array,  7 * 10 + _imod_offset_damage, -2),
			(troop_set_slot, trp.static_data_array,  7 * 10 + _imod_offset_armor, -1),
			(troop_set_slot, trp.static_data_array, 10 * 10 + _imod_offset_damage, 1),
			(troop_set_slot, trp.static_data_array, 13 * 10 + _imod_offset_damage, 3),
			(troop_set_slot, trp.static_data_array, 13 * 10 + _imod_offset_speed, 3),
			(troop_set_slot, trp.static_data_array, 14 * 10 + _imod_offset_damage, 4),
			(troop_set_slot, trp.static_data_array, 17 * 10 + _imod_offset_damage, 5),
			(troop_set_slot, trp.static_data_array, 17 * 10 + _imod_offset_speed, 1),
			(troop_set_slot, trp.static_data_array, 17 * 10 + _imod_offset_difficulty, 4),
			(troop_set_slot, trp.static_data_array, 18 * 10 + _imod_offset_damage, 2),
			(troop_set_slot, trp.static_data_array, 18 * 10 + _imod_offset_armor, 3),
			(troop_set_slot, trp.static_data_array, 18 * 10 + _imod_offset_hp, 10),
			(troop_set_slot, trp.static_data_array, 18 * 10 + _imod_offset_speed, -2),
			(troop_set_slot, trp.static_data_array, 18 * 10 + _imod_offset_difficulty, 1),
			(troop_set_slot, trp.static_data_array, 18 * 10 + _imod_offset_h_charge, 4),
			(troop_set_slot, trp.static_data_array, 19 * 10 + _imod_offset_damage, 3),
			(troop_set_slot, trp.static_data_array, 19 * 10 + _imod_offset_speed, -3),
			(troop_set_slot, trp.static_data_array, 19 * 10 + _imod_offset_difficulty, 2),
			(troop_set_slot, trp.static_data_array, 21 * 10 + _imod_offset_armor, -3),
			(troop_set_slot, trp.static_data_array, 22 * 10 + _imod_offset_armor, -2),
			(troop_set_slot, trp.static_data_array, 24 * 10 + _imod_offset_armor, 1),
			(troop_set_slot, trp.static_data_array, 25 * 10 + _imod_offset_armor, 2),
			(troop_set_slot, trp.static_data_array, 25 * 10 + _imod_offset_hp, 47),
			(troop_set_slot, trp.static_data_array, 26 * 10 + _imod_offset_armor, 3),
			(troop_set_slot, trp.static_data_array, 27 * 10 + _imod_offset_armor, 4),
			(troop_set_slot, trp.static_data_array, 27 * 10 + _imod_offset_hp, 83),
			(troop_set_slot, trp.static_data_array, 29 * 10 + _imod_offset_armor, 6),
			(troop_set_slot, trp.static_data_array, 29 * 10 + _imod_offset_hp, 155),
			(troop_set_slot, trp.static_data_array, 30 * 10 + _imod_offset_h_speed, -10),
			(troop_set_slot, trp.static_data_array, 30 * 10 + _imod_offset_h_maneuver, -5),
			(troop_set_slot, trp.static_data_array, 31 * 10 + _imod_offset_h_speed, -4),
			(troop_set_slot, trp.static_data_array, 31 * 10 + _imod_offset_h_maneuver, -2),
			(troop_set_slot, trp.static_data_array, 32 * 10 + _imod_offset_hp, 5),
			(troop_set_slot, trp.static_data_array, 32 * 10 + _imod_offset_difficulty, 1),
			(troop_set_slot, trp.static_data_array, 33 * 10 + _imod_offset_difficulty, -1),
			(troop_set_slot, trp.static_data_array, 35 * 10 + _imod_offset_h_charge, 1),
			(troop_set_slot, trp.static_data_array, 35 * 10 + _imod_offset_h_speed, 2),
			(troop_set_slot, trp.static_data_array, 35 * 10 + _imod_offset_h_maneuver, 1),
			(troop_set_slot, trp.static_data_array, 35 * 10 + _imod_offset_difficulty, 1),
			(troop_set_slot, trp.static_data_array, 36 * 10 + _imod_offset_h_charge, 2),
			(troop_set_slot, trp.static_data_array, 36 * 10 + _imod_offset_h_speed, 4),
			(troop_set_slot, trp.static_data_array, 36 * 10 + _imod_offset_h_maneuver, 2),
			(troop_set_slot, trp.static_data_array, 36 * 10 + _imod_offset_difficulty, 2),
		(try_end),
	]),
]


strings = [

	# Character Attribute abbreviated and full names (defaults, will be overridden with values retrieved from module_ui_strings if it's present)
	("attribute_0", "STR"),
	("attribute_1", "AGI"),
	("attribute_2", "INT"),
	("attribute_3", "CHA"),

	("attribute_0_full", "Strength"),
	("attribute_1_full", "Agility"),
	("attribute_2_full", "Intelligence"),
	("attribute_3_full", "Charisma"),

	# Weapon Proficiency names (same)
	("proficiency_0", "One-Handed Weapons"),
	("proficiency_1", "Two-Handed Weapons"),
	("proficiency_2", "Polearms"),
	("proficiency_3", "Archery"),
	("proficiency_4", "Crossbows"),
	("proficiency_5", "Thrown Weapons"),
	("proficiency_6", "Firearms"),

	# Skill names (placeholders, will be overridden with values retrieved from module_skills)
	("skill_00", "Trade"),
	("skill_01", "Leadership"),
	("skill_02", "Prisoner Management"),
	("skill_03", "Reserved Skill 1"),
	("skill_04", "Reserved Skill 2"),
	("skill_05", "Reserved Skill 3"),
	("skill_06", "Reserved Skill 4"),
	("skill_07", "Persuasion"),
	("skill_08", "Engineer"),
	("skill_09", "First Aid"),
	("skill_10", "Surgery"),
	("skill_11", "Wound Treatment"),
	("skill_12", "Inventory Management"),
	("skill_13", "Spotting"),
	("skill_14", "Path-finding"),
	("skill_15", "Tactics"),
	("skill_16", "Tracking"),
	("skill_17", "Trainer"),
	("skill_18", "Reserved Skill 5"),
	("skill_19", "Reserved Skill 6"),
	("skill_20", "Reserved Skill 7"),
	("skill_21", "Reserved Skill 8"),
	("skill_22", "Looting"),
	("skill_23", "Horse Archery"),
	("skill_24", "Riding"),
	("skill_25", "Athletics"),
	("skill_26", "Shield"),
	("skill_27", "Weapon Master"),
	("skill_28", "Reserved Skill 9"),
	("skill_29", "Reserved Skill 10"),
	("skill_30", "Reserved Skill 11"),
	("skill_31", "Reserved Skill 12"),
	("skill_32", "Reserved Skill 13"),
	("skill_33", "Power Draw"),
	("skill_34", "Power Throw"),
	("skill_35", "Power Strike"),
	("skill_36", "Ironflesh"),
	("skill_37", "Reserved Skill 14"),
	("skill_38", "Reserved Skill 15"),
	("skill_39", "Reserved Skill 16"),
	("skill_40", "Reserved Skill 17"),
	("skill_41", "Reserved Skill 18"),

	# Item modifier names (placeholders, will be overridden by actual values retrieved from module_item_modifiers if present, or compiler's default module_item_modifiers if not)
	("item_modifier_00", "Plain {s99}"),
	("item_modifier_01", "Cracked {s99}"),
	("item_modifier_02", "Rusty {s99}"),
	("item_modifier_03", "Bent {s99}"),
	("item_modifier_04", "Chipped {s99}"),
	("item_modifier_05", "Battered {s99}"),
	("item_modifier_06", "Poor {s99}"),
	("item_modifier_07", "Crude {s99}"),
	("item_modifier_08", "Old {s99}"),
	("item_modifier_09", "Cheap {s99}"),
	("item_modifier_10", "Fine {s99}"),
	("item_modifier_11", "Well Made {s99}"),
	("item_modifier_12", "Sharp {s99}"),
	("item_modifier_13", "Balanced {s99}"),
	("item_modifier_14", "Tempered {s99}"),
	("item_modifier_15", "Deadly {s99}"),
	("item_modifier_16", "Exquisite {s99}"),
	("item_modifier_17", "Masterwork {s99}"),
	("item_modifier_18", "Heavy {s99}"),
	("item_modifier_19", "Strong {s99}"),
	("item_modifier_20", "Powerful {s99}"),
	("item_modifier_21", "Tattered {s99}"),
	("item_modifier_22", "Ragged {s99}"),
	("item_modifier_23", "Rough {s99}"),
	("item_modifier_24", "Sturdy {s99}"),
	("item_modifier_25", "Thick {s99}"),
	("item_modifier_26", "Hardened {s99}"),
	("item_modifier_27", "Reinforced {s99}"),
	("item_modifier_28", "Superb {s99}"),
	("item_modifier_29", "Lordly {s99}"),
	("item_modifier_30", "Lame {s99}"),
	("item_modifier_31", "Swaybacked {s99}"),
	("item_modifier_32", "Stubborn {s99}"),
	("item_modifier_33", "Timid {s99}"),
	("item_modifier_34", "Meek {s99}"),
	("item_modifier_35", "Spirited {s99}"),
	("item_modifier_36", "Champion {s99}"),
	("item_modifier_37", "Fresh {s99}"),
	("item_modifier_38", "Day-old {s99}"),
	("item_modifier_39", "Two Days-old {s99}"),
	("item_modifier_40", "Smelling {s99}"),
	("item_modifier_41", "Rotten {s99}"),
	("item_modifier_42", "Large Bag of {s99}"),

	("damage_type_0", "cut"),
	("damage_type_1", "pierce"),
	("damage_type_2", "blunt"),

	("damage_type_0_adj", "cutting"),
	("damage_type_1_adj", "piercing"),
	("damage_type_2_adj", "blunt"),

]


def preprocess_entities(glob):
	# Retrieve item modifier names
	for index in xrange(len(glob['item_modifiers'])):
		str_id = ('item_modifier_0%d' if index < 10 else 'item_modifier_%d') % index
		imod_real_name = glob['item_modifiers'][index][1]
		str_offset = int(getattr(WRECK.s, str_id)) & 0xFFFFFFFF # Strip opmask
		glob['strings'][str_offset][1] = imod_real_name % '{s99}'
	# Retrieve skill names
	for index in xrange(len(glob['skills'])):
		str_id = ('skill_0%d' if index < 10 else 'skill_%d') % index
		skill_real_name = glob['skills'][index][1]
		str_offset = int(getattr(WRECK.s, str_id)) & 0xFFFFFFFF # Strip opmask
		glob['strings'][str_offset][1] = skill_real_name
	# If module_ui_strings is active, retrieve attribute and weapon proficiency names
	if WRECK.generate_ui_strings:
		data = {
			'str': 'attribute_0',
			'agi': 'attribute_1',
			'int': 'attribute_2',
			'cha': 'attribute_3',
			'strength': 'attribute_0_full',
			'agility': 'attribute_1_full',
			'intelligence': 'attribute_2_full',
			'charisma': 'attribute_3_full',
			'one_handed_weapons': 'proficiency_0',
			'two_handed_weapons': 'proficiency_1',
			'polearms': 'proficiency_2',
			'archery': 'proficiency_3',
			'crossbows': 'proficiency_4',
			'throwing': 'proficiency_5',
			'firearms': 'proficiency_6',
		}
		for ui_str in glob['ui_strings']:
			try:
				str_id = data[ui_str[0]]
				ui_text = ui_str[1]
				str_offset = int(getattr(WRECK.s, str_id)) & 0xFFFFFFFF # Strip opmask
				glob['strings'][str_offset][1] = ui_text
			except:
				pass



# New string operations.

def str_store_attribute_name(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.attribute_0, value),
		(str_store_string, string_reg, l._cached_),
	]
def str_store_attribute_name_full(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.attribute_0_full, value),
		(str_store_string, string_reg, l._cached_),
	]
def str_store_proficiency_name(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.proficiency_0, value),
		(str_store_string, string_reg, l._cached_),
	]
def str_store_skill_name(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.skill_00, value),
		(str_store_string, string_reg, l._cached_),
	]
def str_store_item_modifier_name(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.item_modifier_00, value),
		(str_store_string, string_reg, l._cached_),
	]
def str_store_damage_type_name(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.damage_type_0, value),
		(str_store_string, string_reg, l._cached_),
	]
def str_store_damage_type_adjective(string_reg, value, *argl):
	return [
		(store_add, l._cached_, s.damage_type_0_adj, value),
		(str_store_string, string_reg, l._cached_),
	]

# Global stack operations

def push_value(value, *argl):
	return [
		(troop_get_slot, l._cached_, stack_storage, 0),
		(val_add, l._cached_, 1),
		(troop_set_slot, stack_storage, 0, l._cached_),
		(troop_set_slot, stack_storage, l._cached_, value),
	]
def pop_value(destination, *argl):
	return [
		(troop_get_slot, l._cached_, stack_storage, 0),
		(troop_get_slot, l.destination, stack_storage, l._cached_),
		(val_sub, l._cached_, 1),
		(troop_set_slot, stack_storage, 0, l._cached_),
	]
def peek_value(destination, *argl):
	return [
		(troop_get_slot, l._cached_, stack_storage, 0),
		(troop_get_slot, l.destination, stack_storage, l._cached_),
	]
def is_stack_empty(*argl):
	return [
		(troop_slot_eq, stack_storage, 0, 0),
	]

# Unlimited mission timers

def start_mission_timer(timer_index, *argl):
	return [
		(store_mission_timer_c_msec, l._cached_),
		(troop_set_slot, timers_storage, timer_index, l._cached_),
	]
def store_mission_timer(destination, timer_index, *argl):
	return [
		(store_mission_timer_c_msec, destination),
		(troop_get_slot, l._cached_, timers_storage, timer_index),
		(val_sub, destination, l._cached_),
	]

# Generic operations

def store_script_params(*argl):
	return [(store_script_param, argl[index], index + 1) for index in xrange(len(argl))]

# Mathematical operations

def get_fixed_point_multiplier(destination, *argl):
	return [
		(assign, destination, 1),
		(convert_to_fixed_point, destination),
	]

# Position operations

def position_set_coordinates(position, x, y, z, *argl):
	return [
		(position_set_x, position, x),
		(position_set_y, position, y),
		(position_set_z, position, z),
	]

def position_aim_at_position(position, target, *argl):
	return [
		(call_script, script.position_aim_at_position, position, target),
	]

# Troop operations

def troop_set_attribute(troop, attribute, value, *argl):
	return [
		(store_attribute_level, l._cached_, troop, attribute),
		(store_sub, l._cached_, value, l._cached_),
		(troop_raise_attribute, troop, attribute, l._cached_),
	]

def troop_set_skill(troop, skill, value, *argl):
	return [
		(store_skill_level, l._cached_, skill, troop),
		(store_sub, l._cached_, value, l._cached_),
		(troop_raise_skill, troop, skill, l._cached_),
	]

# Item operations

def item_get_real_difficulty(destination, item, modifier = None, *argl):
	if modifier is None: return [(item_get_difficulty, destination, item),]
	return [
		(item_get_difficulty, destination, item),
		(try_begin),
			(lt, destination, 1),
		(else_try),
			(is_between, modifier, 17, 20), # We're using numeric references here because imod_* modifiers may be renamed.
			(item_get_type, l._cached_, item),
			(eq, l._cached_, itp_type_horse),
		(else_try),
			(this_or_next|eq, modifier, 18), # imod_heavy
			(this_or_next|eq, modifier, 32), # imod_stubborn
			(eq, modifier, imod.restless),
			(val_add, destination, 1),
		(else_try),
			(this_or_next|eq, modifier, 19), # imod_powerful
			(eq, modifier, 36), # imod_champion
			(val_add, destination, 2),
		(else_try),
			(eq, modifier, 17), # imod_masterwork
			(val_add, destination, 4),
		(else_try),
			(eq, modifier, 33), # imod_timid
			(val_sub, destination, 1),
		(try_end),
	]

# Item modifier operations

def item_modifier_get_damage(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_damage),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_armor(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_armor),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_hp(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_hp),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_weapon_speed(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_speed),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_difficulty(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_difficulty),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_horse_charge(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_h_charge),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_horse_speed(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_h_speed),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_horse_maneuver(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_h_maneuver),
		(troop_get_slot, destination, trp.static_data_array, destination),
	]
def item_modifier_get_value_multiplier(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_value),
		(troop_get_slot, destination, trp.static_data_array, destination), # value multiplied by 1000000
	    (assign, l._cached_, 1),
	    (convert_to_fixed_point, l._cached_),
	    (val_mul, destination, l._cached_),
	    (val_div, destination, 1000000), # convert to current fixed point
	]
def item_modifier_get_rarity_multiplier(destination, modifier, *argl):
	return [
		(call_script, script.plugin_ms_extension_init),
		(store_mul, destination, modifier, 10),
		(val_add, destination, _imod_offset_rarity),
		(troop_get_slot, destination, trp.static_data_array, destination), # value multiplied by 1000000
	    (assign, l._cached_, 1),
	    (convert_to_fixed_point, l._cached_),
	    (val_mul, destination, l._cached_),
	    (val_div, destination, 1000000), # convert to current fixed point
	]


extend_syntax(str_store_attribute_name)        # (str_store_attribute_name, <string_reg_no>, <attribute_id>),
                                               # Stores specified attribute name (3 capitalized letters by default) to string register, as specified in module_ui_strings.
extend_syntax(str_store_attribute_name_full)   # (str_store_attribute_name_full, <string_reg_no>, <attribute_id>),
                                               # Stores specified attribute full name to string register, as specified in module_ui_strings.
extend_syntax(str_store_proficiency_name)      # (str_store_proficiency_name, <string_reg_no>, <proficiency_id>),
                                               # Stores specified proficiency name to string register.
extend_syntax(str_store_skill_name)            # (str_store_skill_name, <string_reg_no>, <skill_id>),
                                               # Stores specified skill name (as specified in module_skills) to string register
extend_syntax(str_store_item_modifier_name)    # (str_store_item_modifier_name, <string_reg_no>, <imod_value>),
                                               # Stores specified item modifier name (as specified in module_item_modifiers) to string register.
extend_syntax(str_store_damage_type_name)      # (str_store_damage_type_name, <string_reg_no>, <damage_type>),
                                               # Stores specified damage type name to string register.
extend_syntax(str_store_damage_type_adjective) # (str_store_damage_type_adjective, <string_reg_no>, <damage_type>),
                                               # Stores specified damage type adjective to string register.

extend_syntax(push_value)                 # (push_value, <value>),
                                          # Saves a single value to stack.
extend_syntax(pop_value)                  # (pop_value, <destination>),
                                          # Retrieves a single value from top of stack.
extend_syntax(peek_value)                 # (peek_value, <destination>),
                                          # Retrieves a single value from top of stack but keeps it in stack.
extend_syntax(is_stack_empty)             # (is_stack_empty),
                                          # Checks that the stack is empty.
extend_syntax(start_mission_timer)        # (start_mission_timer, <timer_index>),
                                          # Starts a new mission timer with specified index.
extend_syntax(store_mission_timer)        # (store_mission_timer, <destination>, <timer_index>),
                                          # Stores current value (in milliseconds) for specified mission timer.
extend_syntax(store_script_params)        # (store_script_params, <param1>, <param2>...),
                                          # Retrieves arbitrary number of script parameters with a single line.
extend_syntax(get_fixed_point_multiplier) # (get_fixed_point_multiplier, <destination>),
                                          # Retrieves current fixed point multiplier value.
extend_syntax(position_set_coordinates)   # (position_set_coordinates, <pos>, <x_fixed_point>, <y_fixed_point>, <z_fixed_point>),
                                          # Sets all 3 position coordinates with a single line.
extend_syntax(position_aim_at_position)   # (position_point_towards, <position_reg>, <aim_position_reg>),
                                          # Rotates the position so it's Y axis points at specified aim position.
extend_syntax(troop_set_attribute)        # (troop_set_attribute, <troop_id>, <attribute_id>, <value>),
                                          # Sets troop attribute to specified value.
extend_syntax(troop_set_skill)            # (troop_set_skill, <troop_id>, <skill_id>, <value>),
                                          # Sets troop skill to specified value.
extend_syntax(item_get_real_difficulty)   # (item_get_real_difficulty, <destination>, <item_id>, [<imod_value>]),
                                          # Retrieves item difficulty value, taking modifier into account. If modifier is omitted, standard item difficulty is returned.

extend_syntax(item_modifier_get_damage)            # (item_modifier_get_damage, <destination>, <imod_value>),
extend_syntax(item_modifier_get_armor)             # (item_modifier_get_armor, <destination>, <imod_value>),
extend_syntax(item_modifier_get_hp)                # (item_modifier_get_hp, <destination>, <imod_value>),
extend_syntax(item_modifier_get_weapon_speed)      # (item_modifier_get_weapon_speed, <destination>, <imod_value>),
extend_syntax(item_modifier_get_difficulty)        # (item_modifier_get_difficulty, <destination>, <imod_value>),
extend_syntax(item_modifier_get_horse_charge)      # (item_modifier_get_horse_charge, <destination>, <imod_value>),
extend_syntax(item_modifier_get_horse_speed)       # (item_modifier_get_horse_speed, <destination>, <imod_value>),
extend_syntax(item_modifier_get_horse_maneuver)    # (item_modifier_get_horse_maneuver, <destination>, <imod_value>),
extend_syntax(item_modifier_get_rarity_multiplier) # (item_modifier_get_rarity_multiplier, <destination_fixed_point>, <imod_value>),
extend_syntax(item_modifier_get_value_multiplier)  # (item_modifier_get_value_multiplier, <destination_fixed_point>, <imod_value>),
