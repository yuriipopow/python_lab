class PrinterQueue:
    def __init__(self):
        self.queue = []

    def add_document(self, document: str):
        self.queue.append(document)

    def print_document(self):
        if self.queue:
            document = self.queue.pop(0)
            print(f"Printing: {document}")

    def queue_size(self):
        return len(self.queue)