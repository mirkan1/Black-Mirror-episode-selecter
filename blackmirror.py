from random import randint

def episode_selecter():
	season = randint(1,4)
	read_txt = open('black-mirror.txt', 'r')

	if season == 1 or season == 2:
		episode = randint(1,3)
	elif season == 3:
		episode = randint(0,6)
	elif season == 4:
		episode = randint(1,6)

	selected_episode = 'S{}E{}'.format(season, episode)
		
	split = read_txt.read().split()		
	for i in split:
		if i == selected_episode:
			read_txt.close()
			print('Selected watched episode...')
			return episode_selecter()

	read_txt.close()
	print(selected_episode)
	save_txt = open('black-mirror.txt', 'a')
	save_txt.write(' {}'.format(selected_episode))
	save_txt.close()

episode_selecter() 

