import streamlit as st
import random

st.title("✨ キラキラ星占い ✨")

st.write("あなたの星座をえらんでね！")

seiza = st.selectbox(
    "星座",
    ["おひつじ座 ♈", "おうし座 ♉", "ふたご座 ♊", "かに座 ♋",
     "しし座 ♌", "おとめ座 ♍", "てんびん座 ♎", "さそり座 ♏",
     "いて座 ♐", "やぎ座 ♑", "みずがめ座 ♒", "うお座 ♓"]
)

if st.button("今日の運勢を見る ⭐"):
    unsei = random.choice(["だいきち ✨✨✨", "きち ✨✨", "ちゅうきち ✨", "しょうきち 💫"])
    lucky_color = random.choice(["ピンク 💗", "きいろ 💛", "みずいろ 💙", "むらさき 💜", "しろ 🤍"])
    lucky_item = random.choice(["リボン 🎀", "ハート 💗", "ほし ⭐", "キラキラ ✨", "はな 🌸"])
    
    st.success(f"🌟 今日の運勢: {unsei}")
    st.info(f"🎨 ラッキーカラー: {lucky_color}")
    st.info(f"🍀 ラッキーアイテム: {lucky_item}")
    st.balloons()
