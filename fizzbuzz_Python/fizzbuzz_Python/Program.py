import sys
from Logic import logic

def main():
    args = sys.argv[1:]

    if len(args) != 3:
        print("error: missing input values")
        print("useage: enter fizzId, buzzId, maxCount")
    else:
        fizzId, buzzId, maxCount = args
        results = logic.process(int(fizzId), int(buzzId), int(maxCount))
        for result in results:
            print (result)
      

if __name__ == '__main__':
    main()