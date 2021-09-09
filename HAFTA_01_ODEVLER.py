###############################################
# ÖDEV 1: Komut satırından Python kodu çalıştırma.
###############################################

# Yazacak olduğunuz "py" uzantılı bir python dosyasını komut satırından çalıştırmanız beklenmektedir.
# Örneğin hi.py isimli bir dosyanız olsun ve içinde print("isim soy isim") kodu olsun.
# Bilgisayarınızın konsolunu açıp konsoldan hi.py dosyasının olduğu dizine gelip buradan "python hi.py" kodunu
# çalıştırdığınızda ekranınızda "isim soy isim" yazmalı.
# Adım adım nasıl yapılacağı anlatılmıştır.

# Adım 1: PyCharm'da "hi.py" isminde python dosyası oluştur.
# Adım 2: Bu dosyanın içirisine şu kodu kendine göre yaz ve kaydet: print("Ben Sinan Artun ÖDEV tamam, bu çok kolaymış")
# Adım 3: Şimdi konsoldan "hi.py" dosyasının olduğu dizine (klasöre) gitmen gerekiyor.
# Neyse ki PyCharm ile bu çok kolay. Sol tarafta yer alan menüde hi.py dosyası hangi klasördeyse
# o klasöre sağ tuş ile tıklayıp şu seçimi yap: "open in > terminal".
# PyCharm'ın alt tarafında terminal ekranı açılacak. Şu anda hi.py dosyası ile aynı dizindesin (klasörde).
# Adım 4: Konsolda şu kodu yazmalısın: python hi.py
# Adım 5: Çıktını ekran görüntüsünü alıp grubunda paylaş.

###############################################
# ÖDEV 2: Kendi adınızda bir virtual environment oluşturunuz ve aşağıdakileri yapınız.
###############################################

###############################################
# Görev 1: Kendi isminizde bir virtual environment oluşturunuz oluşturma esnasında python 3 kurulumu yapınız.
###############################################

###############################################
# Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
###############################################

###############################################
# Görev 3: Yüklü paketleri listeleyiniz.
###############################################

###############################################
# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
###############################################

###############################################
# Görev 5: İndirilen Numpy'ın versiyonu nedir?
###############################################

###############################################
# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyon nedir?
###############################################

###############################################
# Görev 7: Numpy'ı environment'tan siliniz.
###############################################

###############################################
# Görev 8: Seaborn kütüphanesini ve matplotlib kütüphanesini aynı anda güncel versiyonları ile indiriniz.
###############################################

###############################################
# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
###############################################

###############################################
# Görev 10: Oluşturduğunuz environment'i siliniz.
###############################################
# İpucu: Önce environment'i deactivate ediniz.





###############################################
# ÖDEV 3: List Comprehension Applications
###############################################

###############################################
# Görev 1: car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
###############################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# Veri setini baştan okutarak aşağıdaki çıktıyı elde etmeye çalışınız.

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.


###############################################
# Görev 1 Çözüm
###############################################


###############################################
# Görev 2: İsminde "no" BARINDIRMAYAN değişkenlerin isimlerininin SONUNA "FLAG" yazınız.
###############################################

# Notlar:
# Tüm değişken isimleri büyük olmalı.
# Tek bir list comp ile yapılmalı.

# Beklenen çıktı:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

###############################################
# Görev 2 Çözüm
###############################################


###############################################
# Görev 3: Aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçerek yeni bir df oluşturunuz.
###############################################

# df.columns
# og_list = ["abbrev", "no_previous"]

# Notlar:
# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df["new_cols"] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

# Beklenen çıktı:

# new_df.head()
#
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630


###############################################
# Görev 3 Çözüm
###############################################
