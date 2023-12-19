#Oppg 1
for i in range(1, 16):
    if i != 10:
        print(i)

#Oppg 2
def func(list: "list[int]"):
    smallest = list[0]

    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]

    return smallest

print(func([5, 7, 4, 9, 1]))

#Oppg 3
class Strenger:
    def __init__(self, strengverdi: str):
        self.strengverdi = strengverdi

    def get_strengverdi(self):
        return self.strengverdi
    
    def sjekk_gyldig_streng(self):
        if len(self.strengverdi) % 2 == 0:
            return True
        return False
    
    def split_streng(self):
        if self.sjekk_gyldig_streng() is False:
            return None

        list = []
        for i in range(int(len(self.strengverdi) / 2)):
            list.append(self.strengverdi[i*2] + self.strengverdi[i*2 + 1]) 

        return list
    
def main():
    streng1 = Strenger("ababbccd")

    print(streng1.sjekk_gyldig_streng())
    print(streng1.get_strengverdi())
    print(streng1.split_streng())

if __name__ == "__main__":
    main()