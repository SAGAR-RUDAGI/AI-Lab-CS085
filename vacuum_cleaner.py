import random
print("Status : Dirty, clean")

env = [None,None]
env[0] = random.choice(["Dirty", "Clean"])
env[1] = random.choice(["Dirty", "Clean"])

pos = int(input("Position (l = 0 or r = 1) : "))

def clean():
	global pos
	if env[pos] == "Dirty":
		env[pos] = "Clean"
		return "Suck"
	elif pos == 0:
		pos = 1
		return "Right"
	elif pos == 1:
		pos = 0
		return "Left"

while "Dirty" in env:
	env[0] = random.choice(["Dirty", "Clean"])
	env[1] = random.choice(["Dirty", "Clean"])
	print(clean())

else:
	print(env)
