class Text:
    def __init__(self, file):
        try:
            self.file = open(file, 'r')
        except IOError or FileNotFoundError:
            print('File not found or path is incorrect')
            exit()
        self.data = self.file.read()

    def count_words(self):
        return len(self.data.split())

    def count_symbols(self):
        return len(self.data)

    def count_sentence(self):
        sentence = 0
        stop_signs = ('. ', '.\n', '?', '...', '!')
        for i in stop_signs:
            sentence += self.data.count(i)
        return sentence


file_name = "vlad.txt"
statistical_processing = Text(file_name)
print("Number of symbols: ", statistical_processing.count_symbols(), "\nNumber of words: ",
      statistical_processing.count_words(), "\nNumber of sentences: ", statistical_processing.count_sentence())
