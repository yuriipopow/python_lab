class Warehouse:
    def __init__(self):
        self.box_stack = []  # Стек для коробок

    def add_box(self, box: str):
        """Додає коробку до стеку"""
        self.box_stack.append(box)
        print(f"Added box: {box}")

    def remove_box(self):
        """Видаляє верхню коробку зі стеку"""
        if self.box_stack:
            removed_box = self.box_stack.pop()
            print(f"Removed box: {removed_box}")
        else:
            print("No boxes left in the warehouse.")

    def peek_box(self):
        """Повертає верхню коробку без видалення"""
        if self.box_stack:
            print(f"Top box: {self.box_stack[-1]}")
        else:
            print("No boxes in the warehouse.")

    def display_boxes(self):
        """Відображає всі коробки у стеку"""
        if self.box_stack:
            print("Boxes in warehouse:", self.box_stack)
        else:
            print("The warehouse is empty.")

class ClinicQueue:
    def __init__(self):
        self.queue = []  # Черга пацієнтів

    def add_patient(self, name: str, is_urgent: bool):
        """Додає пацієнта до черги. Ургентні пацієнти йдуть на початок."""
        if is_urgent:
            self.queue.insert(0, name)  # Додаємо ургентного пацієнта на початок
            print(f"Urgent patient added: {name}")
        else:
            self.queue.append(name)  # Додаємо звичайного пацієнта в кінець
            print(f"Regular patient added: {name}")

    def process_patient(self):
        """Обробляє пацієнта з черги"""
        if self.queue:
            patient = self.queue.pop(0)  # Видаляємо першого пацієнта
            print(f"Processing patient: {patient}")
        else:
            print("No patients in the queue.")

    def display_queue(self):
        """Відображає чергу пацієнтів"""
        if self.queue:
            print("Current queue:", self.queue)
        else:
            print("The queue is empty.")




if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.add_box("Box 1")
    warehouse.add_box("Box 2")
    warehouse.peek_box()  # Top box: Box 2
    warehouse.remove_box()  # Removed box: Box 2
    warehouse.display_boxes()  # Boxes in warehouse: ['Box 1']

    clinic = ClinicQueue()
    clinic.add_patient("John Doe", is_urgent=False)
    clinic.add_patient("Jane Smith", is_urgent=True)
    clinic.add_patient("Alice Johnson", is_urgent=False)
    clinic.display_queue()  # Current queue: ['Jane Smith', 'John Doe', 'Alice Johnson']
    clinic.process_patient()  # Processing patient: Jane Smith
    clinic.display_queue()  # Current queue: ['John Doe', 'Alice Johnson']