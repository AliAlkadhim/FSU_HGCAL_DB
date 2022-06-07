import csv; import re
filename="HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt"

# with open(filename) as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         print(row)
#         break

def get_V_I_lists(file):
    V_list=[]; I_list=[]
    with open(filename, "r") as f:
        fs = f.readlines()#.split('\n')
        for lineind, line in enumerate(fs):
            if 'Timestamp' in line:
                Timestamp=line.split('\t')[2]
            if 'Error' in line:
                headers = line
                headers_ind = lineind
                # print(headers.split('#'))
                rows_ind = headers_ind + 2
                rows = fs[rows_ind:]
                for row in rows[:10]:
                    # print(row)
                    fields = row.strip().split('\t')
                    voltage = float(fields[0])
                    V_list.append(voltage)
                    channel = float(fields[1])
                    # current=float(fields[2])
                    # error=float(fields[3])
                    total_current=float(fields[4])
                    I_list.append(total_current)
                    
    return V_list, I_list, Timestamp


V_list, I_list, Timestamp = get_V_I_lists(filename)

                    

                
if __name__ == '__main__':
    V_list, I_list, Timestamp = get_V_I_lists(filename)
    print(V_list)