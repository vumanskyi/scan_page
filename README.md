# Simple scraping web pages

This is a alpha version - at the moment is scraping only **status_code**. 
It is necessary to check the page status code.

### How to use

Scan one page and get result

```python
from scanpages.scanpage import Scanpage

scan = Scanpage()
scan.set_page('https://example.com')

res = scan.scan()

print(res)
```

The list of data from json file

```python
import os
from scanpages.scanpage import Scanpage

scan = Scanpage()

res = scan.scan_from_file(os.path.abspath("import/source.json"))
print(res)
```

Import data from file and results export into .txt file

```python
import os
from scanpages.scanpage import Scanpage

scan = Scanpage()

scan.set_filepath(os.path.abspath("import/source.json"))

print(scan.scan_import('export.txt'))
```