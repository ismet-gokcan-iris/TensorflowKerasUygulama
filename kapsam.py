##scope

"""numara = 20 
def carpma(rakam):
    numara =10
    return numara*rakam
d=carpma(25)
print(d)    """


##local,enclosing,global,built-in

"""benimAdım = "ismet"
#global
def benimFonksiyonum():

    benimAdım="mahmut"
    #enclosing
    def icFonksiyon():
        benimAdım="ayşe"
        print(benimAdım)
    icFonksiyon()    
benimFonksiyonum()
print(benimAdım)      
"""

"""y=10

def yeniFonksiyon(y):
    print(y)
    y=5
    print(y)

    return y
a=yeniFonksiyon(3)
print(a)
print(y)"""

"""y=10
def ornekFonksiyon():
    global y
    y=5
    print(y)

ornekFonksiyon()"""


    
