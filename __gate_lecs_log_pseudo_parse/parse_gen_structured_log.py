from pprint import pprint

#return


def get_chunk_metadata(block_chunks):
    metadata = []
    for index, chunk in enumerate(block_chunks[1:]):
        if chunk.find('http') == -1:
            metadata.append(index+1)
            # print(block_chunks[index+1])
    return(metadata)



def generate_srno_and_date(sr_no_date_str):
    srno, date = [el.strip() for el in sr_no_date_str.split(')')]
    date = (date +' 2020').replace('2020 2020', '2020').title()
    return [srno, date]


def generate_links(index, sub_index, no_subs, len_block_chunks, chunks_metadata, block_chunks):
    start_index = sub_index+1
    end_index = len_block_chunks if index+1 == no_subs else chunks_metadata[index+1]+1
    return " ".join(block_chunks[start_index:end_index])


#open log file
with open('gate_lecs_log.txt') as log_src:

    #read and split based on double conssecutive EOL
    log_src_list = log_src.read().split('\n\n')

    #remove leading and trailing whitespaces and EOLs
    log_src_list_clean = list(
        map(lambda one_day_log: one_day_log.strip(), log_src_list))
    # print(log_src_list_clean[0:5])
    blocks = log_src_list_clean

    rows = []

    for block in blocks:
        block_chunks = list(
            map(lambda chunk: chunk.strip(), block.split('\n')))

        len_block_chunks = len(block_chunks)

        #get metadata of chunk
        chunks_metadata = get_chunk_metadata(block_chunks)

        srno, date = generate_srno_and_date(block_chunks[0])

        no_subs = len(chunks_metadata)

        for index, sub_index in enumerate(chunks_metadata):
            sub = block_chunks[sub_index]
            links = generate_links(
                index, sub_index, no_subs, len_block_chunks, chunks_metadata, block_chunks)
            row = ",".join([srno, date, sub, links])
            rows.append(row + "\n")

    print("".join(rows))


            
