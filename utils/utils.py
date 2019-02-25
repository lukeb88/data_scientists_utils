def print_loading(i, total):
    '''
        Just print a loader

        Attributes:
            - i         (int) : actual cycle iterator
            - total     (int) : total elements of the cycle
    '''

    TOTAL_ASHTAG = 20

    i = i + 1

    perc = TOTAL_ASHTAG * i / total

    # 20 : 100 = perc : X
    perc_100 = 100 * perc / 20

    num_ashtag = int(perc)

    s = ''
    for i in range(0, num_ashtag):
        s += '#'

    if num_ashtag < 20:
        for i in range(num_ashtag, 20):
            s += ' '

    output = float("%0.2f"%perc_100)
    print ('|' + s + '| ' + str(output) + '%', end="\r")