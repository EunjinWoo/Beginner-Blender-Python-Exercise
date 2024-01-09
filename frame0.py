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
           "mixamorig9:Neck",
           ]

# eulerangles frame 0
euler_frame0 = [
                # LeftUpLeg
                np.array([-0.07880185, 0.05177845, 0.00204163]), 
#                np.array([0.,0.,0.]),
                
                # LeftLeg
                [-0.00950117, -0.33642704, -0.00161348], 
#                np.array([0.,0.,0.]),
                
                # LeftFoot
                [0., 0., 0.], 
#                np.array([0.,0.,0.]),
                
                # RightUpLeg
                [ 0.0900822 , 0.0880531 , -0.00397125], 
#                np.array([0.,0.,0.]),
                
                # RightLeg
                [-0.04939234, -0.24646739, -0.00611903], 
#                np.array([0.,0.,0.]),
                
                # RightFoot
                [0., 0., 0.], 
#                np.array([0.,0.,0.]),
                
                # LeftShoulder
#                [-0.01594712, 0.00780151, -0.90994567], 
                [-0.01594712, 0.00780151, 0.90994567], 
#                np.array([0.,0.,0.]),
                
                # LeftForeArm
#                [ 0.93867956, -0.08973764, -0.17660835], 
                [ 0.93867956, -0.08973764, 0.17660835], 
#                np.array([0.,0.,0.]),
                
                # LeftHand
                [0., 0., 0.], 
#                np.array([0.,0.,0.]),
                
                # RightShoulder
#                [0.0533663 , 0.02459438, 0.863554 ], 
                [0.0533663 , 0.02459438, -0.863554 ], 
#                np.array([0.,0.,0.]),
                
                # RightForeArm
#                [-0.73090292, -0.14607527, 0.37787561], 
                [-0.73090292, -0.14607527, -0.37787561], 
#                np.array([0.,0.,0.]),
                
                # RightHand
                [0., 0., 0.], 
#                np.array([0.,0.,0.]),
                
                # Hips
                [ 0.01856307, 0.28056028, -0.06883403],
#                np.array([0.,0.,0.]),
                
                # Neck
                [5.00233233e-04, 2.20672709e-02, 3.09626514e+00],
#                np.array([0.,0.,0.]),
                
                ]
                
#euler_frame0 = [
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                np.array([1.,1.,1.]), 
#                ]

#euler_frame0 = [
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                np.array([0.,0.,0.]),
#                ]

# get a reference to the currently active object
armature = bpy.context.active_object # bpy.context.active_object / bpy.data.objects['Armature']

for bone_index, bone_name in enumerate(targets):
    # set each bone's rotation mode to 'ZXY'(euler) from 'QUATERNION'
    armature.pose.bones[bone_name].rotation_mode = 'ZXY'
#    
    for i, angle in enumerate(euler_frame0[bone_index]):
        print(bone_name + str(i) + " " + str(angle))
        armature.pose.bones[bone_name].rotation_euler[i] = angle
#            armature.pose.bones[bone_name].rotation_euler = euler_angles
