# give Python access to Blender's functionality
import bpy

# import numpy
import numpy as np

# extend Python's math functionality
#import math

# targets
targets = ["mixamorig9:LeftUpLeg", 
           "mixamorig9:LeftLeg",
           "mixamorig9:LeftFoot",
           "mixamorig9:RightUpLeg",
           "mixamorig9:RightLeg",
           "mixamorig9:RightFoot",
           "mixamorig9:LeftShoulder", 
           "mixamorig9:LeftForeArm",
           "mixamorig9:LeftHand",
           "mixamorig9:RightShoulder", 
           "mixamorig9:RightForeArm",
           "mixamorig9:RightHand",
           "mixamorig9:Hips", 
           "mixamorig9:Neck",]

# eulerangles frame 0
#euler_frame0 = [
#                np.array([-0.07880185, 0.05177845, 0.00204163]), 
#                np.array([-0.00950117, -0.33642704, -0.00161348]), 
#                np.array([0., 0., 0.]), 
#                np.array([ 0.0900822 , 0.0880531 , -0.00397125]), 
#                np.array([-0.04939234, -0.24646739, -0.00611903]), 
#                np.array([0., 0., 0.]), 
#                np.array([-0.01594712, 0.00780151, -0.90994567]), 
#                np.array([ 0.93867956, -0.08973764, -0.17660835]), 
#                np.array([0., 0., 0.]), 
#                np.array([0.0533663 , 0.02459438, 0.863554 ]), 
#                np.array([-0.73090292, -0.14607527, 0.37787561]), 
#                np.array([0., 0., 0.]), 
#                np.array([ 0.01856307, 0.28056028, -0.06883403]), 
#                np.array([5.00233233e-04, 2.20672709e-02, 3.09626514e+00])
#                ]
                
euler_frame0 = [
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                np.array([1.,1.,1.]), 
                ]

# get a reference to the currently active object
armature = bpy.context.active_object # bpy.context.active_object / bpy.data.objects['Armature']
#neck = armature.pose.bones['mixamorig9:Neck']

for bone_name in targets:
    # set each bone's rotation mode to 'ZXY'(euler) from 'QUATERNION'
    armature.pose.bones[bone_name].rotation_mode = 'ZXY'
    
    for euler_angles in euler_frame0:
        for i, angle in enumerate(euler_angles):
            armature.pose.bones[bone_name].rotation_euler[i] = angle

# insert keyframe at frame one
#start_frame = 1
#neck.keyframe_insert('rotation_euler',frame=start_frame)

# change the location of the targeted bone of the armature on the z-axis
#neck = armature.pose.bones['mixamorig9:Neck']

# insert keyframe at frame one
#end_frame = 180
#neck.keyframe_insert('rotation_euler',frame=end_frame)
