#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    destinations = {}
    trip = []

    for ticket in tickets:
        destinations[ticket.source] = ticket.destination
    
    for i in range(length):
        if i == 0:
            trip.append(destinations["NONE"])
        else:
            trip.append(destinations[trip[i-1]])

    return trip
