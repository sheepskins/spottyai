from coder import main as c_main
from coder_reviewer import main as cr_main
from planner_coder_reviewer import main as pcr_main
import pandas as pd
import os
import time

# Show the results : this can be altered however you like
print("It took", length, "seconds!")



prompt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trial_prompts.csv")
prompts = pd.read_csv(prompt_path, delimiter=',')

for index, row in prompts.iterrows():
    try:
        start = time.time()
        c_main(row["prompt"])
        end = time.time()
        length = end - start 
    except:
        pass
    input(length)
    try: 
        start = time.time()
        cr_main(row["prompt"])
        end = time.time()
        length = end - start
    except:
        pass
    input(length)
    try: 
        start = time.time()
        pcr_main(row["prompt"])
        end = time.time()
        length = end - start
    except:
        pass
    input(length)