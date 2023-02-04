import sys
import webbrowser

arg = sys.argv


def concat(array):
    return "+".join(array)


# Just open maps
if len(arg) == 1:
    webbrowser.open("https://www.google.com/maps/")

# Just lookup the place on Google Maps
elif arg[1] == 'info':
    place = concat(arg[2:])
    webbrowser.open("https://www.google.com/maps/search/" + place)

# Get directions
else:
    if arg[1] == 'go':
        try:
            i = arg.index('to')
            start = concat(arg[2:i])
            dest = concat(arg[i + 1:])
        except:
            pass
    else:
        start = "home"
        dest = concat(arg[1:])

    url = "https://www.google.com/maps/dir/{}/{}".format(start, dest)
    webbrowser.open(url)
