# openpowerlifting-fetch
 
Fetch the Competition History of a lifter from openipf.com


### Table of contents

- [Installation](#installation)
- [Usage](#usage)


### Installation


Clone the github repo
```
$ git clone https://github.com/georgehawkins0/openpowerlifting-fetch.git
```
Change Directory

```
$ cd openpowerlifting-fetch
```

Install Requirements

```
$ python3 -m pip install -r requirements.txt
```


### Usage
#### Quick Start

Import Page

```python
from fetcher import Page
```

- Fetch from URL

```python
# Create a Page object
page = Page(url='https://www.openipf.org/u/timothymonigatti')

data = page.get_data()
print(data)
```

- Fetch from openIPF username

```python
# Create a Page object
page = Page(username='timothymonigatti')

data = page.get_data()
print(data)
```

#### Request
Instantiating a page object as above automatically does the web request when created. If for some reason you want to make the object, but call the request at a different time, the following can be done:

```python
page = Page(username='timothymonigatti', fetch=False)
...
page.fetch()
data = page.get_data()
```

Or just

```python
page = Page(username='timothymonigatti', fetch=False)
...
data = page.get_data() # Auto calls fetch if not fetched before
```

#### Data Refresh
If you want to refresh the data in the object, you can 

```python
page = Page(username='timothymonigatti')
...
data = page.get_data(refresh_data=True) # Auto calls fetch if not fetched before
```



Returned is the full list of competitons, with each having the the keys:

- Place
- Fed
- Date
- Location
- Competition
- Division
- Age
- Equip
- Class
- Weight
- Squat
- Bench
- Deadlift
- Total
- GLP/Dots (OpenIPF.com vs OpenPowerlifting.com)