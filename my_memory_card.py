from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

questions_list = [Question('Перевод слова "дерево"?','tree', 'three', 'willow', 'derevo'),
                Question('Перевод слова обезьяна','monkey', 'rabbit', 'wolf', 'cat'),
                Question('Перевод слова "яблоко"?','apple', 'apply', 'berry', 'pineapple'),
                Question('какой перс есть в "дота2" ?', 'пудж', 'Т-34', 'утюг', 'Путин'),
                Question('Что из этого не фрукт ?', 'виноград', 'персик', 'банан', 'яблоко'),
                Question('как завут главного героя из смишариков ?', 'там нет главного героя', 'крош', 'ёжик', 'пин'),              
                Question('сколько планет в мире ?', 'дафига', '4', '6', '7'),
                Question('какое национальное блюдо в Белоруси ?', 'драники', 'борщ', 'пельмени', 'плов'),
                Question('сколько весит слон ?', 'много', '6т', '4т', '5т'),
                Question(' вопрос на 1 милион долоров?', 'Путин', 'Т-34', 'утюг', 'пудж')]

app = QApplication([])
window = QWidget()

window.setWindowTitle("Memory Card")
window.resize(400,400)

question = QLabel("Какой национальности не существует?")

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
btn_OK = QPushButton('Ответить')

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

AnsGroupBox = QGroupBox("Результаты теста")
lb_Result = QLabel("верно/неверно")
lb_Correct = QLabel("правильный ответ")

layout_res =QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignTop | Qt.AlignLeft)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layout_line3.addWidget(btn_OK, stretch=2)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)

def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос')

def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Ответить')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()

def show_correct(res):
        lb_Result.setText(res)
        show_result()

def check_answer():
        if answers[0].isChecked():
                show_correct('Верно')
                window.score += 1
                print(f'Статистика:\n-всего вопросов: {window.total}\n правильных ответов: {window.score}')
                print(f'Рейтинг: {window.score/window.total*100}%')
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct('Неверно!')

def next_question():
        window.total += 1
        cur_question = randint(0,len(questions_list)-1)
        print(f'Статистика:\n-всего вопросов: {window.total}\n правильных ответов: {window.score}')
        q = questions_list[cur_question]
        ask(q)

def click_OK():
        if btn_OK.text() == 'Ответить':
                check_answer()
        else:
                next_question()

btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()

window.show()
app.exec()
