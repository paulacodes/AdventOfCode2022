def part1():
	get_character_number_based_on_marker_length(4)

def part2():
	get_character_number_based_on_marker_length(14)

def get_character_number_based_on_marker_length(marker_length):
	with open('inputs/day6.txt') as f:
		datastream = f.readline()
	f.close()
	for i in range(len(datastream)):
		chars = []
		for j in range(marker_length):
			chars.append(datastream[i+j])
		if len(set(chars)) == len(chars):
			print(i+marker_length)
			break

part1()
part2()
