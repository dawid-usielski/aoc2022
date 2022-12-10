with open('input.txt', 'r') as file:
	# CODE SOMETIMES WORK AND SOMETIMES DOESN'T #
	# I HAVEN'T FIGURED OUT WHY YET #
	x = 1
	render = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
	tick = 1
	for line in file:
		line = line.strip('\n').split()
		if line[0] == 'noop':
			tick += 1
			render[x] = "#"
			if tick < 40:
				render[x] = "#"
			elif tick >= 40 and tick < 80:
				render[x+40] = "#"
			elif tick >= 80 and tick < 120:
				render[x+80] = "#"
			elif tick >= 120 and tick < 160:
				render[x+120] = "#"
			elif tick >= 160 and tick < 200:
				render[x+160] = "#"
			elif tick >= 200 and tick < 240:
				render[x+200] = "#"
		elif line[0] == 'addx':
			for i in range(0, 2):
				tick += 1
				if tick < 40:
					render[x] = "#"
				elif tick >= 40 and tick < 80:
					render[x+39] = "#"
				elif tick >= 80 and tick < 120:
					render[x+79] = "#"
				elif tick >= 120 and tick < 160:
					render[x+119] = "#"
				elif tick >= 160 and tick < 200:
					render[x+159] = "#"
				elif tick >= 200 and tick < 240:
					render[x+199] = "#"
			x += int(line[1])
	sum = 0
	for x in range(0, 40):
		print(render[x], end="")
	print()
	for x in range(40, 80):
		print(render[x], end="")
	print()
	for x in range(80, 120):
		print(render[x], end="")
	print()
	for x in range(120, 160):
		print(render[x], end="")
	print()
	for x in range(160, 200):
		print(render[x], end="")
	print()
	for x in range(200, 240):
		print(render[x], end="")
	print()