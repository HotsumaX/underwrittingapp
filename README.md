# Progress Report

## ./improve_project.py
### flake8 Report:
./improve_project.py:3:1: E302 expected 2 blank lines, found 1
./improve_project.py:8:1: E305 expected 2 blank lines after class or function definition, found 1
./improve_project.py:36:53: W292 no newline at end of file

### pylint Report:
************* Module improve_project
improve_project.py:36:0: C0304: Final newline missing (missing-final-newline)
improve_project.py:1:0: C0114: Missing module docstring (missing-module-docstring)
improve_project.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
improve_project.py:4:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)

-----------------------------------
Your code has been rated at 8.26/10


### bandit Report:
Run started:2024-06-12 23:52:23.313699

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././improve_project.py:1:0
1	import subprocess
2	
3	def run_command(command):

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././improve_project.py:4:13
3	def run_command(command):
4	    result = subprocess.run(command, capture_output=True, text=True)
5	    return result.stdout if result.stdout else result.stderr

--------------------------------------------------

Code scanned:
	Total lines of code: 23
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


## ./update_files_v4.py
### flake8 Report:
./update_files_v4.py:1:1: F401 'os' imported but unused
./update_files_v4.py:14:80: E501 line too long (87 > 79 characters)
./update_files_v4.py:16:80: E501 line too long (100 > 79 characters)
./update_files_v4.py:17:80: E501 line too long (103 > 79 characters)
./update_files_v4.py:18:80: E501 line too long (101 > 79 characters)
./update_files_v4.py:19:80: E501 line too long (84 > 79 characters)
./update_files_v4.py:23:1: E302 expected 2 blank lines, found 1
./update_files_v4.py:26:80: E501 line too long (116 > 79 characters)
./update_files_v4.py:27:1: E302 expected 2 blank lines, found 1
./update_files_v4.py:35:80: E501 line too long (84 > 79 characters)
./update_files_v4.py:39:80: E501 line too long (108 > 79 characters)
./update_files_v4.py:47:80: E501 line too long (99 > 79 characters)
./update_files_v4.py:62:1: E302 expected 2 blank lines, found 1
./update_files_v4.py:75:80: E501 line too long (84 > 79 characters)
./update_files_v4.py:80:1: E302 expected 2 blank lines, found 1
./update_files_v4.py:83:1: E305 expected 2 blank lines after class or function definition, found 1
./update_files_v4.py:87:26: W292 no newline at end of file

### pylint Report:
************* Module update_files_v4
update_files_v4.py:17:0: C0301: Line too long (103/100) (line-too-long)
update_files_v4.py:18:0: C0301: Line too long (101/100) (line-too-long)
update_files_v4.py:26:0: C0301: Line too long (116/100) (line-too-long)
update_files_v4.py:39:0: C0301: Line too long (108/100) (line-too-long)
update_files_v4.py:87:0: C0304: Final newline missing (missing-final-newline)
update_files_v4.py:1:0: C0114: Missing module docstring (missing-module-docstring)
update_files_v4.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
update_files_v4.py:24:4: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
update_files_v4.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
update_files_v4.py:29:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
update_files_v4.py:57:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
update_files_v4.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
update_files_v4.py:64:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
update_files_v4.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
update_files_v4.py:81:4: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
update_files_v4.py:1:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 6.80/10


### bandit Report:
Run started:2024-06-12 23:52:24.397353

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././update_files_v4.py:2:0
1	import os
2	import subprocess
3	

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././update_files_v4.py:24:4
23	def install_packages():
24	    subprocess.run(["pip", "install", "requests", "selenium"])
25	

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././update_files_v4.py:24:4
23	def install_packages():
24	    subprocess.run(["pip", "install", "requests", "selenium"])
25	

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././update_files_v4.py:81:4
80	def run_improve_project():
81	    subprocess.run(["python3", "improve_project.py"])
82	

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././update_files_v4.py:81:4
80	def run_improve_project():
81	    subprocess.run(["python3", "improve_project.py"])
82	

--------------------------------------------------

Code scanned:
	Total lines of code: 67
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 5
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 5
Files skipped (0):


## ./evaluate_repo.py
### flake8 Report:
./evaluate_repo.py:3:1: F401 're' imported but unused
./evaluate_repo.py:4:1: F811 redefinition of unused 'subprocess' from line 2
./evaluate_repo.py:5:1: F811 redefinition of unused 'os' from line 1
./evaluate_repo.py:7:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:8:80: E501 line too long (80 > 79 characters)
./evaluate_repo.py:11:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:19:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:31:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:33:67: W291 trailing whitespace
./evaluate_repo.py:34:80: E501 line too long (88 > 79 characters)
./evaluate_repo.py:34:89: W291 trailing whitespace
./evaluate_repo.py:42:1: W293 blank line contains whitespace
./evaluate_repo.py:49:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:51:1: E302 expected 2 blank lines, found 0
./evaluate_repo.py:52:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:55:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:56:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:59:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:60:80: E501 line too long (87 > 79 characters)
./evaluate_repo.py:63:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:71:80: E501 line too long (83 > 79 characters)
./evaluate_repo.py:74:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:83:1: E302 expected 2 blank lines, found 1
./evaluate_repo.py:84:80: E501 line too long (120 > 79 characters)
./evaluate_repo.py:96:80: E501 line too long (91 > 79 characters)
./evaluate_repo.py:98:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:99:80: E501 line too long (81 > 79 characters)
./evaluate_repo.py:100:80: E501 line too long (109 > 79 characters)
./evaluate_repo.py:101:80: E501 line too long (112 > 79 characters)
./evaluate_repo.py:102:80: E501 line too long (95 > 79 characters)
./evaluate_repo.py:105:80: E501 line too long (84 > 79 characters)
./evaluate_repo.py:115:1: E305 expected 2 blank lines after class or function definition, found 1
./evaluate_repo.py:116:11: W292 no newline at end of file

### pylint Report:
************* Module evaluate_repo
evaluate_repo.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
evaluate_repo.py:84:0: C0301: Line too long (120/100) (line-too-long)
evaluate_repo.py:116:0: C0304: Final newline missing (missing-final-newline)
evaluate_repo.py:1:0: C0114: Missing module docstring (missing-module-docstring)
evaluate_repo.py:4:0: W0404: Reimport 'subprocess' (imported line 2) (reimported)
evaluate_repo.py:5:0: W0404: Reimport 'os' (imported line 1) (reimported)
evaluate_repo.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:8:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:45:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:52:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:56:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:60:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
evaluate_repo.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
evaluate_repo.py:88:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:112:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
evaluate_repo.py:4:0: C0412: Imports from package subprocess are not grouped (ungrouped-imports)
evaluate_repo.py:5:0: C0412: Imports from package os are not grouped (ungrouped-imports)
evaluate_repo.py:3:0: W0611: Unused import re (unused-import)

-----------------------------------
Your code has been rated at 6.39/10


### bandit Report:
Run started:2024-06-12 23:52:25.779643

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
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: ././evaluate_repo.py:4:0
3	import re
4	import subprocess
5	import os

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ././evaluate_repo.py:8:13
7	def run_command(command):
8	    result = subprocess.run(command, capture_output=True, text=True, shell=True)
9	    return result.stdout if result.stdout else result.stderr

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:52:13
51	def run_flake8(filepath):
52	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
53	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:52:13
51	def run_flake8(filepath):
52	    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
53	    return result.stdout if result.stdout else "No issues found by flake8."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:56:13
55	def run_pylint(filepath):
56	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
57	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:56:13
55	def run_pylint(filepath):
56	    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
57	    return result.stdout if result.stdout else "No issues found by pylint."

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b607_start_process_with_partial_path.html
   Location: ././evaluate_repo.py:60:13
59	def run_bandit(filepath):
60	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
61	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/plugins/b603_subprocess_without_shell_equals_true.html
   Location: ././evaluate_repo.py:60:13
59	def run_bandit(filepath):
60	    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
61	    return result.stdout if result.stdout else "No issues found by bandit."

--------------------------------------------------

Code scanned:
	Total lines of code: 92
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 8
		Medium: 0
		High: 1
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 9
Files skipped (0):


## ./backend/site_scraper.py
### flake8 Report:
./backend/site_scraper.py:8:1: E303 too many blank lines (3)

### pylint Report:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


### bandit Report:
Run started:2024-06-12 23:52:26.967532

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
Run started:2024-06-12 23:52:27.636028

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
Run started:2024-06-12 23:52:28.291848

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
./backend/single_family_evaluation.py:5:1: E303 too many blank lines (3)

### pylint Report:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


### bandit Report:
Run started:2024-06-12 23:52:28.945902

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
Run started:2024-06-12 23:52:29.597928

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
./backend/multi_family_evaluation.py:5:1: E303 too many blank lines (3)

### pylint Report:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


### bandit Report:
Run started:2024-06-12 23:52:30.249631

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
Run started:2024-06-12 23:52:30.909043

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
Run started:2024-06-12 23:52:35.507632

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
Run started:2024-06-12 23:52:36.166487

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
./backend/scrape_zillow_with_selenium.py:8:1: E303 too many blank lines (3)

### pylint Report:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


### bandit Report:
Run started:2024-06-12 23:52:37.281237

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
Run started:2024-06-12 23:52:37.934527

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
./backend/offer_generator.py:5:1: E303 too many blank lines (3)

### pylint Report:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


### bandit Report:
Run started:2024-06-12 23:52:38.586242

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
./backend/server_connection.py:7:1: E303 too many blank lines (3)

### pylint Report:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


### bandit Report:
Run started:2024-06-12 23:52:40.162746

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
Run started:2024-06-12 23:52:40.811433

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

