"""
Applikasi deteksi gempa terkini
Modularisasi dengan function
"""
import deteksiGempa

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = deteksiGempa.ekstraksi_data()
    deteksiGempa.tampilkan_data(result)
