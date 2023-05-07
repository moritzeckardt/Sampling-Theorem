# ~ A2 109.5866767044307
# ~ A3 220.66463546809896
# ~ A4 440.75
# ~ A5 883.4999999999999
# ~ A6 1776.2664088616589
# ~ A7 3610.2512476828747
# ~ D6 1179.8780167508098

import unittest
import numpy as np
import os

from exercise_1_piano import load_sample
from exercise_1_piano import compute_frequency

# set relative tolerance and number of matching decimals
RTOL = 0.01
N_DECIMALS = 2


class TestCalculation(unittest.TestCase):
    def test_download(self):
        if not os.path.exists('sounds'):
            raise Exception('The folder "sounds" was not found')
        for f in ('Piano.ff.A2.npy', 'Piano.ff.A4.npy', 'Piano.ff.A6.npy', 'Piano.ff.XX.npy', 'Piano.ff.A3.npy', 'Piano.ff.A5.npy', 'Piano.ff.A7.npy'):
            filepath = os.path.join('sounds', f)
            if not os.path.exists(filepath):
                raise Exception('Cannot find file %s' % filepath)
        
    def test_load_sample(self):
        res = load_sample(os.path.join('sounds', 'Piano.ff.A2.npy'), duration=1291)
        self.assertIsNot(res, None)
        self.assertEqual(res.shape, (1291,))
        self.assertAlmostEqual(res[0], 0.10849756)
    
    def test_compute_frequency(self):
        signal = np.sin([x/5.436658878408203 for x in range(441000)])
        f = compute_frequency(signal)
        self.assertAlmostEqual(f, 1291, places=4) # if this fails: check the search of the peak
        s = 0
        for f in ('Piano.ff.A2.npy', 'Piano.ff.A4.npy', 'Piano.ff.A6.npy'):
            sample = load_sample(os.path.join('sounds', 'Piano.ff.A4.npy'))
            s += compute_frequency(sample)
        self.assertLess(abs(s-1322.25), 5) # if this fails, maybe finding the start of the note fails
    
if __name__ == '__main__':
    unittest.main()
