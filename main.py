from holder import Holder
import PySimpleGUIQt as sg
import yaml
import multiprocessing

sg.theme('Dark2')
layout = [[sg.Text('HolderMC - your crossbow user')],
          [sg.Text('Delay (in seconds):'), sg.InputText()],
          [sg.Button('Run'), sg.Button('Stop')]]
window = sg.Window('HolderMC', layout, no_titlebar=False, alpha_channel=.7, grab_anywhere=True, keep_on_top=True,
                   icon="C:/Users/k0/Desktop/Programowanie/AHK/Projekty/MakroKit/icons8-cursor-48.ico")

if __name__ == "__main__":
    try:
        with open('options.yml') as f:
            options = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        with open('options.yml', 'w') as f:
            yaml.dump({
                'delay': 10,
                'draw_time': 0.9
            }, f)
        with open('options.yml') as f:
            options = yaml.load(f, Loader=yaml.FullLoader)
    while True:
        event, values = window.Read(close=False)
        if event == sg.WINDOW_CLOSED:
            try:
                crossbow.terminate()
            except NameError:
                pass
            break
        if event == 'Run':
            if values[0] != '':
                try:
                    options['delay'] = float(values[0])
                except ValueError:
                    sg.Popup('Input error', f'Please input a float, your input is {values[0]}', keep_on_top=True)
                with open('options.yml', 'w') as f:
                    yaml.dump(options, f)
            crossbow = multiprocessing.Process(target=Holder, args=(options,))
            crossbow.start()
        if event == 'Stop':
            try:
                crossbow.terminate()
            except NameError:
                pass


window.close()
