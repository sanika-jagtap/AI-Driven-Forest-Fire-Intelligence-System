import numpy as np
import random
from PIL import Image, ImageDraw

def spread_rate(temp, humidity, wind_speed):
    rate = (temp * 0.03) + (wind_speed * 0.05) - (humidity * 0.02)
    if rate < 1:
        rate = 1
    return rate


def predict_fire_spread(start_x, start_y, days, wind_direction, wind_speed, temp, humidity):

    fire_points = [(start_x, start_y)]
    current_points = [(start_x, start_y)]

    rate = spread_rate(temp, humidity, wind_speed)

    for day in range(days):

        new_points = []

        for x, y in current_points:

            for i in range(4):

                dx = random.randint(-20, 20)
                dy = random.randint(-20, 20)

                if wind_direction == "E":
                    dx += wind_speed * 2
                elif wind_direction == "W":
                    dx -= wind_speed * 2
                elif wind_direction == "N":
                    dy -= wind_speed * 2
                elif wind_direction == "S":
                    dy += wind_speed * 2

                new_x = int(x + dx * rate)
                new_y = int(y + dy * rate)

                new_points.append((new_x, new_y))
                fire_points.append((new_x, new_y))

        current_points = new_points

    return fire_points


def draw_future_fire(image_path):

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    start_x = 450
    start_y = 450

    wind_direction = "E"
    wind_speed = 5
    temperature = 35
    humidity = 20

    points = predict_fire_spread(
        start_x,
        start_y,
        5,
        wind_direction,
        wind_speed,
        temperature,
        humidity
    )

    for x, y in points:
        draw.ellipse((x, y, x+6, y+6), fill=(255,0,0))

    img.save("Future_Fire_Spread.jpg")
    img.show()