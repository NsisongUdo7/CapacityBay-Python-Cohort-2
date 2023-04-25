# A program to get a score from a user which will print the appropriate grade.

Math_Score = int(input("Enter score "))

if Math_Score >= 70 and Math_Score <= 100:
    print("A")
elif Math_Score >= 60 and Math_Score <= 69:
    print("B")
elif Math_Score >= 50 and Math_Score <= 59:
    print("C")
elif Math_Score >= 40 and Math_Score <= 49:
    print("D")
elif Math_Score >= 30 and Math_Score <= 39:
    print("E")
elif Math_Score < 30:
    print("F")
else:
    print("Not Available")