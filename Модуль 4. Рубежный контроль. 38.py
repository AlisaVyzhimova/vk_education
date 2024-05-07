import datetime

def parse_time(s: str):
     datetime.datetime
    parsed_time = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    shifted_time = parsed_time + datetime.timedelta(days=1)
    return shifted_time.day
string_datetime = "2023 03 03 12 30 00"
print(parse_time(string_datetime))
