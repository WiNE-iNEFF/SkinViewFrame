import base64
from urllib.parse import quote_plus

with open("axolotl 49.png", "rb") as f:
	skin_base64 = base64.b64encode(f.read()).decode("utf-8")

data = f"data:image/png;base64,{skin_base64}"
quoted = quote_plus(data)
url = f"http://localhost:8000/skin.html?data={quoted}"
print(url)