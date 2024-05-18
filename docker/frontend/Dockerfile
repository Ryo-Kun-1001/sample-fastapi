# ベースイメージとしてNode.jsを使用
FROM node:18

# 作業ディレクトリを設定
WORKDIR /app

# パッケージファイルをコピー
COPY frontend/package*.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY frontend .

# ビルド
RUN npm run build

# アプリケーションを公開するポート
EXPOSE 5173

# アプリケーションを実行
CMD ["npm", "run", "dev"]
