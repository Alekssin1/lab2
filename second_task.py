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
        stop_signs = ('.', '!', '?')
        spaces = (' ', '    ', '\n')
        first_enter = True
        for line in data:
            for i in line:
                if i in stop_signs and first_enter:
                    sentence += 1
                    first_enter = False
                elif i not in spaces and i not in stop_signs:
                    first_enter = True
        data.close()
        return sentence

    def __str__(self):
        return "Number of symbols: " + str(self.count_symbols()) + "\nNumber of words: " + \
               str(self.count_words()) + "\nNumber of sentences: " + str(self.count_sentence())


file_name = "vlad.txt"
statistical_processing = Text(file_name)
print(statistical_processing)
