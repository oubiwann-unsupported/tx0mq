"""
How we might expect a tx0mq Twisted client API to look:

    from twisted.python import log
    from tx0mq.client import ZMQClient


    def processResult(result):
        print "Got something back! --> '%s'" % result

    client = ZMQClient("tcp://127.0.0.1:5555")
    deferred = client.send("Hello")
    deferred.addCallback(processResult)
    deferred.addErrback(log)

We could even provide a custom reactor that adds ZeroMQ support. Usage could
like like this:

    from tx0mq import reactor
    from tx0mq.client import ZMQClientFactory

    factory = ZMQClientFactory()

    reactor.connectZMQ("127.0.0.1", 5555, factory)
    reactor.run()

However, there is not just on 0MQ socket... there are a bunch:

    PAIR
    PUB
    SUB
    REQ
    REP
    XREQ
    DEALER
    XREP
    ROUTER
    PULL
    PUSH
    XPUB
    XSUB
    UPSTREAM
    DOWNSTREAM

These are the socket combinations that are valid for a connect-bind pair
(either side can bind):

    PUB and SUB
    REQ and REP
    REQ and ROUTER
    DEALER and REP
    DEALER and ROUTER
    DEALER and DEALER
    ROUTER and ROUTER
    PUSH and PULL
    PAIR and PAIR

As such, we'll need a means of defining which 0MQ socket type to use. Perhaps
something like this (assuming the imports from above):

    from tx0mq import constants

    def processResult(result):
        print "Got something back! --> '%s'" % result

    client = ZMQClient("tcp://127.0.0.1:5555", socketType=constants.SUB)
    deferred = client.send("Hello")
    deferred.addCallback(processResult)
    deferred.addErrback(log)

We could even provide a custom reactor that adds ZeroMQ support. Usage could
like like this (assuming the imports from above):

    from tx0mq import constants

    factory = ZMQClientFactory(socketType=constants.SUB)

    reactor.connectZMQ("127.0.0.1", 5555, factory)
    reactor.run()
"""
#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import zmq

context = zmq.Context()

#  Socket to talk to server
print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    socket.send ("Hello")
    
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
