def leap_year(year):               
    return not year % 4 and (year % 100 != 0 or not year % 400)