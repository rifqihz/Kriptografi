alpha_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_small = 'abcdefghijklmnopqrstuvwxyz'

def run(msg="",key="",status=0):
    len_key = len(key)   
    key_counter = 0
    
    out = []    
    
    for i in range(len(msg)):
        # Mengatur perhitungan key 
        if key_counter == len_key:
            key_counter = 0
        
        # Mencari nilai key
        if key[key_counter].isalpha():                
            if key[key_counter].islower():
                key_val = alpha_small.index(key[key_counter])
            elif key[key_counter].isUpper():
                key_val = alpha_big.index(key[key_counter])
        # Memeriksa non alfabet
        else : 
            exit(0,('Karakter non alfabet pada kunci : ' + key[key_counter]))        
                
        # Status 1 = Enkripsi
        # Status 2 = Dekripsi
        
        if status == 1 :
            # Mencari nilai pesan             
            if msg[i].isalpha():
                small = msg[i].islower()            
                if small:
                    msg_val = alpha_small.index(msg[i])
                    # Memasukkan karakter Cipher
                    out.append(alpha_small[(msg_val + key_val) % 26])
                elif not small:
                    msg_val = alpha_big.index(msg[i])
                    # Memasukkan karakter Cipher
                    out.append(alpha_big[(msg_val + key_val) % 26])                                
                key_counter += 1
            # Pengecualian pada spasi
            elif msg[i].isspace():
                out.append(' ')
            # Memeriksa karakter non alfabet
            else : 
                exit(0,('Karakter non alfabet pada pesan : ' + msg[i]))
                        
        elif status == 2 : 
            # Mencari nilai cipher
            if msg[i].isalpha():
                small = msg[i].islower()
                if small:
                    msg_val = alpha_small.index(msg[i])
                    # Memasukkan karakter pesan
                    out.append(alpha_small[(msg_val - key_val) % 26])
                elif not small:
                    msg_val = alpha_big.index(msg[i])
                    # Memasukkan karakter pesan
                    out.append(alpha_big[(msg_val - key_val) % 26])
                key_counter += 1
            # Pengecuailian pada spasi
            elif msg[i].isspace():
                out.append(' ')
            # Memeriksa karakter non alfabet                
            else : 
                exit(0,('Karakter non alfabet pada pesan : ' + msg[i]))                
            
            
    return "".join(out)

if __name__ == "__main__":
    print('VIGENERE CIPHER STANDAR')    
    while True :
        status = 0        
        
        # Memasukkan nilai status
        status = str(int(input("\n(1) Enkripsi\n(2) Dekripsi\n(99) Keluar\nKode : ")))
        while (status != 1) & (status != 2) & (status != 99) :     
            print('Kode tidak sesuai')
            status = str(int(input("\n(1) Enkripsi\n(2) Dekripsi\n(99) Keluar\nKode : ")))
        
        # Status 1 = Enkripsi
        # Status 2 = Dekripsi
        # Status 99 = Keluar
        
        if status == '1':
            pesan = str(input('Masukkan pesan :'))
        elif status == '2':
            pesan = str(input('Masukkan cipher : '))
        elif status == '99': 
            print('Selesai ...')
            break
        
        kunci = str(input('Masukkan kunci :'))        
        
        # Menyimpan dan menampilkan output
        output = run(pesan,int(kunci),status)
        print('Output :',output,'\n')
        
