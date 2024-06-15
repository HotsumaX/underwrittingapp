# Progress Report

## ./package.json
## ./package-lock.json
## ./evaluate_repo.py
### flake8 Report:
./evaluate_repo.py:5:80: E501 line too long (80 > 79 characters)
./evaluate_repo.py:7:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:10:80: E501 line too long (96 > 79 characters)
./evaluate_repo.py:15:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:20:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:21:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:22:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:34:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:35:80: E501 line too long (82 > 79 characters)
./evaluate_repo.py:50:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:63:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:70:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:75:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:80:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:82:80: E501 line too long (149 > 79 characters)
./evaluate_repo.py:98:80: E501 line too long (112 > 79 characters)
./evaluate_repo.py:100:80: E501 line too long (127 > 79 characters)
./evaluate_repo.py:102:80: E501 line too long (117 > 79 characters)
./evaluate_repo.py:105:80: E501 line too long (124 > 79 characters)
./evaluate_repo.py:107:80: E501 line too long (91 > 79 characters)
./evaluate_repo.py:109:80: E501 line too long (89 > 79 characters)
./evaluate_repo.py:111:80: E501 line too long (83 > 79 characters)
./evaluate_repo.py:112:1: W293 blank line contains whitespace
./evaluate_repo.py:114:80: E501 line too long (84 > 79 characters)
./evaluate_repo.py:115:80: E501 line too long (92 > 79 characters)
./evaluate_repo.py:117:1: W293 blank line contains whitespace
./evaluate_repo.py:120:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:142:5: F841 local variable 'updated_outline' is assigned to but never used
./evaluate_repo.py:153:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:154:11: W292 no newline at end of file

### pylint Report:
************* Module evaluate_repo
evaluate_repo.py:82:0: C0301: Line too long (149/100) (line-too-long)
evaluate_repo.py:98:0: C0301: Line too long (112/100) (line-too-long)
evaluate_repo.py:100:0: C0301: Line too long (127/100) (line-too-long)
evaluate_repo.py:102:0: C0301: Line too long (117/100) (line-too-long)
evaluate_repo.py:105:0: C0301: Line too long (124/100) (line-too-long)
evaluate_repo.py:112:0: C0303: Trailing whitespace (trailing-whitespace)
evaluate_repo.py:117:0: C0303: Trailing whitespace (trailing-whitespace)
evaluate_repo.py:154:0: C0304: Final newline missing (missing-final-newline)
evaluate_repo.py:1:0: C0114: Missing module docstring (missing-module-docstring)
evaluate_repo.py:142:4: W0612: Unused variable 'updated_outline' (unused-variable)

-----------------------------------
Your code has been rated at 9.08/10


### bandit Report:
Run started:2024-06-15 15:47:14.885395

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././evaluate_repo.py:2:0
1	import os
2	import subprocess
3	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ././evaluate_repo.py:10:17
9	    try:
10	        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
11	        return result.stdout if result.stdout else result.stderr

--------------------------------------------------

Code scanned:
	Total lines of code: 118
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 1
		Medium: 0
		High: 1
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 2
Files skipped (0):


## ./vercel.json
## ./.vscode/settings.json
## ./frontend/package.json
## ./frontend/package-lock.json
## ./frontend/public/index.html
## ./frontend/src/App.js
## ./frontend/src/store.js
## ./frontend/src/index.css
## ./frontend/src/vercel.json
## ./frontend/src/index.js
## ./frontend/src/components/DataDisplay.js
## ./frontend/src/components/HealthCheck.js
## ./frontend/src/components/CrexiScraper.js
## ./frontend/src/components/Logs.js
## ./frontend/src/components/ServerStatus.js
## ./frontend/src/components/ZillowScraper.js
## ./backend/site_scraper.py
### flake8 Report:
./backend/site_scraper.py:3:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module site_scraper
backend/site_scraper.py:3:4: E0001: Parsing failed: 'unexpected indent (site_scraper, line 3)' (syntax-error)

### bandit Report:
Run started:2024-06-15 15:47:15.514107

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 18
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	././backend/site_scraper.py (syntax error while parsing AST from file)


## ./backend/log_section.py
### flake8 Report:
./backend/log_section.py:8:1: W391 blank line at end of file

### pylint Report:
************* Module log_section
backend/log_section.py:8:0: C0305: Trailing newlines (trailing-newlines)
backend/log_section.py:5:0: W0105: String statement has no effect (pointless-string-statement)

-----------------------------------
Your code has been rated at 0.00/10


### bandit Report:
Run started:2024-06-15 15:47:16.150872

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 6
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/page_content.html
## ./backend/property_evaluation.py
### flake8 Report:
./backend/property_evaluation.py:3:1: E302 expected 2 blank lines, found 1
./backend/property_evaluation.py:32:80: E501 line too long (142 > 79 characters)
./backend/property_evaluation.py:44:80: E501 line too long (126 > 79 characters)
./backend/property_evaluation.py:46:80: E501 line too long (92 > 79 characters)
./backend/property_evaluation.py:50:80: E501 line too long (175 > 79 characters)
./backend/property_evaluation.py:51:80: E501 line too long (139 > 79 characters)
./backend/property_evaluation.py:52:80: E501 line too long (166 > 79 characters)
./backend/property_evaluation.py:53:80: E501 line too long (164 > 79 characters)
./backend/property_evaluation.py:57:80: E501 line too long (139 > 79 characters)
./backend/property_evaluation.py:58:80: E501 line too long (149 > 79 characters)
./backend/property_evaluation.py:59:80: E501 line too long (152 > 79 characters)
./backend/property_evaluation.py:63:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/property_evaluation.py:70:38: W292 no newline at end of file

### pylint Report:
************* Module property_evaluation
backend/property_evaluation.py:32:0: C0301: Line too long (142/100) (line-too-long)
backend/property_evaluation.py:44:0: C0301: Line too long (126/100) (line-too-long)
backend/property_evaluation.py:50:0: C0301: Line too long (175/100) (line-too-long)
backend/property_evaluation.py:51:0: C0301: Line too long (139/100) (line-too-long)
backend/property_evaluation.py:52:0: C0301: Line too long (166/100) (line-too-long)
backend/property_evaluation.py:53:0: C0301: Line too long (164/100) (line-too-long)
backend/property_evaluation.py:57:0: C0301: Line too long (139/100) (line-too-long)
backend/property_evaluation.py:58:0: C0301: Line too long (149/100) (line-too-long)
backend/property_evaluation.py:59:0: C0301: Line too long (152/100) (line-too-long)
backend/property_evaluation.py:70:0: C0304: Final newline missing (missing-final-newline)
backend/property_evaluation.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/property_evaluation.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/property_evaluation.py:3:22: W0621: Redefining name 'property_data' from outer scope (line 65) (redefined-outer-name)
backend/property_evaluation.py:4:4: W0621: Redefining name 'report' from outer scope (line 66) (redefined-outer-name)
backend/property_evaluation.py:64:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
backend/property_evaluation.py:69:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

-----------------------------------
Your code has been rated at 6.73/10


### bandit Report:
Run started:2024-06-15 15:47:16.945913

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 51
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/email_contact.py
### flake8 Report:
./backend/email_contact.py:8:1: W391 blank line at end of file

### pylint Report:
************* Module email_contact
backend/email_contact.py:8:0: C0305: Trailing newlines (trailing-newlines)
backend/email_contact.py:5:0: W0105: String statement has no effect (pointless-string-statement)

-----------------------------------
Your code has been rated at 0.00/10


### bandit Report:
Run started:2024-06-15 15:47:17.578026

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 6
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/single_family_evaluation.py
### flake8 Report:
./backend/single_family_evaluation.py:4:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module single_family_evaluation
backend/single_family_evaluation.py:4:4: E0001: Parsing failed: 'unexpected indent (single_family_evaluation, line 4)' (syntax-error)

### bandit Report:
Run started:2024-06-15 15:47:18.211766

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 11
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	././backend/single_family_evaluation.py (syntax error while parsing AST from file)


## ./backend/properties.json
## ./backend/scrape_crexi.py
### flake8 Report:
./backend/scrape_crexi.py:4:1: E302 expected 2 blank lines, found 1
./backend/scrape_crexi.py:9:1: W293 blank line contains whitespace
./backend/scrape_crexi.py:13:1: W293 blank line contains whitespace
./backend/scrape_crexi.py:16:1: W293 blank line contains whitespace
./backend/scrape_crexi.py:22:80: E501 line too long (88 > 79 characters)
./backend/scrape_crexi.py:25:1: W293 blank line contains whitespace
./backend/scrape_crexi.py:34:19: F541 f-string is missing placeholders
./backend/scrape_crexi.py:35:1: W293 blank line contains whitespace
./backend/scrape_crexi.py:38:1: W293 blank line contains whitespace
./backend/scrape_crexi.py:42:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/scrape_crexi.py:43:80: E501 line too long (97 > 79 characters)
./backend/scrape_crexi.py:43:98: W292 no newline at end of file

### pylint Report:
************* Module scrape_crexi
backend/scrape_crexi.py:9:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi.py:13:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi.py:16:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi.py:43:0: C0304: Final newline missing (missing-final-newline)
backend/scrape_crexi.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/scrape_crexi.py:2:0: E0401: Unable to import 'playwright.sync_api' (import-error)
backend/scrape_crexi.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_crexi.py:36:15: W0718: Catching too general exception Exception (broad-exception-caught)
backend/scrape_crexi.py:23:23: W0718: Catching too general exception Exception (broad-exception-caught)
backend/scrape_crexi.py:31:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
backend/scrape_crexi.py:34:18: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)

-----------------------------------
Your code has been rated at 3.08/10


### bandit Report:
Run started:2024-06-15 15:47:18.940440

Test results:
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b110_try_except_pass.html
   Location: ././backend/scrape_crexi.py:23:16
22	                    element_texts[element.get_attribute('class')] = element.inner_text()
23	                except Exception:
24	                    pass
25	            

--------------------------------------------------

Code scanned:
	Total lines of code: 30
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 1
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 1
Files skipped (0):


## ./backend/scrape_crexi_with_selenium.py
### flake8 Report:
./backend/scrape_crexi_with_selenium.py:12:80: E501 line too long (118 > 79 characters)
./backend/scrape_crexi_with_selenium.py:25:1: E302 expected 2 blank lines, found 1
./backend/scrape_crexi_with_selenium.py:29:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:32:80: E501 line too long (106 > 79 characters)
./backend/scrape_crexi_with_selenium.py:34:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:37:80: E501 line too long (80 > 79 characters)
./backend/scrape_crexi_with_selenium.py:41:80: E501 line too long (84 > 79 characters)
./backend/scrape_crexi_with_selenium.py:43:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:45:80: E501 line too long (81 > 79 characters)
./backend/scrape_crexi_with_selenium.py:47:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:50:80: E501 line too long (89 > 79 characters)
./backend/scrape_crexi_with_selenium.py:51:80: E501 line too long (93 > 79 characters)
./backend/scrape_crexi_with_selenium.py:52:80: E501 line too long (89 > 79 characters)
./backend/scrape_crexi_with_selenium.py:58:80: E501 line too long (83 > 79 characters)
./backend/scrape_crexi_with_selenium.py:60:80: E501 line too long (80 > 79 characters)
./backend/scrape_crexi_with_selenium.py:61:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:62:80: E501 line too long (83 > 79 characters)
./backend/scrape_crexi_with_selenium.py:66:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:70:1: W293 blank line contains whitespace
./backend/scrape_crexi_with_selenium.py:71:80: E501 line too long (102 > 79 characters)
./backend/scrape_crexi_with_selenium.py:79:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/scrape_crexi_with_selenium.py:80:19: W292 no newline at end of file

### pylint Report:
************* Module scrape_crexi_with_selenium
backend/scrape_crexi_with_selenium.py:12:0: C0301: Line too long (118/100) (line-too-long)
backend/scrape_crexi_with_selenium.py:29:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:32:0: C0301: Line too long (106/100) (line-too-long)
backend/scrape_crexi_with_selenium.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:61:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:66:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:70:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_crexi_with_selenium.py:71:0: C0301: Line too long (102/100) (line-too-long)
backend/scrape_crexi_with_selenium.py:80:0: C0304: Final newline missing (missing-final-newline)
backend/scrape_crexi_with_selenium.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/scrape_crexi_with_selenium.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_crexi_with_selenium.py:73:11: W0718: Catching too general exception Exception (broad-exception-caught)
backend/scrape_crexi_with_selenium.py:46:12: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_crexi_with_selenium.py:59:23: W0718: Catching too general exception Exception (broad-exception-caught)
backend/scrape_crexi_with_selenium.py:58:20: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_crexi_with_selenium.py:60:20: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_crexi_with_selenium.py:68:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
backend/scrape_crexi_with_selenium.py:71:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_crexi_with_selenium.py:74:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_crexi_with_selenium.py:7:0: C0411: standard import "json" should be placed before third party imports "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "selenium.webdriver.common.by.By", "selenium.webdriver.support.ui.WebDriverWait", "selenium.webdriver.support.expected_conditions", "webdriver_manager.chrome.ChromeDriverManager" (wrong-import-order)
backend/scrape_crexi_with_selenium.py:8:0: C0411: standard import "logging" should be placed before third party imports "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "selenium.webdriver.common.by.By", "selenium.webdriver.support.ui.WebDriverWait", "selenium.webdriver.support.expected_conditions", "webdriver_manager.chrome.ChromeDriverManager" (wrong-import-order)
backend/scrape_crexi_with_selenium.py:9:0: C0411: standard import "time" should be placed before third party imports "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "selenium.webdriver.common.by.By", "selenium.webdriver.support.ui.WebDriverWait", "selenium.webdriver.support.expected_conditions", "webdriver_manager.chrome.ChromeDriverManager" (wrong-import-order)

-----------------------------------
Your code has been rated at 5.38/10


### bandit Report:
Run started:2024-06-15 15:47:20.777983

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 57
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/multi_family_evaluation.py
### flake8 Report:
./backend/multi_family_evaluation.py:4:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module multi_family_evaluation
backend/multi_family_evaluation.py:4:4: E0001: Parsing failed: 'unexpected indent (multi_family_evaluation, line 4)' (syntax-error)

### bandit Report:
Run started:2024-06-15 15:47:21.408269

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 11
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	././backend/multi_family_evaluation.py (syntax error while parsing AST from file)


## ./backend/scrape_zillow.py
### flake8 Report:
./backend/scrape_zillow.py:21:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_zillow
backend/scrape_zillow.py:21:4: E0001: Parsing failed: 'unexpected indent (scrape_zillow, line 21)' (syntax-error)

### bandit Report:
Run started:2024-06-15 15:47:22.037595

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 33
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	././backend/scrape_zillow.py (syntax error while parsing AST from file)


## ./backend/app.py
### flake8 Report:
./backend/app.py:5:1: E302 expected 2 blank lines, found 1
./backend/app.py:6:80: E501 line too long (80 > 79 characters)
./backend/app.py:9:1: E302 expected 2 blank lines, found 1
./backend/app.py:14:1: E302 expected 2 blank lines, found 1
./backend/app.py:26:1: E302 expected 2 blank lines, found 1
./backend/app.py:34:1: E302 expected 2 blank lines, found 1
./backend/app.py:46:1: E302 expected 2 blank lines, found 1
./backend/app.py:48:67: W291 trailing whitespace
./backend/app.py:49:80: E501 line too long (88 > 79 characters)
./backend/app.py:49:89: W291 trailing whitespace
./backend/app.py:57:1: W293 blank line contains whitespace
./backend/app.py:64:1: E302 expected 2 blank lines, found 1
./backend/app.py:66:67: W291 trailing whitespace
./backend/app.py:67:80: E501 line too long (88 > 79 characters)
./backend/app.py:67:89: W291 trailing whitespace
./backend/app.py:70:1: W293 blank line contains whitespace
./backend/app.py:75:1: W293 blank line contains whitespace
./backend/app.py:78:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/app.py:79:11: W292 no newline at end of file

### pylint Report:
************* Module app
backend/app.py:57:0: C0303: Trailing whitespace (trailing-whitespace)
backend/app.py:70:0: C0303: Trailing whitespace (trailing-whitespace)
backend/app.py:75:0: C0303: Trailing whitespace (trailing-whitespace)
backend/app.py:79:0: C0304: Final newline missing (missing-final-newline)
backend/app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/app.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:6:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
backend/app.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 7.55/10


### bandit Report:
Run started:2024-06-15 15:47:23.278906

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././backend/app.py:3:0
2	import os
3	import subprocess
4	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ././backend/app.py:6:13
5	def run_command(command):
6	    result = subprocess.run(command, capture_output=True, text=True, shell=True)
7	    return result.stdout if result.stdout else result.stderr

--------------------------------------------------

Code scanned:
	Total lines of code: 65
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 1
		Medium: 0
		High: 1
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 2
Files skipped (0):


## ./backend/logging_config.py
### flake8 Report:
./backend/logging_config.py:12:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module logging_config
backend/logging_config.py:12:4: E0001: Parsing failed: 'unexpected indent (logging_config, line 12)' (syntax-error)

### bandit Report:
Run started:2024-06-15 15:47:23.912329

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 22
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	././backend/logging_config.py (syntax error while parsing AST from file)


## ./backend/offer_generator.py
### flake8 Report:
./backend/offer_generator.py:4:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module offer_generator
backend/offer_generator.py:4:4: E0001: Parsing failed: 'unexpected indent (offer_generator, line 4)' (syntax-error)

### bandit Report:
Run started:2024-06-15 15:47:24.542547

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 12
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (1):
	././backend/offer_generator.py (syntax error while parsing AST from file)


## ./backend/server_connection.py
### flake8 Report:
./backend/server_connection.py:1:1: F401 'os' imported but unused
./backend/server_connection.py:7:1: E302 expected 2 blank lines, found 1
./backend/server_connection.py:15:1: E302 expected 2 blank lines, found 1
./backend/server_connection.py:21:14: W292 no newline at end of file

### pylint Report:
************* Module server_connection
backend/server_connection.py:21:0: C0304: Final newline missing (missing-final-newline)
backend/server_connection.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/server_connection.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/server_connection.py:12:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/server_connection.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/server_connection.py:20:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/server_connection.py:1:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 5.33/10


### bandit Report:
Run started:2024-06-15 15:47:25.443338

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 15
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/vercel.json
## ./backend/property_management.py
### flake8 Report:
./backend/property_management.py:8:1: W391 blank line at end of file

### pylint Report:
************* Module property_management
backend/property_management.py:8:0: C0305: Trailing newlines (trailing-newlines)
backend/property_management.py:5:0: W0105: String statement has no effect (pointless-string-statement)

-----------------------------------
Your code has been rated at 0.00/10


### bandit Report:
Run started:2024-06-15 15:47:26.071259

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 6
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/evaluation/crexi_listing.json
## ./backend/evaluation/store_data.py
### flake8 Report:
./backend/evaluation/store_data.py:11:1: E302 expected 2 blank lines, found 1
./backend/evaluation/store_data.py:16:80: E501 line too long (83 > 79 characters)
./backend/evaluation/store_data.py:26:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/evaluation/store_data.py:26:13: W292 no newline at end of file

### pylint Report:
************* Module store_data
backend/evaluation/store_data.py:26:0: C0304: Final newline missing (missing-final-newline)
backend/evaluation/store_data.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/evaluation/store_data.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 8.33/10


### bandit Report:
Run started:2024-06-15 15:47:34.610600

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 18
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/evaluation/main.py
### flake8 Report:
./backend/evaluation/main.py:18:48: W292 no newline at end of file

### pylint Report:
************* Module main
backend/evaluation/main.py:18:0: C0304: Final newline missing (missing-final-newline)
backend/evaluation/main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/evaluation/main.py:9:11: E1101: Module 'extract_listing_data' has no 'extract_listing_data' member (no-member)
backend/evaluation/main.py:12:0: E1121: Too many positional arguments for function call (too-many-function-args)

-----------------------------------
Your code has been rated at 0.00/10


### bandit Report:
Run started:2024-06-15 15:47:35.269789

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 8
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/evaluation/extract_listing_data.py
### flake8 Report:
./backend/evaluation/extract_listing_data.py:3:1: E302 expected 2 blank lines, found 1
./backend/evaluation/extract_listing_data.py:6:20: W292 no newline at end of file

### pylint Report:
************* Module extract_listing_data
backend/evaluation/extract_listing_data.py:6:0: C0304: Final newline missing (missing-final-newline)
backend/evaluation/extract_listing_data.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/evaluation/extract_listing_data.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/evaluation/extract_listing_data.py:4:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

-----------------------------------
Your code has been rated at 2.00/10


### bandit Report:
Run started:2024-06-15 15:47:36.040084

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 5
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/evaluation/visualize_data.py
### flake8 Report:
./backend/evaluation/visualize_data.py:7:1: E302 expected 2 blank lines, found 1
./backend/evaluation/visualize_data.py:9:80: E501 line too long (86 > 79 characters)
./backend/evaluation/visualize_data.py:16:15: W292 no newline at end of file

### pylint Report:
************* Module visualize_data
backend/evaluation/visualize_data.py:16:0: C0304: Final newline missing (missing-final-newline)
backend/evaluation/visualize_data.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/evaluation/visualize_data.py:3:0: E0401: Unable to import 'matplotlib.pyplot' (import-error)
backend/evaluation/visualize_data.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/evaluation/visualize_data.py:7:19: W0613: Unused argument 'analysis_results' (unused-argument)

-----------------------------------
Your code has been rated at 1.82/10


### bandit Report:
Run started:2024-06-15 15:47:45.958247

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 11
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## ./backend/evaluation/analyze_data.py
### flake8 Report:
./backend/evaluation/analyze_data.py:6:1: E302 expected 2 blank lines, found 1
./backend/evaluation/analyze_data.py:18:6: W292 no newline at end of file

### pylint Report:
************* Module analyze_data
backend/evaluation/analyze_data.py:18:0: C0304: Final newline missing (missing-final-newline)
backend/evaluation/analyze_data.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/evaluation/analyze_data.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 5.71/10


### bandit Report:
Run started:2024-06-15 15:47:55.741333

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 9
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):


## Summary
### Current Status
The following sections outline the current state of the repository based on the evaluation:
 - **Code Style Improvement**: Address the 121 issues reported by flake8.
 - **Code Quality Enhancement**: Resolve the 191 warnings and errors reported by pylint.
 - **Security Improvement**: Fix the 494 security issues identified by bandit.

### Next Steps
To align the project with the outlined goals, the following actions are recommended:
- Improve code style and consistency by addressing flake8 issues.
- Enhance code quality by resolving pylint warnings and errors.
- Improve security by fixing issues identified by bandit.
- Improve server connection reliability and efficiency.
- Enhance site scraper with better logging and error handling.
- Implement evaluation logic for single-family and multi-family homes.
- Develop the property offer generator module.
