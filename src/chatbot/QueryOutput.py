from prettytable import PrettyTable


class QueryOutput:
    def __init__(self, queryNumber, query, message):
        self.queryNumber = queryNumber
        self.query = query
        self.message = message

    def printQuery2(self, results):
        t = PrettyTable(['Course', 'Grade', 'Term', 'Year'])
        t.align["Course"] = "l"
        t.align["Grade"] = "l"
        t.align["Term"] = "l"
        t.align["Year"] = "l"

        i = 1
        for row in results:
            result = []
            for entry in row:
                result.append(str(entry))
            t.add_row(result)
            i = i + 1
        print(t)

    def printQuery4(self, results):
        t = PrettyTable(['Student Name', 'Id', 'Email'])
        t.align["Student Name"] = "l"
        t.align["Id"] = "l"
        t.align["Email"] = "l"
        i = 1
        for row in results:
            result = []
            for entry in row:
                result.append(str(entry))
            t.add_row(result)
            i = i + 1
        print(t)

    def printQueryWithTable(self, results):
        queryTwoOrFour = self.queryNumber == 2 or self.queryNumber == 4
        if queryTwoOrFour:
            if self.queryNumber == 2:
                self.printQuery2(results)
            if self.queryNumber == 4:
                self.printQuery4(results)
        return queryTwoOrFour