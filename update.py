import requests
import base64
import json

SOURCE_URLS = [
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no1.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no2.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no3.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no4.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no5.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no6.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no7.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no8.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no9.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no10.txt"
]

OUTPUT_FILE = "sub.txt"
PREFIX_NAME = "FIREOWL"   # 

all_lines = []
counter = 1

for url in SOURCE_URLS:
    try:
        resp = requests.get(url, timeout=15)
        lines = resp.text.strip().splitlines()
        all_lines.extend(lines)
    except:
        continue

output = []

for line in all_lines:
    if line.startswith("vmess://"):
        try:
            raw = base64.b64decode(line[8:] + "==").decode()
            data = json.loads(raw)
            data["ps"] = f"{PREFIX_NAME}-{counter}"
            new_raw = base64.b64encode(json.dumps(data).encode()).decode()
            output.append("vmess://" + new_raw)
            counter += 1
        except:
            continue
    else:
        output.append(line)

with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(output))
