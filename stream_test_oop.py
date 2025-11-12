# Let’s build a realistic automation-style system.
# This mimics how you’d test video devices at LiveU.

from abc import ABC, abstractmethod
import random


# This class is an abstract class of camera structure
class CameraDevice(ABC):
    def __init__(self, ip: str):
        self.ip = ip
        self.connected = False

    @abstractmethod
    def connect(self):
        """Connect camera device"""
        pass

    @abstractmethod
    def capture_frame(self) -> bytes:
        """Return a single frame (simulated)"""
        pass


# Now I will use the CameraDevice abs class to implement 2 different types of cameras

# RTSP - Real Time Streaming Protocol
# So an RTSP camera is a network (IP) camera that streams live video over the network using this protocol
# It’s basically a camera that sends real-time video feed that can be watched, processed,
# or recorded by another device — such as a video encoder, media server, or client app (like VLC or OBS).
class RTSPCamera(CameraDevice):
    def connect(self):
        print(f"[RTSPCamera] Connecting to {self.ip}")
        self.connected = True

    def capture_frame(self) -> bytes:
        if not self.connected:
            raise ConnectionError("Camera not connected")
        frame = bytes(random.getrandbits(8) for _ in range(10))  # generates a frame which is 10 bytes
        print(f"[RTSPCamera] Captured frame: {frame}")
        return frame


class USBWebcam(CameraDevice):
    def connect(self):
        print(f"[USBWebcam] USB device initialized at {self.ip}")
        self.connected = True

    def capture_frame(self) -> bytes:
        frame = bytes([255] * 5)  # Generate a constant 5 bytes frame which every byte is 0xff = 255(10)
        print(f"[USBWebcam] Captured frame: {frame}")
        return frame


# A video codec is a program or device that compresses and
# decompresses video data to make files smaller for storage
# and streaming, and to allow them to be played back
class Encoder:
    def __init__(self, codec: str):
        self.codec = codec

    def encode(self, frame: bytes) -> bytes:
        encoded = f"{self.codec}_encoded = ".encode() + frame
        print(f"[Encoder] Encoded frame: {encoded}")
        return encoded


# I will build now a StreamTester to simulate a simple capture frame and encode.
class StreamTester:
    def __init__(self, camera: CameraDevice, encoder: Encoder):
        self.camera = camera
        self.encoder = encoder
        self.results = []

    def run(self, num_frames=3):
        self.camera.connect()
        for _ in range(num_frames):
            frame = self.camera.capture_frame()
            encoded = self.encoder.encode(frame)
            self.results.append(encoded)
        print(f"[StreamTest] Completed {len(self.results)} frames.")


if __name__ == "__main__":
    cam = RTSPCamera("192.168.1.10")
    enc = Encoder("H264")
    test = StreamTester(cam, enc)
    test.run()
