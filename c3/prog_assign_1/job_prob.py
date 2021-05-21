#%%
from collections import namedtuple
from itertools import accumulate

#%% load data
WeightLength = namedtuple('WeightLength', ['weight', 'length'])

with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_1/jobs.txt',
          'r') as f:
  num_jobs = int(f.readline().strip())
  wl_list = [WeightLength(*[int(x) for x in line.strip().split(' ')])
             for line in f.readlines()]


#%% Problem 1
# list of ((weight - length), weight,length pair) for each job
diff_and_wl_list = [tuple([(wl.weight - wl.length), wl]) for wl in wl_list]

# schedule jobs sorting by 1) decreasing (weight - length), 2) decreasing weight
diff_and_wl_list_sorted = sorted(diff_and_wl_list, key=lambda x: (-x[0], -x[1].weight))

# completion times for scheduled jobs
diff_comp_times = list(accumulate([el[1].length for el in diff_and_wl_list_sorted]))

# total weighted completion time for all jobs
diff_wct_sum = 0
for i in range(num_jobs):
  diff_wct_sum += diff_and_wl_list_sorted[i][1].weight * diff_comp_times[i]

print(diff_wct_sum)

#%% Problem 2
# list of ((weight/length), weight,length pair) for each job
ratio_and_wl_list = [tuple([(wl.weight / wl.length), wl]) for wl in wl_list]

# schedule jobs by sorting by 1) decreasing (weight/length)
ratio_and_wl_list_sorted = sorted(ratio_and_wl_list, key=lambda x: -x[0])

# completion times for scheduled jobs
ratio_comp_times = list(accumulate([el[1].length for el in ratio_and_wl_list_sorted]))

# total weighted completion time for all jobs
ratio_wct_sum = 0
for i in range(num_jobs):
  ratio_wct_sum += ratio_and_wl_list_sorted[i][1].weight * ratio_comp_times[i]

print(ratio_wct_sum)