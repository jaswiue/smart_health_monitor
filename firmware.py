import random
import time

def Main_status():
  print("SMART HEALTH MONITOR")  # main title shown when product starts, debating whether to start with menu or main status
  print("Status:" status_current) # qualitifies the data given into different catergories, NNORMAL/---/---- are the options available
  print("Temp:" temp_current) # shows the most recent reading of the patient temperature (questioning whether the readings will be automatic with intervals or when requested)
  print("HR:" hr_current) # shows recent heart rate reading, same issue with temp

def Temp_detail():
  print("TEMP SENSOR") #this will be one of the options on the menu. It more detailed temp reading (including analysis of data)
  print("Current:" temp_current())
  print("Avg:" temp_average())
  print("Trend:" temp_trend())

def heart_rate_detail():
  print("PULSE SENSOR")
  print("HR:" hr_current())
  print("Signal:" hr_signal())
  print("Trend:" hr_trend())

def alert_screen():
  print("ALERT")
  Alert_issue() #depending whether temp too high/low or HR reading is above/ lower than standard it will show warning here
  print("Check reading")
  print("Buzzer:" Buzzer_status())
  

