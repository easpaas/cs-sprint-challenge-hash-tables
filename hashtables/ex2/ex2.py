class Ticket:
    def __init__(self, source, destination):
        # starting airport
        self.source = source
        # next airport
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = {}
    trip = []

    # for each Ticket in tickets 
    for ticket in tickets:
        # link tickets via ticket.destination == ticket.source
        ht[ticket.source] = ticket.destination
        
    # keep index in range
    trip.append(ht['NONE'])

    for i in range(length): 
        # for each Key in ht
        if trip[i] in ht:
            # if destination is equal to source
            if ht[trip[i]] == trip[0]:
                continue
            trip.append(ht[trip[i]])

    return trip

    # return route
