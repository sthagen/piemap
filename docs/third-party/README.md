# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/piemap/blob/default/sbom/cdx.json) with SHA256 checksum ([df24e5fc ...](https://git.sr.ht/~sthagen/piemap/blob/default/sbom/cdx.json.sha256 "sha256:df24e5fc645ddf3eb1db68b442b5d7d38e64159ed62e44920a849faba3156b2b")).
<!--[[[end]]] (checksum: e360010b25956615c8f66fa4e2f61e70)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                           | License                                            | Author                  | Description (from packaging data)                                  |
|:-------------------------------------------|:--------------------------------------------------|:---------------------------------------------------|:------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)        | [10.0.1](https://pypi.org/project/Pillow/10.0.1/) | Historical Permission Notice and Disclaimer (HPND) | Jeffrey A. Clark (Alex) | Python Imaging Library (Fork)                                      |
| [typer](https://github.com/tiangolo/typer) | [0.9.0](https://pypi.org/project/typer/0.9.0/)    | MIT License                                        | Sebastián Ramírez       | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 317d279725387385d5492c68c5a82674)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author  | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:--------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.6](https://pypi.org/project/click/8.1.6/) | BSD License | UNKNOWN | Composable command line interface toolkit |
<!--[[[end]]] (checksum: ec405dc73a3ccb02ae4ac4f6b5c7739e)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Pillow==10.0.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: cc4f3f71b405a2bdc0d351fc7b705440)-->
