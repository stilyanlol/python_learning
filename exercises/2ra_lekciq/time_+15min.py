hour = int(input())
minutes = int(input())

if hour <= 23 and minutes <= 59:
    minutes += 15

    if minutes >= 60:
        hour += 1
        minutes -= 60

    if hour > 23:
        hour = 0

    if minutes < 10:
        print(f"{hour}:0{minutes}")
    else:
        print(f"{hour}:{minutes}")