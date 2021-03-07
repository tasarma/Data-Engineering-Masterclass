<h1> Sorgu: 7-b </h1>

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

<pre>
+------------+-------------------+-----------+-----------+-------------------------------------+---------------------------------------------+
| nconst     | primaryName       | birthYear | deathYear | primaryProfession                   | knownForTitles                              |
+------------+-------------------+-----------+-----------+-------------------------------------+---------------------------------------------+
| nm10332206 | Roksana Wegiel    | 2005      | NULL      | actress,soundtrack,music_department | tt12323496,tt12319552,tt12323226,tt12319646 |
| nm11107925 | Dzejla Ramovic    | 2002      | NULL      | actress,music_department            | tt14072274,tt11714760,tt9728792             |
| nm11290217 | Viki Gabor        | 2007      | NULL      | soundtrack,actress,music_department | tt12317480,tt12317584,tt12323560,tt12319474 |
| nm3010029  | Veronica Powers   | 2001      | NULL      | actress,music_department,editor     | tt2321325,tt1637574,tt4948040,tt1244588     |
| nm3090922  | Chiara D'Ambrosio | 2005      | NULL      | actress,producer,music_department   | tt3596176,tt10838620,tt0069658,tt9695266    |
| nm3090925  | Bianca D'Ambrosio | 2005      | NULL      | actress,producer,music_department   | tt10838620,tt3596176,tt0452046,tt0069658    |
| nm3688576  | Rowan Blanchard   | 2001      | NULL      | actress,music_department,soundtrack | tt1620680,tt2712740,tt2543796,tt4111956     |
| nm4242016  | Talia Jackson     | 2001      | NULL      | actress,music_department            | tt9153270,tt7053188,tt6461784               |
| nm4658287  | Abbey Kochman     | 2001      | NULL      | actress,writer,music_department     | tt2093255,tt2005384,tt2331053,tt3479564     |
| nm4669325  | McKenzie Mack     | 2004      | NULL      | actress,music_department            | tt2084061,tt2175903,tt6857090,tt2048824     |
| nm4703354  | Nia Sioux         | 2001      | NULL      | actress,soundtrack,music_department | tt10520424,tt6385680,tt5539278,tt4883336    |
| nm5097044  | Isabela Merced    | 2001      | NULL      | actress,music_department            | tt3371366,tt7401588,tt7547410,tt5052474     |
| nm5462166  | Madison Hu        | 2002      | NULL      | actress,music_department,soundtrack | tt2712740,tt9664108,tt4800624,tt4196686     |
| nm6484816  | Brennley Brown    | 2002      | NULL      | actress,soundtrack,music_department | tt10687134,tt6303822,tt2136138,tt4902964    |
| nm7111120  | Olivia Rodrigo    | 2003      | NULL      | actress,music_department,soundtrack | tt4800624,tt8510382                         |
| nm8437490  | Grace VanderWaal  | 2004      | NULL      | soundtrack,actress,music_department | tt14109994,tt4858674,tt7133686,tt14112310   |
+------------+-------------------+-----------+-----------+-------------------------------------+---------------------------------------------+

</pre>
