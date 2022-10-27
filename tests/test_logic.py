'''
This unit tests the mirrorTime function with a couple of samples
'''

import mirrorclock.bi

class TestMirrorTimeLogic:
    testdata = [
        ( (5,25), (6,35) ),
        ( (1,50), (10,10) ),
        ( (11,58), (12,2) ),
        ( (12,1), (11,59) )
    ]

    def test_fixed(self):
        for a,b in self.testdata:
            result = mirrorclock.bi.mirrorTime(a[0], a[1])
            assert b == result
            pass
        pass
    pass
