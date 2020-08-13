import psutil
#docker ps --format "{{.Names}}: {{.Status}}"

def get_mem():
    data = psutil.virtual_memory().percent
    return int(round(data))

def get_cpu():
    data = psutil.cpu_percent()
    return int(round(data))

def get_temp():
    data = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return int(round(data))

def get_du():
    du = psutil.disk_usage('/')
    return int(du.percent)

if __name__ == "__main__":
    pass