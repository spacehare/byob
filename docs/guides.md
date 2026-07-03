# Textures

https://quakewiki.org/wiki/Textures

Texture names have a character limit of 16 characters.

They must be at least 16 x 16 pixels tall and wide, and the resolution must be a multiple of 8 (16, 32, 64, 128, 256, 512)

# Palette

The Quake palette has 256 colors. Indexes start at 0, so the first color is at index 0 and the last is at index 255. The last 32 indices are "fullbright" and will always be... fully bright. The final index (255) is used for transparent/fence textures that are prefixed with `{`.

- https://quakewiki.org/wiki/Quake_palette
- https://lospec.com/palette-list/quake

also take a look at this repo's [Palettes folder](../assets/palettes/). It has PNGs and KPL (Krita palette) files.

<!-- Please keep your textures at most 512 pixels in size, and keep your skybox TGA resolution per-face at most 1024 pixels. -->

# External Textures

External textures allow you to use colors outside of the Quake palette. They should have identical file names to the texture names in the WAD. (example: `{window` in the WAD should be `{window.tga` in the textures folder)

You want your textures in the mod folder like this: `id1/textures/byob_rabbit/`. A subfolder with your map's name will help if other mappers have a texture with the same name, to avoid overriding.

The external textures should be in TGA format for engine compatability.

The external file for a liquid texture should be prefixed with `#`, because on Windows you cannot have `*` in a file name. The external version of the texture should not use index 255 as the transparent color.

# Tools

make sure to read the manuals! RTFM!

| Hyperlink                                                                                 | Purpose                           |
| ----------------------------------------------------------------------------------------- | --------------------------------- |
| [Krita](https://krita.org)                                                                | Creating textures                 |
| [Material Maker](https://www.materialmaker.org/)                                          | Creating textures                 |
| [Blender](https://www.blender.org/)                                                       | Creating textures                 |
| [LibreSprite](https://github.com/LibreSprite/LibreSprite)                                 | Creating textures                 |
| [Wally 157](https://github.com/Ty-Matthews-VisualStudio/Wally/releases/tag/WallyDev)      | Creating textures, packing WADs   |
| [qpakman 062b](https://www.quaddicted.com/files/tools/qpakman-062b.zip) (direct download) | packing WADs                      |
| [ImageMagick](https://imagemagick.org/)                                                   | TGA conversion                    |
| [q1tools](https://q1tools.github.io/)                                                     | TGA conversion; many cool things! |
| [IrfanView](https://www.irfanview.com/)                                                   | TGA conversion                    |
| [ummjackson's tools](https://tools.ummjackson.com/)                                       | many cool things!                 |
| [img2pixel](https://captain4lk.itch.io/slk-img2pixel)                                     | downscaler and palettizer         |

other cool tools

- [Error Diffused Quake Palettte Colour Lookup Tables for use with Substance Designer/Painter](https://www.slipseer.com/index.php?resources/error-diffused-quake-palettte-colour-lookup-tables-for-used-with-substance-designer-painter.156/)

<!--
- https://github.com/LibreSprite/LibreSprite (Tei)
- https://captain4lk.itch.io/slk-img2pixel (Ashat Maself) (great username)
  - https://github.com/Captain4LK/SoftLK-tools
- https://www.slipseer.com/index.php?resources/error-diffused-quake-palettte-colour-lookup-tables-for-used-with-substance-designer-painter.156/
- https://www.youtube.com/watch?v=eyNAYiVn0nM Spyro sky panorama
-->

## prototype texture WADs

Here are some prototype texture WADs for reference. These include SKIP, TRIGGER, etc.

- https://github.com/lavenderdotpet/LibreQuake/releases
- https://www.slipseer.com/index.php?resources/prototype-wad.263/
- https://www.slipseer.com/index.php?resources/tool-textures.258/

# Example CLI tool usage

## qpakman

I recommend making a BAT file so you can quickly recompile changes to your textures

```shell
qpakman textures/*.png -o textures.wad
```

```shell
qpakman textures/* -o textures.wad
```

```shell
"I:\Quake\tools\qpakman-062b\qpakman.exe" textures/* -o textures.wad
```

## ImageMagick

```shell
magick mogrify -path example/folder -format tga -compress rle files/*.png
```

## IrfanView

```shell
"C:\Program Files (x86)\IrfanView\i_view32.exe" INPUTFOLDER\*.png /convert=OUTPUTFOLDER\*.tga
```

# Guides

## qpakman

My workflow is to have a folder full of PNG files with proper filenames

- suffix: `_fbr`, to allow fullbright colors to be used
- prefix: `star_` = `*` -- for liquids, because `*` is an invalid file name on Windows.
- prefix: `plus_` = `+` -- for animated textures
- prefix: `minu_` = `-`
- prefix: `divd_` = `/`
- prefix: `{` -- transparent textures

## Krita

- Create a new file
- For tiling textures, enable Wrap-Around mode (SHIFT+W)
- add a paint layer (ALT+L; N; P)
- Load the Quake palette `.kpl` in the Palette dock (ALT+N; D; Select "Palette")
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
- Export your texture
  - In the Preview2D window, click "export"
  - OR add an Export node, and use Quick Export (CTRL+SHIFT+E)

The default Palettize node does not have very much customizability... i recommend checking [the assets folder](../assets/ptex/) for some custom nodes by nick_w100

## Blender

You _can_ make tiling textures in Blender, but there will be some diagonal mirroring. It's good for also modelling out things like doors or windows (see jitspoe's video).

- [jitspoe tutorial](https://www.youtube.com/watch?v=b5taIvtQOXQ)
- [tiling textures with shader nodes](https://blender.stackexchange.com/questions/26692/how-do-i-create-repeating-patterns-with-cycles-procedural-textures)

I set "Filter Size" to `0.0` and "Raw" for Color Management. There is [an example BLEND file](../assets/example_blend.blend) in the assets folder.
