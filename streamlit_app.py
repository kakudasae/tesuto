import streamlit as st
from datetime import datetime

# 星座とその運勢、相性
zodiac_info = {
    "牡羊座": {
        "fortune": "今日は積極的に行動することが吉。新しい挑戦が運気を引き寄せます。",
        "good_match": ["獅子座", "射手座"],
        "bad_match": ["蟹座", "山羊座"]
    },
    "牡牛座": {
        "fortune": "安定が大事な一日。無理せず、穏やかな時間を過ごすと良いでしょう。",
        "good_match": ["乙女座", "山羊座"],
        "bad_match": ["獅子座", "水瓶座"]
    },
    "双子座": {
        "fortune": "社交的な一日。新しい人との出会いが期待できそうです。",
        "good_match": ["天秤座", "水瓶座"],
        "bad_match": ["魚座", "乙女座"]
    },
    "蟹座": {
        "fortune": "感情に振り回されがち。冷静に判断することが重要です。",
        "good_match": ["蠍座", "魚座"],
        "bad_match": ["牡羊座", "天秤座"]
    },
    "獅子座": {
        "fortune": "自信を持って行動することで運気が向上します。",
        "good_match": ["牡羊座", "射手座"],
        "bad_match": ["牡牛座", "蠍座"]
    },
    "乙女座": {
        "fortune": "細かい作業がうまく進みます。集中力が必要な一日。",
        "good_match": ["牡牛座", "山羊座"],
        "bad_match": ["双子座", "射手座"]
    },
    "天秤座": {
        "fortune": "バランスを大切にすることが運を引き寄せます。人間関係が重要。",
        "good_match": ["双子座", "水瓶座"],
        "bad_match": ["牡羊座", "蟹座"]
    },
    "蠍座": {
        "fortune": "直感が冴える一日。大切な決断をするには良いタイミングです。",
        "good_match": ["蟹座", "魚座"],
        "bad_match": ["獅子座", "双子座"]
    },
    "射手座": {
        "fortune": "冒険心が強くなる日。新しいことを始めるには良い時期です。",
        "good_match": ["牡羊座", "獅子座"],
        "bad_match": ["乙女座", "魚座"]
    },
    "山羊座": {
        "fortune": "地道な努力が実を結ぶ日。慎重に行動することが吉。",
        "good_match": ["牡牛座", "乙女座"],
        "bad_match": ["蟹座", "天秤座"]
    },
    "水瓶座": {
        "fortune": "独創的な考えが光る日。人と違う視点で物事を捉えることが大切です。",
        "good_match": ["双子座", "天秤座"],
        "bad_match": ["牡牛座", "蠍座"]
    },
    "魚座": {
        "fortune": "感受性が豊かな一日。リラックスすることが運を良くします。",
        "good_match": ["蟹座", "蠍座"],
        "bad_match": ["双子座", "射手座"]
    }
}

# 星座を決める関数
def get_zodiac(birthdate):
    zodiacs = [
        ("牡羊座", (3, 21), (4, 19)),
        ("牡牛座", (4, 20), (5, 20)),
        ("双子座", (5, 21), (6, 20)),
        ("蟹座", (6, 21), (7, 22)),
        ("獅子座", (7, 23), (8, 22)),
        ("乙女座", (8, 23), (9, 22)),
        ("天秤座", (9, 23), (10, 22)),
        ("蠍座", (10, 23), (11, 21)),
        ("射手座", (11, 22), (12, 21)),
        ("山羊座", (12, 22), (1, 19)),
        ("水瓶座", (1, 20), (2, 18)),
        ("魚座", (2, 19), (3, 20)),
    ]
    
    month, day = birthdate.month, birthdate.day
    for zodiac, start, end in zodiacs:
        start_month, start_day = start
        end_month, end_day = end
        if ((month == start_month and day >= start_day) or (month == end_month and day <= end_day)):
            return zodiac
    return None

# Streamlitアプリのメインコード
def main():
    st.title("星座占いアプリ")

    # ユーザーに生年月日を入力してもらう
    st.write("あなたの生年月日を入力してください。")
    birthdate = st.date_input("生年月日", min_value=datetime(1900, 1, 1))

    # 入力がある場合に星座を占う
    if birthdate:
        zodiac = get_zodiac(birthdate)
        if zodiac:
            st.write(f"あなたの星座は【{zodiac}】です。")
            st.write(f"運勢: {zodiac_info[zodiac]['fortune']}")
            st.write(f"相性の良い星座: {', '.join(zodiac_info[zodiac]['good_match'])}")
            st.write(f"相性の悪い星座: {', '.join(zodiac_info[zodiac]['bad_match'])}")
        else:
            st.write("不正な生年月日です。")

if __name__ == "__main__":
    main()
