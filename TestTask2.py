#  2. Дан файл text.txt в котором содержится произвольный текст.
#  
#  Необходимо написать:
#  - решение, которое будет шифровать данный файл, создавая новый файл text_ encrypted.txt
#  - решение которое будет расшифровывать файл и создавать новый расшифрованный файл text_ decrypted.txt
#  Методы шифрования на ваше усмотрение. Текст до шифрования и после расшифровки должен быть одинаковым. В описании решения укажите какой метод шифрования используется.

    
import base58

# Читаем файл, копируем текст, кодируем текст
with open('text.txt', 'r', encoding='utf-8') as file:
    sourceTxt = file.read()
    
codeText = base58.b58encode(sourceTxt.encode('utf-8')).decode() 

# Пишем в новый файл
with open('text_encrypted.txt', 'w', encoding='utf-8') as file:
    file.write(codeText)  
    
# Читаем файл, копируем текст, декодируем текст      
with open('text_encrypted.txt', 'r') as file:
    encryptedTxt = file.read()
    
decryptedTxt = base58.b58decode(encryptedTxt).decode()

# Пишем в новый файл    
with open('text_decrypted.txt', 'w', encoding='utf-8') as file:
    file.write(decryptedTxt)      

print(decryptedTxt)
   