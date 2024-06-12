# Progress Report

## ./improve_project.py
### flake8 Report:
./improve_project.py:4:1: E302 expected 2 blank lines, found 1
./improve_project.py:6:80: E501 line too long (84 > 79 characters)
./improve_project.py:12:1: E302 expected 2 blank lines, found 1
./improve_project.py:31:1: E302 expected 2 blank lines, found 1
./improve_project.py:52:1: E302 expected 2 blank lines, found 1
./improve_project.py:55:1: W293 blank line contains whitespace
./improve_project.py:72:1: E302 expected 2 blank lines, found 1
./improve_project.py:83:1: E302 expected 2 blank lines, found 1
./improve_project.py:94:1: W293 blank line contains whitespace
./improve_project.py:99:80: E501 line too long (85 > 79 characters)
./improve_project.py:102:1: E302 expected 2 blank lines, found 1
./improve_project.py:109:80: E501 line too long (80 > 79 characters)
./improve_project.py:115:80: E501 line too long (92 > 79 characters)
./improve_project.py:122:1: E305 expected 2 blank lines after class or function definition, found 1
./improve_project.py:124:80: E501 line too long (86 > 79 characters)
./improve_project.py:130:20: W292 no newline at end of file

### pylint Report:
************* Module improve_project
improve_project.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
improve_project.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
improve_project.py:130:0: C0304: Final newline missing (missing-final-newline)
improve_project.py:1:0: C0114: Missing module docstring (missing-module-docstring)
improve_project.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:27:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
improve_project.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:48:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
improve_project.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:65:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
improve_project.py:68:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
improve_project.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:79:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
improve_project.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:119:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

-----------------------------------
Your code has been rated at 7.21/10


### bandit Report:
Run started:2024-06-12 23:03:48.898704

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././improve_project.py:2:0
1	import os
2	import subprocess
3	

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././improve_project.py:6:17
5	    try:
6	        result = subprocess.run(command, capture_output=True, text=True, check=True)
7	        return result.stdout

--------------------------------------------------

Code scanned:
	Total lines of code: 103
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 2
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 2
Files skipped (0):


## ./evaluate_repo.py
### flake8 Report:
./evaluate_repo.py:3:1: F401 're' imported but unused
./evaluate_repo.py:5:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:6:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:9:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:10:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:13:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:14:80: E501 line too long (87 > 79 characters)
./evaluate_repo.py:17:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:25:80: E501 line too long (83 > 79 characters)
./evaluate_repo.py:28:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:37:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:38:80: E501 line too long (120 > 79 characters)
./evaluate_repo.py:50:80: E501 line too long (91 > 79 characters)
./evaluate_repo.py:52:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:53:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:54:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:55:80: E501 line too long (112 > 79 characters)
./evaluate_repo.py:56:80: E501 line too long (95 > 79 characters)
./evaluate_repo.py:59:80: E501 line too long (84 > 79 characters)
./evaluate_repo.py:69:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:70:11: W292 no newline at end of file

### pylint Report:
************* Module evaluate_repo
evaluate_repo.py:38:0: C0301: Line too long (120/100) (line-too-long)
evaluate_repo.py:70:0: C0304: Final newline missing (missing-final-newline)
evaluate_repo.py:1:0: C0114: Missing module docstring (missing-module-docstring)
evaluate_repo.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:6:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:10:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:14:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:42:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:66:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:3:0: W0611: Unused import re (unused-import)

-----------------------------------
Your code has been rated at 6.34/10


### bandit Report:
Run started:2024-06-12 23:03:50.203027

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././evaluate_repo.py:2:0
1	import os
2	import subprocess
3	import re

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:6:13
5	def run_flake8(filepath):
6	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
7	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:6:13
5	def run_flake8(filepath):
6	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
7	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:10:13
9	def run_pylint(filepath):
10	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
11	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:10:13
9	def run_pylint(filepath):
10	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
11	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:14:13
13	def run_bandit(filepath):
14	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
15	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:14:13
13	def run_bandit(filepath):
14	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
15	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------

Code scanned:
	Total lines of code: 53
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 7
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 7
Files skipped (0):


## ./backend/site_scraper.py
### flake8 Report:
./backend/site_scraper.py:10:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module site_scraper
backend/site_scraper.py:10:4: E0001: Parsing failed: 'unexpected indent (site_scraper, line 10)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:03:50.898053

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
Run started:2024-06-12 23:03:51.605852

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
Run started:2024-06-12 23:03:52.305865

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
./backend/single_family_evaluation.py:6:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module single_family_evaluation
backend/single_family_evaluation.py:6:4: E0001: Parsing failed: 'unexpected indent (single_family_evaluation, line 6)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:03:52.947713

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 13
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


## ./backend/scrape_crexi.py
### flake8 Report:
./backend/scrape_crexi.py:12:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_crexi
backend/scrape_crexi.py:12:4: E0001: Parsing failed: 'unexpected indent (scrape_crexi, line 12)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:03:53.585955

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 24
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
	././backend/scrape_crexi.py (syntax error while parsing AST from file)


## ./backend/multi_family_evaluation.py
### flake8 Report:
./backend/multi_family_evaluation.py:6:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module multi_family_evaluation
backend/multi_family_evaluation.py:6:4: E0001: Parsing failed: 'unexpected indent (multi_family_evaluation, line 6)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:03:54.220710

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 13
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
./backend/scrape_zillow.py:18:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_zillow
backend/scrape_zillow.py:18:4: E0001: Parsing failed: 'unexpected indent (scrape_zillow, line 18)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:03:54.860997

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


## ./backend/scrape_zillow_with_langchain.py
### flake8 Report:
./backend/scrape_zillow_with_langchain.py:9:1: F401 'requests' imported but unused
./backend/scrape_zillow_with_langchain.py:9:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:10:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:11:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:12:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:13:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:14:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:15:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:16:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:18:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow_with_langchain.py:38:80: E501 line too long (106 > 79 characters)
./backend/scrape_zillow_with_langchain.py:39:1: W293 blank line contains whitespace
./backend/scrape_zillow_with_langchain.py:56:80: E501 line too long (99 > 79 characters)
./backend/scrape_zillow_with_langchain.py:57:80: E501 line too long (91 > 79 characters)
./backend/scrape_zillow_with_langchain.py:67:1: E302 expected 2 blank lines, found 0
./backend/scrape_zillow_with_langchain.py:72:80: E501 line too long (86 > 79 characters)
./backend/scrape_zillow_with_langchain.py:81:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/scrape_zillow_with_langchain.py:82:80: E501 line too long (94 > 79 characters)

### pylint Report:
************* Module scrape_zillow_with_langchain
backend/scrape_zillow_with_langchain.py:38:0: C0301: Line too long (106/100) (line-too-long)
backend/scrape_zillow_with_langchain.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow_with_langchain.py:5:0: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:9:0: C0413: Import "import requests" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:10:0: C0413: Import "from bs4 import BeautifulSoup" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:11:0: C0413: Import "from selenium import webdriver" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:12:0: C0413: Import "from selenium.webdriver.chrome.service import Service as ChromeService" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:13:0: C0413: Import "from webdriver_manager.chrome import ChromeDriverManager" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:14:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:15:0: C0413: Import "from langchain.prompts import Prompt" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:16:0: C0413: Import "from llama_index import Document, GPTVectorStoreIndex" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:16:0: E0611: No name 'Document' in module 'llama_index' (no-name-in-module)
backend/scrape_zillow_with_langchain.py:16:0: E0611: No name 'GPTVectorStoreIndex' in module 'llama_index' (no-name-in-module)
backend/scrape_zillow_with_langchain.py:22:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:28:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:31:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_langchain.py:34:18: W0621: Redefining name 'url' from outer scope (line 82) (redefined-outer-name)
backend/scrape_zillow_with_langchain.py:61:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:64:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:18:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backend/scrape_zillow_with_langchain.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_langchain.py:67:26: W0621: Redefining name 'url' from outer scope (line 82) (redefined-outer-name)
backend/scrape_zillow_with_langchain.py:82:4: C0103: Constant name "url" doesn't conform to UPPER_CASE naming style (invalid-name)
backend/scrape_zillow_with_langchain.py:14:0: C0411: standard import "time" should be placed before third party imports "requests", "bs4.BeautifulSoup", "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "webdriver_manager.chrome.ChromeDriverManager" (wrong-import-order)
backend/scrape_zillow_with_langchain.py:9:0: W0611: Unused import requests (unused-import)

-----------------------------------
Your code has been rated at 2.44/10


### bandit Report:
Run started:2024-06-12 23:03:59.484295

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 63
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


## ./backend/app.py
### flake8 Report:
./backend/app.py:25:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module app
backend/app.py:25:4: E0001: Parsing failed: 'unexpected indent (app, line 25)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:04:00.124837

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 71
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
	././backend/app.py (syntax error while parsing AST from file)


## ./backend/scrape_zillow_with_selenium.py
### flake8 Report:
./backend/scrape_zillow_with_selenium.py:15:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_zillow_with_selenium
backend/scrape_zillow_with_selenium.py:15:4: E0001: Parsing failed: 'unexpected indent (scrape_zillow_with_selenium, line 15)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:04:00.780571

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 36
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
	././backend/scrape_zillow_with_selenium.py (syntax error while parsing AST from file)


## ./backend/logging_config.py
### flake8 Report:
./backend/logging_config.py:11:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module logging_config
backend/logging_config.py:11:4: E0001: Parsing failed: 'unexpected indent (logging_config, line 11)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:04:01.421892

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
./backend/offer_generator.py:6:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module offer_generator
backend/offer_generator.py:6:4: E0001: Parsing failed: 'unexpected indent (offer_generator, line 6)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:04:02.060527

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
Files skipped (1):
	././backend/offer_generator.py (syntax error while parsing AST from file)


## ./backend/server_connection.py
### flake8 Report:
./backend/server_connection.py:9:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module server_connection
backend/server_connection.py:9:4: E0001: Parsing failed: 'unexpected indent (server_connection, line 9)' (syntax-error)

### bandit Report:
Run started:2024-06-12 23:04:02.698493

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 16
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
	././backend/server_connection.py (syntax error while parsing AST from file)


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
Run started:2024-06-12 23:04:03.333477

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



## Summary

### Current Status
The following sections outline the current state of the repository based on the evaluation:

 - **Server Connection Improvement**: Improve the reliability and efficiency of the server connection module.
 - **Site Scraper Enhancement**: Ensure robust scraping logic and error handling.
 - **Evaluation of Single Family Homes**: Implement a comprehensive evaluation logic for single-family homes.
 - **Multi-Family Homes Evaluation**: Adapt the single-family evaluation logic to handle multi-family specifics.
 - **Property Offer Generator**: Create a module that generates offers based on evaluated data.

### Next Steps
To align the project with the outlined goals, the following actions are recommended:
- Improve server connection reliability and efficiency.
- Enhance site scraper with better logging and error handling.
- Implement evaluation logic for single-family and multi-family homes.
- Develop the property offer generator module.

