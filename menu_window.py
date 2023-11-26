from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)

menu_window = QWidget()

lb_question = QLabel("Введіть питання")
le_question = QLineEdit()

lb_answer = QLabel("Введіть правильну відповідь")
le_answer = QLineEdit()

lb_wrong1 = QLabel("Введіть неправильний варіант 1")
le_wrong1 = QLineEdit()

lb_wrong2 = QLabel("Введіть неправильний варіант 2")
le_wrong2 = QLineEdit()

lb_wrong3 = QLabel("Введіть неправильний варіант 3")
le_wrong3 = QLineEdit()

Button_Dodatu = QPushButton("Додати питання")
Button_clear = QPushButton("Очистити текст")
Button_nazad = QPushButton("Назад")

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_v_line = QVBoxLayout()

menu_h_line_1.addWidget(lb_question)
menu_h_line_1.addWidget(le_question)

menu_h_line_2.addWidget(lb_answer)
menu_h_line_2.addWidget(le_answer)

menu_h_line_3.addWidget(lb_wrong1)
menu_h_line_3.addWidget(le_wrong1)

menu_h_line_4.addWidget(lb_wrong2)
menu_h_line_4.addWidget(le_wrong2)

menu_h_line_5.addWidget(lb_wrong3)
menu_h_line_5.addWidget(le_wrong3)

menu_h_line_6.addWidget(Button_Dodatu)
menu_h_line_6.addWidget(Button_clear)

menu_v_line.addLayout(menu_h_line_1)
menu_v_line.addLayout(menu_h_line_2)
menu_v_line.addLayout(menu_h_line_3)
menu_v_line.addLayout(menu_h_line_4)
menu_v_line.addLayout(menu_h_line_5)
menu_v_line.addLayout(menu_h_line_6)

menu_v_line.addWidget(Button_nazad)

menu_window.setLayout(menu_v_line)
