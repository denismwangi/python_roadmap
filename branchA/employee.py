class EmployeeRecord:
    def __int__(self, n, i, r):
        self.name = n
        self.id = i
        self.pay_rate = r


# noinspection PyArgumentList
def open_database(filename, db):
    lines = open(filename)
    for line in lines:
        name, id, rate = eval(line)

        db.append(EmployeeRecord(name, id, rate))
    lines.close()
    return True


def print_database(db):
    for rec in db:
        print(str.format("{:>5}: {:<10} {:<6.2f}", \
                         rec.id, rec.name, rec.pay_rate))


def less_than_by_name(el, e2):
    return el.name < e2.name


def less_than_by_id(el, e2):
    return el.id < e2.id


def less_than_by_pay(el, e2):
    return el.pay_rate < e2.pay_rate


def sort(db, comp):
    n = len(db)
    for i in range(n - 1):
        smallest = i;

        for j in range(i + 1, n):
            if comp(db[j], db[smallest]):
                smallest = j
        if smallest != i:
            db[i], db[smallest] = db[smallest], db[i]


def main():
    database = []

    if open_database("data.dat", database):
        print("-------------unsorted:")
        print_database(database)

        sort(database, less_than_by_name)
        print("-------------Name Order:")
        print_database(database)

        sort(database, less_than_by_id)
        print("------------ ID ORDER:")
        print_database(database)

        sort(database, less_than_by_pay)
        print("--------------Pay Order")
        print_database(database)

    else:
        print("could not open database file")


main()
