""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    all_out = get_shutdown_events(logfile)
    
    all_out0 = all_out[0]
    
    all_out1 = all_out[-1]
       
    all_out11 = logstamp_to_datetime(all_out0.split()[1])
    
    all_out12 = logstamp_to_datetime(all_out1.split()[1])
    
    final_all_out = all_out12-all_out11
    
    return final_all_out


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
