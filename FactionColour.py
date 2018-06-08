from module_factions import *

def FactionColour():
	#var
	i = 0
	for faction in factions:
		if(len(faction)>6):
			print("(troop_set_slot, \"trp_temp_array_a\", "+str(i)+", \"fac_"+faction[0]+"\"),")
			print("(troop_set_slot, \"trp_temp_array_b\", "+str(i)+", "+hex(faction[6])+"),")
			i+=1

FactionColour()