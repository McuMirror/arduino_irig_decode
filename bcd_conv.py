def bcd(my_str):

	b =[0,0,0,0]

	if(my_str == 0):
		b[3] = 0
	else:
		if(my_str == 1):
			b[3] = 1
		else:
			if(my_str == 2):
				b[2] = 1
				#print("in Second \n")
			else:
				if(my_str == 3):
					b[3] = 1
					b[2] = 1
				else:
					if(my_str == 4):
						b[1] = 1
					else:
						if(my_str ==5):
							b[3] = 1
							b[1] = 1
						else:
							if(my_str == 6):
								b[2] = 1
								b[1] = 1
							else:
								if(my_str == 7):
									b[3] = 1
									b[2] = 1
									b[1] = 1
								else:
									if(my_str == 8):
										b[0] = 1
									else:
										b[0] = 1
										b[3] = 1
	b_1 = [0,0,0,0]
	b_1[0] = b[3]
	b_1[1] = b[2]
	b_1[2] = b[1]
	b_1[3] = b[0]
								

	return b_1

def conv_bcd(n_data):

	units = int(n_data%10)
	tens  = int((n_data-units)/10)
	#print(tens,units)
	bcd_0 = bcd(units)
	bcd_1 = bcd(tens)
	bcd_re = bcd_0 + bcd_1
	#print(bcd_re)

	return bcd_re

    





