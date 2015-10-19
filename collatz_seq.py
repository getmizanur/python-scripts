__author__ = 'Mizanur Rahman <getmizanur@gmail.com>'

seq_length = 0
starting_number = 0
seq = None

for i in range(1, 1000000):
    length = 1
    seq = i
    while seq != 1:
        if seq % 2 == 0:
            seq = seq / 2
        else:
            seq = seq * 3 + 1

        length = length + 1

    if length > seq_length:
        seq_length = length
        starting_number = i
        print 'A Starting number of ' + str(starting_number) + '. produces a sequence of ' + str(seq_length)
    


