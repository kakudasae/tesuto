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
        'lucky_color': 
