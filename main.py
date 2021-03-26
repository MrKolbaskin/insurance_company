import PySimpleGUI as sg

from interface.demands import create_demand_form
from interface.state_company import state_company
from interface.contracts import contracts

buttons = [
    [
        sg.Button('Следующий месяц', button_color=('black', 'green'), size=(16, 1), font=('default', 13)),
        sg.Button('Закончить', size=(16, 1), font=('default', 13), button_color=('black', 'red'))
    ],
    [
        sg.Button('Начать заново', button_color=('black', 'yellow'), size=(16, 1), font=('default', 13)), 
        sg.Button('Изменить условия', size=(16, 1), button_color=('black', 'blue'), font=('default', 13))
    ]
]

begin_fields = [
    [sg.Text('Начальные условия', font=('default', 15), justification='left')],
    [sg.Text('Продолжительность эксперимента', size=(20, None)), sg.InputText()],
    [sg.Text('Продолжительность начальных условий', size=(20, None)), sg.InputText()],
    [sg.Text('Налоговый процент', size=(20, None)), sg.InputText()],
    [sg.Text('Капитал', size=(20, None)), sg.InputText()],
    [create_demand_form('AutoContract'),
    create_demand_form('HouseContract'),
    create_demand_form('LifeContract')]
]

edit_fields = [
    [sg.Text('Текущие условия', font=('default', 15), justification='left')],
    [sg.Text('Продолжительность эксперимента', size=(20, None)), sg.InputText()],
    [sg.Text('Продолжительность начальных условий', size=(20, None)), sg.InputText()],
    [sg.Text('Налоговый процент', size=(20, None)), sg.InputText()],
    [sg.Text('Капитал', size=(20, None)), sg.InputText()],
    [create_demand_form('AutoContract'),
    create_demand_form('HouseContract'),
    create_demand_form('LifeContract')]
]

#sg.Column(life_layout), sg.Column(house_layout)
layout_begin = [
    [sg.Column(begin_fields)],
    [sg.Button('Начать', button_color=('black', 'green'))]
]

layout_edit = [
    [sg.Column(edit_fields)],
    [sg.Button('Продолжить')]
]

headers_contracts = ["Продолж-ть контракта", "Макс. сумма возмещенения", "Размер взноса"]
test_values_contracts = [[ind, ind * 100, ind * 10] for ind in range(1, 50)]

headers_events = ['Коэфиц-т повреждения']
test_values_events = [[ind] for ind in range(1, 50)]

headers_actions = ['Последние действия']
last_actions = [[f"Действие {value}"] for value in test_values_events]

headers_cond_contracts = ['Тип контракта', "Продолж-ть контракта", "Макс. сумма возмещенения", "Размер взноса"]

layout_main = [
    [
        sg.Table(contracts(), headings=headers_cond_contracts, font=('default', 15), size=(None, 5), max_col_width=15, justification='center'), #sg.Text('Условия страховых договоров', background_color='white', text_color='black', size=(25, 5), font=('default', 20), justification='center'),
        sg.Table(last_actions, headings=headers_actions, font=('default', 15), size=(None, 5), max_col_width=15, justification='center')
    ],
    [
        sg.Text(state_company(), text_color='white', size=(35, 4), font=('default', 15), justification='left'), #, background_color='white'
        sg.Column(buttons)#, element_justification='center', relief='flat')
    ],
    [
        sg.Table(test_values_contracts, headings=headers_contracts, font=('default', 15), max_col_width=15, justification='center'), #sg.Text('Действующие страховые договора', background_color='white', text_color='black', size=(25, 5), font=('default', 20), justification='center')
        sg.Table(test_values_events, headings=headers_events, font=('default', 15), justification='center', max_col_width=15) #sg.Text('Страховые случаи за месяц', background_color='white', text_color='black', size=(25, 5), font=('default', 20), justification='center')
    ]
]

window_begin = sg.Window('Insurance Company', layout_begin, resizable=False, finalize=True)
window_edit = None
window_main = None

window = window_begin

#window.hide()
#window_edit.hide()
#window_main.hide()

while True:# The Event Loop
    window.un_hide()
    event, values = window.read()
    if event == 'Начать':
        print(values)
        window.hide()
        if not window_main:
            window_main = sg.Window('Insurance Company', layout_main, resizable=False, finalize=True)
        window = window_main
    if event == 'Продолжить':
        window.hide()
        window = window_main
        #window.un_hide()
    if event == 'Изменить условия':
        window.hide()
        if not window_edit:
            window_edit = sg.Window('Insurance Company', layout_edit, resizable=False, finalize=True)
        window = window_edit
    if event == 'Начать заново':
        window.hide()
        window = window_begin
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel', 'Закончить'):
        break
#