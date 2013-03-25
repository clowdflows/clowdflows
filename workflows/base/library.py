import cPickle

def base_concatenate_lists(input_dict):
    lists = input_dict['lists']
    new_list = []
    for every_list in lists:
        new_list = new_list+every_list
    output_dict = {}
    output_dict['list']=new_list
    return output_dict

def create_list(input_dict):
    return input_dict

def create_tuple(input_dict):
    lists = input_dict['elements']
    output_dict = {}
    output_dict['tuple'] = tuple(lists)
    return output_dict

def create_dictionary(input_dict):
    keys = input_dict['keys']
    values = input_dict['values']
    dic = {}
    for idx in range(0,min(len(keys),len(values))):
        dic[keys[idx]] = values[idx]
    output_dict = {'dict': dic}
    return output_dict

def create_range(input_dict):
    output_dict = {}
    output_dict['rangeout'] = range(int(input_dict['n_range']))
    return output_dict

def delay(input_dict,widget):
    widget.progress=0
    widget.save()
    timeleft = int(input_dict['time'])
    i = 0
    import time
    import math
    while i<timeleft:
        time.sleep(1)
        i=i+1
        widget.progress = math.floor(((i*1.0)/timeleft)*100)
        widget.save()
    widget.progress=100
    widget.save()
    output_dict = {}
    output_dict['data'] = input_dict['data']
    return output_dict

# ENSEMBLE

def ensemble(input_dict):
    import math
    ens = {}
    data_inds = input_dict['data_inds']
    ens_type = input_dict['ens_type']
    # TODO ens_level = input_dict['ens_level']
    for item in data_inds:
        #det_by = item['detected_by']
        for i in item['inds']:
            if not ens.has_key(i):
                ens[i] = 1
            else:
                ens[i] += 1

    ens_out = {}
    ens_out['name'] = input_dict['ens_name']
    ens_out['inds'] = []
    n_algs = len(data_inds)
    print ens_type
    if ens_type == "consensus":
        ens_out['inds'] = sorted([x[0] for x in ens.items() if x[1] == n_algs])
    else: # majority
        ens_out['inds'] = sorted([x[0] for x in ens.items() if x[1] >= math.floor(n_algs/2+1)])

    output_dict = {}
    output_dict['ens_out'] = ens_out
    return output_dict

def pickle_object(input_dict):
    '''
    Serializes the input object.
    '''
    pkl_obj = cPickle.dumps(input_dict['object'])
    output_dict = {}
    output_dict['pickled_object'] = pkl_obj
    return output_dict

def unpickle_object(input_dict):
    '''
    Serializes the input object.
    '''
    obj = cPickle.loads(str(input_dict['pickled_object']))
    output_dict = {}
    output_dict['object'] = obj
    return output_dict

def stopwatch(input_dict):
    import time
    inputTime = input_dict['time_in']
    now = time.time()
    if (isinstance(inputTime, float)):
        elapsedTime = now - inputTime
    else:
        elapsedTime = None
    output_dict = {}
    output_dict['signal_out'] = input_dict['signal']
    output_dict['time_out'] = now
    output_dict['time_span'] = elapsedTime

    return output_dict