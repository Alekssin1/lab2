class Text:
    def __init__(self, file):
        try:
            self.file = open(file, 'r')
        except IOError or FileNotFoundError:
            print('File not found or path is incorrect')
            exit()
        self.data = self.file.read()

    def count_words(self):
        words = self.data.split()
        return "\nNumber of words: " + str(len(words))

    def count_symbols(self):
        return "\nNumber of symbols: " + str(len(self.data))

    def count_sentence(self):
        sentence = 0
        stop_signs = ('. ', '.\n', '?', '?!', '...', '!')
        for i in stop_signs:
            sentence += self.data.count(i)
        return "\nNumber of sentences: " + str(sentence)


file_name = "vlad.txt"
statistical_processing = Text(file_name)
print(statistical_processing.count_symbols(), statistical_processing.count_words(),
      statistical_processing.count_sentence())
