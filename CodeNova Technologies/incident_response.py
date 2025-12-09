from utils import read_json, write_json, timestamp, log_event

INCIDENT_FILE = "data/incidents.json"

def log_incident(username):
    print("\n=== Incident Reporting ===")
    incident_type = input("Incident Type: ")
    affected = input("Affected System(s): ")
    action = input("Actions Taken: ")

    incident = {
        "time": timestamp(),
        "user": username,
        "type": incident_type,
        "affected": affected,
        "action": action,
        "status": "Reported"
    }

    data = read_json(INCIDENT_FILE)
    data.append(incident)
    write_json(INCIDENT_FILE, data)

    log_event(f"Incident logged by {username}: {incident_type}")
    print("Incident recorded successfully!")

def view_incidents():
    incidents = read_json(INCIDENT_FILE)
    print("\n=== Incident Logs ===")
    for i in incidents:
        print(i)
