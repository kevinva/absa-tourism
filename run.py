import torch
import torch.nn as nn
from config import *

def train():
   pass


if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    tokenizer = build_tokenizer(

    )