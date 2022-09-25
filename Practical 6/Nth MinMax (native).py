gfg_list = [8, 1, 7, 10, 5]

# min and max indexes are taken 1st element
# In some cases list might be a single element
min_ele, max_ele = gfg_list[0], gfg_list[0]

for i in range(1, len(gfg_list)):

	if gfg_list[i] < min_ele:
		min_ele = gfg_list[i]
		
	if gfg_list[i] > max_ele:
		max_ele = gfg_list[i]
		
print('Minimum Element in the list', gfg_list, 'is', min_ele)

print('Maximum Element in the list', gfg_list, 'is', max_ele)

