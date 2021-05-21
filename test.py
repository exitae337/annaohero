from annaohero import compress

import os
import unittest



class TestMainCode(unittest.TestCase):
    
    def test_compress(self):
        res = []
        compress('files')
        os.chdir('..')
        for ad, dirs, fil in os.walk('files'):
            for f in fil:
                res.append(f)
        if 'sop.nosh' in res:
            sh = True
        else:
            sh = False
        self.assertEqual(sh, True)
        os.chdir('files')
        os.remove('sop.nosh')

if __name__ == '__main__':
    unittest.main()
