
import random

class PacketIDGenerator:
    def __init__(self):
        self.packet_id = 0

    def generate_packet_id(self):
        self.packet_id = random.randint(1, 1000)
        return self.packet_id

# Create an instance of PacketIDGenerator
packet_id_generator = PacketIDGenerator()

# Generate a packet ID
print("Generated Packet ID:", packet_id_generator.generate_packet_id())
