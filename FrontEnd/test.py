from baseIntialization import UiFields

class backend(UiFields):
    def method(self):
        self.bill_txt = 12
        print(self.bill_txt)
        

v = backend()
# v.bg_color = 'red'
v.method()
