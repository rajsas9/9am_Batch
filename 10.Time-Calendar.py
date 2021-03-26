# Time and Calendar
import time 

time.
#####################################
Index	Attribute	Values
0	  tm_year	    0000, ...., 2018, ..., 9999
1	  tm_mon	    1, 2, ..., 12
2	  tm_mday	    1, 2, ..., 31
3	  tm_hour	    0, 1, ..., 23
4	  tm_min	    0, 1, ..., 59
5	  tm_sec	    0, 1, ..., 61
6	  tm_wday	    0, 1, ..., 6; Monday is 0
7	  tm_yday	    1, 2, ..., 366
8	  tm_isdst      0, 1 or -1
######################################

#No of tricks(seconds) from 12.00 am, 1 st Jan 1970
tricks = time.time()
print('no of tricks :',tricks)

# check the time difference use for pgm execution/response time etc..
t1=time.time()
t2=time.time()
t2-t1

t=time.localtime()
t
type(t)
t[0]
t[6]

time.asctime( time.localtime(time.time()) )
# for the above same we can use time.asctime()
# asctime is to get the time in readable format.
time.asctime()

time.timezone

time.tzname 

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

# Sleep
print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

tricks = time.time()
print(tricks)

result = time.localtime(1586139085)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

result = time.gmtime(1586139085)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)


##################################
%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - month [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 61]
###################################
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

#######################################################################
'''
A date in Python is not a data type of its own, but we can import a module named datetime 
to work with dates as date objects.

Directive	Description	                   Example	
%a	        Weekday, short version	         Wed	
%A	Weekday, full version	                 Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	   3	
%d	Day of month 01-31	                     31	
%b	Month name, short version	             Dec	
%B	Month name, full version	            December	
%m	Month as a number 01-12	                12	
%y	Year, short version, without century	18	
%Y	Year, full version	                    2018	
%H	Hour 00-23	                            17	
%I	Hour 00-12	                            05	
%p	AM/PM	                                PM	
%M	Minute 00-59	                        41	
%S	Second 00-59	                        08	
%f	Microsecond 000000-999999	            548513	
%z	UTC offset	                            +0100	
%Z	Timezone	                            CST	
%j	Day number of year 001-366	            365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	        Mon Dec 31 17:41:00 2018	
%x	Local version of date	                12/31/18	
%X	Local version of time	                17:41:00	
%%	A % character	                        %
'''
import datetime
print(dir(datetime))
############Get Current Date and Time#################
x = datetime.datetime.now()
print(x)
#The output date contains year, month, day, hour, minute, second, and microsecond.
print(x.year)
###############Get Current Date#######################
#today() method defined in the date class to get a date object containing the current local date.
x  = datetime.date.today()
print(x)
#objects into readable strings.
print(x.strftime("%A"))



x = datetime.datetime(2020, 5, 17) #(hour, minute, second, microsecond, tzone),default value of 0, (None for timezone)
print(x)
print(x.strftime("%B"))

from datetime import datetime
# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b) 

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

###############Difference between two dates and times##################
from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  
###################Handling timezone#####################

from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


#*********************CALENDER******************************

import calendar
calendar.
calendar.calendar(1250)
calendar.calendar(2019)

calendar.isleap(2016)
calendar.monthcalendar(2020,4)
calendar.monthcalendar(2020,04)  # Does not accept 04  #
calendar.firstweekday()
t=calendar.weekday(2018,8,1) 
t


