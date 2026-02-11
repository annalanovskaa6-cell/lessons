def log_action(func):
    def wrapper():
        print(f"Выполняется {func.__name__}...")
        return func()
    return wrapper
@log_action
def read_sales():
    with open('transactions.txt', 'r', encoding="utf-8") as f:
        sales = []
        for line in f:
            a = line.strip().split(', ')
            sales.append((a[0], a[1], a[2].strip("\n")))
        return sales
@log_action
def get_total_by_category(category):
    with open ('transactions.txt', encoding="utf-8") as f:
        total = 0
        for line in f:
            a = line.split(',')
            if a[1] == category:
                total += float(a[2].strip("\n"))
    return total
@log_action
def get_average_sales(category):
    with open('transactions.txt', encoding="utf-8") as f:
        s = 0
        count = 0
        for line in f:
            a = line.split(',')
            if a[1] == category:
                count += 1
                s += float(a[2].strip("\n"))
    return s / count
print(read_sales())