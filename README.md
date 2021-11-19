# COVID-19 Disease Prediction(COVID-19 Hastalık Tahmini) Uygulaması

Bu proje, gerçek insanların verilerinden oluşan bir veri setinin, makine öğrenmesi ve derin öğrenme yöntemleri kullanılarak kişinin hastalık tahminine olanak tanımaktadır.

>**Proje Klasör İçeriği**

-Proje, hem makine öğrenmesi yöntemleri ile hem de derin öğrenme yöntemleri kullanılarak kodlanmıştır. Projenin makine öğrenmesi kısmı ile gerçekleştirilen işlemleri 'COVID-19_Disease_Prediction_ML.ipynb' içerisinde, derin öğrenme kısmı ile gerçekleştirilen işlemleri 'COVID-19_Disease_Prediction_DL.ipynb' içerisinde bulunmaktadır.

-Projede kullanılan veri seti klasör içerisinde 'Covid Dataset.csv' adıyla mevcuttur. Veri seti [kaggle](https://www.kaggle.com/) platformu üzerinden indirilmiştir. Makine öğrenmesi kısmında verinin hazırlanması işlemleri sonucunda elde edilen yeni veri seti ise derin öğrenme kısmında kullanılmak üzere(yeniden aynı işlemlerin tekrarlanmaması adına) 'new_COVID-19_Dataset.csv' formatında kaydedilmiştir.

-Eğitim ve test sonucunda en iyi sonucu veren makine öğrenmesi algoritması olarak 'RandomForestClassifier' seçilmiştir. Bu algoritmanın daha sonrasında test edilebilmesi adına 'model' klasörünün içerisine 'rfc_model.pkl' adıyla kaydedilmiştir. Derin öğrenme kısmında ise oluşturulan ağ mimarisiyle eğitilen veri seti sonucunda elde edilen modelin test edilebilmesi için 'model' klasörünün içerisine 'covid19_model.h5' adıyla kaydedilmiştir.

-Mevcut projenin kolayca test edilebilmesi adına Python web framework'ü olan Flask tercih edilmiştir. Bu projeye ait kod dosyaları ise 'COVID-19 Predictor' isimli klasör içerisinde mevcuttur.Bu klasör içerisinde makine öğrenmesi yöntemleri sonucu elde edilen 'rfc_model.pkl' dosyası bulunmaktadır. 'templates' klasörü içerisinde ise basit görünüme sahip, kullanıcıların hastalık ile alakalı sorulara cevap verip test sonucunu öğrendiği bir web sayfası mevcuttur. 'app.py' içerisinde ise Flask kullanılarak makine öğrenmesi modelinin web üzerinde çalışmasını sağlayan kod yapısı bulunmaktadır.

>**Projenin Çalıştırılması**

-Projeyi çalıştırmak için ilk olarak 'COVID-19 Predictor' klasörü içerisinde bulunan 'app.py' dosyası çalıştırılır. Açılan CMD ekranında bulunan 'http://127.0.0.1:8000/' adres kopyalanarak herhangi bir tarayıcının URL kısmna kopyalanır. Bu sırada 'app.py' dosyasının arka planda çalıştığından emin olunuz. Test sayfasına ulaştıktan sonra sorulan sorulara  kullanıcıda bulunup bulunmamasına göre cevaplandıktan sonra 'Test Sonucunu Görüntüle' butonuna tıklanır. Bu sayede kullanıcı test sonucunu kolaylıkla öğrenebilmektedir.

>**Projenin Test Edilmesi**

![COVID-19 Predictor](https://user-images.githubusercontent.com/94120299/142641009-50507f39-7b53-4c1b-865f-8d8784e7d05a.gif)
