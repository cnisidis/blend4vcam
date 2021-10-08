import bpy
import xml.etree.ElementTree as ET

class Exporter():
    
    cameras = []

    def isAlive(self):
        print("Yes Exporter is Alive, fill it with content")

    def FilterCameras(self, selected_objects):
        count_selected_objects = len(selected_objects)
        for obj in selected_objects:
            if obj.type == 'CAMERA':
                self.cameras.append(obj)
        
        

    def Dump(self, camera):
        depsgraph = bpy.context.evaluated_depsgraph_get()

        node = ET.Element('BL_CAMERA')
        node.attrib= {'name':camera.name}
        world_matr = camera.matrix_world.copy()
        world_matr = world_matr.inverted()
        projection_matrix = camera.calc_matrix_camera(depsgraph)
        projection_matrix = projection_matrix.copy()
        projection_matrix.transpose()

        world_matr.transpose()
        
        #RENDERER
        node_renderer = ET.SubElement(node, 'RENDERER')
        
        node_data = ET.SubElement(node, 'DATA')
        #LENS PROPERTIES
        node_lens = ET.SubElement(node_data, 'LENS')
        node_lens.text = str(camera.data.lens)
        node_lens.attrib= {'unit':'mm'}
        #CLIPPING
        node_clip = ET.SubElement(node_data, 'CLIP')
        node_clip.attrib = {'end': str(camera.data.clip_end), 'start': str(camera.data.clip_start)}
        #CAMERA SENSOR
        node_sensor = ET.SubElement(node_data, 'SENSOR')
        node_sensor.attrib = {'width': str(camera.data.sensor_width), 'height': str(camera.data.sensor_height), 'fit':camera.data.sensor_fit }
        #CAMERA SHIFT
        node_shift = ET.SubElement(node_data, 'SHIFT')
        node_shift.attrib = {'x': str(camera.data.shift_x), 'y': str(camera.data.shift_y)}
       
       # | MATRICES  |
       
        node_matrix = ET.SubElement(node, 'MATRIX')
        node_matrix.attrib = {'id':'0', 'name':'WORLD'}
        node_rows = ET.SubElement(node_matrix, 'ROWS')

        for i, row in enumerate(world_matr):
            node_row = ET.SubElement(node_rows, 'ROW')
            node_row.attrib = {'id':str(i)}
            for j, co in enumerate(row):
                node_col = ET.SubElement(node_row, 'COL')
                node_col.attrib = {'id':str(j)}
                node_col.text = str(co)
                print(co)

        node_matrix = ET.SubElement(node, 'MATRIX')
        node_matrix.attrib = {'id':'0', 'name':'PROJECTION'}
        node_rows = ET.SubElement(node_matrix, 'ROWS')

        for i, row in enumerate(projection_matrix):
            node_row = ET.SubElement(node_rows, 'ROW')
            node_row.attrib = {'id':str(i)}
            for j, co in enumerate(row):
                node_col = ET.SubElement(node_row, 'COL')
                node_col.attrib = {'id':str(j)}
                node_col.text = str(co)
                print(co)

        #return dump and add it to a text block or to a file
        return ET.dump(node)


    def ToXML(self, multiple_files=False):
        
        selected_objects = bpy.context.selected_objects
        
        #get all possible selected cameras
        self.FilterCameras(selected_objects)
        if len(self.cameras) > 0:
            
            #create cameras xml node
            collection_node = ET.Element('CAMERAS')
            for camera in self.cameras:
                if multiple_files:
                    #create new file and text block and add content
                    pass
                else:
                    #create new node and add content
                    self.Dump(camera)
                    pass
        else:
            print('no camera was found')
            return {'WARNING'}
            
            

        
            
    