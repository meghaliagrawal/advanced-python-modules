import os
code =1
if code == 1:
	#reading and writing a text file 
	f = open("practice.txt","w+")
	f.write("i have created a nex text file named practice.txt")
	print (f"my txt file has been created at the location: {os.getcwd()}")
	print ("abcd")
	f.close()
	
