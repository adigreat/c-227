
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encryption")
    msg=input("enter your message")
    key=int(input("enter key(1-94): "))
    encrypted_text=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32
        encrypted_text+=chr(temp)
    print("Encrypted: " + encrypted_text)
    main()        


    


    


def decryption():
    print("decrytion")
    print("messgae can only be in uppercase or lowecarse")
    encrypt_msg=input("enter encrypted text")
    decrypt_key =int(input("enter key(1-94):"))
    decrypted_text=""
    for i in range(len(encrypt_msg)):
        temp=(ord(encrypt_msg[i])-decrypt_key)
        if(temp<32):
            temp=temp+127-32
        decrypted_text+=chr(temp)
    print("decrypted_text: " + decrypted_text)





    
    

        
if __name__ == "__main__":
    main()      
