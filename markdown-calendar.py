import time
import sys

def repeat(char,count) :
    rs = ''
    for i in range(count) :
        rs += char
    return rs

HOUR=3600
DAY=24*HOUR
days = ["Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"]
months = ["January","February","March","April","May","June","July","August","September","November","December"]

now = time.localtime()
print(now)

if 2 == len(sys.argv) :
    month = int(sys.argv[1])
    now = time.localtime(time.mktime(now) + 30*DAY*(month - now.tm_mon) + DAY*(15 - now.tm_mday))

print(now)
now = time.localtime(time.mktime(now)
                     + (1 - now.tm_mday)*DAY
                     + (12 - now.tm_hour)*HOUR
                     -now.tm_min * 60
                     -now.tm_sec)
print("first of month:",now)
first_sunday = time.mktime(now) - ((now.tm_wday+1)%7)*DAY 

print(time.localtime(first_sunday))

top = "|"
magic = "|"
for d in days :
    top += "  "+d+"day  |"
    magic += " :"+repeat('-',3+len(d))+": |"
print(top)
print(magic)

line = '|'
body = ''
for mday in range(6*7) :
    ts = time.localtime(first_sunday + mday*DAY)
    entry = ''
    if ts.tm_mon == now.tm_mon :
        entry = "[%d](#%d)"%(ts.tm_mday,ts.tm_mday)
        body += '## <a name=%d>%sday, %s %d</a>\n'%(ts.tm_mday,days[(ts.tm_wday+1)%7],months[ts.tm_mon-1],ts.tm_mday)
    fmt = "%%%ds |"%(6+len(days[mday%7]))
    line += fmt%(entry)
    if 6 == (mday%7) :
        print(line)
        line = '|'
    if 0 == (mday%7) :
        if now.tm_mon < 11 and ts.tm_mon > now.tm_mon : break
        if now.tm_mon == 11 and ts.tm_mon == 0 : break
        
print(body)

