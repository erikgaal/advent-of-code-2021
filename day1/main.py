import logging

DEFAULT_SLIDING_WINDOW = 1

def sonar(input, sliding_window = DEFAULT_SLIDING_WINDOW):
    increased_measurements = 0

    window = []

    for current in input:
        window.append(int(current))

        if len(window) <= sliding_window:
            continue

        previous_sum = sum(window[:-1])
        current_sum = sum(window[1:])

        difference = current_sum - previous_sum

        logging.debug("%s (%s)" % (current_sum, difference))

        if difference > 0:
            increased_measurements += 1

        if (len(window) > sliding_window):
            window.pop(0)
    
    return increased_measurements


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    with open("input", "r") as input:
        print("There were %s sums larger than the previous one." % sonar(input, 3))
