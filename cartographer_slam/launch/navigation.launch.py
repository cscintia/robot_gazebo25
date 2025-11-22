import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch_ros.actions import SetRemap
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from pathlib import Path


def generate_launch_description():
    # Positioning function pack
    pkg_share = FindPackageShare(package='cartographer_slam').find('cartographer_slam')
    
    # Configure node launch information 
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    # Configuration file folder path
    configuration_directory = LaunchConfiguration('configuration_directory',default= os.path.join(pkg_share, 'config') )
    # Configuration file
    configuration_basename = LaunchConfiguration('configuration_basename', default='navigation.yaml')

    # Nodes
    # Navigation

    navigation_node = GroupAction(
        actions=[
            # TODO: enable when navigation2 supports twist stamped
            # SetRemap(src="/cmd_vel", dst="/ap/cmd_vel"),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    str(
                        Path(
                            FindPackageShare("nav2_bringup").find("nav2_bringup"),
                            "launch",
                            "navigation_launch.py",
                        )
                    )
                ),
                launch_arguments={
                    "use_sim_time": "true",
                    "params_file": FindPackageShare("cartographer_slam").find(
                        "cartographer_slam"
                    )
                    + "/config"
                    + "/navigation.yaml",
                }.items(),
            ),
        ]
    )

    #Launch file
    ld = LaunchDescription()
    ld.add_action(navigation_node)

    return ld
