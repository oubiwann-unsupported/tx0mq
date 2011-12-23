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
