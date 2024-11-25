# mypy: ignore-errors

import rospy
from rviz_camera_manager.handlers.models.cam_service import cam_service
from rviz_camera_manager.handlers.models.camera import Camera
from view_controller_msgs.msg import CameraPlacement

class ROSService:
    """
    ROS管理クラス
    """
    def __init__(self):
        rospy.init_node("camera_manager", anonymous = True)
        self.pub = rospy.Publisher("/rviz/camera_placement", CameraPlacement, queue_size = 1)
        self.sub = rospy.Subscriber("/rviz/current_camera_placement", CameraPlacement, cam_service.updateCurrentCam)

    def get_cam_list(self):
        cam_list = rospy.get_param("/cam_list")
        cams = []
        for obj in cam_list:
            cam = Camera.from_struct(obj)
            cams.append(cam)
        return cams
    
    def set_cam_list(self, cam_list):
        rospy.set_param("/cam_list", cam_list)
ros_service = ROSService()