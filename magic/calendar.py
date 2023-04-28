from datetime import datetime
from datetime import date,timedelta

d=datetime.now().date()
# print(d.date())
# print(d.date().strftime("%A"))
d1=date(2022,8,19)
print(d1)
# print(d-d1)
# print(d+31)
print(d1.strftime("%A"))
d1=d1+timedelta(days=28)
print(d1.strftime("%A"))