import streamlit as st
import datetime

# 星座のデータ（ラッキーアイテムを理科的なアイテムに変更）
zodiac_data = {
    'おひつじ座': {
        'dates': [(3, 21), (4, 19)],
        'lucky_item': '顕微鏡',
        'lucky_color': '赤',
        'compatible_zodiac': ['おうし座', 'しし座', 'いて座'],
        'incompatible_zodiac': ['てんびん座', 'やぎ座']
    },
    'おうし座': {
        'dates': [(4, 20), (5, 20)],
        'lucky_item': '化学実験キット',
        'lucky_color': '緑',
        'compatible_zodiac': ['おひつじ座', 'おとめ座', 'やぎ座'],
        'incompatible_zodiac': ['みずがめ座', 'しし座']
    },
    'ふたご座': {
        'dates': [(5, 21), (6, 20)],
        'lucky_item': '元素記号の板',
        'lucky_color': '黄色',
        'compatible_zodiac': ['てんびん座', 'みずがめ座', 'おひつじ座'],
        'incompatible_zodiac': ['おとめ座', 'さそり座']
    },
    'かに座': {
        'dates': [(6, 21), (7, 22)],
        'lucky_item': 'テストチューブ',
        'lucky_color': '白',
        'compatible_zodiac': ['おうし座', 'おとめ座', 'さそり座'],
        'incompatible_zodiac': ['おひつじ座', 'てんびん座']
    },
    'しし座': {
        'dates': [(7, 23), (8, 22)],
        'lucky_item': '天体望遠鏡',
        'lucky_color': '金',
        'compatible_zodiac': ['おひつじ座', 'おとめ座', 'いて座'],
        'incompatible_zodiac': ['おうし座', 'さそり座']
    },
    'おとめ座': {
        'dates': [(8, 23), (9, 22)],
        'lucky_item': '物理実験キット',
        'lucky_color': '青',
        'compatible_zodiac': ['おうし座', 'ふたご座', 'やぎ座'],
        'incompatible_zodiac': ['おひつじ座', 'さそり座']
    },
    'てんびん座': {
        'dates': [(9, 23), (10, 22)],
        'lucky_item': '化学反応実験セット',
        'lucky_color': 'ピンク',
        'compatible_zodiac': ['ふたご座', 'みずがめ座', 'かに座'],
        'incompatible_zodiac': ['おひつじ座', 'おうし座']
    },
    'さそり座': {
        'dates': [(10, 23), (11, 21)],
        'lucky_item': '分光器',
        'lucky_color': '黒',
        'compatible_zodiac': ['かに座', 'おとめ座', 'やぎ座'],
        'incompatible_zodiac': ['ふたご座', 'しし座']
    },
    'いて座': {
        'dates': [(11, 22), (12, 21)],
        'lucky_item': '星座モデル',
        'lucky_color': '紫',
        'compatible_zodiac': ['おひつじ座', 'しし座', 'おうし座'],
        'incompatible_zodiac': ['おとめ座', 'てんびん座']
    },
    'やぎ座': {
        'dates': [(12, 22), (1, 19)],
        'lucky_item': '地球儀',
        'lucky_color': '茶色',
        'compatible_zodiac': ['おうし座', 'おとめ座', 'さそり座'],
        'incompatible_zodiac': ['おひつじ座', 'ふたご座']
    },
    'みずがめ座': {
        'dates': [(1, 20), (2, 18)],
        'lucky_item': '水槽',
        'lucky_color': '青',
        'compatible_zodiac': ['ふたご座', 'てんびん座', 'おひつじ座'],
        'incompatible_zodiac': ['おうし座', 'さそり座']
    },
    'うお座': {
        'dates': [(2, 19), (3, 20)],
        'lucky_item': '水質測定キット',
        'lucky_color': '水色',
        'compatible_zodiac': ['かに座', 'おとめ座', 'さそり座'],
        'incompatible_zodiac': ['ふたご座', 'いて座']
    }
}

# 星座を決定する関数
def get_zodiac(month, day):
    for zodiac, data in zodiac_data.items():
        start_date, end_date = data['dates']
        start_month, start_day = start_date
        end_month, end_day = end_date

        # 開始月日から終了月日を範囲として星座を判定
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day) or (start_month < month < end_month):
            return zodiac
    return None

# アプリのUI作成
def main():
    st.title("星座占いアプリ")
    
    # 生年月日を入力
    st.write("あなたの生年月日を入力してください。")
    birth_date = st.date_input(
        "生年月日", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2024, 12, 31)
    )

    # 生年月日が入力された場合
    if birth_date:
        month = birth_date.month
        day = birth_date.day
        zodiac = get_zodiac(month, day)

        if zodiac:
            st.write(f"あなたの星座は「{zodiac}」です。")

            # 星座の運勢、ラッキーアイテム、ラッキーカラー、相性のいい星座、相性の悪い星座を表示
            st.write(f"ラッキーアイテム: {zodiac_data[zodiac]['lucky_item']}")
            st.write(f"ラッキーカラー: {zodiac_data[zodiac]['lucky_color']}")
            st.write(f"相性のいい星座: {', '.join(zodiac_data[zodiac]['compatible_zodiac'])}")
            st.write(f"相性の悪い星座: {', '.join(zodiac_data[zodiac]['incompatible_zodiac'])}")
        else:
            st.write("星座が判定できませんでした。もう一度確認してください。")
    
if __name__ == "__main__":
    main()
