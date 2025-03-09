class Payload():
    def __init__(self):
        self.sto = None
        self.boja = None
        self.strategija = None
    def printPayload(self):
        print('Sto = ', self.sto)
        print('Boja = ', self.boja)
        print('Strategija = ', self.strategija)
        print('======================')

class run:

    def __init__(self):
        self.gamePayload = Payload()

    def start(self, payload):
        self.gamePayload.sto = payload.sto
        self.gamePayload.boja = payload.boja
        self.gamePayload.strategija = payload.strategija
        self.gamePayload.printPayload()



