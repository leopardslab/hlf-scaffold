from yaml import load, dump
from crypto_config_generator import CryptoConfig 
from new_config_generator import Configtx
import argparse


def main():
# display some lines
    # parser = argparse.ArgumentParser(description='Generate a HyperLedger Network.')
    # parser.add_argument('no_of_orderer_nodes', type=int, help='')
    # parser.add_argument('no_of_peer_nodes', type=int, help='')


    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

    # config = CryptoConfig(4, 1)
    # config.set_default_values()

    congfigtx = Configtx(5, 1, 3)
    #congfigtx.generate_default()

if __name__ == "__main__":main()
    