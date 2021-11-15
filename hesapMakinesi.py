def hesapla(a,b,islem):

    if islem not in "+-*/":
        return "lütfen şu işlemlerden birini seçiniz: +-*/"

    if islem=="+":
        return(str(a)+"+"+str(b)+" "+"="+str(a+b))
    if islem=="-":
        return(str(a)+"-"+str(b)+" "+"="+str(a-b))   
    if islem=="*":
        return(str(a)+"*"+str(b)+" "+"="+str(a*b))
    if islem=="/":
        return(str(a)+"/"+str(b)+" "+"="+str(a/b))

while True:
    try:        
        a = int(input("ilk sayiyi giriniz: "))
        b=int(input("ikinci sayiyi giriniz: "))
        islem = (input("işleminizi seçiniz: +-*/"))
        sonuc =hesapla(a,b,islem)

        print(sonuc)
    except:
        print("lütfen sayıları düzgün giriniz")    


