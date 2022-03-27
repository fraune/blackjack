import numpy

"""
Results of this q-table after 1000 episodes (dealer cheats)
  player losses = 244
  player wins   = 288
  player ties   = 468
"""

human_created_q_table = numpy.array(
    [
        [100, 0],  # Score is 1 - Hit/Stand
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],
        [100, 0],  # Score is 15 - Hit/Stand
        [0, 100],  # Score is 16 - Hit/Stand
        [0, 100],
        [0, 100],
        [0, 100],
        [0, 100],
        [0, 100],  # Score is 21 - Hit/Stand
        [0, 100],  # Player win - Hit/Stand
        [0, 100],  # Player lost - Hit/Stand
    ]
)
