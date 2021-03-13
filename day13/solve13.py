from itertools import count


def get_info(path='test.txt', p2=False):
    with open(path) as f:
        timestamp, bids = f.readlines()

    buses = [
        (int(bid), pts) if p2 else int(bid)
            for pts, bid in enumerate(bids.split(',')) 
                if bid.isnumeric()
    ]

    return int(timestamp), buses



def p1(info):
    earliest_timestamp, buses_ids = info
    earliest_departure = earliest_id = None # earliest departure timestamp & earliest bus id

    for bid in buses_ids:
        for timestamp in range(earliest_timestamp, earliest_timestamp + bid):
            if not timestamp % bid:

                if earliest_departure is None or timestamp < earliest_departure: 
                    earliest_departure = timestamp
                    earliest_id = bid

                break

    return (earliest_departure - earliest_timestamp) * earliest_id



def p2(info):
    timestamp = 0
    _, buses = info
    step = 1

    for bid, pts in buses:
        timestamp = next(c for c in count(timestamp, step) if not (pts + c) % bid)
        step *= bid

    return timestamp



if __name__ == "__main__":
    print(
        p1(get_info()),
        p2(get_info(path='inp.txt', p2=True)),
        sep='\n'
    )