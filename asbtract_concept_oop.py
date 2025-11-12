from abc import ABC, abstractmethod
import time

# In this example I implemented a transmitter abstract class to define basics methods to implement
# different kind of live transmission such as satellite and cellular
# I require each class to have connect / start / stop methods.


class Transmitter(ABC):
    @abstractmethod
    def connect(self):
        """Connect to the transmission network (cellular/satellite/etc.)"""
        pass

    @abstractmethod
    def start_stream(self, source):
        """Start sending video stream from the given source"""
        pass

    @abstractmethod
    def stop_stream(self):
        """Stop the current transmission"""
        pass


# Satellite Broadcast
class SatelliteTransmitter(Transmitter):
    def connect(self):
        print("Connecting to satellite link...")
        time.sleep(1)
        print("Satellite link established ✅")

    def start_stream(self, source):
        print(f"Transmitting {source} via satellite uplink...")

    def stop_stream(self):
        print("Shutting down satellite transmission.")


# Cellular broadcast
class CellularTransmitter(Transmitter):
    def connect(self):
        print("Connecting to bonded cellular modems...")
        time.sleep(1)
        print("Cellular connection ready ✅")

    def start_stream(self, source):
        print(f"Streaming {source} over multiple 4G/5G links...")

    def stop_stream(self):
        print("Stopping cellular stream.")


# Implementation
def run_transmission(transmitter: Transmitter):
    transmitter.connect()
    transmitter.start_stream("Camera A")
    time.sleep(2)
    transmitter.stop_stream()


if __name__ == '__main__':

    sat = SatelliteTransmitter()
    cell = CellularTransmitter()

    run_transmission(sat)
    print("—" * 40)
    run_transmission(cell)
