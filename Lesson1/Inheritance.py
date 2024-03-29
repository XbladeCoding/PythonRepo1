class people:
    def speak(self):
        print('Speaking ')

class american(people):
    def speak(self):
        print('English')

class french(people):
    def speak(self):
        print('French')

Rohan = american
mbappe = french

mbappe.speak()
Rohan.speak()
