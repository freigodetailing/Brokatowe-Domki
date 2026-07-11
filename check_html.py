with open('galeria.html', 'r', encoding='utf-8') as f:
    text = f.read()
start = text.find('id="sec-5be2"')
end = text.find('id="block-1"')
if start != -1 and end != -1:
    print(text[end-800:end+800])
