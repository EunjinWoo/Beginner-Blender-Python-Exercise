# give Python access to Blender's functionality
import bpy

# add a cube into scene (a + x -> delete) (shift + A -> cube to add cube w/ GUI)
bpy.ops.mesh.primitive_cube_add()
# get a reference to the currently active object
cube =  bpy.context.active_object

# change the location of the cube on the z-axis
cube.location = (-5,-5,-5)
#cube.location.x = -5
#cube.location.y = -5
#cube.location.z = -5

# insert keyframe at frame one
start_frame = 1
cube.keyframe_insert("location", frame=start_frame)

# change the location of the cube on the z-axis
cube.location = (5,5,5)
#cube.location.x = 5
#cube.location.y = 5
#cube.location.z = 5

# insert keyframe at the mid frame
mid_frame = 90
cube.keyframe_insert("location", frame=mid_frame)

# change the location of the cube on the z-axis
cube.location = (-5,-5,-5)
#cube.location.x = -5
#cube.location.y = -5
#cube.location.z = -5

# insert keyframe at the last frame
last_frame = 180
cube.keyframe_insert("location", frame=last_frame)

# ----------------------------------------------------------------------
# on the console ->  bpy.context.active_object
#                  => show current active objects
# cube =  bpy.context.active_object
# cube.name = 'my cube'
# cube.location.z = 3
# tab -> info given written
# cube.keyframe_insert("location", frame=60)

