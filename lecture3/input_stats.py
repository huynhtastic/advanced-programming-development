from operator import itemgetter

def input_stats(file_name):
    content = ""
    with open(file_name, 'r') as open_file:
        content = open_file.read().split()
    content = list(map(lambda x: [len(x), x], content))
    content.sort(key=itemgetter(0))
    print('{0} characters\n{1}'.format(*content[-1]))

def input_stats_looped(file_name):
    longest_line = []
    with open(file_name, 'r') as open_file:
        read_line = open_file.readline()
        longest_line = [len(read_line), read_line]
        for line in open_file.read().splitlines():
            if len(line) > longest_line[0]:
                longest_line = [len(line), line]
    print('{0} characters\n{1}'.format(*longest_line))

if __name__ == "__main__":
    input_stats('test.txt')
    input_stats_looped('test.txt')
