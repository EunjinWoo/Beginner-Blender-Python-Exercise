# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
import math

# add a cube into the scene
bpy.ops.mesh.primitive_cube_add()
# get a reference to the currently active object
cube = bpy.context.active_object

# insert keyframe at frame one
start_frame = 1
cube.keyframe_insert('rotation_euler',frame=start_frame) # == cube.keyframe_insert(datapath'rotation_euler',frame=1)

# change the rotation of the cube around y-axis
degrees = 90
radians = math.radians(degrees) # cube.rotation_euler[1] is possible too.
cube.rotation_euler.y = radians

# insert keyframe at the mid frame
mid_frame = 90
cube.keyframe_insert('rotation_euler',frame=mid_frame)

# change the rotation of the cube around x-axis
degrees = 90
radians = math.radians(degrees)
cube.rotation_euler.x = radians

# insert keyframe at the last frame
last_frame = 180
cube.keyframe_insert('rotation_euler',frame=last_frame)

# ------------------------------------------------
# math.radians(45) -> [degrees -> radians]

## reference : CG Python Youtube - Beginner Blender Python Exercise
