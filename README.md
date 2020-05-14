  
- Come up with a SICK repo name

- Retrieve history
  - Detect operating system
  - Detect default browser
  - Extract pages/titles/text (100 or custom)
  - Delete doubles + same-domain clusters
  - Parse url for search word

- Make Spotify playlist
  - Login with credentials
  - Search per search word
  - Add first song
  - Check for doubles
  
  
  
## Usage
Use `make` to train a number of standard models:
```bash
make disc             # train discriminative rnng
make gen              # train generative rnng
make crf              # train crf
make fully-unsup-crf  # train rnng + crf (vi) fully unsupervised
```
You can list all the options with:
```bash
make list
```

Alternatively, you can use command line arguments:
```bash
python src/main.py train --model-type=disc-rnng --model-path-base=models/disc-rnng
```
For all available options use:
```bash
python src/main.py --help
```

To set the environment variables used in evaluation of trained models, e.g. `CRF_PATH=models/crf_dev=90.01`, use:
```bash
source scripts/best-models.sh
```

## Models
Models are saved to folder `models` with their name and development scores. We have included our best models by development score as zip. To use them run `unzip zipped/file.zip` from the `models` directory.

## Acknowledgements
I have relied on some excellent implementations for inspiration and help with my own implementation:
* [pytorch-rnng](https://github.com/kmkurn/pytorch-rnng) inspired the representation of the [RNNG parser class](https://github.com/daandouwe/Thesis/blob/master/src/rnng/parser/parser.py)
* [minimal-span-parser](https://github.com/mitchellstern/minimal-span-parser) provided the foundations of the [tree classes](https://github.com/daandouwe/Thesis/blob/master/src/utils/trees.py), the [vocabulary class](https://github.com/daandouwe/Thesis/blob/master/src/utils/vocabulary.py) and of the [CRF parser](https://github.com/daandouwe/Thesis/blob/master/src/crf/model.py)
* [im2latex](https://github.com/guillaumegenthial/im2latex) inspired the use of a [makefile](https://github.com/daandouwe/Thesis/blob/master/makefile) to organize experiments

Make sure to check them out!