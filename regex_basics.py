# import Regex library for Py
import re
"""
This script demonstrates the use of regular expressions (Regex) in Python for pattern matching and text extraction.
It performs the following tasks:
1. Finds all substrings in a given string that start with 'a' and end with 'c', with any characters in between.
2. Extracts and parses the title text from an HTML tag using Regex.

Libraries used:
- re: For working with regular expressions in Python.

Usage:
- The script initializes a pattern to find substrings that start with 'a' and end with 'c' in a given string.
- It prints the matched substrings.
- It then extracts the title text from an HTML tag by removing the HTML tags using Regex and prints the result.
"""

pattern = "a.*c"
string = "ac, abdc abc abbcaabc. aabcc"
result = re.findall(pattern, string)
print(result)
# res: ['ac', 'abc', 'abbc', 'abc', 'abc']
# and may or may not have 1 or more 'b's in-between
# only extracts strings that start with 'a' and end with 'c'

# extract the title text
# parse the title text using Regex
title_tag = "<TITLE >Profile: Dionysus</title  / >"
pattern = "<title.*?>.*?</title.*?>"
result = re.search(pattern, title_tag, re.IGNORECASE)
if (result):
    res = result.group()
    print(res)
    pattern = "<.*?>"
    title = re.sub(pattern, "", res) # substitute substring with no character
    print(title)
