import unittest

from .basis_functions import *


class BasisFunctionsTests(unittest.TestCase):

    def test_list_of_floats(self):
        nodes = [1.0, 3.0, 2.0]
        theta_t = piecewise_constant(nodes)
        self.assertEqual(theta_t(0.0), 1.0)
        self.assertEqual(theta_t(0.5), 3.0)
        self.assertEqual(theta_t(1.000001), 2.0)

    def test_point_project_floats(self):
        ts = list(jnp.linspace(0, 1, 11))
        points = [jnp.sin(3 * t) for t in ts]
        n = 13
        nodes = point_project(points, ts, n, piecewise_constant)
        self.assertEqual(len(nodes), n)

    def test_point_project_tree_floats(self):
        ts = list(jnp.linspace(0, 1, 11))
        points = [jnp.sin(3 * t) for t in ts]
        n = 13
        nodes = point_project_tree(points, ts, n, piecewise_constant)
        self.assertEqual(len(nodes), n)

    def test_point_project_tree_list(self):
        ts = list(jnp.linspace(0, 1, 11))
        points = [ [1.0+t, 2.0+t] for t in ts]
        n = 13
        nodes = point_project_tree(points, ts, n, piecewise_constant)
        self.assertEqual(len(nodes), n)
        for val in nodes:
            self.assertEqual(len(val), len(points[0]))

    def test_point_project_tree_dict(self):
        ts = list(jnp.linspace(0, 1, 11))
        points = [ {'a': 1.0+t, 'b': 2.0+t} for t in ts]
        n = 13
        nodes = point_project_tree(points, ts, n, piecewise_constant)
        self.assertEqual(len(nodes), n)
        for val in nodes:
            self.assertEqual(jax.tree_structure(val), jax.tree_structure(points[0]))


if __name__ == "__main__":
    unittest.main()
