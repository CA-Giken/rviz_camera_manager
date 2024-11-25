# mypy: ignore-errors

import eel

from rviz_camera_manager.handlers.models.camera import Camera
from rviz_camera_manager.handlers.models.cam_service import cam_service, find_first_index
from rviz_camera_manager.handlers.models.ros_service import ros_service
from view_controller_msgs.msg import CameraPlacement
import os
import yaml
from uuid import uuid4

@eel.expose
def selectCamera(camKey: str):
    index = find_first_index(cam_service.cams, "key", camKey)
    if index is None:
        print("[CA] Failed to select Camera; key not found.")
        return

    cam = cam_service.cams[index]
    if cam.isLabel is True:
        return

    print(f"[CA] Camera selected: {cam.key};{cam.label}")
    ros_service.pub.publish(cam.cp)
    return cam

@eel.expose
def loadCamsFromRosparam():
    cam_list = ros_service.get_cam_list()
    cam_service.loadCams(cam_list)

@eel.expose
def saveCams(self, filename: str = "rviz_camera_manager"):
    cam_list = [
        cam.to_struct()
        for cam in cam_service.cams
    ]
    ros_service.set_cam_list(cam_list)


    # homeディレクトリのyamlに書き出し
    # ホームディレクトリのパスを取得
    home_directory = os.path.expanduser('~')
    # ファイル名をホームディレクトリのパスに結合
    filename = os.path.join(home_directory, f"{filename}.yaml")
    yf=open(filename,"w")
    yaml.dump({ "cam_list": cam_list } ,yf,default_flow_style=False)


@eel.expose
def addCam():
    cam = Camera(
        parentKey = "",
        key = uuid4(),
        label = "New Camera",
        cp = CameraPlacement(),
        isLabel = False
    )
    cam_service.addCam(cam)