from datetime import datetime
from datetime import date
ts = int("1603115260")

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
a = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d ')
print(a)
today = date.today().strftime('%Y-%m-%d ')

print(today)

if(a==today):
  print(1)
else:
  print(0)

