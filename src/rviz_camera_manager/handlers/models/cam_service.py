from typing import List
from rviz_camera_manager.handlers.models.camera import Camera
from view_controller_msgs.msg import CameraPlacement

class CameraService:
    def __init__(self):
        self.cams = []
        self.currentCp = CameraPlacement()
        self.isAutosave = True

    ### Camera Data CRUD ###
    def getCam(self, camKey):
        index = find_first_index(self.cams, "key", camKey)
        if index is None:
            return None
        return self.cams[index]

    def addCam(self, cam: Camera):
        self.cams.append(cam)

        self.autosave()
        return cam

    def updateCam(self, cam: Camera):
        index = find_first_index(self.cams, "key", cam.key)
        self.cams[index] = cam

        self.autosave()
        return self.cams[index]

    def removeCam(self, camKey):
        index = find_first_index(self.cams, "key", camKey)

        if index is None:
            print("[CA] Failed to remove Camera record; key not found.")
            return

        self.cams.pop(index)
        self.autosave()
        return

    def loadCams(self, cams: List[Camera]):
        self.cams = cams

    def getCamLabels(self):
        labelCams = filter(lambda cam: cam.isLabel is True, self.cams)
        labelDict = [{ "key": cam.key, "label": cam.label } for cam in labelCams ]
        return labelDict

    def autosave(self):
        if self.isAutosave:
            pass

    ### Current Camera Placement ###
    def updateCurrentCam(self, cp: CameraPlacement):
        self.cp = cp


def find_first_index(lst, key, value):
    """
    条件に合致する最初の要素のインデックスを見つける

    Parameters
    ----------
    lst : list
        検索対象のリスト
    key : str
        検索するキー
    value : str
        検索する値

    Returns
    -------
    int
        インデックス
    """
    for index, item in enumerate(lst):
        if item[key] == value:
            return index
    return None

cam_service = CameraService()