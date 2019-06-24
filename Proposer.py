from random import randint
class Proposer(object):
    def __init__(self, number, value):
        # self.number = 0
        self.number = number
        self.acceptors = []
        self.value = value
        # self.value = self.proposal_number()
        self.quantTotalProposers = 0
        self.server = None

    def getNumber(self):
        return self.number

    def setNumber(self, newId):
        self.number = newId

    # def getQuantTotalProposers(self):
    #     return self.quantTotalProposers
    #
    # def setQuantTotalProposers(self, newQuantProposers):
    #     self.quantTotalProposers = newQuantProposers

    # def addAcceptor(self, acceptor_number):
    #     self.acceptors.append(acceptor_number)

    # funcoes obrigatorias
    def proposal_number(self):
        return randint(1,1000)

    def prepare_request(self):
        # print("Prop enviou: N: "+str(self.number)+" V: "+str(self.value))
        self.server.send_prepare_request(self.number, self.value)
        # for a in self.acceptors:
        #     a.prepare_reponse(self.number, self.value, self.quantTotalProposers)

    # def accept_request(self, propNumber, propValue):
    def accept_request(self, dictNumberValue):
        # print(dictNumberValue)
        # print("Proposer: "+str(self.number)+" Recebendo valor de Proposer "+str(propNumber)+ ", com valor "+str(propValue))
        if self.server is not None:
            # if propNumber is None or propValue = 0:
            #     self.server.send_final_response(self.number, self.value)
            # else:

            #### mesmo que algum parametro seja None, a funcao max() reconhece, e deixa o outro valor maior
            sendId = max(dictNumberValue)
            # sendId = max(self.number, propNumber)
            sendValue = max([i for i in dictNumberValue.values()])
            # sendValue = max(self.value, propValue)
            print("Proposer: "+str(self.number)+" envia numero "+str(sendId)+ ", com valor "+str(sendValue))

            self.server.send_final_response(sendId, sendValue)

    def propToString(self):
        return "Proposer Id: " + str(self.number) + ", Proposer Value: "+str(self.value)+", Proposer Server Name: "+ str(self.server.getName())
