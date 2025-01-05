@echo off

set /p folderName=Enter the name for the folder:


mkdir %folderName%

mkdir %folderName%\scene\export\fbx
mkdir %folderName%\scene\export\obj
mkdir %folderName%\scene\export\usd
mkdir %folderName%\scene\renderOutput\image\blender
mkdir %folderName%\scene\renderOutput\image\photoshop
mkdir %folderName%\scene\renderOutput\imageSeq
mkdir %folderName%\scene\renderOutput\video
mkdir %folderName%\scene\reference
mkdir %folderName%\scene\textures\cgTextures
mkdir %folderName%\scene\textures\compTextures
mkdir %folderName%\scene\workfile\blender
mkdir %folderName%\scene\workfile\photoshop

mkdir %folderName%\final\export\fbx
mkdir %folderName%\final\export\obj
mkdir %folderName%\final\export\usd
mkdir %folderName%\final\renderOutput\image
mkdir %folderName%\final\renderOutput\imageSeq
mkdir %folderName%\final\renderOutput\video
mkdir %folderName%\final\workfile\blender
mkdir %folderName%\final\workfile\photoshop
