import requests
import base64
import json
PREFIX_NAME = "FIREOWL"   # ← اسم دلخواه تو اینجاست

SOURCE_URLS = [
    "https://github.com/Delta-Kronecker/V2ray-Config/raw/refs/heads/main/config/batches/v2ray/batch_001.txt"
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

    elif line.startswith("vless://"):
        try:
            base = line.split("#")[0]
            output.append(base + "#" + f"{PREFIX_NAME}-{counter}")
            counter += 1
        except:
            continue

    elif line.startswith("ss://"):
        try:
            base = line.split("#")[0]
            output.append(base + "#" + f"{PREFIX_NAME}-{counter}")
            counter += 1
        except:
            continue

    elif line.startswith("trojan://"):
        try:
            base = line.split("#")[0]
            output.append(base + "#" + f"{PREFIX_NAME}-{counter}")
            counter += 1
        except:
            continue

    else:
        output.append(line)


with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(output))






