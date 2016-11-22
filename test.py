# coding=utf-8
# pylint: disable=C0111,too-many-arguments,too-many-instance-attributes,too-many-locals,redefined-outer-name,fixme
# pylint: disable=superfluous-parens, no-member, invalid-name
import sys

sys.path.insert(0, "../../python")
import mxnet as mx
import numpy as np
import cv2


def get_symbol(num_classes=3750):
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

def TestRecognizeOne(img):
    cv2.imshow("img", img);

    print img.shape
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2)
    print img.shape
    batch_size = 1
    _, arg_params, __ = mx.model.load_checkpoint("None", 3)
    data_shape = [("data", (batch_size, 3, 32, 32))]
    input_shapes = dict(data_shape)
    sym = get_symbol()
    executor = sym.simple_bind(ctx=mx.cpu(), **input_shapes)
    for key in executor.arg_dict.keys():
        if key in arg_params:
            arg_params[key].copyto(executor.arg_dict[key])

    executor.forward(is_train=True, data=mx.nd.array([img]))
    probs = executor.outputs[0].asnumpy()
    print probs
    for i in range(probs.shape[0]):
        result = np.argmax(probs[i])
        print  result
    cv2.waitKey(0)


if __name__ == '__main__':
    TestRecognizeOne(cv2.imread("5.jpg"))
