import bpy
import xml.etree.ElementTree as ET
from handler import b4vReport

b4vr = b4vReport()
cameras = []

class CameraCollection:
    pass

def GetCameras():

    context = bpy.context
    scn = context.scene
    selected_objects = context.selected_objects
    if len(selected_objects) > 1:
        # b4vr.type = 'WARNING'
        # b4vr.message = 'Too many objects have been selected'
        print('Too many objects have been selected')
        for obj in selected_objects:
            if obj.type != 'CAMERA':
                print('Selection must contain only CAMERA objects')
                return 0
            else:
                cameras.append(obj)
    elif len(selected_objects) == 0:
        print('No camera is selected')
    else:
        print ('No camera is selected')
        return 0



def AssembleCameraData(cam):

    cam_projection_matrix = cam.calc_matrix_camera()
    cam_view_matrix = cam.matrix_local
    cam_world_matrix = cam.matrix_world

    cam_location = cam.location
    cam_rotation = cam.rotation_euler

    res_x = scn.render.resolution_x
    res_y = scn.render.resolution_y

    shift_x = cam.data.shift_x
    shift_y = cam.data.shift_y

    lens_f = cam.data.lens
    lens_d = cam.data.angle

    sensor_w = cam.data.sensor_width
    sensor_h = cam.data.sensor_height

    h_fov = cam.data.angle_x
    v_fov = cam.data.angle_y

    bl_camera = ET.Element('CAMERA', attrib={'name':cam.name})
    bl_camera_pos = ET.SubElement(bl_camera, 'POSITION', attrib={   'x':str(cam.location[0]),
                                                                    'y':str(cam.location[1]),
                                                                    'z':str(cam.location[2])})

    bl_camera_rot = ET.SubElement(bl_camera, 'ROTATION', attrib={   'x':str(cam.rotation_euler[0]),
                                                                    'y':str(cam.rotation_euler[1]),
                                                                    'z':str(cam.rotation_euler[2])})

    bl_camera_fov =ET.SubElement(bl_camera, 'FOV', attrib={ 'h':str(h_fov),
                                                            'v':str(v_fov)})

    bl_camera_sensor =ET.SubElement(bl_camera, 'SENSOR', attrib={   'w':str(sensor_w),
                                                                    'h':str(sensor_h)})

    bl_camera_lens=ET.SubElement(bl_camera, 'LENS', attrib={    'f':str(lens_f),
                                                                'd':str(lens_d)})

    bl_camera_shift=ET.SubElement(bl_camera, 'SHIFT', attrib={  'x':str(shift_x),
                                                                'y':str(shift_y)})

    bl_camera_res = ET.SubElement(bl_camera, 'RESOLUTION', attrib={ 'w':str(res_x),
                                                                    'h':str(res_y)})

    bl_camera_proj_matrix = ET.SubElement(bl_camera, 'PROJ_MATRIX', attrib={'x':str(cam_projection_matrix[0][0])+';'+
                                                                                str(cam_projection_matrix[0][1])+';'+
                                                                                str(cam_projection_matrix[0][2])+';'+
                                                                                str(cam_projection_matrix[0][3]),
                                                                            'y':str(cam_projection_matrix[1][0])+';'+
                                                                                str(cam_projection_matrix[1][1])+';'+
                                                                                str(cam_projection_matrix[1][2])+';'+
                                                                                str(cam_projection_matrix[1][3]),
                                                                            'z':str(cam_projection_matrix[2][0])+';'+
                                                                                str(cam_projection_matrix[2][1])+';'+
                                                                                str(cam_projection_matrix[2][2])+';'+
                                                                                str(cam_projection_matrix[2][3]),
                                                                            'w':str(cam_projection_matrix[3][0])+';'+
                                                                                str(cam_projection_matrix[3][1])+';'+
                                                                                str(cam_projection_matrix[3][2])+';'+
                                                                                str(cam_projection_matrix[3][3])    })

    bl_camera_world_matrix = ET.SubElement(bl_camera, 'WORLD_MATRIX', attrib={'x':str(cam_world_matrix[0][0])+';'+
                                                                                str(cam_world_matrix[0][1])+';'+
                                                                                str(cam_world_matrix[0][2])+';'+
                                                                                str(cam_world_matrix[0][3]),
                                                                            'y':str(cam_world_matrix[1][0])+';'+
                                                                                str(cam_world_matrix[1][1])+';'+
                                                                                str(cam_world_matrix[1][2])+';'+
                                                                                str(cam_world_matrix[1][3]),
                                                                            'z':str(cam_world_matrix[2][0])+';'+
                                                                                str(cam_world_matrix[2][1])+';'+
                                                                                str(cam_world_matrix[2][2])+';'+
                                                                                str(cam_world_matrix[2][3]),
                                                                            'w':str(cam_world_matrix[3][0])+';'+
                                                                                str(cam_world_matrix[3][1])+';'+
                                                                                str(cam_world_matrix[3][2])+';'+
                                                                                str(cam_world_matrix[3][3])    })

    bl_camera_notes = ET.SubElement(bl_camera, 'NOTES')
    bl_camera_notes.text ='None'
    return bl_camera


def GetCameraData():
    for camera in cameras:
        #get all properties and create document tree
        bl_camera =  AssembleCameraData(camera)
        xmlstr = (str(ET.tostring(bl_camera, encoding='utf8', method='xml')))

        textblock = bpy.data.texts.get("blend4vcam."+cam.name)
        if not textblock:
            textblock = bpy.data.texts.new("blend4vcam."+cam.name)
        textblock.clear()
        textblock.write(xmlstr)


        print (bl_camera)
#tree = ET.ElementTree(bl_camera)
#tree.write('xml_camera_blam.xml')

#xmlstr = ET.dump(bl_camera)
