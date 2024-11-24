from printer_queue import PrinterQueue
from text_editor import TextEditor



def main():

    text_editor = TextEditor()
    text_editor.make_change("First Line")
    text_editor.make_change("Second Line")

    print(text_editor.get_text())

    text_editor.undo()
    print(text_editor.get_text())



    printer_queue = PrinterQueue()
    printer_queue.add_document("First Document")
    printer_queue.add_document("Second Document")
    printer_queue.add_document("Third Document")
    printer_queue.print_document()
    printer_queue.print_document()
    printer_queue.add_document("Fourth Document")
    printer_queue.print_document()
    printer_queue.print_document()



if __name__ == "__main__":
    main()