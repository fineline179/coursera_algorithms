#%% Coursera c2 w4 assignment: 2-SUM

# Import data
with open('/home/fineline/projects/coursera-algorithms/c2/prog_assign_4/2sum_data.txt',
          'r') as f:
  data = [int(line.strip()) for line in f]


#%%
data_set = set(data)

def two_sum(target: int):
  for first_summand in data_set:
    second_summand = target - first_summand
    if second_summand in data_set and second_summand != first_summand:
      return True
  return False


#%%
exist_distinct = []
for t in range(-10000, 10001):
  exist_distinct.append(two_sum(t))
  print('target value: {}, {}'.format(t, exist_distinct[-1]))
