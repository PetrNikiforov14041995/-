import json


class MyIterator:
    with open('countries.json', 'r') as file:
        text = json.load(file)
        for key in text:
            print(key)

    # def __init__(self, start, end):
    #     self.start = start - 1
    #     self.end = end
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.start += 1
    #     if self.start == self.end:
    #         raise StopIteration
    #     return self.start
