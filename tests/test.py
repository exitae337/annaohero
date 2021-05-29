import os, sys
import unittest

sys.path.append(os.path.join(os.path.abspath(os.curdir), 'annaohero'))
from annaohero import compress, uncompress

class TestMainCode(unittest.TestCase):
    
    def test_compress(self):
        arr1 = []
        os.chdir('tests')
        compress('files')
        os.chdir('..')
        for ad, dirs, fil in os.walk('files'):
            for f in fil:
                arr1.append(f)
        if 'sop.nosh' in arr1:
            sh = True
        else:
            sh = False
        self.assertEqual(sh, True)
        os.chdir('files')
        os.remove('sop.nosh')

    def test_uncompress(self):
        arr2 = []
        os.chdir('..')
        uncompress('uncompress')
        os.chdir('..')
        for ad, dirs, fil in os.walk('uncompress'):
            for f in fil:
                arr2.append(f)
        print(arr2)
        if len(arr2) == 4:
            ph = True
        else:
            ph = False
        self.assertEqual(ph, True)
        


if __name__ == '__main__':
    unittest.main()
