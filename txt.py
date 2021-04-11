file = open("voice.txt", "r+")
f = open("voices.txt","w")
for x in file.readlines():
	y = x.replace(" ","")
	f.write(y+"\n")
	

	
	

