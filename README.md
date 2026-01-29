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

Okay, I think I got it figured out, except for what to do when some of the data is missing. For now, I have a potential AI generated solution, but I haven't tried it yet. Here it is:
If a section is missing from the middle of a row in your data, you can still apply a similar approach. The main idea is to check if any specific section (like `data3` in your example) is missing and fill it with an empty string to maintain the proper alignment in the TSV file.

### Step-by-Step Approach

1. **Define the Expected Columns in Order**: Make sure you know the order of the expected columns. In your case, let's say the expected order is `data1`, `data2`, `data3`, `data4`, and `data5`.

2. **Use a Mapping or Template**: Create a list that acts as a template for your expected data sections. 

3. **Iterate and Fill Missing Sections**: When processing each row, map the available data to the expected sections, inserting empty strings for any missing sections.

### Example Code

Here's how you can implement this:

```python
import re

# Define the expected columns in the desired order
EXPECTED_COLUMNS = ['data1', 'data2', 'data3', 'data4', 'data5']

def process_row(input_row):
    # Use Regex to filter and split the row
    sections = re.split(r'\s+', input_row.strip())  # Adjust the Regex if needed

    # Create a mapping for the processed row
    mapped_row = {key: '' for key in EXPECTED_COLUMNS}  # Start with empty values

    # Fill the mapped row with available data
    for i, section in enumerate(sections):
        if i < len(EXPECTED_COLUMNS):  # Avoid index error
            mapped_row[EXPECTED_COLUMNS[i]] = section

    # Return the ordered row with tabs
    return [mapped_row[col] for col in EXPECTED_COLUMNS]

def generate_tsv(input_data):
    with open('output.tsv', 'w') as tsv_file:
        for row in input_data:
            processed_row = process_row(row)
            tsv_file.write('\t'.join(processed_row) + '\n')

# Example usage
input_data = [
    "data1 value1 data2 value2",  # Missing data3
    "data1 value1 data2 value2 data4 value4",  # Missing data3
    "data1 value1 data2 value2 data3 value3 data4 value4 data5 value5",
]

generate_tsv(input_data)
```

### Explanation
1. **Expected Columns**: The `EXPECTED_COLUMNS` variable defines the order of your data.
2. **Mapping**: The `mapped_row` dictionary initializes the expected keys (columns) with empty strings.
3. **Filling Data**: Each section from the input row is inserted into the `mapped_row` based on its index. If a section is missing, it remains an empty string.
4. **Returning the Ordered Data**: The final row is constructed in the order of `EXPECTED_COLUMNS`, ensuring any gaps in the data will appear as empty cells in the TSV.

### Conclusion
This method ensures that even if a section is missing anywhere in the row, your TSV file will remain properly formatted with empty cells in place of missing sections. You can adjust the expected columns and Regex according to your specific needs.
