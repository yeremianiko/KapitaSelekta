from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from packages.classifier import training

datadir = './pre_img'
modeldir = './model_checkpoints/20180402-114759/'
classifier_filename = './model_checkpoints/my_classifier_1.pkl'
print ("Training Start")
obj=training(datadir,modeldir,classifier_filename)
get_file=obj.main_train()
print('Saved classifier model to file "%s"' % get_file)
sys.exit("All Done")
