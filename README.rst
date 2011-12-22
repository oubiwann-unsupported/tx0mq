A Twisted Library for ZeroMQ
============================

Note that though initially based on the work in txZMQ, this project is almost a
complete rewrite.

tx0mq allows to integrate easily `ZeroMQ <http://zeromq.org>`_ sockets into
Twisted event loop (reactor).

Supports CPython and PyPy.

Requirements:

* ZeroMQ library >= 2.1 (heavily tested with 2.1.4)

Python packages required:

* pyzmq (for CPython)
* pyzmq-ctypes (for PyPy)
* Twisted

tx0mq introduces support for general ZeroMQ sockets by class ``ZmqConnection``
that can do basic event loop integration, sending-receiving messages in
non-blocking manner, scatter-gather for multipart messages.

Special descendants of that class, ``ZmqPubConnection`` and ``ZmqSubConnection``
add special nice features for PUB/SUB sockets.

Request/reply pattern is achieved via XREQ/XREP sockets and classes ``ZmqXREQConnection``, 
``ZmqXREPConection`` (by verterok).

Other socket types could be easily derived from ``ZmqConnection``.

Examples
--------

We are slowly adding tx0mq versions of all the Python examples in the zguide.
They are available for your viewing pleasure in the examples directory.

Hacking
-------

Source code for tx0mq is available at `github <https://github.com/oubiwann/tx0mq>`_,
forks and pull requests are welcome.
