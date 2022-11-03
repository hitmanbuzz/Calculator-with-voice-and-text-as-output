# calculator with answer result and error output/msg as voice and text.
# by text mean you will get a text output in your run shell such as terminal, cmd, powershell, etc
# made by Hitman-2005
# discord : H I T M A N#1403
# known as Hitman in other social networks such as game and others sites


# Module Part
import os
import gtts

# num1 = 1st number
# num2 = 2nd number
num1 = input('num1: ')
num2 = input('num2: ')

# op = operator(+, -, *, /)
# addition: +
# subtraction: -
# multiplication: *
# division: /
op = input('op: ')

# Addition Part using if statement
if op == '+':
    result1 = float(num1) + float(num2)
    # Result1 Part for voice and text output
    convert1 = str(result1)
    result1_text = gtts.gTTS(convert1)
    result1_text.save('result1_text.mp3')
    os.startfile('result1_text.mp3')
    print(result1)

# Subtraction Part using if statement
elif op == '-':
    result2 = float(num1) - float(num2)
    # Result2 Part for voice and text output
    convert2 = str(result2)
    result2_text = gtts.gTTS(convert2)
    result2_text.save('result2_text.mp3')
    os.startfile('result2_text.mp3')
    print(result2)

# Multiplication Part using if statement
elif op == '*':
    result3 = float(num1) * float(num2)
    # Result3 Part for voice and text output
    convert3 = str(result3)
    result3_text = gtts.gTTS(convert3)
    result3_text.save('result3_text.mp3')
    os.startfile('result3_text.mp3')
    print(result3)

# division Part using if statement
elif op == '/':
    result4 = float(num1) / float(num2)
    # Result4 Part for voice and text output
    convert4 = str(result4)
    result4_text = gtts.gTTS(convert4)
    result4_text.save('result4_text.mp3')
    os.startfile('result4_text.mp3')
    print(result4)

# Error handling if any of the above 4 if/elif statement define as false or doesn't suit
else:
    # Error Part for voice and text output
    error_text = gtts.gTTS('Your computer is hacked, hahahahahahaha')
    error_text.save('error_text.mp3')
    os.startfile('error_text.mp3')
    print('Your computer is hacked, hahahahahahaha')

# Code end here💕👍