from rez.packages import iter_package_families, iter_packages
from rez.tests.util import TestBase
from rez.vendor.version.version import VersionRange
import rez.vendor.unittest2 as unittest
import os.path


ALL_PACKAGES = set([
    # solver packages
    'bahish-1', 'bahish-2',
    'nada',
    'nopy-2.1',
    'pybah-4', 'pybah-5',
    'pydad-1', 'pydad-2', 'pydad-3',
    'pyfoo-3.0.0', 'pyfoo-3.1.0',
    'pymum-1', 'pymum-2', 'pymum-3',
    'pyodd-1', 'pyodd-2',
    'pyson-1', 'pyson-2',
    'pysplit-5', 'pysplit-6', 'pysplit-7',
    'python-2.5.2', 'python-2.6.0', 'python-2.6.8', 'python-2.7.0',
    # resources packages
    'unversioned',
    'versioned-1.0', 'versioned-2.0',
    'single_unversioned',
    'single_versioned-3.5',
    'multi-1.0', 'multi-1.1', 'multi-1.2','bah-2.0.0',
    'multi_packages_variant_sorted', 'asymmetric_variants', 'bar-4.5.3',
    'permuted_family_names_same_position_weight', 'eek-1.0.1', 'bar-4.8.5',
    'multi_packages_variant_unsorted', 'package_name_in_require_and_variant',
    'multi_version_variant_lower_to_higher_version_order', 'bar-4.8.2',
    'variable_variant_package_in_single_column', 'three_packages_in_variant',
    'multi_version_variant_higher_to_lower_version_order', 'eek-2.0.0',
    'two_packages_in_variant_unsorted', 'variant_with_weak_package_in_variant',
    'foo-1.1.0', 'eek-1.0.0', 'bah-1.0.0', 'bah-1.0.1', 'foo-1.0.0',
    'permuted_family_names', 'variant_with_antipackage'])


ALL_FAMILIES = set(x.split('-')[0] for x in ALL_PACKAGES)


def _to_names(it):
    return set(p.name for p in it)


def _to_qnames(it):
    return set(p.qualified_name for p in it)


class TestPackages(TestBase):
    @classmethod
    def setUpClass(cls):
        path = os.path.dirname(__file__)
        solver_packages_path = os.path.join(
            path, "data", "solver", "packages")
        resource_packages_path = os.path.join(
            path, "data", "resources", "packages")

        cls.settings = dict(
            packages_path=[solver_packages_path,
                           resource_packages_path])

    def test_1(self):
        """package family iteration."""
        all_fams = _to_names(iter_package_families())
        self.assertEqual(all_fams, ALL_FAMILIES)

    def test_2(self):
        """package iteration."""
        all_packages = _to_qnames(iter_packages())
        self.assertEqual(all_packages, ALL_PACKAGES)

        res = _to_qnames(iter_packages(name='nada'))
        self.assertEqual(res, set(['nada']))

        res = _to_qnames(iter_packages(name='python'))
        self.assertEqual(res, set(['python-2.5.2', 'python-2.6.0',
                                   'python-2.6.8', 'python-2.7.0']))

        res = _to_qnames(iter_packages(name='pydad', range=VersionRange("<3")))
        self.assertEqual(res, set(['pydad-1', 'pydad-2']))


def get_test_suites():
    suites = []
    suite = unittest.TestSuite()
    suite.addTest(TestPackages("test_1"))
    suite.addTest(TestPackages("test_2"))
    suites.append(suite)
    return suites


if __name__ == '__main__':
    unittest.main()
