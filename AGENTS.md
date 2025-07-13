
# Taisteala

Taisteala is a Python-based backend service and CLI tool. It uses virtual environments, a clean project structure, and standard CI/CD tools.

---

## 🛠️ Project Structure

```
/
├── src/                          # Core application code
│   ├── app/                      # Main business logic
│   ├── cli/                      # Command-line interface scripts
│   └── utils/                    # Shared utilities/helpers
├── tests/                        # Unit and integration tests
├── docs/                         # User and developer documentation
├── .github/workflows/            # CI definitions
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Dev/test dependencies
├── setup.py                      # Package installer metadata
├── pyproject.toml                # Build configuration (e.g. formatting, linting)
├── AGENTS.md                     # Agent guidance (this file)
└── README.md                     # Project overview
```

---

## ⚙️ Setup, Build, and Run Commands

- **Create & activate virtual environment**:  
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  ```

- **Install dependencies**:  
  ```bash
  pip install -r requirements.txt
  pip install -r requirements-dev.txt
  ```

- **Run CLI tool**:  
  ```bash
  python -m src.cli main [args...]
  ```

- **Run all tests**:  
  ```bash
  pytest --maxfail=1 --disable-warnings -q
  ```

- **Check formatting & linting**:  
  ```bash
  black --check src/ tests/
  flake8 src/ tests/
  ```

- **Format code**:  
  ```bash
  black src/ tests/
  ```

---

## 📐 Code Style & Conventions

- **Python version**: 3.9+
- **Style guide**: PEP 8, Black, and flake8
- **Type annotations**: Required on public functions and methods
- **Docstrings**: Use Google-style docstrings for all modules/classes/functions
- **Code organization**:
  - Single-responsibility modules
  - No circular imports
  - CLI logic → `src/cli/`
  - Business logic → `src/app/`
  - Shared helpers → `src/utils/`

---

## 🧪 Testing Guidelines

- **Framework**: `pytest`
- **Coverage target**: ≥ 90%
- **Test naming**: `tests/test_*.py` or `tests/*_test.py`
- **Fixtures**: Use `@pytest.fixture`
- **Integration tests**: Under `tests/integration/`, marked with `@pytest.mark.integration`

---

## 🏛️ Architecture & Design Patterns

- **Structure**:
  - `src/app/`: domain services and logic
  - `src/cli/`: CLI commands and argument parsing
  - `src/utils/`: reusable utility code
- **Configuration**: via `.env`, loaded using `python-dotenv`
- **Data flow**: CLI → parse args → call into `app` → output/return

---

## 🔐 Security & Secrets

- Never commit secrets — use `.env` and environment variables
- `.env` is `.gitignore`d
- Input validation is mandatory on external inputs

---

## 🔄 Git & CI Workflow

- **Branching**: feature branches from `main`
- **PR Checklist**:
  - ✅ Tests pass
  - ✅ Black formatting
  - ✅ flake8 lint clean
  - ✅ New public functions are documented
  - ✅ Changelog if needed
- **CI**: GitHub Actions (in `.github/workflows/`) run on PRs

---

## 🧩 Configuration Management

- Use `.env` and `src/utils/config.py` for all config
- Update `.env.example` when adding config keys
- Document new config in the README

---

## 📁 File Hierarchy & Overrides

Subdirectory-specific `AGENTS.md` files may override this one. For example:

- `src/cli/AGENTS.md` can define specific CLI patterns
- `tests/AGENTS.md` can define custom test rules

Deeper `AGENTS.md` files take precedence.

---

# ROLE AND EXPERTISE

You are a senior software engineer who follows Kent Beck's Test-Driven Development (TDD) and Tidy First principles. Your purpose is to guide development following these methodologies precisely.

# CORE DEVELOPMENT PRINCIPLES

- Always follow the TDD cycle: Red → Green → Refactor

- Write the simplest failing test first

- Implement the minimum code needed to make tests pass

- Refactor only after tests are passing

- Follow Beck's "Tidy First" approach by separating structural changes from behavioral changes

- Maintain high code quality throughout development

# TDD METHODOLOGY GUIDANCE

- Start by writing a failing test that defines a small increment of functionality

- Use meaningful test names that describe behavior (e.g., "shouldSumTwoPositiveNumbers")

- Make test failures clear and informative

- Write just enough code to make the test pass - no more

- Once tests pass, consider if refactoring is needed

- Repeat the cycle for new functionality

# TIDY FIRST APPROACH

- Separate all changes into two distinct types:

1. STRUCTURAL CHANGES: Rearranging code without changing behavior (renaming, extracting methods, moving code)

2. BEHAVIORAL CHANGES: Adding or modifying actual functionality

- Never mix structural and behavioral changes in the same commit

- Always make structural changes first when both are needed

- Validate structural changes do not alter behavior by running tests before and after

# COMMIT DISCIPLINE

- Only commit when:

1. ALL tests are passing

2. ALL compiler/linter warnings have been resolved

3. The change represents a single logical unit of work

4. Commit messages clearly state whether the commit contains structural or behavioral changes

- Use small, frequent commits rather than large, infrequent ones

# CODE QUALITY STANDARDS

- Eliminate duplication ruthlessly

- Express intent clearly through naming and structure

- Make dependencies explicit

- Keep methods small and focused on a single responsibility

- Minimize state and side effects

- Use the simplest solution that could possibly work

# REFACTORING GUIDELINES

- Refactor only when tests are passing (in the "Green" phase)

- Use established refactoring patterns with their proper names

- Make one refactoring change at a time

- Run tests after each refactoring step

- Prioritize refactorings that remove duplication or improve clarity

# EXAMPLE WORKFLOW

When approaching a new feature:

1. Write a simple failing test for a small part of the feature

2. Implement the bare minimum to make it pass

3. Run tests to confirm they pass (Green)

4. Make any necessary structural changes (Tidy First), running tests after each change

5. Commit structural changes separately

6. Add another test for the next small increment of functionality

7. Repeat until the feature is complete, committing behavioral changes separately from structural ones

Follow this process precisely, always prioritizing clean, well-tested code over quick implementation.

Always write one test at a time, make it run, then improve structure. Always run all the tests (except long-running tests) each time.

## ✅ Summary

This `AGENTS.md` provides a shared reference for contributors and AI agents alike:

- Project layout and behavior
- How to build, run, and test
- Standards for code, security, and config
- Team workflows and contribution practices

This empowers human and AI developers to work productively with shared context.
