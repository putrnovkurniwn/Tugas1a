from collections import deque

class SistemAkademik:
    def __init__(self):
        # 1. Penyimpanan berurutan menggunakan Array/List
        self.data_mahasiswa = []
        
        # 2. Fitur Undo menggunakan Stack (LIFO)
        self.riwayat_undo = []
        
        # 3. Antrean pengolahan data menggunakan Queue (FIFO)
        self.antrean = deque()
        
        # 4. Pencarian berdasarkan key (NIM) menggunakan Hash Table/Dictionary
        self.data_pencarian = {}

    # --- Implementasi 1: Penyimpanan Berurutan (Array) ---
    def tambah_data_berurutan(self, nama):
        self.data_mahasiswa.append(nama)
        print(f"[Array] '{nama}' ditambahkan ke urutan.")

    # --- Implementasi 2: Fitur Undo (Stack) ---
    def lakukan_aksi(self, aksi):
        self.riwayat_undo.append(aksi)
        print(f"[Stack] Aksi '{aksi}' dilakukan dan disimpan di riwayat.")

    def undo_aksi(self):
        if self.riwayat_undo:
            aksi_terakhir = self.riwayat_undo.pop()
            print(f"[Stack] UNDO: Membatalkan aksi '{aksi_terakhir}'.")
        else:
            print("[Stack] Tidak ada aksi untuk di-undo.")

    # --- Implementasi 3: Antrean Pengolahan (Queue) ---
    def tambah_antrean(self, nama):
        self.antrean.append(nama)
        print(f"[Queue] '{nama}' masuk ke dalam antrean.")

    def proses_antrean(self):
        if self.antrean:
            diproses = self.antrean.popleft()
            print(f"[Queue] Memproses antrean milik: '{diproses}'.")
        else:
            print("[Queue] Antrean kosong.")

    # --- Implementasi 4: Pencarian berdasarkan Key (Hash Table) ---
    def simpan_dengan_key(self, nim, nama):
        self.data_pencarian[nim] = nama
        print(f"[Hash Table] Data NIM {nim} ({nama}) berhasil disimpan.")

    def cari_dengan_key(self, nim):
        hasil = self.data_pencarian.get(nim, "Data tidak ditemukan")
        print(f"[Hash Table] Pencarian NIM {nim}: {hasil}")


# ==========================================
# SIMULASI PENGGUNAAN KODE
# ==========================================
if __name__ == "__main__":
    sistem = SistemAkademik()
    print("=== SIMULASI SISTEM AKADEMIK ===\n")

    # 1. Array
    sistem.tambah_data_berurutan("Putra Nova")
    sistem.tambah_data_berurutan("Budi Santoso")
    
    print("-" * 30)
    # 2. Stack (Undo)
    sistem.lakukan_aksi("Hapus Data Budi")
    sistem.lakukan_aksi("Ubah Nilai Putra")
    sistem.undo_aksi() # Membatalkan ubah nilai
    
    print("-" * 30)
    # 3. Queue (Antrean)
    sistem.tambah_antrean("Putra Nova (Daftar Matkul)")
    sistem.tambah_antrean("Budi (Bayar UKT)")
    sistem.proses_antrean() # Memproses Putra duluan
    
    print("-" * 30)
    # 4. Hash Table (Pencarian Instan)
    sistem.simpan_dengan_key("12345", "Putra Nova Kurniawan")
    sistem.cari_dengan_key("12345")