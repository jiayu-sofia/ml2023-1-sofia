class Value:
    def __init__(self):
        self.value = None

    def get_value(self):
        self.value = input('Enter your value: ')
        print('Value entered:', self.value)


class Number:
    def __init__(self):
        self.N = None

    def get_number(self):
        self.N = input('Enter a positive number: ')
        print('Number entered:', self.N)


class Dict:
    def __init__(self):
        self.dict = {}

    def get_dict(self, N):
        for i in range(int(N)):
            value = input('Enter your value: ')
            print('Value entered:', value)
            self.dict[i] = value


class Search:
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def search_value(self):
        final_value = input('Enter your value: ')
        found = False
        for i, value in self.input_dict.items():
            if value == final_value:
                print('Index of your input:', i + 1)
                found = True
                break
        if not found:
            print('Index of your input:', -1)


def main():
    value_input = Value()
    value_input.get_value()

    number_input = Number()
    number_input.get_number()

    dict_input = Dict()
    dict_input.get_dict(number_input.N)

    search_input = Search(dict_input.dict)
    search_input.search_value()


if __name__ == "__main__":
    main()
