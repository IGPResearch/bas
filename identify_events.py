# This code is called by Run_Algorithm.py to assess heat flux events. 
# It was developed in conjunction with Tony Philips at the British Antarctic Survey. 

import numpy as np

def identify_events(data, event_threshold, exit_threshold):
    # array of flag values indicating whether day is in event or not
    # NB: includes sentinel values at start and end (hence +2)
    day_in_event = np.zeros(len(data)+2, dtype=bool)

    # state variable: whether we are currently in an event
    in_event = False

# IMPORANT NOTE
# This code works on the assumption that heat fluxes are positive from ocean to atmosphere. If not please change '>' to '<' in
# Line 23, 29 & 35

    # iterate over the samples, identifying events
    # NB: indexing of day_in_event has +1 because of initial sentinel value
    for i, value in enumerate(data):
        if in_event:
            # if we are already in an event, just see if the event is continuing or not
            if value >= exit_threshold:
                day_in_event[i+1] = True
            else:
                in_event = False
        else:
            # otherwise, see if we should start an event
            if value >= event_threshold:
                in_event = True
                day_in_event[i+1] = True

                # backtrack to find start of event
                for j in range(i-1, -1, -1):
                    if data[j] >= exit_threshold:
                        day_in_event[j+1] = True
                    else:
                        break

    # find indexes of start and ends of events
    start_inds = np.where(np.logical_and(day_in_event[1:], ~day_in_event[0:-1]))[0]
    end_inds = np.where(np.logical_and(~day_in_event[1:], day_in_event[0:-1]))[0] - 1

    # get statistics on event lengths and maxima
    event_lengths = {}
    event_extremes = np.zeros(len(start_inds), dtype=data.dtype)
    event_extreme_inds = np.zeros(len(start_inds), dtype=int)
    for i, (start_ind, end_ind) in enumerate(zip(start_inds, end_inds)):
        event_length = end_ind - start_ind + 1
        if event_length in event_lengths:
            event_lengths[event_length] += 1
        else:
            event_lengths[event_length] = 1
        event_extremes[i]=np.min(data[start_ind:end_ind+1])
        event_extreme_inds[i]=np.where(data[start_ind:end_ind+1] ==
                                       event_extremes[i])[0][0] + start_ind

    # NB: sentinel values are removed from day_in_event array here
    return (day_in_event[1:-1], start_inds, end_inds, event_lengths,
            event_extremes, event_extreme_inds)


def show_events(data, day_in_event, start_inds, end_inds, event_lengths,
                event_extremes, event_extreme_inds):

    # print the data, highlighting the events
    for i, value in enumerate(data):
        in_event = day_in_event[i]
        start = i in start_inds
        end = i in end_inds
        extreme = i in event_extreme_inds
        print('{}: {} {} {}{}{}'.format(i, value, ['   ', '***'][in_event],
            ['','START '][start], ['','EXTREME '][extreme], ['','END'][end]))

    # print a summary of the number of events of different lengths
    event_len_str = ''
    for event_len in sorted(event_lengths.keys()):
        if len(event_len_str) > 0:
            event_len_str += ', '
        event_len_str += '{} x {} days'.format(event_lengths[event_len], event_len)
    print('\nFound {} events: {}'.format(len(start_inds), event_len_str))


if __name__ == '__main__':
    # test data representing 1 year (121 samples) in the range 0 to 1
    data = np.random.rand(121)

    # thresholds for identifying and leaving event
    event_threshold = 0.2
    exit_threshold = 0.5

    # identify the events
    (day_in_event, start_inds, end_inds, event_lengths,
        event_extremes, event_extreme_inds) = identify_events(
        data, event_threshold, exit_threshold)

    # print out the results
    show_events(data, day_in_event, start_inds, end_inds, event_lengths,
event_extremes, event_extreme_inds)
