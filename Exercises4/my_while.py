conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)