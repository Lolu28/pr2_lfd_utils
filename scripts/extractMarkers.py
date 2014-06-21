#! /usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2014, Karol Hausman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# author: Karol Hausman

import rospy 
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pr2_lfd_utils import generalUtils
from pr2_lfd_utils import trajUtils
from pr2_lfd_utils import arWorldModel
from pr2_lfd_utils import drawUtils
import sys
import os
import os.path
      
if __name__ == '__main__':
    try:
    
        rospy.init_node('ExtractMarkersNode')

   
        #Setup utilities and world model
        gen_utils = generalUtils.GeneralUtils()
        traj_utils = trajUtils.TrajUtils()
        draw_utils = drawUtils.DrawUtils()
        wm = arWorldModel.ARWorldModel()

        marker_ids = []
        if (len(sys.argv) >= 3):
            skill_id = int(sys.argv[1])
            for id in sys.argv[2:]:
              marker_ids.append(id)
        else:
            print "\nAborting! Wrong number of command line args"
            print "Usage: python extractMarkers <skill_id> <marker_id> <marker_id> <marker_id> ..."
            sys.exit(0)

        #Construct file names
        basename = 'data/bagfiles/markers_flat/'
        markerfile = basename + 'Marker' + str(skill_id) + '.txt'

        marker_goal_data = []
        marker_difference_data = []

        for i in range (len(marker_ids)):
          print marker_ids[i]
          marker_goal_data.append(traj_utils.createMarkerTrajFromFile(markerfile, int(marker_ids[i]), -1))
          if ((i%2) == 1):
            marker_difference_data.append(traj_utils.createDifferenceTrajFromFile(markerfile, int(marker_ids[i-1]), int(marker_ids[i])))
            [diff, drawable] = traj_utils.createDifferenceTrajFromFile(markerfile, int(marker_ids[i-1]), int(marker_ids[i]))
        
        print drawable

    except rospy.ROSInterruptException:
        print "program interrupted before completion"
            
            