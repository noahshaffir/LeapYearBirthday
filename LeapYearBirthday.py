year = int(input("""Welcome to the age calculator for those born on February 29. 
You guys only have a birthday every 4 years, unlike everyone else.
Please input your year of birth."""))
current_year = int(input("Please enter the current year."))
age = 0
while current_year > year:
    if current_year%4!=0:
        current_year-=1
    else:
        age+=1
        current_year-=4
print(f"{age} is how old you really are.")
