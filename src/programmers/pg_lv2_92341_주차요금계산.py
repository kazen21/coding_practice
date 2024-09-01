
from collections import defaultdict
from math import ceil
def solution(fees, records):
    answer = []

    car_info = defaultdict(list)

    #car_info , car_num= status, in_time, out_time, 누적주차시간

    for r in records:
        time, num, status = r.split(" ")

        if status == "IN":
            if num in car_info:
                car_info[num][0] = status
                car_info[num][1] = time
                car_info[num][2] = ""
                # car_info[num][3] = 0
            else:
                car_info[num] = [status, time, "", 0]
        else:
            car_info[num][0] = "OUT"
            car_info[num][2] = time
            park_time(num, car_info)


    for car in car_info:
        if car_info[car][0] == "IN":
            park_time(car, car_info)

    # print(car_info)
            # return
    car_sort = sorted(car_info.keys())
    print(car_sort)

    result = 0
    for key in car_sort:
        if car_info[key][3] <= fees[0]:
            result = fees[1]
        else:
            result = fees[1] + ceil((car_info[key][3]-fees[0])/fees[2])*fees[3]
    # print(result)
        answer.append(result)
    return answer

def park_time(num, car_info):

    # for car in car_info:
    # print()
    # print(car_info)
    # return
    if car_info[num][0] == "OUT":
        # print(car)
        time_dur = time_duration(car_info[num][1], car_info[num][2])
        # if num == "0000":
        #     print(car_info[num])
        car_info[num][3] += time_dur

    else:
        time_dur = time_duration(car_info[num][1], "23:59")
        # if num == "0000":
            # print(car_info)
        car_info[num][3] += time_dur

def time_duration(inTime, outTime):
    # print(inTime, outTime)
    in_h, in_m = map(int, inTime.split(":"))
    out_h, out_m = map(int, outTime.split(":"))

    in_minutes = in_h*60 + in_m
    out_minutes = out_h*60 + out_m
    time_dur = int(out_minutes) - int(in_minutes)
    return time_dur


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# result = [14600, 34400, 5000]

print(solution(fees, records))
