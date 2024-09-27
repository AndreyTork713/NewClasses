
def main():
    class Books(object):

        def __init__(self, book):
            pass

        def __del__(self):
            pass

        def display_book(self):
            return self.book

        def take_one_book(self):
            return self.book -1

        def put_one_book(self):
            return self.book + 1


    a = Books()

    # new_list = list(input().split())
    new_list = input().split()


    for i in new_list:
        if i.isalpha():
            print(i, end=" ")
        if i.isdigit():
            print(a.display_book(int(i)), end=" ")
            print(a.take_one_book(a.display_book(int(i))), end=" ")
            print(a.put_one_book(a.take_one_book(a.display_book(int(i)))), end=" ")


if __name__ == '__main__':
    main()