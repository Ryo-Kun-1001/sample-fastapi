### ビルド (初回)

```
docker compose build
```

### 起動

全部起動

```
docker compose up -d
```

stremlitの起動

```
streamlit run streamlit.py
```

### ダウン

全部ダウン

```
docker compse down
```

### DB内のデータをリフレッシュ

ボリュームを削除した上でダウンさせて再起動

```
docker compse down -v
```

```
docker compose up -d
```

### テスト実行

```
docker compose run -e TESTING=True --rm fastapi pytest
```

print出力したい場合はsオプションをつける

```
docker compose run -e TESTING=True --rm fastapi pytest -s
```
