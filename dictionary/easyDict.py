import csv
#filename = "/home/emanuel/Downloads/python_dict/python_dict_data.txt"


def easyDict(nFile, sep="\t", subset='All', display=True):
    #open tab-delimited
    fileData = csv.reader(open(nFile, 'rb'), delimiter=sep)
    #select rows to display
    crt = type(subset)

    if crt == str:
        if subset == 'All':
            dct = {row[0]: row[1] for row in fileData}
        else:
            dct = None
    elif crt == int:
        sub = [subset - 1, subset]
    elif crt == list:
        sub = [subset[0] - 1, subset[1]]

    if crt != str:
        d = [row for row in fileData]
        rw = [d[i] for i in range(sub[0], sub[1])]
        dct = {row[0]: row[1] for row in rw}

    if display:
        for k, v in list(dct.items()):
            print(("{}: {}".format(k, v)))

    return dct
