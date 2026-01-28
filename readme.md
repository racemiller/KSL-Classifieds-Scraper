Quick update since I don't have much time.

headers.py is the main program I'm trying to work with. Right now I can't figure out how to bypass the Captcha with Selenium. Selenium is needed to handle KSL's infinite scroll.
Sending user agents via requests is working independently, but not through Selenium. Setting user agents in the Chrome options in Selenium is not working either.
scroll.py is for testing running requests into Selenium. Not much there right now.
chrometest.py was to debug issues with getting Selenium working (having issues launching the browser). Got that fixed so this should probably be deleted later.
soup.py is some BeautifulSoup testing, and that's working just fine, especially when running the user agent through requests. Downside is no infinite scrolling so you only get like 10 results.

I haven't even begun to look into how to format the data once I get a hold of it, let alone how to enter it into a database. Eventually I would like a database that updates daily and shows me when a good deal might be available.

Next steps I guess would be to get cleaned up and a little more organized, then work on overcoming the infinite scroll/Captcha issue.
