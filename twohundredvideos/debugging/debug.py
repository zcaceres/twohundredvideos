"""
    Handles debugging tasks
"""


def print_results(links):
    counter = 0
    print("We found: {0} links!".format(len(links)))
    for link in links:
        counter += 1
        print ("Link {0}: {1}".format(counter, link))