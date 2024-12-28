def dayOfProgrammer(year):
    # Write your code here
    resp=""
    
    if year > 1918:
        if (year%4==0):
            resp=f"12.09.{year}"
        else:
            resp=f"13.09.{year}"
    else:
        if (year%400==0) and ((year%4==0)and(year%100!=0)):
            resp=f"13.09.{year}"
        else:
            resp=f"12.09.{year}"    
    return resp





year=1800


dia=dayOfProgrammer(year)

print(dia)