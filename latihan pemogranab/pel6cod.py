jumlah_tiket = "4"
harga_tiket  = 25000

total_sementara = jumlah_tiket *2
print("Total sementara :", total_sementara)
#total sementara hasilnya 44 karena jumlah tiket diatas pake string " jadi kalo string meskipun dikali tapi tetep cuma dijejer
#dibawah diganti int jadi bisa jumlah normal

jumlah_tiket = int(jumlah_tiket)
total_akhir  = jumlah_tiket*harga_tiket
print("Total akhir :", total_akhir)