'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 0.60612, "gpt-4-0613": {"cost": 0.60612, "prompt_tokens": 18290, "completion_tokens": 957, "total_tokens": 19247}}, "usage_excluding_cached_inference": {"total_cost": 0.60612, "gpt-4-0613": {"cost": 0.60612, "prompt_tokens": 18290, "completion_tokens": 957, "total_tokens": 19247}}}'''
from ai import detect, move_to, say, ask, pose
import rospy
import time

rospy.init_node('SPOTTYAI')

# First, let the user know that we are seeking help
say("Don't worry, I'm getting help.")

while True:
    # Detect if there is any person nearby who could possibly help
    person_df = detect('person')

    # If a person is found, move towards them
    if isinstance(person_df, pd.DataFrame) and not person_df.empty:
        say("I see a person nearby, I'm going to get them for help.")
        # Move towards the person by moving to their x and y coordinates in the robot's frame of reference
        # We pick the first person detected for simplicity
        move_to(person_df.iloc[0]['x'], person_df.iloc[0]['y'])
        break
    else:
        say("I couldn't find anyone nearby. Continuously searching...")
        time.sleep(1)  # Wait for a second before trying again to not overwhelm the detection system

say("Do you have a phone?")
response = ask("Do you have a phone?")
if response.lower() == "yes":
    say("Excellent. Please call emergency services.")
else:
    say("Stay calm while I continue to search for someone to help.")
