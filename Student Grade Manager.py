name = input("Enter your name :")
marks = {}
for subject in ["Maths","Chemistry","Phyics"] :
    while True :
        try :
            score = float(input("Enter marks for {subject}(o-100) :"))
            if 0<= score <= 100 :
                marks[subject] = score
                break
            else :
                print("Number must be between 0 to 100 ")
        except ValueError :
            print("Invalid input! Please enter a number")
total = sum(marks.values())
average = total/len(marks)
print("Name :",name)
print("Marks :",marks)
print("Total marks",marks,"/300")
print("Average marks :",average)
if average >= 90 :
    grade = "A"
elif average >= 80 :
    grade = "B"
elif average >= 70 :
    grade = "C"
elif average >= 60 :
    grade = "D"
else :
    grade = "E"
print("Grade =",grade)