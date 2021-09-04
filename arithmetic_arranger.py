def arithmetic_arranger(problems,showAns = False):
	length = len(problems)
	if length > 5:
		return "Error: Too many problems."

	# get the larger number and set each length to its length plus 2
	#      1
	# - 3801
	# ------
	# the longer number is 3801 which is 4 digits long, then one space, and operator
	# 4 spaces in btwn each problem
	# dashes are equal to the length (6 in this case)
	#
	# have dict, and have each dict[i] = total length of each problem
	# 
	# will store all items to be printed in res array
	# then will iterate thru and concatenate all of res onto arranged_problems string
	# each 3 length(showAns=False) or 4(True) length subarray will contain
	# the first number followed by operator, then 2nd number and finally result(if True)

	arranged_problems = []

	if showAns == False:
		res = [0]*(length*3)
	else:
		res = [0]*(length*4)
	totalLength = [0]*length

	for i in range(length):
		curr = problems[i].split()
		totalLength[i] = max(len(curr[0]),len(curr[2])) + 2
		if totalLength[i] > 6:
			return "Error: Numbers cannot be more than four digits."
		if showAns == False:
			if curr[1] != '-' and curr[1] != '+':
				return "Error: Operator must be '+' or '-'."
			try:
				res[3*i] = int(curr[0])
				res[(3*i)+1] = curr[1]
				res[(3*i)+2] = int(curr[2])
			except:
				return "Error: Numbers must only contain digits."
		else:
			res[4*i] = curr[0]
			res[(4*i)+1] = curr[1]
			res[(4*i)+2] = curr[2]
			if curr[1] == '+':
				try:
					res[(4*i)+3] = int(curr[0])+int(curr[2])
				except:
					return "Error: Numbers must only contain digits."
			elif curr[1] == '-':
				try:
					res[(4*i)+3] = int(curr[0])-int(curr[2])
				except:
					return "Error: Numbers must only contain digits."
			else:
				return "Error: Operator must be '+' or '-'."
	
	# actual printing of the result
	# spaces need to be calculated by taking the total length of each problem
	# and subtracting the size of the number and operations(for line 2)
	# number of dashes is equal to totalLength

	if showAns:
		# line 1
		for i in range(length):
			for j in range(totalLength[i]-len(str(res[4*i]))):
				arranged_problems.append(" ")
			arranged_problems.append(str(res[4*i]))
			if i == length - 1:
				arranged_problems.append("\n")
			else:
				arranged_problems.append("    ")

		# line 2
		for i in range(length):
			arranged_problems.append(f"{res[(4*i)+1]} ")
			for j in range(totalLength[i]-len(str(res[(4*i)+2]))-2):
				arranged_problems.append(" ")
			arranged_problems.append(str(res[(4*i)+2]))
			if i == length - 1:
				arranged_problems.append("\n")
			else:
				arranged_problems.append("    ")

		# line 3
		for i in range(length):
			for j in range(totalLength[i]):
				arranged_problems.append('-')
			if i == length - 1:
				arranged_problems.append("\n")
			else:
				arranged_problems.append("    ")
		
		# line 4
		for i in range(length):
			for j in range(totalLength[i]-len(str(res[(4*i)+3]))):
				arranged_problems.append(" ")
			arranged_problems.append(str(res[(4*i)+3]))
			if i == length - 1:
				continue
			else:
				arranged_problems.append("    ")
	else:
		# line 1
		for i in range(length):
			for j in range(totalLength[i]-len(str(res[3*i]))):
				arranged_problems.append(" ")
			arranged_problems.append(str(res[3*i]))
			if i == length - 1:
				arranged_problems.append("\n")
			else:
				arranged_problems.append("    ")

		# line 2
		for i in range(length):
			arranged_problems.append(f"{res[(3*i)+1]} ")
			for j in range(totalLength[i]-len(str(res[(3*i)+2]))-2):
				arranged_problems.append(" ")
			arranged_problems.append(str(res[(3*i)+2]))
			if i == length - 1:
				arranged_problems.append("\n")
			else:
				arranged_problems.append("    ")

		# line 3
		for i in range(length):
			for j in range(totalLength[i]):
				arranged_problems.append('-')
			if i == length - 1:
				continue
			else:
				arranged_problems.append("    ")
	
	#print("\'","".join(arranged_problems),"\'",sep='')
	#print(res)
	return "".join(arranged_problems)