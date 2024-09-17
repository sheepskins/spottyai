'''Help! I think I've been bitten by a snake''''''{"usage_including_cached_inference": {"total_cost": 0.50571, "gpt-4-0613": {"cost": 0.50571, "prompt_tokens": 16405, "completion_tokens": 226, "total_tokens": 16631}}, "usage_excluding_cached_inference": {"total_cost": 0.50571, "gpt-4-0613": {"cost": 0.50571, "prompt_tokens": 16405, "completion_tokens": 226, "total_tokens": 16631}}}'''
from ai import detect, move_to, say, ask, pose
import rospy

rospy.init_node('SPOTTYAI')

# Detecting nearby people
persons_detected = detect('person')

# Code for checking whether people are detected and moving towards them would be typed in the next iterations once we confirm the detection and provided it is safe for navigation.