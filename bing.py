import webbrowser

def main():
	while True:
		searchfor = input("Search (with Bing): ")
		print("Did you mean %s porn?" % (searchfor))
		print('https://bing.com/search?q=%s+porn (Opening that for you)' % (searchfor))
		webbrowser.open('https://bing.com/search?q=%s+porn' % (searchfor))

main()
