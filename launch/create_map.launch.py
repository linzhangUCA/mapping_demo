from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    gazebo_package_path = get_package_share_path("gazebo_demo")

    launch_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [str(gazebo_package_path / "launch/simulate_bot.launch.py")]
        )
    )

    return LaunchDescription(
        [
            launch_gazebo,
        ]
    )
