import PySimpleGUI as sg

def create_demand_form(name):
    return sg.Column([
    [sg.Text(name, font=('default', 12),  justification='left')],
    [sg.Text('Максимальная сумма выплаты', size=(20, None)),
    sg.InputText(size=(10, None), key=f'{name}.max_sum')],
    [sg.Text('Продолжительность контракта', size=(20, None)),
    sg.InputText(size=(10, None), key=f'{name}.duration')],
    [sg.Text('Сумма взноса', size=(20, None)),
    sg.InputText(size=(10, None), key=f'{name}.contribution_value')],
    [sg.Text('Максимальное кол-во страховых случаев в месяц', size=(20, None)),
    sg.InputText(size=(10, None), key=f'{name}.max_events')]
    ],
    justification='left',
    key=name)