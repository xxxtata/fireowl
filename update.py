import requests
import base64
import json

SOURCE_URL = "اینجا_لینک_سورس_تو"
OUTPUT_FILE = "sub.txt"

resp = requests.get(SOURCE_URL, timeout=15)
lines = resp.text.strip().splitlines()

output = []
count = 1

for line in lines:
    if line.startswith("vmess://"):
        try:
            raw = base64.b64decode(line[8:] + "==").decode()
            data = json.loads(raw)
            data["ps"] = f"MySub-{count}"
            new_raw = base64.b64encode(json.dumps(data).encode()).decode()
            output.append("vmess://" + new_raw)
            count += 1
        except:
            continue
    else:
        output.append(line)

with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(output))
