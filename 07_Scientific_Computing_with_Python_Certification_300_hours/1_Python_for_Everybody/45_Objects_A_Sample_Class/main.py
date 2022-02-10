class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 2
        print(self.x)


an = PartyAnimal()
an.party()
an.party()
