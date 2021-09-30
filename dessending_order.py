import operator
d={'python':90,'cpp':100,'java':80,'php':60}
dsc=dict(sorted(d.items(),key=operator.itemgetter(1)))
print('descending=',dsc)