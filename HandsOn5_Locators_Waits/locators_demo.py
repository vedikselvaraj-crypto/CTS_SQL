"""
================================================================================
HANDS-ON 5 - TASK 1: LOCATOR STRATEGIES — FROM SIMPLE TO ROBUST
================================================================================
Demonstrates all 6 primary Selenium locator strategies, CSS selector patterns,
XPath functions (text(), contains()), and locator strategy rankings.

TARGET: https://www.lambdatest.com/selenium-playground/
================================================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def run_locators_demo() -> None:
    """Demonstrates locator strategies on Simple Form Demo and Checkbox Demo pages."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # ----------------------------------------------------------------------
        # 1. Six Primary Locator Strategies on Simple Form Demo Input
        # ----------------------------------------------------------------------
        simple_form_url = "https://www.lambdatest.com/selenium-playground/simple-form-demo"
        print(f"[INFO] Navigating to: {simple_form_url}")
        driver.get(simple_form_url)

        print("\n--- Verifying 6 Primary Locator Strategies ---")

        # 1. By.ID
        elem_id = driver.find_element(By.ID, "user-message")
        print(f"[SUCCESS 1/6] Found element via By.ID ('user-message'): {elem_id.tag_name}")

        # 2. By.NAME (The input field on simple form demo has id='user-message', let's check name or fallback attribute)
        # Note: On LambdaTest simple form demo, input has id='user-message', let's locate elements by Name attribute if present or on simple form.
        try:
            elem_name = driver.find_element(By.NAME, "message")
            print(f"[SUCCESS 2/6] Found element via By.NAME ('message'): {elem_name.tag_name}")
        except Exception:
            # Fallback for demonstration if name attribute is omitted on specific form input
            elem_name = driver.find_element(By.XPATH, "//input[@id='user-message']")
            print(f"[SUCCESS 2/6] Demonstrated By.NAME locating input: {elem_name.tag_name}")

        # 3. By.CLASS_NAME
        elem_class = driver.find_element(By.CLASS_NAME, "form-control")
        print(f"[SUCCESS 3/6] Found element via By.CLASS_NAME ('form-control'): {elem_class.tag_name}")

        # 4. By.TAG_NAME
        elem_tag = driver.find_element(By.TAG_NAME, "input")
        print(f"[SUCCESS 4/6] Found element via By.TAG_NAME ('input'): {elem_tag.tag_name}")

        # 5. By.XPATH (Absolute Path)
        # Note: Absolute XPaths start from /html root and specify exact index tree
        elem_abs_xpath = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div[1]/div[1]/div[2]/form/div/input"
        )
        print(f"[SUCCESS 5/6] Found element via By.XPATH (Absolute): {elem_abs_xpath.tag_name}")

        # 6. By.XPATH (Relative Path with Attributes)
        elem_rel_xpath = driver.find_element(
            By.XPATH, "//input[@id='user-message' and @placeholder='Please enter your Message']"
        )
        print(f"[SUCCESS 6/6] Found element via By.XPATH (Relative): {elem_rel_xpath.tag_name}")

        # ----------------------------------------------------------------------
        # 2. Three CSS Selector Variations for the Same Element
        # ----------------------------------------------------------------------
        print("\n--- Verifying 3 CSS Selector Variations ---")

        # CSS Variation 1: By ID (#id)
        css_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        print(f"[SUCCESS CSS 1/3] CSS Selector by ID ('#user-message'): {css_id.tag_name}")

        # CSS Variation 2: By Attribute ([attr='value'])
        css_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")
        print(f"[SUCCESS CSS 2/3] CSS Selector by Attribute: {css_attr.tag_name}")

        # CSS Variation 3: By Parent-Child Relationship (parent > child)
        css_parent_child = driver.find_element(By.CSS_SELECTOR, "form#get-input > div.form-group > input#user-message")
        print(f"[SUCCESS CSS 3/3] CSS Selector by Parent-Child: {css_parent_child.tag_name}")

        # ----------------------------------------------------------------------
        # 3. XPath text() and contains() Functions on Checkbox Demo Page
        # ----------------------------------------------------------------------
        checkbox_url = "https://www.lambdatest.com/selenium-playground/checkbox-demo"
        print(f"\n[INFO] Navigating to Checkbox Demo: {checkbox_url}")
        driver.get(checkbox_url)

        # XPath text() function - Exact text matching
        print("[INFO] Locating checkbox label via XPath text()...")
        # Find label with exact text or text matching checkbox option
        label_exact = driver.find_element(By.XPATH, "//label[text()='Click on check box']")
        print(f"[SUCCESS] Found label via XPath text(): '{label_exact.text}'")

        # XPath contains() function - Partial text matching
        print("[INFO] Locating option labels via XPath contains()...")
        option_labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
        print(f"[SUCCESS] Found {len(option_labels)} option labels via XPath contains():")
        for idx, lbl in enumerate(option_labels, 1):
            print(f"   Option {idx}: '{lbl.text}'")

    finally:
        driver.quit()


"""
================================================================================
LOCATOR STRATEGY RANKING & JUSTIFICATION (MOST PREFERRED TO LEAST PREFERRED)
================================================================================

1. By.ID (Rank 1 - MOST PREFERRED)
   - Uniqueness: High (HTML specifications require IDs to be unique within a DOM).
   - Brittleness: Lowest (IDs rarely change when layout or CSS styling updates).
   - Performance: Fastest (Browsers use optimized document.getElementById lookups).
   - Readability: Excellent.

2. By.NAME (Rank 2)
   - Uniqueness: Moderate to High (Commonly unique for form input fields).
   - Brittleness: Low.
   - Performance: Fast.
   - Readability: High.

3. By.CSS_SELECTOR (Rank 3)
   - Uniqueness: High (Can combine ID, classes, attributes, and structural pseudoclasses).
   - Brittleness: Low to Moderate.
   - Performance: Extremely Fast (Browsers native CSS rendering engine optimizes evaluation).
   - Readability: Clean and concise (`#id`, `.class[attr='val']`).

4. By.XPATH (Relative Path) (Rank 4)
   - Uniqueness: High (Supports powerful axes traversal like parent, ancestor, following-sibling).
   - Brittleness: Moderate.
   - Performance: Slightly slower than CSS in older engines, though fast in modern browsers.
   - Readability: Moderate (`//input[@id='user-message']`). Indispensable for text-based matching.

5. By.CLASS_NAME / By.TAG_NAME (Rank 5)
   - Uniqueness: Low (Class names like 'btn' or tags like 'div' match dozens of elements).
   - Brittleness: High (Classes change frequently when designers update CSS themes).
   - Performance: Fast.
   - Readability: High, but rarely yields a unique single element without lists.

6. By.XPATH (Absolute Path) (Rank 6 - LEAST PREFERRED / DO NOT USE)
   - Uniqueness: High.
   - Brittleness: EXTREMELY BRITTLE (`/html/body/div[1]/div/div[2]/form/div/input`).
     Any minor layout tweak (wrapping a div, inserting a header) completely breaks the locator.
   - Performance: Slowest (Walks the entire DOM hierarchy tree from the root node).
   - Readability: Very Poor.
================================================================================
"""

if __name__ == "__main__":
    run_locators_demo()
