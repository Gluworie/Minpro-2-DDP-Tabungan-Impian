*Tabungan Impian*<br>
Ceritanya ada dua jenis akun: admin yang bisa liat dan ngatur semua data, sama user biasa yang cuma bisa pegang tabungannya sendiri. Fitur utamanya ya standar CRUD: tambah, liat, ubah, hapus, plus ada fitur nabung/setor duit yang bakal ngitung otomatis progressnya dalam persen.<br>
File utamanya MINPRO_DDP2.py, jalan di terminal, dan butuh dua library luar, prettytable buat nampilin tabel rapi, sama pwinput buat nyembunyiin ketikan password jadi bintang-bintang.<br>
ini adalah flowchartnya:<br>
<img width="643" height="1010" alt="Flowchart MINPRO DDP2" src="https://github.com/user-attachments/assets/987f439c-2261-4c4a-b323-9a64ce84da0d" /><br>
Intinya program ini muter-muter di satu loop gede (while True paling bawah) yang nampilin menu awal terus-terusan. Begitu login berhasil, dia masuk ke loop lain lagi (menu admin atau menu user tergantung role), dan loop itu juga baru kebuka kalau user pilih logout. Jadi programnya nggak pernah "selesai" sampai user beneran milih opsi Keluar di menu paling awal.<br>
Penjelasan code:<br>
<img width="716" height="294" alt="image" src="https://github.com/user-attachments/assets/6dde1050-c928-44c0-ae41-4d383c2cf644" /><br>
Enam baris pertama itu daftar library yang dipakai. math buat floor pas ngitung persen, random buat milih kutipan motivasi, os buat bersihin layar, dan time buat jeda sleep biar pesan kayak "Login berhasil" sempat kebaca sebelum layarnya dihapus. Dua sisanya library luar, PrettyTable buat tabel dan pwinput buat password.<br>
<br>
Dua variabel di bawahnya itu yang jadi "database"-nya program. users isinya dictionary di dalam dictionary: key-nya username, terus nilainya dictionary lagi yang nyimpen password dan role. Jadi buat ngecek role seseorang tinggal manggil users[username]["role"]. Sedangkan tabungan awalnya kosong, dan tiap data yang ditambah bakal disimpen dengan ID angka sebagai key, misalnya tabungan[1] = {"nama": ..., "target": ..., "terkumpul": ..., "pemilik": ...}. Field pemilik ini penting banget, soalnya dari situ program tau tabungan mana punya siapa.<br>
<img width="416" height="127" alt="image" src="https://github.com/user-attachments/assets/0aecb0c8-9877-44bb-8494-95c12d4a31cd" /><br>
Ini buat bersihin layar terminal. os.name bakal bernilai "nt" kalau jalan di Windows, jadi dia manggil cls, selain itu (Linux/Mac) manggil clear. Dibikin jadi fungsi sendiri biar nggak usah nulis if-else ini berulang-ulang tiap kali mau ngebersihin layar, tinggal panggil bersihkan_layar() aja.<br>
<br>
Empat fungsi di bagian ini intinya sama: dipakai di mana-mana biar program nggak gampang error gara-gara user salah ketik. Semua input() di program ini lewat salah satu dari mereka, kecuali input username/password di login dan konfirmasi y/n pas hapus.<br>
<img width="935" height="198" alt="image" src="https://github.com/user-attachments/assets/071a3a7b-f73e-4786-bcc5-88af7687c9de" /><br>
Fungsi ini random milih satu dari tiga kutipan motivasi buat ditampilin di atas menu, biar programnya nggak garing-garing amat. Yang dipakai len(kutipan) - 1 bukan angka 2 langsung, jadi kalau nanti kutipannya mau ditambah, fungsinya nggak perlu diubah-ubah lagi. Fungsi ini juga cuma nge-return teksnya, yang nge-print tetap menu masing-masing.<br>
<br>
Fungsi validasi input<br>
<br>
Satu hal yang saya pengen banget dari program ini: nggak boleh crash gara-gara salah ketik. Makanya semua input() penting dibungkus fungsi sendiri sendiri.<br>
<img width="737" height="150" alt="image" src="https://github.com/user-attachments/assets/8fc9e382-933c-42f9-a274-e059e27585dd" /><br>
Dipakai tiap kali butuh isian teks, misalnya nama tujuan tabungan atau nama baru pas ngubah data. Pesan yang mau ditampilin dikirim lewat parameter pesan, jadi fungsinya bisa dipakai di banyak tempat dengan tulisan prompt yang beda-beda. Kalau yang diketik kosong, program nampilin peringatan terus nanya lagi.<br>
<img width="764" height="266" alt="image" src="https://github.com/user-attachments/assets/48162c02-f3de-4002-8db0-83405fb00771" /><br>
Ini buat semua isian angka kayak target, jumlah terkumpul, dan jumlah setoran. Ada dua lapis pengecekan. Yang pertama isdigit(), buat nolak huruf, simbol, atau angka desimal/negatif (soalnya tanda minus sama titik bikin isdigit() jadi False). Yang kedua ngecek angkanya nggak di bawah minimal. Contohnya target tabungan minimal 1 (masa target nol), sedangkan uang terkumpul boleh mulai dari 0. Selama belum valid dia terus muter, dan baru setelah lolos dua-duanya nilainya diubah jadi int lalu dikembaliin. Pakai flag angka_ok biar kondisi loop-nya gampang dibaca.<br>
<img width="843" height="263" alt="image" src="https://github.com/user-attachments/assets/33efe58b-4a8f-422c-adab-a3a489b483cc" /><br>
Cara kerjanya mirip input_angka, tapi khusus buat milih nomor menu. Bedanya batas bawahnya selalu 1 dan batas atasnya fleksibel lewat parameter maksimal, jadi menu 3 pilihan, 4 pilihan, atau 6 pilihan bisa pakai fungsi yang sama. Kalau user ngetik di luar rentang, dia dikasih tau pilihannya cuma dari 1 sampai berapa.<br>
<img width="783" height="148" alt="image" src="https://github.com/user-attachments/assets/375ba2ce-fbaf-48cd-b54b-c4db02f80da4" /><br>
Dipakai di fitur ubah, hapus, dan setor, yaitu pas user harus milih satu tabungan lewat ID-nya. Di dalamnya dia manggil input_angka dengan batas minimal 0, karena 0 sengaja dijadiin kode "batal". Terus dicek lagi apakah ID-nya ada di dictionary data yang dikirim ke fungsi ini. Poin pentingnya, yang dicek itu data hasil filter (bukan tabungan mentah), jadi user biasa nggak bisa ngetik ID milik orang lain dan tetep dianggap nggak ada.<br>
<img width="1026" height="296" alt="image" src="https://github.com/user-attachments/assets/d3d59b93-56fd-48a9-98ff-1edc5a1566a3" /><br>
   User dikasih maksimal 3 kali coba. Tiap putaran loop, username diketik biasa tapi password lewat pwinput biar yang muncul bintang-bintang. Kondisi loginnya dua: username harus ada di users, dan password yang diketik harus sama dengan yang tersimpen. Pengecekan username in users ditaruh duluan supaya nggak error (KeyError) kalau username yang diketik emang nggak ada. Kalau berhasil, fungsi langsung nge-return username-nya. Kalau gagal tiga kali, loop selesai dan fungsi nge-return string kosong, yang nanti dibaca program utama sebagai tanda gagal login.<br>
   <img width="959" height="477" alt="image" src="https://github.com/user-attachments/assets/3a7ef81f-5bf5-45af-9a68-fe4f65b02212" /><br>
Bikin akun baru lewat tiga tahap validasi yang berurutan. Pertama username, minimal 3 karakter dan belum dipakai orang lain (pesan error-nya dibedain sesuai masalahnya). Kedua password minimal 6 karakter. Ketiga password harus diketik ulang dan sama persis. Setelah lolos semua baru disimpen ke users. Role-nya di-set "user" secara paten, jadi nggak ada cara daftar sendiri langsung jadi admin. Akun admin cuma bisa dari yang udah ditulis di kode.<br>
<img width="1009" height="155" alt="image" src="https://github.com/user-attachments/assets/a512de0d-9adc-47dc-a1e6-c7770c0228c6" /><br>
Fungsi olah data tabungan<br>
<img width="1009" height="155" alt="image" src="https://github.com/user-attachments/assets/9067b98c-4f53-4175-a8f0-77a8297c5520" /><br>
Ini inti pembagian hak akses antara admin dan user. Fungsi ini nyaring isi tabungan jadi dictionary baru. Kalau role-nya admin, semua data lolos. Kalau bukan, cuma data yang pemilik-nya sama dengan username yang lagi login yang dimasukin. Fungsi lihat, ubah, hapus, dan setor semuanya lewat sini dulu sebelum nampilin atau ngolah apa pun, jadi aturan aksesnya cukup ditulis di satu tempat.<br>
<img width="1299" height="271" alt="image" src="https://github.com/user-attachments/assets/462e366c-db8d-4ba9-b9ef-0fbc84dd8a3c" /><br>
Dari sini tabel yang muncul di layar dibikin pakai PrettyTable. Header kolom di-set dulu lewat field_names, terus tiap data di-loop jadi satu baris. Kolom Progress dihitung langsung di sini: terkumpul dibagi target dikali 100, lalu dibulatin ke bawah pakai math.floor biar nggak ada koma. Misalnya 1 juta dari 5 juta jadi 20%, dan kalau hasilnya 99,9% tetep ditulis 99% (nggak naik ke 100% sebelum beneran penuh). Pembagian dengan nol aman karena target minimal selalu 1 dari validasi input_angka.<br>
<img width="1299" height="583" alt="image" src="https://github.com/user-attachments/assets/823c9f18-5706-4a17-b827-b15dc797ee0b" /><br>
Perbedaan admin dan user kelihatan jelas di sini. User biasa langsung jadi pemilik tabungannya sendiri, sedangkan admin disuruh milih tabungan ini atas nama siapa (daftar username ditampilin dulu, dan input-nya dicek harus ada di users). Habis itu ngisi nama, target, dan uang yang udah terkumpul. Kalau yang terkumpul ternyata lebih gede dari target, otomatis disamain sama target. ID barunya dicari dengan ngecek semua ID yang ada, lalu dipilih angka satu di atas yang paling besar. Karena begitu, ID dari tabungan yang udah dihapus nggak selalu dipakai ulang kalau yang kehapus bukan yang paling besar.<br>
<img width="579" height="175" alt="image" src="https://github.com/user-attachments/assets/4c894c99-d55c-41a8-86f7-d16c569d3442" /><br>
Yang paling pendek. Ambil data sesuai role, kalau kosong kasih tau "belum ada data", kalau ada langsung dioper ke tampilkan_tabel. Karena filternya udah di ambil_data, admin otomatis liat semuanya dan user cuma liat punyanya sendiri tanpa perlu logika tambahan di sini.<br>
<img width="1002" height="622" alt="image" src="https://github.com/user-attachments/assets/82e374d9-67ef-4820-a678-4f6f1362a56e" /><br>
Alurnya: tabel ditampilin dulu biar user bisa liat ID-nya, pilih ID (0 buat batal), lalu pilih mau ngubah nama, target, atau uang terkumpul. Yang menarik ada di bagian akhir. Setelah apa pun yang diubah, program ngecek lagi apakah terkumpul jadi lebih gede dari target. Kasus ini gampang kejadian, misalnya target diturunin ke angka di bawah uang yang udah ada. Kalau kejadian, terkumpul dipotong jadi sama dengan target supaya persentasenya nggak lebih dari 100%.<br>
<img width="834" height="572" alt="image" src="https://github.com/user-attachments/assets/e9850d59-5294-4303-88e5-daa1745ca746" /><br>
Mirip ubah: tampilin tabel, pilih ID, bisa batal pakai 0. Bedanya sebelum beneran dihapus, nama tabungannya disimpen dulu ke variabel nama_hapus buat dipakai di pertanyaan konfirmasi, jadi yang muncul "Yakin mau hapus Liburan ke Bali?" dan bukan sekadar "yakin?". Jawaban cuma diterima kalau y atau n, yang lain diulang. Penghapusannya sendiri pakai del ke dictionary.<br>
<img width="886" height="799" alt="image" src="https://github.com/user-attachments/assets/bd17d89f-a7d6-4f28-81a0-eaf4558c6be3" /><br>
Ini fitur "nabung" yang jadi pembeda dari CRUD biasa. Setelah milih tabungan, program ngitung sisa (target dikurang terkumpul). Kalau sisanya udah nol, langsung dikasih tau targetnya tercapai dan nggak perlu setor lagi. Kalau belum, sisa ditampilin biar user tau butuh berapa lagi, terus minta jumlah setoran minimal 1 rupiah. Kalau setorannya lebih dari sisa, jumlahnya dipotong jadi pas sama sisa. Terakhir, kalau setoran ini bikin terkumpul pas sama dengan target, muncul ucapan selamat. Fitur ini dipake di menu user, sedangkan admin nggak punya menu setor karena tugasnya ngatur data.<br>
<br>
Fungsi khusus admin<br>
<img width="837" height="264" alt="image" src="https://github.com/user-attachments/assets/64cb315a-5e0d-4c4d-a45e-b2dcb996ac45" /><br>
Cuma ada di menu admin. Tiap akun di users di-loop, terus buat masing-masing dihitung ada berapa tabungan yang pemilik-nya cocok. Jadi ada loop di dalam loop: yang luar muter akun, yang dalam muter semua tabungan sambil nambah counter. Hasilnya jadi tabel berisi username, role, dan jumlah tabungannya. Berguna buat admin yang pengen tau siapa aja yang udah kedaftar dan siapa yang udah mulai nabung.<br>
Menu dan program utama<br>
<img width="844" height="787" alt="image" src="https://github.com/user-attachments/assets/a7a25ce9-d45b-4cf2-8dfd-6c1755541e36" /><br>
Menu admin punya enam pilihan: tambah, tampilkan semua, ubah, hapus, lihat pengguna, dan logout. Struktur loop-nya: bersihin layar, tampilin judul plus kutipan, minta pilihan, jalanin fungsi yang cocok. Setelah fungsi selesai ada input("Tekan Enter untuk lanjut...") supaya hasilnya nggak langsung kehapus pas layar dibersihin di putaran berikutnya. Pilihan 6 (logout) jatuh ke else, di situ loop dihentikan pakai break dan program balik ke menu awal. Perhatiin juga kalau role "admin" dikirim manual ke tiap fungsi, itu yang bikin ambil_data ngasih semua data.<br>
<img width="802" height="655" alt="image" src="https://github.com/user-attachments/assets/c0f2c752-7b8c-4cc0-97f0-01e240620367" /><br>
Konsepnya sama persis kayak menu admin, cuma lebih ringkas: empat pilihan (tambah tabungan, lihat tabungan saya, menabung, logout). User biasa sengaja nggak dikasih menu ubah dan hapus. Mereka cuma bisa nambah dan nyetor, dan datanya yang keliatan cuma punya sendiri.<br>
<img width="728" height="610" alt="image" src="https://github.com/user-attachments/assets/79bd8053-d711-49c3-b620-88f28e8fd3f5" /><br>
Ini loop paling luar dan titik mulai program. Kalau pilih Login, hasil login() dicek: string kosong berarti gagal 3 kali (balik ke menu awal), kalau ada isinya dicek rolenya di users dan diarahin ke menu_admin atau menu_user. Pas user logout dan fungsi menu-nya selesai, alur otomatis balik ke atas loop ini dan menu awal muncul lagi. Kalau pilih Register ya manggil register(). Program baru berhenti pas milih Keluar, di mana break mutus loop terluar ini.<br>
Dokumentasi output<br>
<br>
Bagian ini hasil run MINPRO_DDP2.py dari awal sampai akhir (direkam pakai terminal). Skenarionya: daftar akun baru, login, nambah satu tabungan impian, nyoba nabung/setor, terus login sebagai admin buat ngecek semua data dari sisi admin.<br>
<br>
Pas daftar akun baru dan login, kelihatan password-nya kesembunyi jadi bintang-bintang berkat pwinput:<br>
<img width="543" height="394" alt="image" src="https://github.com/user-attachments/assets/904df197-c825-4eb1-a125-1f1fc57f9720" /><br>
Lanjut ke menu user buat nambah tabungan. Di isian nama sempet dicoba enter kosong dulu buat ngecek validasinya, dan programnya nolak lalu minta input lagi:<br>
<img width="766" height="394" alt="image" src="https://github.com/user-attachments/assets/f6e0799e-97b2-40de-a6ed-59f14ead2411" /><br>
Abis itu dicek lewat menu "Lihat Tabungan Saya", progress-nya kehitung otomatis<br>
<img width="769" height="363" alt="image" src="https://github.com/user-attachments/assets/477552fc-cf5a-4111-ad1c-ef60cc177e7d" /><br>
Terus nyoba fitur nabung, setor 2 juta lagi lewat menu "Menabung (Setor Uang)":<br>
<img width="742" height="455" alt="image" src="https://github.com/user-attachments/assets/cb1d2588-cc05-4709-b3bb-50af90d4f1e5" /><br>
Setelah disetor, progress-nya naik jadi 70%:<br>
<img width="767" height="364" alt="image" src="https://github.com/user-attachments/assets/9ee956a2-eb6f-43ee-97da-263bfaefb97b" /><br>
Terakhir, abis logout terus login lagi pakai akun admin, dicek menu "Lihat Daftar Pengguna" (ngitung jumlah tabungan tiap akun) sama "Tampilkan Semua Data" (admin bisa liat punya semua orang, bukan cuma punya sendiri):<br>
<img width="790" height="468" alt="image" src="https://github.com/user-attachments/assets/0ad0e929-f0de-4bdf-81d2-4adbeb3633fc" /><br>
<img width="840" height="485" alt="image" src="https://github.com/user-attachments/assets/8ce4994c-c57a-4753-9696-75cd5201512e" /><br>
Dan terakhir keluar dari program lewat menu awal:<br>
<img width="701" height="222" alt="image" src="https://github.com/user-attachments/assets/7603eac7-7f08-4957-a9be-ecb498001680" /><br>
Dari skenario ini kelihatan semua fitur utamanya jalan sesuai rencana: register, login, tambah, lihat, setor, lihat daftar pengguna, sampai lihat semua data dari sisi admin.Terimakasih 
