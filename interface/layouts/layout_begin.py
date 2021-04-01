import PySimpleGUI as sg

from interface.demands import create_demand_form

SIZE_TEXT = (30, None)
SIZE_FONT = ('default', 12)

INPUT_FONT = ('default', 12)
IS_VISIBLE = False
SIZE_INPUT = (89, None)
INPUT_EVENTS = True

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

layout_begin = [
    [sg.Column(begin_fields)],
    [sg.Button('Начать', button_color=('black', 'green'), key='Начать')]
]