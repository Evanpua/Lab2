import statistics

print("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    x=input()
    k=x.split(',')
    float_list=[float(num) for num in k]
    print("List of floats:",float_list)
    return float_list
def calc_average(float_list):
   average = sum(float_list) / len(float_list)
   return average



def find_min_max(float_list):
    minimum = min(float_list)
    maximum = max(float_list)
    return minimum, maximum


def sort_temperature():
    print("sort_temperature")

def calc_median_temperature(float_list):
   print("Median =" + str(statistics.median(float_list)))



display_main_menu()
x = get_user_input()
min , max = find_min_max(x)
average = calc_average(x)
print("Min value = " + str(min))
print("Max value = " + str(max))
print("Average = " + str(average))
calc_median_temperature(x)