"""
Test :
run_prog test.
"""
# pylint: disable=duplicate-code,too-few-public-methods

from pyconcurrent import run_prog              # noqa: E402


class TestRunProg:
    """
    Tests ProcRunMp with and without a timeout case.
    """
    def test_run_prog_good(self):
        """
        Run prog that succeeds
        """
        pargs = ['/usr/bin/sleep', '1']
        (ret, _stdout, _stderr) = run_prog(pargs)
        assert ret == 0

    def test_run_prog_fails(self):
        """
        Run prog that does not succeed
        """
        pargs = ['/usr/bin/false']
        (ret, _stdout, _stderr) = run_prog(pargs)
        assert ret != 0
