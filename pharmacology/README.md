# 115-1 Pharmacology

- Semester workspace: https://zi-yiii.github.io/pathology/115-1/
- Pharmacology: https://zi-yiii.github.io/pathology/pharmacology/115-1/
- Block 1: reserved.
- Block 2: autacoids, antibiotics, NSAIDs/gout, adrenal corticosteroids.
- Mechanisms and drug reference remain separate. Sources are in `115-1/2/notes/`.

## Update

Run the sync script against the reviewed local standalone HTML folder:

```sh
python3 scripts/sync-pharmacology.py --source <reviewed-html-folder>
```

Review the changes, commit, and push to `main`. This repository already publishes GitHub Pages from the root of `main`.

Individual learning pages support `?embed=1` to hide site navigation for embedding.

Semester and subject navigation share a consistent structure; pharmacology keeps its own minimal white UI. Micro remains organized by slide-exam number; pharmacology uses course Blocks.
