import my_engine.entity as ent
import my_engine.component as cmp


class TransformComponent(cmp.Component):
    def __init__(self, owner: "ent.Entity", component_type: str = "transform") -> None:
        super().__init__(component_type, owner)
        self.position_x = 0.0
        self.position_y = 0.0
        self.rotation_degrees = 0.0
        self.scale_x = 1.0
        self.scale_y = 1.0

    def get_position_x(self):
        return self.position_x

    def get_position_y(self):
        return self.position_y

    def get_rotation_degrees(self):
        return self.rotation_degrees

    def get_scale_x(self):
        return self.scale_x

    def get_scale_y(self):
        return self.scale_y

    # setters
    def set_position_x(self, x_pos: float):
        self.position_x = x_pos

    def set_position_y(self, y_pos: float):
        self.position_y = y_pos

    def set_rotation_degrees(self, rot: float):
        self.rotation_degrees = rot

    def set_scale_x(self, x_scale: float):
        self.scale_x = x_scale

    def set_scale_y(self, y_scale: float):
        self.scale_y = y_scale

