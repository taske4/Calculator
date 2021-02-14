import re

from kivy.app import App
from kivy.uix.widget import Widget

class CalculatorGui(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.changeSystem('dec')
        self._translate(n='0')

    def changeSystem(self, system):
        self.activeSystem = system
        self.changeKeyboard()

    def changeKeyboard(self):
        for id, el in self.ids.items():
            reResult = re.search(r'^key_.+', id)
            if reResult:
                el.disabled = True
                for system in el.groups:
                    if system == self.activeSystem:
                        el.disabled = False

    def _translate(self, n=False):
        sys = self.activeSystem
        if n == False:
            num = self.ids['system_' + sys].text
        else:
            num = n

        if sys != 'dec':
            if sys == 'hex':
                sys = 16
            elif sys == 'bin':
                sys = 2

            num = int(num, sys)
        else:
            num = int(num)

        for id, el in self.ids.items():
            reResult = re.search(r'^system_.+', id)
            if reResult:
                if el.name == 'hex':
                    el.text = str(hex(num))
                elif el.name == 'bin':
                    el.text = str(bin(num))
                elif el.name == 'dec':
                    el.text = str(num)

    def calc(self, num):
        self.ids['system_'+self.activeSystem].text += num
        self._translate()

    def delete(self):
        sys = self.activeSystem
        num = self.ids['system_' + sys].text
        if (len(num) - 1) > 0:
            self.ids['system_'+sys].text = num[:-1]
            self._translate()
        else:
            self.ids['system_'+sys].text = '0'
            self._translate()

    def clear(self):
        sys = self.activeSystem
        self.ids['system_'+sys].text = '0'
        self._translate()

class CalculatorApp(App):
    def build(self):
        return CalculatorGui()

if __name__ == '__main__':
    CalculatorApp().run()