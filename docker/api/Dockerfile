# Pythonの公式イメージをベースに使用
FROM python:3.11-slim

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のファイルをコピー
COPY ./docker/api/requirements.txt .

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースをコピー
COPY ./api /app

# コンテナの起動時に実行するコマンド
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
