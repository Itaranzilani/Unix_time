from datetime import datetime

class UnixTimeConverter:
     def __init__(self):
         pass

     @staticmethod
     def from_unix_time(unix_time):
         """Convert Unix time to normal time."""
         return datetime.utcfromtimestamp(unix_time)

     @staticmethod
     def to_unix_time(normal_time):
         """Convert regular time to Unix time."""
         return int(normal_time.timestamp())


# Create a class object
converter = UnixTimeConverter()

# Convert the current time to Unix time
current_unix_time = converter.to_unix_time(datetime.now())
print("Current Unix time:", current_unix_time)

# Convert Unix time back to normal time
converted_normal_time = converter.from_unix_time(current_unix_time)
print("Converted normal time:", converted_normal_time)
