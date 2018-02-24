from random import randint
from tkinter import *
from tkinter import ttk

def last_episode():
	global episode_show
	read_txt = open('black-mirror.txt', 'r')
	split_read_txt = read_txt.read().split()

	try:
		episode_show.config(text = "The episode you\rRandomed last time is\r{}".format(split_read_txt[-1]))
		print(split_read_txt)
	except:
		episode_show.config(text = "Didnt watch any episode yet\nClick the Button")
		print(split_read_txt)

def episode_selecter():
	global episode_show
	season = randint(1,4)
	read_txt = open('black-mirror.txt', 'r')

	if season == 1 or season == 2:
		episode = randint(1,3)
	elif season == 3:
		episode = randint(0,6)
	elif season == 4:
		episode = randint(1,6)

	selected_episode = 'S{}E{}'.format(season, episode)

	split_read_txt = read_txt.read().split()
	try:	
		for i in split_read_txt:
			if i == selected_episode:
				read_txt.close()
				print('Selected watched episode...')
				return episode_selecter()

		read_txt.close()
		print(selected_episode)
		save_txt = open('black-mirror.txt', 'a')
		save_txt.write(' {}'.format(selected_episode))
		save_txt.close()
		episode_show.config(text=selected_episode)

	except RecursionError:
		episode_show.config(text="No episode left to watch")

	

win = Tk()
win.title('Black Mirror random episode selecter')
win.configure(background="black")

mainframe = ttk.Frame(win, padding="5 5")
mainframe.grid(column=0, row=0)

episode_demand = Button(mainframe, command=episode_selecter, width=22, text='Click for random episode',fg="black", bg="white", font="Arial 16 bold")
episode_demand.grid(column=0, row=0)

episode_show = Label(mainframe, text="as", height=6, width=22, fg="white", bg="black", font="Arial 25 bold")
episode_show.grid(column=0, row=3)

last_episode()
win.mainloop()