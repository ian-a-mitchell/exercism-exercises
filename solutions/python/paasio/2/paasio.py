"""
Module solving the PaaSIO exercise on Exercism. Copied from Madamani's
community solution, so not for sharing. Mostly notable because I was greatly
overthinking it and didn't realize I could just delegate all of the real work
to other objects.
"""

import io

class MeteredFile(io.BufferedRandom):
    """
    Class mock-implementing a file tracking read/write ops and data usage for
    "billing purposes" using a subclassing model.
    """

    def __init__(self, *args, **kwargs):
        """ Constructor method, what's there to say? """
        
        super().__init__(*args, **kwargs)
        
        self._read_ops = 0
        self._write_ops = 0
        self._read_bytes = 0
        self._write_bytes = 0

    def __enter__(self):
        """ Dunder method setting up context management. """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Dunder method needed for context management. Delegates all of the work
        to the superclass method.
        """
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        """ Dunder method to allow iterating over this object. """
        return self

    def __next__(self):
        """
        Dunder method also allowing iteration over this object. Functionally
        very similar to the read method.
        """
        
        data = super().readline()
        self._read_bytes += len(data)
        self._read_ops += 1
        
        if data:
            return data
        raise StopIteration

    def read(self, size=-1):
        """
        Read method which, again, just delegates to the superclass with a small
        amount of tracking data collection for metering.
        """
        
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        
        return data

    @property
    def read_bytes(self):
        """ Getter for _read_bytes. """
        return self._read_bytes

    @property
    def read_ops(self):
        """ Getter for _read_ops. """
        return self._read_ops

    def write(self, input_data):
        """
        Write method. Yet again, delegates to superclass and just collects the
        number of bytes written and the number of ops performed.
        """
        
        write_len = super().write(input_data)
        self._write_bytes += write_len
        self._write_ops += 1
        
        return write_len

    @property
    def write_bytes(self):
        """ Getter for _write_bytes. """
        return self._write_bytes

    @property
    def write_ops(self):
        """ Getter for _write_ops. """
        return self._write_ops


class MeteredSocket:
    """
    Ostensibly a class implementing a "socket" that is metered (tracks
    read/write ops and number of bytes moved) for billing purposes. In fact
    just a thin layer on top of a magic socket object. What can the socket do?
    IDK, it's not made clear.
    """

    def __init__(self, socket):
        """ Constructor method, what's there to say? """
        
        self._socket = socket
        self._recv_ops = 0
        self._recv_bytes = 0
        self._send_ops = 0
        self._send_bytes = 0

    def __enter__(self):
        """ Dunder method setting up context management. """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Dunder method needed for context management. Delegates all of the work
        to the _socket's method.
        """
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        """
        Method calling the socket's "recv" method and updating some of the
        internal data tracking variables.
        """
        
        data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(data)
        self._recv_ops += 1
        
        return data

    @property
    def recv_bytes(self):
        """ Getter for the _recv_bytes variable. """
        return self._recv_bytes

    @property
    def recv_ops(self):
        """ Getter for the _recv_ops variable. """
        return self._recv_ops

    def send(self, data, flags=0):
        """
        Method calling the socket's "send" method and updating some of the
        internal data tracking variables.
        """
        
        send_len = self._socket.send(data, flags)
        self._send_bytes += send_len
        self._send_ops += 1
        
        return send_len

    @property
    def send_bytes(self):
        """ Getter for the _send_bytes variable. """
        return self._send_bytes

    @property
    def send_ops(self):
        """ Getter for the _send_ops variable. """
        return self._send_ops
