A Twisted Library for ZeroMQ
============================

Note that though initially based on the work in txZMQ, this project is almost a
complete rewrite. tx0mq started life as a ``git pull`` from txZMQ, in the event
that they ever wanted to merge it back in, it would be trivial to do so.

tx0mq provides for the easy integration of  `ZeroMQ <http://zeromq.org>`_
sockets into the Twisted event loop (reactor).

Like txZMQ before it, tx0mq Supports CPython and PyPy.

Requirements
------------

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


Architecture
------------

In tx0mq, different considerations need to be made than with standard Twisted
code that use TCP and UDP.  From the zguide [#]_::

 * ØMQ sockets carry messages, rather than bytes (as in TCP) or
   frames (as in UDP). A message is a length-specified blob of
   binary data. We'll come to messages shortly, their design is
   optimized for performance and thus somewhat tricky to
   understand.

 * ØMQ sockets do their I/O in a background thread. This means
   that messages arrive in a local input queue, and are sent
   from a local output queue, no matter what your application
   is busy doing. These are configurable memory queues, by the
   way.

 * ØMQ sockets can, depending on the socket type, be connected
   to (or from, it's the same) many other sockets. Where TCP
   emulates a one-to-one phone call, ØMQ implements one-to-many
   (like a radio broadcast), many-to-many (like a post office),
   many-to-one (like a mail box), and even one-to-one.

 * ØMQ sockets can send to many endpoints (creating a fan-out
   model), or receive from many endpoints (creating a fan-in
   model).


Thoughts on integration with Twisted:
 * `Non-blocking calls and Twisted http://lists.zeromq.org/pipermail/zeromq-dev/2010-April/003163.html`_
 * `Twisted integration, part 2: review http://lists.zeromq.org/pipermail/zeromq-dev/2010-June/003848.html`_
 * `Twisted ZeroMQ Reactor http://lists.zeromq.org/pipermail/zeromq-dev/2010-September/005938.html`_
 * `txZMQ Announcement http://lists.zeromq.org/pipermail/zeromq-dev/2011-April/010880.html`_

Examples
--------

We are slowly adding tx0mq versions of:

1. all the Python examples in the zguide, and
2. the examples that come with the pyzmq source.

They are available for your viewing pleasure in the examples directory.

Hacking
-------

Source code for tx0mq is available at `github <https://github.com/oubiwann/tx0mq>`_,
forks and pull requests are welcome.

Footnotes
---------

.. [#] http://zguide.zeromq.org/page:all#toc22
