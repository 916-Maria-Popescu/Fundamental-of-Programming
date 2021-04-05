

def count_days_between_two_dates(date1, date2):
    """
    It return the number of days between two dates.
    The dates must have the following format : <dd.mm.yyyy>
    """
    date1, date2 = date1.split("."), date2.split(".")
    day1, day2, month1, month2, year1, year2 = date1[0], date2[0],  date1[1], date2[1], date1[2], date2[2]
