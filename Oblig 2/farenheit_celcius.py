#Omgjør farenheit til celcius

def farenheit_til_celcius(farenheit):
    #Gjør om til celcius ved hjelp av formelen
    celcius = round((float(farenheit) - 32) * (5/9), 2)
    #Returnerer temperaturen i celcius 
    return celcius

if __name__ == "__main__":
    temp = input("Temperaturen i farenheit: ")
    #Printer både tempaturen i farenheit og celcius til konsollet
    print(f'{temp} grader F er lik {farenheit_til_celcius(temp)} grader C')
    