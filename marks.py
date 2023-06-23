marks = input ("enter ur mark : ")
marks = float(marks)

if marks>=80 and marks<=100:
    print("ur grade is A+")
    
elif marks>=70 and marks<=79:
    print("ur grade is A")
elif marks>=60 and marks<=69:
    print("ur grade is A-")
elif marks>=50 and marks<=59:
    print("ur grade is B")
elif marks>=40 and marks<=49:
    print("ur grade is C")
elif marks>=33 and marks<=39:
    print("ur grade is D")
else :
    print("ur failed")
