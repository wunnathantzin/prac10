def main():
    in_file = open("data.txt","r")
    in_file.close()
    data = get_data(in_file)
    get_average(data, len(data))


def get_data(in_file):
    data = []
    for line in in_file:
        data.append(float(line))
    return data


def get_average(data, length):
    average = sum(data) / length
    print("The average is", average)


main()