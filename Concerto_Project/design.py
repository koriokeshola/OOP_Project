import time
import sys



#unction that prints what day of game it is
def printing_day(number):
        if number== 1:
            color(""" 
$$$$$$               $$$$$        $$$        $$$        1111111
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$      111111111
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$     1111   1111
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$             1111
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                1111
$$$$  $$$$$      $$$$     $$$$         $$$$                1111
$$$$$$$          $$$$     $$$$         $$$$             111111111 """, 2)
        elif number == 2:
            color(""" 
$$$$$$               $$$$$        $$$        $$$    222222222222
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$             222
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$              222
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$      2222222222
$$$$    $$$$     $$$$$$$$$$$$$         $$$$         222    
$$$$  $$$$$      $$$$     $$$$         $$$$         222       
$$$$$$$          $$$$     $$$$         $$$$         222222222222 """, 2)
        elif number == 3:
            color(""" 
$$$$$$               $$$$$        $$$        $$$    3333333333
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$             333
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$              333
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$          333333
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                  333
$$$$  $$$$$      $$$$     $$$$         $$$$                  333       
$$$$$$$          $$$$     $$$$         $$$$         3333333333   """, 2)
        elif number == 4:
            color(""" 
$$$$$$               $$$$$        $$$        $$$    444      444
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$    444      444        
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$     444      444       
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$      444444444444
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                  444
$$$$  $$$$$      $$$$     $$$$         $$$$                  444       
$$$$$$$          $$$$     $$$$         $$$$                  444  """, 2)
        elif number == 5:
            color(""" 
$$$$$$               $$$$$        $$$        $$$    444444444444
$$$$ $$$$          $$$$$$$$$      $$$$      $$$$    444              
$$$$   $$$$$      $$$$   $$$$      $$$$    $$$$     444             
$$$$    $$$$$    $$$$     $$$$      $$$$  $$$$      444444444444
$$$$    $$$$     $$$$$$$$$$$$$         $$$$                  444
$$$$  $$$$$      $$$$     $$$$         $$$$                  444       
$$$$$$$          $$$$     $$$$         $$$$         444444444444  """, 2)



#function that animates text with typing effect
def type_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char) #Write one character at a time without creating newline like print
        sys.stdout.flush() #forces character to display immediately rather than wait for buffer to fill
        time.sleep(delay) #pauses for delays to create typing effect
    print()  #Move to the next line


#using ANSI Escape Sequences for coloring text
def color(text, number):
    if number == 1:
        #prints text in yellow
        print(f"\033[1;33m{text}\033[0m")
    elif number == 2:
        # prints text in blue
        print(f"\033[1;34m{text}\033[0m")
    elif number == 3:
        # prints text in cyan
        print(f"\033[1;36m{text}\033[0m")
    elif number == 4:
        # prints text in default color
        print(f"\033[0m{text}\033[0m")

