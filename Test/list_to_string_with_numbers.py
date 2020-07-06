ls = [1, 2, 3, 'NULL', 'NONE']
print(','.join(str(s) for s in ls if s not in ['NONE', 'NULL']))
