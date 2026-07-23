# Selenium Basics & QA Automation Architectural Index

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Repository**: `SeleniumBasics/`  

---

## 🗺️ Master Deliverables Index

| Hands-On Module | Primary Artifact / Files | Description & Core Focus |
| :--- | :--- | :--- |
| **Hands-On 1: QA Concepts** | [qa_concepts.md](file:///c:/Users/Admin/Desktop/selenium/HandsOn1_QA_Concepts/qa_concepts.md) | QA fundamentals, testing levels (Unit, Integration, System, UAT), functional vs non-functional classification, formal test cases table, complete defect lifecycle, defect severity/priority matrix, and defect report. |
| **Hands-On 2: SDLC vs TDLC** | [v_model_analysis.md](file:///c:/Users/Admin/Desktop/selenium/HandsOn2_SDLC_TDLC/v_model_analysis.md) | V-Model ASCII mapping, entry/exit criteria per testing level, early QA touchpoints, Agile ceremony roles, 4 Shift-Left practices, and Gherkin acceptance criteria. |
| **Hands-On 3: Automation Strategy** | [automation_strategy.md](file:///c:/Users/Admin/Desktop/selenium/HandsOn3_Automation_Strategy/automation_strategy.md) | 5 automation criteria, 6 test case selection decisions, mathematical ROI calculation, flaky test prevention, comparison of 5 framework types, and hybrid framework folder structure. |
| **Hands-On 4: Selenium Setup** | [setup_test.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn4_Selenium_Setup/setup_test.py)<br>[navigation_windows.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn4_Selenium_Setup/navigation_windows.py) | Selenium architecture breakdown, `webdriver-manager` setup, headless Chrome, implicit wait rationale, browser navigation history, multi-tab switching, screenshots, and window resizing. |
| **Hands-On 5: Locators & Waits** | [locators_demo.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn5_Locators_Waits/locators_demo.py)<br>[explicit_waits.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn5_Locators_Waits/explicit_waits.py)<br>[fluent_wait.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn5_Locators_Waits/fluent_wait.py) | 6 locator strategies, CSS selector patterns, XPath `text()`/`contains()`, strategy rankings, explicit wait benchmarks vs `time.sleep()`, and custom FluentWait. |
| **Hands-On 6: PyTest Framework** | [conftest.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn6_PyTest_Framework/conftest.py)<br>[test_playground.py](file:///c:/Users/Admin/Desktop/selenium/HandsOn6_PyTest_Framework/test_playground.py) | Function-scoped driver fixtures, session-scoped base URL, failure screenshot hook, HTML report generation, and parameterised PyTest test suite. |
| **Hands-On 7: Page Object Model** | [Page Object Framework](file:///c:/Users/Admin/Desktop/selenium/HandsOn7_PageObjectModel/)<br>[POM README.md](file:///c:/Users/Admin/Desktop/selenium/HandsOn7_PageObjectModel/README.md) | Industry-standard Page Object Model (POM) suite. BasePage superclass, page object classes (`SimpleFormPage`, `CheckboxPage`, `DropdownPage`, `InputFormPage`), zero `driver.find_element` test files, and maintenance analysis. |

---

## 🛠️ Environment Prerequisites

- **Python**: 3.12 (or 3.10+)
- **Browser**: Google Chrome (latest)
- **Driver Management**: Automated via `webdriver-manager`

### Quick Run Commands
```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Run All PyTest Suites with HTML Report
pytest -v --html=report.html --self-contained-html
```
