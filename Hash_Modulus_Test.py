# Modulus Hash test to determine if loction of modulus affects the hash time
# significantly.

import time
import datetime

# Performs a string hash utilizing a single modulus operation.
def hash_string_single_modulus(keyword, buckets):
    bucket = 0
    for chars in keyword:
        bucket += ord(chars)
    bucket = bucket % buckets
    return bucket

# Performs a string hash utilizing a modulus operation for each character in the string.
def hash_string_multiple_modulus(keyword, buckets):
    bucket = 0
    for chars in keyword:
        bucket = bucket + (ord(chars)) % buckets
    return bucket

# Tests the hash provided with slowly mutating strings.
def test_hash(hash, str_len, cnt):
    str_ = create_str(str_len)
    str_cnt = 0
    start = time.clock()
    while str_cnt < cnt:
        word = make_string(str_)
        useless_return = hash(word, 12) # Return is unnecessary to process as we are measuring the length of hash()
        str_ = mutate_str(str_)
        str_cnt += 1
    stop = time.clock()
    return stop - start

# Creates a string (Python List of Characters) to be used by test_hash
def create_str(length):
    str_ = []
    cnt = 0
    while cnt < length:
        str_.append('a')
        cnt += 1
    return str_

# Mutates the string (Python List of Characters) provided by incrementing the characters.
def mutate_str(str_):
    for i in range(len(str_) - 1, 0, -1):
        if str_[i] < 'z':
            str_[i] = chr(ord(str_[i]) + 1)
            break
        else:
            str_[i] = 'a'
    return str_

# Turns a Python List of Characters "String" into a real String object.
def make_string(str_):
    s = ""
    for e in str_:
        s = s + e
    return s

# Performs test_hash loop times and averages the result
def average(hash, str_size, cnt, loop):
    time_cnt = 0
    loop_cnt = 0
    while loop_cnt < loop:
        time_cnt += test_hash(hash, str_size, cnt)
        loop_cnt += 1
    return time_cnt / loop

# Creates a report string for reporting the status of the test
def report_string(multiple, average, seconds, size, count, loop):
    str_return = ""
    
    if multiple:
        str_return += 'MULTIPLE '
    else:
        str_return += 'SINGLE '
    str_return += 'MODULUS HASH '
    if average:
        str_return += 'AVERAGE: '
    else:
        str_return += 'TOOK: '    
    str_return += str(seconds)
    str_return += " SECONDS FOR A "
    str_return += str(size)
    str_return += " CHARACTER STRING, "
    str_return += str(count)
    str_return += " TIMES"
    if loop != -1:
        str_return += ", LOOPED "
        str_return += str(loop)
        str_return += " TIMES."
    else:
        str_return += "."
        
    return str_return 

# These values are used for controlling the variables of the test.  Use the to 
# construct your own tests!  Remember to ensure that only one variable is 
# changing in a single test.
str_size_1, cnt_1, loop_1 = 20, 10000000, 10
str_size_2, cnt_2, loop_2 = 50, cnt_1, loop_1
str_size_3, cnt_3, loop_3 = 100, cnt_1, loop_1


# The following code is used to log the data collected.  This was needed as
# running the program took several hours.  I fully intend to take this code, and
# with some modifications produce a Logger module to easily make log files my
# next programming endeavor.  If there is already a default Logging module in 
# Python, I will no doubt come along it later, when I get to know the language
# better.
filename = "[LOG]Hash_Modulus_Test.dat"

start_time = time.clock()

FILE = open(filename,'wb')

current_string = "TESTING HASH STRING SINGLE VS MULTIPLE MODULUS"
print current_string
FILE.write(current_string + '\n')
current_string = report_string(False, False, test_hash(hash_string_single_modulus, str_size_1, cnt_1), str_size_1, cnt_1, -1)
print current_string
FILE.write(current_string + '\n')
current_string = report_string(True, False, test_hash(hash_string_multiple_modulus, str_size_1, cnt_1), str_size_1, cnt_1, -1)
print current_string
FILE.write(current_string + '\n')
current_string = ""
current_string = report_string(False, False, test_hash(hash_string_single_modulus, str_size_2, cnt_2), str_size_2, cnt_2, -1)
print current_string
FILE.write(current_string + '\n')
current_string = report_string(True, False, test_hash(hash_string_multiple_modulus, str_size_2, cnt_2), str_size_2, cnt_2, -1)
print current_string
FILE.write(current_string + '\n')
current_string = ""
current_string = report_string(False, False, test_hash(hash_string_single_modulus, str_size_3, cnt_3), str_size_3, cnt_3, -1)
print current_string
FILE.write(current_string + '\n')
current_string = report_string(True, False, test_hash(hash_string_multiple_modulus, str_size_3, cnt_3), str_size_3, cnt_3, -1)
print current_string
FILE.write(current_string + '\n')

current_string = ""
print current_string
FILE.write(current_string + '\n')
current_string = "***"
print current_string
FILE.write(current_string + '\n')
current_string = ""
print current_string
FILE.write(current_string + '\n')

current_string = "AVERAGE HASH STRING SINGLE VS MULTIPLE MODULUS"
print current_string
FILE.write(current_string + '\n')
current_string = report_string(False, True, average(hash_string_single_modulus, str_size_1, cnt_1, loop_1), str_size_1, cnt_1, loop_1)
print current_string
FILE.write(current_string + '\n')
current_string = report_string(True, True, average(hash_string_multiple_modulus, str_size_1, cnt_1, loop_1), str_size_1, cnt_1, loop_1)
print current_string
FILE.write(current_string + '\n')
current_string = ""
current_string = report_string(False, True, average(hash_string_single_modulus, str_size_2, cnt_2, loop_2), str_size_2, cnt_2, loop_2)
print current_string
FILE.write(current_string + '\n')
current_string = report_string(True, True, average(hash_string_multiple_modulus, str_size_2, cnt_2, loop_2), str_size_2, cnt_2, loop_2)
print current_string
FILE.write(current_string + '\n')
current_string = ""
current_string = report_string(False, True, average(hash_string_single_modulus, str_size_3, cnt_3, loop_3), str_size_3, cnt_3, loop_3)
print current_string
FILE.write(current_string + '\n')
current_string = report_string(True, True, average(hash_string_multiple_modulus, str_size_3, cnt_3, loop_3), str_size_3, cnt_3, loop_3)
print current_string
FILE.write(current_string + '\n')

current_string = ""
print current_string
FILE.write(current_string + '\n')
current_string = "***"
print current_string
FILE.write(current_string + '\n')
current_string = ""
print current_string
FILE.write(current_string + '\n')

# This portion of code is used to determine the amount of time the entire 
# program spent running.  (Because I was curious. :P)
stop_time = time.clock()
app_length_s = stop_time - start_time
app_length = str(datetime.timedelta(seconds=app_length_s))

timestamp = []
prev_end = 0
chr_cur = 0
for char in app_length:
    if char == ':':
        timestamp.append(app_length[prev_end:chr_cur])
        prev_end == chr_cur + 1
    chr_cur += 1
timestamp.append(app_length[prev_end:chr_cur])

hours, minutes, seconds = timestamp[0], timestamp[1], timestamp[2]

current_string = "THIS APPLICATION TOOK " + hours + " HOURS " + minutes + " MINUTES AND " + seconds + " SECONDS TO COMPLETE."
print current_string
FILE.write(current_string + '\n')

FILE.close()

print "[LOG] FILE COMPLETED - ENDING PROGRAM"