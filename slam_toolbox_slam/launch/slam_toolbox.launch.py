from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

  localization_params_path = os.path.join(
    get_package_share_directory("slam_toolbox_slam") + '/config/slam_toolbox_params.yaml'
    )

  # Path to the Slam Toolbox launch file
  nav2_localization_launch_path = os.path.join(
    get_package_share_directory('slam_toolbox'),
    'launch',
    'online_async_launch.py'
    )

  localization_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(nav2_localization_launch_path),
    launch_arguments={
      'use_sim_time': 'true',
      'slam_params_file': localization_params_path,
      }.items()
      )

  launchDescriptionObject = LaunchDescription()
  launchDescriptionObject.add_action(localization_launch)

  return launchDescriptionObject