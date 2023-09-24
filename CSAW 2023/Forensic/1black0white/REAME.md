# 1black0white

## Overview
Point    = 50 <br/>
Category = Forensic

## Descriptions
Players receive a text file with seeming random numbers. They need to take clues from the title and the challenge description in order to convert these numbers to a QR code which contains the flag.

### Solution
1. The first step I took was to download ```qr.code.txt.``` After the download was complete, I changed the directory from the folder in the terminal to the folder containing ```qr.code.txt``` <br/> <br/>
```Locate File``` <br/>
![image (1)](https://github.com/G34ts/cjv_writeups/assets/126637263/5e389f94-6cee-44da-979b-a15dd320ea27) <br/> <br/>
```Directory Changes``` <br/>
![image](https://github.com/G34ts/cjv_writeups/assets/126637263/e440ef54-1302-4834-a2e0-dbc833da50fd) <br/>
<br/>

2. The second step I did was to try to open the downloaded file, and see what it contained. <br/> <br/>
```Opening File``` <br/>
```./[file]``` <br/>
![image](https://github.com/G34ts/cjv_writeups/assets/126637263/174d578c-ce60-4672-a9b2-ac0280eb12eb) <br/> <br/>
We can see, that in the ```qr.code.txt``` file, there are 29 lines of text, each of which contains a set of numbers that are randomized in order along with the amount. From what we know, the creator of the challenge mentions that these numbers are a **QR Code**. <br/> <br/>

3. Then for the third step, we can analyze how we can turn this set of numbers into a QR Code that can be scanned. The first thing I did was look at the title of this challenge. That is 1black0white. <br/> <br/>
If we associate that title with QR Codes is. The most dominant colors on an average QR Code are black and white. That was the first thing I thought of. Next is the number 1 in black and 0 in white. What we can associate for these 2 numbers for me are binary numbers. This made me have an idea, which is what if we convert each of these 29 numbers into binary numbers first, then use an online tool/python code to convert the binary numbers into an image. Which if the system detects there is a number 1, it will produce 1 black pixel, and vice versa. If the system detects a 0, it will produce 1 white pixel.

4. Then the fourth step I did was to convert all the numbers contained in qr.code.txt into binary numbers using python. Then I put it in notes for validation at the end. <br/> <br/>
```Dec-to-Binary.py``` <br/>
```py
h = open("qr_code.txt", "r")

h = h.read()

for i in h.split():
    binn = bin(int(i))[2:].zfill(29)
    print(binn)
```
