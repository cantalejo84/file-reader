import sys
import os
import datetime


def is_line_valid(line_list, output_file):
    try:
        a = int(line_list[0])
        b = line_list[1]
        c = line_list[2]
        return True
    except ValueError or IndexError:
        error_file = 'outputs/error_'+output_file
        exists = os.path.isfile(error_file)
        if exists:
            with open('outputs/error_'+output_file, 'a') as f3:
                f3.write(' '.join(line_list))
        else:
            f4 = open(error_file, 'w')
            f4.write(' '.join(line_list))
            f4.close()
        return False


def checker(file, init_datetime, end_datetime, hostname):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_folder = 'outputs'
    output_file = 'batch_out_'+str(init_datetime)+'_'+str(end_datetime)+'_'+hostname+'_'+now+'.csv'
    output_path = output_folder+'/'+output_file
    f = open(output_path, 'w')
    f.close()
    flag_csv = True
    with open(file) as f:
        line = f.readline()
        while line:
            line_list = list(line.strip().split(" "))
            if is_line_valid(line_list, output_file):
                time = int(line_list[0])
                host_origin = line_list[1]
                host_dest = line_list[2]
                if init_datetime <= time <= end_datetime and host_dest == hostname:
                    with open(output_path, 'a') as f2:
                        if flag_csv:
                            f2.write(host_origin)
                            flag_csv = False
                        else:
                            f2.write(';'+host_origin)

            line = f.readline()


def main():

    if len(sys.argv) != 5:
        print("ERROR: The correct arguments format are: <file> <unix_init_date> <unix_end_date> <hostname>")
        sys.exit()

    file, init_datetime, end_datetime, hostname = sys.argv[1:]

    if not os.path.isfile(file):
        print("ERROR: File \"{}\" not exist".format(file))
        sys.exit()

    try:
        init_datetime = int(init_datetime)
    except ValueError:
        print("ERROR: The argument \"{}\" must be numeric".format(init_datetime))
        sys.exit()

    try:
        end_datetime = int(end_datetime)
    except ValueError:
        print("ERROR: The argument \"{}\" must be numeric".format(end_datetime))
        sys.exit()

    if end_datetime < init_datetime:
        print("ERROR: The argument <unix_end_date> must be greater than <unix_init_date>")
        sys.exit()

    checker(file, init_datetime, end_datetime, hostname)


if __name__ == '__main__':
    main()
