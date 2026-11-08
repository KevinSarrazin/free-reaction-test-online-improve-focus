# Tes reaksi gratis online

Bahasa lain: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Tes waktu reaksi gratis yang berjalan di browser, dalam satu file HTML.

Coba online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/id/

Tunggu sampai panelnya berubah warna, lalu klik, ketuk, atau tekan Spasi secepat mungkin. Setelah sepuluh percobaan, kamu mendapat:

- **Rata-rata**: waktu rata-ratamu.
- **Median**: nilai tengah, yang tidak banyak bergeser karena satu percobaan yang meleset, tidak seperti rata-rata.
- **Tercepat**: percobaan terbaikmu.
- **Sebaran**: simpangan baku. Makin kecil, makin konsisten.
- **Klik terlalu cepat**: klik sebelum warnanya berubah. Percobaannya diulang.

Sepuluh seri terakhir disimpan di penyimpanan lokal browsermu. Tidak ada yang dikirim ke mana pun: tanpa pelacakan, tanpa skrip eksternal, tanpa pendaftaran.

## Cara menjalankan

Buka `index.html` di browser apa pun. Tanpa proses build, tanpa dependensi.

## Cara membaca hasilnya

Kebanyakan orang dewasa mendapat 200 hingga 300 ms pada tes visual sederhana seperti ini. Layar, mouse atau layar sentuh, dan browser masing-masing menambah beberapa milidetik, jadi bandingkan dirimu dengan dirimu sendiri, di perangkat yang sama. Tidur, kelelahan, kafein, dan jam berapa kamu mengerjakannya, semuanya memengaruhi hasil.

Tes ini mengukur waktu reaksi sederhana. Ini bukan diagnosis, dan bukan tes atensi klinis.

## Pasang tes ini di situs web kamu

Kamu bisa menampilkan tes waktu reaksi lengkap dari upchin.app di halamanmu sendiri, gratis. Tes ini tersedia dalam 17 bahasa: atur `data-lang` (atau `lang=` di alamat frame) ke `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Dengan skrip** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), yang menyesuaikan tinggi frame dengan isinya:

```html
<div data-upchin-embed="reaction-time-test" data-lang="id">
  <p>Tes waktu reaksi oleh <a href="https://upchin.app/id/alat/tes-reaksi">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Tanpa skrip**, jika situsmu hanya menerima HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=id" title="Tes waktu reaksi" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Tes waktu reaksi oleh <a href="https://upchin.app/id/alat/tes-reaksi">Upchin</a></p>
```

Mohon pertahankan baris kredit di bawah tes. Skrip menambahkan frame di sebelahnya dan tidak pernah menghapusnya.

## Versi lengkap

Versi lengkapnya, [tes waktu reaksi di upchin.app](https://upchin.app/id/alat/tes-reaksi), tersedia dalam 17 bahasa. Versi ini menyimpan riwayatmu, menjelaskan setiap angka, dan memungkinkanmu membagikan hasil.

Tes ini dibuat oleh tim di balik Upchin. Seperti kata situs webnya: "Aplikasimu dirancang supaya kamu terus scroll. Upchin dirancang untuk mengembalikan waktumu." Aplikasi iPhone-nya memakai Durasi Layar dari Apple untuk membantumu [mengurangi durasi layarmu](https://upchin.app/id), tanpa menggurui, dengan sedikit hambatan di saat yang tepat.
