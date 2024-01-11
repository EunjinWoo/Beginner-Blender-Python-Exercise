# give Python access to Blender's functionality
import bpy

# import numpy
import numpy as np

# extend Python's math functionality
import math

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
                [-0.01594712, 0.00780151, -0.90994567], 
#                np.array([0.,0.,0.]),
                
                # LeftForeArm
                [ 0.93867956, -0.08973764, -0.17660835], 
#                np.array([0.,0.,0.]),
                
                # LeftHand
                [0., 0., 0.], 
#                np.array([0.,0.,0.]),
                
                # RightShoulder
                [0.0533663 , 0.02459438, 0.863554 ],
#                np.array([0.,0.,0.]),
                
                # RightForeArm
                [-0.73090292, -0.14607527, 0.37787561],
#                np.array([0.,0.,0.]),
                
                # RightHand
                [0., 0., 0.], 
#                np.array([0.,0.,0.]),
                
                # Hips
                [ 0.01856307, 0.28056028, -0.06883403],
#                np.array([0.,0.,0.]),
                
                # Neck
                np.array([5.00233233e-04, 2.20672709e-02, 3.09626514e+00]),
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

# Decompose ZXY
#euler_frame300 = [
#                np.array([ 0.62597033,  0.72275924, -0.24343524]), 
#                np.array([-0.32280454, -0.22570775, -0.03690204]), 
#                np.array([0., 0., 0.]), 
#                np.array([-0.06397794,  0.60802306,  0.02007843]), 
#                np.array([ 0.08519165, -0.02473634,  0.00105436]), 
#                np.array([0., 0., 0.]), 
#                np.array([-0.23429985, -0.01458588,  0.12377988]), 
#                np.array([-0.25497261,  0.01959656, -0.15258947]), 
#                np.array([0., 0., 0.]), 
#                np.array([ 1.51105682, -0.39924061, -0.42312582]), 
#                np.array([1.33255188, 0.21414169, 0.27173313]), 
#                np.array([0., 0., 0.]), 
#                np.array([-0.23631965,  0.04637208, -0.21550363]), 
#                np.array([-0.8561505 ,  1.25292613, -2.01651646]),
#                ]

# Decompose ZYX
euler_frame300 = [
                np.array([ 0.32018722,  0.68415048, -0.11486783]), 
                np.array([-0.25548312, -0.20419534, -0.02631704]), 
                np.array([0., 0., 0.]), 
                np.array([-0.21402233,  0.56639147,  0.06250273]), 
                np.array([ 0.04928659, -0.03057812,  0.00075376]), 
                np.array([0., 0., 0.]), 
                np.array([-0.15513398, -0.03059995,  0.38876468]), 
                np.array([ 0.06076612, -0.00903323, -0.29506237]), 
                np.array([0., 0., 0.]), 
                np.array([2.17589188, 0.94828593, 0.52562199]), 
                np.array([0.77629487, 0.27334028, 0.64891303]), 
                np.array([0., 0., 0.]), 
                np.array([-0.03017312,  0.04746849, -0.21526832]), 
                np.array([-3.10736546,  2.90196898, -0.28244139]),
                ]
                
# Decompose XYZ (ChatGPT)
#euler_frame300 = [
#                np.array([0.73255337, 0.18135932, 0.46550754]), 
#                np.array([-0.22184923,  0.03565699, -0.31747326]), 
#                np.array([0., 0., 0.]), 
#                np.array([ 0.60960953, -0.01657267, -0.05266613]), 
#                np.array([-0.02572539, -0.00109238,  0.08487076]), 
#                np.array([0., 0., 0.]), 
#                np.array([ 0.01481046,  0.12507051, -0.23543574]), 
#                np.array([-0.01970438, -0.15113364, -0.25881184]), 
#                np.array([0., 0., 0.]), 
#                np.array([ 0.43963495, -0.39352699,  1.68461238]), 
#                np.array([-0.21748485,  0.25988217,  1.3919602 ]), 
#                np.array([0., 0., 0.]), 
#                np.array([-0.00476714, -0.2108183 , -0.23487474]), 
#                np.array([-1.70763234, -0.27643974, -2.90024129])
#                ]

# get a reference to the currently active object
armature = bpy.context.active_object # bpy.context.active_object / bpy.data.objects['Armature']

for bone_index, bone_name in enumerate(targets):
    # set each bone's rotation mode to 'ZXY'(euler) from 'QUATERNION'
    armature.pose.bones[bone_name].rotation_mode = 'ZXY'
#    
    for i, angle in enumerate(euler_frame300[bone_index]):
        print(f"{bone_name}{i} {angle:.4e}")
        # put each bone_angle array into ZXY angles of this character's rotation angle
        armature.pose.bones[bone_name].rotation_euler[(i+2)%3] = angle
#            armature.pose.bones[bone_name].rotation_euler = euler_angles
        
#    if bone_name == 'mixamorig9:Neck':
#        armature.pose.bones[bone_name].rotation_euler.y += math.radians(180)
