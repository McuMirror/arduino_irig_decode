def inc_time(days,hours,minutes,sec):

	if(sec == 59):
		sec = 0
		minutes = minutes + 1 
	else:
		sec = sec + 1

	if(minutes == 60):
		minutes = 0
		hours = hours + 1
	else:
		minutes = minutes + 1
	if(hours == 24):
		hours = 0
		days = days +1
	else :
		hours = hours +1

	return days,hours,minutes,sec

