# 2.2 - Hadoop MapReduce

## Tujuan
Menjalankan Hadoop single-node dan mempraktikkan program **MapReduce WordCount** untuk memahami alur Map → Shuffle → Reduce secara langsung, bukan cuma teori.

## Environment
- **OS**: Windows 11 + WSL (Ubuntu)
- **Hadoop**: versi 3.3.6, instalasi standalone (bukan Docker)
- **Java**: OpenJDK 11 (`openjdk-11-jdk`)
- **Data**: `data.txt` dari IBM Skills Network (3 baris teks pendek)

## Materi & Command yang Dipakai

| Tahap | Command | Keterangan |
|---|---|---|
| Download Hadoop | `curl https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz --output hadoop-3.3.6.tar.gz` | Ambil paket instalasi Hadoop dari server resmi Apache |
| Extract | `tar -xvf hadoop-3.3.6.tar.gz` | Buka arsip `.tar.gz` (`-x` extract, `-v` verbose, `-f` nama file) |
| Cek instalasi | `bin/hadoop` | Smoke test — pastikan script Hadoop bisa jalan |
| Install Java | `sudo apt install -y openjdk-11-jdk` | Hadoop butuh JVM untuk berjalan |
| Cari path Java | `update-alternatives --list java` | Menemukan lokasi instalasi Java untuk `JAVA_HOME` |
| Set environment | `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64`<br>`export PATH=$PATH:$JAVA_HOME/bin` | Kasih tahu Hadoop di mana Java berada |
| Download data | `curl <url>/data.txt --output data.txt` | File teks contoh untuk dihitung kata-katanya |
| Jalankan WordCount | `bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar wordcount data.txt output` | Jalankan job MapReduce: `data.txt` = input, `output` = folder hasil (dibuat otomatis) |
| Cek hasil | `ls output` → `cat output/part-r-00000` | `_SUCCESS` menandakan job selesai; `part-r-00000` berisi hasil akhir count |

**Hasil akhir WordCount:**
```
BigData   2
Hadoop    1
IBM       1
MapReduce 2
```

## Relevansi ke Data Engineering
- **Map → Shuffle → Reduce langsung terlihat lewat log job**: Map input records=3 (3 baris) → Map output records=6 (6 kata mentah) → Combine output records=4 (digabung dulu di tahap Map) → Reduce output records=4 (hasil akhir 4 kata unik). Ini bikin teori MapReduce yang abstrak jadi konkret lewat angka nyata.
- **Combiner sebagai optimisasi**: sebelum data dikirim lewat jaringan (shuffle), Hadoop sudah menggabungkan sebagian di tahap Map lokal — konsep ini penting dipahami untuk optimasi pipeline data besar di masa depan (mengurangi network I/O).
- **Instalasi standalone vs Docker**: setelah sebelumnya pakai Docker untuk Hive (Lab 2.1), lab ini kasih pengalaman instalasi Hadoop native — membantu memahami dependency seperti JVM yang sering jadi sumber masalah environment di dunia DE nyata.

## Catatan Pribadi
- Awalnya dapat error `Unrecognized option: -` saat menjalankan wordcount. Ternyata penyebabnya adalah **spasi di nama folder** (`12 - Introduction to Big Data with Spark and Hadoop` dan `2.2 - Hadoop MapReduce`) — shell script internal Hadoop tidak meng-quote path dengan benar, sehingga bagian path yang mengandung tanda `-` malah dibaca sebagai opsi JVM. Solusinya: pindahkan instalasi Hadoop ke folder tanpa spasi (`~/hadoop-lab/`), lalu cukup simpan README/bukti kerja saja ke repo yang bernama panjang.
- Sempat juga kena `JAVA_HOME is not set` di awal — karena WSL ini belum pernah dipasangi JDK sebelumnya. Solusinya install `openjdk-11-jdk`, lalu set `JAVA_HOME` manual ke path hasil `update-alternatives --list java`.
- Pelajaran utama: nama folder dengan spasi bisa jadi sumber bug yang membingungkan di tool berbasis shell script lama seperti Hadoop — baik dicatat sebagai kebiasaan untuk proyek instalasi software besar ke depannya, sebaiknya dijalankan di path tanpa spasi.