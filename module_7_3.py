import re

# нашел такой способ удалить знаки препиная, если необходимо это сделать выборочно, дефис, окруженный пробелами
# удаляется отдельно, апостроф же оставил, но как и одинарные кавычки
def remove_punctuation(text):
    punctuation_to_replace = ['\\','/',',', '.', '=', '!', '?', ';', ':', '"', '—']
    text = re.sub(r'\s-\s', ' ', text)
    pattern = '[' + re.escape(''.join(punctuation_to_replace)) + ']'
    text = re.sub(pattern, ' ', text).lower()
    return text.split()

class WordsFinder:

    def __init__(self, *file_names):
        file_n = [i.split(', ') for i in file_names]
        self.file_names = sum(file_n, [])


    def __str__(self):
        return f'{self.file_names}'


    def get_all_words(self):
        all_words = {}
        for files in self.file_names:
            with open(files, encoding='utf-8') as file:
                all_words[files] = remove_punctuation(file.read())

        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count_in = words.count(word)
            if count_in > 0:
                result[name] = count_in
        return result


h1 = WordsFinder('file1.txt, file2.txt', 'file3.txt')

print(h1.get_all_words())
print(h1.find('file'))
print(h1.count('file'))
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего