class TextEditor:
    def __init__(self):
        self.history = []
        self.current_text = ""

    def make_change(self, new_text: str):
        self.history.append(self.current_text)
        self.current_text = new_text

    def undo(self):
        if self.history:
            self.current_text = self.history.pop()

    def get_text(self):
        return " ".join([*self.history, self.current_text]).strip()