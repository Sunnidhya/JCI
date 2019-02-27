# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:38:12 2019

@author: jroysu
"""

from pykalman import KalmanFilter as KF
import numpy as np
kf = KF(transition_matrices = [[1,1],[0,1]], observation_matrices = [[0.1,0.5],[-0.3,0.0]])
measure = np.asarray([[0.0259552001953125,-0.3058624267578125],
                      [0.0084686279296875,-0.326202392578125],
                      [-0.013336181640625,-0.27691650390625],
                      [-0.0063323974609375,-0.3102874755859375],
                      [0.0027313232421875,-0.3132781982421875],
                      [-0.0302276611328125,-0.2928619384765625],
                      [-0.028411865234375,-0.280670166015625],
                      [0.0291900634765625,-0.3231964111328125],
                      [0.032012939453125,-0.349884033203125],
                      [0.0872650146484375,-0.3453826904296875],
                      [0.02099609375,-0.3380279541015625],
                      [0.0034027099609375,-0.306243896484375],
                      [0.0285797119140625,-0.3502349853515625],
                      [0.0035247802734375,-0.2036590576171875],
                      [-0.03045654296875,-0.2128143310546875],
                      [0.008880615234375,-0.2248077392578125],
                      [0.007476806640625,-0.251556396484375],
                      [-0.0158233642578125,-0.294219970703125],
                      [0.0392303466796875,-0.395904541015625],
                      [0.004852294921875,-0.156585693359375],
                      [0.15362548828125,-0.3006134033203125],
                      [0.049407958984375,-0.2059478759765625],
                      [0.046844482421875,-0.2570953369140625],
                      [0.115386962890625,-0.3175048828125],
                      [0.14532470703125,-0.287384033203125],
                      [0.0682830810546875,-0.24188232421875],
                      [0.0101165771484375,-0.2095184326171875],
                      [0.04425048828125,-0.3264007568359375],
                      [0.0078582763671875,-0.318878173828125]])
(filtered_state_means,filtered_state_covariances) = kf.filter(measure)
(filtered_state_means1,filtered_state_covariances1) = kf.smooth(measure)

print((filtered_state_means,filtered_state_covariances))
print((filtered_state_means1,filtered_state_covariances1))