from coder import main as c_main
from coder_reviewer import main as cr_main
from planner_coder_reviewer import main as pcr_main
import pandas as pd

prompts = pd.read_csv('./trial_prompts.csv')

for index, row in prompts.iterrows():
    try: 
        c_main(row)
    except:
        pass
    input()
    try: 
        cr_main(row)
    except:
        pass
    input()
    try: 
        pcr_main(row)
    except:
        pass
    input()