import sys, os

if len(sys.argv) < 2:
	print("""
	 Pour utiliser ce script python ajouter le nom du fichier md
	 example:
	    python fix_url.py 31-janvier-2023.md
	""")
else:
	
	path = os.path.join(sys.argv[1])
	text = open( path ).read()
	words = text.strip().replace("\n"," ").split()
	urls = filter( lambda word: word.startswith("http"), words)
	
	for url in set(urls):
	    text = text.replace( url, "<"+url+">" )
	
	open( path, 'w' ).write(text)
