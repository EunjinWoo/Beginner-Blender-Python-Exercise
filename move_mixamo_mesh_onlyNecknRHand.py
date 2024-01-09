# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
import math

# get a reference to the currently active object
armature = bpy.context.active_object # bpy.context.active_object / bpy.data.objects['Armature']
neck = armature.pose.bones['mixamorig9:Neck']
right_hand = armature.pose.bones['mixamorig9:RightHand']

# set each bone's rotation mode to 'ZXY'(euler) from 'QUATERNION'
neck.rotation_mode = 'ZXY'
right_hand.rotation_mode = 'ZXY'

# insert keyframe at frame one
start_frame = 1
neck.keyframe_insert('rotation_euler',frame=start_frame)
right_hand.keyframe_insert('rotation_euler',frame=start_frame)

# change the location of the targeted bone of the armature on the z-axis
#neck = armature.pose.bones['mixamorig9:Neck']

degrees = 360
radians = math.radians(degrees) 
neck.rotation_euler.z = radians # cube.rotation_euler[2] is possible too.

degrees = 90
radians = math.radians(degrees) 
right_hand.rotation_euler.z = radians # cube.rotation_euler[2] is possible too.

# insert keyframe at frame one
end_frame = 180
neck.keyframe_insert('rotation_euler',frame=end_frame)
right_hand.keyframe_insert('rotation_euler',frame=end_frame)
