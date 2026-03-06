import json, os 

status_file = "/tmp/waybar_timer_status"

if os.path.exists(status_file):
    with open(status_file, "r") as f:
        status = json.load(f)
    status["active"] = not status.get("active", False)
    with open(status_file, "w") as f:
        json.dump(status, f)