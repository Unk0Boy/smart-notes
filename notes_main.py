from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
QListWidget, QPushButton, QLineEdit, QTextEdit, QVBoxLayout,
QHBoxLayout)

app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle("Умные заметки")

notes_win.resize(300, 300)

list_notes = QListWidget()
list_notes_label = QLabel("Список заметок")
button_note_create = QPushButton("Создать заметку")
button_note_del =  QPushButton("Удалить заметку")
button_note_save = QPushButton("Сохранитьт заметку")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введите тег...")
field_text = QTextEdit() # создаём объект поля для заметок

button_tag_add = QPushButton("Добавить к заметтке")
button_tag_del = QPushButton("Открепить от заметке")
button_tag_search = QPushButton("Искать заметку по тегу")

list_tags = QListWidget()
list_tags_lable = QLabel("Список тегов") # Создание объекта надписи


# расположение веджетов по лайаутам >>>

layout_notes = QHBoxLayout()

col_1 = QVBoxLayout() # создание направляющей линии
col_1.addWidget(field_text) # добавляем виджет на лойаулт

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

# добавление одного лайаута на другой
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_lable)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2 ) #добавляем линию на главный лайаут и растягиваем её в ширину
layout_notes.addLayout(col_2, stretch = 1)

notes_win.setLayout((layout_notes)) # добавление главного лайаута на объект окна



notes_win.show()
app.exec()



