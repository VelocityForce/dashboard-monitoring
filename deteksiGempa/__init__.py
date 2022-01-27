import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal : 22 Januari 2022
    Waktu : 15:34:38 WIB
    Magnitudo : 3.9
    Kedalaman : 10 km
    Lokasi : 7.49 LS - 107.31 BT
    Pusat_gempa : Pusat gempa berada di darat 57 km BaratDaya Kab-Bandung
    Diraskan : Dirasakan (Skala MMI): III Cidaun, III Cidora, III Cijayanti, III Rancabuaya, II Pamengpeuk, II Pakenjeng, II Bungbulang, II Cisompet, II Margaasih
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
        print(Exception)

    if content.status_code == 200:
        # print(content.text)
        soup = BeautifulSoup(content.text, "html.parser")
        print(soup.prettify())

        hasil = dict()
        hasil['Tanggal'] = "22 Januari 2022"
        hasil['Waktu'] = "15:34:38 WIB"
        hasil['Magnitudo'] = 4.0
        hasil['Kedalaman'] = "10 KM"
        hasil['Lokasi'] = {'LS': 7.49, 'BT': 107.31}
        hasil['Pusat'] = "Pusat gempa berada di darat 57 km BaratDaya Kab-Bandung"
        hasil['Dirasakan'] = "Dirasakan (Skala MMI): III Cidaun, III Cidora, III Cijayanti, III Rancabuaya, II Pamengpeuk, " \
                             "II Pakenjeng, II Bungbulang, II Cisompet, II Margaasih "
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Data tidak ditemukan")
        return

    print("Gempa terakhir bersarkan data BMKG")
    print(f"Tanggal     : {result['Tanggal']}")
    print(f"Waktu       : {result['Waktu']}")
    print(f"Magnitudo   : {result['Magnitudo']}")
    print(f"Kedalaman   : {result['Kedalaman']}")
    print(f"Lokasi      : {result['Lokasi']['LS']} LS, {result['Lokasi']['BT']}  BT")
    print(f"Pusat       : {result['Pusat']}")
    print(f"Dirasakan   : {result['Dirasakan']}")
