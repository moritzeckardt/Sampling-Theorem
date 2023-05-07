import unittest
import numpy as np
from chirp import createChirpSignal
from decomposition import createTriangleSignal, createSquareSignal, createSawtoothSignal

# set relative tolerance and number of matching decimals
RTOL = 0.01
N_DECIMALS = 2


def round_tuple(t: tuple) -> tuple:
    return tuple(round(e, ndigits=N_DECIMALS) for e in t)


class TestChirp(unittest.TestCase):
    def setUp(self):
        try:
            # load linear chirp with params createChirpSignal(200, 1, 1, 20, True) with arrange and linspace as x-axis
            self.truth_lin_2 = np.load('signals/chirpsig_lin_2.npy')
            self.truth_lin_2_arrange = np.load('signals/chirpsig_lin_2_arrange.npy')

            # load exp chirp with params createChirpSignal(200, 1, 1, 20, False) with arrange and linspace as x-axis
            self.truth_exp_2 = np.load('signals/chirpsig_ex_2.npy')
            self.truth_exp_2_arrange = np.load('signals/chirpsig_ex_2_arrange.npy')

        except IOError:
            print("Test Setup failed. Missing ground truth files!")
        except ValueError:
            print("Test Setup failed. Ground Truth files are corrupted!")

    def test_chirp_uses_numpy(self):
        # get the student answer
        observed = createChirpSignal(200, 1, 1, 20, False)
        self.assertIsInstance(observed, np.ndarray, msg="Use np arrays for your results!")

    def test_chirp_linear(self):
        # get the student answer
        observed_lin = createChirpSignal(200, 1, 1, 20, True)
        # test with 1% tolerance and allow both linspace and arange for x-axis
        linspace_case = np.allclose(observed_lin, self.truth_lin_2, RTOL)
        arrange_case = np.allclose(observed_lin, self.truth_lin_2_arrange, RTOL)
        self.assertTrue(linspace_case or arrange_case, msg="Check your linear chirp!")

    def test_chirp_exponential(self):
        # get the student answer
        observed_exp = createChirpSignal(200, 1, 1, 20, False)
        # test with 1% tolerance and allow both linspace and arange for x-axis
        linspace_case = np.allclose(observed_exp, self.truth_exp_2, RTOL)
        arrange_case = np.allclose(observed_exp, self.truth_exp_2_arrange, RTOL)
        self.assertTrue(linspace_case or arrange_case, msg="Check your exponential chirp!")


class TestDecomposition(unittest.TestCase):
    def setUp(self):
        try:
            # load ground truth signals
            self.truth_triangle = np.load('signals/triangle_sig.npy')
            self.truth_triangle_arrange = np.load('signals/triangle_sig_arrange.npy')
            self.truth_square = np.load('signals/square_sig.npy')
            self.truth_square_arrange = np.load('signals/square_sig_arrange.npy')
            self.truth_sawtooth = np.load('signals/sawtooth_sig.npy')
            self.truth_sawtooth_arrange = np.load('signals/sawtooth_sig_arrange.npy')
        except IOError:
            print("Test Setup failed. Missing ground truth files!")
        except ValueError:
            print("Test Setup failed. Ground Truth files are corrupted!")

    def test_triangle(self):
        # get the student answer
        observed_triangle = createTriangleSignal(200, 2, 10000)
        # test with 1% tolerance and allow both linspace and arange for x-axis
        linspace_case = np.allclose(observed_triangle, self.truth_triangle, RTOL)
        arrange_case = np.allclose(observed_triangle, self.truth_triangle_arrange, RTOL)
        self.assertTrue(linspace_case or arrange_case, msg="Check your triangle signal!")

    def test_square(self):
        # get the student answer
        observed_square = createSquareSignal(200, 2, 10000)
        # test with 1% tolerance and allow both linspace and arange for x-axis
        linspace_case = np.allclose(observed_square, self.truth_square, RTOL)
        arrange_case = np.allclose(observed_square, self.truth_square_arrange, RTOL)
        self.assertTrue(linspace_case or arrange_case, msg="Check your square signal!")

    def test_sawtooth(self):
        # get student answer
        observed_sawtooth = createSawtoothSignal(200, 2, 10000, 1)
        # test with 1% tolerance and allow both linspace and arange for x-axis
        linspace_case = np.allclose(observed_sawtooth, self.truth_sawtooth, RTOL)
        arrange_case = np.allclose(observed_sawtooth, self.truth_sawtooth_arrange, RTOL)
        self.assertTrue(linspace_case or arrange_case, msg="Check your sawtooth signal!")


if __name__ == '__main__':
    unittest.main()
