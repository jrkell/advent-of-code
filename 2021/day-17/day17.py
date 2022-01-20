# TODO read from file...
target_x_start = 96
target_x_end = 125
target_y_start = -144
target_y_end = -98

def hitTarget(x, y):
    return (target_x_start <= x <= target_x_end and target_y_start <= y <= target_y_end)

def main(part2 = False):
    winner_y_list = []
    winner_init_vel_list = []

    for init_x_velocity in range(0, target_x_end+1):
        for init_y_velocity in range(target_y_start, target_y_start*-1+1):
            x_velocity = init_x_velocity
            y_velocity = init_y_velocity
            position = [0,0]
            max_y = 0
            while position[1] > target_y_start:
                if position[1] > max_y:
                    max_y = position[1]

                position[0] += x_velocity 
                position[1] += y_velocity
                x_velocity = max(0, x_velocity-1)
                y_velocity -= 1
                if hitTarget(position[0], position[1]):
                    winner_y_list.append(max_y)
                    winner_init_vel_list.append((init_x_velocity, init_y_velocity))

    if not part2:
        return max(winner_y_list)
    return len(set(winner_init_vel_list))

if __name__ == '__main__':
    print('Part 1 = ' + str(main()))
    print('Part 2 = ' + str(main(True)))