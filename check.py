import requests, os

headers = {
    "Authorization": f"Bearer {os.getenv('NVIDIA_API_KEY')}"
}

r = requests.get(
    "https://integrate.api.nvidia.com/v1/models",
    headers=headers
)

print(r.json())
