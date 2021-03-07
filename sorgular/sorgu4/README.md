<h1> Sorgu: 6-d </h1>

<h2> Kütüphanelerin dahil edilmesi </h2>
import mysql.connector --> Python'ı MySQL ile ilişki kurmak için dahil edilmiştir.
import csv	       --> Veri setleri ".tsv" uzantılı oldukları için csv kütüphanesi dahil edilmiştir.
import time   	       --> Uygulamanın çalışma süresini ölçmek için içe aktarılmıştır.

<h2> MySQL ile bağlantı kurulması </h2>
mysql.connector.connect --> Veritabanın yüklü olduğu host.
db.cursor()		--> Veritabanına bağlanması için gerekli komutları çalıştırır.

! Sorgunun  MySQL'den  yapılabilmesi için kod içerisinde gerekli olan özellikler belirtilerek query oluşturulmuştur.

<h2> Sorgunun gerçekleştirilmesi </h2>
cursor.execute(query) --> Komutu kullanılarak MySQL üzerinde sorgu gerçekleştirilmiştir.
cursor.fetchall()     --> Sorgu sonucu alınarak "myresult" a değişkenine atanmıştır.

for döngüsü kullanılarak istenilen sonuç ekrana yazılmıştır.

<h2> "Seçtiğiniz dizinin IMDB'de en az kişi tarafından oylanmış 5 bölümü"</h2>
<pre>
+-----------------+---------------+----------+
| originalTitle   | episodeNumber | numVotes |
+-----------------+---------------+----------+
| Game of Thrones | 3             |    23449 |
| Game of Thrones | 7             |    23487 |
| Game of Thrones | 2             |    23707 |
| Game of Thrones | 4             |    23711 |
| Game of Thrones | 5             |    23886 |
+-----------------+---------------+----------+

</pre>
