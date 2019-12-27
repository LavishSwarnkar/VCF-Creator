# VCF-Creator
A Simple VCF Creator made in Python. Just give a bunch of phone numbers as input and this script will generate a VCF with numerical dummy names.\
\
**Sample Input:**
+919828098280,+919988227733\
\
**Sample Output (.vcf file):**
```
BEGIN:VCARD
VERSION:2.1
N:;1;;;
FN:1
TEL;CELL:+919828098280
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:;2;;;
FN:2
TEL;CELL:+919988227733
END:VCARD
```
**Intent to create this script :** Sending WhatsApp message to many people without saving their numbers\
\
**How this script solves the problem:** Just give this script a CSV of numbers and it will generate a VCF which can then be saved to device. This script names the contacts with numerical names such as 1, 2, ... so they are easily distinguishable. And then you can send messages and then delete all those contacts at once!
