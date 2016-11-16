from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
        self.bunny = self.loader.loadModel("./models/bvw-f2004--bunny/bunny")
        self.bunny.reparentTo(self.render)
        self.bunny.setPos(0, 20, 0)

MyApp().run()