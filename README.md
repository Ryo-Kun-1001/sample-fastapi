### ビルド (初回)

```
docker compose build
```

### コンテナ起動

DBとテスト用DBの起動

```
docker compose up -d db test_db
```

### サーバー系の起動

APIサーバー起動

```
docker compose up fastapi
```

テスト実行

```
docker-compose run -e TESTING=True --rm fastapi pytest
```

print出力したい場合はsオプションをつける

```
docker-compose run -e TESTING=True --rm fastapi pytest -s
```

stremlitの起動

```
streamlit run streamlit.py
```
