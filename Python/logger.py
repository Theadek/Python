class Logger:

    def __init__(self):
        self.__komunikaty = []

    def dodajLog(self, napis):
        self.__komunikaty.append(napis)

    def czyscLog(self):
        self.__komunikaty.clear()

    def piszLog(self):
        for i in self.__komunikaty:
            print(i)

    def getLog(self):
        return self.__komunikaty