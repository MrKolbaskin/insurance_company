import PySimpleGUI as sg

from interface.contracts import contracts

COMPANY_INFO = '-COMPANY_INFO-'
LOGS = '-LOGS-'
CONTRACTS_INFO = '-CONTRACTS_INFO-'
CONTRACTS = '-CONTRACTS-'
CURRENT_DEMAND = '-CURRENT_DEMAND-'


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


headers_contracts = ['Тип контракта', "Продолжительность контракта", "Максимальная сумма возмещенения", "Размер взноса", "Коэф-ты повреждения по страховым случаям"]
headers_events = ['Коэфиц-т повреждения']
#headers_actions = ['Последние действия']
headers_cond_contracts = ['Тип контракта', "Продолж-ть контракта", "Макс. сумма возмещенения", "Размер взноса"]

layout_main = [
    [
        sg.Column(
            [
                [sg.Text('Условия контрактов', text_color='white', font=('default', 20))],
                [sg.Table(contracts(), headings=headers_cond_contracts, font=('default', 15), size=(None, 5), max_col_width=15, justification='center', key=CONTRACTS_INFO, hide_vertical_scroll=True)]
            ]
        ),
        sg.Column(
            [
                [sg.Text('Последние действия', text_color='white', font=('default', 20))],
                [sg.Table([[""]], font=('default', 15), size=(20, 5), auto_size_columns=False, def_col_width=52, max_col_width=30, justification='center', key=LOGS)]
            ]
        )
    ],
    [
        sg.Text('', text_color='white', size=(37, 6), font=('default', 15), justification='left', key=COMPANY_INFO),
        sg.Text('', text_color='white', size=(30, 6), font=('default', 15), justification='left', key=CURRENT_DEMAND),
        sg.Column(buttons, pad=((75, 0), None)),
        sg.Column([[sg.Button('Выход', size=(16, 1), button_color=('black', 'red'), font=('default', 13))]])
    ],
    [
        sg.Column(
            [
                [sg.Text('Действующие контракты компании', text_color='white', font=('default', 20))],
                [sg.Table([["", "", "", "", ""]], headings=headers_contracts, font=('default', 15), max_col_width=15, justification='center', key=CONTRACTS)]
            ]
        )
    ]
]