from fetcher import Page    
import time

# Create a Page object
page = Page(username='timothymonigatti', fetch=True)

print(time.time())
page.fetch()
print(time.time())
page.get_data()
print(time.time())