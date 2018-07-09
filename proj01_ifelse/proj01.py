# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!

# part1
currentMonth=7;
currentDay=9;
userName = raw_input("Enter your name: ")
userGrade =  raw_input("Enter your grade: ")
grad = 13-int(userGrade)
userName=userName.lower()
userName=userName[0].upper()+userName[1:]
print userName + ", you will graduate high school in", grad , "years."

# part2
# conditional
name=raw_input("Enter your name: ")
month=raw_input("Enter your birth month (number): ")
day=raw_input("Enter your birth day (number): ")
month=int(month)
day=int(day)
monthTill=0
dayTill=0
if month>=currentMonth :
    monthTill=int(month)-currentMonth
else :
    monthTill=12-(currentMonth-int(month))
if day>currentDay :
    dayTill=int(day)-currentDay
else :
    monthTill -= 1
    dayTill=30-(currentDay-int(day))
name=name.lower()
name=name[0].upper()+name[1:]
print name+", your birthday is in", monthTill,"months and",dayTill,"days!"
age=raw_input("Enter your age (number of years): ")
age=int(age)
ret= "You can see: G-rated movies, "
if age>=5 :
    ret+= "PG-rated movies, "
if age>=13 :
    ret+="PG-13 rated movies, "
if age>=17 :
    ret+="R-rated movies."
print ret