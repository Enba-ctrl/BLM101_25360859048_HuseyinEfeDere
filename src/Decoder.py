print("----- Brookshear Makine Dili Yorumlayıcısı -----")

#Gecerli hex karakterlerini tanımlama
gecerli_hex_karakterler = "0123456789ABCDEFabcdef"

# Kullanıcıdan veri al
#Başa ve sona hatalı boşluk durumunu engelleek için 
girilen_kod = input("Lütfen 4 haneli HEX kodunu giriniz (Örn: 14A3): ").strip()  #Başa ve sona hatalı boşluk tuşu gelme durumunu engellemek için strip yapısı var.

# Çıktı değişkenleri
parcalama_metni = ""
aciklama_metni = ""

# 2. Hata Kontrolleri
if len(girilen_kod) != 4:
    # Hata durumu 1: Uzunluk
    print(f"HATA: Girilen kod 4 haneli olmalıdır. (Girilen: {len(girilen_kod)} hane)")

elif not all(c in gecerli_hex_karakterler for c in girilen_kod):
    # Hata durumu 2: Karakter
    print("HATA: Kod sadece 0-9 ve A-F arası karakterlerden oluşmalıdır.")

else:
    
    # Büyük harfe çevir
    hex_kod = girilen_kod.upper()

    # Kodu Parçala
    opcode = hex_kod[0]
    reg_id = hex_kod[1]
    op2 = hex_kod[2]
    op3 = hex_kod[3]
    son_iki = hex_kod[2:]

    # Yorumlama kısmı
    if opcode == '1':
        parcalama_metni = f"Opcode={opcode}, Register={reg_id}, Adres={son_iki}"
        aciklama_metni = f"{son_iki} adresindeki bellek hücresinin içeriğini, {reg_id} numaralı kaydediciye (Register) yükle."

    elif opcode == '2':
        parcalama_metni = f"Opcode={opcode}, Register={reg_id}, Değer={son_iki}"
        aciklama_metni = f"{son_iki} değerini (hexadecimal), {reg_id} numaralı kaydediciye (Register) yükle."

    elif opcode == '3':
        parcalama_metni = f"Opcode={opcode}, Register={reg_id}, Adres={son_iki}"
        aciklama_metni = f"{reg_id} numaralı kaydedicinin içeriğini, {son_iki} adresindeki bellek hücresine kaydet."

    elif opcode == '4':
        parcalama_metni = f"Opcode={opcode}, Hedef Reg={op2}, Kaynak Reg={op3}"
        aciklama_metni = f"{op3} numaralı kaydedicinin içeriğini, {op2} numaralı kaydediciye kopyala."

    elif opcode == '5':
        parcalama_metni = f"Opcode={opcode}, Hedef Reg={reg_id}, Kaynak1={op2}, Kaynak2={op3}"
        aciklama_metni = f"{op2} ve {op3} kaydedicilerini (Tam Sayı) topla, sonucu {reg_id} numaralı kaydediciye yaz."

    elif opcode == '6':
        parcalama_metni = f"Opcode={opcode}, Hedef Reg={reg_id}, Kaynak1={op2}, Kaynak2={op3}"
        aciklama_metni = f"{op2} ve {op3} kaydedicilerini (Kayan Noktalı) topla, sonucu {reg_id} numaralı kaydediciye yaz."

    elif opcode == '7':
        parcalama_metni = f"Opcode={opcode}, Hedef Reg={reg_id}, Kaynak1={op2}, Kaynak2={op3}"
        aciklama_metni = f"{op2} ve {op3} kaydedicilerine OR (VEYA) işlemi yap, sonucu {reg_id} numaralı kaydediciye yaz."

    elif opcode == '8':
        parcalama_metni = f"Opcode={opcode}, Hedef Reg={reg_id}, Kaynak1={op2}, Kaynak2={op3}"
        aciklama_metni = f"{op2} ve {op3} kaydedicilerine AND (VE) işlemi yap, sonucu {reg_id} numaralı kaydediciye yaz."

    elif opcode == '9':
        parcalama_metni = f"Opcode={opcode}, Hedef Reg={reg_id}, Kaynak1={op2}, Kaynak2={op3}"
        aciklama_metni = f"{op2} ve {op3} kaydedicilerine XOR (ÖZEL VEYA) işlemi yap, sonucu {reg_id} numaralı kaydediciye yaz."

    elif opcode == 'A':
        parcalama_metni = f"Opcode={opcode}, Register={reg_id}, Döndürme Miktarı={op3}"
        aciklama_metni = f"{reg_id} numaralı kaydedicinin içeriğini sağa doğru {op3} bit kadar döndür (Rotate)."

    elif opcode == 'B':
        parcalama_metni = f"Opcode={opcode}, Register={reg_id}, Hedef Adres={son_iki}"
        aciklama_metni = f"Eğer {reg_id} numaralı kaydedici, 0 numaralı kaydediciye eşitse; {son_iki} adresine atla (JUMP)."

    elif opcode == 'C':
        parcalama_metni = f"Opcode={opcode}, Parametreler=Yok"
        aciklama_metni = "Programı durdur (HALT)."

    else:
        # Tanımlanamayan Opcode durumu
        parcalama_metni = "BİLİNMİYOR"
        aciklama_metni = "HATA: Girdiğiniz İşlem Kodu (Op-code) tanımlı değildir. Tekrar deneyiniz."

    # SONUÇ EKRANI (Sadece hata yoksa ve işlem yapıldıysa gösterilir)
    # Eğer parcalama_metni hala boşsa (BİLİNMİYOR durumu hariç) yukarıdaki else'e hiç girmemiş demektir.
    
    print("-" * 80)
    print(f"Girilen Kod: {hex_kod}")
    
    if parcalama_metni != "BİLİNMİYOR":
        print(f"Program kodu parçaları: {parcalama_metni}")
        print(f"Kodun İşlevi: \"{aciklama_metni}\"")
    else:
        print(aciklama_metni)
        
    print("-" * 80)