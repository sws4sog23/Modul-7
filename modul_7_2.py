def custom_write(file_name, strings):
    strings_positions = {}
    file_n = str(file_name)
    a = 0
    file = open(file_n, 'a', encoding='utf-8')
    file.seek(0)
    for i in strings:
        a +=1
        ssb = file.tell()
        ii = str(i) + '\n'
        file.write(ii)
        strings_positions.update({(a, ssb): i})
    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)