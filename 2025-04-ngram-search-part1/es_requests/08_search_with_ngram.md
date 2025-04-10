# N-gramを利用した検索リクエスト

```
GET /ngram_sample_202504/_search
{
  "query": {
    "multi_match": {
      "fields": [ "content.ngram^5", "content" ],
       "query": "タイパ"
    }
  }
}
```

# min_score を指定した検索リクエスト

```
GET /ngram_sample_202504/_search
{
  "query": {
    "multi_match": {
      "fields": [ "content.ngram^5", "content" ],
       "query": "タイパ"
    }
  },
  "min_score": 5
}
```

