## Number of days in a month
def days_in_month(year, month):
    """
    Input:
        :int year
        :int month
    Output: 
        :int :number of days in a month
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 29
    else:
        return 28