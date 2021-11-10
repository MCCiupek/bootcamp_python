from csvreader import CsvReader


if __name__ == "__main__":
    with CsvReader('good.csv') as myfile:
        data = myfile.getdata()
        header = myfile.getheader()

    # myfile = CsvReader('good.csv')
    # myfile.__enter__()
    # try:
    #     header = myfile.getheader()
    #     data = myfile.getdata()
    # finally:
    #     myfile.__exit__(0, 0, 0)
    print(header)
    print(data)