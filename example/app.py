import os
from scanpages.scanpage import Scanpage

scan = Scanpage()
# scan.set_page('https://example.com')

# res = scan.scan()

# print(res)

# res = scan.scan_from_file('./source/source.json')
# print(res)

scan.set_filepath(os.path.abspath("import/source.json"))

print(scan.scan_import('export.txt'))