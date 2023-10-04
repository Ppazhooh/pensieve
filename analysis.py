import pandas as pd
#Read the tab seperated data as csv file
file_dir = 'real_exp/results/log_RL_1'

column_names = ['time_stamp', 'bit_rate', 'buffer_size', 'rebuffer_time',
                'video_chunk_size', 'download_time', 'reward']

df = pd.read_csv(file_dir, delimiter=r'\s+', header=None, names = column_names)



df['bit_rate_diff'] = df['bit_rate'].diff().abs()

bit_rate_sum = df['bit_rate'].sum() / 1000.0
rebuffer_sum = df['rebuffer_time'].sum()
bit_rate_diff_sum = df['bit_rate_diff'].sum() / 1000.0
penalty = 4.3

qoe = bit_rate_sum - penalty * rebuffer_sum - bit_rate_diff_sum
qoe_normalized = qoe / len(df['bit_rate'])
qoe_normalized = round(qoe_normalized, 2)
print (qoe_normalized)
