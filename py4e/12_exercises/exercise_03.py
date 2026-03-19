# Use `urllib`, to replicate the previous exercise of
# (1) retrieving the document from a URL, (2) displaying
# up to 3000 characters, (3) counting the overall number
# of characters, in the document.

# Don't worry about the headers, for this exercise, simply
# show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error

try:
    url = input("Enter a URL: ")

    fhand = urllib.request.urlopen(url)
    
    string_data = ""
    
    for line in fhand:
        words = line.decode()
        string_data = string_data + words
    
    print(string_data[:3000])
    print(len(string_data))
except:
    print("Invalid URL.")
