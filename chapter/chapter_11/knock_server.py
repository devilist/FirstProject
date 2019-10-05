from twisted.internet import protocol, reactor


class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print('Client:', data)
        if data.startsWith("Knock knock"):
            response = "who is  there?"
        else:
            response = data + " who?"
        print('Server:', response)
        self.transport.write(response)


class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()


reactor.listenTCP(8000, KnockFactory())
reactor.run()
