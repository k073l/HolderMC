import time
from ahk import AHK


class Holder:

    def __init__(self, yaml):
        self.ahk = AHK()
        self.options = yaml
        self.delay = self.options['delay']
        self.get_window()

    def get_window(self):
        self.window = self.ahk.find_window(title=b'Minecraft', process='javaw.exe')
        # print(self.window.title)
        self.crossbow()

    def crossbow(self):
        while True:
            # print('Sending RButton down')
            self.ahk.run_script('ControlClick, , ' + self.window.title.decode() + ', ,Right, , NAD')
            time.sleep(float(self.options['draw_time']))
            # print('Sending RButton up')
            self.ahk.run_script('ControlClick, , ' + self.window.title.decode() + ', ,Right, , NAU')
            time.sleep(0.2)
            # print('Sending RButton')
            self.ahk.run_script('ControlClick, , ' + self.window.title.decode() + ', ,Right, , NA')
            # print(f'Waiting for {self.delay}s')
            time.sleep(float(self.delay))


# Holder()
