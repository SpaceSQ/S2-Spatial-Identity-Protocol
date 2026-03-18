# 示例代码：如何让你的 AI Agent 连上 Space2 Matrix 获得坐标
import requests
import time

def sync_matrix_status(agent_did, agent_address, task_log):
    url = "https://space2.world/api/v1/matrix/telemetry"
    headers = {"X-Space2-DID": agent_did, "X-Space2-Address": agent_address}
    payload = {"timestamp": int(time.time()), "status": "ACTIVE", "log": task_log}
    
    try:
        requests.post(url, json=payload, headers=headers)
        print(f"🦞 [Matrix] Identity {agent_did} anchored at {agent_address}")
    except:
        print("📡 [Matrix] Uplink failed.")

# Check your dynamic dossier at: https://space2.world/address/{agent_address}
