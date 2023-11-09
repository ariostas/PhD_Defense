# PhD Defense

This is the source code for the presentation I made for my PhD defense. I used [Manim](https://www.manim.community/) to make the animations, and I put them together into slides using [Manim Editor](https://docs.editor.manim.community/).

The final product of this code can be found at [this page](https://ariostas.github.io/PhD_Defense/).

This code was written in only a couple of weeks, so it is far from ideal and the quality is not representative of my work. It is also not very user-friendly, but I have included a rough guide for how to set everything up. This repository is mainly meant to be used as an example gallery for people who are starting to use Manim.

## Generating the slides

Manim has quite a few dependencies, so it is very convenient to work with the [Manim Docker image](https://hub.docker.com/r/manimcommunity/manim). I have made a makefile with a target to launch Jupyter Lab in a container from this image. Simply run the following command.

``` bash
make jupyter
```

Once in Jupyter Lab, you'll need to open a terminal and install Manim Editor.

``` bash
pip install manim-editor
```

At the time this was made there was some conflict between packages, so the latest version of Manim had to be reinstalled with `pip`. For this, and other inconveniences I have found using Manim Editor, I would suggest people who are starting a new project to look into [Manim Slides](https://eertmans.be/manim-slides/) or other alternatives to Manim Editor. However, some parts from the code will need to be adjusted to work with those alternatives.

Once Manim Editor is installed, you can compile the full set of scenes by running the following command in the Juputer Lab terminal. Keep in mind that some scenes take very long to render (up to a couple of hours).

``` bash
make render-all
```

Finally, to make the slides you run Manim Editor with `manedit`, add all the scenes in the right order, and let it process. I would suggest exporting the slides so that they can be displayed without any dependencies.
