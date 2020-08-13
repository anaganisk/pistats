import psutil
import arrow
du = psutil.virtual_memory().percent
print(du)