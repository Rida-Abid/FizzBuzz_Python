import sys

class Program:
    def main():
        args = sys.argv[1:]

        if (len(args) != 5):
            print ("error:enter 5 words")
            print ("usage: enter 5 words")

        else:
            list = []
            list = args
            print(list)
           


    if __name__ == '__main__':
        main()