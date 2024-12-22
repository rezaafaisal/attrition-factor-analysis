# Proyek Pertama: Menyelesaikan Permasalahan HR Pada Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

### Permasalahan Bisnis

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Cakupan Proyek

Adapun cakupan pada proyek pertama ini adalah dengan mengidentifikasi faktor-faktor penyebab attrition rate yang signifikan serta membuatkan dashboard yang dapat dilihat secara visual dan model machine learning yang bisa digunakan untuk memprediksi dini apakah karyawan tersebut berpotensi untuk attrition atau tidak

### Persiapan

Sumber data: Dicoding

Setup environment:

```
pip install -r requirements.txt
```
*Menginstall dependecy yang diperlukan*
```
python prediction.py 
```
*Melakukan prediksi sederhana menggunakan model yang sudah di latih*

## Business Dashboard

- **Persentase Attrition Berdasarkan Departemen**, adalah bagan yang menampilkan persentase attrition rate berdasarkan departemen secara berurutan dari yang paling tinggi.
- **Rata-Rata Pendapatan Perbulan Setiap Job Role**, adalah rata-rata pendapatan perbulan dari masing-masing Job Role dengan total rata-ratanya adalah $68.3 dalam bentuk Pie Chart.
- **Rata-Rata Kepuasan Dalam Kantor**, merupakan gabungan dari 3 atribut yaitu kapuasan dalam kerjaan, kepuasan lingkungan kerja, kepuasan hubungan dengan rekan kerja.
- **Rata-rata Berdasarkan Usia**, adalah salah satu faktor yang mempengaruhi attrition rate yang tinggi dalam bentuk Scatter Plot.
- **Penghasilan (Gaji Bulanan dan Kenaikan Gaji)**, merupakan salah satu faktor yang mempengaruhi attrition rate yang tinggi berdasarkan 2 attribute yaitu rata-rata pemasukan bulanan dan rata-rata kenaikan gaji dalam bentuk Column Chart.


Link Dashboard : https://metabase.frealabs.web.id/public/dashboard/a1c2f77d-1cce-4ee0-93cf-35db1e71d0ab

## Conclusion

Berdasarkan hasil analisis, sebagian terdapat 2 faktor yang mempengaruhi attrition rate yaitu berdasarkan usia dan Penghasilan (Gaji Bulanan dan Kenaikan Gaji). Sedangkan dashboard bagian atas adalah hasil analisis secara berurutan departemen mana yang paling tinggi attrition rate-nya dan Rata-rata Pendapatan setiap bulan berdasarkan Job Role nya.

Pada faktor kepuasan, rata-rata satisfaction yang attrition rate yang tinggi cenderung lebih rendah dibanding yang tidak attrition.

Pada faktor usia, employee yang berusia anatara 18 dan 21 cenderung attrition ratenya lebih tinggi.

Sedangkan pada faktor penghasilan, dapat dilihat secara langsung bahwa gaji yang lebih sedikit dengan rata-rata gaji yang tidak attrition cenderung memiliki attrition rate yang tinggi.

### Rekomendasi Action Items (Optional)

####  Kepuasan Karyawan
- Memberikan fleksibilitas jam kerja atau opsi  kerja jarak jauh untuk meningkatkan keseimbangan kerja dan kehidupan.
- Bangun budaya kerja yang mendukung kolaborasi, inovasi, dan komunikasi terbuka.
- Mengadakan program pelatihan atau pendidikan untuk membantu karyawan meningkatkan keterampilan dan mencapai tujuan karir.
- Membuat program bimbingan untuk membantu karyawan merasa didukung dalam perjalanan karir mereka.

#### Usia 
- Meningkatkan fleksibilitas kerja untuk kelompok usia ini.
- Menawarkan program pelatihan karir atau peluang kenaikan jabatan.


#### Penghasilan
- Lakukan survei pasar untuk memahami standar industri dan gunakan data tersebut untuk merevisi skala gaji.
- Menawarkan insentif, dengan ini dapat membantu mempertahankan karyawan yang merasa bahwa gaji pokok mereka belum memadai.