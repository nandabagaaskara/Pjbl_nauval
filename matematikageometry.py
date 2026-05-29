import streamlit as st
st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="📐"
)
with st.sidebar:
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.image("mtk.jpg")
        
        st.title("Bangun Datar")
        pilihan = st.selectbox("Pilih Bangun Datar",["Persegi","Persegi Panjang","Segitiga","Lingkaran", "Trapesium"])
        st.caption("Aplikasi ini dibuat oleh ***Nauval***")
if pilihan == "Persegi":
    st.title("Persegi")
    st.markdown("Menghitung luas dan keliling persegi")
    sisi = st.number_input("Masukkan panjang sisi", 0)
    if st.button("Hitung", type="primary"):
        luas = sisi * sisi
        keliling = 4 * sisi
        st.write(f"Luas Persegi: {luas}")
        st.write(f"Keliling Persegi: {keliling}")
        st.success(f"Perhitungan berhasil! Luasnya {luas} dan kelilingnya {keliling}")
        col1 , col2 , col3 = st.columns([1,2,1])
        with col1:
            st.metric("Luas", value=luas, border =True)
        with col2:
            st.metric("Keliling", value=keliling, border =True)
        st.balloons()
elif pilihan == "Persegi Panjang":
    st.title("Persegi Panjang")
    st.markdown("Menghitung luas dan keliling persegi panjang")
    panjang = st.number_input("Masukkan panjang", 0)
    lebar = st.number_input("Masukkan lebar", 0)
    if st.button("Hitung", type="primary"):
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        st.write(f"Luas Persegi Panjang: {luas}")
        st.write(f"Keliling Persegi Panjang: {keliling}")
        st.success(f"Perhitungan berhasil! Luasnya {luas} dan kelilingnya {keliling}")
        col1 , col2 , col3 = st.columns([1,2,1])
        with col1:
            st.metric("Luas", value=luas, border =True)
        with col2:
            st.metric("Keliling", value=keliling, border =True)
        st.balloons()
elif pilihan == "Segitiga":
    st.title("Segitiga")
    st.markdown("Menghitung luas dan keliling segitiga")
    alas = st.number_input("Masukkan panjang alas", 0)
    tinggi = st.number_input("Masukkan tinggi", 0)
    sisi1 = st.number_input("Masukkan panjang sisi 1", 0)
    sisi2 = st.number_input("Masukkan panjang sisi 2", 0)
    sisi3 = st.number_input("Masukkan panjang sisi 3", 0)
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    if st.button("Hitung", type="primary"):
        st.write(f"Luas Segitiga: {luas}")
        st.write(f"Keliling Segitiga: {keliling}")
        st.success(f"Perhitungan berhasil! Luasnya {luas:.2f} dan kelilingnya {keliling:.2f}")
        col1 , col2 , col3 = st.columns([1,2,1])
        with col1:
            st.metric("Luas", value=luas, border =True)
        with col2:
            st.metric("Keliling", value=keliling, border =True)
        st.snow()
elif pilihan == "Lingkaran":
    st.title("Lingkaran")
    st.markdown("Menghitung luas dan keliling lingkaran")
    jari_jari = st.number_input("Masukkan panjang jari-jari", 0)
    if st.button("Hitung", type="primary"):
        luas = 3.14 * jari_jari * jari_jari
        keliling = 2 * 3.14 * jari_jari
        st.write(f"Luas Lingkaran: {luas}")
        st.write(f"Keliling Lingkaran: {keliling}")
        st.success(f"Perhitungan berhasil! Luasnya {luas:.2f} dan kelilingnya {keliling:.2f}")
        col1 , col2 , col3 = st.columns([1,2,1])
        with col1:
            st.metric("Luas", value=luas, border =True)
        with col2:
            st.metric("Keliling", value=keliling, border =True)
        st.snow()
elif pilihan == "Trapesium":
        st.title("Trepesium")
        st.markdown("Menghitung luas dan keliling trapesium")
        st.title("Trapesium")
        st.markdown("Menghitung luas dan keliling trapesium")
        alas1 = st.number_input("Masukkan Alas 1")
        alas2 = st.number_input("Masukkan Alas 2")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")
        sisi4 = st.number_input("Masukkan Sisi 4")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * (alas1 + alas2) * tinggi
            keliling = sisi1 + sisi2 + sisi3 + sisi4
        st.write(f"Luas Lingkaran: {luas}")
        st.write(f"Keliling Lingkaran: {keliling}")
        st.success(f"Perhitungan berhasil! Luasnya {luas:.2f} dan kelilingnya {keliling:.2f}")
        col1 , col2 , col3 = st.columns([1,2,1])
        with col1:
            st.metric("Luas", value=luas, border =True)
        with col2:
            st.metric("Keliling", value=keliling, border =True)
        st.snow()
            
        
        

    
        
        

    
