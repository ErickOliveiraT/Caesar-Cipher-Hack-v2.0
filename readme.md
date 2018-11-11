# Ceasar Cipher Hack v2.0

This is a brute force algorithm to decode a text encoded with caesar cipher. It works by trying every possible key (1 to 25) and printing the possible result for each key. Than, the program will try to indicate de most likely match by searching the words in a big wordlist that is read from a ".txt" document.

Even if the brute force don't suceed, you can look for your text by reading key per key that was printed.

Thanks for supporting !! I'm able to receive improve tips !!
 
### Usage
```sh
$ python cesar.py
```
Then, follow the interative menu

### For Linux or Mac Users

You will have to eliminate all calls for lambda functions declared on lines 5, 6 and 7. It does not cause any efect to the algorithm, it's just for the visual.

### Setting a Wordlist

You can set a wordlist on line 8, using the format "archive_name.extension"