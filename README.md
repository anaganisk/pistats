# Quick Pi stats LCD (16x2 I2c) for raspberrypi 3
A quick display of raspberry pi 3 stats on 16x2 LCD screen using I2C module, with progress bars for relevant stats.

I couldn't find any python libraries which support progress bars to the LCD display, you can take a look into pistat.py file to checkout the implementation incase you are interested.

[Homepage](https://github.com/anaganisk/pistats)

[Docker](https://hub.docker.com/repository/docker/anaganisk/pistats)

![LCD Screen image](https://raw.githubusercontent.com/anaganisk/pistats/master/screen.jpg)

**This docker image is a arm64 build**

This project was intended for personal use, and a quick 30 min dirty hack to get my pi with basic stats up and running.

Though you may use it, it is better suggested to look around and get an idea and build may be a better way.

Requirements:
 - docker

Stats displayed
 - Current time - Uptime
 - CPU, Memory and Temperature
 - Current running dockers container with uptime

usage
```bash
docker run --privileged -e TIMEZONE='Asia/Kolkata' -v /var/run/docker.sock:/var/run/docker.sock --name=pistats --restart unless-stopped -d anaganisk/pistats:0.0.1
```

License:
MIT