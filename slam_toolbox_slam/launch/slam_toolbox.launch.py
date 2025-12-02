from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

  slam_toolbox_params_path = os.path.join(
    get_package_share_directory("slam_toolbox_slam") + '/config/slam_toolbox_params.yaml'
    )

  # Path to the Slam Toolbox launch file
  slam_toolbox_launch_path = os.path.join(
    get_package_share_directory('slam_toolbox'),
    'launch',
    'online_async_launch.py'
    )

  slam_toolbox_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(slam_toolbox_launch_path),
    launch_arguments={
      'use_sim_time': 'true',
      'slam_params_file': slam_toolbox_params_path,
      }.items()
      )

  launchDescriptionObject = LaunchDescription()
  launchDescriptionObject.add_action(slam_toolbox_launch)

  return launchDescriptionObject