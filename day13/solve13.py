from itertools import count

def get_info(path='inp.txt'):
    with open(path) as f:
        lines = f.readlines()

    timestamp = int( lines[0] )
    #buses = list( map( int, filter( lambda x: x != 'x', lines[1].split(',') ) ) )  #p1

    bids = lines[1].split(',')
    buses = list( filter( lambda x: x != 'x', ( (int(bid), pts) if bid.isnumeric() else bid for pts, bid in enumerate(bids) ) ) ) # pts = required departure post timestamp

    return timestamp, buses 


def earliest_bus(info): #p1
    timestamp, buses = info
    bts = {} # busses with corresponding earliest timestamps

    for b in buses:
        tsrange = range(timestamp, timestamp + b)
        for ts in tsrange:
            if ts % b == 0:
                bts[b] = ts

    eb, ebts = min(bts.items(), key=lambda x: x[1]) #eb stands for earliest bus
    return (ebts - timestamp) * eb


def earliest_timestamp(info):
    timestamp, buses = info
    step = 1

    for bid, pts in buses: 
        timestamp = next(c for c in count(timestamp, step) if (pts + c) % bid == 0)
        step *= bid

    return timestamp


if __name__ == "__main__":
    #print( earliest_bus( get_info() ) ) # part 1
    print(earliest_timestamp( get_info()))