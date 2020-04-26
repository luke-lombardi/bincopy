import sys
import argparse

from bincopy.dump import Dump
from bincopy.runner import Runner

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out", type=str, default=None, help="output executable filename"
    )

    args = parser.parse_args()
    d = Dump(bin_a="/bin/ls", bin_b="./bin/test2")
    d.dump()

    r = Runner()
    r.run_a()
