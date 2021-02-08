alpha_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_small = 'abcdefghijklmnopqrstuvwxyz'

def run(msg="",key="",status=0):        
    out = []    
    
    for i in range(len(msg)):        
        
        # Mencari nilai key
        if key[i].isalpha():                
            if key[i].islower():
                key_val = alpha_small.index(key[i])
            elif key[i].isUpper():
                key_val = alpha_big.index(key[i])
        # Memeriksa non alfabet
        else : 
            exit(0,('Karakter non alfabet pada kunci : ' + key[i]))                                
        
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
            # Pengecuailian pada spasi
            elif msg[i].isspace():
                out.append(' ')
            # Memeriksa karakter non alfabet
            else : 
                exit(0,('Karakter non alfabet pada pesan : ' + msg[i]))                
            
    return "".join(out)

if __name__ == "__main__":
    print('VIGENERE CIPHER AUTO-KEY')    
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
        
        # Menambahkan kunci dengan bagian dari pesan
        if len(kunci) < len(pesan):
           min = len(pesan) - len(kunci)
           for i in range(min):
               kunci += pesan[i]            
                        
        # Menyimpan dan menampilkan output
        output = run(pesan,int(kunci),status)
        print('Output :',output,'\n')