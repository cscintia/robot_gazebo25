import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/cintia/robotverseny/robot_gazebo25/cartographer_slam/install/cartographer_slam'
