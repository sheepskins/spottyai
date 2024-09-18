'''Help! I think I've been bitten by a snake.''''''{"usage_including_cached_inference": {"total_cost": 1.4441999999999997, "gpt-4-0613": {"cost": 1.4441999999999997, "prompt_tokens": 43732, "completion_tokens": 2204, "total_tokens": 45936}}, "usage_excluding_cached_inference": {"total_cost": 1.4441999999999997, "gpt-4-0613": {"cost": 1.4441999999999997, "prompt_tokens": 43732, "completion_tokens": 2204, "total_tokens": 45936}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Inform the user that we are checking the environment for danger
say("We are checking your surroundings for any danger. Please wait...")

# Detect objects in immediate surrounding from the full range of categories
detection_result = detect('person,bicycle,car,motorcycle,airplane,bus,train,truck,boat,traffic light,fire hydrant,stop sign,parking meter,bench,bird,cat,dog,horse,sheep,cow,elephant,bear,zebra,giraffe,backpack,umbrella,handbag,tie,suitcase,frisbee,skis,snowboard,sports ball,kite,baseball bat,baseball glove,skateboard,surfboard,tennis racket,bottle,wine glass,cup,fork,knife,spoon,bowl,banana,apple,sandwich,orange,broccoli,carrot,hot dog,pizza,donut,cake,chair,couch,potted plant,bed,dining table,toilet,tv,laptop,mouse,remote,keyboard,cell phone,microwave,oven,toaster,sink,refrigerator,book,clock,vase,scissors,teddy bear,hair drier,toothbrush')

if isinstance(detection_result, pd.DataFrame):
    # If there are objects detected, move the user away from the objects
    for i, (x, y, id_, label) in detection_result.iterrows():
        # We are avoiding the object by moving to the opposite direction
        move_to(-x, -y)

# Ask the user if they can call the emergency services
can_call = ask("Can you call the emergency services? Please respond with yes or no.").lower()

if can_call == "no":
    # We must ask for help from surrounding people
    say("Help! The user has been bitten by a snake and cannot call for help. Please call the emergency services.")
elif can_call == "yes":
    # If user can call, instruct them to do so
    say("Please call the emergency services immediately and tell them you have been bitten by a snake.")
else:
    say("I didn't understand your response. Please respond with either 'yes' or 'no'.")

# Confirm whether or not they are able to move 
can_move = ask("Are you able to move? Please respond with yes or no. Try to stay as still as possible. The venom can spread faster with movement.").lower()

if can_move == "yes":
    # If user can move away from potential snake, instruct them to do so slowly
    say("If safe, slowly move away from the location of the snake bite.")
elif can_move == "no":
    # If user is unable to move, inform them that help is on the way
    say("Okay, try not to panic. Help is on the way, and they have been informed that you can't move.")
else:
    say("I didn't understand your response. Please respond with either 'yes' or 'no'.")