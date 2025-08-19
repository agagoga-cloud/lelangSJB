
import streamlit as st
import pandas as pd

st.title("Aplikasi Input Jadwal Lelang dan Surat Laporan")

# Input form
with st.form("form_lelang"):
    tanggal = st.date_input("Tanggal Lelang")
    nama_barang = st.text_input("Nama Barang")
    jenis_barang = st.text_input("Jenis Barang")
    nilai_limit = st.number_input("Nilai Limit", min_value=0.0, format="%.2f")
    lokasi = st.text_input("Lokasi Lelang")
    nama_balai = st.text_input("Nama Balai Lelang")
    alamat_balai = st.text_input("Alamat Balai Lelang")
    nomor_surat = st.text_input("Nomor Surat Permohonan Lelang")
    submitted = st.form_submit_button("Tambahkan Data")

    if submitted:
        new_data = {
            "Tanggal Lelang": tanggal,
            "Nama Barang": nama_barang,
            "Jenis Barang": jenis_barang,
            "Nilai Limit": f"Rp {nilai_limit:,.2f}",
            "Lokasi Lelang": lokasi,
            "Nama Balai Lelang": nama_balai,
            "Alamat Balai Lelang": alamat_balai,
            "Nomor Surat Permohonan Lelang": nomor_surat
        }
        st.session_state.data.append(new_data)

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = []

# Display table
if st.session_state.data:
    st.subheader("Tabel Jadwal Lelang")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

    # Generate report
    st.subheader("Surat Laporan Jadwal Lelang")
    st.write("Kepada Yth.\nPanitia Lelang\nDi Tempat\n")
    st.write("Dengan ini kami sampaikan laporan jadwal lelang sebagai berikut:\n")

    for i, row in enumerate(st.session_state.data, start=1):
        st.write(f"{i}. Tanggal: {row['Tanggal Lelang']}, Barang: {row['Nama Barang']} ({row['Jenis Barang']}), "
                 f"Nilai Limit: {row['Nilai Limit']}, Lokasi: {row['Lokasi Lelang']}, "
                 f"Balai: {row['Nama Balai Lelang']}, Alamat: {row['Alamat Balai Lelang']}, "
                 f"Nomor Surat: {row['Nomor Surat Permohonan Lelang']}")

    st.write("\nDemikian laporan ini kami sampaikan untuk dapat digunakan sebagaimana mestinya.\n")
    st.write("Hormat kami,\nPanitia Lelang")
