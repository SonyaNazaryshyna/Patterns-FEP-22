from urllib.parse import urlencode, uses_query

def build_api_query(base_url: str, endpoint: str, params: dict = None) -> str:
    full_url = f"{base_url}/{endpoint}"

    if params:
        url_values = urlencode(params)
        full_url = f"{base_url}/{endpoint}?{url_values}"

    return full_url
