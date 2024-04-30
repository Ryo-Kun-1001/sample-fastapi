### ビルド (初回)

```
docker compose build
```

### 起動

```
docker compose up -d
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
