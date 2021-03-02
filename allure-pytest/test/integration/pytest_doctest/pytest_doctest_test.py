import allure
from hamcrest import assert_that
from allure_commons_test.report import has_test_case
from allure_commons_test.result import with_status


@allure.feature("Integration")
def test_pytest_flakes(allured_testdir):
    allured_testdir.testdir.makepyfile("""
        def some_func():
            \"\"\"
            >>> some_func()
            \"\"\"
            return True

    """)

    allured_testdir.run_with_allure("--doctest-modules")

    assert_that(allured_testdir.allure_report,
                has_test_case("some_func",
                              with_status("passed"))
                )
