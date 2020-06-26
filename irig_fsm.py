states = 0
sec_d = [0,0,0,0,0,0,0,0,0,0]
minutes_d = [0,0,0,0,0,0,0,0,0,0]
hours_d = [0,0,0,0,0,0,0,0,0,0]
days_d = [0,0,0,0,0,0,0,0,0,0]
days2_d = [0,0,0,0,0,0,0,0,0,0]

sec = 0
minutes = 0
hours = 0
days = 0

# Bit counter
b_cntr = 0


# State Var
state = 0
next_state = 0

st_unlock = 0
st_prelock= 1
st_start = 2
st_second = 3
st_minute =4
st_hour =5
st_days =6
st_days2 =7 
st_year =8
st_unused1= 9
st_unused2 = 10
st_unused3 = 11
st_unused4 = 12


ZERO = 0
ONE = 1
MARK = 2















def fsm(symbol_data):
	global state
	global b_cntr
	global next_state

	data = symbol_data.strip();
	symbol = int(data)
	print(symbol,":",state,":",b_cntr)
	#print(":")
	#print(state)

	if(state == st_unlock ):
		if(symbol == MARK):
			next_state = st_prelock
	else:
		if(state == st_prelock):
			if(symbol == MARK):
				next_state = st_second
		else:
			if(state == st_start):
				if(symbol == MARK):
					next_state = st_second
					b_cntr= 0
			else:
				if(state == st_second):
					if(symbol == MARK):
						next_state = st_minute
						b_cntr = 0
					else:
						sec_d[b_cntr] = symbol
						b_cntr = b_cntr +1
				else:
					if(state == st_minute):
						if(symbol == MARK):
							next_state = st_hour
							b_cntr = 0
						else:
							minutes_d[b_cntr] = symbol
							b_cntr = b_cntr +1
					else:
						if(state == st_hour):
							if(symbol == MARK):
								next_state = st_days
								b_cntr =0
							else:
								hours_d[b_cntr] = symbol
								b_cntr = b_cntr+1
						else:
							if(state == st_days):
								if(symbol == MARK):
									next_state = st_days2
									b_cntr = 0
								else:
									days_d[b_cntr] = symbol
									b_cntr = b_cntr +1
							else:
								if(state == st_days2):
									if(symbol == MARK):
										next_state = st_unused1
										b_cntr =0
									else:
										days2_d[b_cntr] = symbol
										b_cntr = b_cntr +1
								else:
									if(state == st_unused1):
										print(sec_d,minutes_d,hours_d)
										if(state == MARK):
											next_state = st_unused2
									else:
										if(state == st_unused2):
											if(symbol == MARK):
												next_state = st_unused3
										else:
											if(state == st_unused3):
												if(symbol == MARK):
													print(sec_d,minutes_d,hours_d)
													next_state = st_unused4
											else:
												if(state == st_unused4):
													if(symbol == MARK):
														next_state = st_start

	state = next_state













handle = open("irig_frames.txt")

for _ in range(0,101):
	data = handle.readline()
	fsm(data)