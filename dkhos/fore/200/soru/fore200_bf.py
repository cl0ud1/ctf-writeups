
import os
import zbarlight
from itertools import permutations
import numpy as np
from PIL import Image

resimler=["3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg","11.jpg","12.jpg","13.jpg","14.jpg","16.jpg","17.jpg","18.jpg","19.jpg","20.jpg","21.jpg"]
perm = permutations(resimler, 6)



# 11 12 13 - 1.satır
# 21 22 23 - 2.satır
# 31 32 33 - 3.satır

sonuc11="15.jpg"
sonuc31="1.jpg"
sonuc13="2.jpg"




sayac = 1
while True:
    for tek_deger in list(perm):

        satir_resimler = [ Image.open(i) for i in [sonuc11, tek_deger[0], sonuc13]]
        minimum_boyut = sorted( [(np.sum(i.size), i.size ) for i in satir_resimler])[0][1]
        satir_1 = np.hstack( (np.asarray( i.resize(minimum_boyut,Image.ANTIALIAS) ) for i in satir_resimler ) )

        satir_1 = Image.fromarray(satir_1)





        satir_resimler = [ Image.open(i) for i in [tek_deger[1], tek_deger[2], tek_deger[3]]]
        minimum_boyut = sorted( [(np.sum(i.size), i.size ) for i in satir_resimler])[0][1]
        satir_2 = np.hstack( (np.asarray( i.resize(minimum_boyut,Image.ANTIALIAS) ) for i in satir_resimler ) )

        satir_2 = Image.fromarray(satir_2)





        satir_resimler = [ Image.open(i) for i in [sonuc31, tek_deger[4], tek_deger[5]]]
        minimum_boyut = sorted( [(np.sum(i.size), i.size ) for i in satir_resimler])[0][1]
        satir_3 = np.hstack( (np.asarray( i.resize(minimum_boyut,Image.ANTIALIAS) ) for i in satir_resimler ) )

        satir_3 = Image.fromarray(satir_3)


        toplam_resimler=[satir_1,satir_2,satir_3]

        minimum_boyut1 = sorted( [(np.sum(i.size), i.size ) for i in toplam_resimler])[0][1]
        satir__result = np.vstack( (np.asarray( i.resize(minimum_boyut1,Image.ANTIALIAS) ) for i in toplam_resimler ) )
        satir__result = Image.fromarray( satir__result)
        satir__result.save( './sonuclar/result.jpg' )


        file_path = './sonuclar/result.jpg'
        with open(file_path, 'rb') as sonuc_resim:
            image = Image.open(sonuc_resim  )
            image.load()
        codes = zbarlight.scan_codes('qrcode', image)
        print(str(sayac) + ' QR Sonuc: %s' % codes)
        if codes is not None:
            break
        os.remove(file_path)
        sayac += 1
    break
