with open('input.txt', 'r') as file:
	x = 1
	checkpoints = {'20': 0, '60': 0, '100': 0, '140': 0, '180': 0, '220': 0}
	tick = 1
	for line in file:
		line = line.strip('\n').split()
		if line[0] == 'noop':
			if str(tick) in checkpoints:
				checkpoints[str(tick)] = x * tick
			tick += 1
		elif line[0] == 'addx':
			for i in range(0, 2):
				if str(tick) in checkpoints:
					checkpoints[str(tick)] = x * tick
				tick += 1
			x += int(line[1])
	sum = 0
	for element in checkpoints:
		sum += checkpoints[element]
	print(f'Checkpoints: {checkpoints}')
	print(f'Sum: {sum}')