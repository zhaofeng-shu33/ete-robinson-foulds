import unittest

from ete3 import Tree

from robinson_foulds import robinson_foulds


class TreeCompare(unittest.TestCase):
    def test_tree_compare(self):
        t_1 = Tree('((a,b),c);')
        t_2 = Tree('((a,c),b);')
        result = robinson_foulds(t_1, t_2)
        self.assertAlmostEqual(result['norm_rf'], 1.0)
    def test_non_binary_tree_compare(self):
        t_1 = Tree('((a,b,d),c);')
        t_2 = Tree('(((a,b),d),c);')
        result = robinson_foulds(t_1, t_2)
        self.assertAlmostEqual(result['norm_rf'], 1/3.0)

if __name__ == '__main__':
    unittest.main()