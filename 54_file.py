
# READ FILE
f = open('introduction', 'r')  # r represents read mode

print(f)
# <_io.TextIOWrapper name='introduction' mode='r' encoding='cp1252'>

# Read first line of file
print(f.readline(), end="")

# Read first four character of line
print(f.readline(4))

# Read entire file
print(f.read())


# WRITE FILE
f1 = open('introduction1', 'w')  # w represents write mode | file will be created if it doesn't exist
f1.write("Writing in file using python")


# APPEND IN FILE
f1 = open('introduction1', 'a')  # a represents append
f1.write("Further text appended")


# COPY FILE CONTENT
for data in f:
    f1.write(data)

# READ IMAGE FILE
f2 = open('me.jpg', 'rb')  # rb represents read binary
for data in f2:
    print(data)

# COPY IMAGE FILE
f3 = open('me1.JPG', 'wb')  # wb represents write binary
for data in f2:
    f3.write(data)
