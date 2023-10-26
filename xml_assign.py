import urllib.request
import xml.etree.ElementTree as ET

# URL of the XML data
url = 'https://py4e-data.dr-chuck.net/comments_1851797.xml'

# Fetch the XML data from the URL
response = urllib.request.urlopen(url)
data = response.read()

# Parse the XML data
tree = ET.fromstring(data)

# Find all 'count' elements using XPath
counts = tree.findall('.//count')

# Initialize a variable to store the sum of counts
total_count = 0

# Iterate through the 'count' elements and sum the numbers
for count in counts:
    total_count += int(count.text)

# Print the total count
print("Total Count:", total_count)
