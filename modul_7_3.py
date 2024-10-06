class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self, *file_names):
        all_words = {}
        for i in self.file_names:
            symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
            with open(i, 'r', newline='', encoding='utf-8') as file: # почему не работает newline=''?
                file = file.read().replace('\r\n', ' ').lower()
                for symbol in symbols:
                    if symbol in file:
                        file = file.replace(symbol, '')
                file = file.split()
            all_words.update({i: file})
        return all_words

    def find(self, word):
        dic_word = {}
        for j in self.file_names:
            word = word.lower()
            for name, words in self.get_all_words().items():
                if word in words:
                    pos = words.index(word) + 1
                    dic_word.update({name: pos})
        return dic_word

    def count(self, word):
        dic_word = {}
        for j in self.file_names:
            word = word.lower()
            for name, words in self.get_all_words().items():
                if word in words:
                    con = words.count(word)
                    dic_word.update({name: con})
        return dic_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте

