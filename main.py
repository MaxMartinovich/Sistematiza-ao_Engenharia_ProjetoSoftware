import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox, QLabel
from PySide6.QtGui import QPixmap

class ToDoApp(QWidget):

    def adicionar_tarefa(self):
        texto = self.input_tarefa.text()
        if texto == "":
            QMessageBox.warning(self, "Erro", "Escreva uma tarefa primeiro!!")
        else:
            self.lista_tarefa.addItem(texto)
            self.input_tarefa.clear()

    def completar_tarefa(self):
        item = self.lista_tarefa.currentItem()
        if item:
            item.setText(item.text() + " ☑️")
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma tarefa selecionada")

    def deletar_tarefa(self):
        item = self.lista_tarefa.currentItem()
        if item:
            self.lista_tarefa.takeItem(self.lista_tarefa.row(item))
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma tarefa selecionada")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")

        # Layout principal
        main_layout = QHBoxLayout()

        # LADO ESQUERDO (tarefas)
        left_layout = QVBoxLayout()

        self.input_tarefa = QLineEdit()
        left_layout.addWidget(self.input_tarefa)

        self.btn_add = QPushButton("Adicionar")
        self.btn_add.clicked.connect(self.adicionar_tarefa)
        left_layout.addWidget(self.btn_add)

        self.lista_tarefa = QListWidget()
        left_layout.addWidget(self.lista_tarefa)

        self.btn_concluir = QPushButton("Concluir")
        self.btn_concluir.clicked.connect(self.completar_tarefa)
        left_layout.addWidget(self.btn_concluir)

        self.btn_excluir = QPushButton("Excluir")
        self.btn_excluir.clicked.connect(self.deletar_tarefa)
        left_layout.addWidget(self.btn_excluir)

        # LADO DIREITO (imagem)
        right_layout = QVBoxLayout()
        self.label_img = QLabel()
        pixmap = QPixmap("frase.png")
        self.label_img.setPixmap(pixmap.scaled(175, 175))
        right_layout.addWidget(self.label_img)

        # Montando os dois lados
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ToDoApp()
    janela.show()
    app.exec()