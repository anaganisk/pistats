import arrow
import os
import psutil

def uptime():
    time = psutil.boot_time()
    return "UP " + arrow.get(time).humanize()


def get_time():
    utc = arrow.utcnow()
    local = utc.to(os.environ.get('TIMEZONE', 'GMT'))
    return local.format('HH:mm DD/MM/YYYY')

def get_uptime_ip():
    return [get_time(), uptime()]


if __name__ == "__main__":
    pass