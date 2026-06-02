import streamlit as st

st.set_page_config(
    page_title="Matematika Geometry", 
    page_icon="👾"
)

with st.sidebar:
    col1, col2, col3 = st.columns([0.2, 3.6, 0.2])
    with col2:
        st.image("Gemini_Generated_Image_ykkt82ykkt82ykkt-removebg-preview.png", use_container_width=True)
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilih Bangun Datar", ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran", "Jajar Genjang"])
    st.caption("Dibuat Dengan 🫸🏼**Deka Fajar Bayu Anggoro, Kelas X PPLG 1**🫷🏼")


match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung Luas dan Keliling Persegi")
        sisi = st.number_input("Masukkan Sisi Persegi", min_value=0.0)
        if st.button("Hitung"):
            luas = sisi * sisi
            keliling = 4 * sisi
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung Luas dan Keliling Persegi Panjang")
        panjang = st.number_input("Masukkan Panjang Persegi Panjang", min_value=0.0)
        lebar = st.number_input("Masukkan Lebar Persegi Panjang", min_value=0.0)
        if st.button("Hitung"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung Luas dan Keliling Segitiga")
        alas = st.number_input("Masukkan Alas Segitiga", min_value=0.0)
        tinggi = st.number_input("Masukkan Tinggi Segitiga", min_value=0.0)
        sisi1 = st.number_input("Masukkan Sisi 1", min_value=0.0)
        sisi2 = st.number_input("Masukkan Sisi 2", min_value=0.0)
        sisi3 = st.number_input("Masukkan Sisi 3", min_value=0.0)
        if st.button("Hitung"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung Luas dan Keliling Lingkaran")
        jari_jari = st.number_input("Masukkan Jari-jari Lingkaran", min_value=0.0)
        if st.button("Hitung"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung Luas dan Keliling Jajar Genjang")
        alas_jg = st.number_input("Masukkan Alas Jajar Genjang", min_value=0.0)
        tinggi_jg = st.number_input("Masukkan Tinggi Jajar Genjang", min_value=0.0)
        sisi_miring = st.number_input("Masukkan Sisi Miring (untuk keliling)", min_value=0.0)
        if st.button("Hitung"):
            luas = alas_jg * tinggi_jg
            keliling = 2 * (alas_jg + sisi_miring)
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case _:
        st.error("Terjadi Kesalahan")
