b = "text"
while True:
	a = input()
	b += "\n" + a
	f= open("note.txt","w+")
	f.write(b)
	f.close()
