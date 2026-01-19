# Pytest Configuration Issues - "test" Naming

## Summary
The codebase uses "test" in multiple contexts that could potentially conflict:

| Location | Problem | Status | Solution |
|----------|---------|--------|----------|
| `Robot/libs/test_api.py` | File starts with `test_` | ✅ FIXED | Renamed `Test_Api` → `MeasurementTestApi` + added `norecursedirs` |
| `Code/test_runner.py` | Contains `TestRunner` class | ⚠️ OK | Not a pytest test, in `Code/` not `tests/` |
| `Code/test_worker.py` | Contains `TestWorker` class | ⚠️ OK | Not a pytest test, in `Code/` not `tests/` |
| `tests/test_imports.py` | Properly named test file | ✅ OK | Correct naming convention |

## What Was Changed

### 1. Renamed Class (test_api.py)
**Before:**
```python
class Test_Api:
    """API for Robot Framework"""
```

**After:**
```python
class MeasurementTestApi:
    """API for Robot Framework test execution - NOT a pytest test class."""
```

**Why:** 
- Pytest looks for classes starting with `Test` as potential test classes
- Pytest was potentially trying to instantiate and run methods on `Test_Api`
- The class is NOT a pytest test class, it's a Robot Framework API wrapper
- Renaming prevents pytest from falsely detecting it as a test

### 2. Updated pytest.ini
**Added:**
```ini
norecursedirs = Robot venv .venv __pycache__ .git build dist
```

**Why:**
- Explicitly tells pytest to ignore Robot Framework directory
- Prevents scanning Robot/libs/ for test files
- Improves test discovery performance

### 3. Updated pyproject.toml
**Added same exclusions to tool.pytest.ini_options**

## How Pytest Discovers Tests

Pytest uses these patterns:
1. **Files:** `test_*.py` or `*_test.py` in `testpaths`
2. **Classes:** `Test*` (case-sensitive) 
3. **Functions:** `test_*` (must be functions, not methods of non-test classes)

## Important Notes

- ✅ `TestRunner` and `TestWorker` are safe (not in `tests/` directory)
- ✅ `test_imports.py` functions are correctly named
- ✅ Robot Framework tests use `.robot` files, not picked up by pytest
- ⚠️ Be careful adding new classes starting with `Test` outside `tests/` directory

## Testing Locally

```bash
# Verify pytest finds only correct tests
pytest --collect-only

# Should show only tests/test_imports.py functions
# Should NOT show Robot/libs/test_api.py classes

# Run tests
pytest tests/ -v
```

## CI/CD Integration

The GitHub Actions workflow already uses:
```yaml
- name: Run pytest tests
  run: |
    pytest tests/ -v --tb=short 2>&1 || echo "Pytest complete"
```

This explicitly scans only `tests/` directory, so it's not affected by the Robot Framework files.
