# 4128 with optimization, 5213 ms without
import math

# from pybloom import BloomFilter

num_moons = 4
# pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
# pos = [[14, 9, 14], [9, 11, 6], [-6, 14, -4], [4, -4, -3]]
pos = [[-4, -14, 8], [1, -8, 10], [-15, 2, 1], [-17, -17, 16]]
vel = [[0, 0, 0] for _ in range(num_moons)]
steps = 0
total_steps = 1000

run_x = True
run_y = True
run_z = True


def determine_acc(this_pos, other_pos):
    delta = this_pos - other_pos
    if delta == 0:
        return 0
    elif delta < 0:
        return 1
    else:
        return -1


def calc_vel():
    for i in range(num_moons):
        i_pos = pos[i]
        for j in range(num_moons):
            if i == j:
                continue  # same moon

            j_pos = pos[j]
            if run_x:
                vel[i][0] += determine_acc(i_pos[0], j_pos[0])

            if run_y:
                vel[i][1] += determine_acc(i_pos[1], j_pos[1])

            if run_z:
                vel[i][2] += determine_acc(i_pos[2], j_pos[2])


def update_pos():
    for i in range(num_moons):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]
        pos[i][2] += vel[i][2]


x_history = set()
x_period = None
y_history = set()
y_period = None
z_history = set()
z_period = None

# bloom_filter = BloomFilter(error_rate=0.0000000001, max_number_of_element_expected=int(10e15))

# for _ in range(total_steps):
for t in range(100000000000000):
    if x_period and y_period and z_period:
        break
    calc_vel()
    update_pos()
    if not x_period:
        x_now = (pos[0][0], pos[1][0], pos[2][0], pos[3][0], vel[0][0], vel[1][0], vel[2][0], vel[3][0])
        if x_now in x_history:
            x_period = t
            print(x_period)
            run_x = False
        else:
            x_history.add(x_now)
    if not y_period:
        y_now = (pos[0][1], pos[1][1], pos[2][1], pos[3][1], vel[0][1], vel[1][1], vel[2][1], vel[3][1])
        if y_now in y_history:
            y_period = t
            print(y_period)
            run_y = False
        else:
            y_history.add(y_now)
    if not z_period:
        z_now = (pos[0][2], pos[1][2], pos[2][2], pos[3][2], vel[0][2], vel[1][2], vel[2][2], vel[3][2])
        if z_now in z_history:
            z_period = t
            print(z_period)
            run_z = False
        else:
            z_history.add(z_now)

e_tot = 0

for i in range(num_moons):
    e = abs(pos[i][0]) + abs(pos[i][1]) + abs(pos[i][2])
    f = abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2])
    e_tot += e * f

print(f'total energy = {e_tot}')


def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


print(f'Overall period = {lcm(lcm(x_period, y_period), z_period)}')
