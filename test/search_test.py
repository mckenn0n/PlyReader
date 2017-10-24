data = ['text', 'foo2', 'foo1', 'sample',"","","","","","","","","","h","fo2","",'','!foo3','','','foo3','','','3','3','3']
indeces = [i for i,val in enumerate(data) if val.startswith('foo')]
print(indeces)