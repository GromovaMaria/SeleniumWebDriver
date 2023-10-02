
def calculate_profit(N, M, X):
    periods = N//M
    total_profit = 0

    for i in range(periods):
        start_floor = M * i + 1
        end_floor = min(start_floor + M, N + 1)
        cost = X + (1000 * M * i)  # Стоимость квартиры в текущем периоде
        total_profit += cost * (end_floor - start_floor)
    return total_profit

N = 30 # Кол-во этажей в доме
M = 10 # Период возрастания стоимости (этаж.)
X = 10000 # Стоимость кв. на 1 этаже

profit = calculate_profit(N, M, X)
print(profit)