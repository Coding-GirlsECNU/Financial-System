import os
import uuid
import subprocess
MODELS = {
    "triformer":"E:\\python310\\python G:\\desktop\\ToTrain\\train\Triformer\\main.py --data ETTh1 --model pa"
}

COLS = {
    "triformer":[
        ("date","datetime"),
        ("y","float"),
        ("y_pred","float")
    ]
}
import re 
def parse(data):
    x_values = [int(match.group(1)) for match in re.finditer(r'x:(\d+)', data)]
    y_values = [float(match.group(1)) for match in re.finditer(r'y:(.\d+)', data)]
    return x_values, y_values
        

if __name__ == '__main__':
    with open('./78f3e7da484c45d4b76c33a582ee185e') as f :
        data = f.read()
        print(parse(data))


