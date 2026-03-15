def detect_content_type(key: str):

    if key.endswith(".json"):
        return "application/json", None

    if key.endswith(".json.gz"):
        return "application/json", "gzip"

    if key.endswith(".parquet"):
        return "application/octet-stream", None

    return None, None