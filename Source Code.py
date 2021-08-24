import kahoot

bots = []

pin = int(input("Game Pin: "))
botname = input("Bot Name: ")
num = int(input("Number Of Bots: "))

for i in range(num):
	bots.append(kahoot.client())
	bots[i].join(pin, " ".join([botname, str(i)]))
	bots[i].on("joined", lambda : print("Joined Bot #" + str(i)))