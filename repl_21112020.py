import datetime

d = datetime.date(2020, 1, 1)
print(d)
cd = datetime.date.today()
print(cd)
print(cd - d)
print(cd + datetime.timedelta(days=5))
print(cd - datetime.timedelta(days=5))
print(cd.strftime('%d-%b-%Y'))
print(datetime.datetime.strptime('1-1-2020', '%d-%m-%Y'))
