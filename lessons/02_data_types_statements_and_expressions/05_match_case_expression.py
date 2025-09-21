# x = 2

# match x:
#     case 0:
#         print("x = 0")
#     case 1:
#         print("x = 1")
#     case _:
#         print("x is different from 0 or 1")

# class Point1d:
#     def __init__(self, x):
#         print("Point coordinates:", x)

# class Point2d:
#     def __init__(self, x, y):
#         print("Point coordinates:", x, y)

# class Point3d:
#     def __init__(self, x, y, z):
#         print("Point coordinates:", x, y, z)


# def create_point(point):
#     match point:
#         case(x, ):
#             return Point1d(x)
#         case(x, y):
#             return Point2d(x, y)
#         case(x, y, z):
#             return Point3d(x, y, z)
#         case _:
#             print("Not a point we support.")

# create_point((1, ))
# create_point((3, 4))
# create_point([5, 6, 7])
# create_point(1)

shipping_cost = 0

def calculate_shipping_cost(item_size):
    match(item_size):
        case 'small':
            return 10
        case 'medium':
            return 15
        case 'big':
            return 20
        case 'large':
            return 30

flag = True

while flag:
    item_size = input("Enter size of item (small, medium, big, large): ")
    flag = False if item_size == 'small' or item_size == 'medium' or item_size == 'big' or item_size == 'large' else True

    if flag == 0:
        print("Shipping cost equal: {}.".format(calculate_shipping_cost(item_size)))



