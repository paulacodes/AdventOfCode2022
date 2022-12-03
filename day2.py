def part1():
	move_scores = {"X":1, "Y":2, "Z":3}
	game_scores = {"A Z":0, "B X":0, "C Y":0, "A X":3, "B Y":3, "C Z":3, "A Y":6, "B Z":6, "C X":6}
	total_score = 0
	with open('day2.txt') as f:
		for line in f:
			game = line.rstrip()
			my_move = game.split(" ")[1]
			total_score += move_scores[my_move] + game_scores[game]	
	f.close()
	print(total_score)

def part2():
	loss_matches = {"A":"Z", "B":"X", "C":"Y"}
	draw_matches = {"A":"X", "B":"Y", "C":"Z"}
	win_matches = {"A":"Y", "B":"Z", "C":"X"}
	move_scores = {"X":1, "Y":2, "Z":3}
	total_score = 0
	with open('day2.txt') as f:
		for line in f:
			game = line.rstrip()
			opponent_move = game.split(" ")[0]
			my_ending = game.split(" ")[1]
			if my_ending == "X":
				total_score += 0 + move_scores[loss_matches[opponent_move]]
			elif my_ending == "Y":
				total_score += 3 + move_scores[draw_matches[opponent_move]]
			elif my_ending == "Z":
				total_score += 6 + move_scores[win_matches[opponent_move]]
	f.close()
	print(total_score)

part1()
part2()