import random
import string

def generatePassword(min_length, numbers=True, specialCharacters=True):
    #string.ascii_letters ASCII karakterlerini temsil eden büyük ve küçük harflerini
    #içeren bir dizedir.
    letters = string.ascii_letters
    #string.digits rakamları içerir.
    digits = string.digits
    #string.punctuation özel karakterleri içerir.
    special = string.punctuation
    #characters değişkeni harf karakterini içerir.
    characters = letters
    #Eğer numbers seçeneği True olarak belirtilmişse characters değişkenine özel
    #sayıları da ekler.
    if numbers:
        characters += digits
    #specialCharacters seçeneği True olarak belirtilmişse characters değişkenine özel
    #karakterleri de ekler.
    if specialCharacters:
        characters += special
    #boş bir şifre dizi oluşturulur.
    pwd = ""
    #meetsCriteria şifrenin belirtilen kriterlere uygun olup olmadığını kontrol etmek için
    #tanımlanır ve başlangıçta False olarak ayarlanır.
    meetsCriteria=False
    #has_number ve has_special her ikisi de başlangıçta false olarak ayarlanır.Şifrenin içinde
    #sayılar ve özel karakterler bulunup bulunmadığını izlemek için kullanılır.
    has_number= False
    has_special=False
    #Bu döngü şifrenin belirtilen kriterlere uygun olup olmadığını ve belirtilen minimum uzunluğunu
    #kontrol eder.
    while not meetsCriteria or len(pwd) < min_length:
        #her döngüde new_char adında rastgele bir karakter seçilir ve 'pwd' değişkenine eklenir.
        new_char = random.choice(characters)
        pwd += new_char
        #seçilen yeni karakter rakam içeriyorsa 'has_nubmer' True olarak ayarlanır.
        if new_char in digits:
            has_number = True
        #seçilen yeni karakter özel bir karakterse 'has_special' True olarak ayarlanır.
        elif new_char in special:
            has_special = True
        #meetsCriteria başlangıçta True ayarlanır,ancak eğer 'numbers' seçeneği True ve has_number False ise
        #veya 'specialCharacters' True ve 'has_special' False ise meetdCriteria tekrar False olur.
        #Yani belirli kriterler sağlamıyorsa,'meetsCriteria' False olur ve döngü devam eder.
        meetsCriteria = True
        if numbers:
            meetsCriteria = has_number
        if specialCharacters:
            meetsCriteria = meetsCriteria and has_special
    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers? (y/n)").lower() == "y"
has_special = input("Do you want to have special characters? (y/n)").lower() == "y"
pwd = generatePassword(min_length,has_number,has_special)
print("The generated password is:", pwd)