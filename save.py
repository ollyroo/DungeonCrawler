import io, os
def quicksave(x, y, mana, manamax, health, healthmax):
	savefile = io.open(os.path.join('saves' + '\\' + 'savefile.txt'), 'r')
	wholefile = savefile.readlines()
	savefile.close()
	savefile = io.open(os.path.join('saves' + '\\' + 'savefile.txt'), 'w')
	wholefile[0] = (str(x) + '\n')
	wholefile[1] = (str(y) + '\n')
	wholefile[3] = (str(health) + '\n')
	wholefile[4] = (str(healthmax) + '\n')
	wholefile[6] = (str(mana) + '\n')
	wholefile[7] = (str(manamax) + '\n')
	savefile.seek(0, 0)
	savefile.writelines(wholefile)
	savefile.close()
	print ("Quicksaved\nCharacter x =", str(x), "\nCharacter y = ", str(y))
	
def newgame():
	savefile = io.open(os.path.join('saves' + '\\' + 'savefile.txt'), 'w')
	file = ['-280\n', '-199\n', '\n', '80\n', '100\n', '\n', '100\n', '100\n']
	savefile.seek(0, 0)
	savefile.writelines(file)
	savefile.close()
	
