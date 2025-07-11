import wfdb
import numpy as np
import csv


AAMI_MIT  = {'N': 'Nfe/jnBLR',
             'S': 'SAJa',
             'V': 'VEr',
             'F': 'F',
             'Q': 'Q?'}

AAMI = {'N': [],'S': [],'V': [],'F': [], 'Q': []}
file_name =['100', '101', '102', '103', '104', '105', '106', '107',
            '108', '109', '111', '112', '113', '114', '115', '116',
            '117', '118', '119', '121', '122', '123', '124', '200',
            '201', '202', '203', '205', '207', '208', '209', '210',
            '212', '213', '214', '215', '217', '219', '220', '221',
            '222', '223', '228', '230', '231', '232', '233', '234']
ECG = {'N': [], 'f': [], 'e': [], '/': [], 'j': [], 'n': [], 'B': [],
       'L': [], 'R': [], 'S': [], 'A': [], 'J': [], 'a': [], 'V': [],
       'E': [], 'r': [], 'F': [], 'Q': [], '?': []}
for F_name in file_name:
    signal_annotation = wfdb.rdann(f'D:/ECG/mit-bih-arrhythmia-database-1.0.0/{F_name}', "atr", sampfrom=0, sampto=650000)
    record = wfdb.rdrecord(f'D:/ECG/mit-bih-arrhythmia-database-1.0.0/{F_name}', sampfrom=0, sampto=650000, physical=True, channels=[0, ])

    ECG_R_list = np.array(['N', 'f', 'e', '/', 'j', 'n', 'B',
                           'L', 'R', 'S', 'A', 'J', 'a', 'V',
                           'E', 'r', 'F', 'Q', '?'])

    Index = np.isin(signal_annotation.symbol, ECG_R_list)

    Label = np.array(signal_annotation.symbol)

    Label = Label[Index]

    Sample = signal_annotation.sample[Index]

    Label_kind = list(set(Label))

    for k in Label_kind:
        index = [i for i, x in enumerate(Label) if x == k]
        Signal_index = Sample[index]
        length = len(record.p_signal)


        for site in Signal_index:
            if 130 < site < length-200:
                ECG_signal = record.p_signal.flatten().tolist()[site-130:site+200]

                ECG[str(k)].append(ECG_signal)


for key, value in ECG.items():
    print(f'{key} = {len(value)}')

for ECG_key, ECG_value in ECG.items():
    for AAMI_MIT_key, AAMI_MIT_value in AAMI_MIT.items():
        if ECG_key in AAMI_MIT_value:
            AAMI[AAMI_MIT_key].extend(ECG_value)


for key, value in AAMI.items():
    with open(f'{key}.csv', 'w',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(value)
