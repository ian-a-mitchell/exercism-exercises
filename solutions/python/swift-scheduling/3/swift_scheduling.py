from datetime import datetime, timedelta

TIMECODE = "%Y-%m-%dT%H:%M:%S"

QUARTERS = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 3,
    10: 4,
    11: 4,
    12: 4
}

IN_Q = {
        1: 3,
        2: 6,
        3: 9,
        4: 12
}

FRONT_WEEK = (0, 1, 2)
BACK_WEEK = (3, 4)

FRI = 4
SUN = 6

EAR = 8
EOD = 17
MID = 13
LEOW = 20

def set_time(date, time):
        
    return date.replace(hour = time, minute = 0, second = 0)

def set_month(key_year, key_month, key_day):
    
    output = datetime(year = key_year, month = key_month, day = key_day)
            
    return set_time(output, EAR)

def delivery_date(start, description):
    
    output = datetime.strptime(start, TIMECODE)
    
    match description:
        case "NOW":
            
            output = output + timedelta(hours = 2)
            
        case "ASAP":
            
            if output.hour < MID:
                output = set_time(output, EOD)
            else:
                output = output + timedelta(days = 1)
                output = set_time(output, MID)
                
        case "EOW":
            
            weekday = output.weekday()
            
            if weekday in FRONT_WEEK:
                output = output + timedelta(days = (FRI - weekday))
                output = set_time(output, EOD)
                
            elif weekday in BACK_WEEK:
                output = output + timedelta(days = (SUN - weekday))
                output = set_time(output, LEOW)
                
        case description if description[-1] == "M" and description[0] != "Q":
            
            key_month = int(''.join([x for x in description if x.isdigit()]))
            cur_month = output.month
            
            key_day = 1
            
            if cur_month < key_month:
                output = set_month(output.year, key_month, key_day)
            else:
                output = set_month(output.year + 1, key_month, key_day)
                
            weekday = output.weekday()
            
            # If the first day of the month is a weekend, move due date forward.
            if weekday not in (FRONT_WEEK + BACK_WEEK):
                output = output + timedelta(7 - weekday)
                
        case description if description[0] == "Q" and description[-1] != "M":
            
            key_q = int(''.join([x for x in description if x.isdigit()]))
            cur_q = QUARTERS[output.month]
            
            key_day = 30
            key_month = IN_Q[key_q]
            if key_month in (3, 12): # Adjust last day for March and December
                key_day = 31

            if cur_q <= key_q:
                output = set_month(output.year, key_month, key_day)
            else:
                output = set_month(output.year + 1, key_month, key_day)
                
            # If the last day of the quarter is a weekend, move due date back.
            weekday = output.weekday()
            
            if weekday not in (FRONT_WEEK + BACK_WEEK):
                output = output + timedelta(-(weekday - FRI))
                
        case _:
            
            raise ValueError('unknown description code')
    
    return output.strftime(TIMECODE)