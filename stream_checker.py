import sys
import os
import time
from datetime import datetime, timedelta
from collections import Counter


def stream_checker(filename, host_proc1, host_proc2):

    file = open(filename, 'r')
    where = file.tell()

    while 1:
        dict_counter = []
        host = ''
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        output_folder = 'outputs'

        output_file_proc1 = 'stream_out_proc1_' + host_proc1 + '_' + now + '.csv'
        output_path_proc1 = output_folder + '/' + output_file_proc1
        f_out_1 = open(output_path_proc1, 'w')
        f_out_1.close()

        output_file_proc2 = 'stream_out_proc2_' + host_proc2 + '_' + now + '.csv'
        output_path_proc2 = output_folder + '/' + output_file_proc2
        f_out_2 = open(output_path_proc2, 'w')
        f_out_2.close()

        output_file_proc3 = 'stream_out_proc3_' + now + '.csv'
        output_path_proc3 = output_folder + '/' + output_file_proc3
        f_out_3 = open(output_path_proc3, 'w')
        f_out_3.close()

        file.seek(where)
        line = file.readline()
        flag_csv_1 = True
        flag_csv_2 = True
        while line:
            line_list = list(line.strip().split(" "))
            host_origin = line_list[1]
            host_dest = line_list[2]

            line_list = list(line.strip().split(" "))
            dict_counter.append(line_list[1])
            for x in Counter(dict_counter).most_common(1):
                host = x[0]

            if host_dest == host_proc1:
                with open(output_path_proc1, 'a') as f1:
                    if flag_csv_1:
                        f1.write(host_origin)
                        flag_csv_1 = False
                    else:
                        f1.write(';' + host_origin)

            if host_origin == host_proc2:
                with open(output_path_proc2, 'a') as f2:
                    if flag_csv_2:
                        f2.write(host_dest)
                        flag_csv_2 = False
                    else:
                        f2.write(';' + host_dest)

            line = file.readline()
            where = file.tell()+1

        with open(output_path_proc3, 'a') as f3:
            f3.write(host)

        new_date = datetime.now() + timedelta(minutes=1)
        while datetime.now() < new_date:
            time.sleep(1)


def main():

    if len(sys.argv) != 4:
        print("ERROR: The correct arguments format are: <file> <hostname_proc1> <hostname_proc2>")
        sys.exit()

    if len(sys.argv) == 2:
        file = sys.argv[2]
    else:
        file, host_proc1, host_proc2 = sys.argv[1:]

    if not os.path.isfile(file):
        print("ERROR: File \"{}\" not exist".format(file))
        sys.exit()

    stream_checker(file, host_proc1, host_proc2)


if __name__ == '__main__':
    main()
