from inc_time import inc_time
import bcd_conv

days = 200
hours = 13
minutes = 33
sec = 33

file = open("irig_frames.txt","w")
file.write("2")
file.write("\n")


for x in range(1,3):

	# sec_data
	sub_frame = []
	file.write(str(2))
	file.write("\n")
	sub_frame = bcd_conv.conv_bcd(sec)
	for i in range(0,4):
		file.write(str(sub_frame[i]))
		file.write("\n")
	file.write(str(0))
	file.write("\n")
	for i in range(4,7):
		file.write(str(sub_frame[i]))
		file.write("\n")



    #Min Data
	sub_frame = []
	file.write(str(2))
	file.write("\n")
	sub_frame = bcd_conv.conv_bcd(minutes)
	for i in range(0,4):
		file.write(str(sub_frame[i]))
		file.write("\n")
	file.write(str(0))
	file.write("\n")

	for i in range(4,7):
		file.write(str(sub_frame[i]))
		file.write("\n")


	
	file.write(str(0))
	file.write("\n")

	# Hours Data

	sub_frame = []
	file.write(str(2))
	file.write("\n")
	sub_frame = bcd_conv.conv_bcd(hours)
	for i in range(0,4):
		file.write(str(sub_frame[i]))
		file.write("\n")
	
	file.write(str(0))
	file.write("\n")

	for i in range(4,6):
		file.write(str(sub_frame[i]))
		file.write("\n")

	file.write(str(0))
	file.write("\n")
	
	file.write(str(0))
	file.write("\n")

	# Days Data 

	sub_frame = []
	file.write(str(2))
	file.write("\n")
	sub_frame = bcd_conv.conv_bcd(days%100)
	for i in range(0,4):
		file.write(str(sub_frame[i]))
		file.write("\n")
	
	file.write(str(0))
	file.write("\n")

	for i in range(4,8):
		file.write(str(sub_frame[i]))
		file.write("\n")

	#days hundreds
	sub_frame = []
    
	file.write(str(2))
	file.write("\n")

	sub_frame = bcd_conv.conv_bcd((days-(days%100))/100)
	for i in range(0,2):
		file.write(str(sub_frame[i]))
		file.write("\n")
	for i in range(2,9):
		file.write(str(0))
		file.write("\n")

	# garbge frame #1

	file.write(str(2))
	file.write("\n")

	for i in range(0,9):
		file.write(str(0))
		file.write("\n")

	# Garbage frame 2

	file.write(str(2))
	file.write("\n")

	for i in range(0,9):
		file.write(str(0))
		file.write("\n")

	# garbge frame #3

	file.write(str(2))
	file.write("\n")

	for i in range(0,9):
		file.write(str(0))
		file.write("\n")

	# Garbage frame 4

	file.write(str(2))
	file.write("\n")

	for i in range(0,9):
		file.write(str(0))
		file.write("\n")

	# Garbage frame 5

	file.write(str(2))
	file.write("\n")

	for i in range(0,9):
		file.write(str(0))
		file.write("\n")

	file.write(str(2))
	file.write("\n")











file.close()
print("File Closed \n")



















	



    



