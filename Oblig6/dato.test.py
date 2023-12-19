import dato

date = dato.Dato(15, 12, 2023)

print(date.les_aar())

if date.check_date(15) is True:
    print("Lønningsdag!")
elif date.check_date(1) is True:
    print("Ny måned, nye muligheter")

date_readable = str(date)
print(date_readable)

date.increase_day()

print(date)

u_day = int(input("Skriv en dag: "))
u_mnth = int(input("Skriv en måned: "))
u_yr = int(input("Skriv et år: "))

print(date.compare(dato.Dato(u_day, u_mnth, u_yr)))