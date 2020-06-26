from yaml import load, dump

import argparse




def main():
# display some lines
    parser = argparse.ArgumentParser(description='Generate a HyperLedger Network.')
    parser.add_argument('no_of_orderer_nodes', type=int, help='')
    parser.add_argument('no_of_peer_nodes', type=int, help='')


    args = parser.parse_args()
    print(args.accumulate(args.integers))

    print(1)

if __name__ == "__main__": main()