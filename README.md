# Progress Report

## ./improve_project.py
### flake8 Report:
./improve_project.py:11:6: E999 SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

### pylint Report:
************* Module improve_project
improve_project.py:11:5: E0001: Parsing failed: 'invalid syntax. Maybe you meant '==' or ':=' instead of '='? (improve_project, line 11)' (syntax-error)

### bandit Report:
Run started:2024-06-13 11:24:18.276996

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
./update_files.py:9:80: E501 line too long (99 > 79 characters)
./update_files.py:29:80: E501 line too long (96 > 79 characters)
./update_files.py:62:67: W291 trailing whitespace
./update_files.py:63:80: E501 line too long (88 > 79 characters)
./update_files.py:63:89: W291 trailing whitespace
./update_files.py:71:1: W293 blank line contains whitespace
./update_files.py:81:80: E501 line too long (93 > 79 characters)
./update_files.py:87:80: E501 line too long (93 > 79 characters)
./update_files.py:93:80: E501 line too long (99 > 79 characters)
./update_files.py:106:80: E501 line too long (83 > 79 characters)
./update_files.py:123:80: E501 line too long (120 > 79 characters)
./update_files.py:136:80: E501 line too long (91 > 79 characters)
./update_files.py:138:80: E501 line too long (109 > 79 characters)
./update_files.py:139:80: E501 line too long (81 > 79 characters)
./update_files.py:140:80: E501 line too long (109 > 79 characters)
./update_files.py:141:80: E501 line too long (112 > 79 characters)
./update_files.py:142:80: E501 line too long (95 > 79 characters)
./update_files.py:145:80: E501 line too long (84 > 79 characters)
./update_files.py:155:1: E305 expected 2 blank lines after class or function definition, found 1
./update_files.py:156:11: W292 no newline at end of file

### pylint Report:
************* Module update_files
update_files.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
update_files.py:123:0: C0301: Line too long (120/100) (line-too-long)
update_files.py:156:0: C0304: Final newline missing (missing-final-newline)
update_files.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 9.52/10


### bandit Report:
Run started:2024-06-13 11:24:19.899483

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././update_files.py:5:0
4	
5	import subprocess
6	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ././update_files.py:29:17
28	    try:
29	        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
30	        return result.stdout if result.stdout else result.stderr

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././update_files.py:81:13
80	    """Run flake8 on the given file."""
81	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True, check=True)
82	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././update_files.py:81:13
80	    """Run flake8 on the given file."""
81	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True, check=True)
82	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././update_files.py:87:13
86	    """Run pylint on the given file."""
87	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True, check=True)
88	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././update_files.py:87:13
86	    """Run pylint on the given file."""
87	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True, check=True)
88	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././update_files.py:93:13
92	    """Run bandit on the given file."""
93	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True, check=True)
94	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././update_files.py:93:13
92	    """Run bandit on the given file."""
93	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True, check=True)
94	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------

Code scanned:
	Total lines of code: 116
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


## ./evaluate_repo.py
### flake8 Report:
./evaluate_repo.py:9:80: E501 line too long (96 > 79 characters)
./evaluate_repo.py:42:67: W291 trailing whitespace
./evaluate_repo.py:43:80: E501 line too long (88 > 79 characters)
./evaluate_repo.py:43:89: W291 trailing whitespace
./evaluate_repo.py:51:1: W293 blank line contains whitespace
./evaluate_repo.py:62:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:71:80: E501 line too long (97 > 79 characters)
./evaluate_repo.py:80:80: E501 line too long (103 > 79 characters)
./evaluate_repo.py:95:80: E501 line too long (83 > 79 characters)
./evaluate_repo.py:112:80: E501 line too long (120 > 79 characters)
./evaluate_repo.py:124:80: E501 line too long (91 > 79 characters)
./evaluate_repo.py:126:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:127:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:128:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:129:80: E501 line too long (112 > 79 characters)
./evaluate_repo.py:130:80: E501 line too long (95 > 79 characters)
./evaluate_repo.py:133:80: E501 line too long (84 > 79 characters)
./evaluate_repo.py:143:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:144:11: W292 no newline at end of file

### pylint Report:
************* Module evaluate_repo
evaluate_repo.py:51:0: C0303: Trailing whitespace (trailing-whitespace)
evaluate_repo.py:80:0: C0301: Line too long (103/100) (line-too-long)
evaluate_repo.py:112:0: C0301: Line too long (120/100) (line-too-long)
evaluate_repo.py:144:0: C0304: Final newline missing (missing-final-newline)
evaluate_repo.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 9.37/10


### bandit Report:
Run started:2024-06-13 11:24:21.218843

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././evaluate_repo.py:3:0
2	
3	import subprocess
4	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ././evaluate_repo.py:9:17
8	    try:
9	        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
10	        return result.stdout if result.stdout else result.stderr

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:62:17
61	    try:
62	        result = subprocess.run(['flake8', filepath], capture_output=True, text=True, check=True)
63	        return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:62:17
61	    try:
62	        result = subprocess.run(['flake8', filepath], capture_output=True, text=True, check=True)
63	        return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:71:17
70	    try:
71	        result = subprocess.run(['pylint', filepath], capture_output=True, text=True, check=True)
72	        return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:71:17
70	    try:
71	        result = subprocess.run(['pylint', filepath], capture_output=True, text=True, check=True)
72	        return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:80:17
79	    try:
80	        result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True, check=True)
81	        return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:80:17
79	    try:
80	        result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True, check=True)
81	        return result.stdout if result.stdout else "No issues found by bandit."

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
./backend/site_scraper.py:7:1: E302 expected 2 blank lines, found 1

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 11:24:22.461545

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
Run started:2024-06-13 11:24:23.195294

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
Run started:2024-06-13 11:24:23.987745

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
./backend/single_family_evaluation.py:3:1: E302 expected 2 blank lines, found 1

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 11:24:24.785152

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
./backend/scrape_crexi.py:13:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_crexi
backend/scrape_crexi.py:13:4: E0001: Parsing failed: 'unexpected indent (scrape_crexi, line 13)' (syntax-error)

### bandit Report:
Run started:2024-06-13 11:24:25.530912

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
./backend/multi_family_evaluation.py:3:1: E302 expected 2 blank lines, found 1

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 11:24:26.311409

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
./backend/scrape_zillow.py:21:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module scrape_zillow
backend/scrape_zillow.py:21:4: E0001: Parsing failed: 'unexpected indent (scrape_zillow, line 21)' (syntax-error)

### bandit Report:
Run started:2024-06-13 11:24:27.077173

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
./backend/scrape_zillow_with_langchain.py:10:1: F401 'requests' imported but unused
./backend/scrape_zillow_with_langchain.py:10:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:11:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:12:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:13:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:14:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:16:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:17:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:18:1: E402 module level import not at top of file
./backend/scrape_zillow_with_langchain.py:20:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow_with_langchain.py:40:80: E501 line too long (106 > 79 characters)
./backend/scrape_zillow_with_langchain.py:41:1: W293 blank line contains whitespace
./backend/scrape_zillow_with_langchain.py:58:80: E501 line too long (99 > 79 characters)
./backend/scrape_zillow_with_langchain.py:59:80: E501 line too long (91 > 79 characters)
./backend/scrape_zillow_with_langchain.py:70:1: E302 expected 2 blank lines, found 1
./backend/scrape_zillow_with_langchain.py:75:80: E501 line too long (86 > 79 characters)
./backend/scrape_zillow_with_langchain.py:84:1: E305 expected 2 blank lines after class or function definition, found 1
./backend/scrape_zillow_with_langchain.py:85:80: E501 line too long (94 > 79 characters)

### pylint Report:
************* Module scrape_zillow_with_langchain
backend/scrape_zillow_with_langchain.py:40:0: C0301: Line too long (106/100) (line-too-long)
backend/scrape_zillow_with_langchain.py:41:0: C0303: Trailing whitespace (trailing-whitespace)
backend/scrape_zillow_with_langchain.py:5:0: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:10:0: C0413: Import "import requests" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:11:0: C0413: Import "from bs4 import BeautifulSoup" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:12:0: C0413: Import "from selenium import webdriver" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:13:0: C0413: Import "from selenium.webdriver.chrome.service import Service as ChromeService" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:14:0: C0413: Import "from webdriver_manager.chrome import ChromeDriverManager" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:16:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:17:0: C0413: Import "from langchain.prompts import Prompt" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:18:0: C0413: Import "from llama_index import Document, GPTVectorStoreIndex" should be placed at the top of the module (wrong-import-position)
backend/scrape_zillow_with_langchain.py:18:0: E0611: No name 'Document' in module 'llama_index' (no-name-in-module)
backend/scrape_zillow_with_langchain.py:18:0: E0611: No name 'GPTVectorStoreIndex' in module 'llama_index' (no-name-in-module)
backend/scrape_zillow_with_langchain.py:24:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:30:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:33:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_langchain.py:36:18: W0621: Redefining name 'url' from outer scope (line 85) (redefined-outer-name)
backend/scrape_zillow_with_langchain.py:63:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:66:4: W0105: String statement has no effect (pointless-string-statement)
backend/scrape_zillow_with_langchain.py:20:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backend/scrape_zillow_with_langchain.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
backend/scrape_zillow_with_langchain.py:70:26: W0621: Redefining name 'url' from outer scope (line 85) (redefined-outer-name)
backend/scrape_zillow_with_langchain.py:85:4: C0103: Constant name "url" doesn't conform to UPPER_CASE naming style (invalid-name)
backend/scrape_zillow_with_langchain.py:16:0: C0411: standard import "time" should be placed before third party imports "requests", "bs4.BeautifulSoup", "selenium.webdriver", "selenium.webdriver.chrome.service.Service", "webdriver_manager.chrome.ChromeDriverManager" (wrong-import-order)
backend/scrape_zillow_with_langchain.py:10:0: W0611: Unused import requests (unused-import)

-----------------------------------
Your code has been rated at 2.44/10


### bandit Report:
Run started:2024-06-13 11:24:32.790412

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
./backend/app.py:27:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module app
backend/app.py:27:4: E0001: Parsing failed: 'unexpected indent (app, line 27)' (syntax-error)

### bandit Report:
Run started:2024-06-13 11:24:33.583964

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
./backend/scrape_zillow_with_selenium.py:7:1: E302 expected 2 blank lines, found 1

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 11:24:35.000678

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
./backend/logging_config.py:12:5: E999 IndentationError: unexpected indent

### pylint Report:
************* Module logging_config
backend/logging_config.py:12:4: E0001: Parsing failed: 'unexpected indent (logging_config, line 12)' (syntax-error)

### bandit Report:
Run started:2024-06-13 11:24:35.742507

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
./backend/offer_generator.py:3:1: E302 expected 2 blank lines, found 1

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 11:24:36.516185

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
./backend/server_connection.py:6:1: E302 expected 2 blank lines, found 1

### pylint Report:

------------------------------------
Your code has been rated at 10.00/10


### bandit Report:
Run started:2024-06-13 11:24:38.572295

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
Run started:2024-06-13 11:24:39.276955

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

