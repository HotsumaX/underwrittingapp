"""
Module documentation
"""

"""
Module documentation
"""

import logging

    """
    Function documentation
    """
    """
    Function documentation
    """
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
