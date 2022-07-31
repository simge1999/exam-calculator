def exam_score(number):
	if number == 100:
		print(str(number) + ": You are best.")
	elif number >= 85 and number <= 99:
		print(str(number) + ": Top score")
	elif number <= 85 and number >=70:
	    print(str(number)+ ": It can be better.Work more harder.") 
	elif number <= 70 and number >= 61:
		print(str(number)+ ": You must work harder.")
	elif number >= 60:
		print(str(number) + ": You barely passed.")
	else:
		print(str(number) + ": Failed")
exam_score(70)
exam_score(57)
exam_score(20)
exam_score(98)
exam_score(100)
exam_score(78)
exam_score(57)
exam_score(60)
exam_score(80)

def last_semester(first,second):
	exam1 = first * 70 / 100
	exam2 = second * 30 / 100
	total = exam1 + exam2

	if total >= 90:
		print(str(total) + ": A")
	elif total <= 89 and total >= 80:
		print(str(total) + ": B")
	elif total >= 79 and total <= 70:
		print(str(total) + ": C")
	elif total <= 69 and total >= 60:
		print(str(total) + ": D")
	else:
		print(str(total) + ": You failed.Try another year.")
last_semester(30,69)
last_semester(57,67)
last_semester(57,97)
last_semester(85,69)
last_semester(96,87)