from bs4 import BeautifulSoup
import re

url = "/home/race/ksl/truck-large.html"

soup = BeautifulSoup(open(url), 'html.parser')

# with open('truck-1.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

# data = '' 
# for data in soup.find_all('a'): 
#     print(data.get_text())

# for data in soup.find_all('a'):
#     with open('truck.csv', 'a', encoding='utf-8') as f:
#         f.write(data.get_text(' ') + '\n')

output = '\n'.join([data.get_text(separator=' | ') for data in soup.find_all('a')])
# print(output)


corrected = re.sub(r'\s*\|\s*', '\t', output) # removes spaces around |
corrected_1 = re.sub(r'\t+', '\t', corrected) # replaces multiple tabs with a single tab
# corrected_2 = re.sub(r'\s*est\..*$', '', corrected_1) # removes 'est.' monthly payment info and anything after it
corrected_2 = re.sub(r' ', '\t', corrected_1) # replaces non-breaking spaces with a single tab
corrected_3 = re.sub(r'^Spotlight\t', '', corrected_2, flags=re.MULTILINE) # removes 'Spotlight' at the start of lines
corrected_4 = re.sub(r'^Price Reduced\t', '', corrected_3, flags=re.MULTILINE) # removes 'Price Reduced' at the start of lines
corrected_5 = re.sub(r'Trusted Dealer\t', '', corrected_4, flags=re.MULTILINE) # removes 'Trusted Dealer' at the end of lines
corrected_6 = re.sub(r'KSL Verified\t', '', corrected_5) # removes 'KSL Verified' at the end of lines
corrected_7 = re.sub(r'MSRP \$\d\d,\d\d\d', '', corrected_6) # removes 'MSRP' price on new vehicles
# corrected_8 = re.sub(r'est\.\s*\$\d[\d,]*.*$', '', corrected_7) # removes 'est.' monthly payment info and anything after it
# corrected_8 = re.sub(r'est\..*$', '', corrected_7) # removes 'est.' monthly payment info and anything after it
lines = corrected_7.split('\n')

corrected_lines = [line.split("est.")[0].strip() for line in lines] # removes 'est.' monthly payment info and anything after it

# for corrected in corrected_lines:
#     print(corrected)


with open('truck.tsv', 'w', encoding='utf-8') as f:
    # f.write('\n'.join(lines))
    f.write('\n'.join(corrected_lines))