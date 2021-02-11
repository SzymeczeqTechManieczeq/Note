try:
    print("Write name and localisation of file which you want to edit or which you want to do.")
    b = "text"
    d = input()
    text = open(d,"a+").read()
    print(text)
    while True:
        a = input()
        b = b + "\n" + a
        f= open(d,"w+")
        f.write(b)
        f.close()
except KeyboardInterrupt:
    pass
