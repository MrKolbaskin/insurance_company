import PySimpleGUI as sg

from interface.demands import create_demand_form

SIZE_TEXT = (30, None)
SIZE_FONT = ('default', 12)

INPUT_FONT = ('default', 12)
IS_VISIBLE = False
SIZE_INPUT = (89, None)
INPUT_EVENTS = True

edit_fields = [
    [sg.Text('Общие параметры', font=('default', 15), justification='left')],
    [
        sg.Text('Продолжительность новых условий в месяцах (1-24)', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='duration', default_text='12', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только число', font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', size=SIZE_INPUT, key='duration.num')],
        [sg.Text('Значение >= 1 и <= 24', font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', size=SIZE_INPUT, key='duration.seq')]])
    ],
    [
        sg.Text('Налоговый процент (0-100)', size=SIZE_TEXT, font=SIZE_FONT),
        sg.Column([
        [sg.InputText(key='tax', default_text='5', font=INPUT_FONT, size=SIZE_INPUT, enable_events=INPUT_EVENTS)],
        [sg.Text('Только число', font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', size=SIZE_INPUT, key='tax.num')],
        [sg.Text('Значение >= 0 и <= 100', font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', size=SIZE_INPUT, key='tax.seq')]])
    ],
    [create_demand_form('AutoContract'),
    create_demand_form('HouseContract'),
    create_demand_form('LifeContract')]
]

layout_edit = [
    [sg.Column(edit_fields)],
    [sg.Button('Продолжить', key='Продолжить')]
]