"""Bots to run the experiment in an automated manner."""
import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dallinger.bots import BotBase

logger = logging.getLogger(__file__)


class Bot(BotBase):
    """Bot tasks for experiment participation."""

    def participate(self):
        """Click the button."""
        try:
            logger.info("Entering participate method")
            submit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'submit-response')))
            submit.click()
            return True
        except TimeoutException:
            return False
