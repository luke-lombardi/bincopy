class Dump(object):
    def __init__(self, *, bin_a, bin_b):
        self.bin_a_filename = bin_a
        self.bin_b_filename = bin_b

    def dump(self):
        # load binaries
        with open(self.bin_a_filename, "rb") as f_in:
            _raw_bin_a = str(f_in.read())

        with open(self.bin_b_filename, "rb") as f_in:
            _raw_bin_b = str(f_in.read())

        # dump to module
        with open("./bincopy/bin.py", "w") as f_out:
            f_out.write(f"BIN_A={_raw_bin_a}\n")

        with open("./bincopy/bin.py", "a") as f_out:
            f_out.write(f"\nBIN_B={_raw_bin_a}\n")
