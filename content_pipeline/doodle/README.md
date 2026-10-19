# Chalk-doodle animation (free tools)

White hand-wobbled lines on a black board, a stick figure, handwritten labels, orange accents, chalk-scratch sound. Original artwork and script (a style, not anyone's video).

Files: `engine.py` (drawing + animation primitives), `example_homeschool_day.py` (the example), `fonts/` (open-licensed handwriting fonts).

Run on your computer:
```
pip install skia-python numpy
# ffmpeg must be installed (or set FFMPEG=/path/to/ffmpeg)
python3 example_homeschool_day.py out.mp4            # silent + chalk sound
pip install edge-tts
python3 example_homeschool_day.py out.mp4 --voice    # adds a voiceover; scene lengths follow the voice
```
On Linux, skia-python may need `libegl1`/`libgl1` installed.

How to make a new video: copy `example_homeschool_day.py`, change `SCENES` (narration + captions) and write one drawing function per scene using `b.write`, `b.circle`, `b.line`, `b.rect`, `b.arrow`, `b.figure`. Every element takes a progress value 0-1, so it draws itself on in time with the narration.

Tested here: silent render with chalk sound. Not tested here: the voiceover (the voice service is blocked in this environment) and playback on your devices. Check the voice service's terms before using it commercially.
