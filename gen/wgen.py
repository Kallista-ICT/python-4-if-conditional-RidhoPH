year = int(input("Enter your birth year: "))

if year in range(1928, 1946):                 #First threshold condition
 Category_Name = "Silent Generation"          #Category for first condition
elif year in range(1946, 1965):               #Second threshold condition
 Category_Name = "Baby Boomer"                #Category for second condition
elif year in range(1965, 1981):               #Third threshold condition
 Category_Name = "Generation X"               #Category for third condition
elif year in range(1981, 1997):               #Fourth threshold condition
 Category_Name = "Millennials"                #Category for fourth condition
elif year in range(1997, 2013):               #Fifth threshold condition
 Category_Name = "Generation Z"               #Category for fifth condition
else:                                         #Default condition for all other cases  
 Category_Name = "Generation Alpha"           #Default category for else condition

print(f"You belong to: {Category_Name}")