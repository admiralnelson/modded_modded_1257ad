import re
def IntialiseIDItems():
	i = 0
	regex = re.compile(r"(?P<quote>['\"])(?P<string>.*?)(?<!\\)(?P=quote)")
	with open("module_items.py") as fileobject:
		for line in fileobject:
			if line.startswith(" [\"") or line.startswith("  [\"") or line.startswith("\t\t[\"") or line.startswith("\t[\"") or line.startswith("[\"") :
				match = regex.search(line)
				if match:
					print("itm_"+match.group('string')+" = " + str(i) ) 
				i += 1
IntialiseIDItems()
