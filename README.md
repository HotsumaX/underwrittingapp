# Progress Report

## Repository Files

### ./gpt_code_review.py
#### flake8 Report:
./gpt_code_review.py:3:1: E302 expected 2 blank lines, found 1
./gpt_code_review.py:8:80: E501 line too long (87 > 79 characters)

#### pylint Report:
************* Module gpt_code_review
gpt_code_review.py:1:0: C0114: Missing module docstring (missing-module-docstring)
gpt_code_review.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
gpt_code_review.py:4:15: E1101: Module 'openai' has no 'ChatCompletion' member (no-member)

-----------------------------------
Your code has been rated at 0.00/10


#### bandit Report:
Run started:2024-06-12 21:27:31.893764

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 10
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


### ./evaluate_repo.py
#### flake8 Report:
./evaluate_repo.py:5:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:10:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:11:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:14:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:15:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:18:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:19:80: E501 line too long (87 > 79 characters)
./evaluate_repo.py:22:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:38:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:46:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:66:80: E501 line too long (124 > 79 characters)
./evaluate_repo.py:78:80: E501 line too long (115 > 79 characters)
./evaluate_repo.py:88:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:89:11: W292 no newline at end of file

#### pylint Report:
************* Module evaluate_repo
evaluate_repo.py:66:0: C0301: Line too long (124/100) (line-too-long)
evaluate_repo.py:78:0: C0301: Line too long (115/100) (line-too-long)
evaluate_repo.py:89:0: C0304: Final newline missing (missing-final-newline)
evaluate_repo.py:1:0: C0114: Missing module docstring (missing-module-docstring)
evaluate_repo.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:6:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:11:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:15:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:19:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:26:19: W0612: Unused variable 'status' (unused-variable)
evaluate_repo.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:50:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:60:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:63:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:83:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:85:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

-----------------------------------
Your code has been rated at 7.04/10


#### bandit Report:
Run started:2024-06-12 21:27:33.315139

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././evaluate_repo.py:2:0
1	import os
2	import subprocess
3	import re

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:11:13
10	def run_flake8(filepath):
11	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
12	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:11:13
10	def run_flake8(filepath):
11	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
12	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:15:13
14	def run_pylint(filepath):
15	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
16	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:15:13
14	def run_pylint(filepath):
15	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
16	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:19:13
18	def run_bandit(filepath):
19	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
20	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:19:13
18	def run_bandit(filepath):
19	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
20	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------

Code scanned:
	Total lines of code: 76
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


### ./backend/site_scraper.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:33.957667

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/log_section.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:34.597006

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/email_contact.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:35.235039

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/single_family_evaluation.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:35.879535

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/scrape_crexi.py
#### flake8 Report:
./backend/scrape_crexi.py:4:1: E302 expected 2 blank lines, found 1
./backend/scrape_crexi.py:10:80: E501 line too long (86 > 79 characters)
./backend/scrape_crexi.py:11:80: E501 line too long (138 > 79 characters)
./backend/scrape_crexi.py:12:80: E501 line too long (132 > 79 characters)

#### pylint Report:
************* Module scrape_crexi
backend/scrape_crexi.py:11:0: C0301: Line too long (138/100) (line-too-long)
backend/scrape_crexi.py:12:0: C0301: Line too long (132/100) (line-too-long)
backend/scrape_crexi.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/scrape_crexi.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_crexi.py:6:15: W3101: Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely (missing-timeout)

-----------------------------------
Your code has been rated at 5.83/10


#### bandit Report:
Run started:2024-06-12 21:27:36.872090

Test results:
>> Issue: [B113:request_without_timeout] Requests call without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b113_request_without_timeout.html
   Location: ././backend/scrape_crexi.py:6:15
5	    url = 'https://www.crexi.com/properties'
6	    response = requests.get(url)
7	    soup = BeautifulSoup(response.text, 'html.parser')

--------------------------------------------------

Code scanned:
	Total lines of code: 12
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 1
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 1
		Medium: 0
		High: 0
Files skipped (0):


### ./backend/multi_family_evaluation.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:37.519228

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/scrape_zillow.py
#### flake8 Report:
./backend/scrape_zillow.py:6:1: F401 'selenium.webdriver.common.by.By' imported but unused
./backend/scrape_zillow.py:13:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow.py:21:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:24:80: E501 line too long (85 > 79 characters)
./backend/scrape_zillow.py:25:80: E501 line too long (166 > 79 characters)
./backend/scrape_zillow.py:26:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:27:80: E501 line too long (114 > 79 characters)
./backend/scrape_zillow.py:28:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:30:80: E501 line too long (91 > 79 characters)
./backend/scrape_zillow.py:31:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:34:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:36:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:40:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:41:80: E501 line too long (107 > 79 characters)
./backend/scrape_zillow.py:42:80: E501 line too long (99 > 79 characters)
./backend/scrape_zillow.py:43:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:45:1: W293 blank line contains whitespace
./backend/scrape_zillow.py:47:80: E501 line too long (88 > 79 characters)
./backend/scrape_zillow.py:49:80: E501 line too long (82 > 79 characters)
./backend/scrape_zillow.py:53:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow.py:59:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/scrape_zillow.py:60:80: E501 line too long (94 > 79 characters)

#### pylint Report:
************* Module scrape_zillow
backend/scrape_zillow.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:25:0: C0301: Line too long (166/100) (line-too-long)
backend/scrape_zillow.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:27:0: C0301: Line too long (114/100) (line-too-long)
backend/scrape_zillow.py:28:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:36:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:40:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:41:0: C0301: Line too long (107/100) (line-too-long)
backend/scrape_zillow.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:45:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/scrape_zillow.py:13:0: C0115: Missing class docstring (missing-class-docstring)
backend/scrape_zillow.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow.py:17:18: W0621: Redefining name 'url' from outer scope (line 60) (redefined-outer-name)
backend/scrape_zillow.py:46:19: W0718: Catching too general exception Exception (broad-exception-caught)
backend/scrape_zillow.py:20:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_zillow.py:47:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/scrape_zillow.py:17:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
backend/scrape_zillow.py:13:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backend/scrape_zillow.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow.py:53:26: W0621: Redefining name 'url' from outer scope (line 60) (redefined-outer-name)
backend/scrape_zillow.py:60:4: C0103: Constant name "url" doesn't conform to UPPER_CASE naming style (invalid-name)
backend/scrape_zillow.py:7:0: C0411: standard import "logging" should be placed before third party imports "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "webdriver_manager.chrome.ChromeDriverManager", "selenium.webdriver.common.by.By" (wrong-import-order)
backend/scrape_zillow.py:6:0: C0412: Imports from package selenium are not grouped (ungrouped-imports)
backend/scrape_zillow.py:6:0: W0611: Unused By imported from selenium.webdriver.common.by (unused-import)

-----------------------------------
Your code has been rated at 4.13/10


#### bandit Report:
Run started:2024-06-12 21:27:39.366240

Test results:
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/blacklists/blacklist_calls.html#b311-random
   Location: ././backend/scrape_zillow.py:30:27
29	                driver.get(url)
30	                time.sleep(random.uniform(2, 5))  # Random delay to simulate human behavior
31	                

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/blacklists/blacklist_calls.html#b311-random
   Location: ././backend/scrape_zillow.py:49:31
48	                if attempt < self.retries - 1:
49	                    time.sleep(random.uniform(3, 6))  # Wait a bit before retrying
50	                else:

--------------------------------------------------

Code scanned:
	Total lines of code: 47
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


### ./backend/scrape_zillow_with_langchain.py
#### flake8 Report:
./backend/scrape_zillow_with_langchain.py:1:1: F401 'requests' imported but unused
./backend/scrape_zillow_with_langchain.py:10:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow_with_langchain.py:18:80: E501 line too long (106 > 79 characters)
./backend/scrape_zillow_with_langchain.py:19:1: W293 blank line contains whitespace
./backend/scrape_zillow_with_langchain.py:36:80: E501 line too long (99 > 79 characters)
./backend/scrape_zillow_with_langchain.py:37:80: E501 line too long (91 > 79 characters)
./backend/scrape_zillow_with_langchain.py:41:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow_with_langchain.py:46:80: E501 line too long (86 > 79 characters)
./backend/scrape_zillow_with_langchain.py:55:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/scrape_zillow_with_langchain.py:56:80: E501 line too long (94 > 79 characters)

#### pylint Report:
************* Module scrape_zillow_with_langchain
backend/scrape_zillow_with_langchain.py:18:0: C0301: Line too long (106/100) (line-too-long)
backend/scrape_zillow_with_langchain.py:19:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow_with_langchain.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/scrape_zillow_with_langchain.py:8:0: E0611: No name 'Document' in module 'llama_index' (no-name-in-module)
backend/scrape_zillow_with_langchain.py:8:0: E0611: No name 'GPTVectorStoreIndex' in module 'llama_index' (no-name-in-module)
backend/scrape_zillow_with_langchain.py:10:0: C0115: Missing class docstring (missing-class-docstring)
backend/scrape_zillow_with_langchain.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_langchain.py:14:18: W0621: Redefining name 'url' from outer scope (line 56) (redefined-outer-name)
backend/scrape_zillow_with_langchain.py:10:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backend/scrape_zillow_with_langchain.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_langchain.py:41:26: W0621: Redefining name 'url' from outer scope (line 56) (redefined-outer-name)
backend/scrape_zillow_with_langchain.py:56:4: C0103: Constant name "url" doesn't conform to UPPER_CASE naming style (invalid-name)
backend/scrape_zillow_with_langchain.py:6:0: C0411: standard import "time" should be placed before third party imports "requests", "bs4.BeautifulSoup", "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "webdriver_manager.chrome.ChromeDriverManager" (wrong-import-order)
backend/scrape_zillow_with_langchain.py:1:0: W0611: Unused import requests (unused-import)

-----------------------------------
Your code has been rated at 4.36/10


#### bandit Report:
Run started:2024-06-12 21:27:43.874728

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 39
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


### ./backend/app.py
#### flake8 Report:
./backend/app.py:5:1: F401 'selenium.webdriver.common.by.By' imported but unused
./backend/app.py:17:1: E302 expected 2 blank lines, found 1
./backend/app.py:24:1: E302 expected 2 blank lines, found 1
./backend/app.py:39:1: E302 expected 2 blank lines, found 1
./backend/app.py:45:1: E302 expected 2 blank lines, found 1
./backend/app.py:49:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/app.py:50:24: W292 no newline at end of file

#### pylint Report:
************* Module app
backend/app.py:50:0: C0304: Final newline missing (missing-final-newline)
backend/app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:34:11: W0718: Catching too general exception Exception (broad-exception-caught)
backend/app.py:36:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
backend/app.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/app.py:9:0: C0411: standard import "time" should be placed before third party imports "flask.Flask", "flask_cors.CORS", "selenium.webdriver" (...) "selenium.webdriver.chrome.service.Service", "webdriver_manager.chrome.ChromeDriverManager", "selenium.webdriver.chrome.options.Options" (wrong-import-order)
backend/app.py:8:0: C0412: Imports from package selenium are not grouped (ungrouped-imports)
backend/app.py:5:0: W0611: Unused By imported from selenium.webdriver.common.by (unused-import)

-----------------------------------
Your code has been rated at 7.18/10


#### bandit Report:
Run started:2024-06-12 21:27:47.590543

Test results:
>> Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
   Severity: High   Confidence: Medium
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b201_flask_debug_true.html
   Location: ././backend/app.py:50:4
49	if __name__ == '__main__':
50	    app.run(debug=True)

--------------------------------------------------

Code scanned:
	Total lines of code: 41
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 1
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 1
		High: 0
Files skipped (0):


### ./backend/scrape_zillow_with_selenium.py
#### flake8 Report:
./backend/scrape_zillow_with_selenium.py:7:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow_with_selenium.py:10:80: E501 line too long (102 > 79 characters)
./backend/scrape_zillow_with_selenium.py:11:1: W293 blank line contains whitespace
./backend/scrape_zillow_with_selenium.py:17:80: E501 line too long (102 > 79 characters)
./backend/scrape_zillow_with_selenium.py:18:5: E722 do not use bare 'except'
./backend/scrape_zillow_with_selenium.py:23:80: E501 line too long (90 > 79 characters)
./backend/scrape_zillow_with_selenium.py:24:5: E722 do not use bare 'except'
./backend/scrape_zillow_with_selenium.py:26:1: W293 blank line contains whitespace

#### pylint Report:
************* Module scrape_zillow_with_selenium
backend/scrape_zillow_with_selenium.py:10:0: C0301: Line too long (102/100) (line-too-long)
backend/scrape_zillow_with_selenium.py:11:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow_with_selenium.py:17:0: C0301: Line too long (102/100) (line-too-long)
backend/scrape_zillow_with_selenium.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow_with_selenium.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backend/scrape_zillow_with_selenium.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_selenium.py:18:4: W0702: No exception type(s) specified (bare-except)
backend/scrape_zillow_with_selenium.py:24:4: W0702: No exception type(s) specified (bare-except)

-----------------------------------
Your code has been rated at 6.19/10


#### bandit Report:
Run started:2024-06-12 21:27:48.847893

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
Files skipped (0):


### ./backend/offer_generator.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:49.487664

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/server_connection.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:50.195189

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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


### ./backend/property_management.py
#### flake8 Report:
No issues found by flake8.
#### pylint Report:
No issues found by pylint.
#### bandit Report:
Run started:2024-06-12 21:27:50.830036

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 0
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

 - **./gpt_code_review.py**: 11 lines, has flake8 issues, has pylint issues, has bandit issues
 - **./evaluate_repo.py**: 89 lines, has flake8 issues, has pylint issues
 - **./backend/site_scraper.py**: 0 lines, has bandit issues
 - **./backend/log_section.py**: 0 lines, has bandit issues
 - **./backend/email_contact.py**: 0 lines, has bandit issues
 - **./backend/single_family_evaluation.py**: 0 lines, has bandit issues
 - **./backend/scrape_crexi.py**: 15 lines, has flake8 issues, has pylint issues, has bandit issues
 - **./backend/multi_family_evaluation.py**: 0 lines, has bandit issues
 - **./backend/scrape_zillow.py**: 62 lines, has flake8 issues, has pylint issues, has bandit issues
 - **./backend/scrape_zillow_with_langchain.py**: 59 lines, has flake8 issues, has pylint issues, has bandit issues
 - **./backend/app.py**: 50 lines, has flake8 issues, has pylint issues, has bandit issues
 - **./backend/scrape_zillow_with_selenium.py**: 32 lines, has flake8 issues, has pylint issues, has bandit issues
 - **./backend/offer_generator.py**: 0 lines, has bandit issues
 - **./backend/server_connection.py**: 0 lines, has bandit issues
 - **./backend/property_management.py**: 0 lines, has bandit issues

### Next Steps
To align the project with the outlined goals, the following actions are recommended:
- ## 1. Server Connection Status
- ## Goals:
- ## Tasks:
- ## Change Log:
- ## 2. Site Scraper
- ## Goals:
- ## Tasks:
- ## Change Log:
- ## 3. Single Family Homes Evaluation
- ## Goals:
- ## Tasks:
- ## 4. Multi Family Homes Evaluation
- ## Goals:
- ## Tasks:
- ## 5. Email to Point of Contact for the Listing
- ## Goals:
- ## Tasks:
- ## 6. Property Management Section (Future)
- ## Goals:
- ## Tasks:
- ## 7. Log Section
- ## Goals:
- ## Tasks:
- ## 8. Property Offer Generator Feature
- ## Goals:
- ## Data Collection Modules:
- ## Market Comparables Module
- ## Financial Data Module
- ## Property Condition Module
- ## Market Trends Module
- ## Financing Options Module
- ## Data Analysis and Interpretation:
- ## Comparative Market Analysis (CMA)
- ## Financial Analysis
- ## Property Condition Assessment
- ## Market and Economic Analysis
- ## Financing Impact Analysis
- ## Offer Generation:
- ## Offer Price Calculation
- ## Offer Letter Drafting
- ## Customization Options
- ## User Interface:
- ## Dashboard Overview
- ## Detailed Reports
- ## Offer Letter Preview and Edit
- ## Submission and Tracking
- ## Integration and Automation:
- ## APIs for Data Fetching
- ## Automated Report Generation
- ## Notification System
- ## Testing and Validation:
- ## Module Testing
- ## User Acceptance Testing
- ## Performance Optimization
- ## Documentation and Support:
- ## User Guide
- ## Technical Documentation
- ## Customer Support Integration
- ## Change Log
- ## Server Connection Status:
- ## Site Scraper:
- ## Property Offer Generator:
- ## Server Connection.Py
- ## Site Scraper.Py
- ## Single Family Evaluation.Py
- ## Multi Family Evaluation.Py
- ## Email Contact.Py
- ## Property Management.Py
- ## Log Section.Py
- ## Offer Generator.Py
- ## Frontend
- ## Server Connection.Py
- ## Site Scraper.Py
- ## Single Family Evaluation.Py
- ## Multi Family Evaluation.Py
- ## Email Contact.Py
- ## Property Management.Py
- ## Log Section.Py
- ## Offer Generator.Py
- ## Frontend
- ## Server Connection.Py
- ## Site Scraper.Py
- ## Single Family Evaluation.Py
- ## Multi Family Evaluation.Py
- ## Email Contact.Py
- ## Property Management.Py
- ## Log Section.Py
- ## Offer Generator.Py
- ## Frontend
- ## Server Connection.Py
- ## Site Scraper.Py
- ## Single Family Evaluation.Py
- ## Multi Family Evaluation.Py
- ## Email Contact.Py
- ## Property Management.Py
- ## Log Section.Py
- ## Offer Generator.Py
- ## Frontend

