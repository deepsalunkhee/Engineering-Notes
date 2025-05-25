import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chat App')
        self.setGeometry(200, 200, 500, 500)

        self.text_input = QTextEdit(self)
        self.text_input.setGeometry(50, 50, 300, 200)

        self.send_button = QPushButton('Send', self)
        self.send_button.setGeometry(370, 50, 80, 30)
        self.send_button.clicked.connect(self.send_message)

        self.message_log = QTextEdit(self)
        self.message_log.setGeometry(50, 100, 400, 300)
        self.message_log.setReadOnly(True)

    def send_message(self):
        message = self.text_input.toPlainText()
        self.text_input.clear()
        self.message_log.append(f'You: {message}')
        self.emit_message(message)

def emit_message(self, message):
    from socketIO_client import SocketIO, BaseNamespace
    with SocketIO('localhost', 5000, BaseNamespace) as socketIO:
        socketIO.emit('message', {'message': message, 'sender': 'You'})


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
