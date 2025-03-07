import time
print("Hello user, may I know your name?")

name = input("Enter your name: ")
time.sleep(1)
print("Hello," + name, "how are you?")
time.sleep(1)

while True:
	try:
		assign_grade = int(input("What is your grade: "))
		if assign_grade >=90:
			print("Grade A")
		
		elif assign_grade >=80:
			print("Grade B")
		
		elif assign_grade >=70:
			print("Grade C")
		
		elif assign_grade >=60:
			print("Grade D")
			
		elif assign_grade <=60:
			print("Grade F")
		
		else:
			print("please inpur your age in no.")
			break
			
	except ValueError:
			print("please input your grade in no.")