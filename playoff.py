from random import shuffle, choice


def random_score() -> tuple:
	list_0_7 = [x for x in range(7)]
	score_1 = choice(list_0_7)
	list_0_7.pop(score_1)
	score_2 = choice(list_0_7)
	return (score_1, score_2)

def main():
	teams = ["Arsenal", "Manchester City", "Manchester United", "Chelsea",
			"Liverpool", "Real Madrid", "Tottenham Hotspur", "West Ham United",
			"Everton", "Hull City", "Stoke City", "Middlesbrough",
			"Watford", "Rangers", "Southampton", "Lelcester City"]
	
	history = dict()
	
	print("Play-off championship simulator")
	print("Total: {} teams".format(len(teams)))
	print()

	shuffle(teams)
	
	for stage in ("1/8", "1/4", "1/2", "Final"):
		winners = list()
		print("{}:".format(stage))
		for i in range(len(teams)//2):
			team_1 = teams.pop()
			team_2 = teams.pop()
			score = random_score()
			if score[0] > score[1]:
				winners.append(team_1)																						
				print('{} {} - {} {}'.format(team_1, score[0], score[1], team_2))
			else:
				winners.append(team_2)
				print('{} {} - {} {}'.format(team_2, score[1], score[0], team_1))
			history[team_1] = history.get(team_1, '') + '{}: {} {} - {} {}\n'.format(stage, team_1, score[0], score[1], team_2)
			history[team_2] = history.get(team_2, '') + '{}: {} {} - {} {}\n'.format(stage, team_2, score[1], score[0], team_1)
		teams = winners
		print()
		
	team = input('Enter team name case sensitive (e.g. Chelsea): ')
	print()
	while team != '':
		print(history.get(team, 'no such team!'))
		team = input()
	

if __name__ == "__main__":
	main()
