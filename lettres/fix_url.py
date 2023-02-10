import sys, os

path = os.path.join(sys.argv[1])
text = open( path ).read()
words = text.strip().replace("\n"," ").split()
urls = filter( lambda word: word.startswith("http"), words)

for url in set(urls):
    text = text.replace( url, "<"+url+">" )

open( path, 'w' ).write(text)
