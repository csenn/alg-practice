
def write_files():
    f1 = open('data1.txt', 'w')
    f2 = open('data2.txt', 'w')
    for i in range(100):
        val = str(i) + '\n'
        if i % 2 == 0:
            f1.write(val)
        else:
            f2.write(val)
    f1.close()
    f2.close()

# write_files()


class Merge():
    def __init__(self):
        self.f1 = open('data1.txt', 'r')
        self.f2 = open('data2.txt', 'r')

    def do_merge(self):
        result = open('data_result.txt', 'w')
        f1_buffer, f2_buffer = None, None
        f1_done, f2_done = False, False
        while True:
            if not f1_done and not f1_buffer:
                f1_buffer = int(self.f1.readline())
                if not f1_buffer:
                    f1_done = True

            if not f2_done and not f2_buffer:
                f2_buffer = int(self.f2.readline())
                if not f2_buffer:
                    f2_done = True

            if f1_done and f2_done:
                break


            if not f1_buffer:
                write_val = f2_buffer
                f2_buffer = None
            elif not f2_buffer:
                write_val = f1_buffer
                f1_buffer = None
            elif f1_buffer < f2_buffer:
                write_val = f1_buffer
                f1_buffer = None
            else:
                write_val = f2_buffer
                f2_buffer = None

            result.write(str(write_val) + '\n')

        result.close()

merge = Merge()
merge.do_merge()
