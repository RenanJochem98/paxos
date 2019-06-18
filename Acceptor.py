class Acceptor(object):
    def __init__(self, id):
        self.id = id
        self.minimumNumber = 0
        self.highestValue = 0
        self.propInfos = {}
        self.server = None

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def prepare_response(self, propNumber, propValue, quantTotalProposers):
        # print("Acceptor "+str(self.id)+" recebeu valor "+ str(propValue) +" do proposer "+ str(propNumber))
        # tentar garantir que cheguem todos os valores de proposers antes de prosseguir
        if self.server is not None:
            if not self.propInfos:
                # print("Recebeu id "+str(propNumber)+" e valor "+str(propValue)+ " sem outros valores")
                self.server.prop_accept_request(propNumber, propValue)
                self.minimumNumber = propNumber
            else:
                if propNumber > self.minimumNumber:
                    self.server.prop_accept_request(propNumber, propValue)
                    # self.server.prop_accept_request(self.minimumNumber, self.highestValue)
                    # print("Recebeu id "+str(propNumber)+" e valor "+str(propValue)+ " com outros valores")
                    # print("Recebeu id "+str(self.minimumNumber)+" e valor "+str(self.highestValue)+ " com outros valores")
                    self.minimumNumber = propNumber
                # else:
                #     print("Igonorou id "+str(propNumber)+" e valor "+str(propValue)+ " com outros valores")

            if propValue > self.highestValue:
                self.highestValue = propValue

            self.propInfos[propNumber] = propValue
            # print("")
    def accepted(self, propId, value):
        self.server.send_value_to_learners(value, self.id, propId)

    def acceptToString(self):
        return "Acceptor Id: " + str(self.id) + ", Acceptor Server Name: "+ str(self.server.getName())
