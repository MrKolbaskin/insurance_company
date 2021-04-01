import PySimpleGUI as sg

from interface.demands import create_demand_form
from interface.state_company import state_company, current_demands
from interface.contracts import contracts

from interface.layouts.layout_begin import layout_begin
from interface.layouts.layout_edit import layout_edit
from interface.layouts.layout_main import layout_main

from resources.parse_info import parse_begin_info
from resources.validation import validation

from classes.modelClass import Model

COMPANY_INFO = '-COMPANY_INFO-'
LOGS = '-LOGS-'
CONTRACTS_INFO = '-CONTRACTS_INFO-'
CONTRACTS = '-CONTRACTS-'
CURRENT_DEMAND = '-CURRENT_DEMAND-'

window_begin = sg.Window('Insurance Company - Начальные условия', layout_begin, resizable=False, finalize=True)
window_edit = None
window_main = None

window = window_begin
is_begin = True
is_edit = False

while True:# The Event Loop
    window.un_hide()
    event, values = window.read()
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
    if event == 'OK' or event == "Нет":
        window.close()
        window = window_main
    if event == 'Начать':
        is_begin = False
        begin_values = parse_begin_info(values)
        model = Model(**begin_values)
        model.start()
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
    if event == 'Симуляция до конца':
        window.hide()
        window = sg.Window('Предупреждение', [
                [sg.Text('Вы точно хотите просимулировать\n до конца эскперимента?', text_color='white', size=(25, 2), font=('default', 20), justification='center', key=COMPANY_INFO)],
                [
                    sg.Button('Да', font=('default', 15), button_color=('black', 'green')),
                    sg.Button('Нет', font=('default', 15), button_color=('black', 'red'))
                ]
            ], resizable=False, finalize=True)
    if event == 'Да':
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