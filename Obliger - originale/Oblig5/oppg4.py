def les_fil_måned(filnavn):
    MaxTemperaturer = {}

    fil = open(filnavn, "r")

    for linje in fil:
        måned, temperatur = linje.strip().split(",")
        MaxTemperaturer[måned] = float(temperatur)
    return MaxTemperaturer

def finn_rekord(month_max_dict, filnavn):
    fil = open(filnavn, "r")

    for linje in fil:
        måned, dag, temperatur = linje.strip().split(",")
        
        if float(temperatur) > month_max_dict[måned]:
            print(f'Ny varmerekord {dag} {måned}: {temperatur} grader Celcius (Gammel rekord var {month_max_dict[måned]})')
    
max_temps = les_fil_måned("max_temperatures_per_month.csv")

print(max_temps)

finn_rekord(max_temps, "max_daily_temperature_2018.csv")