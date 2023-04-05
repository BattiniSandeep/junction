"""Automation using nox.
"""
import nox

@nox.session(python=["3.9"])
def test(session):
    session.install("-r", "requirements.txt")
    session.install("coverage")
    session.run("coverage", "run", "--source=.", "manage.py", "test")
    session.run("coverage", "report", "-m")

    # Check coverage and fail if coverage is less than 80%
    coverage_output = session.run("coverage", "report")
    coverage_percentage = coverage_output.splitlines()[-1].split()[3]
    if float(coverage_percentage) < 80:
        session.error(f"Coverage {coverage_percentage}% is less than 80%")

@nox.session
def lint(session):
    session.install("-r", "requirements.txt")
    session.run("flake8", "--max-line-length=88", ".")
    session.run("black", "--check", ".")
    session.run("isort", "--check-only", ".")



# import nox

# nox.options.sessions = ["dev"]
# nox.options.reuse_existing_virtualenvs = True
# nox.options.error_on_external_run = True

# @nox.session(python=["3.10"])
# def install_deps(session):
#     session.install("-r", "requirements.txt")


# @nox.session(python="3")
# def dev(session):
#     session.install("-r", "requirements.txt")
#     session.run("python", "manage.py", *session.posargs)


# @nox.session(python=["2.7", "3.5", "3.6", "3.7", "3.8"])
# def test(session):
#     session.install("-r", "requirements.txt")
#     session.install("-r", "tools/requirements-test.txt")

#     session.run("pytest", "--cov", "-v", "--tb=native")
#     session.run("coverage", "report", "-m")


# @nox.session(python=["3.5", "3.6", "3.7", "3.8"])
# def lint(session):
#     session.install("pre-commit")
#     session.run("pre-commit", "run", "--all-files")


# @nox.session(python=["3.10"])
# def test_coverage(session):
#     # Install dependencies
#     session.install("-r", "requirements.txt")
#     session.install("-r", "tools/requirements-test.txt")
#     session.run("pytest", "--cov", "-v", "--tb=native")
#     session.run("coverage", "report", "-m")

#     # Run tests with coverage
#     session.run("coverage", "run", "--source", "myapp", "./manage.py", "test")

#     # Generate coverage report
#     session.run("coverage", "report", "--fail-under=80")


# @nox.session(python="3.5")
# def docs(session):
#     session.install("-r", "tools/requirements-docs.txt")

#     def get_sphinx_build_command(kind):
#         return [
#             "sphinx-build",
#             "-W",
#             "-d",
#             "docs/build/_doctrees/" + kind,
#             "-b",
#             kind,
#             "docs/source",
#             "docs/build/" + kind,
#         ]

#     session.run(*get_sphinx_build_command("html"))
