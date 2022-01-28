import datetime
from os import name, system

def date_delta(start, end):
	start = datetime.datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
	end = datetime.datetime.strptime(end,"%Y-%m-%d %H:%M:%S")
	return (end-start).total_seconds()
	
with open("result.txt", "r", encoding="utf-8") as f:
    content = f.readlines()

time_list = list()
name_list = list()

for i in range(1900, 2100):

    # 1900 年 1月 两日子只差
    # 1900-1#6日 02:03:57小寒#20日 19:32:25大寒
    for j in range(1, 13):

        t = ""
        for temp in content:
            if (str(i)+"-"+str(j)) in temp:
                t = temp
                break

        st = t.split("#")

        try:
            start_name = st[1].split(" ")[1][-2:]
            end_name = st[2].split(" ")[1][-3:-1]
        except:
            print(st)
            print(i)
            print(j)
            system("pause")

        time1 = str(i)+"-"+str(j)+"-"+st[1].split(" ")[0][:-1]+" "+st[1].split(" ")[1][:-2]
        time2 = str(i)+"-"+str(j)+"-"+st[2].split(" ")[0][:-1]+" "+st[2].split(" ")[1][:-3]

        name_list.append(start_name)
        name_list.append(end_name)

        time_list.append(time1)
        time_list.append(time2)

temp_result = list()
temp_string = ""
for i in range(0, len(name_list) - 1):

    if name_list[i] == "小寒":
        if temp_string != "":
            temp_result.append(temp_string)
        temp_string = ""
    time_diff = date_delta(time_list[i], time_list[i+1])
    temp_string = temp_string + str(int(time_diff)) + ", "

f = open("result_cc.txt", "w", encoding="utf-8")
for temp in temp_result:
    f.write(temp+"\n")
f.close()

            
