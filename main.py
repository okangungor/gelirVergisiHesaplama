import streamlit as st

st.title("Gelir Vergisi Hesaplama")

vergiOran=[15,20,27,35,40]
vergiMatrah=[16500,40500,213300,958800]
gelir=[110000,230000,870000,3000000]

kznc=st.number_input("Kazancınızı Giriniz")
kznc=int(kznc)
st.button("Hesapla")

if kznc<=gelir[0]:
  matrah1=kznc/100*vergiOran[0]
  st.write("Vergi Matrahı :",kznc)
  st.write("Ödenecek Gelir Vergisi :",matrah1)
  st.write("Vergi Sonrası Net Gelir :",kznc-matrah1)
elif kznc<=gelir[1] and kznc > gelir[0]:
  matrah2=kznc-gelir[0]
  sonuc1=(matrah2/100*vergiOran[1])+vergiMatrah[0]
  st.write("Vergi Matrahı :",kznc)
  st.write("Ödenecek Gelir Vergisi :",sonuc1)
  st.write("Vergi Sonrası Net Gelir :",kznc-sonuc1)
elif kznc<=gelir[2] and kznc>gelir[1]:
  matrah3=kznc-gelir[1]
  sonuc2=(matrah3/100*vergiOran[2])+vergiMatrah[1]
  st.write("Vergi Matrahı :",kznc)
  st.write("Ödenecek Gelir Vergisi :",sonuc2)
  st.write("Vergi Sonrası Net Gelir :",kznc-sonuc2)
elif kznc<=gelir[3] and kznc>gelir[2]:
  matrah4=kznc-gelir[2]
  sonuc3=(matrah4/100*vergiOran[3])+vergiMatrah[2]
  st.write("Vergi Matrahı :",kznc)
  st.write("Ödenecek Gelir Vergisi :",sonuc3)
  st.write("Vergi Sonrası Net Gelir :",kznc-sonuc3)
elif kznc>gelir[3]:
  matrah5=kznc-gelir[3]
  sonuc4=(matrah5/100*vergiOran[4])+vergiMatrah[3]
  st.write("Vergi Matrahı :",kznc)
  st.write("Ödenecek Gelir Vergisi :",sonuc4)
  st.write("Vergi Sonrası Net Gelir :",kznc-sonuc4)
  st.balloons()
  st.image('https://media3.giphy.com/media/1216HpvhbzganS/100.webp?cid=790b7611ir8nf17u6rf5fb6lwv39x5v7f6jdvo217i6pdvg7&ep=v1_gifs_search&rid=100.webp&ct=g')