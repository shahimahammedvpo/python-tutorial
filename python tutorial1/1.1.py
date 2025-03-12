def convert_seconds(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
total_seconds = int(input("Enter time in seconds: "))
formatted_time = convert_seconds(total_seconds)
print(f"Time in HH:MM:SS format: {formatted_time}")