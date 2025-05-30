import time
import datetime
import pygame

def set_alarm(alarmtime):
  print(f"Alarm set for {alarmtime}")
  sound_file = "sparkle.m4a"

  is_running = True
  while is_running:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    if current_time == alarmtime:
      pygame.mixer.init()
      pygame.mixer.music.load(sound_file)
      pygame.mixer.music.play()
      is_running = False
    time.sleep(1)

if __name__ == "__main__":
  alarm_time = input("Enter the alarm time (HH:MM:SS): ")
  set_alarm(alarm_time)
