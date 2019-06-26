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
        if self.server is not None:
            if not self.propInfos:
                self.server.prop_accept_request(propNumber, propValue)
                self.minimumNumber = propNumber
            else:
                if propNumber > self.minimumNumber:
                    self.server.prop_accept_request(propNumber, self.highestValue)
                    self.minimumNumber = propNumber
                else:
                    self.server.prop_accept_request(propNumber, None)
                    print("Ignorou Proposer "+str(propNumber)+" e valor "+str(propValue)+ " com outros valores")

            if propValue > self.highestValue:
                self.highestValue = propValue

            self.propInfos[propNumber] = propValue

    def accepted(self, propId, value):
        self.server.send_value_to_learners(value, self.id, propId)

    def acceptToString(self):
        return "Acceptor Id: " + str(self.id) + ", Acceptor Server Name: "+ str(self.server.getName())
