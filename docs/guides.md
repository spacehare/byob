# Tools

| Hyperlink                                                                                 | Purpose                          |
| ----------------------------------------------------------------------------------------- | -------------------------------- |
| [Krita](https://krita.org)                                                                | Creating textures                |
| [Material Maker](https://www.materialmaker.org/)                                          | Creating textures                |
| [Blender](https://www.blender.org/)                                                       | Creating textures                |
| [Wally 157](https://github.com/Ty-Matthews-VisualStudio/Wally)                            | Creating textures, packing WADs  |
| [qpakman 062b](https://www.quaddicted.com/files/tools/qpakman-062b.zip) (direct download) | packing WADs                     |
| [q1tools](https://q1tools.github.io/)                                                     | File conversion (ex: PNG -> TGA) |
| [ImageMagick](https://imagemagick.org/)                                                   | File conversion (ex: PNG -> TGA) |
| [IrfanView](https://www.irfanview.com/)                                                   | File conversion (ex: PNG -> TGA) |

- https://github.com/LibreSprite/LibreSprite (Tei)
- https://captain4lk.itch.io/slk-img2pixel (Ashat Maself)
  - https://github.com/Captain4LK/SoftLK-tools
- https://www.slipseer.com/index.php?resources/error-diffused-quake-palettte-colour-lookup-tables-for-used-with-substance-designer-painter.156/

# Example CLI tool usage

## qpakman

```shell
qpakman textures/*.png -o textures.wad
```

## IrfanView

```shell
"C:\Program Files (x86)\IrfanView\i_view32.exe" INPUTFOLDER\*.png /convert=OUTPUTFOLDER\*.tga
```

## ImageMagick

```shell
magick mogrify -path example/folder -format tga files/*.png
```

# Guides

## qpakman

make sure to read the manual! RTFM!

My workflow is to have a folder full of PNG files with proper filenames

- suffix: `_fbr`, to allow fullbright colors to be used
- prefix: `star_` = `*` -- for liquids, because `*` is an invalid file name on Windows.
- prefix: `plus_` = `+` -- for animated textures
- prefix: `minu_` = `-`
- prefix: `divd_` = `/`

## Krita

- Create a new file
- For tiling textures, enable Wrap-Around mode (SHIFT+W)
- add a paint layer (ALT+L; N; P)
- Load the quake palette in the Palette dock (ALT+N; D; Select "Palette")
  - Click the little palette button
  - Click the left-facing arrow icon, "Import new palette from file"
- add a filter layer (ALT+L; N; F)
  - Map -> Palettize. tweak the settings until it looks good to you
  - You can hit F3 to edit the currently selected layer's settings
- Save your `.kra` file (CTRL+S)
- File -> Export (ALT+F; X)
  - export as PNG into a folder with all your textures
  - disable "Store alpha channel" (ALT+R)
    - set the "Transparent color" to hex `#9f5b53` or RGB `159, 91, 83` (palette index 255)

## Material Maker

Add nodes by right-clicking. Connect sockets by left-click dragging.

- Create a new file
- Save your file
- Add: Noise (such as Clouds or Voronoi)
- Add: Colorize
- Connect Noise's output to Colorize's Input
- Change Colorize's gradient to something weird.
- Add: Palettize, with Size 16
- Add: Image, and load the square palette PNG
- Connect the Image's Output to the Palettize's Palette socket
- Connect Colorize's input to Palettize's Input
- Connect the Palettize's Output to the PBR's Albedo socket
- Export your texture as a Blender material to get a PNG

## Blender

++ tiling textures with TAU

# Palette

The Quake palette has 256 colors. The last 32 indices are "fullbright" and ignore all lighting. The final index is used for transparent/fence textures that are prefixed `{`.

- https://quakewiki.org/wiki/Quake_palette
- https://lospec.com/palette-list/quake

# Textures

Texture names have a character limit of 12 characters.

They must be at least 16 x 16 pixels tall and wide, and the resolution must be a multiple of 8 (16, 32, 64, 128, 256, 512)

Please keep your textures at most 512 pixels in size, and keep your skybox TGA resolution per-face at most 1024 pixels.

# Goals

You should aim to make AT LEAST the number of textures listed. So if it says to make 3 textures, make 3 or more (`>=3`).

## Dev and prototype textures

- trigger
- skip
- clip
- sky (256x128)
- \*waterskip
- \*lavaskip
- \*slimeskip
- region
- antiregion

## User-facing textures

- 1 atlas texture?
- 1 animated texture (button) `+0` `+1`
- 2 liquid textures `*`
  - exit teleport portal
  - water, slime, or lava
- 1 transparent texture `{`
- 7 regular textures (floors, walls, ceilings, whatever)
- Skybox: 6 TGA Files (6 faces)
  - suffixes: `[up, dn, lf, rt, ft, bk]`
