import keras
import sys
import numpy as np
import json

class SimilarModel(object):
    def __init__(self):
        print("\n** LOADING MODEL from pairwise_top_100_per_member_id.json **")
        with open('pairwise_top_100_per_member_id.json') as fp:
            self.model = json.load(fp) 
        print("\n** LOADED MODEL from pairwise_top_100_per_member_id.json **")

    def predict(self, X, feature_names, **kwargs):
        convert_image_to_width = 224
        convert_image_to_height = 224
        profile_pic = './images/%s_0.png' % str(X[0])
        similar_image_arr = self.model[str(X[0])]
        return similar_image_arr

if __name__== "__main__":
    model = SimilarModel()
    print(model.predict([0], ['member_id']))
