from datetime import datetime, UTC, date, time

# dt_utc = datetime.now(UTC)
# print("UTC Time:", dt_utc)
# print(dt_utc.strftime("%H:%M:%S"))

# dt_local = datetime.now()
# print("Local time:", dt_local)
# print(dt_local.strftime("%H:%M:%S"))


# d = date(year=2023, month=6, day=4)
# t = time(hour=14, minute=30, second=59)
# dt = datetime(year=2050, month=10, day=13, hour=22, minute=15, second=15)

# print(d, t, dt, sep='\n')

# d_n_t = datetime.combine(date=d, time=t)
# print("Combined:", d_n_t)


# d = date.fromisoformat("2025-09-22")
# t = time.fromisoformat("22:12:59")
# dt = datetime.fromisoformat("2025-09-22 22:12:59")

# print(d, t, dt, sep='\n')


# date_string = "22.09.2025 22:20:00"
# format_string = "%d.%m.%Y %H:%M:%S"
# dt = datetime.strptime(date_string, format_string)
# print(dt)


input_date = input("Date (dd.mm.yyyy): ")
date = datetime.strptime(input_date, "%d.%m.%Y")
countdown = date - datetime.now()

print("Countdown in days:", countdown.days)