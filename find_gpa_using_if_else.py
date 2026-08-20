#we find cgpa
gpa = float (input("Enter Your GPA :"))

if gpa < 0  or gpa > 4.00 :
  print("invalid GPA")
elif gpa == 4.00 :
  print("A+")
elif gpa >= 3.75:
  print ("A")
elif gpa >= 3.50 :
  print("A-")
elif gpa >= 3.25 :
  print ("B+")
elif gpa >= 3.00 :
    print("B")
elif gpa >= 2.75:
    print("B-")
elif gpa >= 2.50 :
    print("C+")
elif gpa >= 2.25 :
    print("C")
elif gpa >= 2.00:
    print("D")
else:
    print("F")
