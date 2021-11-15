"""ogrenciler={
    "120" : {
        "ad":"ali",
        "soyad":"yılmaz",
        "telefon":"532 000 00 00"
    },
    "125" : {
        "ad": "can",
        "soyad": "korkmaz",
        "telefon": "534 000 00 00"
    },
    "128": {
        "ad":"volkan",
        "soyad": "yükselen",
        "telefon": "539 000 00 00"
    }
}"""

ogrenciler={}

number=input("öğrenci no: ")
name=input("öğrenci adi: ")
surname= input("öğrenci soyad: ")
phone= input("öğrenci telefon: ")

"""
ogrenciler[number]={
    "ad": name,
    "soyad":surname,
    "telefon":phone
}"""


ogrenciler.update({
    number : {

         "ad": name,
         "soyad":surname,
         "telefon":phone
    }
})

number=input("öğrenci no: ")
name=input("öğrenci adi: ")
surname= input("öğrenci soyad: ")
phone= input("öğrenci telefon: ")

ogrenciler.update({
    number : {

         "ad": name,
         "soyad":surname,
         "telefon":phone
    }
})

number=input("öğrenci no: ")
name=input("öğrenci adi: ")
surname= input("öğrenci soyad: ")
phone= input("öğrenci telefon: ")

ogrenciler.update({
    number : {

         "ad": name,
         "soyad":surname,
         "telefon":phone
    }
})




print(ogrenciler)


ogr = input("öğrenci no: ")

ogrenci=ogrenciler[number]

print(ogrenci)