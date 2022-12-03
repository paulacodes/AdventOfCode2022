def part1():
	priorities_sum = 0
	with open('inputs/day3.txt') as f:
		for line in f:
			rucksack_items = line.rstrip()
			first_compartment_items = rucksack_items[0:int(len(rucksack_items)/2)]
			second_compartment_items = rucksack_items[int(len(rucksack_items)/2):len(rucksack_items)]
			for letter in first_compartment_items:
				if letter in second_compartment_items:
					priorities_sum += get_letter_priority(letter)
					break
	f.close()
	print(priorities_sum)

def part2():
	priorities_sum = 0
	group_number = 0
	group_elves = []
	with open('inputs/day3.txt') as f:
		for line in f:
			rucksack_items = line.rstrip()
			group_elves.append(rucksack_items)
			group_number += 1
			if group_number%3 == 0:
				for letter in group_elves[0]:
					if letter in group_elves[1] and letter in group_elves[2]:
						priorities_sum += get_letter_priority(letter)
						break
				group_number = 0
				group_elves = []
	f.close()
	print(priorities_sum)

def get_letter_priority(letter):
	if letter.islower():
		return(ord(letter)-96)
	else:
		return(ord(letter)-38)

part1()
part2()