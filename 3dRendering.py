from vtkplotter import *

embedWindow(backend='k3d')
# actor = load('./data_embrions/embryo.tif', threshold=40)
actor = load('./data_embrions/focal1.tif', threshold=100)
actor.color('green')
show(actor)
