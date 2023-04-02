import time
import datetime
import random
import winsound

#### This is a program for those poker nights with Hope!! But hey, a random countdown timer can be for anything.

# Set up count down timer.
MINIMUM_TIME_SEC = 0.5*60
MAXIMUM_TIME_DELTA = 1*60
countdown_time = MINIMUM_TIME_SEC + random.randint(0,MAXIMUM_TIME_DELTA)
# countdown_time = 10

while countdown_time > 0 :
    # Produces a string formatted for displaying a hh:mm:ss time value
    timer = datetime.timedelta(seconds = countdown_time)

    # Prints the string, and then ends in a return-carriage character,
    # which will result in the next print starting from the same line.
    print(timer, end="\r")

    # Sleep 1 second. This is how our timer will get timed.
    time.sleep(1)

    # Decrement countdown_time by 1s since we waited 1s.
    countdown_time -= 1

# To indicate the end of the time, produce a monotonous alarm tone.
ALARM_FREQUENCY = 1000      # Hz
ALARM_DURATION = 5000       # seconds
winsound.Beep(frequency=ALARM_FREQUENCY, duration=ALARM_DURATION)
print('Bzzzt! Timer has run out!!')