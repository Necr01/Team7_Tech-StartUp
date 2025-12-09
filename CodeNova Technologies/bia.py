from utils import read_json, write_json, timestamp, log_event

BIA_FILE = "data/bia.json"

def add_bia_record(username):
    print("\n=== Add BIA Record ===")
    asset = input("Asset Name: ")
    threat = input("Threat Scenario: ")
    financial = input("Estimated Financial Impact: ")
    operational = input("Operational Impact: ")
    recovery = input("Recovery Strategy: ")

    record = {
        "time": timestamp(),
        "user": username,
        "asset": asset,
        "threat": threat,
        "financial": financial,
        "operational": operational,
        "recovery": recovery
    }

    data = read_json(BIA_FILE)
    data.append(record)
    write_json(BIA_FILE, data)

    log_event(f"BIA record added by {username} for {asset}")
    print("BIA record added.")

def view_bia_records():
    bia = read_json(BIA_FILE)
    print("\n=== BIA Records ===")
    for b in bia:
        print(b)
