import streamlit as st
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# nltkのストップワードをダウンロード
nltk.download('stopwords')
nltk.download('punkt')

# Streamlitアプリの開始
st.title("CSVファイル解析アプリｖ4")

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

# 解析ボタンが押されたかどうかのチェック
if st.button("解析"):
    if uploaded_file is not None:
        # アップロードされたCSVファイルの読み込み
        df = pd.read_csv(uploaded_file)

        # CSVファイルの内容を表形式で表示
        st.write("CSVファイルの内容:")
        st.dataframe(df)

        # テキスト情報から頻出頻度ごとのキーワードを抽出
        text_data = ' '.join(df.apply(lambda x: ' '.join(map(str, x)), axis=1))  # すべての列を文字列に結合
        tokens = word_tokenize(text_data.lower())  # 小文字に変換してトークン化
        stop_words = set(stopwords.words('english'))  # 日本語のストップワードを使用
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

        # 頻出単語のカウント
        word_freq = Counter(filtered_tokens)

        # 上位30位までの頻出ワードランキングを取得
        top_words = word_freq.most_common(30)

        # データフレームに変換して表形式で表示
        top_words_df = pd.DataFrame(top_words, columns=['単語', '出現回数'])
        st.write("頻出ワードランキング:")
        st.dataframe(top_words_df)

    else:
        st.warning("CSVファイルがアップロードされていません。やりなおしてください")
