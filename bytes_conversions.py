import struct
import time
import dataclasses
from typing import List

# Here's a short example of how to convert a python class
# into a string of bytes, and back.
# Of course, on the client side (c++) you'll need to find a way
# to emulate `struct.unpack` It should be relatively straightforward
# since the struct packing and unpacking is based on C structs.
# https://docs.python.org/3/library/struct.html

@dataclasses.dataclass
class Point:
    x: float
    y: float
    timestamp: float

# unpack a couple bytes from a stream
def from_bytes(data: bytes) -> Point:
    (x, y, timestamp) = struct.unpack('ddd', data)
    return Point(x, y, timestamp)

def to_bytes(point: Point) -> bytes:
    return struct.pack('ddd', point.x, point.y, point.timestamp)

def test():
    p = Point(123.0243, 0.32412, 0.0)
    bs = to_bytes(p)
    unit = from_bytes(bs)
    print('point: %s'%p)
    print('bytes: %s'%bs)
    print('parsed: %s'%unit)
    assert unit == p # this fails since the precision isn't kept up that well (difference of ~0.0001)