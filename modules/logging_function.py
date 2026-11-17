import os
import logging

logger = logging.getLogger(__name__) # attributes logs in function to their own logs

def logging_config(log_dir: str, timestamp: str):
    """Function to configure logging

    Args:
        log_dir (str): where logs are saved
        timestamp (str): timestamp used for naming log file
        log_level (str): level of logging eg. INFO
    """
    # setting up files for logging
    os.makedirs(log_dir,exist_ok=True)
    log_filename = f'{log_dir}/extract_{timestamp}.log' 

    # configuration of log file
    logging.basicConfig(
        filename = log_filename,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO # ignore anything below INFO
    )

    logger = logging.getLogger() # at this point the log is set up but won't create files. need to add these bits in
    logger.info('Logger was succesfully initialised.')