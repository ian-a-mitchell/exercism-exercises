import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        
        self._reads = 0
        self._writes = 0
        self._read_bytes = 0
        self._write_bytes = 0

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def read(self, size=-1):
        pass

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._reads

    def write(self, b):
        pass

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._writes


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def recv(self, bufsize, flags=0):
        pass

    @property
    def recv_bytes(self):
        pass

    @property
    def recv_ops(self):
        pass

    def send(self, data, flags=0):
        pass

    @property
    def send_bytes(self):
        pass

    @property
    def send_ops(self):
        pass
