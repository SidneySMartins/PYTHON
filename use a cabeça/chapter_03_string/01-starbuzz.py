import urllib.request

page = urllib.request.urlopen("https://www.google.com/")
text = page.read().decode('utf8')
# a instrução decode ->converte á página para algo mais fácil para os humanos aprenderem
info = text[300:310]
print(text)
print(info)
