from header import *


	## script_economy_get_buildings
	# WARNING: this is totally new procedure (not present in native). 1257AD devs
		## Input: none
		## Output: s1..s27
economy_get_buildings =	(
	"economy_get_buildings",
	[
		(party_get_slot, ":acres_pasture", "$g_encountered_party", slot_center_acres_pasture),
		
		(party_get_slot, ":head_cattle", "$g_encountered_party", slot_center_head_cattle),
		(party_get_slot, ":head_sheep", "$g_encountered_party", slot_center_head_sheep),
		(party_get_slot, ":head_horses", "$g_encountered_party", slot_center_head_horses),
		(party_get_slot, ":acres_grain", "$g_encountered_party", slot_center_acres_grain),
		(party_get_slot, ":acres_olives", "$g_encountered_party", slot_center_acres_olives),
		(party_get_slot, ":acres_vineyard", "$g_encountered_party", slot_center_acres_vineyard),
		(party_get_slot, ":acres_flax", "$g_encountered_party", slot_center_acres_flax),
		(party_get_slot, ":acres_dates", "$g_encountered_party", slot_center_acres_dates),
		(party_get_slot, ":fishing_fleet", "$g_encountered_party", slot_center_fishing_fleet),
		(party_get_slot, ":salt_pans", "$g_encountered_party", slot_center_salt_pans),
		(party_get_slot, ":apiaries", "$g_encountered_party", slot_center_apiaries),
		(party_get_slot, ":silk_farms", "$g_encountered_party", slot_center_silk_farms),
		(party_get_slot, ":kirmiz_farms", "$g_encountered_party", slot_center_kirmiz_farms),
		(party_get_slot, ":iron_deposits", "$g_encountered_party", slot_center_iron_deposits),
		(party_get_slot, ":fur_traps", "$g_encountered_party", slot_center_fur_traps),
		(party_get_slot, ":household_gardens", "$g_encountered_party", slot_center_household_gardens),
		
		(party_get_slot, ":mills", "$g_encountered_party", slot_center_mills),
		(party_get_slot, ":breweries", "$g_encountered_party", slot_center_breweries),
		(party_get_slot, ":wine_presses", "$g_encountered_party", slot_center_wine_presses),
		(party_get_slot, ":olive_presses", "$g_encountered_party", slot_center_olive_presses),
		(party_get_slot, ":linen_looms", "$g_encountered_party", slot_center_linen_looms),
		(party_get_slot, ":silk_looms", "$g_encountered_party", slot_center_silk_looms),
		(party_get_slot, ":wool_looms", "$g_encountered_party", slot_center_wool_looms),
		(party_get_slot, ":pottery_kilns", "$g_encountered_party", slot_center_pottery_kilns),
		(party_get_slot, ":smithies", "$g_encountered_party", slot_center_smithies),
		(party_get_slot, ":tanneries", "$g_encountered_party", slot_center_tanneries),
		(party_get_slot, ":shipyards", "$g_encountered_party", slot_center_shipyards),
		
		(assign, reg1, ":head_cattle"),
		(assign, reg2, ":head_sheep"),
		(assign, reg3, ":head_horses"),
		(assign, reg4, ":acres_grain"),
		(assign, reg5, ":acres_olives"),
		(assign, reg6, ":acres_vineyard"),
		(assign, reg7, ":acres_flax"),
		(assign, reg8, ":acres_dates"),
		(assign, reg9, ":fishing_fleet"),
		(assign, reg10, ":salt_pans"),
		(assign, reg11, ":apiaries"),
		(assign, reg12, ":silk_farms"),
		(assign, reg13, ":kirmiz_farms"),
		(assign, reg14, ":iron_deposits"),
		(assign, reg15, ":fur_traps"),
		(assign, reg16, ":household_gardens"),
		
		(assign, reg17, ":mills"),
		(assign, reg18, ":breweries"),
		(assign, reg19, ":wine_presses"),
		(assign, reg20, ":olive_presses"),
		(assign, reg21, ":linen_looms"),
		(assign, reg22, ":silk_looms"),
		(assign, reg23, ":wool_looms"),
		(assign, reg24, ":pottery_kilns"),
		(assign, reg25, ":smithies"),
		(assign, reg26, ":tanneries"),
		(assign, reg27, ":shipyards"),
		
		
		(assign, reg0, cost_head_cattle),
		(str_store_string, s1,  "@Cattle farms({reg1})   {reg0}"),
		(assign, reg0, cost_head_sheep),
		(str_store_string, s2,  "@Sheep farms({reg2})    {reg0}"),
		(assign, reg0, cost_head_horses),
		(str_store_string, s3,  "@Horse stables({reg3})  {reg0}"),
		(assign, reg0, cost_acres_grain),
		(str_store_string, s4,  "@Grain farms({reg4})    {reg0}"),
		(assign, reg0, cost_acres_olives),
		(str_store_string, s5,  "@Olive farms({reg5})    {reg0}"),
		(assign, reg0, cost_acres_vineyard),
		(str_store_string, s6,  "@Vineyard farms({reg6}) {reg0}"),
		(assign, reg0, cost_acres_flax),
		(str_store_string, s7,  "@Flax farms({reg7})     {reg0}"),
		(assign, reg0, cost_acres_dates),
		(str_store_string, s8,  "@Date farms({reg8})     {reg0}"),
		(assign, reg0, cost_fishing_fleet),
		(str_store_string, s9,  "@Fishing fleets({reg9}) {reg0}"),
		(assign, reg0, cost_salt_pans),
		(str_store_string, s10, "@Salt pans({reg10})     {reg0}"),
		(assign, reg0, cost_apiaries),
		(str_store_string, s11, "@Apiaries({reg11})      {reg0}"),
		(assign, reg0, cost_silk_farms),
		(str_store_string, s12, "@Silk farms({reg12})    {reg0}"),
		(assign, reg0, cost_kirmiz_farms),
		(str_store_string, s13, "@Kirmz famrs({reg13})   {reg0}"),
		(assign, reg0, cost_iron_deposits),
		(str_store_string, s14, "@Iron deposits({reg14}) {reg0}"),
		(assign, reg0, cost_fur_traps),
		(str_store_string, s15, "@Fur traps({reg15})     {reg0}"),
		(assign, reg0, cost_household_gardens),
		(str_store_string, s16, "@Gabbage farms({reg16}) {reg0}"),
		
		(assign, reg0, cost_mills),
		(str_store_string, s17, "@Mills({reg17})         {reg0}"),
		(assign, reg0, cost_breweries),
		(str_store_string, s18, "@Breweries({reg18})     {reg0}"),
		(assign, reg0, cost_wine_presses),
		(str_store_string, s19, "@Wineries({reg19})      {reg0}"),
		(assign, reg0, cost_olive_presses),
		(str_store_string, s20, "@Olive presses({reg20}) {reg0}"),
		(assign, reg0, cost_linen_looms),
		(str_store_string, s21, "@Linen looms({reg21})   {reg0}"),
		(assign, reg0, cost_silk_looms),
		(str_store_string, s22, "@Silk looms({reg22})    {reg0}"),
		(assign, reg0, cost_wool_looms),
		(str_store_string, s23, "@Wool looms({reg23})    {reg0}"),
		(assign, reg0, cost_pottery_kilns),
		(str_store_string, s24, "@Pottery kilns({reg24}) {reg0}"),
		(assign, reg0, cost_smithies),
		(str_store_string, s25, "@Smithies({reg25})      {reg0}"),
		(assign, reg0, cost_tanneries),
		(str_store_string, s26, "@Tanneries({reg26})     {reg0}"),
		(assign, reg0, cost_shipyards),
		(str_store_string, s27, "@Shipyards({reg27})     {reg0}"),
	])