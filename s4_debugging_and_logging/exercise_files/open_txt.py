import pstats
import os
import snakeviz
print(os.getcwd())
p = pstats.Stats('dtu_mlops_fork/s4_debugging_and_logging/exercise_files/cProfile.prof')
p.sort_stats('cumulative').print_stats(10)
