# ベースイメージを指定
FROM python:3.11-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# libgd3は個別にインストールしないと、依存関係かイメージビルドが失敗することがある
RUN apt-get update && apt-get install -y libgd3

# 作業ディレクトリの設定
WORKDIR /app

# 依存ファイルをコピー
COPY ./docker/api/requirements.txt .

# 依存パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY ./api /app/api

# コンテナ起動時に実行するコマンド
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
