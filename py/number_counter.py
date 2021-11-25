import PySimpleGUI as sg

number = 0
layout = [ [sg.Text(number, font=("Helvetica", 18, 'bold')), sg.Button("Plus"), sg.Button("Minus")] ]
window = sg.Window('Counter', layout)

while True:
    event, values = window.Read()
    if event in ('Exit', None): break
    if event == "Plus": number+=1
    if event == "Minus": number-=1
    window.Close()
    layout = [ [sg.Text(number, font=("Helvetica", 18, 'bold')), sg.Button("Plus"), sg.Button("Minus")] ]
    window = sg.Window('Counter', layout)