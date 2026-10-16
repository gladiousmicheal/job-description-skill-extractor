from job_analyzer import extract_skills


def test_python_and_sql():
    result = extract_skills("Looking for Python and SQL skills")
    assert "Python" in result
    assert "SQL" in result


def test_excel_and_power_bi():
    result = extract_skills("Must know Excel and Power BI")
    assert "Excel" in result
    assert "Power BI" in result


def test_unsupported_skill():
    result = extract_skills("Looking for a Java developer")
    assert "Java" not in result


def test_case_insensitive():
    result = extract_skills("python and SQL")
    assert "Python" in result
    assert "SQL" in result