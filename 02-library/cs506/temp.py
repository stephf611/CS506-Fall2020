ret = []
with open("./temp.txt", "r") as f:
	lines = f.readlines()
    for line in lines:
    	#do something
    	# line looks like "value, value, value, ..."
    	list_of_strings = line.split(",")
    	res = [eval(x) for x in list_of_strings]
    	ret += res
 print(ret)