import os
import math

class Poi(object):
    """Points of Interest have a ptype, location, level and points"""


    def __init__(self, ptype, level, points, coords):
        self.ptype = ptype
        self.level = level
        self.points = points
        self.coords = coords

    @classmethod
    def load_file(cls, source_file, source_dir=''):
        """Load POI from a text file

        For groups of POI types, the text file looks like this:
        [b][u]Tiberium[/u][/b] 
        L26 [coords]704:271[/coords] (1500)
        L23 [coords]681:241[/coords] (400)
        """

        RESOURCES = [
            'Tiberium',
            'Crystal',
            'Reactor',
            'Tungsten',
            'Uranium',
            'Aircraft',
            'Resonator',
            ]

        source_filepath = os.path.join(source_dir, source_file)
        poi_type = ''
        poi_list = []
        sf = open(source_filepath, 'U')
        for line in sf:
            line_type = ''
            # print(line)
            for r in RESOURCES:
                if line.find(r) != -1:
                    line_type = 'poi type'
                    # print(line, 'matched', r)
                    poi_type = r
            if (line.find('coords') != -1) \
            and (line[0] != '#'):
                line_type = 'poi location'
                level, coords, points = line.split(' ')
                poi_level = level[1:]
                poi_coords = (int(coords[8:11]), int(coords[12:15]))
                poi_points = points[1:len(points) - 2]
                # print (poi_type, poi_level, poi_coords, poi_points)
                poi = Poi(poi_type, poi_level, poi_points, poi_coords)
                poi_list.append(poi)
        return poi_list

    def coords_link(self):
        link = "[coords]{0}:{1}[/coords]".format(
            self.coords[0], self.coords[1])
        return link

    def distance(self, point2):
        """Points are xy coordinates"""

        r = 0.0
        x1, y1 = self.coords
        x2, y2 = point2
        # print(x1, y1)
        r = round(math.sqrt((x2-x1)**2+(y2-y1)**2),1)
        return r

    def print_csv(self):
        print("{0},{1},{2},{3}".format(
            self.ptype, self.level, self.points, self.coords))

    def print_table(self):
        print("{0:9}  {1:2}  {2:4}  {3:10}".format(
            self.ptype, self.level, self.points, self.coords))

    def print_email(self):
        print("{0}-{1}, {2} points at {3}".format(
            self.ptype, self.level, self.points, self.coords_link()))
