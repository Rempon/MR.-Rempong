# PEMOGRAMAN SUHU

# Salam Pembuka

print (63*"=")
print ("=",12*"¤>•<¤","=")
print ("=__  __ ____      ____                                         =")
print ("=|  \/  |  _ \    |  _ \ ___ _ __ ___  _ __   ___  _ __   __ _ =")
print ("=| |\/| | |_) |   | |_) / _ \ '_ ` _ \| '_ \ / _ \| '_ \ / _` |=")
print ("=| |  | |  _ < ___|  _ <  __/ | | | | | |_) | (_) | | | | (_| |=")
print ("=|_|  |_|_| \_|___|_| \_\___|_| |_| |_| .__/ \___/|_| |_|\__, |=")
print ("=                                     |_|                |___/ =")
print ("=",12*"¤>•<¤","=")
print (63*"=")

# Mengambil Input Dari User
#salam pembuka

print (49*"=")
print ("=WELCOME TO THE PROGRAM=<¤>=BY MR.REMPONG (MR.F)=")
print (49*"=")

#pemilihan suhu

print ("")
print ("Silakan Pilih Suhu")
print ("[1].Celcius")
print ("[2].Reamur")
print ("[3].Fahreheit")
print ("[4].Kelvin")

suhu = int (input ("Masukan Nomor :"))

# Membuat Program 
#mengubah suhu celcius ke satuan lain

if suhu == 1:
    celcius = float (input ("Masukan Suhu Dalam Celcius :"))
    print ("Suhu adalah",celcius,"°C")

    #Reamur
    reamur = (4/5) * celcius
    print ("Suhu Adalah",reamur,"°R")

    #Fahraenheit
    fahrenheit = ((2/5) * celcius) + 32
    print ("Suhu Adalah",fahrenheit,"°F")

    #Kelvin
    kelvin = celcius + 273
    print ("Suhu Adalah",kelvin,"°K")

    #selesai
    print ("")
    print (17*'=')
    print ("=PROGRAM SELESAI=")
    print (17*'=')

#mengubah suhu reamur ke satuan lain

elif suhu == 2:
    reamur = float (input ("Masukan Suhu Dalam Reamur :"))
    print ("Suhu Adalah",reamur,"°R")

    #Celcius
    celcius= (5/4) * reamur
    print ("Suhu Adalah",celcius,"°C")

    #Fahraenheit
    fahrenheit = ((9/4) * reamur) + 32
    print ("Suhu Adalah",fahrenheit,"°F")

    #Kelvin
    kelvin = ((5/4) * reamur) + 273
    print ("Suhu Adalah",kelvin,"°K")

    #selesai
    print ("")
    print (17*'=')
    print ("=PROGRAM SELESAI=")
    print (17*'=')

#mengubah suhu fahrenheit ke satuan lain

elif suhu == 3:
    fahrenheit = float (input ("Masukan Suhu Dalam Fahrenheit :"))
    print ("Suhu Adalah",fahrenheit,"°F")

    #Celcius
    celcius = 5/9 * (fahrenheit-32)
    print ("Suhu Adalah",celcius,"°C")

    #Reamur
    reamur = 4/9 * (fahrenheit-32)
    print ("Suhu Adalah",reamur,"°R")

    #Kelvin
    kelvin = (5/9 * (fahrenheit-32)) + 273
    print ("Suhu Adalah",kelvin,"°K")

    #selesai
    print ("")
    print (17*'=')
    print ("=PROGRAM SELESAI=")
    print (17*'=')

#mengubah suhu kelvin ke satuan lain

elif suhu == 4:
    kelvin = float (input ("Masukan Suhu Dalam Kelvin :"))
    print ("Suhu Adalah",kelvin,"°K")

    #Celcius
    celcius = kelvin - 273
    print ("Suhu Adalah",celcius,"°C")

    #Reamur
    reamur = 4/5 * (kelvin-273)
    print ("Suhu Adalah",reamur,"°R")

    #Fahrenheit
    fahrenheit = ((kelvin-273) * 9/5) + 32
    print ("Suhu Adalah",fahrenheit,"°F")

    #selesai
    print ("")
    print (17*'=')
    print ("=PROGRAM SELESAI=")
    print (17*'=')

#selesai

else :
    print ("Maaf Suhu Tidak Ada")
    print ("")
    print (17*'=')
    print ("=PROGRAM SRLESAI=")
    print (17*'=')


