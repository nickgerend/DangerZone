# Written by: Nick Gerend, @dataoutsider
# Viz: "Danger Zone", enjoy!

import pandas as pd
import os

class point:
    def __init__(self, index, item, side, path, x, y, z ): 
        self.index = index
        self.item = item
        self.side = side
        self.path = path
        self.x = x
        self.y = y
        self.z = z
    def to_dict(self):
        return {
            'index' : self.index,
            'item' : self.item,
            'side' : self.side,
            'path' : self.path, 
            'x' : self.x,
            'y' : self.y,
            'z' : self.z }

#CA_DEN_5000
#CA_Density
df = pd.read_csv(os.path.dirname(__file__) + '/CA_DEN_5000.csv')

#region algorithm
list_xy = []
spacing = 5000.
offset = spacing/2.
ix = 0
scale = 100000.
for id, row in df.groupby('id'):
    
    # 1  2
    # 3  4

    #bottom
    list_xy.append(point(ix, id, 'btm', 1, (row['x'].values[0]-offset)/scale, (row['y'].values[0]+offset)/scale, 0.))
    list_xy.append(point(ix, id, 'btm', 2, (row['x'].values[0]+offset)/scale, (row['y'].values[0]+offset)/scale, 0.))
    list_xy.append(point(ix, id, 'btm', 3, (row['x'].values[0]+offset)/scale, (row['y'].values[0]-offset)/scale, 0.))
    list_xy.append(point(ix, id, 'btm', 4, (row['x'].values[0]-offset)/scale, (row['y'].values[0]-offset)/scale, 0.))
    #top
    list_xy.append(point(ix, id, 'top', 1, (row['x'].values[0]-offset)/scale, (row['y'].values[0]+offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'top', 2, (row['x'].values[0]+offset)/scale, (row['y'].values[0]+offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'top', 3, (row['x'].values[0]+offset)/scale, (row['y'].values[0]-offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'top', 4, (row['x'].values[0]-offset)/scale, (row['y'].values[0]-offset)/scale, len(row)))
    #left
    list_xy.append(point(ix, id, 'left', 1, (row['x'].values[0]-offset)/scale, (row['y'].values[0]+offset)/scale, 0.))
    list_xy.append(point(ix, id, 'left', 2, (row['x'].values[0]-offset)/scale, (row['y'].values[0]+offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'left', 3, (row['x'].values[0]-offset)/scale, (row['y'].values[0]-offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'left', 4, (row['x'].values[0]-offset)/scale, (row['y'].values[0]-offset)/scale, 0.))
    #right
    list_xy.append(point(ix, id, 'right', 1, (row['x'].values[0]+offset)/scale, (row['y'].values[0]+offset)/scale, 0.))
    list_xy.append(point(ix, id, 'right', 2, (row['x'].values[0]+offset)/scale, (row['y'].values[0]+offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'right', 3, (row['x'].values[0]+offset)/scale, (row['y'].values[0]-offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'right', 4, (row['x'].values[0]+offset)/scale, (row['y'].values[0]-offset)/scale, 0.))
    #front
    list_xy.append(point(ix, id, 'front', 1, (row['x'].values[0]-offset)/scale, (row['y'].values[0]-offset)/scale, 0.))
    list_xy.append(point(ix, id, 'front', 2, (row['x'].values[0]-offset)/scale, (row['y'].values[0]-offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'front', 3, (row['x'].values[0]+offset)/scale, (row['y'].values[0]-offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'front', 4, (row['x'].values[0]+offset)/scale, (row['y'].values[0]-offset)/scale, 0.))
    #back
    list_xy.append(point(ix, id, 'back', 1, (row['x'].values[0]-offset)/scale, (row['y'].values[0]+offset)/scale, 0.))
    list_xy.append(point(ix, id, 'back', 2, (row['x'].values[0]-offset)/scale, (row['y'].values[0]+offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'back', 3, (row['x'].values[0]+offset)/scale, (row['y'].values[0]+offset)/scale, len(row)))
    list_xy.append(point(ix, id, 'back', 4, (row['x'].values[0]+offset)/scale, (row['y'].values[0]+offset)/scale, 0.))

#endregion

df_out = pd.DataFrame.from_records([s.to_dict() for s in list_xy])
df_out.to_csv(os.path.dirname(__file__) + '/poly.csv', encoding='utf-8', index=False)