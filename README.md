# Progress Report

## ./improve_project.py
### flake8 Report:
./improve_project.py:9:6: E999 SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

### pylint Report:
************* Module improve_project
improve_project.py:9:5: E0001: Parsing failed: 'invalid syntax. Maybe you meant '==' or ':=' instead of '='? (improve_project, line 9)' (syntax-error)

### bandit Report:
Run started:2024-06-13 00:26:02.158567

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 27
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
	././improve_project.py (syntax error while parsing AST from file)


## ./update_files.py
### flake8 Report:
./update_files.py:2:1: F401 'os' imported but unused
./update_files.py:4:1: E302 expected 2 blank lines, found 1
./update_files.py:7:80: E501 line too long (81 > 79 characters)
./update_files.py:13:1: E302 expected 2 blank lines, found 1
./update_files.py:18:1: W293 blank line contains whitespace
./update_files.py:20:1: W293 blank line contains whitespace
./update_files.py:23:1: W293 blank line contains whitespace
./update_files.py:27:1: W293 blank line contains whitespace
./update_files.py:31:1: E305 expected 2 blank lines after class or function definition, found 1
./update_files.py:40:29: W292 no newline at end of file

### pylint Report:
************* Module update_files
update_files.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
update_files.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
update_files.py:23:0: C0303: Trailing whitespace (trailing-whitespace)
update_files.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
update_files.py:40:0: C0304: Final newline missing (missing-final-newline)
update_files.py:1:0: C0114: Missing module docstring (missing-module-docstring)
update_files.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
update_files.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
update_files.py:13:17: W0621: Redefining name 'file_paths' from outer scope (line 32) (redefined-outer-name)
update_files.py:16:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
update_files.py:21:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
update_files.py:28:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
update_files.py:2:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 4.35/10


### bandit Report:
Run started:2024-06-13 00:26:03.399077

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 30
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


## ./evaluate_repo.py
### flake8 Report:
./evaluate_repo.py:4:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:7:80: E501 line too long (96 > 79 characters)
./evaluate_repo.py:12:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:21:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:34:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:37:67: W291 trailing whitespace
./evaluate_repo.py:38:80: E501 line too long (88 > 79 characters)
./evaluate_repo.py:38:89: W291 trailing whitespace
./evaluate_repo.py:46:1: W293 blank line contains whitespace
./evaluate_repo.py:53:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:56:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:61:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:64:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:69:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:72:80: E501 line too long (103 > 79 characters)
./evaluate_repo.py:77:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:86:80: E501 line too long (83 > 79 characters)
./evaluate_repo.py:89:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:99:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:101:80: E501 line too long (120 > 79 characters)
./evaluate_repo.py:113:80: E501 line too long (91 > 79 characters)
./evaluate_repo.py:115:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:116:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:117:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:118:80: E501 line too long (112 > 79 characters)
./evaluate_repo.py:119:80: E501 line too long (95 > 79 characters)
./evaluate_repo.py:122:80: E501 line too long (84 > 79 characters)
./evaluate_repo.py:132:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:133:11: W292 no newline at end of file

### pylint Report:
************* Module evaluate_repo
evaluate_repo.py:46:0: C0303: Trailing whitespace (trailing-whitespace)
evaluate_repo.py:72:0: C0301: Line too long (103/100) (line-too-long)
evaluate_repo.py:101:0: C0301: Line too long (120/100) (line-too-long)
evaluate_repo.py:133:0: C0304: Final newline missing (missing-final-newline)
evaluate_repo.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 9.37/10


### bandit Report:
Run started:2024-06-13 00:26:04.830200

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
   Location: ././evaluate_repo.py:7:17
6	    try:
7	        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
8	        return result.stdout if result.stdout else result.stderr

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:56:17
55	    try:
56	        result = subprocess.run(['flake8', filepath], capture_output=True, text=True, check=True)
57	        return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:56:17
55	    try:
56	        result = subprocess.run(['flake8', filepath], capture_output=True, text=True, check=True)
57	        return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:64:17
63	    try:
64	        result = subprocess.run(['pylint', filepath], capture_output=True, text=True, check=True)
65	        return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:64:17
63	    try:
64	        result = subprocess.run(['pylint', filepath], capture_output=True, text=True, check=True)
65	        return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:72:17
71	    try:
72	        result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True, check=True)
73	        return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:72:17
71	    try:
72	        result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True, check=True)
73	        return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------

Code scanned:
	Total lines of code: 109
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 7
		Medium: 0
		High: 1
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 8
Files skipped (0):


## ./backend/site_scraper.py
### flake8 Report:
./backend/site_scraper.py:6:1: E302 expected 2 blank lines, found 0

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 00:26:06.398249

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
Run started:2024-06-13 00:26:07.158560

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
Run started:2024-06-13 00:26:07.894692

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
./backend/single_family_evaluation.py:2:1: E302 expected 2 blank lines, found 0

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 00:26:08.625536

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


## ./backend/scrape_crexi.py
### flake8 Report:
./backend/scrape_crexi.py:12:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_crexi
backend/scrape_crexi.py:12:4: E0001: Parsing failed: 'unexpected indent (scrape_crexi, line 12)' (syntax-error)

### bandit Report:
Run started:2024-06-13 00:26:09.341189

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
./backend/multi_family_evaluation.py:2:1: E302 expected 2 blank lines, found 0

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 00:26:10.109359

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


## ./backend/scrape_zillow.py
### flake8 Report:
./backend/scrape_zillow.py:18:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_zillow
backend/scrape_zillow.py:18:4: E0001: Parsing failed: 'unexpected indent (scrape_zillow, line 18)' (syntax-error)

### bandit Report:
Run started:2024-06-13 00:26:10.814906

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
Run started:2024-06-13 00:26:15.842028

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
Run started:2024-06-13 00:26:16.573672

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
./backend/scrape_zillow_with_selenium.py:6:1: E302 expected 2 blank lines, found 0

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 00:26:17.844612

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
Files skipped (0):


## ./backend/logging_config.py
### flake8 Report:
./backend/logging_config.py:11:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module logging_config
backend/logging_config.py:11:4: E0001: Parsing failed: 'unexpected indent (logging_config, line 11)' (syntax-error)

### bandit Report:
Run started:2024-06-13 00:26:18.555261

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
./backend/offer_generator.py:2:1: E302 expected 2 blank lines, found 0

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 00:26:19.294795

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
Files skipped (0):


## ./backend/server_connection.py
### flake8 Report:
./backend/server_connection.py:4:1: E302 expected 2 blank lines, found 0

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 00:26:21.174513

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 17
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
Run started:2024-06-13 00:26:21.969843

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

