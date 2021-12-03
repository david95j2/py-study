import tensorflow as tf

A = tf.Variable(([1.],[2.]))
B = tf.constant(([3.],[4.]))
C = tf.matmul(A,B)
