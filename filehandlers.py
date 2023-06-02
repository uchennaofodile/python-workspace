#open()
#file handlers must be closed after each use .close()
#two arguements path to file, and read or write

f1 = open("diary.txt", "r")
reading = f1.read()
print(reading)
f1.close()

f2 = open("diary2.txt", "w")
f2.write("Writing in my diary file!")
f2.close()