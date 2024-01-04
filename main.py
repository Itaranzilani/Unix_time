from datetime import datetime

class UnixTimeConverter:
     def __init__(self):
         pass

     @staticmethod
     def from_unix_time(unix_time):
         return datetime.utcfromtimestamp(unix_time)

     @staticmethod
     def to_unix_time(normal_time):
         return int(normal_time.timestamp())


converter = UnixTimeConverter()

current_unix_time = converter.to_unix_time(datetime.now())
print("Current Unix time:", current_unix_time)

converted_normal_time = converter.from_unix_time(current_unix_time)
print("Converted normal time:", converted_normal_time)
