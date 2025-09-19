# Podstawowa forma i zastosowanie klauzuli match/case
x = 5

match x:
    case 0:
        print("x = 0")
    case 1:
        print("x = 1")
    case _:
        print("x is different from 0 or 1")

# Bardziej złożone zastosowanie klauzuli match/case
class Point1d:
    def __init__(self, x):
        print("Point coordinates:", x)

class Point2d:
    def __init__(self, x, y):
        print("Point coordinates:", x, y)

class Point3d:
    def __init__(self, x, y, z):
        print("Point coordinates:", x, y, z)

def create_point(point):
    match point:
        case (x, ):
            return Point1d(x)
        case (x, y):
            return Point2d(x, y)
        case (x, y, z):
            return Point3d(x, y, z)
        case _:
            print("Not a point we support.")

create_point((1, ))
create_point((1, 2))
create_point((1, 2, 3))
create_point(1)


# Praktyczne wykorzystanie klauzuli match/case
def calculate_shipping_cost(item):
    match item:
        case 'small':
            return 5.0
        case 'medium':
            return 10.0
        case 'large':
            return 15.0
        case _:
            return 20.0


item_size = input("Enter item size (small, medium, large): ")
shipping_cost = calculate_shipping_cost(item_size)
print("Shipping cost:", shipping_cost)
