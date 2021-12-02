def depth(input, aiming = False):
    x, depth, aim = 0, 0, 0

    for line in input:
        [dir, dis] = line.split(' ')
        dis = int(dis)

        if aiming:
            if dir == 'forward':
                x += dis
                depth += aim * dis
            elif dir == 'up':
                aim -= dis
            elif dir == 'down':
                aim += dis
        else:
            if dir == 'forward':
                x += dis
            elif dir == 'up':
                depth -= dis
            elif dir == 'down':
                depth += dis

    return x * depth


if __name__ == '__main__':
    with open("input", "r") as input:
        print("There result is %s." % depth(input, aiming=True))
