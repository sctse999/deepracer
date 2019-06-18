import math

def reward_function(params):
    # initial reward value
    reward = 1

    # Penalize if the car goes off track
    all_wheels_on_track = params['all_wheels_on_track']
    if not all_wheels_on_track:
        reward = 1e-3
        return reward

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    # steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Stay away from the edge of the track pls
    edge_of_track_distance = 0.4 * track_width
    distance_from_center_factor = 1

    if distance_from_center > edge_of_track_distance:
        distance_from_center_factor = 0.5

    # Step 3
    # Calculate the direction of the center line based on the closest waypoints

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert to degree
    track_direction = math.degrees(track_direction)

    is_left_of_center = params['is_left_of_center']
    heading = params['heading']


	# Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

	# Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5


    # if is_left_of_center:
    #     if (heading - track_direction > 5):
    #         # on the left of the track and turn more left than track line, going off track
    #         reward = 1e-3
    #         return reward
    # else:
    #     if (track_direction - heading > 5):
    #         reward = 1e-3
    #         return reward


    # direction_diff = abs(track_direction - heading)
    # HEADING_THRESHOLD_LVL_1 = 10
    # HEADING_THRESHOLD_LVL_2 = 25

    # if (direction_diff < 2 ):
    #     reward *= 100
    # elif (direction_diff > HEADING_THRESHOLD_LVL_1):
    #     reward *= 0.5

    # reward = reward * distance_from_center_factor

    return float(reward)
