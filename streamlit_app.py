import streamlit as st
from datetime import datetime

# 星座の期間と対応する星座名を辞書で定義
zodiac_dates = [
    ((1, 20), (2, 18), "みずがめ座"),
    ((2, 19), (3, 20), "うお座"),
    ((3, 21), (4, 19), "おひつじ座"),
    ((4, 20), (5, 20), "おうし座"),
    ((5, 21), (6, 20), "ふたご座"),
    ((6, 21), (7, 22), "かに座"),
    ((7, 23), (8, 22), "しし座"),
    ((8, 23), (9, 22), "おとめ座"),
    ((9, 23), (10, 22), "てんびん座"),
    ((10, 23), (11, 21), "さそり座"),
    ((11, 22), (12, 21), "いて座"),
    ((12, 22), (1, 19), "やぎ座"),
]

# ラッキーアイテム、ラッキーカラー、相性の良い星座、相性の悪い星座を辞書で定義
fortune_data = {
    "みずがめ座": {"lucky_item": "時計", "lucky_color": "青", "good_match": "ふたご座", "bad_match": "おうし座"},
    "うお座": {"lucky_item": "絵の具", "lucky_color": "緑", "good_match": "かに座", "bad_match": "おひつじ座"},
    "おひつじ座": {"lucky_item": "財布", "lucky_color": "赤", "good_match": "しし座", "bad_match": "うお座"},
    "おうし座": {"lucky_item": "ブレスレット", "lucky_color": "ピンク", "good_match": "おとめ座", "bad_match": "みずがめ座"},
    "ふたご座": {"lucky_item": "ノート", "lucky_color": "黄色", "good_match": "みずがめ座", "bad_match": "おひつじ座"},
    "かに座": {"lucky_item": "写真立て", "lucky_color": "白", "good_match": "うお座", "bad_match": "いて座"},
    "しし座": {"lucky_item": "アクセサリー", "lucky_color": "金", "good_match": "おひつじ座", "bad_match": "おとめ座"},
    "おとめ座": {"lucky_item": "ペン", "lucky_color": "緑", "good_match": "おうし座", "bad_match": "しし座"},
    "てんびん座": {"lucky_item": "鏡", "lucky_color": "ピンク", "good_match": "さそり座", "bad_match": "おとめ座"},
    "さそり座": {"lucky_item": "鍵", "lucky_color": "黒", "good_match": "てんびん座", "bad_match": "ふたご座"},
    "いて座": {"lucky_item": "地図", "lucky_color": "紫", "good_match": "おひつじ座", "bad_match": "かに座"},
    "やぎ座": {"lucky_item": "ペンケース", "lucky_color": "茶", "good_match": "おうし座", "bad_match": "ふたご座"},
}

# 星座を計算する関数
def get_zodiac(birthdate):
    month = birthdate.month
    day = birthdate.day
    for start, end, zodiac in zodiac_dates:
        start_date = datetime(birthdate.year, start[0], start[1])
        end_date = datetime(birthdate.year, end[0], end[1])
        if start_date <= birthdate <= end_date or (
            start_date.month == 12 and end_date.month == 1 and birthdate.month == 1):
            return zodiac
    return None

# Streamlitでアプリを作成
st.title("星座占いアプリ")

# 生年月日を入力してもらう
birthdate_input = st.date_input("生年月日を入力してください", min_value=datetime(1900, 1, 1), max_value=datetime(2024, 12, 31))

# ユーザーの生年月日を基に星座を判定
birthdate = datetime.strptime(str(birthdate_input), "%Y-%m-%d")
zodiac = get_zodiac(birthdate)

if zodiac:
    st.write(f"あなたの星座は「{zodiac}」です。")

    # 運勢情報を表示
    st.write(f"ラッキーアイテム: {fortune_data[zodiac]['lucky_item']}")
    st.write(f"ラッキーカラー: {fortune_data[zodiac]['lucky_color']}")
    st.write(f"相性のいい星座: {fortune_data[zodiac]['good_match']}")
    st.write(f"相性の悪い星座: {fortune_data[zodiac]['bad_match']}")
else:
    st.write("不正な日付です。再度入力してください。")
