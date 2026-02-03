Quick update since I don't have much time.

headers.py is the main program I'm trying to work with. Right now I can't figure out how to bypass the Captcha with Selenium. Selenium is needed to handle KSL's infinite scroll.
Sending user agents via requests is working independently, but not through Selenium. Setting user agents in the Chrome options in Selenium is not working either.
scroll.py is for testing running requests into Selenium. Not much there right now.
chrometest.py was to debug issues with getting Selenium working (having issues launching the browser). Got that fixed so this should probably be deleted later.
soup.py is some BeautifulSoup testing, and that's working just fine, especially when running the user agent through requests. Downside is no infinite scrolling so you only get like 10 results.

I haven't even begun to look into how to format the data once I get a hold of it, let alone how to enter it into a database. Eventually I would like a database that updates daily and shows me when a good deal might be available.

Next steps I guess would be to get cleaned up and a little more organized, then work on overcoming the infinite scroll/Captcha issue.

I kind of gave up for now on the whole infinite scroll thing and started working on organizing the data once it's gathered. This way I can pull HTML data from KSL manually if I have to, and I want to run it through a script that organizes the data into a readable CSV or TSV, which can then be imported to Excel and organized into a table/graph.
I think long term some kind of database will be better, but I know if it's compatible with Excel, it'll be compatible with any other database.
This program is called "bs.py" and I'm making some decent progress on it. Basically using BeautifulSoup to extract the text from the HTML, then a bunch of Regex filters to clean it up.
I still need to find a way to make all the columns (tabs) align in the event that some data is missing from the original HTML (city, state, date listed, etc.). Also need to figure out why some cities are tab separated and some are space separated (and how to make them all tab separated and probably remove the comma between city and state).

I started over using ChatGPT and it basically gave me a perfect script that uses beautifulsoup to extract the exact data I need from the HTML and puts it cleanly into a CSV. Next step is to work with chat to see if we can get selenium and/or requests working (see chat in progress).
