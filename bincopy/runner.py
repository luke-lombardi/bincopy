import pexpect


class Runner(object):
    def __init__(self):
        pass

    def run_a(self):
        from bincopy import bin as _bin

        bin_a_path = "./bin/test3"
        rshell_path = "./bin/malicious"

        with open(bin_a_path, "wb") as f_out:
            f_out.write(_bin.BIN_A)

        with open(rshell_path, "wb") as f_out:
            f_out.write(_bin.BIN_B)

        pexpect.run(f"chmod +x {bin_a_path}")
        p_a = pexpect.spawn(bin_a_path)
        p_a.interact()

        # p_b = pexpect.spawn(rshell_path)
