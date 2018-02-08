import datetime

today = datetime.date.today()
print('Today: ', today)

# Get EOP (End Of Period)
idx = (today.weekday() + 1) % 7 # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
lastsat = today - datetime.timedelta(7+idx-6)
print('EOP: ',lastsat)

# Get BOP (Beginning Of Period)
lastsun = today - datetime.timedelta(7+idx)
bop = lastsun - datetime.timedelta(days=2*365)
print('BOP: ', bop)
