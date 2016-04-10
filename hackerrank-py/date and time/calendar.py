import datetime

month, day,year = map(int,raw_input().split())

dt = datetime.date(year,month,day)

k = dt.weekday()
if k == 0:
    print "MONDAY"
elif k == 1:
    print "TUESDAY"
elif k == 2:
    print "WEDNESDAY"
elif k == 3:
    print "THURSDAY"
elif k == 4:
    print "FRIDAY"
elif k == 5:
    print "SATURDAY"
elif k == 6:
    print "SUNDAY"


