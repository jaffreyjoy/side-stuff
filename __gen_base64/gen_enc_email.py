import csv
from sys import argv
from base64 import b64encode


def main():
    # Filename of the csv to be used  with extension
    INPUT_CSV_FILE_NAME = argv[1].replace('"','')

    # Col no of the Email in the csv
    EMAIL_COL_NO  = int(argv[2]) - 1

    # Col name of encrypted email
    ENCRYPTED_EMAIL_COL_NAME = 'ENEMAIL'

    # Output file name
    OUTPUT_CSV_FILE_NAME = INPUT_CSV_FILE_NAME[0:-4] + '_ENEMAIL' + '.csv'

    # Output file
    outfile = open(OUTPUT_CSV_FILE_NAME, 'w+', newline='')

    OUTPUT_CSV_FILE_NAME = INPUT_CSV_FILE_NAME[0:-4] + '_ENEMAIL' + '.csv'

    with open(INPUT_CSV_FILE_NAME, 'r', newline='') as inputfile:

        reader = csv.DictReader(inputfile)

        # Get actual col name of email
        EMAIL_COL_NAME = reader.fieldnames[EMAIL_COL_NO]
        
        # print(EMAIL_COL_NAME)
        # print(reader.line_num)

        # add enemail col to ouput file fieldnames
        outfile_fieldnames = [*reader.fieldnames, ENCRYPTED_EMAIL_COL_NAME]

        # Create witer object for output file
        writer = csv.DictWriter(outfile, fieldnames=outfile_fieldnames)

        # Write csv header in 
        writer.writeheader()

        for row in reader:
            # Encrypt EMAIL and do necessary replacements
            ENCRYPTED_EMAIL = b64encode((row[EMAIL_COL_NAME]).encode()).decode()    \
                                .replace('+', 'SLUP')                               \
                                .replace('=', 'LAUQE')                              \
                                .replace('/', 'HSALS')

            # Write row with encrypted email
            writer.writerow({**row, ENCRYPTED_EMAIL_COL_NAME: ENCRYPTED_EMAIL})

        #Close outfile object
        outfile.close()

if __name__ == "__main__":
    main()
