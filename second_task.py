import re


class Text:
    def __init__(self, name_of_file):
        self.file = name_of_file
        try:
            data = open(self.file, 'r')
        except IOError:
            raise IOError("File can't be opened")
        except FileNotFoundError:
            raise FileNotFoundError('File not found or path is incorrect')
        data.close()

    def count_words(self):
        count = 0
        data = open(self.file, 'r')
        for line in data:
            count += len(re.findall(r"[A-Za-z']+", line))
        data.close()
        return count

    def count_symbols(self):
        data = open(self.file, 'r')
        count = 0
        for line in data:
            count += len(line) - line.count(' ') - line.count('\n')
        data.close()
        return count

    def count_sentence(self):
        data = open(self.file, 'r')
        sentence = 0
        for line in data:
            sentence += len(re.findall(r"\w+[.?!]+", line))
        data.close()
        return sentence

    def __str__(self):
        return "Number of symbols: " + str(self.count_symbols()) + "\nNumber of words: " + \
               str(self.count_words()) + "\nNumber of sentences: " + str(self.count_sentence())


file_name = "vlad.txt"
statistical_processing = Text(file_name)
print(statistical_processing)
