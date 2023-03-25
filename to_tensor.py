from deepsvg.svglib.geom import Point
from deepsvg.svglib.svg import SVG
from deepsvg.svglib.svg_path import SVGPath
from deepsvg.svglib.utils import to_gif

from deepsvg.difflib.tensor import SVGTensor
from deepsvg.difflib.utils import *
from deepsvg.difflib.loss import *
import pickle

import os

path = "./dataset/svgs_simplified"
dir_list = os.listdir(path)

for file in dir_list:
    svg = SVG.load_svg(f"./dataset/svgs_simplified/{file}").normalize().zoom(0.9).canonicalize().simplify_heuristic()
    svg_dict = {}
    svg_dict['tensors'] = [[svg.to_tensor()]]
    svg_dict['fillings'] = svg.to_fillings()

    # print(svg_dict['tensors'][0])
    # with open(f"./dataset/svgs_simp_tensor/{file[:-4]}.pkl", "rb") as f:
    #     data = pickle.load(f)
    #     print(data)


    # break
    # with open(f"./dataset/icons_tensor/0.pkl", "rb") as f:
    #     data = pickle.load(f)
        # print(data['tensors'][0])
    #     # data = dict(data)
    #     # print(len(data['tensors']))
        # print(data)
    
    # break


    # torch.save(svg_dict, f"./dataset/svgs_simp_tensors/{file[:-4]}.pkl")
    pickle.dump(svg_dict, open(f"./dataset/svgs_simp_tensor/{file[:-4]}.pkl", "wb"))
