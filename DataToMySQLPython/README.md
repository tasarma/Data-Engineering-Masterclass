<h1> Python ile Verilerin MySQL'e Aktarımı </h1>
Verileri MySQL veritabanına aktarmak için Python programlama dili kullanılmıştır. Programa ait açıklayıcı detaylara aşağıda bulabilirsiniz.

<h2> Kütüphanelerin dahil edilmesi </h2>
import mysql.connector --> Python'ı MySQL ile ilişki kurmak için dahil edilmiştir.
import csv	       --> Veri setleri ".tsv" uzantılı oldukları için csv kütüphanesi dahil edilmiştir.
import time   	       --> Uygulamanın çalışma süresini ölçmek için içe aktarılmıştır.

<h2> MySQL ile bağlantı kurulması </h2>
mysql.connector.connect --> Veritabanın yüklü olduğu host.
db.cursor()		--> Veritabanına bağlanması için gerekli komutları çalıştırır.

! Verilerin MySQL'e aktarılabilmesi için kod içerisinde gerekli olan özellikler belirtilerek insert değerleri oluşturulmuştur. Her tabloya uygun olacak şekilde sütunlar belirlenerek değerler atanmıştır.

<h2> Verinin okunması </h2>
Verilerin doğru bir şekilde varitabanına aktarılması amacıyla, değerler öncelikle "csv.reader" ile dosyalardan okunmuştur. Daha sonra "my data" listesi oluşturularak veriler içine aktarılmıştır. Liste oluşturulmasının sebebi, verileri düzenledikten sonra hepsini bir yerde toplayıp veritabanına aktarabilmektir.

<h2> Verinin aktarılması </h2>
cursor.executemany --> Veriler, yazılan insert değerleri ile my data veri listesi her tabloya uygun olacak şekilde "executemany" komutu ile tablolara aktarılmıştır.


