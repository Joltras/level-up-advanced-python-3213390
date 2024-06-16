# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
import os
import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    dir_path = os.path.dirname(os.path.realpath(__file__))  # get the directory of the current file
    file_path = os.path.join(dir_path, '10k_racetimes.txt')  # join the directory path with the file name
    with open(file_path, 'rt') as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()

    rhine_times = re.findall(r'.*Jennifer Rhines.*', races)
    times = []
    for rhine_time in rhine_times:
        times.append(re.findall(r'\d{2}:\d{2}\.?[0-9]{0,3}', rhine_time)[0])
    print(times)
    return times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total_milliseconds = 0
    for racetime in racetimes:
        times = racetime.split(':')
        minutes = int(times[0])
        seconds = 0
        milliseconds = 0
        if '.' in times[1]:
            seconds = int(times[1].split('.')[0])
            milliseconds = int(times[1].split('.')[1])
        else:
            seconds = int(times[1])
        total_milliseconds += milliseconds + (seconds * 1000) + (minutes * 60 * 1000)

    # Calculate average total milliseconds
    average_milliseconds = total_milliseconds / len(racetimes)

    # Convert average milliseconds back to minutes, seconds, and milliseconds
    average_minutes = int(average_milliseconds // (60 * 1000))
    average_seconds = (average_milliseconds % (60 * 1000)) / 1000
    whole_seconds = int(average_seconds)
    milliseconds = int((average_seconds - whole_seconds) * 10)  # We need only the first digit of milliseconds

    # Formatting the result
    average_time = f'{average_minutes:02}:{whole_seconds:02}.{milliseconds}'
    return average_time
