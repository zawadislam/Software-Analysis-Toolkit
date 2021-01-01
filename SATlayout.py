
from flexx import flx

class mainpage(flx.Widget):

    def init(self):
        flx.Label(text='Software Analysis Tool')
        flx.Button(text='Hello')
        flx.Button(text='World')
        
app = flx.App(mainpage)
app.export('mainpage.html', link=0)
app.launch('browser')        
flx.run()