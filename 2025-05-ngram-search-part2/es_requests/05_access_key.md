# Access Key の作成

## 読み取り用 Access Key の作成

```
POST /_security/api_key
{
  "name": "medicine_read",
  "role_descriptors": {
    "medication_read": {
      "cluster": ["all"],
      "indices": [
        {
          "names": ["medicine*"],
          "privileges": ["read"]
        }
      ]
    }
  }
}
```

  "encoded": "aDdVOGhaWUJQX1Z1MEZYSDlzUDU6YmxsbGlPUjhFVUdXNEY1X01yRkdLQQ=="

  "encoded": "ek9yekU1WUJaSUZOcVRqS3Z2dU86bGwzVTZ1MGhTQ2FMOGM5YTdjWm4wZw=="  (for local (broken))

  