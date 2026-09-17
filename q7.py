# MAP A 0-100 SCORE TO A/B/C/FAIL (>=90,>=75,>=40,ELSE)
def letter_grade(marks):
    if marks>=90:
        return'grade A'

    elif marks>=75:
        return"grade B"

    elif marks>=40:
        return"grade C"
        
    else:
        return'Fail'

marks=int(input("enter the marks :"))
print(letter_grade(marks))