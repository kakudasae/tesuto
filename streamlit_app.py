import streamlit as st

# 星座の運勢データ（サンプル）
zodiac_info = {
    'おひつじざ': {
        'lucky_item': '赤いペン',
        'lucky_color': '赤',
        'good_match': ['ししざ', 'いてざ'],
        'bad_match': ['おうしざ', 'やぎざ'],
    },
    'おうしざ': {
        'lucky_item': '緑色の財布',
        'lucky_color': '緑',
        'good_match': ['おとめざ', 'かにざ'],
        'bad_match': ['おひつじざ', 'みずがめざ'],
    },
    'ふたござ': {
        'lucky_item': '本',
        'lucky_color': '黄色',
        'good_match': ['てんびんざ', 'みずがめざ'],
        'bad_match': ['おとめざ', 'うおざ'],
    },
    'かにざ': {
        'lucky_item': '白い花',
        'lucky_color': '白',
        'good_match': ['おうしざ', 'おとめざ'],
        'bad_match': ['おひつじざ', 'てんびんざ'],
    },
    'ししざ': {
        'lucky_item': '金のネックレス',
        'lucky_color': '金色',
        'good_match': ['おひつじざ', 'いてざ'],
        'bad_match': ['おうしざ', 'さそりざ'],
    },
    'おとめざ': {
        'lucky_item': 'メモ帳',
        'lucky_color': '青',
        'good_match': ['おうしざ', 'かにざ'],
        'bad_match': ['ふたござ', 'ししざ'],
    },
    'てんびんざ': {
        'lucky_item': '美しい花瓶',
        'lucky_color': 'ピンク',
        'good_match': ['ふたござ', 'みずがめざ'],
        'bad_match': ['かにざ', 'さそりざ'],
    },
    'さそりざ': {
        'lucky_item': '黒い財布',
        'lucky_color': '黒',
        'good_match': ['おひつじざ', 'おとめざ'],
        'bad_match': ['ししざ', 'てんびんざ'],
    },
    'いてざ': {
        'lucky_item': '遠足用のバッグ',
        'lucky_color': '青',
        'good_match': ['おひつじざ', 'ししざ'],
        'bad_match': ['おうしざ', 'うおざ'],
    },
    'やぎざ': {
        'lucky_item': 'シルバーの時計',
        'lucky_color': 'グレー',
        'good_match': ['おうしざ', 'おとめざ'],
        'bad_match': ['おひつじざ', 'ふたござ'],
    },
    'みずがめざ': {
        'lucky_item': '金のペン',
        'lucky_color': '水色',
        'good_match': ['ふたござ', 'てんびんざ'],
        'bad_match': ['おうしざ', 'さそりざ'],
    },
    'うおざ': {
        'lucky_item': '柔らかい毛布',
        'lucky_color': 'ピンク',
        'good_match': ['かにざ', 'おとめざ'],
        'bad_match': ['ふたござ', 'いてざ'],
    },
}

# Streamlitアプリのタイトル
st.title('星座占いアプリ')

# ユーザーに星座を選んでもらう
zodiac = st.selectbox('あなたの星座を選んでください（ひらがなで入力）', [
    'おひつじざ', 'おうしざ', 'ふたござ', 'かにざ', 'ししざ', 'おとめざ', 'てんびんざ', 'さそりざ', 'いてざ', 'やぎざ', 'みずがめざ', 'うおざ'])

# 選んだ星座の運勢情報を表示
info = zodiac_info[zodiac]
st.header(f'{zodiac} の運勢')

# ラッキーアイテムとラッキーカラー
st.subheader('ラッキーアイテムとラッキーカラー')
st.write(f'ラッキーアイテム: {info["lucky_item"]}')
st.write(f'ラッキーカラー: {info["lucky_color"]}')

# 相性のいい星座と相性の悪い星座
st.subheader('相性のいい星座と相性の悪い星座')
st.write(f'相性のいい星座: {", ".join(info["good_match"])}')
st.write(f'相性の悪い星座: {", ".join(info["bad_match"])}')

