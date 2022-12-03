from FollowerBot import FollowerBot

robot = FollowerBot()

robot.set_wheels_speed(30)
robot.sleep(6)
robot.set_wheels_speed(0)
robot.done()