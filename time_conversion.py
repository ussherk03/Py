
def time_conversion (time=input()) :
    time_arr = time.split(':')
    hour = int(time_arr[0])

    if 'PM' in time:
        time_arr.insert(0, repr(hour + 12))

    else:
        time_arr.insert(0, repr(hour))

    return ':'.join(time_arr)

new_time = time_conversion()

print(new_time)



















