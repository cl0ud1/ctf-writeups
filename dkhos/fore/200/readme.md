Bu tarz durumlarda genelde ilk bakılan resim isimleri, dosya isimleri, meta datalar(oluşturulma/değiştirilme zamanı, yorum, oluşturan kullanıcı bilgileri...) olur fakat karmaşık bi şekilde aramaktansa diğer sorularla uğraşırken bu işi benim yerime bi scriptin yapması daha mantıklı geldi.

![alt text](https://github.com/cl0ud1/ctf-writeups/blob/master/dkhos/fore/200/pics/2.png)




İlk olarak resimlere bakıldığında benim sonradan 1.jpg,2.jpg ve 15.jpg olarak adlandırdığım resimlerin köşelere geldiğini ve burda her bir kesilmiş resimin kendi içerisinde yakında olduğu köşeye(beyaz bölgelerin az olduğu kısımlar) denk geldiği anlaşılıyor. 21 resim var 3x3, 4x4 ihtimalleri üzerine duruyorum. İlk olarak 3x3 olarak 3 resmin konumunu tahmin ettiğimi göz önünde bulundurarak. 9 parçadan oluşmasını beklediğim sonucun 6 parçasını kaba kuvvet ile denemeye karar veriyorum. 3 parça dışında kalan 18 parçanın 6 lı permutasyonunun sonucu yeni bir kod elde ediyorum ve bu elde edilen kodu qr decode işlemine maruz bırakıyorum. Sonuc olarak bi cevap dönene kadar bu işlem devam ediyor ve sonuç resimdeki gibi geliyor.


![alt text](https://github.com/cl0ud1/ctf-writeups/blob/master/dkhos/fore/200/pics/1.png)


