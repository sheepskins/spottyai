from ai import detect, move_to, say, ask, pose
import rospy
import time

rospy.init_node('SPOTTYAI')

# Ask all users if they are ready
if ask("Am I ready to start a 30 second solo salsa dance?") == "yes":
    # Inform user of intent 
    say("Starting a 30 second solo salsa dance")
    # Start timer
    start_time = rospy.get_time()

    # Basic salsa move 1 - front and back
    for cycle in range(3):
        pose(10, 0, 0, 0)  # Move body forward
        time.sleep(0.5)  # Hold pose for a beat
        pose(-10, 0, 0, 0)  # Move body backward
        time.sleep(0.5)  # Hold pose for a beat
        # Pause after three steps
        time.sleep(1)

    # Pause between moves for music transition
    time.sleep(1)

    # Basic salsa move 2 - side step
    for cycle in range(3):
        pose(0, 10, 0, 0)  # Move body left
        time.sleep(0.5)  # Hold pose for a beat
        pose(0, -10, 0, 0)  # Move body right
        time.sleep(0.5)  # Hold pose for a beat
        # Pause after three steps
        time.sleep(1)

    # Pause between moves for music transition
    time.sleep(1)

    # Basic salsa move 3 - body roll
    pose(10, 10, 0, 0)  # Rotate body diagonally
    time.sleep(0.5)  # Hold pose for a beat
    pose(-10, -10, 0, 0)  # Rotate body opposite diagonally
    time.sleep(0.5)  # Hold pose for a beat
else:
    say("Waiting for all users to be ready")

# Ensure the routine is only 30 seconds long.
if rospy.get_time() - start_time < 30:
    time.sleep(30 - (rospy.get_time() - start_time))

# Inform users the dance has ended
say("Finished salsa dance!")