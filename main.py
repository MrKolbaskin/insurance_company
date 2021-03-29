import PySimpleGUI as sg

from interface.demands import create_demand_form
from interface.state_company import state_company, current_demands
from interface.contracts import contracts

from resources.parse_info import parse_begin_info
from resources.validation import validation

from classes.modelClass import Model

COMPANY_INFO = '-COMPANY_INFO-'
LOGS = '-LOGS-'
CONTRACTS_INFO = '-CONTRACTS_INFO-'
CONTRACTS = '-CONTRACTS-'
CURRENT_DEMAND = '-CURRENT_DEMAND-'

SIZE_TEXT = (30, None)
SIZE_FONT = ('default', 12)

INPUT_FONT = ('default', 12)
IS_VISIBLE = False
SIZE_INPUT = (89, None)
INPUT_EVENTS = True

SUBMIT = '-SUBMIT-'

buttons = [
    [
        sg.Button('Следующий месяц', button_color=('black', 'green'), size=(16, 1), font=('default', 13)),
        sg.Button('Симуляция', size=(16, 1), font=('default', 13), button_color=('black', 'orange'))
    ],
    [
        sg.Button('Начать заново', button_color=('black', 'yellow'), size=(16, 1), font=('default', 13)), 
        sg.Button('Изменить условия', size=(16, 1), button_color=('black', 'blue'), font=('default', 13))
    ]
]

begin_fields = [
    [sg.Text('Общие параметры', font=('default', 15), justification='left')],
    [
        sg.Text('Продолжительность эксперимента', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='m', default_text='24', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только целое число', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='m.num')],
        [sg.Text('Значение >= 6 и <= 24', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='m.seq')]])
    ],
    [
        sg.Text('Продолжительность начальных условий', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='duration', default_text='12', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только целое число', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='duration.num')],
        [sg.Text('Значение >= 1', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='duration.seq')]])
    ],
    [
        sg.Text('Налоговый процент', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='tax', default_text='5', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только целое число', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='tax.num')],
        [sg.Text('Значение >= 0 и <= 100', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='tax.seq')]])
    ],
    [
        sg.Text('Начальный капитал в у.е.', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='capital', default_text='100000', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только целое число', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='capital.num')],
        [sg.Text('Значение >= 0', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='capital.seq')]])
    ],
    [create_demand_form('AutoContract'),
    create_demand_form('HouseContract'),
    create_demand_form('LifeContract')]
]

edit_fields = [
    [sg.Text('Общие параметры', font=('default', 15), justification='left')],
    [
        sg.Text('Продолжительность новых условий', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='duration', default_text='12', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только число', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='duration.num')],
        [sg.Text('Значение >= 1', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='duration.seq')]])
    ],
    [
        sg.Text('Налоговый процент', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='tax', default_text='5', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только число', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='tax.num')],
        [sg.Text('Значение >= 0 и <= 100', font=INPUT_FONT, visible=IS_VISIBLE, background_color='red', size=SIZE_INPUT, key='tax.seq')]])
    ],
    [create_demand_form('AutoContract'),
    create_demand_form('HouseContract'),
    create_demand_form('LifeContract')]
]

#sg.Column(life_layout), sg.Column(house_layout)
layout_begin = [
    [sg.Column(begin_fields)],
    [sg.Button('Начать', button_color=('black', 'green'), key='Начать')]
]

layout_edit = [
    [sg.Column(edit_fields)],
    [sg.Button('Продолжить', key='Продолжить')]
]

headers_contracts = ['Тип контракта', "Продолжительность контракта", "Максимальная сумма возмещенения", "Размер взноса", "Коэф-ты повреждения по страховым случаям"]
test_values_contracts = [[ind, ind * 100, ind * 10] for ind in range(1, 50)]

headers_events = ['Коэфиц-т повреждения']
test_values_events = [[ind] for ind in range(1, 50)]

headers_actions = ['Последние действия']
last_actions = [[f"Действие {value}"] for value in test_values_events]

headers_cond_contracts = ['Тип контракта', "Продолж-ть контракта", "Макс. сумма возмещенения", "Размер взноса"]

layout_main = [
    [
        sg.Table(contracts(), headings=headers_cond_contracts, font=('default', 15), size=(None, 5), max_col_width=15, justification='center', key=CONTRACTS_INFO), #sg.Text('Условия страховых договоров', background_color='white', text_color='black', size=(25, 5), font=('default', 20), justification='center'),
        sg.Table(last_actions, headings=headers_actions, font=('default', 15), size=(20, 5), auto_size_columns=False, def_col_width=52, max_col_width=30, justification='center', key=LOGS)
    ],
    [
        sg.Text('', text_color='white', size=(37, 6), font=('default', 15), justification='left', key=COMPANY_INFO),
        sg.Text('', text_color='white', size=(30, 6), font=('default', 15), justification='left', key=CURRENT_DEMAND),
        #sg.Image('/Users/vdubinin/Desktop/msu/insurance_company/logo.png', pad=((100, 0), None), size=(100, 100)), #, background_color='white'
        sg.Column(buttons, pad=((75, 0), None)),
        sg.Column([[sg.Button('Выход', size=(16, 1), button_color=('black', 'red'), font=('default', 13))]])#, element_justification='center', relief='flat')
    ],
    [
        sg.Table([["", "", "", "", ""]], headings=headers_contracts, font=('default', 15), max_col_width=15, justification='center', key=CONTRACTS) #sg.Text('Действующие страховые договора', background_color='white', text_color='black', size=(25, 5), font=('default', 20), justification='center')
        #sg.Table(test_values_events, headings=headers_events, font=('default', 15), justification='center', max_col_width=15) #sg.Text('Страховые случаи за месяц', background_color='white', text_color='black', size=(25, 5), font=('default', 20), justification='center')
    ]
]

window_begin = sg.Window('Insurance Company - Начальные условия', layout_begin, resizable=False, finalize=True)
window_edit = None
window_main = None

window = window_begin
is_begin = True
is_edit = False

#window.hide()
#window_edit.hide()
#window_main.hide()

while True:# The Event Loop
    window.un_hide()
    event, values = window.read()
    #print(event)
    if is_begin or is_edit:
        validation_log = validation(values)
        if not validation_log:
            for key in values:
                window[f'{key}.num'].update(visible=False)
                window[f'{key}.seq'].update(visible=False)
            if is_begin:
                window['Начать'].update(disabled=False)
            elif is_edit:
                window['Продолжить'].update(disabled=False)
        else:
            for key in validation_log:
                window[key].update(visible=True)
            if is_begin:
                window['Начать'].update(disabled=True)
            elif is_edit:
                window['Продолжить'].update(disabled=True)
    #print(values)
    if event == 'OK':
        window.close()
        window = window_main
    if event == 'Начать':
        is_begin = False
        begin_values = parse_begin_info(values)
        model = Model(**begin_values)
        model.start()
        #print(model.get_contracts())
        window.hide()
        if not window_main:
            window_main = sg.Window('Insurance Company - Моделирование', layout_main, resizable=False, finalize=True)
        window_main[LOGS].update(model.logs)
        window_main[COMPANY_INFO].update(state_company(model.company, model.cur_month, model.current_demand))
        window_main[CURRENT_DEMAND].update(current_demands(model.current_demand))
        window_main[CONTRACTS_INFO].update(model.get_contracts_info())
        window_main[CONTRACTS].update(model.get_contracts())
        window = window_main
    if event == 'Следующий месяц':
        mes = model.tick()
        if mes:
            window.hide()
            window = sg.Window('Insurance Company', [
                [sg.Text(mes, text_color='white', size=(20, 1), font=('default', 30), justification='center')],
                [sg.Button('OK', font=('default', 15))]
            ], resizable=False, finalize=True)
            continue
        #print(model.json())
        window_main[LOGS].update(model.logs)
        window_main[COMPANY_INFO].update(state_company(model.company, model.cur_month, model.current_demand))
        window_main[CURRENT_DEMAND].update(current_demands(model.current_demand))
        window_main[CONTRACTS_INFO].update(model.get_contracts_info())
        window_main[CONTRACTS].update(model.get_contracts())
    if event == 'Продолжить':
        is_edit = False
        window.hide()
        new_values = parse_begin_info(values)
        model.update(**new_values)
        window_main[LOGS].update(model.logs)
        window_main[COMPANY_INFO].update(state_company(model.company, model.cur_month, model.current_demand))
        window_main[CURRENT_DEMAND].update(current_demands(model.current_demand))
        window_main[CONTRACTS_INFO].update(model.get_contracts_info())
        window_main[CONTRACTS].update(model.get_contracts())
        window = window_main
    if event == 'Симуляция':
        mes = model.simulation()
        if mes:
            window.hide()
            window = sg.Window('Insurance Company', [
                [sg.Text(mes, text_color='white', size=(20, 1), font=('default', 30), justification='center', key=COMPANY_INFO)],
                [sg.Button('OK', font=('default', 15))]
            ], resizable=False, finalize=True)
        window_main[LOGS].update(model.logs)
        window_main[COMPANY_INFO].update(state_company(model.company, model.cur_month, model.current_demand))
        window_main[CURRENT_DEMAND].update(current_demands(model.current_demand))
        window_main[CONTRACTS_INFO].update(model.get_contracts_info())
        window_main[CONTRACTS].update(model.get_contracts())
    if event == 'Изменить условия':
        is_edit = True
        window.hide()
        if not window_edit:
            window_edit = sg.Window('Insurance Company - Изменение условий', layout_edit, resizable=False, finalize=True)
        window = window_edit
    if event == 'Начать заново':
        is_begin = True
        window.hide()
        window = window_begin
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel', 'Выход'):
        break
#