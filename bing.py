import webbrowser
import json
import random
import time

with open("pornlist.json") as f:
    pornlist = json.load(f)

def main():
	while True:
		searchfor = input("Search (with Bing): ")
		prefix = random.choice(pornlist['prefix'])
		prefix2 = random.choice(pornlist['prefix2'])
		suffix = random.choice(pornlist['suffix'])
		suffix2 = random.choice(pornlist['suffix2'])
		final = prefix + prefix2 + searchfor + suffix + suffix2
		print("Did you mean: %s (Opening in 3 seconds)" % (final))
		time.sleep(3)
		webbrowser.open('https://bing.com/search?q=%s' % (final))

main()
