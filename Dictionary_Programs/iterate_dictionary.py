class IterateDictionary:
    def __init(self):
        self.dictionary_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    def iterate_over_dictionary(self):
        """
        iterating over dictionary using for loops
        """
        for key, value in self.dictionary_data.items():
            print(key, value)


if __name__ == "__main__":
    iteratedict = IterateDictionary()
    iteratedict.iterate_over_dictionary()