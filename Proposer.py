from random import randint
class Proposer(object):
    def __init__(self):
        self.id = 0
        self.acceptors = []
        self.value = self.proposal_number()
        self.quantTotalProposers = 0
        self.server = None

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    # def getQuantTotalProposers(self):
    #     return self.quantTotalProposers
    #
    # def setQuantTotalProposers(self, newQuantProposers):
    #     self.quantTotalProposers = newQuantProposers

    # def addAcceptor(self, acceptor_id):
    #     self.acceptors.append(acceptor_id)

    # funcoes obrigatorias
    def proposal_number(self):
        return randint(1,1000)

    def prepare_request(self):
        self.server.send_prepare_request(self.id, self.value)
        # for a in self.acceptors:
        #     a.prepare_reponse(self.id, self.value, self.quantTotalProposers)

    def accept_request(self, propNumber, propValue):
        if self.server is not None:
            # if propNumber is None or propValue = 0:
            #     self.server.send_final_response(self.id, self.value)
            # else:

            #### mesmo que algum parametro seja None, a funcao max() reconhece, e deixa o outro valor maior
            sendId = max(self.id, propNumber)
            sendValue = max(self.value, propValue)
            self.server.send_final_response(sendId, sendValue)

    def propToString(self):
        return "Proposer Id: " + str(self.id) + ", Proposer Value: "+str(self.value)+", Proposer Server Name: "+ str(self.server.getName())
