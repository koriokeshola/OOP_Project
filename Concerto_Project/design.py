# Program Description: Program used for displaying day designs,
# and allowing for life like typing when the player is introduced to the game.
# Gives the player a more immersive experience.

import time
import sys

# Function that prints what day of game it is.
def printing_day(number):
        if number== 1:
            print(""" 
$$$$$$               $$$$$        $$$        $$$        1111111
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$      111111111
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$     1111   1111
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$             1111
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                1111
$$$$  $$$$$      $$$$     $$$$         $$$$                1111
$$$$$$$          $$$$     $$$$         $$$$             111111111 """)
        elif number == 2:
            print(""" 
$$$$$$               $$$$$        $$$        $$$    222222222222
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$             222
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$              222
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$      2222222222
$$$$    $$$$     $$$$$$$$$$$$$         $$$$         222    
$$$$  $$$$$      $$$$     $$$$         $$$$         222       
$$$$$$$          $$$$     $$$$         $$$$         222222222222 """)
        elif number == 3:
            print(""" 
$$$$$$               $$$$$        $$$        $$$    3333333333
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$             333
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$              333
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$          333333
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                  333
$$$$  $$$$$      $$$$     $$$$         $$$$                  333       
$$$$$$$          $$$$     $$$$         $$$$         3333333333   """)
        elif number == 4:
            print(""" 
$$$$$$               $$$$$        $$$        $$$    444      444
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$    444      444        
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$     444      444       
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$      444444444444
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                  444
$$$$  $$$$$      $$$$     $$$$         $$$$                  444       
$$$$$$$          $$$$     $$$$         $$$$                  444  """)
        elif number == 5:
            print(""" 
$$$$$$               $$$$$        $$$        $$$    555555555555
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$    555              
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$     555             
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$      555555555555
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                  555
$$$$  $$$$$      $$$$     $$$$         $$$$                  555       
$$$$$$$          $$$$     $$$$         $$$$         555555555555  """)

# Function that animates text with a slow typing effect.
def type_text(text, delay=0.075):
    for char in text:
        sys.stdout.write(char) # Write one character at a time without creating a newline like print.
        sys.stdout.flush() # Forces character to display immediately rather than wait for buffer to fill.
        time.sleep(delay) # Pauses for delays to create a typing effect.
    print()  # Move to the next line.
