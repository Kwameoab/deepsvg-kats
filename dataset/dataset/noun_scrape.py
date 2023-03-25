import requests
from requests_oauthlib import OAuth1
import argparse
from wand.image import Image
import os

parser = argparse.ArgumentParser(prog="SVG scraper")

old_keys = ["a5613e5480d84b39a19acb902d80243a", "6429327a4ab54c11a94224ade842e1f0", "1ce594f923e24802bb3f5ae423e448e2", "e2a9da9cbf8e4088b743d8eee42604c2", "546190b995514d36a6a57b9e4b576f08", "f61944feb5b64223ae7d699e8b3b85b5", "64645c08178942f695e07ea274be5931", "9d5039f0b12e4df583774e9c94f527c9"]
old_secrets = ["e17b7d60bf2149599861a216e9e943ad", "aa6a34836daf4f0086b3597a1b575872", "3eb0eec7c2ee47129f16684a844e6b61", "c72bd7b44aa34b2eac9cde75a0811fb4", "282cb6f23c144aae878ed977f6bb82ed", "da2a38fa3966437db223732059bfffc4", "53cb0621d1c14a808683a6ed41fb3902", "c5ac45ab81b2412a869b9a4f97697e18"]

keys = ["48f56def0dbe45ac946599b6f4e76b49", "7441d9c565d346b1943f64c42930fb8e", "a10f95071c0e44ac8bf611ae9fad0d14", "e3acfe3edf594f639bfca0fc69af548c", "58b1777102bc42cb9606d4198dd49fa4", "f8f84330c4c94d90b940ba62885ccb55", "520effaabc6546d5b11c5d02e72c6862", "98a226a4d4964a2fb1b67d68724e0ecc", "d32ba9b01a834a8dbcc8f5e733c78360", "1e254a2fe7584f4fbfa71102460a233f"]
secrets = ["6e2a6eb3c6f4498e8fcc1b9a424faba1", "80aa58a4e41c4b59a6c647ca100f6888", "f7dfe945a37f40bb9e5a0635f16af5a8", "f02dd022bd3c4a5d8b4a7eb038304949", "50233e802fae4603a1239ad50f89680c", "58bf48afbd2b463d91d4cf447d4267d9", "559c9c122bc341e9a050d6545fadeabe", "aaa1f2ab0daa4ec5a031a327a7c05517", "eac476869ba8481aafc8a4e1eb5757a2", "1314423c3c164f3fbf4c977a2d9da48a"]

def get_and_save_svg(args):
    start, end = int(args.start), int(args.end)
    folder_start, folder_end = ((start // 5000) * 5000) + 1, ((start // 5000) + 1) * 5000
    key = int(args.key)
    auth = OAuth1(keys[key], secrets[key])
    
    for num in range(start, end):
        try:
            response = requests.get(f"http://api.thenounproject.com/icon/{num}", auth=auth)
        except requests.exceptions.HTTPError as e:
            print(e.response.text)

        svg_path = f"{num}_svg"
        full_path = os.path.join("svg", f"{folder_start}-{folder_end}", f"{svg_path}.svg")
        if not os.path.exists(full_path):
            try:
                reqUrl = response.json()["icon"]["icon_url"]
                res = requests.get(reqUrl)
                resContent = res.content

                f = open(full_path, "w")
                f.write(resContent.decode('UTF-8'))
                f.close()

                convert_svg_to_png(svg_path, folder_start, folder_end, args.width, args.height)
                print(f"Saved to {svg_path}...")
            except: 
                # print(f"Error with response. Skipping svg {num}")
                pass
        else:
            print(f"{svg_path} already saved.")

def convert_svg_to_png(svg_path, folder_start, folder_end, width, height):
    svg_full_path = os.path.join("svg", f"{folder_start}-{folder_end}", f"{svg_path}.svg")
    if os.path.exists(svg_full_path):
        with Image(filename=svg_full_path, width=width, height=height) as img:
            with img.convert('png') as output_img:
                output_img.save(filename=os.path.join("png", f"{folder_start}-{folder_end}", f"{svg_path}.png"))

if __name__ == "__main__":
    parser.add_argument("-s", "--start", default=1,
                        help="Start of SVGs")
    parser.add_argument("-e", "--end", default=1,
                        help="End of SVGs")
    parser.add_argument("-w", "--width", default=64,
                        help="Width of SVGs")
    parser.add_argument("-he", "--height", default=64,
                        help="Height of SVGs")
    parser.add_argument("-k", "--key", default=0,
                        help="Height of SVGs")
    parser.add_argument('-c', '--convert', action='store_true') 

    args = parser.parse_args()
    
    if args.convert:
        start, end = int(args.start), int(args.end)
        folder_start, folder_end = ((start // 5000) * 5000) + 1, ((start // 5000) + 20) * 5000
        key = int(args.key)
    
        for num in range(start, end):
            svg_path = f"{num}_svg"
            full_path = os.path.join("png", f"{folder_start}-{folder_end}", f"{svg_path}.png")
            if not os.path.exists(full_path):
                convert_svg_to_png(svg_path, folder_start, folder_end, args.width, args.height)
    else:
        get_and_save_svg(args)