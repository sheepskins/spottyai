from coder import main as c_main
from coder_reviewer import main as cr_main
from planner_coder_reviewer import main as pcr_main
import pandas as pd
import os
import time

prompt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trial_prompts.csv")
prompts = pd.read_csv(prompt_path, delimiter=',')

for index, row in prompts.iterrows():
    start_c = time.time()
    try:
        c_main(row["prompt"])
    except Exception as e:
        print(e)
    end_c = time.time()
    length_c = end_c - start_c
    input(length_c)
    start_cr = time.time()
    try: 
        cr_main(row["prompt"])
    except Exception as e:
        print(e)
    end_cr = time.time()
    length_cr = end_cr - start_cr
    input(length_cr)
    start_pcr = time.time()
    try: 
        pcr_main(row["prompt"])
    except Exception as e:
        print(e)
    end_pcr = time.time()
    length_pcr = end_pcr - start_pcr
    input(length_pcr)