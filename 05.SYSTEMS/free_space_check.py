import uos

# Get filesystem information
filesystem_info = uos.statvfs('/')

# Calculate free space in bytes
free_space_bytes = filesystem_info[0] * filesystem_info[3]

# Print the free space
print("Free space available: {} bytes".format(free_space_bytes))
