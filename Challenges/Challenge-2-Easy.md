CTF Name: eduCTF

Challenge Name: PLACEHOLDERPLACEHOLDERPLACEHOLDERPLACEHOLDER

Category: Forensics (Steganography), Cryptography

Difficulty: Easy

Challenge Description: "PLACEHOLDERPLACEHOLDERPLACEHOLDER"

Hints: You modify something to change it, so how did the suspect change something about this image?

TOOLS USED TO WRITE CHALLENGE:

GENERAL IDEA:

My idea for this challenge is simple:

The user is given 1 image, and 20 text files. 

The image metadata has been modified with a base64 encoded version of the time and date.

The 20 text files are named after dates. (e.g, January1.txt, January2.txt, etc.)

All text files have some variant of the flag, but only one of them has the correct one.

The player must decode the base64 in order to find out which .txt file is the correct one to choose.

Let's begin.

CHALLENGE WRITING PROCESS:

First of all, I'll make a directory for this second challenge called "Challenge2Easy"

    ┌──(hellopo㉿rald)-[~/eduCTF2026]
    └─$ mkdir Challenge2Easy/

Now, I have a sample file to experiment with called testing.jpg. Eventually this file will be replaced with the final image we'll use, but this will serve as a placeholder for now.

That is what files called "testing" are for from here on forward.

Right now, that file is in my Downloads dir. I'll just move it to the dir of choice.

    ┌──(hellopo㉿rald)-[~/Downloads]
    └─$ mv testing.jpg ~/eduCTF2026/Challenge2Easy/

Now let's work on the file using exiftool. I want to edit the -FileModifyDate flag and set it to April 16, today.

April 16 will be the correct .txt file to open by the player. 
    
    ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy]
    └─$ exiftool -FileModifyDate="2026:04:16 12:21:00" testing.jpg 
        1 image files updated

  Looks like it successfully updated, let's check it out.
                                                                                                      
    ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy]
    └─$ exiftool testing.jpg                                      
    ExifTool Version Number         : 13.50
    File Name                       : testing.jpg
    Directory                       : .
    File Size                       : 400 kB
    File Modification Date/Time     : 2026:04:16 12:21:00-04:00
    File Access Date/Time           : 2026:04:16 12:21:00-04:00
    File Inode Change Date/Time     : 2026:04:15 12:28:12-04:00

Great! Now the File Modification Date has been changed.

Let's shift our focus to the dates dir. First, let's make it.

    ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy]
    └─$ mkdir dates

Let's enter dates.

    ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy]
    └─$ cd dates

Now we have to make a whole bunch of .txt files with the wrong flag, except for the one named "April16"

        ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy/dates]
        └─$ for i in {1..20}; do echo "eduCTF{1s_th1s_th3_r1ght_fl4g?$i}" > "April_$i"; done

We don't wanna just create 20 files over and over, that'll waste a bit of time. Let's write our own bash code to automate this all in 1 line.

It starts off with a for loop which will loop 20 times, and for each loop it will echo eduCTF{1s_th1s_th3_r1ght_fl4g?}, which is attached to a number that increases 
per each loop starting from 1 right before its curly brace ends, and we will output it in April_[increasing number starting from 1]. We end it with "done" to indicate that's the last bit of command.

Result:       

        ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy/dates]
        └─$ ls      
        April_1   April_11  April_13  April_15  April_17  April_19  April_20  April_4  April_6  April_8
        April_10  April_12  April_14  April_16  April_18  April_2   April_3   April_5  April_7  April_9

Let's double check if these files actually contain eduCTF{1s_th1s_th3_r1ght_fl4g?} along with an increasing number.

        ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy/dates]
        └─$ cat *       
        eduCTF{1s_th1s_th3_r1ght_fl4g?1}
        eduCTF{1s_th1s_th3_r1ght_fl4g?2}
        eduCTF{1s_th1s_th3_r1ght_fl4g?3}
        eduCTF{1s_th1s_th3_r1ght_fl4g?4}
        eduCTF{1s_th1s_th3_r1ght_fl4g?5}
        eduCTF{1s_th1s_th3_r1ght_fl4g?6}
        eduCTF{1s_th1s_th3_r1ght_fl4g?7}
        eduCTF{1s_th1s_th3_r1ght_fl4g?8}
        eduCTF{1s_th1s_th3_r1ght_fl4g?9}
        eduCTF{1s_th1s_th3_r1ght_fl4g?10}
        eduCTF{1s_th1s_th3_r1ght_fl4g?11}
        eduCTF{1s_th1s_th3_r1ght_fl4g?12}
        eduCTF{1s_th1s_th3_r1ght_fl4g?13}
        eduCTF{1s_th1s_th3_r1ght_fl4g?14}
        eduCTF{1s_th1s_th3_r1ght_fl4g?15}
        eduCTF{1s_th1s_th3_r1ght_fl4g?16}
        eduCTF{1s_th1s_th3_r1ght_fl4g?17}
        eduCTF{1s_th1s_th3_r1ght_fl4g?18}
        eduCTF{1s_th1s_th3_r1ght_fl4g?19}
        eduCTF{1s_th1s_th3_r1ght_fl4g?20}

Well ain't that a treat.

Okay! Now let's just peek into April_16 to take a mental note of the correct answer for future development.

        ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge2Easy/dates]
        └─$ cat April_16
        eduCTF{1s_th1s_th3_r1ght_fl4g?16}

And there you have it!

Flag:

eduCTF{1s_th1s_th3_r1ght_fl4g?16}
