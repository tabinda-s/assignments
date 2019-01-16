birthday = "1/May/12"

#Goal:print date as "5/1/2012"

import datetime

raw_date = "1-May-12"

date_format = "%d/%B/%y"

parsed_date = datetime.datetime.strptime (birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") 
print(date_str)