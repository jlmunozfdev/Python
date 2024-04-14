# @jlmunozfdev

# install & import required libraries
import pyautogui # pip install pyautogui
import time #  pip install pillow

# Define the interval in seconds
interval = 10    

# Wait for the specified interval
time.sleep(interval)  

# Take a screenshot
screenshot = pyautogui.screenshot()  

# Save the screenshot with a timestamp as the filename
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  
screenshot.save(f"screenshot_{timestamp}.png")  

print("Screenshot taken and saved.")  
