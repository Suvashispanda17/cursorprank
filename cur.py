# import pyautogui as pag
# import random
# import time
# import keyboard as ke
# import cowsay as cs

# while True:
#     if ke.is_pressed('q'):
#         cs.daemon("you got pranked my friend.......")
#         print("you got pranked my friend.......")
#         break
#     # Move the mouse to a random location on the screen
#     x= random.randint(500,1000)
#     y= random.randint(200,600)
#     pag.moveTo(x,y)
#     # Move the mouse to a random location on the screen
#     time.sleep(3) # wait for 3 seconds before moving again
    



import pyautogui as pag
import random
import time
import keyboard as ke
import cowsay as cs

while True:    
    # Move the mouse to a random location on the screen
    x = random.randint(500, 1000)
    y = random.randint(200, 600)
    pag.moveTo(x, y)
    
    # Wait for short intervals (split 3 seconds into smaller intervals to allow key detection)
    for i in range(30):  # This loops for 3 seconds (30 * 0.1 = 3)
        if ke.is_pressed('q'):
            cs.daemon("you got pranked my friend.......")
            break
        time.sleep(0.1)  # Sleep for a short time to frequently check for the 'q' press
    else:
        continue  # Continue if the loop is not broken
    break  # Exit the outer loop if 'q' was pressed
