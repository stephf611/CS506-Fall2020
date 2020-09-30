def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    ret = []
    with open(csv_file_path, "r") as f:
    	lines = f.readlines()
    	for line in lines:
    		
    		# line looks like "value, value, value, ..."
    		list_of_strings = line.split(",")
    		list_of_values = []
    		for item in list_of_strings:
    			try:
    				v = int(item)
    				list_of_values.append(v)
    			except ValueError:
    				try:
    					v = float(item)
    					list_of_values.append(v)
    				except ValueError:
    					v = str(item)
    					list_of_values.append(v)
    		ret += list_of_values
    		
    return ret