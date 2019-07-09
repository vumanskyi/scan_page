from scanpages.scanpage import Scanpage

scan = Scanpage()
scan.set_page('https://example.com')

res = scan.scan()

print(res)