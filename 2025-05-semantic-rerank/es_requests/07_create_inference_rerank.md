# �������N�p�� inference �̍쐬���N�G�X�g

�����ł́A Cohere �� rerank-v3.5 �𗘗p���܂��B

```
PUT _inference/rerank/cohere_rerank_v3pt5
{
  "service": "cohere",
  "service_settings": {
    "api_key": "<Cohere��API-KEY>",
    "model_id": "rerank-v3.5",
    "rate_limit": {
      "requests_per_minute": 10
    }
  },
  "task_settings": {
    "top_n": 10,
    "return_documents": true
  }
}
```

����́A�]���p�� Cohere �� API Key �𗘗p���邱�Ƃ�z�肵�Ă��邽�߁A

```
"rate_limit": {
  "requests_per_minute": 10
}
```

��ݒ肵�Ă��܂��B

�L���_�񂵂āA�{�Ԃŉ^�p����ꍇ�ɂ́A����������グ�Ă��������B
