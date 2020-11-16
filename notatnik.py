print("every note is writed")
while True:
	a = input("write: ")
	print(a)
	f= open("autosave.txt","w+")
	f.write(a)
	f.close() 
	b = input("do u want to save it? y/n ")
	if b == 'y':
		print('this file will name save.txt and it is only 1 file')
		f= open("save.txt","w+")
		f.write(b)
		f.close() 
