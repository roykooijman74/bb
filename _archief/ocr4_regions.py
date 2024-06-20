"""Python3.11"""
import signal

SMURFWINDOWS = [
    [2560, 0, 790, 460, 'Smurf 1'],
    [3414, 0, 790, 460, 'Smurf 2'],
    [4267, 0, 790, 460, 'Smurf 3'],
    [2560, 461, 790, 460, 'Smurf 4'],
    [3414, 461, 790, 460, 'Smurf 5'],
    [4267, 461, 790, 460, 'Smurf 6'],
    [2560, 921, 790, 460, 'Smurf 7'],
    [3414, 921, 790, 460, 'Smurf 8'],
    [4267, 921, 790, 460, 'Smurf 9'],
    [1770, 0, 790, 460, 'Smurf 0'],
    [1770, 461, 790, 460, 'A Supersmurf'],
    [1770, 921, 790, 460, 'B MiniSmurf']
]


def enablectrlc():
    '''enable ctrl-c'''
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def main():
    '''main function'''
    enablectrlc()

    smurf1_corrected_coords = SMURFWINDOWS[0][0:4]
    smurf1_corrected_region = [3223, 61, 3290, 73]

    x, y = smurf1_corrected_coords[0:2]
    x2, y2, x2end, y2end = smurf1_corrected_region[0:4]
    x_delta = x2-x
    y_delta = y2-y
    x_width = x2end-x2
    y_width = y2end-y2

    for roi in SMURFWINDOWS:
        xx = roi[0]+x_delta
        yy = roi[1]+y_delta
        print(xx, yy, x_width, y_width, roi)


if __name__ == '__main__':
    main()
