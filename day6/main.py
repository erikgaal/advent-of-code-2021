from collections import deque

def prepare_input(input):
    fish = deque([0] * 9)

    for x in map(lambda x: int(x), input.split(',')):
        fish[x] = fish[x] + 1

    return fish

def lanternsim(fish, day=0, max_days=0):
    while day < max_days:
        # Every fish's timer advances one day
        fish.rotate(-1)
        # We create a new fish for every fish that had its timer reset.
        fish[6] = fish[6] + fish[8]

        return lanternsim(
            fish=fish,
            day=day+1,
            max_days=max_days
        )

    return sum(fish)


if __name__ == '__main__':
    with open('input', 'r') as file:
        fish = prepare_input(file.read())

        print("There are %i lanternfish in the sea." % lanternsim(fish, max_days=256))
