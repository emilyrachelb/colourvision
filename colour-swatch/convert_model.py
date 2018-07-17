#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       convert_model.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 14, 2018
#   Description:    convert tensorflow model to coreml model

from __future__ import print_function

import urllib
import os
import sys
import zipfile
from os.path import dirname
import numpy as np
import tensorflow as tf
from tensorflow.core.framework import graph_pb2
import coremltools

# load the TF graph definition
tf_model_path = './colour_model_graph.pb'

with open(tf_model_path, 'rb') as f:
    serialized = f.read()

tf.reset_default_graph()
original_gdef = tf.GraphDef()
original_gdef.ParseFromString(serialized)

# show the first 25 ops of the TF model
with tf.Graph().as_default() as g:
    tf.import_graph_def(original_gdef, name='')
    ops = g.get_operations()

    for i in range(25):
        print('op id {} : op name: {}, op type: {}'.format(str(i),ops[i].name, ops[i].type))

# This model uses DecodeJpeg op to read from JPEG images,
# encoded as string Tensors. You can visualize with Tensorboard,
# but it is being omitted here. For deployment, the JPEG decoder
# and related ops need to be removed and replaced with a placeholder
# where image data can be fed in

# Strip the JPEG decoder and preprocessing part of the TF model
# In this model, the actual op that feeds the pre-processed image into
# the network is 'Mul'. The op that generates probabilities per class
# is 'final_result'. To figure out what are inputs/outputs for the model
# Use TensorFlow's summarize_graph or the TensorBoard visualization tool.

from tensorflow.python.tools import strip_unused_lib
from tensorflow.python.framework import dtypes
from tensorflow.python.platform import gfile

input_node_names = ['Mul']
output_node_names = ['final_result']

gdef = strip_unused_lib.strip_unused(
    input_graph_def= original_gdef,
    input_node_names=input_node_names,
    output_node_names=output_node_names,
    placeholder_type_enum = dtypes.float32.as_datatype_enum)

# save to an outputfile
frozen_model_file = './colour_model.pb'

with gfile.GFile(frozen_model_file, 'wb') as f:
    f.write(gdef.SerializeToString())

# TF model is now ready to be converted to coreml
import tfcoreml

# supply a dictionary of input tensors' name and shape (with batch axis)
input_tensor_shapes = {"Mul:0": [1, 299, 299, 3]} # batch size is 1

# output coreml model path
coreml_model_file = './ColourModel.mlmodel'

# The TF model's output tensor name
output_tensor_names = ['final_result:0']

# Call the converter. This may take a while
coreml_model = tfcoreml.convert(
        tf_model_path=frozen_model_file,
        mlmodel_path=coreml_model_file,
        input_name_shape_dict=input_tensor_shapes,
        output_feature_names=output_tensor_names,
        image_input_names = ['Mul:0'],
        red_bias = -1,
        green_bias = -1,
        blue_bias = -1,
        image_scale = 2.0/255.0)

model = coremltools.models.MLModel(coreml_model_file)
model.author = "Samantha Emily-Rachel Belnavis"
model.license = "MIT"
model.short_description = "Colour Recognition CoreML Model"

model.save(coreml_model_file)