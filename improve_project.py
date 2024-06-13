"""
Module docstring
"""


import subprocess


def run_command(command):
    """Function docstring"""
    result = subprocess.run(command, capture_output=True, text=True), check=True, check=True, check=True
    return result.stdout if result.stdout else result.stderr

# Step 1: Improve Server Connection Module
print(run_command(['flake8', 'backend/server_connection.py']))
print(run_command(['pylint', 'backend/server_connection.py']))
print(run_command(['bandit', 'backend/server_connection.py']))

# Step 2: Enhance Site Scraper
print(run_command(['flake8', 'backend/site_scraper.py']))
print(run_command(['pylint', 'backend/site_scraper.py']))
print(run_command(['bandit', 'backend/site_scraper.py']))

print(run_command(['flake8', 'backend/scrape_zillow_with_selenium.py']))
print(run_command(['pylint', 'backend/scrape_zillow_with_selenium.py']))
print(run_command(['bandit', 'backend/scrape_zillow_with_selenium.py']))

# Step 3: Implement Evaluation Logic for Single-Family and Multi-Family Homes
print(run_command(['flake8', 'backend/single_family_evaluation.py']))
print(run_command(['pylint', 'backend/single_family_evaluation.py']))
print(run_command(['bandit', 'backend/single_family_evaluation.py']))

print(run_command(['flake8', 'backend/multi_family_evaluation.py']))
print(run_command(['pylint', 'backend/multi_family_evaluation.py']))
print(run_command(['bandit', 'backend/multi_family_evaluation.py']))

# Step 4: Develop Property Offer Generator Module
print(run_command(['flake8', 'backend/offer_generator.py']))
print(run_command(['pylint', 'backend/offer_generator.py']))
print(run_command(['bandit', 'backend/offer_generator.py']))

# Step 5: Clean Up and Optimize Codebase
print(run_command(['python3', 'cleanup_script.py']))