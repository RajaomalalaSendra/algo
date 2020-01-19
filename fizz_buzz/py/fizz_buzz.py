# fizz buzz
class FizzBuzz:
    def __init__(self, listFizzBuzz):
        self.listFizzBuzz = listFizzBuzz

    def returnFizzBuzz(self):
        fizz_buzz = list()

        for i in self.listFizzBuzz:
            if i % 15 == 0:
                fizz_buzz.append("fizz buzz")
            elif i % 3 == 0:
                fizz_buzz.append("fizz")
            elif i % 5 == 0:
                fizz_buzz.append("buzz")
            else:
                fizz_buzz.append(i)
        
        return fizz_buzz


def getListFizzBuzz():
    listFizzBuzz = list()
    while True:
        line = input(">> ")
        try:
            listFizzBuzz.append(int(line))
        except ValueError:
            if line == "stop":
                break
            else:
                print("You must enter an integer number")
    return listFizzBuzz

if __name__ == "__main__":
    listFizzBuzz = getListFizzBuzz()
    fizzBuzz = FizzBuzz(listFizzBuzz)
    if fizzBuzz != []:
        fizzBuzz.returnFizzBuzz()
