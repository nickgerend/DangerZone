# Written by: Nick Gerend, @dataoutsider
# Viz: "Danger Zone", enjoy!

import pandas as pd
import os
from math import pi, sin, cos

df = pd.read_csv(os.path.dirname(__file__) + '/poly.csv')
df = df.sort_values(by=['y'], ascending=True)

#region tornado
min_Y = df['y'].min()
max_Y = df['y'].max()+0.1
cutoff_L = 42. #42.
cutoff_R = 46.
N_L = cutoff_L-min_Y
N_R = max_Y-cutoff_R
offset_L = 1.5
offset_R = -2.
Y_r = 0.
Z_r = 0.
ix = 0
z_factor = 0.25
left_factor = 2.0 #2.5
right_factor = 1.0
y_step = 0.
Y_last = 0.
found = False
import csv
with open(os.path.dirname(__file__) + '/poly_curve.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['index', 'item', 'item2', 'side', 'path', 'x', 'y', 'z', 'type', 'yr', 'zr'])
    for row in df.itertuples():
        Y = row.y
        Z = row.z*z_factor

        if not found:
            Y_last = Y
          
        if Y >= cutoff_R:
            angle = (2.*pi)*(((Y-cutoff_R)%N_R)/N_R)
            angle_deg = angle*180./pi/right_factor
            if angle_deg >= 180:
                found = True
                angle_deg = 180.
            angle_rotated = (abs(angle_deg-360.)+90.) % 360.
            angle_new = angle_rotated * pi/180.
            Y_r = (Z+offset_R)*cos(angle_new)*-1.+cutoff_R-(Y-Y_last)
            Z_r = (Z+offset_R)*sin(angle_new)-offset_R
        elif Y <= cutoff_L:
            angle = (2.*pi)*(((Y-min_Y)%N_L)/N_L)
            angle_deg = angle*180./pi/left_factor
            angle_rotated = (abs(angle_deg-360.)+90.) % 360. + (360./left_factor)
            angle_new = angle_rotated * pi/180.
            Y_r = (Z+offset_L)*cos(angle_new)+cutoff_L
            Z_r = (Z+offset_L)*sin(angle_new)-offset_L
        else:
            Y_r = Y
            Z_r = Z

        writer.writerow([ix, row.item, row.item2, row.side, row.path, row.x, row.y, row.z, row.type, Y_r, Z_r])
        ix += 1
#endregion

print('finished')