distance_mi = 7
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

if distance_mi == False:
    print('False')
elif distance_mi <= 1 and not is_raining:
    print('True')
elif distance_mi <= 1 and is_raining:
    print('False')
elif distance_mi < 1 and is_raining:
    print('False')
elif (distance_mi > 1 and distance_mi <= 6) and is_raining and not has_bike:
    print('False')
elif (distance_mi > 1 and distance_mi <= 6) and not is_raining and has_bike:
    print('True')
elif (distance_mi > 1 and distance_mi <= 6) and is_raining and not has_bike:
    print('False')
elif (distance_mi > 6) and has_ride_share_app:
    print('True')
elif (distance_mi > 6) and has_car:
    print('True')
else:
    print('False')