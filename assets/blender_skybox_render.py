import math
from pathlib import Path

import bpy

# lots of this code was just yoinked from my Spyro skyboxes project
# https://github.com/spacehare/spyro-blender/tree/main

#           FORWARD     RIGHT   UP
# BLENDER   +Y          +X      +Z
# QUAKE     +X          -Y      +Z

BLENDER_FORWARD = (90, 0, 0)
BLENDER_RIGHT = (90, 0, 270)
BLENDER_UP = (180, 0, 0)
BLENDER_BACK = (90, 0, 180)
BLENDER_LEFT = (90, 0, 90)
BLENDER_DOWN = (0, 0, 0)

QUAKE_FORWARD = BLENDER_RIGHT
QUAKE_RIGHT = BLENDER_FORWARD
QUAKE_UP = BLENDER_UP
QUAKE_BACK = BLENDER_LEFT
QUAKE_LEFT = BLENDER_BACK
QUAKE_DOWN = BLENDER_DOWN

rotations = {
    "ft": QUAKE_FORWARD,
    "rt": QUAKE_RIGHT,
    "bk": QUAKE_BACK,
    "lf": QUAKE_LEFT,
    "up": QUAKE_UP,
    "dn": QUAKE_DOWN,
}
scene_camera = bpy.context.scene.camera
output_path = Path.home() / Path(r"example/stem")
resolution = 1024


def setup():
    bpy.context.scene.render.image_settings.file_format = "TARGA"
    camera = bpy.context.scene.camera
    camera.rotation_mode = "XYZ"
    camera.data.lens = 18  # 90 FOV
    camera.data.clip_end = 10000
    camera.hide_select = True


def rotate(what, vector):
    what.rotation_euler.x = math.radians(vector[0])
    what.rotation_euler.y = math.radians(vector[1])
    what.rotation_euler.z = math.radians(vector[2])


def render(output_file_path: Path, xy: int):
    bpy.context.scene.render.resolution_x = xy
    bpy.context.scene.render.resolution_y = xy
    bpy.context.scene.render.filepath = str(output_file_path)
    bpy.ops.render.render(write_still=True)


def render_skybox(file_path: Path, camera, resolution: int):
    print(f"{resolution}x{resolution}", file_path)

    for direction, vector in rotations.items():
        item_path = file_path.with_stem(f"{file_path.stem}_{direction}")
        rotate(camera, vector)
        render(item_path, resolution)


setup()
render_skybox(output_path, scene_camera, resolution)
