class Hayvan():
    def __init__(self):
        print("init çağırıldı")

    def method1(self):
        print("hayvan sınıfı method1 çağırıldı")
    def method2(self):
        print("hayvan sınıfı method2 çağırıldı")

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("kedi sınıfı init çağırıldı")
    def miyavla(self):
        print("miyav")
    def method1(self):
        print("kedi sınıfındaki method1 çağırıldı")
           
           

benimKedi = Kedi()

benimKedi.miyavla()
benimKedi.method1()
diğerHayvan=Hayvan()

diğerHayvan.method1()

              
        