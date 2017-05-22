from trainFile import gen_text_and_image, max_result_length
from testFile import gen_test_text_and_image, get_test_length
import numpy as np
import tensorflow as tf

class cnn7:
    def __init__(self, imgs, weights=None, sess=None):
        self.imgs = imgs
        self.convlayers()
        self.fc_layers()
        self.probs = tf.nn.softmax(self.fc31)
        if weights is not None and sess is not None:
            self.load_weights(weights, sess)



if __name__ == '__main__':
    with tf.Session() as sess:
        imgs = tf.placeholder(tf.float32, [None, 160, 60, 3])

        prob = sess.run(vgg.probs, feed_dict={vgg.imgs: [img1]})[0]
        preds = (np.argsort(prob)[::-1])[0:5]
        for p in preds:
            print(class_names[p], prob[p])