from datetime import datetime, date, time

# Pobranie aktualnego czasu UTC
dt_utc = datetime.utcnow()
print("UTC Time:", dt_utc)

# Pobranie aktualnego lokalnego czasu (zależne od ustawień komputera)
dt_local = datetime.now()
print("Local Time:", dt_local)

# Tworzenie nowych obiektów date, time i datetime
d = date(year=2023, month=6, day=4)
t = time(hour=14, minute=30, second=59)
dt = datetime(year=2050, month=10, day=15, hour=12, minute=10, second=10)
print(d, t, dt, sep='\n')
d_n_t = datetime.combine(date=d, time=t)
print("Combined:", d_n_t)

# Tworzenie nowych obiektów date, time i datetime z wykorzystaniem funkcji fromisoformat
d = date.fromisoformat("2030-06-12")
t = time.fromisoformat("14:32:13")
dt = datetime.fromisoformat("2030-06-12 14:32:13")
print(d, t, dt, sep='\n')

# Formatowanie daty
date_string = "31.01.2020 15:30:00"
format_string = "%d.%m.%Y %H:%M:%S"
dt = datetime.strptime(date_string, format_string)
print(dt)

# Przykład prostego programu
input_date = input("Date (dd.mm.yyyy): ")
date = datetime.strptime(input_date, '%d.%m.%Y')
countdown = date - datetime.now()
print("Countdown in days:", countdown.days)
