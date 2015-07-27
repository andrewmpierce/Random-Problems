class Epact:
    def __init__(self):
        self.year = input("Enter a 4 digit year.  ")

    def calc_C(self):
        C = self.year//100
        return C

    C = calc_C()

    def calc_epact(self, C):
        epact = (8 + (C // 4)) - C + ((8C + 13) // 25) + 11 
