returned_day, returned_month, returned_year = [int(date) for date in input().split(' ')]
expected_day, expected_month, expected_year = [int(date) for date in input().split(' ')]

if (returned_year, returned_month, returned_day) <= (expected_year, expected_month, expected_day):
  print(0)
elif ( returned_year, returned_month ) == ( expected_year, expected_month ):
  print(15 * (returned_day - expected_day))
elif returned_year == expected_year:
  print(500 * (returned_month - expected_month))
else:
  print(10000)
