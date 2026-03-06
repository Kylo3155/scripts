import subprocess, time, json, os

minutes = 50

status_file = "/tmp/waybar_timer_status"

def load_status():
    if not os.path.exists(status_file):
        return {"seconds": minutes*60, "active": False}
    with open(status_file, "r") as f:
        return json.load(f)

def save_status(status):
    with open(status_file, "w") as f:
        json.dump(status, f)

status = load_status()
save_status(status)

if status["active"] and status["seconds"] > 0:
    status["seconds"] -= 1
    save_status(status)

mins = status["seconds"] // 60
secs = status["seconds"] % 60
time_text = f"{mins:02d}:{secs:02d}"

icon = "󱎫" if status["active"] else "󱎩"

output = {
    "text": f"{icon} {time_text}",
    "class": "active" if status["active"] else "paused",
    "tooltip": "Click to start pause | Right-click to reset"
}

print(json.dumps(output))

'''
def countdown(minutes, stage):
    seconds = minutes*60
    while seconds >= 0:
        #subprocess.run('clear', shell=True)
        mins, secs = divmod(seconds, 60)
        #print(f"{mins:02d}:{secs:02d} remaining of {state}")
        data = {
            "text": f"{mins:02d}:{secs:02d}, {stage}",
            "tooltip": f"{mins:02d}:{secs:02d} remaining of {stage}",
            "class": "custom-python"
        }
        #print(json.dumps(data))
        time.sleep(1)
        seconds-=1

while(minutes >= 10):
    countdown(minutes, "work")
    countdown(10, "break")
    minutes-=10
'''