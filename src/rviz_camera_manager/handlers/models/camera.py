from view_controller_msgs.msg import CameraPlacement

class Camera(dict):
    def __init__(self, parentKey: str, key: str, label: str, cp: CameraPlacement, isLabel = False):
        super().__init__()
        self.__dict__ = self
        self.parentKey = parentKey
        self.key = key
        self.label = label
        self.isLabel = isLabel
        
        self.cp = cp
    
    def from_struct(self, struct):
        self.parentKey = struct["parentKey"]
        self.key = struct["key"]
        self.label = struct["label"]
        self.isLabel = struct["isLabel"]
        cp = CameraPlacement()

        cp.interpolation_mode = struct["camera_placement"]["interpolation_mode"]
        cp.target_frame = struct["camera_placement"]["target_frame"]
        cp.time_from_start.secs = struct["camera_placement"]["time_from_start"]["secs"]
        cp.time_from_start.nsecs = struct["camera_placement"]["time_from_start"]["nsecs"]
        cp.eye.header.seq = struct["camera_placement"]["eye"]["header"]["seq"]
        cp.eye.header.stamp.secs = struct["camera_placement"]["eye"]["header"]["stamp"]["secs"]
        cp.eye.header.stamp.nsecs = struct["camera_placement"]["eye"]["header"]["stamp"]["nsecs"]
        cp.eye.header.frame_id = struct["camera_placement"]["eye"]["header"]["frame_id"]
        cp.eye.point.x = struct["camera_placement"]["eye"]["point"]["x"]
        cp.eye.point.y = struct["camera_placement"]["eye"]["point"]["y"]
        cp.eye.point.z = struct["camera_placement"]["eye"]["point"]["z"]
        cp.focus.header.seq = struct["camera_placement"]["focus"]["header"]["seq"]
        cp.focus.header.stamp.secs = struct["camera_placement"]["focus"]["header"]["stamp"]["secs"]
        cp.focus.header.stamp.nsecs = struct["camera_placement"]["focus"]["header"]["stamp"]["nsecs"]
        cp.focus.header.frame_id = struct["camera_placement"]["focus"]["header"]["frame_id"]
        cp.focus.point.x = struct["camera_placement"]["focus"]["point"]["x"]
        cp.focus.point.y = struct["camera_placement"]["focus"]["point"]["y"]
        cp.focus.point.z = struct["camera_placement"]["focus"]["point"]["z"]
        cp.up.header.seq = struct["camera_placement"]["up"]["header"]["seq"]
        cp.up.header.stamp.secs = struct["camera_placement"]["up"]["header"]["stamp"]["secs"]
        cp.up.header.stamp.nsecs = struct["camera_placement"]["up"]["header"]["stamp"]["nsecs"]
        cp.up.header.frame_id = struct["camera_placement"]["up"]["header"]["frame_id"]
        cp.up.vector.x = struct["camera_placement"]["up"]["vector"]["x"]
        cp.up.vector.y = struct["camera_placement"]["up"]["vector"]["y"]
        cp.up.vector.z = struct["camera_placement"]["up"]["vector"]["z"]
        cp.mouse_interaction_mode = struct["camera_placement"]["mouse_interaction_mode"]
        cp.interaction_disabled = struct["camera_placement"]["interaction_disabled"]
        cp.allow_free_yaw_axis = struct["camera_placement"]["allow_free_yaw_axis"]

        self.cp = cp
        
        return self

    def to_struct(self):
        cam = self
        data = {
            "parentKey" : cam.parentKey,
            "key": cam.key,
            "label": cam.label,
            "isLabel": cam.isLabel,

            # CameraPlacementをそのまま保存
            "camera_placement": {
                "interpolation_mode": cam.cp.interpolation_mode,
                "target_frame": cam.cp.target_frame,
                "time_from_start": {
                    "secs": cam.cp.time_from_start.secs,
                    "nsecs": cam.cp.time_from_start.nsecs
                },
                "eye": {
                    "header": {
                        "seq": cam.cp.eye.header.seq,
                        "stamp": {
                            "secs": cam.cp.eye.header.stamp.secs,
                            "nsecs": cam.cp.eye.header.stamp.nsecs
                        },
                        "frame_id": cam.cp.eye.header.frame_id
                    },
                    "point": {
                        "x": cam.cp.eye.point.x,
                        "y": cam.cp.eye.point.y,
                        "z": cam.cp.eye.point.z,
                    },
                },
                "focus": {
                    "header": {
                        "seq": cam.cp.focus.header.seq,
                        "stamp": {
                            "secs": cam.cp.focus.header.stamp.secs,
                            "nsecs": cam.cp.focus.header.stamp.nsecs
                        },
                        "frame_id": cam.cp.focus.header.frame_id
                    },
                    "point": {
                        "x": cam.cp.focus.point.x,
                        "y": cam.cp.focus.point.y,
                        "z": cam.cp.focus.point.z,
                    },
                },
                "up": {
                    "header": {
                        "seq": cam.cp.up.header.seq,
                        "stamp": {
                            "secs": cam.cp.up.header.stamp.secs,
                            "nsecs": cam.cp.up.header.stamp.nsecs
                        },
                        "frame_id": cam.cp.up.header.frame_id
                    },
                    "vector": {
                        "x": cam.cp.up.vector.x,
                        "y": cam.cp.up.vector.y,
                        "z": cam.cp.up.vector.z,
                    },
                },
                "mouse_interaction_mode": cam.cp.mouse_interaction_mode,
                "interaction_disabled": cam.cp.interaction_disabled,
                "allow_free_yaw_axis": cam.cp.allow_free_yaw_axis
            }
        }
        return data