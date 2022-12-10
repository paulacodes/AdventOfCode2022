def part1():
	with open('inputs/day10.txt') as f:
		lines = f.readlines()
	current_x_value = 1
	cycle_counts = []
	for line in lines:
		if line.rstrip() == "noop":
			cycle_counts.append(current_x_value)
		else:
			cycle_counts.append(current_x_value)
			current_x_value += int(line.rstrip().split(" ")[1])
			cycle_counts.append(current_x_value)
	signal_strength_sum = 0
	for i in [20, 60, 100, 140, 180, 220]:
		signal_strength_sum += cycle_counts[i-2]*i
	print(signal_strength_sum)

def part2():
	with open('inputs/day10.txt') as f:
		lines = f.readlines()
	pixel_matrix = []
	for i in range(6):
		pixel_row = []
		for j in range(40):
			pixel_row.append(".")
		pixel_matrix.append(pixel_row)
		
	current_x_value = 1
	current_crt_position = 0
	current_crt_row = 0
	current_crt_col = 0
	sprite_position = [0,1,2]

	for line in lines:
		if line.rstrip() == "noop":
			if current_crt_col in sprite_position:
				pixel_matrix[current_crt_row][current_crt_col] = "#"
			current_crt_position += 1
			current_crt_col = current_crt_position % 40
			current_crt_row = int(current_crt_position / 40)
		else:
			current_x_value += int(line.rstrip().split(" ")[1])
			for i in range(2):
				if current_crt_col in sprite_position:
					pixel_matrix[current_crt_row][current_crt_col] = "#"
				current_crt_position += 1
				current_crt_col = current_crt_position % 40
				current_crt_row = int(current_crt_position / 40)
			sprite_position = [current_x_value - 1, current_x_value, current_x_value + 1]

	for i in pixel_matrix:
		row = ""
		for j in i:
			row += j
		print(row)

part1()
part2()