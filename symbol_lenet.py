"""
Reference:

Krizhevsky, Alex, Ilya Sutskever, and Geoffrey E. Hinton. "Imagenet classification with deep convolutional neural networks." Advances in neural information processing systems. 2012.
"""
import find_mxnet
import mxnet as mx

def get_symbol(num_classes = 1000):
    data = mx.symbol.Variable('data')

    # stage 1
    conv1 = mx.symbol.Convolution(data=data, kernel=(5, 5), num_filter=20)
    relu1 = mx.symbol.Activation(data=conv1, act_type="relu")
    pool1 = mx.symbol.Pooling(data=relu1, pool_type="max",kernel=(2, 2), stride=(2, 2))
    # stage 2
    conv2 = mx.symbol.Convolution(data=pool1, kernel=(5, 5), num_filter=50)
    relu2 = mx.symbol.Activation(data=conv2, act_type="relu")
    pool2 = mx.symbol.Pooling(data=relu2, pool_type="max",kernel=(2, 2), stride=(2, 2))

    # stage 3
    flatten = mx.symbol.Flatten(data=pool2)
    fc1 = mx.symbol.FullyConnected(data=flatten, num_hidden=5000)
    relu3 = mx.symbol.Activation(data=fc1, act_type="relu")

    # stage 4
    fc2 = mx.symbol.FullyConnected(data=relu3, num_hidden=num_classes)
    # loss
    lenet = mx.symbol.SoftmaxOutput(data=fc2, name='softmax')
    return lenet