# ベースイメージとして公式のUbuntuイメージを使用
FROM ubuntu:latest

# メタデータの設定
LABEL maintainer="Your Name <your.email@example.com>"

# 環境変数の設定
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# 必要なパッケージのインストール
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

# アプリケーションコードをコピー
COPY ./src /app

# 作業ディレクトリの指定
WORKDIR /app

# Pythonライブラリのインストール
RUN pip3 install streamlit
RUN pip3 install pandas
RUN pip3 install Counter
RUN pip3 install nltk

# ポートの公開
EXPOSE 8501

# アプリケーションの実行（例: Streamlitアプリの場合）
CMD ["streamlit", "run", "csvkai_v2.py"]
