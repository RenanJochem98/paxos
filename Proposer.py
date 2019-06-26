from random import randint
class Proposer(object):
    def __init__(self, number, value):
        self.number = 0
        # self.number = number
        self.acceptors = []
        # self.value = value
        self.value = self.proposal_number()
        self.quantTotalProposers = 0
        self.server = None

    def getNumber(self):
        return self.number

    def setNumber(self, newId):
        self.number = newId

    # funcoes obrigatorias
    def proposal_number(self):
        return randint(1,1000)

    def prepare_request(self):
        self.server.send_prepare_request(self.number, self.value)

    # def accept_request(self, dictNumberValue):
    def accept_request(self, propNumber, propValue):
        if self.server is not None:
            # print("Proposer: "+str(self.number)+" envia numero "+str(sendId)+ ", com valor "+str(sendValue))
            # sendId = max(dictNumberValue)
            # sendValue = max([i for i in dictNumberValue.values()])
            #### mesmo que algum parametro seja None, a funcao max() reconhece, e deixa o outro valor maior
            sendId = max(self.number, propNumber)
            sendValue = max(self.value, propValue)
            self.server.send_final_response(sendId, sendValue)

    def propToString(self):
        return "Proposer Id: " + str(self.number) + ", Proposer Value: "+str(self.value)+", Proposer Server Name: "+ str(self.server.getName())
