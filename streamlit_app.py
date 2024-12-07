import streamlit as st
from datetime import datetime

# 星座に関する情報を定義
horoscopes = {
    "おひつじ座": {
        "dates": [(3, 21), (4, 19)],
        "fortune": "今日の運勢は非常に良好です。新しい挑戦に最適な日！",
        "lucky_item": "赤い財布",
        "lucky_color": "赤",
        "good_match": ["しし座", "いて座"],
        "bad_match": ["おうし座", "やぎ座"]
    },
    "おうし座": {
        "dates": [(4, 20), (5, 20)],
        "fortune": "今日は冷静に物事を考え、慎重に行動することが大切です。",
        "lucky_item": "緑の花",
        "lucky_color": "緑",
        "good_match": ["おとめ座", "やぎ座"],
        "bad_match": ["おひつじ座", "みずがめ座"]
    },
    "ふたご座": {
        "dates": [(5, 21), (6, 20)],
        "fortune": "今日はコミュニケーションが活発になり、新しい友達と出会えるかもしれません。",
        "lucky_item": "黄色い本",
        "lucky_color": "黄色",
        "good_match": ["てんびん座", "みずがめ座"],
        "bad_match": ["おうし座", "おとめ座"]
    },
    "かに座": {
        "dates": [(6, 21), (7, 22)],
        "fortune": "感情が高まりやすい一日。心を落ち着けて過ごしましょう。",
        "lucky_item": "シルバーのアクセサリー",
        "lucky_color": "シルバー",
        "good_match": ["おとめ座", "さそり座"],
        "bad_match": ["おひつじ座", "てんびん座"]
    },
    "しし座": {
        "dates": [(7, 23), (8, 22)],
        "fortune": "自信を持って行動することで、良い結果を得ることができるでしょう。",
        "lucky_item": "金色のリング",
        "lucky_color": "金",
        "good_match": ["おひつじ座", "いて座"],
        "bad_match": ["おうし座", "おとめ座"]
    },
    "おとめ座": {
        "dates": [(8, 23), (9, 22)],
        "fortune": "細かいことに気を配ることで、予期しないラッキーが訪れる日。",
        "lucky_item": "青いペン",
        "lucky_color": "青",
        "good_match": ["おうし座", "かに座"],
        "bad_match": ["ふたご座", "さそり座"]
    },
    "てんびん座": {
        "dates": [(9, 23), (10, 22)],
        "fortune": "バランスを取ることが鍵。人との調和を大切に。",
        "lucky_item": "ピンクのバッグ",
        "lucky_color": "ピンク",
        "good_match": ["ふたご座", "みずがめ座"],
        "bad_match": ["おうし座", "おとめ座"]
    },
    "さそり座": {
        "dates": [(10, 23), (11, 21)],
        "fortune": "感情的になりすぎず冷静な判断が求められる日。",
        "lucky_item": "黒い靴",
        "lucky_color": "黒",
        "good_match": ["かに座", "おとめ座"],
        "bad_match": ["しし座", "おひつじ座"]
    },
    "いて座": {
        "dates": [(11, 22), (12, 21)],
        "fortune": "冒険心が芽生える日。新しいことにチャレンジしてみましょう。",
        "lucky_item": "紫のネクタイ",
        "lucky_color": "紫",
        "good_match": ["おひつじ座", "しし座"],
        "bad_match": ["おうし座", "さそり座"]
    },
    "やぎ座": {
        "dates": [(12, 22), (1, 19)],
        "fortune": "堅実な行動が吉。焦らず計画的に進めることが大切。",
        "lucky_item": "黒い手帳",
        "lucky_color": "黒",
        "good_match": ["おうし座", "おとめ座"],
        "bad_match": ["おひつじ座", "ふたご座"]
    },
    "みずがめ座": {
        "dates": [(1, 20), (2, 18)],
        "fortune": "独創的なアイデアが浮かびやすい日。柔軟な思考を活かしましょう。",
        "lucky_item": "銀のペンダント",
        "lucky_color": "銀",
        "good_match": ["ふたご座", "てんびん座"],
        "bad_match": ["おうし座", "さそり座"]
    },
    "うお座": {
        "dates": [(2, 19), (3, 20)],
        "fortune": "直感が冴える一日。自分の感覚に従って行動すると吉。",
        "lucky_item": "白い花束",
        "lucky_color": "白",
        "good_match": ["かに座", "さそり座"],
        "bad_match": ["しし座", "おひつじ座"]
    }
}

# 生年月日から星座を取得する関数
def get_zodiac_sign(birthdate):
    month = birthdate.month
    day = birthdate.day

    for sign, info in horoscopes.items():
        start_date, end_date = info["dates"]
        if (month == start_date[0] and day >= start_date[1]) or (month == end_date[0] and day <= end_date[1]):
            return sign
    return None

# Streamlit アプリケーションのUI
st.title("星座占いアプリ")

# 生年月日の入力
birthdate = st.date_input("生年月日を入力してください")
if birthdate:
    # 星座を取得
    zodiac = get_zodiac_sign(birthdate)
    if zodiac:
        st.write(f"あなたの星座は「{zodiac}」です。")

        # 星座の運勢、ラッキーアイテム、ラッキーカラー、相性を表示
        st.write(f"運勢: {horoscopes[zodiac]['fortune']}")
        st.write(f"ラッキーアイテム: {horoscopes[zodiac]['lucky_item']}")
        st.write(f"ラッキーカラー: {horoscopes[zodiac]['lucky_color']}")
        st.write(f"相性のいい星座: {', '.join(horoscopes[zodiac]['good_match'])}")
        st.write(f"相性の悪い星座: {', '.join(horoscopes[zodiac]['bad_match'])}")
    else:
        st.write("星座を計算できませんでした。")
