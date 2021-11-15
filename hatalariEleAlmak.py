while True:
    try:
        benimInt=int(input("numara giriniz: "))
    except:
        print("lütfen gerçekten numara giriniz")
    else:
        print("teşekkürler")
        break
    finally:
        print("finally çağırıldı")
                

        





