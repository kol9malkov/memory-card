#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel,
    QButtonGroup
)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Какая функция используется для ввода информации в Python?', 'input()', 'print()', 'str()', 'int()'))
question_list.append(Question('Вопрос 2', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
question_list.append(Question('Вопрос 3', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
question_list.append(Question('Вопрос 4', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
question_list.append(Question('Вопрос 5', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))


app = QApplication([])
window = QWidget()

window.setWindowTitle('Memory Card')
window.resize(400, 400)

''' Интерфейс '''
question = QLabel('Какая функция используется для ввода информации в Python?')
btn_ok = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('input()')
rbtn_2 = QRadioButton('print()')
rbtn_3 = QRadioButton('str()')
rbtn_4 = QRadioButton('int()')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Панель результатов
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

''' Размещение виджетов '''
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)

''' Функции '''
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q : Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')


def next_question():
    cur_question = randint(0, len(question_list)-1)
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_ok.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
''' Показ окна и закрытие на крестик '''
window.show()
app.exec_()