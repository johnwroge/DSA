

'''

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.


How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

def count_first_sundays():
    curr_day = 1 
    total_sundays = 0
    
    def get_days_in_month(month, year):
        if month in [4, 6, 9, 11]:  
            return 30
        elif month == 2:  # February
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            return 28
        else:
            return 31
    
    # Start from 1900 to set up correct day of week
    for year in range(1900, 2001):
        for month in range(1, 13):
            # Count Sundays on first of month (but only from 1901-2000)
            if curr_day == 0 and year >= 1901:  # Sunday is 0
                total_sundays += 1
                
            # Move to first day of next month
            days = get_days_in_month(month, year)
            curr_day = (curr_day + days) % 7
            
    return total_sundays

print(count_first_sundays())  # Output: 171
        
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_sundays():
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Start from January 1, 1901
    # January 1, 1901 was a Tuesday (day = 2)
    day = 2  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    sundays = 0
    
    for year in range(1901, 2001):
        for month in range(12):
            # Check if it's Sunday (day == 0) on the first of the month
            if day == 0:
                sundays += 1
                
            # Add days in current month
            days = days_in_month[month]
            
            # Adjust February for leap years
            if month == 1 and is_leap_year(year):
                days = 29
                
            # Update day of week
            # (current day + number of days in month) % 7 gives us the day of week
            # for the first of next month
            day = (day + days) % 7
            
    return sundays

print(count_sundays())  
