
# coding: utf-8

# In[1]:


import math
import numpy as np
import tensorflow as tf
## Slim is an interface to contrib functions, examples and models.
import tensorflow.contrib.slim as slim
from tensorflow.python.framework import ops


# In[9]:


import math
import numpy as np
import tensorflow as tf
## Slim is an interface to contrib functions, examples and models.
import tensorflow.contrib.slim as slim
from tensorflow.python.framework import ops


def batch_normalization(x, name="Batch_normalization"):
    return tf.contrib.layers.batch_norm(
    x,
    decay=0.999,
    center=True,
    scale=True,
    epsilon=0.001,
    activation_fn=None,
    param_initializers=None,
    param_regularizers=None,
    updates_collections=None,
    is_training=True,
    reuse=None,
    variables_collections=None,
    outputs_collections=None,
    trainable=True,
    batch_weights=None,
    fused=None,
    data_format=DATA_FORMAT_NHWC,
    zero_debias_moving_mean=False,
    scope=name,
    renorm=False,
    renorm_clipping=None,
    renorm_decay=0.99,
    adjustment=None)


def instance_norm(x, name="instance_norm"):
    """
    instance normalization 
    paper's link = https://arxiv.org/pdf/1607.08022.pdf
    'it increases style transfering models' perfomance' 
    """
    with tf.variable_scope(name):
        depth = x.get_shape()[3]
        # two learnable parameters : scale, offset 
        scale = tf.get_variable("scale", [depth], initializer=tf.random_normal_initializer(1.0, 0.02, dtype=tf.float32))
        offset = tf.get_variable("offset", [depth], initializer=tf.constant_initializer(0.0))
        mean, variance = tf.nn.moments(x, axes=[1,2], keep_dims=True)
        epsilon = 1e-5
        inv = tf.rsqrt(variance + epsilon)
        normalized = (x-mean)*inv
        return scale*normalized + offset
    
def conv2d(input_, output_dim, kernel_size=4, stride=2, stddev=0.02, padding='SAME', name="conv2d"):
    """ generating conv2d layer
    
    args :
    input_ : input 
    output_dim : output_dim
    kernel_size : 4
    stride : 2 
    stddev : tf.truncated_normal_initializer(stddev=stddev)
    padding : SAME
    name : conv2d
    
    return :
    slim.conv2d(input_, output_dim, kernel_size, stride, padding=padding, activation_fn=None,
                            weights_initializer=tf.truncated_normal_initializer(stddev=stddev),
                            biases_initializer=None)

    """
    with tf.variable_scope(name):
        return slim.conv2d(input_, output_dim, kernel_size=kernel_size, stride=stride, 
                           padding=padding, activation_fn=None,
                            weights_initializer=tf.truncated_normal_initializer(stddev=stddev),
                            biases_initializer=None)

def deconv2d(input_, output_dim, ks=4, s=2, stddev=0.02, name="deconv2d"):
    """ generating conv2d_transpose layer
    
    args :
    input_ : input 
    output_dim : output_dim
    kernel_size : 4
    stride : 2 
    stddev : tf.truncated_normal_initializer(stddev=stddev)
    name : deconv2d
    
    return :
    slim.conv2d_transpose(input_, output_dim, ks, s, padding="SAME", activation_fn=None,
                                    weights_initializer=tr.truncated_normal_initializer(stddev=stddev),
                                    biases_initializer=None)
    """
    with tf.variable_scope(name):
        return slim.conv2d_transpose(input_, output_dim, ks, s, padding="SAME", activation_fn=None,
                                    weights_initializer=tr.truncated_normal_initializer(stddev=stddev),
                                    biases_initializer=None)
    
def leaky_relu(x, leak=0.2, name="leaky_relu"):
    return tf.maximum(x, leak * x)

def linear(input_, output_size, scope=None, stddev=0.02, bias_start=0.0, with_w=False):
    
    with tf.variable_scope(scope or "Linear"):
        
        matrix = tf.get_variable("Matrix", [input_.get_shape()[-1], output_size], tf.float32,
                                tf.random_normal_initializer(stddev=stddev))
        bias = tf.get_variable("bias", [output_size],
                                  initializer=tf.constant_initializer(bias_start))
        
        if with_w :
            return tf.matmul(input_, matrix) + bias, matrix, bias
        else:
            return tf.matmul(input_, matrix) + bias
        

