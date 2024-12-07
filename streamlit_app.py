import streamlit as st
import random

# 昼ご飯の候補となる料理リスト
lunch_options = [
    "カレーライス",
    "ラーメン",
    "お寿司",
    "サンドイッチ",
    "パスタ",
    "うどん",
    "丼物",
    "ハンバーガー",
    "天ぷら",
    "チキンライス"
]

# アプリのタイトル
st.title('昼ご飯を決めるアプリ')

# ランダムに昼ご飯を提案するボタン
if st.button('昼ご飯を決める！'):
    # ランダムに料理を選ぶ
    selected_lunch = random.choice(lunch_options)
    st.write(f'今日の昼ご飯は、**{selected_lunch}**に決まりました！')
else:
    st.write("上のボタンを押して、昼ご飯を決めてください。")
