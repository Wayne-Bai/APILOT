from werkzeug import StreamReceiver

class LineReceiver(StreamReceiver):
    def __init__(self, output):
        self.output = output

    def receive(self, data):
        if data:
            self.output.write(data)
            self.output.flush()

# Usage
with open('input.txt', 'r') as f:
    with LineReceiver(f) as receiver:
        for line in receiver:
            print(line.strip())
