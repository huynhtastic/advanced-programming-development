def compute_times(file_name):
    with open(file_name, 'r') as open_file:
        for line in open_file.read().splitlines():
            worker_info = line.split()
            total_time = sum(map(lambda x: float(x), worker_info[2:]))
            average_time = total_time / len(worker_info[2:])
            print('{0} ID {1} worked {2} hours: {3} / day'.format(
                worker_info[0], worker_info[1], total_time, average_time))

def show_lines(file_name):
    with open(file_name, 'r') as open_file:
        all_lines = open_file.read()
        print(all_lines)
        split_lines = all_lines.splitlines()
        print(split_lines)

if __name__ == "__main__":
    compute_times('hours.txt')
#    show_lines('hours.txt')
