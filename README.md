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

Import Page

```python
from fetcher import Page
```

- Fetch from URL

```python
# Create a Page object
page = Page(url='https://www.openipf.org/u/timothymonigatti')

print(page.get_data())
```

- Fetch from openIPF username

```python
# Create a Page object
page = Page(username='timothymonigatti')

print(page.get_data())
```