import PySimpleGUI as sg

SIZE_FONT = ('default', 12)
INPUT_FONT = ('default', 12)

INPUT_SIZE = (15, None)
VAL_MES = 'Только целое число'

IS_VISIBLE = False
INPUT_EVENTS = True

def create_demand_form(name):
    return sg.Column([
    [sg.Text(name, font=('default', 15),  justification='left')],
    [sg.Text('Максимальная сумма выплаты в у.е. (>= 1)', size=(20, None), font=SIZE_FONT),
    sg.Column([
        [sg.InputText(size=INPUT_SIZE, key=f'{name}.max_sum', default_text='10000', font=INPUT_FONT, enable_events=INPUT_EVENTS)],
        [sg.Text(VAL_MES, size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.max_sum.num')],
        [sg.Text('Значение >= 1', size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.max_sum.seq')]])
    ],
    [sg.Text('Продолжительность контракта в месяцах (>= 1)', size=(20, None), font=SIZE_FONT),
    sg.Column([
        [sg.InputText(size=INPUT_SIZE, key=f'{name}.duration', default_text='12', font=INPUT_FONT, enable_events=INPUT_EVENTS)],
        [sg.Text(VAL_MES, size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.duration.num')],
        [sg.Text('Значение >= 1', size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.duration.seq')]])
    ],
    [sg.Text('Сумма взноса в у.е. (>= 1)', size=(20, None), font=SIZE_FONT),
    sg.Column([
        [sg.InputText(size=INPUT_SIZE, key=f'{name}.contribution_value', default_text='5000', font=INPUT_FONT, enable_events=INPUT_EVENTS)],
        [sg.Text(VAL_MES, size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.contribution_value.num')],
        [sg.Text('Значение >= 1', size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.contribution_value.seq')]])
    ],
    [sg.Text('Максимальное кол-во страховых случаев в месяц (>= 1)', size=(20, None), font=SIZE_FONT),
    sg.Column([
        [sg.InputText(size=INPUT_SIZE, key=f'{name}.max_events', default_text='3', font=INPUT_FONT, enable_events=INPUT_EVENTS)],
        [sg.Text(VAL_MES, size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.max_events.num')],
        [sg.Text('Значение >= 1', size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.max_events.seq')]])
    ],
    [sg.Text('Текущий спрос, случайная величина (>= 1)', size=(20, None), font=SIZE_FONT),
    sg.Column([
        [sg.InputText(size=INPUT_SIZE, key=f'{name}.random_count', default_text='10', font=INPUT_FONT, enable_events=INPUT_EVENTS)],
        [sg.Text(VAL_MES, size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.random_count.num')],
        [sg.Text('Значение >= 1', size=INPUT_SIZE, font=INPUT_FONT, visible=IS_VISIBLE, text_color='#960101', background_color='#FF9696', key=f'{name}.random_count.seq')]])
    ]
    ],
    justification='left',
    key=name)