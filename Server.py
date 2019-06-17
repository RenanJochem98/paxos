from random import randint
class Server(object):

    def __init__(self):
        self.name = "Server"
        self.proposers = []
        self.acceptors = []
        self.learners = []
        self.quantProposers = 0;
        self.quantAcceptors = 0
        self.ids_usados = []
        self.temp_store = {} # guarda temporariamente proposers para nao executar tudo sequencial

    #apenas para testes
    def getName(self):
        return self.name
    def showAllProposers(self):
        print("     ----- Todos os PROPOSERS Adicionados -----")
        for p in self.proposers:
            print(p.propToString())
        print("")

    def showAllAcceptors(self):
        print("     ----- Todos os ACCEPTORS Adicionados -----")
        for a in self.acceptors:
            print(a.acceptToString())
        print("")

    # para organizacao
    def getQuantProposers(self):
        return self.quantProposers

    def getQuantAcceptors(self):
        return self.quantAcceptors

    def addProposer(self, proposer):
        proposer.server = self
        proposer.setId(self.getUniqueId())
        self.proposers.append(proposer)
        self.quantProposers += 1

    def addAcceptor(self, acceptor):
        acceptor.server = self
        self.acceptors.append(acceptor)
        self.quantAcceptors += 1

    def getUniqueProposer(self, propNumber):
        for p in self.proposers:
            if propNumber == p.getId():
                return p
        return None

    def start(self):
        for p in self.proposers:
            p.prepare_request()

    # para execucao
    def getUniqueId(self):
        id = -1
        tem_id = False
        while not tem_id:
            id = randint(1,1000)
            if id not in self.ids_usados:
                self.ids_usados.append(id)
                tem_id = True
        return id

    def send_prepare_request(self, propId, propValue):
        # self.temp_store[propId] = propValue
        # if(len(self.temp_store)) == self.quantProposers:
        # for key in self.temp_store:
        for a in self.acceptors:
            # print("Enviando valor de Proposer "+str(propId)+ " para Acceptor "+str(a.getId()))
                a.prepare_response(propId, propValue, self.quantProposers)
        # self.temp_store.clear()
        # else:
        #     print("Proposer "+str(propId)+" barrado no send_prepare_request()")
        # print("")
        # self.showAllProposers()
    def prop_accept_request(self, propNumber, propValue):
        prop = self.getUniqueProposer(propNumber)
        if prop is not None:
            prop.accept_request(propNumber, propValue)

    def send_final_response(self, greaterPropId, greaterPropValue):
        # self.temp_store.append(greaterPropId)
        # if(len(self.temp_store)) == self.quantProposers:
        #     del self.temp_store[:]
        for a in self.acceptors:
            a.accepted(greaterPropId, greaterPropValue)
        # else:
        #     print("Proposer "+str(greaterPropId)+" barrado no send_final_response()")
        #     print("")

    def send_value_to_learners(self, value, acceptorId, propId):
        print("****************************************************")
        print("Valor aceito em Paxos: "+str(value)+", enviado pelo Acceptor: "+str(acceptorId)+" e gerado pelo Proposer: "+str(propId))
        print("")
