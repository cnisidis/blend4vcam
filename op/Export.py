import bpy
import xml.etree.ElementTree as ET

class Exporter():
    
    

    def isAlive(self):
        print("Yes Exporter is Alive, fill it with content")

    def ToXML(self):
        depsgraph = bpy.context.evaluated_depsgraph_get()
        selected_objects = bpy.context.slected_objects
        camera = None

        if camera == None:
            print('no camera was found')
            return {'WARNING'}
        elif camera.type == 'CAMERA':
            print('camera selected: '+ camera.name)
            
            

        node = ET.Element('BL_CAMERA')
        world_matr = camera.matrix_world.copy()
        world_matr = world_matr.inverted()
        projection_matrix = camera.calc_matrix_camera(depsgraph)
        projection_matrix = projection_matrix.copy()
        projection_matrix.transpose()

        world_matr.transpose()
        projection_matrix

        node_data = ET.SubElement(node, 'DATA')
        node_lens = ET.SubElement(node_data, 'LENS')
        node_lens.text = str(camera.data.lens)
        node_lens.attrib= {'unit':'mm'}
        node_clip = ET.SubElement(node_data, 'CLIP')
        node_clip.attrib = {'end': str(camera.data.clip_end), 'start': str(camera.data.clip_start)}
        node_sensor = ET.SubElement(node_data, 'SENSOR')
        node_sensor.attrib = {'width': str(camera.data.sensor_width), 'height': str(camera.data.sensor_height), 'fit':camera.data.sensor_fit }
        node_shift = ET.SubElement(node_data, 'SHIFT')
        node_shift.attrib = {'x': str(camera.data.shift_x), 'y': str(camera.data.shift_y)}



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

        ET.dump(node)
            
    