def factorial (num):
    result=1
    if num == 0 or num ==1:
        return(1)
    elif num < 0:
        return(-1)
    else: 
        while num > 1:
            result*=num
            num -= 1
        return(result)

def leapYear (num):
    if num ==0:
        return(-1)
    elif (num % 400 == 0) or (num % 4 ==0 and num % 100 != 0):
        return (1)
    else:
        (-1)
        
    
    
def daysInMonth (mes, anno):
    if leapYear(anno) == 1 and mes == 2:
        return(29)
    elif mes == 2:
        return(28)
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes ==12:
        return(38)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return(30)
    return(-1)
    
    print(daysInMonth(0, 2020))
    
def dayOfWeek(dia, mes, anno):
    a = int ((14 - mes) / 12) 
    y = anno - a 
    m = mes + 12 * a - 2 
    d = ((dia + y + int (y/4) - int (y/100) + int (y/400) + (31*m)/12) % 7)
    return(d)
       
    
        
    