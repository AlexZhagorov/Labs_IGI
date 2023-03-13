FILE_NAME = '/home/my_ubuntu/labs/lab_2/Task_1/input.txt'

def get_text(flag):
    if flag == "f":
        return fileread()
    elif flag == "m":
        return consoleread()


def fileread():
    file = None
    file_data = None

    try:
        file = open(FILE_NAME, 'rt')
        file_data = file.read()
        file.close()
    except OSError:
        print("Problem with a file")
        file_data = None
        

    return file_data


def consoleread():
    return input()