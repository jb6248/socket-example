import struct
import time
import dataclasses
from typing import List


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
    assert unit == p