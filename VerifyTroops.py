# -*- coding: utf-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *
import random
from header_common import *
from header_troops import *
from header_skills import *
from ID_items import *
from ID_scenes import *
from module_items import *
from module_troops import *

itp_type_horse

def VerifyTroop():
	#var
	i = 0
	for troop in troops:
		if (troop[3] & tf_mounted):
			itm_result = []
			itm_index = 0
			for itm in items:
				if ((itm[3] == itp_type_horse) or (itm[3] == itp_type_horse|itp_merchandise) ):
					#print itm[0] + " " + str(itm_index) + " " + str(hex(itm[3])) 
					itm_result += [itm_index]
				itm_index+=1
			#print troop[7]
			#print itm_result

			#var 
			count_item = 0
			print "\ntroop: " + troop[0] + " -- friendly name:" + troop[1]  + ". here's what inside his/her inv:"
			for itm_troop in troop[7]:
				#if(itm_troop in itm_result):
				#	print "troop: " + troop[0] + " contains mounts in his/her inv: " + str(itm_troop) + "  " + str(items[itm_troop][1])				
				if(itm_troop in itm_result):
					print "|-> item:" + str(items[itm_troop][0]) + " -- friendly name:" + str(items[itm_troop][1]) 					
			#	if (itm_troop in itm_result):
			#		count_item += 1
			#if(count_item<1):
			#	print "\ntroop: " + troop[0] + " -- friendly name:" + troop[1]  + " doesn't have any mounts in his/her inv. here's what inside his/her inv:"
			#	for itm_troop in troop[7]:
			#		print "|-> item:" + str(items[itm_troop][0]) + " -- friendly name:" + str(items[itm_troop][1]) 					
		i+=1
	print i

VerifyTroop()
itm_index = 0
itm_result = []
for itm in items:
	if ((itm[3] == itp_type_horse) or (itm[3] == itp_type_horse|itp_merchandise) ):
		#print itm[0] + " " + str(itm_index) + " " + str(hex(itm[3])) 
		itm_result += [itm_index]
	itm_index+=1
print "  "
print itm_result
#trp_result = [troop for troop in troops if (troop[3] & tf_mounted)]
#for troop in trp_result:
#	print troop[0] + " " + str(hex(troop[3]))+ " " + str(troop[7])
