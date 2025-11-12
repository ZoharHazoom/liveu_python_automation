# Concept
# Manage setup/teardown cleanly — use with or implement __enter__/__exit__.
import os


# with open("log.txt", "w") as f:
#     f.write("Automation run started\n")

# class Timer:
#     import time
#
#     def __enter__(self):
#         self.start = self.time.time()
#         return self
#
#     def __exit__(self, *args):
#         print(f"Took {self.time.time() - self.start:.3f}s")
#
#
# with Timer():
#     sum(i for i in range(10_000_000))

# Exercise: create a context manager that temporarily changes a directory (os.chdir) and restores it.
class DirectoryChanger:

    import os

    def __enter__(self):
        self.current_working_dir = os.getcwd()
        os.chdir('C:\\Users')
        print(f'Working dir changed to be "C:\\Users" ')
        return self

    def __exit__(self, *args):
        os.chdir(self.current_working_dir)
        print(f'Working dir is returned to be {self.current_working_dir}')

with DirectoryChanger():
    pass



