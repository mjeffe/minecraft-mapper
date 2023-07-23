import sys

# This will parse and output a data file appropriate for the mcmap call to
# gnuplot, given a data file with the following layaout:
#
#  location name: x y z
#
# where x y z are minecraft coordinates
#
# Note that I do some coordinate manipulation here:
#   - I swap y and z so that my 2D plot can use the x and y as x=east/west and y=north/south
#   - I reverse the direction of the y coordinate to make +y North and -y South
#

#import csv
## output for gnuplot
#def for_gnuplot(file):
#    with open(file) as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=':')
#        for row in csv_reader:
#            if not row or row[0][0] == '#':
#                continue
#            coords = row[1].split()
#            print(f"{coords[0]},{coords[2]},{row[0]}")


def output_for_calc(name, x, y, z):
    print(f"{name},{x},{y},{z}")

def output_for_gnuplot(name, x, y, z):
    y_mc = y * -1
    print(f"{x},{y},{name} ({x} {z} {y_mc})")
    #print(f"{x},{y},{name}")

def main(strategy, filename):
    # get output function
    #fn = globals()[f"for_{strategy}"]
    fn = globals()[f"output_for_{strategy}"]

    with open(filename) as file:
        for line in file:
            # ignore comments and empty lines
            if not line.strip() or line[0] == '#':
                continue

            # split line into name and coordinates
            parts = line.split(':')
            coords = parts[1].split()

            # minecraft coordinates are
            #  X : -west +east
            #  Y : -down +up
            #  Z : -north +south
            # but everything else IRL expects y as nort/south, and z as up/down, so here we switch them
            x, z, y = coords

            y = int(y) * -1
            fn(parts[0], x, y, z)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(f"usage: {sys.argv[0]} <minecraft-coords-file> [calc|gnuplot]")

    file = sys.argv[1]
    strategy = sys.argv[2]

    main(strategy, file)

