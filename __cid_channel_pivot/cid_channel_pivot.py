
def add_to_dict(dict_var, key, value):
    if key in dict_var:
        dict_var[key].append(value)
    else:
        dict_var[key] = [value]
    return dict_var

# Open input file
with open('channel-cids_input.csv') as cid_channel_fo:
    # get each line of input as a string file into a list
    channel_cid_list_strs = cid_channel_fo.read().split('\n')[1::]

    print('channel_cid_list_strs', channel_cid_list_strs[0:3])

    #split each line read as string into a list of cids creating a matrix with first value as channel no
    channel_cid_matrix = [channel_cid_list_str.split(',') for channel_cid_list_str in channel_cid_list_strs]

    print('channel_cid_matrix', channel_cid_matrix[0:3])

    # get all first elements of the channel_cid matrix into channel list 
    # (this will be used to map the cid back to the channel later on using row index where the cid is found)
    channel_list = [row[0] for row in channel_cid_matrix]

    print('channel_list', channel_list[0:3])

    # get all first elements of the channel_cid matrix into channel list
    cid_list = [row[1::] for row in channel_cid_matrix]

    print('cid_list', cid_list[0:3])

    # keep only cids with actual values in every row as  there are many empty cells
    cid_list_coalesced = [list(filter(lambda el: False if el == '' else True, row[1::])) for row in cid_list]

    print('cid_list_coalesced', cid_list_coalesced[0:3])

    # instantiate cid dict with key as cid and value as array of channel nos
    cid_dict = {}

    # for every cell(i.e cid) map the cid to its channel no using the row it is present on
    for row_no, row in enumerate(cid_list_coalesced):
        for cell in row:
            cid_dict = add_to_dict(cid_dict, cell, channel_list[row_no])


    with open('cid-channel_output.csv', 'w+') as cid_channel_outfile:
        
        cid_channel_output_list = []

        for key, value in cid_dict.items():
            cid_channel_output_list.append(','.join([key, *value]))

        cid_channel_outfile.write('cid,channels\n' + '\n'.join(cid_channel_output_list))
    
