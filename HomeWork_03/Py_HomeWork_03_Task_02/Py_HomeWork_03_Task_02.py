# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

# Ряд Нилаканта: π = 3 + 4/(2*3*4) — 4/(4*5*6) + 4/(6*7*8) — 4/(8*9*10) + 4/(10*11*12) — 4/(12*13*14) …


def calc_pi (difference : float): 
    number_pi = 3
    
    i = 2
    j = 0

    while (4/(i*(i+1)*(i+2))) > difference:
        number_pi += ((-1) ** j) * (4 /(i*(i+1)*(i+2)))
        i += 2
        j += 1

    number_pi += ((-1) ** j) * (4 /(i*(i+1)*(i+2)))

    return round(number_pi, (len(str(difference)))-2)

diff = 0.0001

print(f"число Пи с точностью {diff} = {calc_pi(diff)}")
