import logging
import datetime

class AppLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format='%(message)s'
        )
    
    def log_user_action(self, user_id, action, details):
        message = f"{datetime.datetime.now()} - User {user_id} performed {action}: {details}"
        logging.info(message)
    
    def log_error(self, error, context):
        message = f"ERROR: {error} - Context: {context}"
        logging.error(message)
    
    def log_api_request(self, endpoint, params, headers):
        message = f"API Request to {endpoint} with params {params} and headers {headers}"
        logging.debug(message)