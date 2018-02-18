import random

def choose():
	sezon = random.randint(1,4)
	read_txt = open('black-mirror.txt', 'r')

	if sezon == 1 or sezon == 2:
		bolum = random.randint(1,3)
	elif sezon == 3:
		bolum = random.randint(0,6)
	elif sezon == 4:
		bolum = random.randint(1,6)

	sonuc = 'S{}B{}'.format(sezon, bolum)
		
	split = read_txt.read().split()		
	for i in split:
		if i == sonuc:
			read_txt.close()
			print('varolan secildi')
			return choose()

	read_txt.close()
	print(sonuc)
	save_txt = open('black-mirror.txt', 'a')
	save_txt.write(' {}'.format(sonuc))
	save_txt.close()

choose() 

