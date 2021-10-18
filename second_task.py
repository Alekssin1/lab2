class Text:
    def __init__(self, name_of_file):
        self.file = name_of_file

    def count_words(self):
        try:
            data = open(self.file, 'r')
        except IOError or FileNotFoundError:
            print('File not found or path is incorrect')
            exit()
        count = 0
        for line in data:
            count += len(line.split())
        data.close()
        return count

    def count_symbols(self):
        try:
            data = open(self.file, 'r')
        except IOError or FileNotFoundError:
            print('File not found or path is incorrect')
            exit()
        count = 0
        for line in data:
            count += len(line)
        data.close()
        return count

    def count_sentence(self):
        try:
            data = open(self.file, 'r')
        except IOError or FileNotFoundError:
            print('File not found or path is incorrect')
            exit()
        sentence = 0
        stop_signs = ('. ', '.\n', '?', '...', '!')
        for line in data:
            for i in stop_signs:
                sentence += line.count(i)
        data.close()
        return sentence


file_name = "vlad.txt"
statistical_processing = Text(file_name)
print("Number of symbols: ", statistical_processing.count_symbols(), "\nNumber of words: ",
      statistical_processing.count_words(), "\nNumber of sentences: ", statistical_processing.count_sentence())
