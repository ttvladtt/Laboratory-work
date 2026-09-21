# Решение задания 7
def load_data():
    return [3, 17, 8, 25, 6, 12, 25, 9, 14]
def filter_above(values, threshold=10):
    return [x for x in values if x>threshold]
def mean(values):
    if not values:
        return 0
    return sum(values)/len(values)
